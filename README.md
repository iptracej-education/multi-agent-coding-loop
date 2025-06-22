# Multi-Agent Coding Loop

A lightweight agent orchestration framework for enhancing code development through multi-agent LLM collaboration.

Supports flexible combinations of local and cloud-based LLMs:

- **Claude Code (API)**: Main code generation engine
- **Code LLaMA Python**: Reviewer / AI/LLM specialist (Vast.ai GPU)
- **StarCoder 2**: Reviewer / testing agent (Vast.ai GPU)
- **Local LLMs (CPU / GPU)**: Additional meta reasoning agents
- **GPT-4o / Claude API (optional)**: For reflection, advanced feedback

---

## Project Objectives and Philosophy

The project started as a simple **class-based agent loop** using local LLMs — to provide an educational foundation for multi-agent orchestration (Writer, Reviewer, Tester classes).

Now evolving toward a flexible architecture that can:

✅ Combine cloud APIs + local models + GPU agents  
✅ Run adaptable coding loops with multiple reviewers  
✅ Support learning loops for self-improvement (fine-tune open models from experience)  
✅ Stay **framework-light** — no heavy orchestration frameworks required

Future: Agents will gain memory, reflection, adaptive behaviors — using frameworks like LangGraph or CrewAI — but with clear, reusable architecture.

---

## Goals

- Accelerate AI/LLM project development using multi-agent loops
- Combine strengths of different LLMs (Claude, Code LLaMA, StarCoder, etc.)
- Provide cross-model feedback and validation
- Build reusable agent layers for future self-improving loops

---

## Current Architectures

### v0.1 — Initial Architecture (Local CPU loop)

- Local LLMs running in Ollama (Mistral 7B)
- Class-based Writer / Reviewer / Tester agents
- Run fully on local CPU

### v0.2 — Next Architecture (Mixed Cloud + GPU loop)

- **Claude Code API** → Main code generator
- **Code LLaMA Python 7B/34B** → Reviewer (AI/LLM specialist)
- **StarCoder 2 15B** → Reviewer / testing agent
- **Optional Local LLM on CPU** → Meta reasoning agent
- MCP (Multi-Agent Coding Loop) orchestrates interactions

Runs across:

- Local CPU agents  
- Vast.ai GPU agents (Code LLaMA, StarCoder)  
- Claude API agents  

---

## Features

- See [ROADMAP.md](ROADMAP.md)

---

## Approach

- Modular class-based agents
- CPU loop (Ollama)
- GPU loop (Vast.ai)
- Cloud APIs (Claude, OpenAI) — optional but supported
- MCP coordinates all agents (Claude + GPU + CPU)
- Focus on **adaptive loops** + learning from experience

---

## Sample Code

```bash
# Assume you are on Linux

# Install Python 3.10
sudo apt update
sudo apt install python3.10 python3.10-venv python3.10-dev python3.10-distutils

# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone this repo
git clone https://github.com/iptracej-education/multi-agent-coding-loop
cd multi-agent-coding-loop

# Setup UV
uv venv .venv
source .venv/bin/activate
uv pip install requests

# Install Ollama
curl https://ollama.com/install.sh | bash
ollama --version

# Check if Ollama is running
ps aux | grep -i ollama

# If not running:
ollama serve

# Pull Mistral 7B model (used in this sample)
ollama pull mistral

# Run the sample local CPU loop
uv run python loops/local_cpu_loop.py

# or

uv run python examples/local_cpu_loop_simple.py
```

---

### Coming soon

- Example configs for **Claude + GPU reviewers**
- Unified agent API for easy extension
- Data logging for fine-tuning local models

---

### License

MIT — open educational project.