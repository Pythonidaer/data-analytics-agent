# The Cost of Building

> Agent-native development vs. traditional teams.

This document compares the old way of building software with the new agent-assisted model. The economics have fundamentally shifted.

---

## The Shift

**Old model:** Hire engineers to write code.
**New model:** Guide agents to write code, review their output.

The cost of *writing* code is approaching zero. The cost of *deciding what to build* and *reviewing quality* remains.

---

## Cost Comparison

### Traditional Team (2020-2023 Model)

Building a production AI agent like this one:

| Role | Count | Annual Salary | Monthly Cost |
|------|-------|---------------|--------------|
| Senior Engineer | 1 | $180,000 | $15,000 |
| Mid Engineer | 1-2 | $130,000 | $10,800 |
| Junior Engineer | 1 | $85,000 | $7,100 |
| Designer | 0.5 | $120,000 | $5,000 |
| PM | 0.5 | $140,000 | $5,800 |
| DevOps | 0.5 | $150,000 | $6,300 |
| **Total** | **4-6 FTE** | | **$50,000/month** |

**Timeline:** 3-6 months to MVP
**Total to MVP:** $150,000 - $300,000

**Ongoing:** $50,000/month for maintenance and iteration

---

### Agent-Native Development (2024+ Model)

Same production AI agent:

| Component | Monthly Cost | Notes |
|-----------|--------------|-------|
| Claude API (coding) | $150-250 | Claude Code, Cursor, etc. |
| Claude API (runtime) | $30-50 | Agent serving users |
| Hosting (Netlify Pro) | $19 | Or Railway ~$20 |
| Human oversight | 20 hrs @ $100/hr* | Review, direction, decisions |
| **Total** | | **$2,200/month** |

*$100/hr is a blended rate. Could be you at $0/hr opportunity cost, or a contractor.

**Timeline:** 1-4 weeks to MVP
**Total to MVP:** $2,200 - $8,800

**Ongoing:** $2,200/month for maintenance and iteration

---

## The Math

| Metric | Traditional | Agent-Native | Savings |
|--------|-------------|--------------|---------|
| Monthly cost | $50,000 | $2,200 | **95%** |
| Time to MVP | 4 months | 1 month | **75%** |
| Cost to MVP | $200,000 | $5,000 | **97%** |
| Annual cost | $600,000 | $26,400 | **96%** |

**The gap is not small.** It's a category shift.

---

## What Changes

### What Agents Do Well

| Task | Quality | Speed |
|------|---------|-------|
| Boilerplate code | Excellent | Instant |
| API integrations | Excellent | Minutes |
| UI components | Good | Minutes |
| Test generation | Good | Minutes |
| Refactoring | Excellent | Minutes |
| Documentation | Good | Minutes |
| Bug fixes (common) | Good | Minutes |

### What Humans Still Do

| Task | Why Humans |
|------|------------|
| Architecture decisions | Context of business needs |
| Product direction | Understanding user problems |
| Quality review | Catching subtle issues |
| Edge case handling | Domain expertise |
| Security review | High-stakes judgment |
| User research | Human connection |
| Prioritization | Business tradeoffs |

---

## The New Team Structure

### Micro-Team (1-2 people)

| Role | Time | Responsibility |
|------|------|----------------|
| Technical Lead | 10-15 hrs/week | Architecture, review, deployment |
| Product Lead | 10-15 hrs/week | Direction, user feedback, priorities |

Both roles can be the same person for small projects.

### Agent Constellation

| Agent | Purpose | Tool |
|-------|---------|------|
| Coding Agent | Write code | Claude Code, Cursor |
| Review Agent | Check quality | Claude with codebase context |
| Test Agent | Generate tests | Claude + test framework |
| Doc Agent | Write documentation | Claude + repo context |

**The agents work. The humans direct and review.**

---

## Real Cost Breakdown

### Month 1: Building MVP

| Activity | Hours | Cost |
|----------|-------|------|
| Requirements + architecture | 10 | $1,000 |
| Agent-assisted development | 30 | $3,000 (labor) + $200 (tokens) |
| Review + refinement | 15 | $1,500 |
| Deployment + testing | 5 | $500 |
| **Total** | **60** | **$6,200** |

### Months 2+: Operation

