#!/usr/bin/env python
"""Mirror surrealdb/docs.surrealdb.com MDX content as pure markdown.

Pulls the main branch tarball, walks src/content/**/*.mdx, transforms each
into clean GitHub-flavored markdown, downloads referenced image assets,
rewrites internal /docs/... links to local files, and writes an index.

Output layout:
    docs/
      README.md
      all.md
      assets/img/...
      <category>/.../<page>.md
"""

from __future__ import annotations

import argparse
import io
import json
import re
import shutil
import sys
import tarfile
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import railroad  # vendored copy

TARBALL_URL = (
    "https://github.com/surrealdb/docs.surrealdb.com/archive/refs/heads/main.tar.gz"
)
HEADER_TSX_URL = (
    "https://raw.githubusercontent.com/surrealdb/docs.surrealdb.com/main/"
    "src/components/Layout/header.tsx"
)
SITE = "https://surrealdb.com"
DOCS_BASE = "/docs"


def download_repo(dest: Path) -> Path:
    """Fetch docs repo tarball, extract src/content + src/assets to dest."""
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    print(f"downloading {TARBALL_URL}", flush=True)
    with urllib.request.urlopen(TARBALL_URL) as r:
        buf = io.BytesIO(r.read())
    with tarfile.open(fileobj=buf, mode="r:gz") as tar:
        keep_prefixes = ("/src/content/", "/src/assets/img/")
        members = []
        for m in tar.getmembers():
            # strip leading "repo-main"
            parts = m.name.split("/", 1)
            if len(parts) < 2:
                continue
            rel = "/" + parts[1]
            if any(rel.startswith(p) for p in keep_prefixes):
                m.name = parts[1]  # strip top dir
                members.append(m)
        tar.extractall(dest, members=members, filter="data")
    return dest


FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm: dict = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        v = v.strip()
        if (v.startswith('"') and v.endswith('"')) or (
            v.startswith("'") and v.endswith("'")
        ):
            v = v[1:-1]
        fm[k.strip()] = v
    return fm, text[m.end() :]


def emit_frontmatter(fm: dict) -> str:
    if not fm:
        return ""
    lines = ["---"]
    for k, v in fm.items():
        s = str(v)
        if any(c in s for c in ":#\"'") or s != s.strip():
            s = '"' + s.replace('"', '\\"') + '"'
        lines.append(f"{k}: {s}")
    lines.append("---\n")
    return "\n".join(lines)


_ATTR_RE = re.compile(r'\s*([A-Za-z_][\w:-]*)(?:\s*=\s*("[^"]*"|\'[^\']*\'|\{))?')


def parse_jsx_attrs(s: str) -> dict[str, str]:
    """Parse JSX-like attributes: foo="bar" baz={expr} qux.

    Bare attributes (no `=`) resolve to "" rather than JSX's `true` semantics,
    since no component we handle relies on boolean prop presence.
    """
    out: dict[str, str] = {}
    pos = 0
    while True:
        m = _ATTR_RE.match(s, pos)
        if not m or m.group(1) is None:
            break
        name, val = m.group(1), m.group(2)
        if val is None:
            out[name] = ""
            pos = m.end()
        elif val[0] in ('"', "'"):
            out[name] = val[1:-1]
            pos = m.end()
        else:  # '{' — scan for the matching close, respecting string literals
            start, j, depth = m.end() - 1, m.end(), 1
            while j < len(s) and depth:
                c = s[j]
                if c in ('"', "'"):
                    j += 1
                    while j < len(s) and s[j] != c:
                        j += 2 if s[j] == "\\" else 1
                    j += 1
                elif c == "{":
                    depth += 1
                    j += 1
                elif c == "}":
                    depth -= 1
                    j += 1
                else:
                    j += 1
            if depth:
                raise ValueError(f"unterminated {{...}} in attribute {name!r}")
            out[name] = s[start:j]
            pos = j
    return out


# ---- single-tag void components ----


def sub_since(text: str) -> str:
    return re.sub(r"<Since\s+([^/>]*?)/>", _since_repl, text)


def _since_repl(m):
    attrs = parse_jsx_attrs(m.group(1))
    v = attrs.get("v", "")
    return f"*Since {v}*" if v else "*Since latest*"


