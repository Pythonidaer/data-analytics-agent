# Learning Path

> Your guide from "I just bought this" to "I'm running a production agent."

---

## Where Are You Starting?

Before diving in, check your current level:

### Pre-Assessment

**1. Have you used the OpenAI/Anthropic API before?**
- [ ] No, just the ChatGPT/Claude interface → Start at Level 1
- [ ] Yes, made API calls → Start at Level 2
- [ ] Yes, with tools/function calling → Start at Level 3

**2. Can you run Python from the terminal?**
- [ ] No → [Complete this 15-min setup first](https://realpython.com/installing-python/)
- [ ] Yes → Continue

**3. Have you deployed a web app before?**
- [ ] No → That's fine, Week 2 covers this
- [ ] Yes → You'll move fast through Module 4

---

## The Capability Levels

| Level | Name | You Can... | Time to Reach |
|-------|------|------------|---------------|
| **1** | **Emerging** | Run the agent locally, ask questions | 30 minutes |
| **2** | **Developing** | Modify prompts, observe output changes | 2 hours |
| **3** | **Proficient** | Create custom tools, integrate data sources | 4 hours |
| **4** | **Advanced** | Deploy to production, monitor costs, iterate | 6 hours |

**Total time to Advanced: ~12 hours of focused work**

---

## Level 1: Emerging (30 minutes)

### Goal
Get the agent running locally and have a conversation with it.

### Steps
1. Clone the repository
2. Set up your environment (Python, Node.js)
3. Configure your API key
4. Run the backend
5. Run the frontend
6. Ask the agent a question

### Success Criteria
- [ ] Agent responds to your question
- [ ] You see the streaming response in your browser
- [ ] No error messages in the terminal

### Expected Output
```
You: "What is product positioning?"
Agent: [Provides a structured explanation using April Dunford's framework...]
```

### If You Get Stuck

| Problem | Solution |
|---------|----------|
| `ANTHROPIC_API_KEY not set` | Export your key: `export ANTHROPIC_API_KEY=sk-ant-...` |
| `Port 8123 already in use` | Kill the process: `lsof -ti:8123 | xargs kill` |
| `Module not found` | Activate venv: `source .venv/bin/activate` |
| Still stuck? | Email support (response within 48 hours) |

### You're Ready for Level 2 When...
- You can explain what happened when you asked the agent a question
- You understand: User → Frontend → Backend → Claude API → Response

---

## Level 2: Developing (2 hours)

### Goal
Modify a prompt and observe how the agent's behavior changes.

### Steps
1. Open `apps/agent/src/pmm_agent/prompts.py`
2. Read the `MAIN_SYSTEM_PROMPT`
3. Find the "Your Workflow" section
4. Add a new instruction (e.g., "Always ask 2 clarifying questions before providing analysis")
5. Restart the backend
6. Test the change with a query

### Success Criteria
- [ ] Agent behavior changed according to your modification
- [ ] You can predict how prompt changes affect output
- [ ] You understand the prompt structure

### Expected Output
```
# Before modification:
You: "Analyze Slack's positioning"
Agent: [Jumps straight into analysis]

# After modification:
You: "Analyze Slack's positioning"
Agent: "Before I analyze, let me ask:
1. What market segment are you targeting?
2. Who are you positioning against?"
```

### If You Get Stuck

| Problem | Solution |
|---------|----------|
| Changes not appearing | Make sure you restarted uvicorn |
| Agent ignoring instruction | Make instruction more explicit/prominent |
| Syntax error in Python | Check for matching quotes and proper indentation |
| Still stuck? | Check TROUBLESHOOTING.md |

### You're Ready for Level 3 When...
- You've made 3+ prompt modifications and observed changes
- You understand the MoE (Mixture of Experts) structure
- You can explain what each section of the prompt does

---

## Level 3: Proficient (4 hours)

### Goal
Create a custom tool that extends the agent's capabilities.

### Steps
1. Open `apps/agent/src/pmm_agent/tools/`
2. Study an existing tool (e.g., `analyze_product` in `intake.py`)
3. Identify ONE capability you want to add
4. Create a new tool following the pattern:
   - Define input schema
   - Write the docstring (this is what Claude reads)
   - Implement the logic
   - Return structured output
5. Register the tool in `agent.py`
6. Test the tool with a query that triggers it

### Success Criteria
- [ ] Your tool appears in the agent's tool list
- [ ] Agent correctly decides when to use your tool
- [ ] Tool returns structured, useful output

### Expected Output
```python
# Your new tool in tools/custom.py
@tool
def analyze_landing_page(url: str) -> dict:
    """
    Analyze a landing page for conversion optimization.

    Use this when a user wants feedback on their website
    or landing page effectiveness.
    """
    # Your implementation
    return {
        "headline_score": 7,
        "cta_analysis": "...",
        "recommendations": [...]
    }
```

### If You Get Stuck

| Problem | Solution |
|---------|----------|
| Tool not appearing | Check it's in the TOOLS list in agent.py |
| Agent not using tool | Improve the docstring—be more specific about when to use |
| Tool errors at runtime | Add try/except and log errors |
| Still stuck? | See EXERCISES.md Exercise 3 for detailed walkthrough |

### You're Ready for Level 4 When...
- You've created at least 1 custom tool
- You understand how Claude decides which tool to use
- You can explain the tool lifecycle: schema → docstring → invocation → response

---

## Level 4: Advanced (6 hours)

### Goal
Deploy your customized agent to production and set up monitoring.

### Steps
1. Choose your deployment target (Netlify recommended)
2. Follow DEPLOYMENT.md for your chosen platform
3. Set environment variables in production
4. Verify the deployment works
5. Set up cost monitoring (Anthropic dashboard)
6. Share your live URL

### Success Criteria
- [ ] Agent accessible at a public URL
- [ ] HTTPS enabled
- [ ] Can track API costs
- [ ] Agent handles errors gracefully

### Expected Output
```
Your agent: https://my-pmm-agent.netlify.app

Health check: curl https://my-pmm-agent.netlify.app/api/health
Response: {"status": "ok", "agent": "jai-agent-accelerator"}
```

### If You Get Stuck

| Problem | Solution |
|---------|----------|
| Build fails | Check Node.js version, check for missing dependencies |
| Function timeout | Netlify free tier = 10s limit. Upgrade or optimize |
| CORS errors | Check ALLOWED_ORIGINS environment variable |
| High costs | See ADVANCED.md for cost optimization patterns |
| Still stuck? | Book office hours (Pro tier) |

### You've Completed the Path When...
- [ ] Your agent is deployed and accessible
- [ ] You can explain the architecture to someone else
- [ ] You have a plan for iteration based on real usage
- [ ] You're ready for the showcase (see SHOWCASE.md)

---

## What's Next?

### Completed Level 4? Here's your path forward:

**1. Build Your Showcase**
- Document what you built in SHOWCASE.md format
- Share in Discord for feedback
- Add to your portfolio

**2. Go Deeper (Advanced Topics)**
- Multi-agent patterns
- RAG integration
- Cost optimization at scale
- See ADVANCED.md

**3. Join the Cohort Course**
- Live feedback from Jai
- Peer learning
- Structured 4-week progression
- Starts January 27, 2025

**4. Consider Team Access**
- 3 seats for your team
- Private Slack channel
- 1-hour onboarding call
- Quarterly roadmap reviews

---

## Time Estimates by Persona

| Persona | Time to Level 4 | Notes |
|---------|-----------------|-------|
| **PM with some coding** | 12-16 hours | Take your time on Level 3 |
| **Developer** | 6-8 hours | You'll fly through Levels 1-2 |
| **Founder (technical)** | 8-12 hours | Focus on Level 4 deployment |
| **Designer learning AI** | 16-20 hours | Extra time on Python basics |

---

## Need Help?

| Channel | Response Time | For |
|---------|---------------|-----|
| **TROUBLESHOOTING.md** | Instant | Common issues |
| **Discord Community** | Hours | Peer support |
| **Email Support** | 48 hours | Starter tier |
| **Priority Email** | 24 hours | Pro/Team tier |
| **Office Hours** | Weekly | Pro/Team tier |

---

[Back to README](../README.md) | [Exercises →](EXERCISES.md) | [Troubleshooting →](TROUBLESHOOTING.md)
