#!/usr/bin/env python3
"""
Mirror surrealdb.com/blog as pure-markdown with local images and indexes.

Daily run (GH Actions):
    python mirror.py --all

Layout produced:
    <outdir>/
        README.md                 # stats + nav
        all.md                   # chronological list
        posts.json               # manifest
        atom.xml                 # Atom 1.0 feed
        assets/<hash>.<ext>      # cover + inline images
        years/<YYYY>.md          # per-year index
        categories/<slug>.md     # per-category index
        <YYYY>/<MM>/<slug>.md    # posts (YAML frontmatter + body)
"""

import argparse
import asyncio
import hashlib
import html
import json
import logging
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
import mimetypes

import aiohttp
from bs4 import BeautifulSoup
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception,
    wait_exponential_jitter,
)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

try:
    import mdformat

    HAS_MDFORMAT = True
except ImportError:
    HAS_MDFORMAT = False

BLOG_BASE = "https://surrealdb.com/blog/"
ASSETS_DIRNAME = "assets"
VIDEO_EXTS = {
    ext for ext, mime in mimetypes.types_map.items() if mime.startswith("video/")
}
USER_AGENT = "just a cute lil scraper (ꈍ ω ꈍ) github.com/n0kovo/surrealdb_blog_mirror"

CDN_BASE = "https://cdn.surrealdb.com/"


def is_retryable_exception(exc):
    if isinstance(exc, aiohttp.ClientResponseError):
        return exc.status == 429 or exc.status >= 500
    return isinstance(exc, (aiohttp.ClientConnectorError, asyncio.TimeoutError))


def slugify(text):
    text = (text or "").lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "untitled"


def yaml_str(s):
    """JSON-encode a string for safe YAML (JSON is a subset of YAML 1.2)."""
    return json.dumps(s, ensure_ascii=False)


def parse_publish_date(date_str):
    if not date_str:
        return None
    if date_str.startswith("!Date:"):
        date_str = date_str[len("!Date:") :]
    try:
        return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    except Exception:
        return None


def _digest(url):
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


def _normalize_url(url):
    """Strip over-escaped forward slashes from URLs.

    Some upstream JSON serializers double-encode `/` as `\\/`, which JSON-decodes
    to a literal backslash-slash sequence rather than a plain slash. Left alone,
    aiohttp percent-encodes the backslash to %5C and the request fails.
    """
    if not url:
        return url
    return url.replace("\\/", "/")


def _cdn_image_url(code):
    """Reconstruct the public CDN URL for a CDNImage block (`.auto` lets the CDN
    pick the format based on Accept headers)."""
    return f"{CDN_BASE}{code}.auto" if code else ""


def _cdn_video_url(code, fmt="mp4"):
    """Reconstruct the public CDN URL for a CDNVideo block."""
    return f"{CDN_BASE}{code}.{fmt}" if code else ""


def _code_fence(code):
    """Pick a backtick fence that won't collide with content inside the block."""
    longest = current = 0
    for c in code:
        if c == "`":
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return "`" * max(3, longest + 1)


_YT_RE = re.compile(r"(?:youtube\.com/(?:watch\?v=|embed/)|youtu\.be/)([A-Za-z0-9_-]+)")

_CALLOUT_THEMES = {
    "default": "NOTE",
    "info": "TIP",
    "success": "IMPORTANT",
    "warning": "WARNING",
    "error": "CAUTION",
}


def asset_filename(url, content_type=None):
    ext = None
    if content_type:
        ct = content_type.split(";")[0].strip().lower()
        ext = mimetypes.guess_extension(ct, strict=False)
    if not ext:
        path = urlparse(url).path
        url_ext = Path(path).suffix
        if url_ext and len(url_ext) <= 6 and url_ext.lower() != ".auto":
            ext = url_ext.lower()
    return f"{_digest(url)}{ext or '.bin'}"


def transform_link(url, slug_map):
    if not url or not url.startswith(BLOG_BASE):
        return url
    slug = url.replace(BLOG_BASE, "").strip("/")
    if slug in slug_map:
        return f"../../{slug_map[slug]}/{slug}.md"
    return url


