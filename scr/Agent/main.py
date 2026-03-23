from openai import OpenAI
import os
from dotenv import load_dotenv
import json



load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
Client = OpenAI()
tools = [
    {
        "type": "function",
        "function": {
            "name": "run_cmd_command",
            "description": "Execute a PowerShell command on the system",
            "parameters": {
                "type": "object",
                "properties": {
                    "cmd_command": {
                        "type": "string",
                        "description": "PowerShell command to execute",
                    }
                },
                "required": ["cmd_command"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "load_prompt",
            "description": "Load a prompt file from disk",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path of the prompt file",
                    }
                },
                "required": ["file_path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "create_playwright_tools",
            "description": "Start Playwright MCP server and return browser automation tools",
            "parameters": {"type": "object", "properties": {}},
        },
    },
]


def main():
    user_quary = input("Ask Your AI Agent: ")
    Response = Client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_quary},
        ],
        tools=tools,
    )
    print(f"Agent Reply : {Response.choices[0].message.content}")


main()
