# Environment Variables Reference

> Quick reference for all environment variables used by the Data Analytics Agent

## Required Environment Variables

### `ANTHROPIC_API_KEY`
**Required:** Yes  
**Description:** Your Anthropic API key for Claude API access  
**Example:** `sk-ant-api03-xxxxxxxxxxxxx`  
**Where to get:** [console.anthropic.com](https://console.anthropic.com)

**Set locally:**
```bash
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

**Set in Vercel:**
```bash
vercel env add ANTHROPIC_API_KEY production
# Paste your key when prompted
```

---

## Domain Selection (New for Analytics)

### `DOMAIN`
**Required:** No (defaults to "pmm" for backward compatibility)  
**Description:** Selects which domain agent to use  
**Options:** 
- `pmm` - Product Marketing Manager agent (default)
- `data_analytics` - Data Analytics Expert Agent

**Set locally:**
```bash
export DOMAIN=data_analytics
```

**Set in Vercel:**
```bash
vercel env add DOMAIN production
# Enter: data_analytics
```

**Note:** This will be wired up in `server.py` next - currently defaults to PMM.

---

## Optional Environment Variables

### `MODEL`
**Required:** No  
**Default:** `claude-sonnet-4-20250514`  
**Description:** Claude model to use  
**Options:**
- `claude-sonnet-4-20250514` (default, most capable)
- `claude-3-5-haiku-20241022` (cheaper, faster)
- `claude-3-5-sonnet-20241022` (middle ground)

**Set locally:**
```bash
export MODEL=claude-sonnet-4-20250514
```

### `MAX_MESSAGE_HISTORY`
**Required:** No  
**Default:** `100`  
**Description:** Maximum number of messages to keep in conversation history (prevents token bloat)

**Set locally:**
```bash
export MAX_MESSAGE_HISTORY=100
```

### `LOG_LEVEL`
**Required:** No  
**Default:** `INFO`  
**Description:** Logging verbosity level  
**Options:** `DEBUG`, `INFO`, `WARNING`, `ERROR`

**Set locally:**
```bash
export LOG_LEVEL=INFO
```

### `ALLOWED_ORIGINS`
**Required:** No (defaults to `*` in dev, empty in production)  
**Description:** Comma-separated list of allowed CORS origins  
**Example:** `https://my-app.vercel.app,https://www.myapp.com`

**Set locally:**
```bash
export ALLOWED_ORIGINS=http://localhost:3003
```

**Set in Vercel:**
```bash
vercel env add ALLOWED_ORIGINS production
# Enter: https://your-app.vercel.app
```

---

## Quick Setup for Local Development

```bash
# In apps/agent directory
cd apps/agent
source .venv/bin/activate

# Required
export ANTHROPIC_API_KEY=sk-ant-your-key-here

# For analytics domain (after we wire it up)
export DOMAIN=data_analytics

# Optional
export MODEL=claude-sonnet-4-20250514
export LOG_LEVEL=INFO
export MAX_MESSAGE_HISTORY=100

# Start server
python3 -m uvicorn src.pmm_agent.server:app --port 8123
```

---

## Quick Setup for Vercel Production

```bash
# Required
vercel env add ANTHROPIC_API_KEY production
# Paste your key

# Domain selection (after we wire it up)
vercel env add DOMAIN production
# Enter: data_analytics

# Optional
vercel env add MODEL production
# Enter: claude-sonnet-4-20250514

vercel env add LOG_LEVEL production
# Enter: INFO
```

---

## Current Status

**Already Working:**
- ✅ `ANTHROPIC_API_KEY` - Required, already in use
- ✅ `MODEL` - Optional, already in use
- ✅ `MAX_MESSAGE_HISTORY` - Optional, already in use
- ✅ `LOG_LEVEL` - Optional, already in use
- ✅ `ALLOWED_ORIGINS` - Optional, already in use

**To Be Wired Up:**
- ⚠️ `DOMAIN` - New variable, needs to be added to `server.py` to switch between PMM and analytics agents

---

## Next Steps

1. Wire up `DOMAIN` env var in `server.py` to use `create_analytics_agent()` when `DOMAIN=data_analytics`
2. Test domain switching locally
3. Update frontend quick actions
4. Deploy to Vercel with `DOMAIN=data_analytics`