| Activity | Hours | Cost |
|----------|-------|------|
| Feature development | 10 | $1,000 (labor) + $100 (tokens) |
| Bug fixes + maintenance | 5 | $500 (labor) + $50 (tokens) |
| User support + feedback | 5 | $500 |
| Infrastructure | 0 | $20 (hosting) + $40 (runtime API) |
| **Total** | **20** | **$2,210** |

---

## Token Economics

### Coding Tokens (Development)

| Activity | Tokens/Month | Cost @ Claude |
|----------|--------------|---------------|
| Feature development | 2M input, 500K output | $80 |
| Refactoring | 1M input, 200K output | $30 |
| Bug investigation | 500K input, 100K output | $15 |
| Documentation | 500K input, 200K output | $20 |
| **Total** | | **~$150/month** |

### Runtime Tokens (Serving Users)

| Usage Level | Queries/Day | Tokens/Month | Cost |
|-------------|-------------|--------------|------|
| Light | 50 | 3M | $10 |
| Medium | 200 | 12M | $40 |
| Heavy | 1000 | 60M | $200 |

**Total API costs:** $150-350/month for most projects.

---

## When This Doesn't Work

### You Still Need Traditional Teams For:

| Scenario | Why |
|----------|-----|
| Novel research problems | Agents can't invent new algorithms |
| Safety-critical systems | Need human expertise throughout |
| Highly regulated industries | Compliance requires human accountability |
| Massive scale (millions of users) | Complex systems need deep expertise |
| Hardware/embedded | Agents aren't great here yet |

### The Hybrid Model

Most companies will have:
- **Core team:** 2-4 humans for strategy, architecture, review
- **Agent layer:** Coding agents for implementation
- **Specialist contractors:** For specific expertise when needed

---

## Skills That Matter Now

### Less Valuable
- Writing boilerplate code
- Memorizing syntax
- Manual testing
- Basic documentation

### More Valuable
- Architectural thinking
- Prompt engineering
- Code review (knowing what good looks like)
- Product judgment
- Human-agent collaboration

---

## How to Start

### If You're a PM/Designer

1. **Learn to read code** — Not write, just read
2. **Learn to prompt effectively** — The skill that multiplies everything
3. **Build with this starter kit** — Hands-on experience
4. **Review agent output critically** — The quality layer

### If You're a Developer

1. **Shift to architect mode** — Design systems, let agents implement
2. **Master code review** — Your value is judgment, not typing
3. **Learn the agent tools** — Claude Code, Cursor, Copilot
4. **Focus on the hard parts** — Edge cases, security, performance

### If You're a Founder

1. **Rethink your hiring plan** — 2 people + agents vs. 6 people
2. **Invest in agent tooling** — $200/month in API costs = $50K/month in labor
3. **Build review processes** — Agents write, humans approve
4. **Move faster** — Your competitors with agents are moving faster

---

## The Jai Agent Accelerator Economics

### What You're Buying

| Component | Traditional Cost | Your Cost |
|-----------|------------------|-----------|
| Architecture design | $20,000 | Included |
| Initial codebase | $50,000 | Included |
| Documentation | $10,000 | Included |
| Deployment guides | $5,000 | Included |
| Learning materials | $5,000 | Included |
| **Total value** | **$90,000** | **$497-1,997** |

### What You're Getting

- **Starter ($497):** Skip 3 months of architecture decisions
- **Pro ($997):** Skip 3 months + learn the patterns
- **Team ($1,997):** Skip 3 months + learn + get direct guidance

### Your Ongoing Costs

| Month 1 | Months 2+ |
|---------|-----------|
| $497-1,997 (one-time) | $0 |
| ~$50 (API + hosting) | ~$50 (API + hosting) |
| 20 hrs setup | 5-10 hrs/month maintenance |

**Total Year 1 cost:** ~$1,500-3,000
**Traditional equivalent:** ~$200,000

---

## Summary

| Era | Model | Monthly Cost | Speed |
|-----|-------|--------------|-------|
| 2010-2020 | Outsource | $30,000 | Slow |
| 2020-2023 | In-house team | $50,000 | Medium |
| 2024+ | Human + agents | $2,000-5,000 | Fast |

**The question isn't whether to use agents. It's how fast you can adapt.**

---

[← Architecture Decisions](ARCHITECTURE_DECISIONS.md) | [Back to README](../README.md)
