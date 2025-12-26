# Exercises

> Five progressive challenges to build your agent skills.

Each exercise builds on the previous one. Complete them in order.

---

## Exercise 1: Hello, Agent (15 minutes)

**Level:** Emerging
**Goal:** Get the agent running and have a conversation.

### Your Task

1. Follow the Quick Start in README.md
2. Ask the agent: "What is product positioning and why does it matter?"
3. Screenshot the response
4. Post in Discord: "Exercise 1 complete! My first agent response."

### Success Criteria

- [ ] Agent is running at `http://localhost:3003`
- [ ] You received a structured response about positioning
- [ ] The response mentions April Dunford or competitive alternatives

### Expected Output

The agent should explain positioning as:
- Competitive context (not aspiration)
- Foundation for messaging
- Includes: target customer, competitive alternative, key differentiator

### If Stuck

```bash
# Common fix: API key not set
export ANTHROPIC_API_KEY=sk-ant-your-key-here

# Common fix: Port in use
lsof -ti:8123 | xargs kill

# Then restart
python -m uvicorn pmm_agent.server:app --host 0.0.0.0 --port 8123
```

---

## Exercise 2: Prompt Surgery (30 minutes)

**Level:** Developing
**Goal:** Modify the agent's behavior through prompt engineering.

### Your Task

1. Open `apps/agent/src/pmm_agent/prompts.py`
2. Find the section that defines the agent's communication style
3. Add this instruction:

```python
## Clarification Protocol
Before providing any analysis:
1. Identify the most critical unknown
2. Ask ONE targeted clarifying question
3. Wait for the answer before proceeding
```

4. Restart the backend
5. Test with: "Help me position my SaaS product"
6. Verify the agent asks a clarifying question before analyzing

### Success Criteria

- [ ] Agent asks a clarifying question before analysis
- [ ] Question is targeted and useful (not generic)
- [ ] After you answer, agent provides relevant analysis

### Expected Output

```
You: "Help me position my SaaS product"

Agent: "Before I help with positioning, I need to understand one thing:
What are your customers using today before they find your product?
This helps me identify the competitive alternative we're positioning against."

You: "They're using spreadsheets and email"

Agent: "Got it. Let me analyze your positioning against spreadsheets/email as the competitive alternative..."
```

### If Stuck

- **Agent ignoring instruction?** Place it earlier in the prompt (before Phase 1)
- **Syntax error?** Check for proper Python string formatting
- **Changes not appearing?** Make sure you restarted uvicorn

### Bonus Challenge

Add a second behavior: Make the agent always end with "What would you like to explore next?"

---

## Exercise 3: Build Your First Tool (1 hour)

**Level:** Proficient
**Goal:** Create a custom tool that extends the agent.

### Your Task

Create a tool that calculates a "positioning readiness score" based on inputs.

1. Create a new file: `apps/agent/src/pmm_agent/tools/scoring.py`

2. Add this code:

```python
"""
Positioning Readiness Scoring Tool.

Calculates how ready a product is for positioning work.
"""

from langchain_core.tools import tool
from pydantic import BaseModel, Field
from typing import List


class ReadinessScore(BaseModel):
    """Structured readiness assessment output."""
    score: int = Field(description="Readiness score 1-10")
    strengths: List[str] = Field(description="What's ready")
    gaps: List[str] = Field(description="What's missing")
    next_action: str = Field(description="Most important next step")


@tool
def calculate_positioning_readiness(
    has_target_customer: bool,
    has_competitive_alternative: bool,
    has_key_differentiator: bool,
    has_customer_proof: bool,
    has_clear_category: bool,
) -> ReadinessScore:
    """
    Calculate how ready a product is for positioning work.

    Use this when a user wants to assess if they're ready
    to create positioning, or what gaps they need to fill first.

    Args:
        has_target_customer: Do they know their ideal customer?
        has_competitive_alternative: Do they know what customers use instead?
        has_key_differentiator: Do they have a unique capability?
        has_customer_proof: Do they have customer evidence/testimonials?
        has_clear_category: Do they know their market category?

    Returns:
        Readiness score with strengths, gaps, and next action
    """
    checks = {
        "Target Customer Definition": has_target_customer,
        "Competitive Alternative Identified": has_competitive_alternative,
        "Key Differentiator Articulated": has_key_differentiator,
        "Customer Proof Available": has_customer_proof,
        "Market Category Defined": has_clear_category,
    }

    strengths = [k for k, v in checks.items() if v]
    gaps = [k for k, v in checks.items() if not v]
    score = len(strengths) * 2  # 0-10 scale

    # Determine next action based on gaps
    if not has_target_customer:
        next_action = "Define your target customer segment first"
    elif not has_competitive_alternative:
        next_action = "Identify what customers use before finding you"
    elif not has_key_differentiator:
        next_action = "Articulate what you have that alternatives don't"
    elif not has_customer_proof:
        next_action = "Collect customer testimonials and use cases"
    elif not has_clear_category:
        next_action = "Define your market category"
    else:
        next_action = "You're ready to create positioning!"

    return ReadinessScore(
        score=score,
        strengths=strengths,
        gaps=gaps,
        next_action=next_action,
    )


# Export for agent
SCORING_TOOLS = [calculate_positioning_readiness]
```

3. Register the tool in `apps/agent/src/pmm_agent/agent.py`:

```python
from pmm_agent.tools.scoring import SCORING_TOOLS

# Add to your tools list
tools = INTAKE_TOOLS + RESEARCH_TOOLS + PLANNING_TOOLS + SCORING_TOOLS
```