def serialize_text_nodes(nodes, slug_map=None):
    out = []
    for node in nodes:
        if "text" in node:
            text = html.unescape(node["text"])
            if node.get("code"):
                text = f"`{text}`"
            if node.get("bold"):
                text = f"**{text}**"
            if node.get("italic"):
                text = f"*{text}*"
            if node.get("strike"):
                text = f"~~{text}~~"
            if node.get("underline"):
                text = f"<u>{text}</u>"
            out.append(text)
        elif "type" in node:
            t = node["type"]
            if t in ("link", "surreal-link"):
                url = _normalize_url(node.get("props", {}).get("url", ""))
                if slug_map:
                    url = transform_link(url, slug_map)
                inner = serialize_text_nodes(node.get("children", []), slug_map)
                out.append(f"[{inner}]({url})")
            elif "children" in node:
                out.append(serialize_text_nodes(node["children"], slug_map))
        elif "children" in node:
            out.append(serialize_text_nodes(node["children"], slug_map))
    return "".join(out)


def extract_asset_urls_from_yoopta(payload):
    """All downloadable media URLs in a Yoopta payload — covers stock `Image`
    blocks plus SurrealDB-specific `CDNImage` and `CDNVideo` blocks."""
    data = json.loads(payload) if isinstance(payload, str) else payload
    urls = []
    for block in data.get("blocks", []):
        btype = block.get("type")
        for v in block.get("value", []) or []:
            props = v.get("props") or {}
            if btype == "Image":
                src = props.get("src")
                if src:
                    urls.append(_normalize_url(src))
            elif btype == "CDNImage":
                code = props.get("code")
                if code:
                    urls.append(_cdn_image_url(code))
            elif btype == "CDNVideo":
                code = props.get("code")
                fmt = props.get("format") or "mp4"
                if code:
                    urls.append(_cdn_video_url(code, fmt))
    return urls


