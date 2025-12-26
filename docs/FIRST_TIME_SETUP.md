# First-Time Setup Guide

> Getting started without the footguns.

This guide walks you through setting up the Data Analytics Expert Agent. We've tested this on fresh machines and documented every gotcha so you don't have to discover them yourself.

**Note:** This project is configured for the Data Analytics domain. To use the PMM agent, set `DOMAIN=pmm` in your `.env` file.

---

## Find Your Path

**What's your relationship with the terminal?**

| If you... | You are... | Go to... |
|-----------|------------|----------|
| Avoid it whenever possible | **Path A: PM/Designer** | [Path A](#path-a-pmdesigner) |
| Use it but don't love it | **Path B: Technical PM/Founder** | [Path B](#path-b-technical-pmfounder) |
| Live in it daily | **Path C: Developer** | [Path C](#path-c-developer) |

---

## Path A: PM/Designer

**Time estimate:** 45-60 minutes (includes installing prerequisites)

**Mindset:** We're going to install some tools, copy-paste some commands, and get this running. You don't need to understand everything—just follow the steps.

### Step 0: Check What You Have

Open Terminal (Mac: Cmd+Space, type "Terminal") or Command Prompt (Windows: search "cmd").

Copy-paste these commands one at a time:

```bash
python3 --version
```
**Good:** `Python 3.11.x` or higher
**Bad:** `command not found` or `Python 3.9.x` → Go to [Install Python](#install-python)

```bash
node --version
```
**Good:** `v18.x.x` or higher
**Bad:** `command not found` or `v16.x.x` → Go to [Install Node](#install-node)

```bash
git --version
```
**Good:** `git version 2.x.x`
**Bad:** `command not found` → Go to [Install Git](#install-git)

### Step 1: Get an API Key

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in
3. Click "Get API Keys" in the left sidebar
4. Click "Create Key"
5. Name it "data-analytics-agent" (or any name you prefer - this is just for your reference)
6. **Copy the key immediately** — you won't see it again

**The key looks like:** `sk-ant-api03-xxxxxxxxxxxxx`

**Footgun:** If you close the popup before copying, you'll need to create a new key.

### Step 2: Download the Code

```bash
cd ~/Desktop
git clone <your-repo-url>
cd data-analytics-agent
```

**Note:** Replace `<your-repo-url>` with your actual repository URL.

**Footgun:** If you get "Permission denied," make sure you have access to the repository.

### Step 3: Set Up the Backend

```bash
cd apps/agent
python3 -m venv .venv
```

**Note:** If you see a `.env.example` file, you can copy it to `.env` later to set your environment variables easily.

**Now activate the virtual environment:**

**Mac/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

You should see `(.venv)` appear at the start of your terminal line.

**Footgun:** If you see "cannot be loaded because running scripts is disabled" on Windows:
1. Open PowerShell as Administrator
2. Run: `Set-ExecutionPolicy RemoteSigned`
3. Try again

**Install the packages:**
```bash
pip install -e .
```

This takes 2-3 minutes. You'll see a lot of text scrolling by. That's normal.

**Footgun:** If you see red error text about "Microsoft Visual C++":
1. Download [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. Install "Desktop development with C++"
3. Restart your terminal and try again

### Step 4: Set Your API Key

**Option 1: Using .env file (Recommended)**

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API key
# On Mac/Linux:
nano .env
# On Windows:
notepad .env

# Add this line (replace with your actual key):
# ANTHROPIC_API_KEY=sk-ant-your-key-here
# DOMAIN=data_analytics
```

**Option 2: Export in terminal**

**Mac/Linux:**
```bash
export ANTHROPIC_API_KEY=sk-ant-your-key-here
export DOMAIN=data_analytics
```

**Windows (Command Prompt):**
```bash
set ANTHROPIC_API_KEY=sk-ant-your-key-here
set DOMAIN=data_analytics
```

**Windows (PowerShell):**
```bash
$env:ANTHROPIC_API_KEY="sk-ant-your-key-here"
$env:DOMAIN="data_analytics"
```

**Footgun:** Replace `sk-ant-your-key-here` with YOUR actual key from Step 1.

**Footgun:** The `.env` file method persists across terminal sessions. Export method only lasts for this session.

### Step 5: Start the Backend

```bash
python3 -m uvicorn src.pmm_agent.server:app --port 8123
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8123
INFO:     Application startup complete.
```

**Keep this terminal open.** Don't close it.

**Footgun:** If you see "Address already in use":
```bash
lsof -ti:8123 | xargs kill  # Mac/Linux
# Then try the uvicorn command again
```

### Step 6: Set Up the Frontend

**Open a NEW terminal window** (Cmd+T on Mac, or open Terminal again).

```bash
cd ~/Desktop/data-analytics-agent/apps/web
npm install
```

This takes 1-2 minutes.

**Footgun:** If you see "npm: command not found," you need to [install Node](#install-node).

```bash
npm run dev
```

You should see:
```
VITE v5.x.x ready in xxx ms
➜  Local:   http://localhost:3003/
```

### Step 7: Use Your Agent

1. Open [http://localhost:3003](http://localhost:3003) in your browser
2. You should see the **Data Analytics Expert Agent** with blue/cyan theme
3. Try a quick action like "Create a metrics dictionary"
4. Or ask: "Help me define KPIs for user activation"

**You're running a production-grade AI agent configured for data analytics.**

### If Something Went Wrong

| Symptom | Fix |
|---------|-----|
| "Connection refused" in browser | Is the backend still running? Check that first terminal. |
| "API key invalid" | Re-set your API key (Step 4). Make sure no extra spaces. |
| Blank screen | Check browser console (Cmd+Option+J on Mac) for errors. |
| Everything broke | Close both terminals. Start over from Step 3. |

**Still stuck?** Email support with:
1. Screenshot of the error
2. Which step you're on
3. Mac or Windows

---

## Path B: Technical PM/Founder

**Time estimate:** 20-30 minutes

**Mindset:** You can follow CLI instructions but don't want to debug obscure issues. Let's get you running fast.

### Prerequisites Checklist

```bash
python3 --version  # Need 3.11+
node --version     # Need 18+
git --version      # Need 2.0+
```

**If any are missing:** [Installation links](#installing-prerequisites)

### Quick Setup

```bash
# Clone
git clone <your-repo-url>
cd data-analytics-agent

# Backend
cd apps/agent
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
# Set up .env file (recommended)
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY and DOMAIN=data_analytics

# Or export directly
export ANTHROPIC_API_KEY=sk-ant-your-key
export DOMAIN=data_analytics
python3 -m uvicorn src.pmm_agent.server:app --port 8123

# Frontend (new terminal)
cd apps/web
npm install
npm run dev

# Open http://localhost:3003
```

### Common Footguns (and Fixes)

| Footgun | Prevention |
|---------|------------|
| Forgot to activate venv | `source .venv/bin/activate` before pip commands |
| API key not persisting | Add to `~/.zshrc` or `~/.bashrc` |
| Port 8123 in use | `lsof -ti:8123 | xargs kill` |
| npm can't find modules | Delete `node_modules`, run `npm install` again |
| CORS errors | Backend must be on 0.0.0.0, not 127.0.0.1 |

### Persistence (Don't Lose Your API Key)

Add to your shell config:

```bash
# ~/.zshrc or ~/.bashrc
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Then:
```bash
source ~/.zshrc  # or ~/.bashrc
```

### Next Steps

- [Exercises](EXERCISES.md) — Build your skills
- [Deployment](DEPLOYMENT.md) — Go live with Netlify
- [Architecture Decisions](ARCHITECTURE_DECISIONS.md) — When you're ready to productionize

---

## Path C: Developer

**Time estimate:** 10-15 minutes

**Mindset:** You know what you're doing. Here's the minimal path.

### TL;DR

```bash
git clone <your-repo-url> && cd data-analytics-agent

# Backend
cd apps/agent && python3 -m venv .venv && source .venv/bin/activate && pip install -e .
cp .env.example .env
# Edit .env with your ANTHROPIC_API_KEY and DOMAIN=data_analytics
# Or: export ANTHROPIC_API_KEY=sk-ant-xxx && export DOMAIN=data_analytics
python3 -m uvicorn src.pmm_agent.server:app --port 8123 &

# Frontend
cd ../web && npm i && npm run dev

# Done: http://localhost:3003
```

### Architecture Quick Reference

```
apps/agent/src/pmm_agent/
├── agent.py     # LangGraph agent factory, domain switching
├── prompts.py   # PMM prompts (legacy)
├── server.py    # FastAPI, /chat and /chat/stream, /config
├── domains/
│   └── data_analytics/
│       ├── prompts.py   # Analytics system + specialist prompts
│       └── tools/       # Analytics tools (intake, research, planning, risk)
└── tools/       # PMM tools (legacy)

apps/web/        # React + Vite + Tailwind, domain-aware frontend
config/domains/  # Domain configurations (data_analytics.json)
```

### For Productionization

You're probably considering:
- **Netlify** → [One-click deploy](DEPLOYMENT.md#option-1-netlify-recommended)
- **Railway** → [Docs](https://docs.railway.app/quick-start)
- **AWS/GCP** → [Architecture Decisions](ARCHITECTURE_DECISIONS.md)

Don't over-engineer. Start with Netlify, optimize later.

### Skip to Advanced

- [Architecture Decisions](ARCHITECTURE_DECISIONS.md) — Backend patterns, scaling
- [Customization](CUSTOMIZATION.md) — Domain conversion
- [Methodology](METHODOLOGY.md) — MoE patterns

---

## Installing Prerequisites

### Install Python

**Mac:**
```bash
brew install python@3.11
```

No Homebrew? First:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Windows:**
1. Download from [python.org](https://python.org/downloads/)
2. **Check "Add Python to PATH"** during installation
3. Restart terminal

**Footgun:** On Windows, make sure to check "Add Python to PATH" or nothing will work.

### Install Node

**Mac:**
```bash
brew install node@18
```

**Windows:**
1. Download from [nodejs.org](https://nodejs.org/) (LTS version)
2. Run installer with defaults
3. Restart terminal

### Install Git

**Mac:**
```bash
xcode-select --install
```
Click "Install" when prompted.

**Windows:**
1. Download from [git-scm.com](https://git-scm.com/download/win)
2. Run installer with defaults
3. Restart terminal

---

## Environment-Specific Gotchas

### Mac (Apple Silicon M1/M2/M3)

Some Python packages need Rosetta. If you see architecture errors:

```bash
# Install Rosetta
softwareupdate --install-rosetta

# Or force x86 Python
arch -x86_64 pip install -e .
```

### Mac (Intel)

Usually works without issues. If you have old Python versions:

```bash
# Check which Python
which python3  # Should be /usr/local/bin/python3 or /opt/homebrew/bin/python3

# If it's /usr/bin/python3, that's the system Python. Install a newer one.
```

### Windows 10/11

**Footgun:** Windows Defender might block Python. Add an exception:
1. Settings → Windows Security → Virus & threat protection
2. Manage settings → Exclusions → Add exclusion
3. Add your project folder

**Footgun:** Use PowerShell or Git Bash, not Command Prompt. More things will work.

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip nodejs npm git
```

### WSL2 (Windows Subsystem for Linux)

Best of both worlds. Follow Linux instructions inside WSL.

```bash
# Install WSL2 first (PowerShell as Admin)
wsl --install

# Then open Ubuntu and follow Linux setup
```

---

## Verification Checklist

Run through this before saying "it's working":

| Check | Command | Expected |
|-------|---------|----------|
| Backend running | `curl http://localhost:8123/health` | `{"status": "ok"...}` |
| Frontend running | Open http://localhost:3003 | See analytics agent interface (blue theme) |
| Agent responds | Ask a question | See streaming response |
| Domain correct | `curl http://localhost:8123/config` | `{"domain": "data_analytics"...}` |
| Tools working | Use "Create a metrics dictionary" quick action | See structured output |

---

## Time Budget by Persona

| Persona | Fresh Machine | Prerequisites Ready |
|---------|---------------|---------------------|
| PM/Designer | 60 min | 30 min |
| Technical PM | 30 min | 15 min |
| Developer | 15 min | 10 min |

**These are realistic times.** If you're spending more, something went wrong—check the troubleshooting or email support.

---

## What's Next

| You finished setup. Now... | Go to... |
|----------------------------|----------|
| Learn by doing | [Exercises](EXERCISES.md) |
| Modify the agent | [Learning Path](LEARNING_PATH.md) |
| Deploy to the internet | [Deployment](DEPLOYMENT.md) |
| Understand the architecture | [Architecture Decisions](ARCHITECTURE_DECISIONS.md) |

---

[← Back to README](../README.md) | [Learning Path →](LEARNING_PATH.md) | [Troubleshooting →](TROUBLESHOOTING.md)