4. Restart the backend

5. Test with: "Am I ready to create positioning? I have a target customer and key differentiator, but no customer proof yet."

### Success Criteria

- [ ] Tool appears in the agent's available tools
- [ ] Agent correctly decides to use the tool based on your query
- [ ] Tool returns structured output with score, strengths, gaps
- [ ] Agent interprets the result conversationally

### Expected Output

```
You: "Am I ready to create positioning? I have a target customer
and key differentiator, but no customer proof yet."

Agent: [Uses calculate_positioning_readiness tool]

"Based on your positioning readiness assessment:

**Score: 4/10**

**Strengths:**
- Target Customer Definition
- Key Differentiator Articulated

**Gaps:**
- Competitive Alternative Identified
- Customer Proof Available
- Market Category Defined

**Recommended Next Step:**
Identify what customers use before finding you. Understanding
the competitive alternative is essential for strong positioning.

Would you like help identifying competitive alternatives?"
```

### If Stuck

- **Tool not appearing?** Check the import path is correct
- **Agent not using tool?** Improve the docstring to be more specific
- **Type errors?** Ensure Pydantic model fields match return values

---

## Exercise 4: Deploy to Production (45 minutes)

**Level:** Advanced
**Goal:** Get your agent live on the internet.

### Your Task

Deploy to Netlify (recommended for simplicity).

1. Ensure you have a GitHub account with your repo

2. Install Netlify CLI:
```bash
npm install -g netlify-cli
netlify login
```

3. Create `netlify.toml` in project root (see DEPLOYMENT.md)

4. Create the function wrapper (see DEPLOYMENT.md)

5. Deploy:
```bash
netlify init
netlify env:set ANTHROPIC_API_KEY sk-ant-your-key
netlify deploy --prod
```

6. Verify:
```bash
curl https://your-site.netlify.app/api/health
```

7. Share your URL in Discord: "Exercise 4 complete! My agent is live at [URL]"

### Success Criteria

- [ ] Agent accessible at public URL
- [ ] HTTPS enabled (automatic with Netlify)
- [ ] Health check returns `{"status": "ok"}`
- [ ] Can have a conversation through the web interface

### Expected Output

```bash
$ curl https://your-pmm-agent.netlify.app/api/health
{"status": "ok", "agent": "jai-agent-accelerator", "version": "1.0.0"}
```

### If Stuck

| Problem | Solution |
|---------|----------|
| Build fails | Check `package.json` and `pyproject.toml` are valid |
| Function not found | Verify `netlify.toml` paths are correct |
| Environment variable missing | Use `netlify env:list` to check |
| Timeout errors | Netlify free tier = 10s limit |

### Bonus Challenge

Set up a custom domain: `my-agent.yourdomain.com`

---

## Exercise 5: Domain Conversion (2 hours)

**Level:** Advanced
**Goal:** Convert the PMM agent to YOUR domain.

### Your Task

Transform the agent for a domain you care about.

**Example domains:**
- Sales Enablement
- Customer Success
- Content Marketing
- HR/People Ops
- Legal Operations
- Finance/FP&A

1. Create new domain config: `config/domains/your-domain.json`
2. Identify 3-5 experts for your domain
3. Create 3+ custom tools specific to your domain
4. Write domain-specific prompts with expert knowledge
5. Update the frontend quick actions
6. Deploy the customized agent

### Success Criteria

- [ ] Agent responds with domain-specific expertise
- [ ] At least 3 custom tools working
- [ ] Quick actions match your domain
- [ ] Can explain the "Giants" for your domain

### Template: Domain Configuration

```json
{
  "domain": "your-domain",
  "name": "Your Domain Agent",
  "description": "AI agent for [your domain] workflows",

  "experts": [
    {
      "id": "expert_1",
      "name": "Expert Role 1",
      "focus": "What this expert knows"
    }
  ],

  "tools": {
    "intake": ["tool_1", "tool_2"],
    "research": ["tool_3"],
    "planning": ["tool_4", "tool_5"],
    "risk": ["tool_6"]
  },

  "frameworks": [
    {
      "name": "Framework Name",
      "applied_when": "When to use this framework"
    }
  ],

  "quick_actions": [
    {
      "label": "Action Label",
      "message": "What to send to agent",
      "icon": "emoji"
    }
  ]
}
```

### Expected Output

Your agent should:
- Use terminology from your domain
- Reference frameworks experts in your domain actually use
- Provide outputs in formats your domain uses
- Make decisions the way practitioners in your domain think

### If Stuck

See CUSTOMIZATION.md for the full domain conversion guide.

---

## Completion Checklist

| Exercise | Time | Status |
|----------|------|--------|
| 1. Hello, Agent | 15 min | ☐ |
| 2. Prompt Surgery | 30 min | ☐ |
| 3. Build Your First Tool | 1 hour | ☐ |
| 4. Deploy to Production | 45 min | ☐ |
| 5. Domain Conversion | 2 hours | ☐ |

**Total: ~5 hours of hands-on work**

---

## What's Next?

Completed all exercises?

1. **Create your showcase** → See SHOWCASE.md
2. **Go deeper** → See ADVANCED.md
3. **Get feedback** → Join office hours (Pro tier)
4. **Join the cohort** → January 27, 2025

---

[← Learning Path](LEARNING_PATH.md) | [Showcase →](SHOWCASE.md) | [Advanced →](ADVANCED.md)
