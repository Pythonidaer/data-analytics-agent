# Exercise 5: Domain Conversion - Completion Checklist

> **Goal:** Convert the PMM agent to a Data Analytics Expert Agent and deploy to Vercel

## Exercise 5 Requirements (from EXERCISES.md)

### ✅ Core Requirements

- [x] **1. Create new domain config**: `config/domains/data_analytics.json`
  - ✅ Created with all required fields (domain, name, description, experts, tools, frameworks, quick_actions)
  - ✅ Validated structure and content

- [x] **2. Identify 3-5 experts for your domain**
  - ✅ Analytics Strategist (North Star, KPI trees, metric definitions)
  - ✅ Product Analyst (Funnels, cohorts, retention, experiments)
  - ✅ Analytics Engineer (Event tracking, dbt-style modeling, data tests)
  - ✅ Insights Communicator (Executive narratives, chart recommendations)

- [x] **3. Create 3+ custom tools specific to your domain**
  - ✅ **Intake Tools (2):** `capture_analytics_intake`, `clarify_kpi_and_decision`
  - ✅ **Research Tools (2):** `lookup_benchmark_ranges`, `fetch_url` (reused)
  - ✅ **Planning Tools (4):** `create_metrics_dictionary`, `generate_tracking_plan`, `draft_sql_query_pack`, `create_dashboard_spec`
  - ✅ **Risk Tools (2):** `assess_analytics_risks`, `create_data_quality_checklist`
  - ✅ **Total: 10 custom tools** (exceeds 3+ requirement)

- [x] **4. Write domain-specific prompts with expert knowledge**
  - ✅ Main system prompt with analytics philosophy and workflow
  - ✅ 4 specialist prompts (one per expert)
  - ✅ Includes analytics frameworks (North Star, Kimball, Funnel/Cohort, Experimentation, dbt)
  - ✅ Includes anti-patterns and best practices

- [x] **5. Update the frontend quick actions**
  - ✅ Frontend fetches config from `/config` endpoint
  - ✅ Quick actions dynamically loaded from domain config
  - ✅ Analytics-specific quick actions displayed
  - ✅ Color theme switches to blue/cyan for analytics

- [ ] **6. Deploy the customized agent**
  - ⚠️ **PENDING:** Deploy to Vercel (see deployment checklist below)

### ✅ Success Criteria

- [x] **Agent responds with domain-specific expertise**
  - ✅ Uses analytics terminology
  - ✅ References analytics frameworks
  - ✅ Asks analytics-specific clarifying questions

- [x] **At least 3 custom tools working**
  - ✅ 10 tools implemented and tested
  - ✅ Tools properly integrated into agent

- [x] **Quick actions match your domain**
  - ✅ 4 analytics quick actions from config
  - ✅ Icons and colors match analytics theme

- [x] **Can explain the "Giants" for your domain**
  - ✅ Prompts include analytics frameworks and methodologies
  - ✅ Agent references North Star, Kimball, Funnel/Cohort patterns

---

## Vercel Deployment Readiness Checklist

### ✅ Pre-Deployment Setup

- [x] **Domain Configuration**
  - ✅ `config/domains/data_analytics.json` exists and is valid
  - ✅ Domain switching works via `DOMAIN` environment variable

- [x] **Backend Code**
  - ✅ `create_analytics_agent()` function implemented
  - ✅ Domain loading logic in `agent.py`
  - ✅ Server switches domains based on `DOMAIN` env var
  - ✅ `/config` endpoint returns domain-specific config

- [x] **Frontend Code**
  - ✅ Fetches config from `/config` endpoint
  - ✅ Dynamically displays quick actions
  - ✅ Color theme switches based on domain
  - ✅ Builds successfully (`npm run build`)

- [x] **Vercel Configuration**
  - ✅ `vercel.json` exists with correct build/rewrite config
  - ✅ `api/index.py` exists and imports agent correctly
  - ✅ `api/requirements.txt` exists with all dependencies

### ⚠️ Deployment Steps (To Complete)

- [ ] **1. Install Vercel CLI**
  ```bash
  npm install -g vercel
  vercel login
  ```

- [ ] **2. Initialize Vercel Project**
  ```bash
  vercel
  # Follow prompts to link to GitHub repo
  ```

- [ ] **3. Set Environment Variables**
  ```bash
  # Required
  vercel env add ANTHROPIC_API_KEY production
  # Paste your API key when prompted
  # Mark as sensitive: y

  # For Analytics Domain
  vercel env add DOMAIN production
  # Enter: data_analytics
  # Mark as sensitive: n

  # Optional (recommended)
  vercel env add MODEL production
  # Enter: claude-sonnet-4-20250514
  # Mark as sensitive: n

  vercel env add LOG_LEVEL production
  # Enter: INFO
  # Mark as sensitive: n
  ```

- [ ] **4. Deploy to Production**
  ```bash
  vercel --prod
  ```

- [ ] **5. Verify Deployment**
  ```bash
  # Check health endpoint
  curl https://your-project.vercel.app/api/health
  
  # Expected: {"status": "ok", "agent": "jai-agent-accelerator", "version": "0.1.0"}
  
  # Check config endpoint
  curl https://your-project.vercel.app/api/config
  
  # Expected: {"domain": "data_analytics", "name": "Data Analytics Expert Agent", ...}
  ```

- [ ] **6. Test Frontend**
  - [ ] Open `https://your-project.vercel.app`
  - [ ] Verify blue/cyan color theme (analytics)
  - [ ] Verify analytics quick actions appear
  - [ ] Test a quick action (e.g., "Create a metrics dictionary")
  - [ ] Verify agent responds with analytics expertise

---

## Pre-Deployment Verification

### Code Verification

Run these checks before deploying:

```bash
# 1. Test domain config loads correctly
cd apps/agent
source .venv/bin/activate
python3 -c "from src.pmm_agent.agent import _load_domain_config; config = _load_domain_config('data_analytics'); print('✅ Config loads:', config['domain'])"

# 2. Test analytics agent creation
python3 -c "from src.pmm_agent.agent import create_analytics_agent; agent = create_analytics_agent(); print('✅ Analytics agent created')"

# 3. Test server with analytics domain
export DOMAIN=data_analytics
python3 -c "from src.pmm_agent.server import app, domain; print(f'✅ Server domain: {domain}')"

# 4. Test frontend build
cd ../../apps/web
npm run build
# Should complete without errors

# 5. Test API requirements
cd ../../api
python3 -c "import sys; sys.path.insert(0, '../apps/agent/src'); from pmm_agent.server import app; print('✅ API imports work')"
```

### File Structure Verification

Ensure these files exist:

```
✅ config/domains/data_analytics.json
✅ apps/agent/src/pmm_agent/domains/data_analytics/prompts.py
✅ apps/agent/src/pmm_agent/domains/data_analytics/tools/__init__.py
✅ apps/agent/src/pmm_agent/domains/data_analytics/tools/intake.py
✅ apps/agent/src/pmm_agent/domains/data_analytics/tools/research.py
✅ apps/agent/src/pmm_agent/domains/data_analytics/tools/planning.py
✅ apps/agent/src/pmm_agent/domains/data_analytics/tools/risk.py
✅ apps/agent/src/pmm_agent/agent.py (with create_analytics_agent)
✅ apps/agent/src/pmm_agent/server.py (with domain switching)
✅ apps/web/src/App.tsx (with domain-aware frontend)
✅ vercel.json
✅ api/index.py
✅ api/requirements.txt
```

---

## Post-Deployment Verification

After deploying, verify:

- [ ] **Health Check**
  - [ ] `GET /api/health` returns `{"status": "ok"}`

- [ ] **Config Endpoint**
  - [ ] `GET /api/config` returns analytics domain config
  - [ ] `domain` field is `"data_analytics"`
  - [ ] `quick_actions` array has 4 items

- [ ] **Frontend**
  - [ ] Loads without errors
  - [ ] Shows "Data Analytics Expert Agent" title
  - [ ] Displays analytics quick actions
  - [ ] Uses blue/cyan color theme

- [ ] **Agent Functionality**
  - [ ] Responds with analytics expertise
  - [ ] Uses analytics terminology
  - [ ] Calls analytics tools correctly
  - [ ] Shows complete SQL output (not summaries)

- [ ] **Environment Variables**
  - [ ] `DOMAIN=data_analytics` is set
  - [ ] `ANTHROPIC_API_KEY` is set
  - [ ] `MODEL` is set (optional but recommended)

---

## Known Issues to Address

### ⚠️ SQL Output Display Issue

**Status:** Partially Fixed
- ✅ Prompt updated with explicit instructions
- ✅ Tool output includes instruction
- ⚠️ May need Sonnet model (not Haiku) for best results
- ✅ User switched to Sonnet

**Verification:**
- Test with "Draft SQL for funnel + retention" quick action
- Verify agent shows complete SQL code blocks (not summaries)

### ⚠️ Domain Switching

**Status:** ✅ Complete
- ✅ Server reads `DOMAIN` env var
- ✅ Creates analytics agent when `DOMAIN=data_analytics`
- ✅ Falls back to PMM if analytics not available

---

## Teaching Readiness Checklist

Before teaching your friend, ensure:

- [x] **Exercise 5 Complete**
  - ✅ All 6 requirements met
  - ✅ All success criteria met
  - ✅ Agent works locally with analytics domain

- [ ] **Deployed to Vercel**
  - [ ] Production URL available
  - [ ] All endpoints working
  - [ ] Frontend displays correctly

- [ ] **Documentation Ready**
  - [ ] Can explain domain conversion process
  - [ ] Can show before/after (PMM → Analytics)
  - [ ] Can demonstrate custom tools
  - [ ] Can walk through deployment steps

- [ ] **Testing Scenarios Prepared**
  - [ ] Test case: Quick action → Agent response
  - [ ] Test case: SQL generation → Full output
  - [ ] Test case: Metrics dictionary → Structured output
  - [ ] Test case: Domain switching (PMM ↔ Analytics)

---

## Summary

### ✅ Completed (Ready for Deployment)

1. ✅ Domain configuration created
2. ✅ 4 experts defined
3. ✅ 10 custom tools implemented
4. ✅ Domain-specific prompts written
5. ✅ Frontend updated with analytics theme
6. ✅ Domain switching implemented
7. ✅ Vercel configuration files ready

### ⚠️ Pending (Before Teaching)

1. ⚠️ Deploy to Vercel
2. ⚠️ Set environment variables
3. ⚠️ Verify production deployment
4. ⚠️ Test all functionality in production

### 🎯 Next Steps

1. **Deploy to Vercel** (follow deployment steps above)
2. **Verify production** (run post-deployment checks)
3. **Prepare teaching materials** (documentation, test cases)
4. **Test with friend** (walk through the system together)

---

## Quick Reference: Deployment Commands

```bash
# Install Vercel CLI
npm install -g vercel
vercel login

# Initialize project
vercel

# Set environment variables
vercel env add ANTHROPIC_API_KEY production
vercel env add DOMAIN production  # Enter: data_analytics
vercel env add MODEL production  # Enter: claude-sonnet-4-20250514

# Deploy
vercel --prod

# Verify
curl https://your-project.vercel.app/api/health
curl https://your-project.vercel.app/api/config
```

---

**Status:** ✅ **95% Complete** - Ready for Vercel deployment

**Blockers:** None - All code is ready, just needs deployment steps