def sub_label(text: str) -> str:
    def repl(m):
        attrs = parse_jsx_attrs(m.group(1))
        return f"*[{attrs.get('label', '')}]*"

    return re.sub(r"<Label\s+([^/>]*?)/>", repl, text)


def sub_version(text: str) -> str:
    # <Version sdk="rust" />, <Version />, <Version prefix="v" sdk="php" />
    return re.sub(r"<Version\s*([^/>]*?)/>", "*(latest)*", text)


def sub_icon(text: str) -> str:
    return re.sub(r"<Icon\s+([^/>]*?)/>", "", text)


def sub_iconbox(text: str) -> str:
    # multi-line; attrs span newlines. Strip leading whitespace on the line.
    pattern = re.compile(r"^[ \t]*<IconBox\s+(.*?)/>[ \t]*$", re.S | re.M)

    def repl(m):
        attrs = parse_jsx_attrs(m.group(1))
        title = attrs.get("title", "")
        desc = attrs.get("description", "").strip()
        href = attrs.get("href", "")
        head = f"**[{title}]({href})**" if href else f"**{title}**"
        return f"- {head} — {desc}" if desc else f"- {head}"

    return pattern.sub(repl, text)


def strip_tag(text: str, tag: str) -> str:
    # strip both <Tag ...> and </Tag>, single-line attrs
    text = re.sub(rf"<{tag}\b[^>]*>", "", text)
    text = re.sub(rf"</{tag}>", "", text)
    return text


def sub_surrealist_mini(text: str) -> str:
    pattern = re.compile(r"<SurrealistMini\s+(.*?)/>", re.S)

    def repl(m):
        attrs = parse_jsx_attrs(m.group(1))
        url = attrs.get("url", "")
        query = attrs.get("query", "")
        if url:
            return f"\n[▶ Open in Surrealist]({url})\n"
        if query:
            q = urllib.parse.quote(query)
            return (
                f"\n[▶ Open in Surrealist](https://app.surrealdb.com/mini?query={q})\n"
            )
        return ""

    # also handle <SurrealistMini ...>...</SurrealistMini> (with body)
    text = pattern.sub(repl, text)
    text = re.sub(r"<SurrealistMini\b[^>]*>.*?</SurrealistMini>", "", text, flags=re.S)
    return text


# ---- tabs ----


def sub_tabs(text: str) -> str:
    """Flatten <Tabs><TabItem label="X">...</TabItem></Tabs>. Handles nesting."""
    # Strip <Tabs ...> and </Tabs> wrappers (and common typos like </abs>).
    text = re.sub(r"</?Tabs\b[^>]*>", "", text)
    text = re.sub(r"</?[Tt][Aa][Bb][Ss]\b[^>]*>", "", text)
    # Walk TabItem tags with a balanced-depth scanner.
    open_re = re.compile(r"<TabItem\s+([^>]*?)>", re.S)
    close_re = re.compile(r"</TabItem>")
    out: list[str] = []
    i = 0
    while i < len(text):
        m = open_re.search(text, i)
        if not m:
            out.append(text[i:])
            break
        out.append(text[i : m.start()])
        attrs = parse_jsx_attrs(m.group(1))
        label = attrs.get("label") or attrs.get("title") or "Tab"
        # find matching </TabItem>, tracking nested <TabItem>
        depth = 1
        j = m.end()
        while depth > 0:
            n_open = open_re.search(text, j)
            n_close = close_re.search(text, j)
            if not n_close:
                break  # unclosed; bail
            if n_open and n_open.start() < n_close.start():
                depth += 1
                j = n_open.end()
            else:
                depth -= 1
                close_end = n_close.end()
                if depth == 0:
                    body = text[m.end() : n_close.start()]
                    body = sub_tabs(body)  # recurse for nested
                    out.append(f"\n**{label}**\n\n{body.strip()}\n")
                    i = close_end
                    break
                j = close_end
        else:
            continue
        if depth > 0:
            # unbalanced; drop the open tag and continue past it
            i = m.end()
    return "".join(out)


# ---- railroad diagram ----

