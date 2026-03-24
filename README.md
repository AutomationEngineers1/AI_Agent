AI Agent with Playwright + MCP + Memory

This project builds an AI-powered browser automation agent using:

Playwright MCP Server
AutoGen Agent Framework
OpenAI Models
Optional Memory (Qdrant + Mem0)

SETUP INSTRUCTIONS

Create Virtual Environment

python -m venv venv

Activate Virtual Environment

Windows:
venv\Scripts\activate

IMPORTANT

Select the correct Python interpreter in your IDE (VS Code recommended), otherwise you may face import errors.

Create requirements.txt

pip freeze > requirements.txt

Install Dependencies from requirements.txt

pip install -r requirements.txt

MANUAL PACKAGE INSTALLATION

Install OpenAI:
pip install openai

Install AutoGen Framework:
pip install "autogen-ext[openai]"
pip install autogen-agentchat autogen-ext

Install MCP (Model Context Protocol):
pip install mcp

PLAYWRIGHT MCP SETUP

Playwright MCP runs via npx, so make sure:

Install Node.js from:
https://nodejs.org/

Run MCP Server:
npx @playwright/mcp@latest

FEATURES

AI Agent using AutoGen
Browser automation with Playwright MCP
Tool-based execution
Interactive CLI agent
Optional memory integration (Mem0 + Vector DB)

RUN THE PROJECT

python your_script_name.py

COMMON ISSUES & FIXES

Import Errors:

Ensure virtual environment is activated
Select correct Python interpreter

MCP Not Working:

Ensure Node.js is installed
Run: npx @playwright/mcp@latest

Slow First Run:

Playwright downloads browser binaries (one-time setup)

RECOMMENDED PROJECT STRUCTURE

project/
│
├── venv/
├── scr/
│ └── Agent/
│ └── AutoGen.py
│
├── tools/
├── AI_Context_Messages/
├── requirements.txt

