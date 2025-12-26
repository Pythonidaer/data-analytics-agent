# Build vs Buy: Infrastructure Decisions

> A practical guide for choosing your deployment and hosting stack.

**Who this is for:** PMs, designers, and founders who want to understand the infrastructure decisions without becoming DevOps engineers.

---

## The TL;DR Decision Tree

```
Do you want to think about infrastructure?
│
├─ NO → Use Netlify (30 min setup, $0-25/month)
│       └─ Done. Move on with your life.
│
└─ YES → Keep reading for the full breakdown
```

---

## What You Actually Need

Your agent needs 4 things to run in production:

| Need | What It Does | Options |
|------|--------------|---------|
| **Hosting** | Runs your code | Netlify, Railway, Vercel, AWS |
| **Domain** | yourname.com | Namecheap, Google Domains, Cloudflare |
| **CI/CD** | Deploys on push | GitHub Actions, Netlify, Railway |
| **Monitoring** | Alerts when broken | Anthropic dashboard, Sentry, LogTail |

---

## Quick Comparison

### Hosting Platforms

| Platform | Setup Time | Monthly Cost | Best For | Limitation |
|----------|------------|--------------|----------|------------|
| **Netlify** | 30 min | $0-25 | "Just works" | 10s timeout (free) |
| **Railway** | 20 min | $5-20 | More control | Learning curve |
| **Vercel** | 25 min | $0-20 | React apps | Python quirks |
| **Fly.io** | 40 min | $5-15 | Global edge | More config |
| **AWS Lambda** | 2+ hours | $1-50 | Enterprise scale | Complex setup |
| **Self-hosted** | 4+ hours | $5-100+ | Full control | You maintain it |

### Our Recommendation

**Start with Netlify.** If you outgrow it, migrate later.

```
Your progression:
1. Netlify (free) → Learning, demos, early users
2. Netlify (Pro) → Real users, longer timeouts
3. Railway → Need more control, background jobs
4. Self-hosted → Enterprise, compliance requirements
```

---

## The Full Breakdown

### Option 1: Netlify (Recommended)

**What you get:**
- Frontend + backend in one platform
- Automatic deploys from GitHub
- Free SSL certificates
- CDN for fast global access
- Serverless functions for Python

**Cost breakdown:**

| Tier | Monthly | Function Calls | Timeout | Best For |
|------|---------|----------------|---------|----------|
| Free | $0 | 125K | 10s | Learning, demos |
| Pro | $19 | 125K | 26s | Production |
| Business | $99 | 2M | 26s | Scale |

**The 10-second timeout issue:**

Netlify free tier kills functions after 10 seconds. Agent responses can take 15-30 seconds for complex queries.

**Solutions:**
1. **Upgrade to Pro ($19/month)** → 26 second timeout
2. **Implement streaming** → Response starts immediately
3. **Use Railway instead** → No timeout

**Setup time:** 30 minutes

---

### Option 2: Railway

**What you get:**
- Full control over deployment
- No function timeouts
- Built-in PostgreSQL, Redis
- Easy environment variables
- One-click GitHub deploys

**Cost breakdown:**

| Usage | Monthly |
|-------|---------|
| Minimal | $5 |
| Moderate | $10-20 |
| Heavy | $20-50 |

**When to choose Railway:**
- You need background jobs
- You want longer timeouts
- You need a database
- You want more control

**Setup time:** 20 minutes

---

### Option 3: Vercel

**What you get:**
- Excellent React/Next.js support
- Edge functions (fast globally)
- Easy GitHub integration
- Good free tier

**Cost breakdown:**

| Tier | Monthly | Best For |
|------|---------|----------|
| Hobby | $0 | Personal projects |
| Pro | $20 | Teams |

**The Python caveat:**

Vercel's Python runtime has quirks. If you're not a developer, Netlify is easier for Python.

**Setup time:** 25 minutes

---

### Option 4: Self-Hosted (Docker)

**What you get:**
- Complete control
- No platform limits
- Run anywhere (AWS, DigitalOcean, your server)