_RAILROAD_NODES = {
    "Diagram": lambda children, **k: railroad.Diagram(*children),
    "ComplexDiagram": lambda children, **k: railroad.ComplexDiagram(*children),
    "Sequence": lambda children, **k: railroad.Sequence(*children),
    "Stack": lambda children, **k: railroad.Stack(*children),
    "OptionalSequence": lambda children, **k: railroad.OptionalSequence(*children),
    "AlternatingSequence": lambda children, **k: railroad.AlternatingSequence(
        *children
    ),
    "Choice": lambda children, index=0, **k: railroad.Choice(
        int(index or 0), *children
    ),
    "HorizontalChoice": lambda children, **k: railroad.HorizontalChoice(*children),
    "MultipleChoice": lambda children, index=0, type="any", **k: (
        railroad.MultipleChoice(int(index or 0), type, *children)
    ),
    "Optional": lambda child, skip=False, **k: railroad.Optional(
        child, skip=bool(skip)
    ),
    "OneOrMore": lambda child, repeat=None, **k: railroad.OneOrMore(child, repeat),
    "ZeroOrMore": lambda child, repeat=None, **k: railroad.ZeroOrMore(child, repeat),
    "Group": lambda child, label=None, **k: railroad.Group(child, label),
    "Terminal": lambda **k: railroad.Terminal(
        k.get("text", ""), title=k.get("title"), href=k.get("href")
    ),
    "NonTerminal": lambda **k: railroad.NonTerminal(
        k.get("text", ""), title=k.get("title"), href=k.get("href")
    ),
    "Comment": lambda **k: railroad.Comment(
        k.get("text", ""), title=k.get("title"), href=k.get("href")
    ),
    "Skip": lambda **k: railroad.Skip(),
    "Start": lambda **k: railroad.Start(
        type=k.get("type", "simple"), label=k.get("label")
    ),
    "End": lambda **k: railroad.End(type=k.get("type", "simple")),
}


def _build_railroad(node):
    t = node["type"]
    fn = _RAILROAD_NODES.get(t)
    if not fn:
        raise ValueError(f"Unknown railroad node: {t}")
    if "children" in node:
        kids = [_build_railroad(c) for c in node["children"]]
        kwargs = {k: v for k, v in node.items() if k not in ("type", "children")}
        return fn(kids, **kwargs)
    if "child" in node:
        kid = _build_railroad(node["child"])
        kwargs = {k: v for k, v in node.items() if k not in ("type", "child")}
        return fn(kid, **kwargs)
    kwargs = {k: v for k, v in node.items() if k != "type"}
    return fn(**kwargs)


def sub_railroad(text: str) -> str:
    # ast= JSON may contain ">" chars (e.g. "->" terminals), so we anchor
    # on the matching quote of the ast attribute rather than the next ">".
    pattern = re.compile(
        r"<RailroadDiagram\b[^>]*?\bast=(['\"])(.*?)\1[^>]*?/>",
        re.S,
    )

    def repl(m):
        try:
            ast = json.loads(m.group(2))
            diag = _build_railroad(ast)
            out = []
            diag.writeText(out.append)
            return "\n```\n" + "".join(out).rstrip() + "\n```\n"
        except Exception as e:
            return f"\n*[Railroad diagram unavailable: {e}]*\n"

    return pattern.sub(repl, text)


# ---- HTML inline tags ----


def sub_inline_html(text: str) -> str:
    # <code>X</code> -> `X` (when not in a code block)
    text = re.sub(r"<code>(.*?)</code>", r"`\1`", text, flags=re.S)
    text = re.sub(r"<br\s*/?>", "  \n", text)
    return text


# ---- assets ----

ASSET_REWRITE_RE = re.compile(r"~/assets/img/([^\s)\"']+)")


def collect_asset_refs(text: str) -> list[str]:
    return list(set(m.group(1) for m in ASSET_REWRITE_RE.finditer(text)))


def rewrite_asset_paths(text: str, depth: int) -> str:
    """Rewrite ~/assets/img/foo to relative path from current file."""
    prefix = "../" * depth
    return ASSET_REWRITE_RE.sub(lambda m: f"{prefix}assets/img/{m.group(1)}", text)


def sub_imgtag(text: str) -> str:
    """Convert <img src="..." alt="..."/> to markdown image syntax."""
    pattern = re.compile(r"<img\s+([^>]*?)/?>", re.S)

    def repl(m):
        attrs = parse_jsx_attrs(m.group(1))
        src = attrs.get("src", "")
        alt = attrs.get("alt", "")
        if not src:
            return ""
        return f"![{alt}]({src})"

    return pattern.sub(repl, text)