def convert_yoopta_to_markdown(payload, slug_map=None, asset_map=None, asset_prefix=""):
    data = json.loads(payload) if isinstance(payload, str) else payload
    asset_map = asset_map or {}
    blocks = data.get("blocks", [])
    blocks.sort(key=lambda x: x.get("meta", {}).get("order", 0))

    md_blocks = []
    for block in blocks:
        b_type = block.get("type")
        value = block.get("value", [])
        if not value:
            continue
        meta = block.get("meta", {})
        indent = "  " * meta.get("depth", 0)
        root = value[0]
        children = root.get("children", [])
        props = root.get("props", {}) or {}

        def text():
            return serialize_text_nodes(children, slug_map)

        if b_type == "Paragraph":
            md_blocks.append(f"{indent}{text()}")
        elif b_type == "HeadingOne":
            md_blocks.append(f"{indent}# {text()}")
        elif b_type == "HeadingTwo":
            md_blocks.append(f"{indent}## {text()}")
        elif b_type == "HeadingThree":
            md_blocks.append(f"{indent}### {text()}")
        elif b_type == "Blockquote":
            md_blocks.append(f"{indent}> {text()}")
        elif b_type == "Divider":
            md_blocks.append(f"{indent}---")
        elif b_type == "BulletedList":
            md_blocks.append(f"{indent}- {text()}")
        elif b_type == "NumberedList":
            md_blocks.append(f"{indent}1. {text()}")
        elif b_type == "TodoList":
            mark = "x" if props.get("checked") else " "
            md_blocks.append(f"{indent}- [{mark}] {text()}")
        elif b_type == "SurrealCodeBlock":
            code = props.get("code") or ""
            language = props.get("language") or ""
            # "syntax" is a SurrealDB pseudo-language for byte-format diagrams;
            # leave it as the fence info string — renderers will just skip
            # highlighting rather than choke.
            fence = _code_fence(code)
            md_blocks.append(f"{indent}{fence}{language}\n{code}\n{indent}{fence}")
        elif b_type == "Image":
            src = _normalize_url(props.get("src", "") or "")
            alt = props.get("alt", "") or ""
            if src in asset_map:
                src = f"{asset_prefix}{asset_map[src]}"
            md_blocks.append(f"{indent}![{alt}]({src})")
        elif b_type == "CDNImage":
            code = props.get("code") or ""
            alt = props.get("alt", "") or ""
            src = _cdn_image_url(code)
            if src in asset_map:
                src = f"{asset_prefix}{asset_map[src]}"
            md_blocks.append(f"{indent}![{alt}]({src})")
        elif b_type == "CDNVideo":
            code = props.get("code") or ""
            fmt = props.get("format") or "mp4"
            src = _cdn_video_url(code, fmt)
            if src in asset_map:
                src = f"{asset_prefix}{asset_map[src]}"
            md_blocks.append(f"{indent}![]({src})")
        elif b_type == "VideoEmbed":
            url = _normalize_url(props.get("url", "") or "")
            m = _YT_RE.search(url) if url else None
            if m:
                md_blocks.append(
                    f"{indent}[YouTube: {m.group(1)}](https://www.youtube.com/watch?v={m.group(1)})"
                )
            elif url:
                md_blocks.append(f"{indent}[{url}]({url})")
        elif b_type == "MantineButton":
            url = _normalize_url(props.get("url") or "")
            label = props.get("label") or text() or url
            md_blocks.append(f"{indent}[{label}]({url})" if url else f"{indent}{label}")
        elif b_type == "Callout":
            kind = _CALLOUT_THEMES.get(props.get("theme") or "default", "NOTE")
            title = (props.get("title") or "").strip()
            header = f"[!{kind}]" + (f" {title}" if title else "")
            body = text()
            lines = [f"{indent}> {header}"]
            for line in body.split("\n"):
                lines.append(f"{indent}> {line}")
            md_blocks.append("\n".join(lines))
        elif b_type == "MantineTable":
            rows = props.get("rows", [])
            with_header = props.get("withHeaderRow", False)
            table = []
            for i, row in enumerate(rows):
                escaped = [
                    html.unescape(str(c)).replace("|", "\\|").replace("\n", " ")
                    for c in row
                ]
                table.append(f"{indent}| " + " | ".join(escaped) + " |")
                if i == 0 and with_header:
                    table.append(f"{indent}|" + "|".join("---" for _ in row) + "|")
            md_blocks.append("\n".join(table))
        else:
            md_blocks.append(f"{indent}{text()}")

    final = ""
    for i, md in enumerate(md_blocks):
        if i > 0:
            prev = blocks[i - 1].get("type")
            curr = blocks[i].get("type")
            sep = (
                "\n"
                if prev in ("BulletedList", "NumberedList", "TodoList") and curr == prev
                else "\n\n"
            )
            final += sep + md
        else:
            final += md
    return final


@retry(
    retry=retry_if_exception(is_retryable_exception),
    wait=wait_exponential_jitter(exp_base=2, max=300),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)
async def fetch_vike_data(session, url):
    async with session.get(url, headers={"User-Agent": USER_AGENT}, timeout=30) as resp:
        resp.raise_for_status()
        text = await resp.text()
    soup = BeautifulSoup(text, "html.parser")
    script = soup.find("script", {"id": "vike_pageContext", "type": "application/json"})
    if not script:
        raise ValueError(f"Could not find vike_pageContext at {url}")
    return json.loads(script.text)


@retry(
    retry=retry_if_exception(is_retryable_exception),
    wait=wait_exponential_jitter(exp_base=2, max=300),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)
async def _fetch_asset_bytes(session, url):
    headers = {"User-Agent": USER_AGENT, "Accept": "image/*,*/*"}
    async with session.get(url, headers=headers, timeout=60) as resp:
        resp.raise_for_status()
        return await resp.read(), resp.headers.get("Content-Type", "")


