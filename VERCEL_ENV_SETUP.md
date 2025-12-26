# Vercel Environment Variables Setup Guide

## Quick Setup Commands

Run these commands in your terminal (from project root):

```bash
# 1. Set required API key
vercel env add ANTHROPIC_API_KEY production
# When prompted: Paste your API key (starts with sk-ant-...)
# When asked "Mark as sensitive? (y/N)": y

# 2. Set domain to analytics (REQUIRED for analytics agent)
vercel env add DOMAIN production
# When prompted: Enter: data_analytics
# When asked "Mark as sensitive? (y/N)": n

# 3. Set model (recommended)
vercel env add MODEL production
# When prompted: Enter: claude-sonnet-4-20250514
# When asked "Mark as sensitive? (y/N)": n

# 4. Set log level (optional)
vercel env add LOG_LEVEL production
# When prompted: Enter: INFO
# When asked "Mark as sensitive? (y/N)": n

# 5. Verify all variables are set
vercel env ls
```

## Step-by-Step Instructions

### Step 1: Set ANTHROPIC_API_KEY (Required)

```bash
vercel env add ANTHROPIC_API_KEY production
```

**What to enter:**
- Paste your full API key (e.g., `sk-ant-api03-xxxxxxxxxxxxx`)
- When asked "Mark as sensitive? (y/N)": Type `y` and press Enter

**Why:** This is your Anthropic API key for Claude. Keep it secret.

### Step 2: Set DOMAIN (Required for Analytics)

```bash
vercel env add DOMAIN production
```

**What to enter:**
- Type: `data_analytics`
- When asked "Mark as sensitive? (y/N)": Type `n` and press Enter

**Why:** This tells the server to use the analytics agent instead of PMM.

### Step 3: Set MODEL (Recommended)

```bash
vercel env add MODEL production
```

**What to enter:**
- Type: `claude-sonnet-4-20250514`
- When asked "Mark as sensitive? (y/N)": Type `n` and press Enter

**Why:** Sonnet 4 is more capable than Haiku and will follow instructions better (like showing full SQL output).

### Step 4: Set LOG_LEVEL (Optional)

```bash
vercel env add LOG_LEVEL production
```

**What to enter:**
- Type: `INFO`
- When asked "Mark as sensitive? (y/N)": Type `n` and press Enter

**Why:** Controls logging verbosity. INFO is good for production.

### Step 5: Verify Environment Variables

```bash
vercel env ls
```

**Expected output:**
```
ANTHROPIC_API_KEY  production  [hidden]
DOMAIN             production  data_analytics
MODEL              production  claude-sonnet-4-20250514
LOG_LEVEL          production  INFO
```

## Alternative: Set via Vercel Dashboard

1. Go to [vercel.com](https://vercel.com)
2. Select your project: `my-pmm-agent`
3. Go to **Settings** → **Environment Variables**
4. Click **Add New**
5. For each variable:
   - **Name:** `ANTHROPIC_API_KEY`
   - **Value:** Your API key
   - **Environment:** Production (and Preview if you want)
   - **Mark as sensitive:** ✅ (for API key only)
   - Click **Save**

Repeat for:
- `DOMAIN` = `data_analytics`
- `MODEL` = `claude-sonnet-4-20250514`
- `LOG_LEVEL` = `INFO`

## After Setting Variables

**Important:** Environment variables are only applied on the next deployment.

```bash
# Redeploy to apply new environment variables
vercel --prod
```

## Troubleshooting

### "Variable not found" error

**Problem:** Server can't find environment variable

**Solution:**
1. Verify variable is set: `vercel env ls`
2. Make sure it's set for `production` environment
3. Redeploy: `vercel --prod`

### Wrong domain showing

**Problem:** Still seeing PMM agent instead of analytics

**Solution:**
1. Check `DOMAIN` is set: `vercel env ls | grep DOMAIN`
2. Should show: `DOMAIN production data_analytics`
3. If missing or wrong, set it: `vercel env add DOMAIN production`
4. Redeploy: `vercel --prod`

### API key errors

**Problem:** "ANTHROPIC_API_KEY not set" errors

**Solution:**
1. Verify key is set: `vercel env ls | grep ANTHROPIC`
2. Should show: `ANTHROPIC_API_KEY production [hidden]`
3. If missing, set it: `vercel env add ANTHROPIC_API_KEY production`
4. Make sure you pasted the full key (starts with `sk-ant-`)
5. Redeploy: `vercel --prod`

## Quick Reference

| Variable | Value | Required | Sensitive |
|----------|-------|----------|-----------|
| `ANTHROPIC_API_KEY` | `sk-ant-...` | ✅ Yes | ✅ Yes |
| `DOMAIN` | `data_analytics` | ✅ Yes | ❌ No |
| `MODEL` | `claude-sonnet-4-20250514` | ⚠️ Recommended | ❌ No |
| `LOG_LEVEL` | `INFO` | ❌ Optional | ❌ No |