def sub_image_component(text: str) -> str:
    """Astro <Image src={Var} alt="..."/> — src is a JS var we can't resolve. Drop to placeholder."""
    pattern = re.compile(r"<Image\s+(.*?)/>", re.S)

    def repl(m):
        attrs = parse_jsx_attrs(m.group(1))
        alt = attrs.get("alt", "image")
        return f"\n*[image: {alt}]*\n"

    return pattern.sub(repl, text)


# ---- internal links ----

_TOP_RENAMES = {"labs-items": "labs"}


def content_path_to_out(rel_mdx: Path) -> Path:
    """src/content layout -> output md path. The 'index/' tree mounts at /docs root."""
    parts = list(rel_mdx.with_suffix(".md").parts)
    if parts and parts[0] == "index":
        parts = parts[1:] or ["index.md"]
    if parts and parts[0] in _TOP_RENAMES:
        parts[0] = _TOP_RENAMES[parts[0]]
    return Path(*parts)


def build_url_to_path_map(mdx_files: list[Path], src_root: Path) -> dict[str, str]:
    """Map /docs/<path> -> relative output md file path."""
    out: dict[str, str] = {}
    for p in mdx_files:
        rel = p.relative_to(src_root)
        md = content_path_to_out(rel).as_posix()
        url = "/docs/" + md[:-3]  # strip .md
        out[url] = md
        if url.endswith("/index"):
            out[url[: -len("/index")]] = md
    return out


def rewrite_internal_links(text: str, current_md: str, url_map: dict[str, str]) -> str:
    """Rewrite /docs/X and https://surrealdb.com/docs/X to local file paths when known."""
    cur_dir = Path(current_md).parent
    text = re.sub(
        r"\[([^\]]+)\]\((/docs/[^)\s#]+)(#[^)\s]*)?\)",
        lambda m: (
            f"[{m.group(1)}]({_resolve_link(m.group(2), m.group(3) or '', cur_dir, url_map)})"
        ),
        text,
    )
    text = re.sub(
        r"\[([^\]]+)\]\(https?://surrealdb\.com(/docs/[^)\s#]+?)/?(#[^)\s]*)?\)",
        lambda m: (
            f"[{m.group(1)}]({_resolve_link(m.group(2), m.group(3) or '', cur_dir, url_map)})"
        ),
        text,
    )
    return text


def _resolve_link(
    path: str, anchor: str, cur_dir: Path, url_map: dict[str, str]
) -> str:
    target = url_map.get(path)
    if not target:
        return f"{SITE}{path}{anchor}"
    rel = relpath(Path(target), cur_dir)
    return rel + anchor


def relpath(target: Path, from_dir: Path) -> str:
    """POSIX-style relative path from from_dir to target."""
    # both are relative to docs/ root
    from_parts = list(from_dir.parts) if str(from_dir) not in ("", ".") else []
    tgt_parts = list(target.parts)
    # drop common prefix
    i = 0
    while (
        i < len(from_parts) and i < len(tgt_parts) - 1 and from_parts[i] == tgt_parts[i]
    ):
        i += 1
    up = [".."] * (len(from_parts) - i)
    return "/".join(up + tgt_parts[i:]) or target.name


UNKNOWN_TAG_LOG: dict[str, int] = defaultdict(int)


def transform(
    text: str,
    current_md_path: str,
    source_mdx_path: str,
    url_map: dict[str, str],
    depth: int,
) -> str:
    fm, body = parse_frontmatter(text)

    # remove any stray top-level imports (rare)
    body = re.sub(r"^import\s+[^\n]+\n", "", body, flags=re.M)

    # railroad first (contains escaped chars that other passes might mangle)
    body = sub_railroad(body)

    body = sub_tabs(body)
    body = sub_iconbox(body)
    body = strip_tag(body, "Boxes")
    body = strip_tag(body, "Table")
    body = sub_icon(body)
    body = sub_label(body)
    body = sub_since(body)
    body = sub_version(body)
    body = sub_image_component(body)
    body = sub_surrealist_mini(body)
    body = sub_imgtag(body)
    body = sub_inline_html(body)

    # asset paths -> local
    body = rewrite_asset_paths(body, depth)

    # internal /docs links
    body = rewrite_internal_links(body, current_md_path, url_map)

    # collapse runs of >2 blank lines
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"

    # frontmatter (keep original keys, add source)
    fm.setdefault(
        "source",
        f"https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/{source_mdx_path}",
    )
    return emit_frontmatter(fm) + "\n" + body