def _downscale_video(path, max_height=1080, max_bytes=90 * 1024 * 1024):
    """Re-encode in place if video exceeds max_height OR max_bytes.

    Idempotent: a file already at/below both thresholds is left alone.
    Needs ffmpeg + ffprobe on PATH; no-op if missing."""
    path = Path(path)
    if not (shutil.which("ffmpeg") and shutil.which("ffprobe")):
        return
    try:
        out = (
            subprocess.check_output(
                [
                    "ffprobe",
                    "-v",
                    "error",
                    "-select_streams",
                    "v:0",
                    "-show_entries",
                    "stream=height",
                    "-of",
                    "csv=p=0",
                    str(path),
                ],
                text=True,
                stderr=subprocess.DEVNULL,
            )
            .strip()
            .splitlines()
        )
        height = int(out[0]) if out else 0
    except (subprocess.CalledProcessError, ValueError, FileNotFoundError):
        return

    size = path.stat().st_size
    if height and height <= max_height and size <= max_bytes:
        return

    tmp = path.with_suffix(path.suffix + ".reenc.mp4")
    vf = f"scale=-2:'min({max_height},ih)'"
    try:
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-loglevel",
                "error",
                "-i",
                str(path),
                "-vf",
                vf,
                "-c:v",
                "libx264",
                "-preset",
                "medium",
                "-crf",
                "23",
                "-c:a",
                "aac",
                "-b:a",
                "128k",
                "-movflags",
                "+faststart",
                str(tmp),
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        logger.warning(f"ffmpeg failed for {path}: {e}")
        if tmp.exists():
            tmp.unlink()
        return

    new_size = tmp.stat().st_size
    if new_size >= size:
        # re-encode bigger than original: keep original
        tmp.unlink()
        logger.info(f"Skipped downscale (re-encode larger) for {path}")
        return
    tmp.replace(path)
    logger.info(
        f"Downscaled {path.name}: "
        f"{height}p {size // 1024 // 1024}MB → ≤{max_height}p {new_size // 1024 // 1024}MB"
    )


class AssetStore:
    """Hash-based asset cache. URL hash → filename. Survives across runs.

    Files on disk are named `<sha1(url)[:16]>.<ext>` so we can match an
    existing file purely from a URL we haven't downloaded yet."""

    def __init__(self, assets_dir, semaphore, max_video_height=1080):
        self.assets_dir = Path(assets_dir)
        self.semaphore = semaphore
        self.max_video_height = max_video_height
        self.url_cache = {}  # url -> filename
        self.inflight = {}  # url -> Task
        self._by_digest = {}  # digest -> filename (from existing files)

        self.assets_dir.mkdir(parents=True, exist_ok=True)
        for entry in self.assets_dir.iterdir():
            if "." in entry.name:
                self._by_digest[entry.name.split(".", 1)[0]] = entry.name
        self._sweep_videos()

    def _sweep_videos(self):
        """Downscale any pre-existing oversize videos so git doesn't choke."""
        if not (shutil.which("ffmpeg") and shutil.which("ffprobe")):
            return
        for entry in self.assets_dir.iterdir():
            ext = entry.suffix.lower()
            if ext in VIDEO_EXTS:
                _downscale_video(entry, max_height=self.max_video_height)

    async def fetch(self, session, url):
        if url in self.url_cache:
            return self.url_cache[url]
        d = _digest(url)
        if d in self._by_digest:
            self.url_cache[url] = self._by_digest[d]
            return self._by_digest[d]
        if url in self.inflight:
            return await self.inflight[url]
        task = asyncio.create_task(self._do_fetch(session, url, d))
        self.inflight[url] = task
        try:
            return await task
        finally:
            self.inflight.pop(url, None)

    async def _do_fetch(self, session, url, digest):
        async with self.semaphore:
            try:
                data, ct = await _fetch_asset_bytes(session, url)
            except Exception as e:
                logger.warning(f"Asset download failed {url}: {e}")
                return None
        filename = asset_filename(url, ct)
        outpath = self.assets_dir / filename
        tmp = outpath.with_suffix(outpath.suffix + ".tmp")

        tmp.write_bytes(data)
        tmp.replace(outpath)

        if outpath.suffix.lower() in VIDEO_EXTS:
            _downscale_video(outpath, max_height=self.max_video_height)

        self.url_cache[url] = filename
        self._by_digest[digest] = filename
        return filename


