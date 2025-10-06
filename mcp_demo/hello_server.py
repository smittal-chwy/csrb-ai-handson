# server/hello_server.py
from datetime import datetime
from mcp.server.fastmcp import FastMCP

# Create server instance
mcp = FastMCP("chewy-demo-server")

# ────────────────────────────────────────────────────────────────
# TOOLS
# ────────────────────────────────────────────────────────────────

@mcp.tool()
async def say_hello(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}! 👋 Welcome to the Chewy MCP Demo."

@mcp.tool()
async def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b

@mcp.tool()
async def reverse_text(text: str) -> str:
    """Reverse the given string."""
    return text[::-1]

@mcp.tool()
async def get_time(timezone: str = "UTC") -> str:
    """Return the current time (demo only)."""
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"Current time in {timezone}: {now}"

# ────────────────────────────────────────────────────────────────
# RESOURCES
# ────────────────────────────────────────────────────────────────
# Resources in MCP are small content blobs (like docs, text files, datasets)
# You can expose them with static content or dynamic generation.
from pathlib import Path
@mcp.resource("resource://static/greeting.md")
async def greeting_resource():
    """A static markdown resource for demo."""
    path = Path(__file__).parent / "static" / "greeting.md"
    return path.read_text()
# ────────────────────────────────────────────────────────────────
# MAIN ENTRY
# ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run(transport="stdio")
