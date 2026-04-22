import asyncio
from dotenv import load_dotenv
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain.agents import create_agent 
from langgraph.prebuilt import create_react_agent


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",   # or "gemini-1.5-pro"
    temperature=0.7)

stdio_server_parameters = StdioServerParameters(
    command="python",
    args=["C:\\Users\\rajes\\aiml_projects\\mcp-crash-course\\servers\\math_server.py"],
)

async def main():
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
   asyncio.run(main())