def build_frontmatter(post, cover_filename, asset_prefix):
    lines = ["---"]
    lines.append(f"title: {yaml_str(post.get('title') or '')}")
    lines.append(f"slug: {yaml_str(post['slug'])}")
    raw_date = post.get("publishDate", "") or ""
    if raw_date.startswith("!Date:"):
        raw_date = raw_date[len("!Date:") :]
    if raw_date:
        lines.append(f"date: {yaml_str(raw_date)}")
    cats = post.get("categories") or []
    if cats:
        lines.append("categories:")
        for c in cats:
            lines.append(f"  - {yaml_str(c)}")
    rt = post.get("readTime")
    if rt:
        lines.append(f"read_time: {yaml_str(rt)}")
    summary = post.get("summary")
    if summary:
        lines.append(f"summary: {yaml_str(summary)}")
    lines.append(f"source: {yaml_str(BLOG_BASE + post['slug'])}")
    if cover_filename:
        lines.append(f"cover: {yaml_str(asset_prefix + cover_filename)}")
    lines.append("---")
    return "\n".join(lines)


async def download_post(
    session,
    post,
    outdir,
    post_sem,
    asset_store,
    slug_map,
    refresh=False,
    format_md=True,
    download_images=True,
):
    slug = post.get("slug")
    pub_date = parse_publish_date(post.get("publishDate"))
    if not slug or not pub_date:
        return False

    outdir = Path(outdir)
    year, month = str(pub_date.year), f"{pub_date.month:02d}"
    outfile = outdir / year / month / f"{slug}.md"
    if outfile.exists() and not refresh:
        return False

    post_url = f"{BLOG_BASE}{slug}"
    asset_prefix = f"../../{ASSETS_DIRNAME}/"

    async with post_sem:
        try:
            page_ctx = await fetch_vike_data(session, post_url)
        except Exception as e:
            logger.error(f"✗ Fetch failed {post_url}: {e}")
            return False

    try:
        yoopta_html = page_ctx["data"]["post"]["html"]
        body = BeautifulSoup(yoopta_html, "html.parser").find("body")
        if not body:
            logger.warning(f"✗ Malformed body at {post_url}")
            return False
        yoopta_data = body.get("data-yoopta-json")
    except Exception as e:
        logger.error(f"✗ Parse failed {post_url}: {e}")
        return False

    # download images (cover + inline)
    asset_map = {}
    cover_filename = None
    if download_images:
        urls = set(extract_asset_urls_from_yoopta(yoopta_data))
        cover_url = post.get("imageUrl")
        if cover_url:
            urls.add(cover_url)
        if urls:
            results = await asyncio.gather(
                *(asset_store.fetch(session, u) for u in urls),
                return_exceptions=False,
            )
            for u, fn in zip(urls, results):
                if fn:
                    asset_map[u] = fn
            if cover_url:
                cover_filename = asset_map.get(cover_url)

    # convert body
    body_md = convert_yoopta_to_markdown(
        yoopta_data,
        slug_map=slug_map,
        asset_map=asset_map,
        asset_prefix=asset_prefix,
    )
    if format_md and HAS_MDFORMAT:
        try:
            body_md = mdformat.text(body_md)
        except Exception as e:
            logger.warning(f"mdformat failed for {slug}: {e}")

    title = (post.get("title") or "").strip()
    starts_with_h1 = bool(re.match(r"^\s*#\s+\S", body_md))

    parts = [build_frontmatter(post, cover_filename, asset_prefix), ""]
    if title and not starts_with_h1:
        parts += [f"# {title}", ""]
    if cover_filename:
        alt = title.replace("]", "")
        parts += [f"![{alt}]({asset_prefix}{cover_filename})", ""]
    parts.append(body_md)

    outfile.parent.mkdir(parents=True, exist_ok=True)
    outfile.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")

    logger.info(f"✓ Saved {outfile}")
    return True