# Navigation mirrors surrealdb/docs.surrealdb.com Layout/header.tsx NAV_LINKS.
# Each href is a /docs/... URL; we map to local md paths via url_map.
NAV: list[dict] = [
    {"label": "Start", "href": "/docs/"},
    {
        "label": "Learn",
        "sections": [
            {
                "heading": "Database",
                "items": [
                    {
                        "label": "Querying",
                        "href": "/docs/learn/querying",
                        "description": "SurrealQL and live result handling.",
                    },
                    {
                        "label": "Schema management",
                        "href": "/docs/learn/schema-management",
                        "description": "Namespaces, tables, and indexes.",
                    },
                    {
                        "label": "Data models",
                        "href": "/docs/learn/data-models",
                        "description": "Documents, graphs, vectors, time series.",
                    },
                    {
                        "label": "Security",
                        "href": "/docs/learn/security",
                        "description": "Authentication, scopes, and permissions.",
                    },
                ],
            },
            {
                "heading": "Extending",
                "items": [
                    {
                        "label": "Agent memory context",
                        "href": "/docs/learn/context",
                        "description": "LLM memory and tool context patterns.",
                    },
                    {
                        "label": "Extensions",
                        "href": "/docs/learn/extensions",
                        "description": "Functions, procedures, and plugins.",
                    },
                ],
            },
        ],
    },
    {
        "label": "Build",
        "sections": [
            {
                "heading": "Running",
                "items": [
                    {
                        "label": "Deployment",
                        "href": "/docs/build/deployment",
                        "description": "Cloud, edge, and on-premises.",
                    },
                    {
                        "label": "Embedding SurrealDB",
                        "href": "/docs/build/embedding",
                        "description": "Native and WebAssembly embedding.",
                    },
                ],
            },
            {
                "heading": "Ecosystem",
                "items": [
                    {
                        "label": "Migrating",
                        "href": "/docs/build/migrating",
                        "description": "Import data and schemas from elsewhere.",
                    },
                    {
                        "label": "Integrations",
                        "href": "/docs/build/integrations",
                        "description": "SDKs, frameworks, and connectors.",
                    },
                ],
            },
            {
                "heading": "Intelligence",
                "items": [
                    {
                        "label": "AI agents",
                        "href": "/docs/build/ai-agents",
                        "description": "Design patterns for AI agents.",
                    },
                ],
            },
        ],
    },
    {
        "label": "Manage",
        "sections": [
            {
                "heading": "Hosting",
                "items": [
                    {
                        "label": "SurrealDB Cloud",
                        "href": "/docs/manage/cloud",
                        "description": "Hosted instances and Cloud console.",
                    },
                    {
                        "label": "Self-hosted",
                        "href": "/docs/manage/self-hosted",
                        "description": "Clusters, backups, your infrastructure.",
                    },
                ],
            },
            {
                "heading": "Operations",
                "items": [
                    {
                        "label": "Schema migration",
                        "href": "/docs/manage/schema-migration",
                        "description": "Promote schema updates safely.",
                    },
                ],
            },
        ],
    },
    {
        "label": "Explore",
        "sections": [
            {
                "heading": "Tools",
                "items": [
                    {
                        "label": "Surrealist UI",
                        "href": "/docs/explore/surrealist",
                        "description": "Official SurrealDB IDE.",
                    },
                ],
            },
            {
                "heading": "Guides and resources",
                "items": [
                    {
                        "label": "Tutorials & demos",
                        "href": "/docs/explore/tutorials",
                        "description": "Hands-on walkthroughs and demos.",
                    },
                    {
                        "label": "SurrealDB Labs",
                        "href": "/docs/labs",
                        "description": "Preview features and lab notes.",
                    },
                ],
            },
        ],
    },
    {
        "label": "Reference",
        "sections": [
            {
                "heading": None,
                "items": [
                    {
                        "label": "Query language",
                        "href": "/docs/reference/query-language",
                        "description": "Syntax, statements, and builtins.",
                    },
                    {
                        "label": "CLI tools",
                        "href": "/docs/reference/cli",
                        "description": "CLI install, backup, and ops.",
                    },
                    {
                        "label": "REST API",
                        "href": "/docs/reference/rest-api",
                        "description": "HTTP API for queries and admin.",
                    },
                ],
            },
        ],
    },
]


