# New Vercel Project Setup for Analytics Agent

## Step 1: Complete Project Creation

You're currently at the project name prompt. Here's what to enter:

```
? What's your project's name? (data-analytics-agent)
```
**Answer:** Press Enter to accept `data-analytics-agent` (or type a different name)

Then you'll be asked:
```
? In which directory is your code located? ./
```
**Answer:** Press Enter (current directory is correct)

```
? Want to override the settings? [y/N]
```
**Answer:** Type `N` and press Enter

## Step 2: Set Environment Variables

After the project is created, run these commands:

```bash
# 1. API Key (REQUIRED)
vercel env add ANTHROPIC_API_KEY production
# Paste your API key (starts with sk-ant-...)
# Type 'y' when asked if sensitive

# 2. Domain (REQUIRED for analytics agent)
vercel env add DOMAIN production
# Type: data_analytics
# Type 'n' when asked if sensitive

# 3. Model (RECOMMENDED)
vercel env add MODEL production
# Type: claude-sonnet-4-20250514
# Type 'n' when asked if sensitive

# 4. Log Level (OPTIONAL)
vercel env add LOG_LEVEL production
# Type: INFO
# Type 'n' when asked if sensitive
```

## Step 3: Verify Variables

```bash
vercel env ls
```

Should show:
```
ANTHROPIC_API_KEY  production  [hidden]
DOMAIN             production  data_analytics
MODEL              production  claude-sonnet-4-20250514
LOG_LEVEL          production  INFO
```

## Step 4: Deploy to Production

```bash
vercel --prod
```

## Step 5: Verify Deployment

```bash
# Check health
curl https://data-analytics-agent.vercel.app/api/health

# Check config (should show analytics domain)
curl https://data-analytics-agent.vercel.app/api/config
```

## Troubleshooting

If you get errors:
1. Make sure `vercel.json` is correct (we fixed the output directory)
2. Check that all environment variables are set: `vercel env ls`
3. Check deployment logs: `vercel logs`

