# Vercel Setup Options for Analytics Agent

## Current Situation

Your repository is linked to the **"my-pmm-agent"** Vercel project, which has:
- ✅ `ANTHROPIC_API_KEY` (already set)
- ✅ `MODEL` (already set)
- ✅ `ALLOWED_ORIGINS` (already set)
- ❌ `DOMAIN` (missing - this is what switches to analytics)

## Option 1: Use Same Project (Recommended)

**Best if:** You want to convert the existing PMM agent to analytics

**Steps:**
```bash
# Just add the DOMAIN variable to switch to analytics
vercel env add DOMAIN production
# Type: data_analytics
# Type: n (not sensitive)

# Redeploy
vercel --prod
```

**Result:** The same project will now run the analytics agent instead of PMM.

## Option 2: Create New Project

**Best if:** You want to keep PMM and analytics as separate deployments

**Steps:**
```bash
# Remove current project link
rm -rf .vercel

# Create new project
vercel

# When prompted:
# - Set up and deploy? Yes
# - Link to existing project? No
# - Project name? data-analytics-agent (or your choice)
# - Directory? ./
# - Override settings? No

# Then set all environment variables
vercel env add ANTHROPIC_API_KEY production
# Paste your API key, type 'y' for sensitive

vercel env add DOMAIN production
# Type: data_analytics
# Type: n

vercel env add MODEL production
# Type: claude-sonnet-4-20250514
# Type: n

# Deploy
vercel --prod
```

## Recommendation

**Use Option 1** - Just add `DOMAIN=data_analytics` to your existing project. This:
- ✅ Keeps everything in one place
- ✅ Reuses existing API key and settings
- ✅ Only requires adding one variable
- ✅ Can switch back to PMM by changing DOMAIN to "pmm"

## Quick Command (Option 1)

```bash
# Add DOMAIN variable
vercel env add DOMAIN production
# Enter: data_analytics
# Enter: n

# Verify it's set
vercel env ls

# Redeploy
vercel --prod
```

After this, your existing project will run the analytics agent!