def _resolve_nav_target(href: str, url_map: dict[str, str]) -> str | None:
    """Resolve /docs/... href to local md path; try /index variants."""
    href = href.rstrip("/")
    for candidate in (href, href + "/index"):
        target = url_map.get(candidate)
        if target:
            return target
    return None


def generate_stub_indexes(outdir: Path, pages: list[dict]) -> None:
    """For dirs containing pages but no index.md, write a stub listing children."""
    have_index: set[str] = set()
    files_by_parent: dict[str, list[dict]] = defaultdict(list)
    subdirs_by_parent: dict[str, set[str]] = defaultdict(set)
    all_parents: set[str] = set()
    for p in pages:
        parts = p["rel"].split("/")
        for i in range(1, len(parts)):
            parent = "/".join(parts[:i])
            all_parents.add(parent)
            if i < len(parts) - 1:
                subdirs_by_parent[parent].add(parts[i])
        if len(parts) > 1:
            files_by_parent["/".join(parts[:-1])].append(p)
        if parts[-1] == "index.md":
            have_index.add("/".join(parts[:-1]))
    by_rel = {p["rel"]: p for p in pages}
    for parent in sorted(all_parents):
        if parent in have_index:
            continue
        stub = outdir / parent / "index.md"
        if stub.exists():
            continue
        title = parent.split("/")[-1].replace("-", " ").title()
        files = files_by_parent.get(parent, [])
        subdirs = sorted(subdirs_by_parent.get(parent, set()))
        parts_summary = [f"{len(files)} page{'s' if len(files) != 1 else ''}"]
        if subdirs:
            parts_summary.append(
                f"{len(subdirs)} sub-section{'s' if len(subdirs) != 1 else ''}"
            )
        lines = [
            "---",
            f"title: {title}",
            "generated: stub",
            "---",
            "",
            f"# {title}",
            "",
            f"_Auto-generated index — {' and '.join(parts_summary)}._",
            "",
        ]
        if subdirs:
            lines.append("## Sub-sections\n")
            for sd in subdirs:
                child_index = f"{parent}/{sd}/index.md"
                child_page = by_rel.get(child_index)
                label = (child_page or {}).get("title") or sd.replace("-", " ").title()
                desc = (child_page or {}).get("description", "")
                line = f"- **[{label}]({sd}/index.md)**"
                if desc:
                    line += f" — {desc}"
                lines.append(line)
            lines.append("")
        if files:
            lines.append("## Pages\n")
            for kid in sorted(files, key=lambda x: x["rel"]):
                name = kid["rel"].split("/")[-1]
                kid_title = kid.get("title") or name
                lines.append(f"- [{kid_title}]({name})")
                if kid.get("description"):
                    lines.append(f"  {kid['description']}")
        stub.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_indexes(outdir: Path, pages: list[dict], url_map: dict[str, str]) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    by_dir: dict[str, list[dict]] = defaultdict(list)
    for p in pages:
        parts = p["rel"].split("/")
        for i in range(1, len(parts)):
            by_dir["/".join(parts[:i])].append(p)
        by_dir[""].append(p)

    def count_under(target_md: str) -> int:
        prefix = target_md.rsplit("/", 1)[0] if "/" in target_md else ""
        return len(by_dir.get(prefix, [])) or 1

    out = [
        "# SurrealDB Documentation Mirror\n",
        f"_Last updated: {now}_\n",
        "_Mirrored from [surrealdb/docs.surrealdb.com](https://github.com/surrealdb/docs.surrealdb.com)_\n",
        "## Stats\n",
        f"- **Total pages:** {len(pages)}\n",
        "## Browse\n",
        "- [All pages (flat list)](all.md)\n",
    ]
    covered_top: set[str] = set()
    for entry in NAV:
        label = entry["label"]
        if "href" in entry:
            target = _resolve_nav_target(entry["href"], url_map)
            out.append(f"## [{label}]({target})\n" if target else f"## {label}\n")
            continue
        out.append(f"## {label}\n")
        for sec in entry.get("sections", []):
            if sec.get("heading"):
                out.append(f"### {sec['heading']}\n")
            for item in sec["items"]:
                target = _resolve_nav_target(item["href"], url_map)
                desc = item.get("description", "")
                if target:
                    top = target.split("/", 1)[0]
                    covered_top.add(top)
                    prefix = target.rsplit("/", 1)[0] if "/" in target else ""
                    n = len(by_dir.get(prefix, []))
                    suffix = f" — _{n} pages_" if n > 1 else ""
                    out.append(f"- **[{item['label']}]({target})** — {desc}{suffix}")
                else:
                    out.append(f"- **{item['label']}** — {desc} _(not mirrored)_")
            out.append("")

    # Content present in the source tree but not in the header nav.
    extras = [
        (
            "languages",
            "SDKs",
            "Official client SDKs for Rust, JavaScript, Python, Go, .NET, PHP, and Java.",
        ),
        ("frameworks", "Frameworks", "Framework integrations and starter templates."),
        (
            "self-hosted",
            "Self-hosted quickstart",
            "Install and run SurrealDB locally for SDK development.",
        ),
        ("labs", "SurrealDB Labs", "Community-contributed lab notes and previews."),
    ]
    extra_present = [
        (d, lbl, desc)
        for d, lbl, desc in extras
        if d not in covered_top and any(p["rel"].startswith(d + "/") for p in pages)
    ]
    if extra_present:
        out.append("## More content\n")
        for d, lbl, desc in extra_present:
            n = sum(1 for p in pages if p["rel"].startswith(d + "/"))
            index_md = _resolve_nav_target("/docs/" + d, url_map) or f"{d}/index.md"
            out.append(f"- **[{lbl}]({index_md})** — {desc} _({n} pages)_")
        out.append("")

    (outdir / "README.md").write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")

    flat = [
        "# All Documentation Pages\n",
        f"_{len(pages)} pages_  \n[← Index](README.md)\n",
    ]
    for p in sorted(pages, key=lambda x: x["rel"]):
        title = p.get("title") or p["rel"]
        flat.append(f"- [{title}]({p['rel']})")
        if p.get("description"):
            flat.append(f"  {p['description']}")
    (outdir / "all.md").write_text("\n".join(flat).rstrip() + "\n", encoding="utf-8")


