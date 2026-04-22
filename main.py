import asyncio
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain.agents import create_agent 
from langgraph.prebuilt import create_react_agent


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",   # or "gemini-1.5-pro"
    temperature=0.7)

stdio_server_parameters = StdioServerParameters(
    command="python",
    args=["C:\\Users\\rajes\\aiml_projects\\mcp-crash-course\\servers\\math_server.py"],
)

async def main():
    async with stdio_client(stdio_server_parameters) as (read,write): 
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("Connected to the server")
            tools = await load_mcp_tools(session)
            
            agent = create_react_agent(llm, tools)

            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 10 + 20?")]})
            print(result["messages"][-1].content)

if __name__ == "__main__":
   asyncio.run(main())
