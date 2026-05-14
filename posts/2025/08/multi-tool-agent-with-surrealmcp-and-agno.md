---
title: "Multi-tool agent with SurrealMCP and Agno"
slug: "multi-tool-agent-with-surrealmcp-and-agno"
date: "2025-08-27T00:00:00.000Z"
categories:
  - "featured"
  - "tutorials"
  - "ai"
read_time: "3 min read"
summary: "Using SurrealMCP and Agno, this is how you can build a “researcher” agent that finds information on the web, structures the data, and stores it in SurrealDB."
source: "https://surrealdb.com/blog/multi-tool-agent-with-surrealmcp-and-agno"
cover: "../../assets/abaf81ceb1f12b75.jpg"
---

# Multi-tool agent with SurrealMCP and Agno

![Multi-tool agent with SurrealMCP and Agno](../../assets/abaf81ceb1f12b75.jpg)

[Agno](https://docs.agno.com/introduction) is a Python framework for building multi-agent systems with shared memory, knowledge and reasoning. This blog post will show you how to build an agent with multiple tools, including [SurrealMCP](/mcp), the Model Context Protocol integration for SurrealDB. Our agent will be a “researcher” that finds information on the web, structures the data, and stores it in SurrealDB.

The agent does quite a good job at responding to naturally worded requests. Here’s a sample user question and the output it generated:

> Who are the F1 drivers since the year 2000, including how many race starts and wins

## Before we get started

If you are not familiar with Agno agents, check out the post entitled [What are Agents?](https://docs.agno.com/agents/introduction) from Agno's own website.

Next, we’ll need an LLM and the SurrealMCP server.

### LLM

For the LLM, I recommend Claude from Anthropic. You’ll need an `ANTHROPIC_API_KEY`, which you can get [from Anthropic here](https://console.anthropic.com/settings/keys). You can also try with a [model from Ollama that supports tools](https://ollama.com/search?c=tools), which runs locally on your computer without requiring an API key. Keep in mind that these models are typically smaller than those from Anthropic, so results may vary significantly. I tested `qwen3:8b` and found it difficult to get the agent working reliably. Nevertheless, it's worth (and even recommended) to begin with an inferior model so you can see where LLMs get confused and identify opportunities to improve your prompts. This is why I prefer starting with smaller (and cheaper) LLMs to develop agents in worst-case scenarios. When things go wrong, you get valuable chances to implement proper error handling.

### SurrealMCP

There are many ways to set [SurrealMCP](https://github.com/surrealdb/surrealmcp) up. This is one way to run it locally with a local DB in memory:

1. [Install SurrealDB](/docs/surrealdb/installation)

and [run SurrealDB](/docs/surrealdb/installation/running). Run in-memory with:

```cli
    surreal start -u root -p root
```

Or [with Docker](/docs/surrealdb/installation/running/docker):

```cli
    docker run --rm --pull always -p 8000:8000 surrealdb/surrealdb:latest start
```

2. Start the MCP server:

Using cargo:

```cli
    RUST_LOG=debug cargo run -- start -e "ws://localhost:8000/rpc" \
        --ns mcp --db test -u root -p root \
        --auth-disabled \
        --server-url "http://localhost:8080" \
        --bind-address 0.0.0.0:8080
```

Or with Docker:

```cli
    docker run --rm -i --pull always surrealdb/surrealmcp:latest start
```

## Let’s start with a basic agent

This basic agent uses one tool (our SurrealMCP) and has simple `description` and `instructions`. Optionally, you can enable a second tool, `ReasoningTools`, which lets the agent reflect after each step, adjust its thinking, and update its actions on the fly.

```python

from textwrap import dedent

from agno.agent import Agent
from agno.models.anthropic import Claude
# from agno.models.ollama import Ollama
from agno.tools.mcp import MCPTools
from agno.tools.reasoning import ReasoningTools
from agno.utils.log import log_info
from dotenv import load_dotenv

# Required env var: ANTHROPIC_API_KEY
load_dotenv()


async def run_mcp_agent(message: str):
    mcp_tools = MCPTools(
        command=None, url="http://localhost:8080/mcp", transport="streamable-http"
    )
    await mcp_tools.connect()

    agent = Agent(
        model=Claude(id="claude-sonnet-4-20250514"),
        # model=Ollama(id="qwen3:8b"),
        tools=[
            mcp_tools,
            # - Try with and without this. More info about this here: https://docs.agno.com/tools/reasoning_tools/reasoning-tools
            # ReasoningTools(add_instructions=True),
        ],
        description="You are a SurrealDB expert",
        instructions="You are already connected to the DB",
        show_tool_calls=True,
        markdown=True,
    )

    log_info(f"Running agent with message: {message}")
    await agent.aprint_response(
        message,
        stream=True,
        stream_intermediate_steps=True,
        show_full_reasoning=True,
    )
    await mcp_tools.close()


if __name__ == "__main__":
    query = dedent("""\
    Insert Brandon Sanderson's top 10 books in the `books` table, including
    title, year, ang page count.
    """)
    asyncio.run(run_mcp_agent(query))
```

## The multi-tool agent

Now, let’s add more tools to make our agent more interesting. Besides the tools, we also need to provide better instructions.

```python

from textwrap import dedent

from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.mcp import MCPTools
from agno.tools.reasoning import ReasoningTools
from agno.tools.website import WebsiteTools
from agno.utils.log import log_info
from dotenv import load_dotenv

from src.tools.ddg import search_text

# Required env var: ANTHROPIC_API_KEY
load_dotenv()


async def run_mcp_agent(message: str):
    surrealmcp = MCPTools(
        command=None, url="http://localhost:8080/mcp", transport="streamable-http"
    )
    await surrealmcp.connect()

    description = "You are a SurrealDB expert"

    instructions = dedent(f"""\
        Based on the user's question: {message}

        Follow this steps:
        1. Search the web for the information required to answer
        2. Extract the main content from the first URL using the read_url tool from website_tools
        3. Analyze the content and structure it as a JSON list that provides the data the user is asking for
        4. Think about the name of the table where this data will be stored
        5. Store the JSON in that table using the create tool from MCPTools for each record
        6. Answer by giving the user the name of the table where you stored the data, and a summarized answer

        Notes:
        - you are already connected to the DB
    """)

    agent = Agent(
        model=Claude(id="claude-sonnet-4-20250514"),
        # - Other models you can try:
        # model=Gemini(id="gemini-2.5-pro"),
        # model=Ollama(id="qwen3:8b"),
        tools=[
            surrealmcp,
            search_text,
            WebsiteTools(),
            ReasoningTools(add_instructions=True),
        ],
        description=description,
        instructions=instructions,
        show_tool_calls=True,
        markdown=True,
        # -- Uncomment to get more debug logs
        # debug_mode=True,
        # debug_level=2,
    )

    log_info(f"Running agent with message: {message}")
    await agent.aprint_response(
        message,
        stream=True,
        stream_intermediate_steps=True,
        show_full_reasoning=True,
    )
    await surrealmcp.close()


if __name__ == "__main__":
    query = "Who are the F1 drivers since the year 2000, including how many race starts and wins"

    # - Other queries you can try:
    # query = "What are Brandon Sanderson's top 10 books?"
    # query = dedent("""\
    # Insert Brandon Sanderson's top 10 books in the `books` table, including
    # title, year, ang page count.
    # """)

    asyncio.run(run_mcp_agent(query))
```

## Running it

```cli
uv run main.py
```

## Ready to build?

Get started for free with [SurrealDB Cloud](https://app.surrealdb.com/signin).

Any questions or thoughts? Feel free to [drop by our Discord](https://discord.gg/surrealdb) to get in touch.
