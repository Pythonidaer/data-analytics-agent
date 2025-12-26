# Updating Existing Vercel Environment Variables

## The Issue

You're seeing: "A variable with the name `ANTHROPIC_API_KEY` already exists"

This means the variable is already set. You have two options:

## Option 1: Update Existing Variable (Recommended)

```bash
# Remove the existing variable first
vercel env rm ANTHROPIC_API_KEY production

# Then add it again with the new value
vercel env add ANTHROPIC_API_KEY production
# Paste your API key when prompted
# Type 'y' for sensitive
```

## Option 2: Check Current Values

```bash
# List all environment variables
vercel env ls

# This will show what's currently set (values are hidden for sensitive vars)
```

## Quick Setup for All Variables

Since some variables might already exist, here's the complete setup:

```bash
# 1. Check what's already set
vercel env ls

# 2. Update/Add ANTHROPIC_API_KEY
vercel env rm ANTHROPIC_API_KEY production 2>/dev/null || true
vercel env add ANTHROPIC_API_KEY production
# Paste your key, type 'y' for sensitive

# 3. Update/Add DOMAIN (for analytics agent)
vercel env rm DOMAIN production 2>/dev/null || true
vercel env add DOMAIN production
# Type: data_analytics
# Type 'n' for sensitive

# 4. Update/Add MODEL
vercel env rm MODEL production 2>/dev/null || true
vercel env add MODEL production
# Type: claude-sonnet-4-20250514
# Type 'n' for sensitive

# 5. Verify all are set
vercel env ls

# 6. Redeploy to apply changes
vercel --prod
```

## What You Should See After Setup

```bash
$ vercel env ls

ANTHROPIC_API_KEY  production  [hidden]
DOMAIN             production  data_analytics
MODEL              production  claude-sonnet-4-20250514
```

## Important Notes

1. **Removing and re-adding is safe** - it just updates the value
2. **Sensitive variables** (like API keys) are hidden in the list
3. **Changes only apply after redeploy** - run `vercel --prod` after setting variables
4. **DOMAIN must be `data_analytics`** - otherwise you'll get the PMM agent

