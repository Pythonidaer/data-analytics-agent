# Jai's Agent Accelerator

> **Build your first production AI agent this weekend.**

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start)
[![Powered by LangChain](https://img.shields.io/badge/Powered%20by-LangChain-blue)](https://langchain.com)

---

## Quick Start (10 minutes)

**New here?** → [First-Time Setup Guide](docs/FIRST_TIME_SETUP.md) has step-by-step instructions for your experience level.

Get the agent running locally in 4 steps.

### Prerequisites

- Python 3.11+ ([install](https://python.org))
- Node.js 18+ ([install](https://nodejs.org))
- Anthropic API key ([get one](https://console.anthropic.com))

### Step 1: Clone & Setup Backend

```bash
git clone https://github.com/chai-with-jai/jai-agent-accelerator.git
cd jai-agent-accelerator/apps/agent

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .

export ANTHROPIC_API_KEY=sk-ant-your-key-here
python -m uvicorn pmm_agent.server:app --host 0.0.0.0 --port 8123
```

### Step 2: Setup Frontend (New Terminal)

```bash
cd jai-agent-accelerator/apps/web
npm install
npm run dev
```

### Step 3: Use the Agent

Open [http://localhost:3003](http://localhost:3003)

Ask: "What is product positioning and why does it matter?"

### Step 4: Verify It Works

You should see a structured response explaining positioning using April Dunford's framework.

**Stuck?** → [Troubleshooting Guide](docs/TROUBLESHOOTING.md)

---

## What You'll Build

A production-ready AI agent that:

- **Analyzes products** and extracts value propositions
- **Researches competitors** and market positioning
- **Creates deliverables** (positioning statements, battlecards, messaging)
- **Validates decisions** with human-in-the-loop checkpoints

**The architecture:**
```
User Query → React Frontend → FastAPI Backend → Claude + Tools → Structured Output
```

---

## Your Learning Path

| Level | You Can... | Time |
|-------|------------|------|
| **Emerging** | Run agent locally, ask questions | 30 min |
| **Developing** | Modify prompts, observe changes | 2 hours |
| **Proficient** | Create custom tools | 4 hours |
| **Advanced** | Deploy to production | 6 hours |

**Total time to production: ~12 hours of focused work**

→ [Full Learning Path](docs/LEARNING_PATH.md)
→ [Exercises](docs/EXERCISES.md)

---

## Pre-Assessment: Where Are You Starting?

**Have you used the API before?**
- [ ] No, just ChatGPT/Claude interface → Start at Emerging
- [ ] Yes, made API calls → Start at Developing
- [ ] Yes, with tools/function calling → Start at Proficient

**Can you run Python from terminal?**
- [ ] No → [15-min Python setup first](https://realpython.com/installing-python/)
- [ ] Yes → Continue with Quick Start above

---

## Who This Is For

### Product Managers
Building AI features into your product? You need to understand what's possible and how to spec AI work.

**Before:** Copy-paste prompts, generic outputs that need heavy editing.
**After:** Working prototype you can demo, framework for speccing AI features.

### Product Marketing Managers
Drowning in positioning docs and battlecards? You want AI that understands PMM workflows.

**Before:** Start from scratch every time, hours editing generic outputs.
**After:** Agent that generates battlecards and positioning in YOUR voice.

### Founders & Solo Operators
Need PMM/PM output without hiring a team? You want to move fast with quality.

**Before:** Your "AI strategy" is copying prompts and hoping.
**After:** Production agent handling research and deliverables for YOUR startup.

### Designers Learning AI
Want to understand how AI products work? You know AI is changing design.

**Before:** Used ChatGPT but don't understand the architecture.
**After:** Practical experience building agents, framework for AI UX.

---

## The Story

I've taught hundreds of people to build AI agents. The pattern is always the same:

1. **Day 1:** "I made a ChatGPT wrapper!"
2. **Day 3:** "Why is the output so generic?"
3. **Day 7:** "How do I make it remember context?"
4. **Day 14:** "How do I know if it's actually good?"
5. **Day 30:** "Why can't I deploy this anywhere?"

This repo solves all of that. It's the system I use to prototype and productionize every agent—battle-tested with Claude, LangChain, and Netlify.

**My credentials:**
- Professional Agent Engineer (LLM observability & evaluations)
- 2 years teaching AI to non-technical people
- QEDC-validated methodology for real business outcomes
- Research documented at [pm-ai-lab.netlify.app](https://pm-ai-lab.netlify.app)

---

## What's Inside

### The Framework

```
jai-agent-accelerator/
├── apps/
│   ├── agent/                    # Python backend (LangChain + FastAPI)
│   │   └── src/pmm_agent/
│   │       ├── agent.py          # Agent factory with 5 operating modes
│   │       ├── prompts.py        # MoE methodology + 10 Giants framework
│   │       ├── server.py         # Production-ready FastAPI
│   │       └── tools/            # 15+ domain-specific tools
│   └── web/                      # React frontend (Vite + Tailwind)
├── config/domains/               # Domain configurations
└── docs/                           # Learning materials
    ├── FIRST_TIME_SETUP.md        # Setup by experience level
    ├── LEARNING_PATH.md           # Your progression guide
    ├── EXERCISES.md               # 5 progressive challenges
    ├── SHOWCASE.md                # Present your project
    ├── METHODOLOGY.md             # Mixture of Experts explained
    ├── CUSTOMIZATION.md           # Adapt for your domain
    ├── DEPLOYMENT.md              # 4 deployment options
    ├── TROUBLESHOOTING.md         # When things go wrong
    ├── BUILD_VS_BUY.md            # Infrastructure decisions
    ├── ARCHITECTURE_DECISIONS.md  # Productionization guide
    └── COST_OF_BUILDING.md        # Agent-native economics
```

### The Methodology: Mixture of Experts

Instead of one monolithic prompt, we decompose expertise into specialized sub-agents:

1. **Domain Decomposition** — Break complex domains into specialized experts
2. **Semantic Grounding** — Ground behavior in established frameworks
3. **Human-in-the-Loop** — Critical decisions require human approval
4. **Eval-Driven** — Every output is measurable and improvable
5. **Iterative Refinement** — Start rough, improve through feedback

### Standing on Giants

The agent's intelligence is grounded in 10 practitioners:

| Giant | Key Insight | Applied When |
|-------|-------------|--------------|
| Geoffrey Moore | The Chasm exists | Targeting segments |
| Clay Christensen | Jobs to Be Done | Understanding needs |
| April Dunford | Positioning is foundation | Before messaging |
| Marty Cagan | Discovery over delivery | Validating assumptions |
| Ash Maurya | Constraints are features | Prioritizing scope |
| Eric Ries | Build-Measure-Learn | Planning experiments |
| swyx | Evals are the new tests | Assessing quality |
| Harrison Chase | Tools extend capability | Orchestrating actions |
| Anthropic Team | Human-AI collaboration | Surfacing decisions |
| Rahul & Alex | Observability matters | Debugging outcomes |

→ [Full Methodology](docs/METHODOLOGY.md)

---

## Tools Reference

### Agent Modes

| Mode | Tools Available | Use Case |
|------|-----------------|----------|
| `full` | All 15+ tools | Complete workflow |
| `intake` | Product analysis | Understanding product |
| `research` | Competitive intel | Market analysis |
| `planning` | Positioning/messaging | Strategic deliverables |
| `risk` | Validation | Risk assessment |

### Available Tools

**Intake:** `analyze_product`, `extract_value_props`, `identify_icp`
**Research:** `search_competitors`, `analyze_pricing`, `fetch_url`, `analyze_reviews`
**Planning:** `create_positioning_statement`, `create_messaging_matrix`, `create_battlecard`, `create_launch_plan`
**Risk:** `assess_market_risks`, `validate_positioning`, `identify_gaps`

---

## Deployment

When you're ready to go live, choose your platform:

| Platform | Best For | Setup Time | Cost |
|----------|----------|------------|------|
| **Netlify** | Just works | 30 min | $0-25/mo |
| **Railway** | More control | 20 min | $5-20/mo |
| **Docker** | Self-hosted | 45 min | Your infra |
| **Vercel** | React apps | 25 min | $0-20/mo |

→ [Deployment Guide](docs/DEPLOYMENT.md)
→ [Build vs Buy](docs/BUILD_VS_BUY.md)
→ [Architecture Decisions](docs/ARCHITECTURE_DECISIONS.md) (when you're ready to scale)
→ [Cost of Building](docs/COST_OF_BUILDING.md) (agent-native vs. traditional teams)

---

## Pricing & Support

This is a premium product sold on [LemonSqueezy](https://chaiwithjai.lemonsqueezy.com).

| Tier | Price | Includes |
|------|-------|----------|
| **Starter** | $497 | Source code + docs + 30-day email support |
| **Pro** | $997 | + Video modules + Office hours + Priority support |
| **Team** | $1,997 | + 3 seats + Private Slack + Onboarding call |

### What's in Each Tier

**Starter ($497):**
- Complete source code (MIT licensed)
- All documentation (Learning Path, Exercises, etc.)
- 4 deployment guides
- 30-day email support
- Lifetime updates

**Pro ($997):**
Everything in Starter, plus:
- 5+ hours of self-paced video
- Monthly office hours access
- Priority email support (24-hour response)
- Maven cohort waitlist priority

**Team ($1,997):**
Everything in Pro, plus:
- 3 team seats
- Private Slack channel
- 1-hour onboarding call
- Quarterly roadmap review

### Cohort Course

Want live instruction? Join my **cohort-based course starting January 27, 2025**.

4 weeks, 8 sessions, working agent at the end.

[Learn more →](https://chaiwithjai.com/course)

---

## FAQ

**Do I need to code?**
You should be comfortable reading Python and terminal commands. Not senior developer level, but not no-code either.

**What about OpenAI/GPT-4?**
Uses Claude, but patterns work with any model. LangChain layer makes swapping models easy.

**How much does it cost to run?**
$30-50/month in API costs at typical usage.

**Can I use this for client work?**
Yes. MIT licensed. Build products, deliver client projects, sell what you create.

**Refund policy?**
30-day money-back guarantee. No questions asked.

---

## Get Help

| Channel | Response Time | For |
|---------|---------------|-----|
| [Troubleshooting](docs/TROUBLESHOOTING.md) | Instant | Common issues |
| Discord | Hours | Peer support |
| Email | 48 hours | Starter tier |
| Priority Email | 24 hours | Pro/Team |
| Office Hours | Weekly | Pro/Team |

---

## Author

**Jai Bhagat** — Agent Engineer & Educator

- LLM Observability & Evaluations (via LangChain)
- Prototype → Production Framework (Claude + Netlify)
- 2 Years Teaching AI to Non-Technical People
- QEDC-Validated Methodology

[chaiwithjai.com](https://chaiwithjai.com)

---

## License

MIT License — see [LICENSE](LICENSE)

---

Built with [LangChain](https://langchain.com), [Claude](https://anthropic.com), and [Netlify](https://netlify.com)
