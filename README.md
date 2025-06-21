# Multi-Agent Coding Loop

## WORKING-IN-PROGRESS

A lightweight agent orchestration framework to enhance code development using multiple LLMs:

- **GitHub Copilot**: Inline autocomplete
- **Grok 3**: Debugging and alternative solutions
- **DeepSeekCoder**: Syntax-aware refactoring and improvements
- **Claude API**: Explanations, tests, refactoring, documentation
- **GPT-4o** (optional): General fallback reasoning

## Goals

- Accelerate coding workflows with a multi-agent loop
- Combine strengths of different LLMs
- Provide cross-model feedback and validation
- Maintain a reusable agent layer across projects

## How to Run

```bash
python agent_loop.py --file sample_code/test1.py
