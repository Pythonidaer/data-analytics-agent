# Showcase Your Agent

> Turn your project into a portfolio piece.

You built an agent. Now let's document it so others can see what you learned.

---

## The Showcase Template

Copy this template and fill in your details.

```markdown
# [Your Project Name]

## Headline
I built a [TYPE] that helps [AUDIENCE] do [OUTCOME].

Example: "I built a sales enablement agent that helps reps find the right content 5x faster."

---

## The Problem (3-5 sentences)

What was broken before this existed?

- Who experiences the problem
- What they were doing before (the workaround)
- Why that workaround was painful
- Any numbers that show the scale

---

## The Solution (3-5 sentences)

What does your agent do?

- Core capability
- Key differentiator
- Architecture choice (MoE, tools, human-in-loop)

---

## The Stack

- **Backend:** [Python, FastAPI, LangChain, LangGraph]
- **Frontend:** [React, TypeScript, Vite]
- **Model:** [Claude, GPT-4, etc.]
- **Deployment:** [Netlify, Railway, etc.]

---

## Key Learnings (3-5 bullets)

What did you learn building this?

-
-
-

---

## Demo

🔗 [Live URL](https://your-agent.netlify.app)

📸 Screenshot:
[Insert screenshot of key interaction]

Optional: 2-minute Loom walkthrough

---

## What's Next

Where are you taking this?

-
-
```

---

## Example Showcase

### PMM Intelligence Agent

**Headline:**
I built a PMM intelligence agent that helps product marketers create positioning statements in 30 minutes instead of 3 days.

**The Problem:**
Product marketing teams spend 2-3 days creating positioning statements. They interview stakeholders, research competitors, and iterate through multiple drafts. Most of that time is spent on information gathering, not strategic thinking. When they use ChatGPT, they get generic outputs that need heavy editing.

**The Solution:**
This agent uses a Mixture of Experts architecture—specialized sub-agents for competitive analysis, positioning strategy, and messaging development. It's grounded in April Dunford's Obviously Awesome framework, so outputs match what practitioners actually use. Human-in-the-loop checkpoints ensure strategic decisions get human approval.

**The Stack:**
- **Backend:** Python, FastAPI, LangChain, LangGraph
- **Frontend:** React, TypeScript, Vite
- **Model:** Claude 3.5 Sonnet
- **Deployment:** Netlify (serverless functions)

**Key Learnings:**
- Decomposing expertise into specialized agents beats one monolithic prompt
- The tool docstring IS the prompt—Claude reads it to decide when to call
- Structured outputs (Pydantic models) reduce editing time by 80%
- Human-in-loop isn't a limitation, it's a trust-building feature

**Demo:**
🔗 [my-pmm-agent.netlify.app](https://my-pmm-agent.netlify.app)

**What's Next:**
Adding RAG integration for internal documentation and expanding to sales enablement domain.

---

## Showcase Formats

### 1. Portfolio Page
Full showcase for personal site, Notion, or LinkedIn article.

**Length:** 500-800 words
**Includes:** All sections above

### 2. LinkedIn Post
Short version for social sharing.

**Length:** 250 words max
**Format:**
```
I built [THING] that helps [AUDIENCE] do [OUTCOME].

The problem: [2 sentences]

What I learned building it:
• [Learning 1]
• [Learning 2]
• [Learning 3]

Try it: [URL]

Built with #LangChain #Claude #AI
```

### 3. README Section
For adding to your project's README.

**Length:** 150 words
**Format:**
```markdown
## What I Built

[Headline]

### Problem
[2 sentences]

### Solution
[3 sentences including architecture]

### Demo
[Screenshot + URL]
```

### 4. Slide Deck (5 slides)

| Slide | Content |
|-------|---------|
| 1 | Headline + screenshot |
| 2 | Problem + before/after |
| 3 | Solution + architecture diagram |
| 4 | Key learnings (3 bullets) |
| 5 | Demo link + what's next |

---

## What NOT to Include

### Code
- No function implementations
- No prompt text (that's the IP)
- No tool logic
- No configuration values

### Secrets
- No API keys (even examples that look real)
- No internal URLs
- No database connection strings

### Business Logic
- No pricing algorithms
- No competitive analysis details
- No customer data

### Safe Alternatives

Instead of showing code, describe patterns:

| Don't Say | Say Instead |
|-----------|-------------|
| "Here's my prompt..." | "Uses structured outputs with Pydantic models" |
| "My tool does X by..." | "Implements a tool-calling pattern for extensibility" |
| "The algorithm works by..." | "Follows human-in-loop for approval workflows" |

---

## Self-Assessment Rubric

Before sharing your showcase, check these:

### Content Quality
- [ ] Headline clearly states what + who + outcome
- [ ] Problem is specific (not "AI is hard")
- [ ] Solution mentions architecture choice
- [ ] Learnings are specific (not "AI is powerful")
- [ ] Demo link works

### Presentation
- [ ] Screenshot shows the agent in action
- [ ] Text is scannable (headers, bullets)
- [ ] No typos or broken links

### Privacy
- [ ] No API keys or secrets visible
- [ ] No internal business logic exposed
- [ ] No customer data visible
- [ ] No proprietary prompts shared

---

## Sharing Your Showcase

### Where to Post

1. **Discord** — Share with the community for feedback
2. **LinkedIn** — Professional network visibility
3. **Personal Site** — Portfolio piece
4. **GitHub README** — Project documentation
5. **Twitter/X** — Quick demo + learnings

### When to Share

- After completing Exercise 5
- When you have a working deployment
- When you're ready for feedback

### Getting Feedback

Post in Discord with:
1. Your showcase (link or inline)
2. Specific question: "Does my problem statement resonate?" or "Is my demo clear?"
3. Context: "I'm targeting PMMs" or "This is for my portfolio"

---

## Showcase Gallery

*Coming soon: Featured showcases from the community.*

Want to be featured? Share your showcase in Discord with #showcase.

---

[← Exercises](EXERCISES.md) | [Advanced →](ADVANCED.md) | [Back to README](../README.md)
