# Local Setup Checklist - Data Analytics Agent

> Track your progress getting the agent running locally before domain conversion

## Prerequisites Check

- [x] Python 3.11+ installed (`python3 --version`)
- [x] Node.js 18+ installed (`node --version`)
- [x] Git installed (`git --version`)
- [x] Anthropic API key obtained ([console.anthropic.com](https://console.anthropic.com))

## Backend Setup

- [x] Navigate to `apps/agent` directory
- [x] Create virtual environment: `python3 -m venv .venv`
- [x] Activate virtual environment: `source .venv/bin/activate` (Mac/Linux) or `.venv\Scripts\activate` (Windows)
- [x] Install dependencies: `pip install -e .`
- [x] Set API key: `export ANTHROPIC_API_KEY=sk-ant-your-key-here`
- [x] Start backend: `python3 -m uvicorn src.pmm_agent.server:app --port 8123`
- [x] Verify backend health: `curl http://localhost:8123/health` returns `{"status": "ok"}`

## Frontend Setup

- [x] Navigate to `apps/web` directory (in new terminal)
- [x] Install dependencies: `npm install`
- [x] Start frontend: `npm run dev`
- [x] Verify frontend loads at `http://localhost:3003`

## Initial Testing

- [x] Open browser to `http://localhost:3003`
- [x] Ask agent: "What is product positioning and why does it matter?"
- [x] Verify streaming response appears
- [x] Verify no errors in browser console (Cmd+Option+J on Mac)
- [x] Verify no errors in backend terminal

## Ready for Domain Conversion

- [x] Backend running and responding
- [x] Frontend running and displaying chat interface
- [x] Can have conversation with PMM agent
- [x] Tool calls appear in UI when triggered
- [x] All checks above completed ✅

---

**Next Steps:** Once all checks are complete, we'll proceed with Exercise 5: Domain Conversion (PMM → Data Analytics)