**What you need:**
- Server ($5-100+/month)
- Domain name (~$12/year)
- SSL certificate (free with Let's Encrypt)
- Docker knowledge
- Monitoring setup

**When to choose self-hosted:**
- Compliance requirements (data residency)
- Enterprise IT policies
- You enjoy DevOps
- Cost optimization at scale

**Setup time:** 4+ hours (first time)

---

## CI/CD: Automatic Deployments

### What is CI/CD?

When you push code to GitHub, CI/CD automatically:
1. Runs tests
2. Builds your app
3. Deploys to production

**You want this because:** Manual deploys are error-prone and slow.

### Option A: Platform Built-In (Easiest)

**Netlify/Railway/Vercel** all have this built-in:
1. Connect GitHub repo
2. Push code
3. It deploys automatically

**Cost:** Free (included)
**Setup:** 5 minutes

### Option B: GitHub Actions (More Control)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to Netlify
        uses: nwtgck/actions-netlify@v2
        with:
          publish-dir: './apps/web/dist'
          production-deploy: true
        env:
          NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
          NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
```

**Cost:** Free (2,000 min/month)
**Setup:** 30 minutes

---

## Monitoring: Know When It Breaks

### Minimum Viable Monitoring

1. **Anthropic Dashboard** (free)
   - Track token usage
   - Monitor costs
   - See error rates

2. **Netlify Analytics** ($9/month)
   - Traffic patterns
   - Error logs
   - Performance data

### Advanced Monitoring

| Tool | Purpose | Cost |
|------|---------|------|
| **Sentry** | Error tracking | Free tier |
| **LogTail** | Log aggregation | Free tier |
| **Checkly** | Uptime monitoring | Free tier |
| **PagerDuty** | Alerting | $25/month |

---

## The Decision Matrix

### For PMs & Designers

**Your situation:** You want to show stakeholders, not become a DevOps engineer.

**Recommended stack:**
- **Hosting:** Netlify Pro ($19/month)
- **Domain:** Optional, use `yourname.netlify.app`
- **CI/CD:** Netlify built-in (free)
- **Monitoring:** Anthropic dashboard (free)

**Total: $19/month**
**Setup: 30 minutes**

---

### For Technical Founders

**Your situation:** You want control but not overhead.

**Recommended stack:**
- **Hosting:** Railway ($10-20/month)
- **Domain:** Namecheap (~$12/year)
- **CI/CD:** Railway built-in (free)
- **Monitoring:** Sentry free tier + Anthropic dashboard

**Total: $12-22/month**
**Setup: 1 hour**

---

### For Enterprise/Compliance

**Your situation:** You need data residency, audit logs, SOC2.

**Recommended stack:**
- **Hosting:** AWS/GCP/Azure (self-managed)
- **Domain:** Route 53 or Cloudflare
- **CI/CD:** GitHub Actions
- **Monitoring:** Full observability stack

**Total: $50-500/month (depending on scale)**
**Setup: 4+ hours + ongoing maintenance**

---

## Bonus Exercise: Calculate Your True Cost

### The Calculation

| Component | Monthly Cost | Annual Cost |
|-----------|--------------|-------------|
| Hosting | $____ | $____ |
| Domain | $____ | $____ |
| API (Claude) | $____ | $____ |
| Monitoring | $____ | $____ |
| **Total** | $____ | $____ |

### Typical Costs by Usage

| Usage Level | Description | Monthly Total |
|-------------|-------------|---------------|
| **Learning** | 100 queries/month | $3-5 |
| **Demo** | 500 queries/month | $10-20 |
| **Production** | 5,000 queries/month | $50-100 |
| **Scale** | 50,000+ queries/month | $200+ |

### The Hidden Costs

**Time is money.** Factor in:
- Setup time (hourly rate × hours)
- Maintenance time (ongoing)
- Debugging time (when things break)

**Netlify at $19/month** that "just works" is often cheaper than **free self-hosted** that takes 2 hours to debug every month.

---

## Migration Paths

### Netlify → Railway

When you outgrow Netlify:
1. Export environment variables
2. Create Railway project
3. Connect GitHub repo
4. Verify deployment

**Time:** 1 hour

### Railway → AWS

When you need enterprise:
1. Containerize with Docker
2. Set up ECS/EKS
3. Configure VPC, security groups
4. Set up CI/CD pipeline

**Time:** 4+ hours (hire help if needed)

---

## FAQ

**Q: Can I start free and upgrade later?**
A: Yes. Start with Netlify free, upgrade when you hit limits.

**Q: What if my company has AWS/GCP credits?**
A: Great, use them. But know the setup is more complex.

**Q: Should I use Kubernetes?**
A: No. Not until you have 10,000+ users and a DevOps team.

**Q: What about Cloudflare Workers?**
A: Good for edge computing, but Python support is limited.

**Q: Can I change my mind later?**
A: Yes. The agent is portable. Migration is ~1 hour.

---

## Recommendation Summary

| Persona | Platform | Monthly Cost | Setup Time |
|---------|----------|--------------|------------|
| **PM/Designer** | Netlify Pro | $19 | 30 min |
| **Technical Founder** | Railway | $15 | 1 hour |
| **Enterprise** | AWS/GCP | $100+ | 4+ hours |
| **Learning** | Netlify Free | $0 | 30 min |

**When in doubt, choose Netlify.** You can always migrate later.

---

[← Troubleshooting](TROUBLESHOOTING.md) | [Deployment Guide](DEPLOYMENT.md) | [Advanced →](ADVANCED.md)
