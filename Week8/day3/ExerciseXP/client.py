import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(command="mcp", args=["run", "server.py"], env=None)


def extract_content(payload):
    """Best-effort to pull text from MCP responses."""
    if hasattr(payload, "contents"):
        contents = payload.contents
        if contents:
            first = contents[0]
            if hasattr(first, "text"):
                return first.text
            if isinstance(first, dict) and "text" in first:
                return first["text"]
            return str(first)
    if hasattr(payload, "content"):
        return payload.content
    return str(payload)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # List resources and print their URIs
            resources = await session.list_resources()
            print("\nResources:")
            for uri in resources:
                print(f"- {uri}")

            # List tools and print their names
            tools = await session.list_tools()
            print("\nTools:")
            for tool_name in tools:
                print(f"- {tool_name}")

            # Read greeting://hello and print the content
            greeting_response = await session.read("greeting://hello")
            print(f"\nGreeting: {extract_content(greeting_response)}")

            # Call add with a=1, b=7 and print the result
            add_response = await session.call("add", a=1, b=7)
            print(f"\nAdd result: {extract_content(add_response)}")


if __name__ == "__main__":
    asyncio.run(run())
