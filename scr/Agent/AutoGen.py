import os
import asyncio
import subprocess
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.tools.mcp import StdioServerParams,McpWorkbench

from dotenv import load_dotenv


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def main():

    file = StdioServerParams(command="npx", args=["@playwright/mcp@latest"])
    playwritwork =McpWorkbench(file)
    tas = input("UserQuestion : ")
    async with playwritwork as Pl_Wb :
        model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini", api_key=OPENAI_API_KEY
            )
        Ai_Agent = AssistantAgent(
        name="AI_Agent",
        model_client=model_client,
        workbench=Pl_Wb
        )
        response = await Ai_Agent.run(task=tas)

        print("AI Agent Response:", response.messages[-1].content)
asyncio.run(main())
