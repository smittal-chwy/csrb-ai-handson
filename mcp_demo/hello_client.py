# hello_client.py
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["hello_server.py"],
        env=None,
    )

    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()

            # List tools
            tools_resp = await session.list_tools()
            print("\nTools:", [t.name for t in tools_resp.tools])

            # List resources
            res_resp = await session.list_resources()
            print("\n📚 Resources:", [r.uri for r in res_resp.resources])

            # Call tools
            result = await session.call_tool("say_hello", {"name": "Smittal"})
            print("\n👋 say_hello →", result.content)

            add_result = await session.call_tool("add_numbers", {"a": 5, "b": 7})
            print("add_numbers →", add_result.content)

            rev_result = await session.call_tool("reverse_text", {"text": "Chewy"})
            print("reverse_text →", rev_result.content)

            time_result = await session.call_tool("get_time", {"timezone": "UTC"})
            print("get_time →", time_result.content)

            # Fetch resource
            res = await session.read_resource("resource://static/greeting.md")
            print("\n📖 greeting.md →")
            print(res.contents[0].text)

if __name__ == "__main__":
    asyncio.run(main())
