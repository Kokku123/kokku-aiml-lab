import asyncio
from dotenv import load_dotenv
import os


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
print(GOOGLE_API_KEY)

async def main():
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
   asyncio.run(main())