def _flatten_nav(nav: list[dict]) -> tuple[set[str], set[str]]:
    labels: set[str] = set()
    hrefs: set[str] = set()
    for entry in nav:
        labels.add(entry["label"])
        if "href" in entry:
            hrefs.add(entry["href"].rstrip("/") or "/docs")
        for sec in entry.get("sections", []):
            if sec.get("heading"):
                labels.add(sec["heading"])
            for item in sec.get("items", []):
                labels.add(item["label"])
                if "href" in item:
                    hrefs.add(item["href"].rstrip("/") or "/docs")
    return labels, hrefs


def check_nav_drift(nav: list[dict], allow_drift: bool) -> None:
    """Compare local NAV against upstream header.tsx; exit on drift unless allowed."""
    try:
        with urllib.request.urlopen(HEADER_TSX_URL, timeout=20) as r:
            tsx = r.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(
            f"  nav-drift: could not fetch header.tsx ({e}); skipping check",
            file=sys.stderr,
        )
        return

    m = re.search(r"export const NAV_LINKS[^=]*=\s*\[", tsx)
    if not m:
        print(
            "  nav-drift: NAV_LINKS not found in header.tsx; skipping check",
            file=sys.stderr,
        )
        return
    # Walk forward, balancing brackets to find the end of the array literal.
    i, depth = m.end() - 1, 0
    while i < len(tsx):
        c = tsx[i]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                break
        i += 1
    block = tsx[m.end() - 1 : i + 1]

    # Strip line and block comments to avoid picking up commented-out entries.
    block = re.sub(r"//[^\n]*", "", block)
    block = re.sub(r"/\*.*?\*/", "", block, flags=re.S)

    upstream_labels = set(re.findall(r'\blabel\s*:\s*"([^"]+)"', block))
    upstream_labels |= set(re.findall(r'\bheading\s*:\s*"([^"]+)"', block))
    upstream_hrefs = {
        h.rstrip("/") or "/docs" for h in re.findall(r'\bhref\s*:\s*"([^"]+)"', block)
    }

    local_labels, local_hrefs = _flatten_nav(nav)
    missing_labels = upstream_labels - local_labels
    extra_labels = local_labels - upstream_labels
    missing_hrefs = upstream_hrefs - local_hrefs
    extra_hrefs = local_hrefs - upstream_hrefs

    if not (missing_labels or extra_labels or missing_hrefs or extra_hrefs):
        print("  nav-drift: OK (NAV matches upstream header.tsx)")
        return

    print(
        "  nav-drift: DETECTED — NAV constant out of sync with header.tsx",
        file=sys.stderr,
    )
    if missing_labels:
        print(f"    MISSING labels: {sorted(missing_labels)}", file=sys.stderr)
    if extra_labels:
        print(f"    EXTRA labels:   {sorted(extra_labels)}", file=sys.stderr)
    if missing_hrefs:
        print(f"    MISSING hrefs:  {sorted(missing_hrefs)}", file=sys.stderr)
    if extra_hrefs:
        print(f"    EXTRA hrefs:    {sorted(extra_hrefs)}", file=sys.stderr)
    if not allow_drift:
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="docs", help="output dir (default: docs)")
    ap.add_argument("--workdir", default=".cache-docs", help="tarball extract dir")
    ap.add_argument("--keep-workdir", action="store_true")
    ap.add_argument(
        "--allow-nav-drift",
        action="store_true",
        help="warn but don't fail on NAV/header.tsx mismatch",
    )
    args = ap.parse_args()

    outdir = Path(args.outdir).resolve()
    workdir = Path(args.workdir).resolve()

    check_nav_drift(NAV, args.allow_nav_drift)

    download_repo(workdir)
    src_root = workdir / "src" / "content"
    asset_root = workdir / "src" / "assets" / "img"

    mdx_files = sorted(src_root.rglob("*.mdx"))
    print(f"found {len(mdx_files)} mdx files", flush=True)

    url_map = build_url_to_path_map(mdx_files, src_root)

    # Pre-register stub index paths so cross-page links resolve to them.
    out_paths = {
        content_path_to_out(m.relative_to(src_root)).as_posix() for m in mdx_files
    }
    have_index_dirs = {
        p.rsplit("/", 1)[0] if "/" in p else ""
        for p in out_paths
        if p.endswith("index.md")
    }
    for p in out_paths:
        if "/" not in p:
            continue
        parent = p.rsplit("/", 1)[0]
        if parent in have_index_dirs:
            continue
        stub_url = "/docs/" + parent
        url_map.setdefault(stub_url, f"{parent}/index.md")

    # clean output (everything except assets dir, which we'll repopulate)
    if outdir.exists():
        for child in outdir.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    outdir.mkdir(parents=True, exist_ok=True)

    pages_meta: list[dict] = []
    assets_used: set[str] = set()

    for mdx in mdx_files:
        src_rel = mdx.relative_to(src_root)
        rel = content_path_to_out(src_rel)
        rel_posix = rel.as_posix()
        depth = len(rel.parent.parts) if str(rel.parent) != "." else 0
        text = mdx.read_text(encoding="utf-8")
        try:
            out = transform(text, rel_posix, src_rel.as_posix(), url_map, depth)
        except Exception as e:
            print(f"  ERROR transforming {mdx}: {e}", file=sys.stderr)
            continue
        for asset in collect_asset_refs(text):
            assets_used.add(asset)
        target = outdir / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(out, encoding="utf-8")
        fm, _ = parse_frontmatter(text)
        pages_meta.append(
            {
                "rel": rel_posix,
                "title": fm.get("title", ""),
                "description": fm.get("description", ""),
            }
        )

    # copy assets
    if asset_root.exists():
        copied = 0
        for asset in sorted(assets_used):
            src = asset_root / asset
            if not src.exists():
                continue
            dst = outdir / "assets" / "img" / asset
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
            copied += 1
        print(f"copied {copied}/{len(assets_used)} assets", flush=True)

    generate_stub_indexes(outdir, pages_meta)
    write_indexes(outdir, pages_meta, url_map)

    if not args.keep_workdir:
        shutil.rmtree(workdir, ignore_errors=True)

    print(f"wrote {len(pages_meta)} pages to {outdir}")


if __name__ == "__main__":
    main()
