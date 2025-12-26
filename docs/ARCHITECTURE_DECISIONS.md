# Architecture Decisions

> When you're ready to productionize, read this.

This guide helps you make infrastructure decisions. We focus on **what matters** and skip the enterprise complexity you don't need yet.

---

## The Key Insight

**The application code is an implementation detail.**

With modern AI coding agents, the cost of writing application code approaches zero. What matters is:

1. **Architecture pattern** — How components connect
2. **Deployment model** — Where it runs
3. **Human oversight** — Who reviews what

The code itself? That's generated. Focus on the decisions.

---

## Architecture Patterns

You have three options. Pick one.

### Pattern 1: Serverless (Recommended)

```
User → Frontend (CDN) → Serverless Function → Claude API
```

**Use when:** Starting out, low-to-medium traffic, want simplicity
**Cost:** $0-50/month
**Scaling:** Automatic

**Where to deploy:**
- **Netlify** — [Deploy guide](DEPLOYMENT.md#option-1-netlify-recommended)
- **Vercel** — [vercel.com/docs](https://vercel.com/docs)

**Limitations:**
- 10-26 second function timeout (depending on tier)
- Cold starts (first request slow)
- Limited background processing

### Pattern 2: Container Service

```
User → Load Balancer → Container(s) → Claude API
```

**Use when:** Need longer timeouts, background jobs, more control
**Cost:** $15-100/month
**Scaling:** Manual or auto-scaling rules

**Where to deploy:**
- **Railway** — [docs.railway.app](https://docs.railway.app)
- **Fly.io** — [fly.io/docs](https://fly.io/docs)
- **Render** — [render.com/docs](https://render.com/docs)

**Limitations:**
- You manage scaling
- Need to think about containers
- More configuration

### Pattern 3: Full Cloud (Advanced)

```
User → CDN → API Gateway → Lambda/ECS → Claude API
       ↓
    S3/CloudFront
```

**Use when:** Enterprise requirements, compliance, massive scale
**Cost:** $100-1000+/month
**Scaling:** Whatever you configure

**Where to deploy:**
- **AWS** — [Lambda](https://docs.aws.amazon.com/lambda/), [ECS](https://docs.aws.amazon.com/ecs/)
- **GCP** — [Cloud Run](https://cloud.google.com/run/docs), [Cloud Functions](https://cloud.google.com/functions/docs)
- **Azure** — [Functions](https://docs.microsoft.com/azure/azure-functions/), [Container Apps](https://docs.microsoft.com/azure/container-apps/)

**If you're reading this section because you think you need it:** You probably don't. Start with Pattern 1 or 2. Migrate when you have real scale problems.

---

## Decision Framework

### Question 1: How long do agent responses take?

| Response Time | Pattern |
|---------------|---------|
| < 10 seconds | Serverless (Netlify free tier) |
| 10-30 seconds | Serverless (Netlify Pro) or Container |
| > 30 seconds | Container or implement streaming |

### Question 2: Do you need background jobs?

| Need | Pattern |
|------|---------|
| No background jobs | Serverless |
| Some async processing | Container (Railway) |
| Complex job queues | Full Cloud (with SQS/Pub-Sub) |

### Question 3: What's your compliance situation?

| Compliance | Pattern |
|------------|---------|
| None / startup | Serverless |
| SOC2 in progress | Container (with logging) |
| HIPAA / FedRAMP | Full Cloud (with proper configs) |

---

## The Application Code (Implementation Detail)

This is the code you're getting. Here's the 2-minute overview.

### Backend Structure

```
apps/agent/src/pmm_agent/
├── agent.py      # Creates the LangGraph agent
├── prompts.py    # System prompts (MoE methodology)
├── server.py     # FastAPI endpoints
└── tools/        # Tool implementations
    ├── intake.py
    ├── research.py
    ├── planning.py
    └── risk.py
```

**Key files:**
- `agent.py:create_pmm_agent()` — Factory function, returns configured agent
- `server.py:/chat/stream` — Streaming endpoint, SSE format
- `prompts.py:MAIN_SYSTEM_PROMPT` — The intelligence layer

### Frontend Structure

```
apps/web/src/
├── App.tsx       # Main component
├── api.ts        # Backend communication
└── components/   # UI pieces
```

**Key pattern:**
- React + Vite + Tailwind
- Streams responses via EventSource
- Quick actions trigger pre-built prompts

### What You'll Modify

| Goal | File | Section |
|------|------|---------|
| Change agent behavior | `prompts.py` | `MAIN_SYSTEM_PROMPT` |
| Add new capability | `tools/*.py` | New `@tool` function |
| Change UI | `App.tsx` | React component |
| Add endpoint | `server.py` | New FastAPI route |

**You don't need to understand the internals.** Use Claude Code or Cursor to make changes. Describe what you want, let the agent write the code.

---

## For Railway Users

**Minimum setup:**

```bash
# In project root
railway login
railway init
railway variables set ANTHROPIC_API_KEY=sk-ant-xxx
railway up
```

**Docs:** [docs.railway.app/quick-start](https://docs.railway.app/quick-start)

That's it. Railway auto-detects Python and Node.

---

## For AWS Users

**Minimum viable setup:**

1. **Lambda + API Gateway** for backend
2. **S3 + CloudFront** for frontend
3. **Secrets Manager** for API key

**Start here:** [AWS Lambda Python Tutorial](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)

**Use SAM or CDK**, not raw CloudFormation:
- [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/)
- [AWS CDK](https://docs.aws.amazon.com/cdk/)

---

## For GCP Users

**Minimum viable setup:**

1. **Cloud Run** for backend (container)
2. **Cloud Storage + CDN** for frontend
3. **Secret Manager** for API key

**Start here:** [Cloud Run Quickstart](https://cloud.google.com/run/docs/quickstarts)

**Use Terraform or Pulumi** for infrastructure:
- [Terraform GCP Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)

---

## Scaling Considerations

### When to Scale

| Signal | Action |
|--------|--------|
| Timeouts increasing | Add more instances / upgrade tier |
| Cold starts hurting UX | Implement keep-warm or switch to containers |
| Costs > $100/month | Optimize prompts, cache responses |
| Users > 1000/day | Consider dedicated infrastructure |

### What NOT to Do

- **Don't pre-optimize.** Start simple, add complexity when needed.
- **Don't use Kubernetes** unless you have a DevOps team.
- **Don't build a microservices architecture** for an MVP.
- **Don't add a database** unless you actually need persistence.

### The 90% Solution

Most projects never need to leave Pattern 1 (Serverless).

Netlify Pro ($19/month) handles:
- 125,000 function calls/month
- 26-second timeouts
- Automatic scaling
- Global CDN

That's enough for ~4,000 daily users before you need to think harder.

---

## Security Checklist

Before going live:

- [ ] API key in environment variables (not in code)
- [ ] HTTPS enforced
- [ ] CORS restricted to your domain
- [ ] Input validation on user messages
- [ ] Rate limiting configured
- [ ] Error messages don't leak internals

---

## Migration Paths

### Netlify → Railway

When you outgrow serverless:

1. Create Railway project
2. Copy environment variables
3. Push code to Railway
4. Update DNS

**Time:** 1-2 hours

### Railway → AWS

When you need enterprise features:

1. Containerize with Docker (already done)
2. Set up ECS or Lambda
3. Configure API Gateway
4. Set up CI/CD pipeline
5. Migrate DNS

**Time:** 4-8 hours (first time), hire help if needed

---

## The Bottom Line

| Stage | Pattern | Monthly Cost | Your Time |
|-------|---------|--------------|-----------|
| Learning | Local | $3 (API only) | — |
| Demo | Netlify Free | $3 | 30 min setup |
| Production | Netlify Pro | $22 | 30 min setup |
| Scale | Railway | $30-100 | 2 hr setup |
| Enterprise | AWS/GCP | $200+ | 8+ hr setup |

**Start at the top. Move down only when you have to.**

---

[← Build vs Buy](BUILD_VS_BUY.md) | [Deployment](DEPLOYMENT.md) | [Cost of Building →](COST_OF_BUILDING.md)
