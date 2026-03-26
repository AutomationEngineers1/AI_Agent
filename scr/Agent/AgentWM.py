from asyncio import tools
from logging import config
import os
import asyncio
import subprocess
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console




from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench
from autogen_agentchat.teams import RoundRobinGroupChat
from tools import load_prompt

from dotenv import load_dotenv
from sympy import true
from mem0 import Memory


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def main():

    file = StdioServerParams(
        command="npx",
        args=[
            "@playwright/mcp@latest",
            "--timeout-action=15000",
            "--timeout-navigation=90000",
        ],
        startup_timeout=20,
        read_timeout_seconds=60,
        timeout_seconds=120,
    )
    playwritwork = McpWorkbench(file)
    system_message = load_prompt(
        r"C:\Users\Aman Verma\Desktop\Final Agent\Agent\AI_Context_Massages\System_Messages.txt"
    )
    
    system_message2 = load_prompt(
        r"C:\Users\Aman Verma\Desktop\Final Agent\Agent\AI_Context_Massages\System_Messages2.txt"
    )

    # tas = load_prompt(
    #     r"C:\Users\Aman Verma\Desktop\Final Agent\Agent\AI_Context_Massages\User_quary.txt"
    # )

    async with playwritwork as Pl_Wb:
            model_client = OpenAIChatCompletionClient(
                model="gpt-4o", api_key=OPENAI_API_KEY
            )
            playwrightTester  = AssistantAgent(
                name="Playwrite_Tester",
                model_client=model_client,
                workbench=Pl_Wb,
                system_message=system_message,
            )
            Step_Creator  = AssistantAgent(
                name="Test_Step_Planer",
                model_client=model_client,
                system_message=system_message2,
            )
            team = RoundRobinGroupChat(participants=[Step_Creator,playwrightTester],max_turns=3,)
            await Console(team.run_stream(task="Find the current job openings in Testing Xpert. Open Google, search for the company, go to the official website, navigate to the careers or jobs section, and show the available openings."))



asyncio.run(main())
