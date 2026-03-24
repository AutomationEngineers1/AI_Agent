from asyncio import tools
from logging import config
import os
import asyncio
import subprocess
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench
from tools import load_prompt

from dotenv import load_dotenv
from sympy import true
from mem0 import Memory


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {"api_key": OPENAI_API_KEY, "model": "text-embedding-3-small"},
    },
    "llm": {
        "provider": "openai",
        "config": {"api_key": OPENAI_API_KEY, "model": "gpt-4o"},
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {"host": "localhost", "port": 6333},
    },
}
memclient = Memory.from_config(config)


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

    # tas = load_prompt(
    #     r"C:\Users\Aman Verma\Desktop\Final Agent\Agent\AI_Context_Massages\User_quary.txt"
    # )

    while true:
        async with playwritwork as Pl_Wb:
            model_client = OpenAIChatCompletionClient(
                model="gpt-4o", api_key=OPENAI_API_KEY
            )
            Ai_Agent = AssistantAgent(
                name="AI_Agent",
                model_client=model_client,
                workbench=Pl_Wb,
                system_message=system_message,
            )
            

            tasks = input("How may i help you: ")
            memclient.add(
            messages=[{"role": "user", "content": tasks}],
            user_id="aman"
         )

         # ✅ retrieve memory
            memory = memclient.search(
            query=tasks,
            user_id="aman",
            limit=3
             )

         # ✅ inject memory
            task_with_memory = f"""
             Previous conversation:
            {memory}

            Current query:
            {tasks}

         Answer using memory if relevant.
            """

            response = await Ai_Agent.run(task=task_with_memory)
            print("AI Agent Response:", response.messages[-1].content)


asyncio.run(main())