def _post_entry(p, slug_to_date_path, path_prefix):
    slug = p["slug"]
    title = p.get("title") or slug
    date = parse_publish_date(p.get("publishDate"))
    date_str = date.strftime("%Y-%m-%d") if date else "----------"
    date_path = slug_to_date_path.get(slug, "unknown/unknown")
    link = f"{path_prefix}{date_path}/{slug}.md"
    cats = p.get("categories") or []
    cat_str = " ".join(f"`{c}`" for c in cats)
    summary = (p.get("summary") or "").strip().replace("\n", " ")
    line = f"- **{date_str}** · [{title}]({link})"
    extras = [s for s in (cat_str, summary) if s]
    if extras:
        line += "  \n  " + " — ".join(extras)
    return line


def write_indexes(outdir, posts, slug_to_date_path):
    outdir = Path(outdir)
    if not posts:
        return

    def key(p):
        d = parse_publish_date(p.get("publishDate"))
        return d or datetime.min.replace(tzinfo=timezone.utc)

    posts_sorted = sorted(posts, key=key, reverse=True)

    by_year = defaultdict(list)
    by_category = defaultdict(list)
    for p in posts_sorted:
        d = parse_publish_date(p.get("publishDate"))
        if d:
            by_year[d.year].append(p)
        for c in p.get("categories") or []:
            by_category[c].append(p)

    dates = [
        d for d in (parse_publish_date(p.get("publishDate")) for p in posts_sorted) if d
    ]
    earliest, latest = (min(dates), max(dates)) if dates else (None, None)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # main index — written to outdir.parent so its links need the outdir name
    # as a prefix to reach files that actually live inside outdir.
    readme_prefix = f"{outdir.name}/" if str(outdir) not in (".", "") else ""

    out = ["# SurrealDB Blog Mirror\n", f"_Last updated: {now}_\n", "## Stats\n"]
    out.append(f"- **Total posts:** {len(posts_sorted)}")
    if earliest and latest:
        out.append(f"- **First post:** {earliest.strftime('%Y-%m-%d')}")
        out.append(f"- **Latest post:** {latest.strftime('%Y-%m-%d')}")
    out.append(f"- **Years covered:** {len(by_year)}")
    out.append(f"- **Categories:** {len(by_category)}\n")

    out.append("## Browse\n")
    out.append(f"- [All posts (chronological)]({readme_prefix}all.md)")
    out.append(f"- [Manifest (`posts.json`)]({readme_prefix}posts.json)")
    out.append(f"- [Atom feed (`atom.xml`)]({readme_prefix}atom.xml)")
    docs_readme = outdir.parent / "docs" / "README.md"
    if docs_readme.exists():
        out.append("- [SurrealDB Documentation (Markdown mirror)](docs/README.md)")
    out.append("")

    out.append("### By year\n")
    for y in sorted(by_year, reverse=True):
        out.append(f"- [{y}]({readme_prefix}years/{y}.md) — {len(by_year[y])} posts")
    out.append("")

    out.append("### By category\n")
    for c in sorted(by_category):
        out.append(
            f"- [{c}]({readme_prefix}categories/{slugify(c)}.md) — {len(by_category[c])} posts"
        )
    out.append("")

    out.append("## Latest posts\n")
    for p in posts_sorted[:10]:
        out.append(_post_entry(p, slug_to_date_path, readme_prefix))

    (outdir.parent / "README.md").write_text(
        "\n".join(out).rstrip() + "\n", encoding="utf-8"
    )

    # all.md — inside outdir, so back-link climbs one level
    out = ["# All Posts\n", f"_{len(posts_sorted)} posts_  \n[← Index](../README.md)\n"]
    for p in posts_sorted:
        out.append(_post_entry(p, slug_to_date_path, ""))
    (outdir / "all.md").write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")

    #  years/
    years_dir = outdir / "years"
    years_dir.mkdir(parents=True, exist_ok=True)
    for y, items in by_year.items():
        out = [
            f"# Posts from {y}\n",
            f"_{len(items)} posts_  \n[← Index](../../README.md)\n",
        ]
        for p in items:
            out.append(_post_entry(p, slug_to_date_path, "../"))
        (years_dir / f"{y}.md").write_text(
            "\n".join(out).rstrip() + "\n", encoding="utf-8"
        )

    #  categories/
    cats_dir = outdir / "categories"
    cats_dir.mkdir(parents=True, exist_ok=True)
    for c, items in by_category.items():
        items = sorted(items, key=key, reverse=True)
        out = [
            f"# Category: {c}\n",
            f"_{len(items)} posts_  \n[← Index](../../README.md)\n",
        ]
        for p in items:
            out.append(_post_entry(p, slug_to_date_path, "../"))
        path = cats_dir / f"{slugify(c)}.md"
        path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def write_manifest(outdir, posts, slug_to_date_path):
    outdir = Path(outdir)

    def norm_date(raw):
        if raw and raw.startswith("!Date:"):
            return raw[len("!Date:") :]
        return raw

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(posts),
        "posts": [
            {
                "slug": p["slug"],
                "title": p.get("title"),
                "summary": p.get("summary"),
                "publishDate": norm_date(p.get("publishDate")),
                "categories": p.get("categories") or [],
                "readTime": p.get("readTime"),
                "imageUrl": p.get("imageUrl"),
                "source": BLOG_BASE + p["slug"],
                "local_path": (
                    f"{slug_to_date_path[p['slug']]}/{p['slug']}.md"
                    if p["slug"] in slug_to_date_path
                    else None
                ),
            }
            for p in posts
        ],
    }
    with (outdir / "posts.json").open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)


