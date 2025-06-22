# Multi-Agent Coding Loop

## WORKING-IN-PROGRESS - 

A lightweight agent orchestration framework to enhance code development using multiple LLMs:

- **GitHub Copilot**: Inline autocomplete
- **Grok 3**: Debugging and alternative solutions
- **DeepSeekCoder**: Syntax-aware refactoring and improvements
- **Claude API**: Explanations, tests, refactoring, documentation
- **GPT-4o** (optional): General fallback reasoning

## Project Objectives and Philosophy

This project starts with a simple class-based agent implementation — where each agent (Writer, Reviewer, Tester) is a Python class that prompts an LLM for a specific role. The goal is to provide a clear, educational example of how multi-agent LLM loops work — without heavy frameworks or complex orchestration. In future phases, we will evolve these agents toward more “real” agents — with memory, reasoning, and adaptive loops — using frameworks like LangGraph or CrewAI. The priority is to keep the project flexible, educational, and easy for others to understand and extend.

## Goals in mind

- Accelerate coding workflows with a multi-agent loop
- Combine strengths of different LLMs
- Provide cross-model feedback and validation
- Maintain a reusable agent layer across projects

## Features

- See [ROADMAP.md](ROADMAP.md)

## Approach 

- Local CPU loop (Ollama)
- Cloud GPU loop (Vast.ai)
- Direct API backends (OpenAI, Anthropic) — optional
- Better than Cline: adaptive loops, memory, visualization


## Sample Code

```bash

pip install requests 

# install ollama 
curl https://ollama.com/install.sh | bash
ollama --version

# check if ollama is running. If not, run ollama serve
ps aux | grep -i ollama
ollama serve

# pull mistral 
ollama pull mistral

# run a python code 
python examples/local_cpu_loop_simple.py

```