ATOM_NS = "http://www.w3.org/2005/Atom"


def write_atom_feed(outdir, posts, feed_self_url=None, limit=50):
    """Write atom.xml — Atom 1.0 feed of the most recent posts.

    Entry IDs use the canonical surrealdb.com URL so feed readers correctly
    dedupe against the original site if a user happens to subscribe to both.
    """
    outdir = Path(outdir)

    def key(p):
        d = parse_publish_date(p.get("publishDate"))
        return d or datetime.min.replace(tzinfo=timezone.utc)

    posts_sorted = sorted(posts, key=key, reverse=True)
    if limit:
        posts_sorted = posts_sorted[:limit]

    ET.register_namespace("", ATOM_NS)
    feed = ET.Element(f"{{{ATOM_NS}}}feed")

    def el(parent, tag, text=None, **attrs):
        e = ET.SubElement(parent, f"{{{ATOM_NS}}}{tag}", attrs)
        if text is not None:
            e.text = text
        return e

    el(feed, "title", "SurrealDB Blog (mirror)")
    el(feed, "subtitle", "Daily mirror of surrealdb.com/blog")
    el(feed, "id", BLOG_BASE)
    el(feed, "link", rel="alternate", href=BLOG_BASE, type="text/html")
    if feed_self_url:
        el(feed, "link", rel="self", href=feed_self_url, type="application/atom+xml")

    now = datetime.now(timezone.utc)
    latest = None
    for p in posts_sorted:
        d = parse_publish_date(p.get("publishDate"))
        if d:
            latest = d
            break
    el(
        feed,
        "updated",
        (latest or now).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    )

    author = ET.SubElement(feed, f"{{{ATOM_NS}}}author")
    el(author, "name", "SurrealDB")

    for p in posts_sorted:
        slug = p["slug"]
        url = BLOG_BASE + slug
        d = parse_publish_date(p.get("publishDate")) or now
        d_utc = d.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        entry = ET.SubElement(feed, f"{{{ATOM_NS}}}entry")
        el(entry, "id", url)
        el(entry, "title", p.get("title") or slug)
        el(entry, "link", rel="alternate", href=url, type="text/html")
        el(entry, "published", d_utc)
        el(entry, "updated", d_utc)
        summary = (p.get("summary") or "").strip()
        if summary:
            s = el(entry, "summary", summary)
            s.set("type", "text")
        for c in p.get("categories") or []:
            el(entry, "category", term=c)

    tree = ET.ElementTree(feed)
    ET.indent(tree, space="  ")
    tree.write(
        outdir / "atom.xml",
        encoding="utf-8",
        xml_declaration=True,
    )


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_url", nargs="?", default=BLOG_BASE.rstrip("/"))
    parser.add_argument("-o", "--output", help="Output file (single-URL mode)")
    parser.add_argument("--all", action="store_true", help="Mirror all blog posts")
    parser.add_argument("--outdir", default="posts")
    parser.add_argument("--concurrency", type=int, default=5)
    parser.add_argument("--image-concurrency", type=int, default=10)
    parser.add_argument(
        "--refresh", action="store_true", help="Re-download existing posts"
    )
    parser.add_argument("--no-images", action="store_true", help="Skip image downloads")
    parser.add_argument("--no-format", action="store_true", help="Skip mdformat pass")
    parser.add_argument(
        "--feed-url",
        help="Public URL where atom.xml will be served (used as the feed's self link)",
    )
    parser.add_argument(
        "--feed-limit",
        type=int,
        default=50,
        help="Max entries in atom.xml (default: 50)",
    )
    parser.add_argument(
        "--max-video-height",
        type=int,
        default=1080,
        help="Downscale videos taller than this with ffmpeg (default: 1080)",
    )
    args = parser.parse_args()

    post_sem = asyncio.Semaphore(args.concurrency)
    img_sem = asyncio.Semaphore(args.image_concurrency)
    connector = aiohttp.TCPConnector(limit=20)

    outdir = Path(args.outdir)

    async with aiohttp.ClientSession(connector=connector) as session:
        if args.all:
            outdir.mkdir(parents=True, exist_ok=True)
            asset_store = AssetStore(
                outdir / ASSETS_DIRNAME,
                img_sem,
                max_video_height=args.max_video_height,
            )

            logger.info("Fetching blog index...")
            try:
                vike = await fetch_vike_data(session, BLOG_BASE.rstrip("/"))
            except Exception as e:
                logger.error(f"Fatal: could not fetch blog index: {e}")
                return

            posts = [
                p for p in vike["data"]["allPostsCombined"] if not p.get("isPress")
            ]
            for p in posts:
                if p.get("imageUrl"):
                    p["imageUrl"] = _normalize_url(p["imageUrl"])

            slug_to_date_path = {}
            for p in posts:
                slug = p.get("slug")
                d = parse_publish_date(p.get("publishDate"))
                if slug and d:
                    slug_to_date_path[slug] = f"{d.year}/{d.month:02d}"

            tasks = [
                download_post(
                    session,
                    p,
                    outdir,
                    post_sem,
                    asset_store,
                    slug_to_date_path,
                    refresh=args.refresh,
                    format_md=not args.no_format,
                    download_images=not args.no_images,
                )
                for p in posts
                if p.get("slug") in slug_to_date_path
            ]
            logger.info(f"Processing {len(tasks)} posts...")
            results = await asyncio.gather(*tasks, return_exceptions=True)
            new_count = sum(1 for r in results if r is True)
            logger.info(f"Downloaded {new_count} new post(s).")

            # Indexes + manifest always rebuilt from current allPostsCombined
            logger.info("Writing indexes, manifest, and feed...")
            write_indexes(outdir, posts, slug_to_date_path)
            write_manifest(outdir, posts, slug_to_date_path)
            write_atom_feed(
                outdir,
                posts,
                feed_self_url=args.feed_url,
                limit=args.feed_limit,
            )
            logger.info(f"Done. Output: {outdir}")
        else:
            # Minimal single-URL mode
            url = args.input_url
            slug = urlparse(url).path.rstrip("/").split("/")[-1] or "post"
            outfile = Path(args.output) if args.output else Path(f"{slug}.md")
            try:
                page_ctx = await fetch_vike_data(session, url)
                yoopta_html = page_ctx["data"]["post"]["html"]
                body = BeautifulSoup(yoopta_html, "html.parser").find("body")
                if not body:
                    logger.error("Malformed page data")
                    return
                md = convert_yoopta_to_markdown(body.get("data-yoopta-json"))
                if not args.no_format and HAS_MDFORMAT:
                    md = mdformat.text(md)
                outfile.parent.mkdir(parents=True, exist_ok=True)
                outfile.write_text(md, encoding="utf-8")
                logger.info(f"Saved {outfile}")
            except Exception as e:
                logger.error(f"Failed: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
