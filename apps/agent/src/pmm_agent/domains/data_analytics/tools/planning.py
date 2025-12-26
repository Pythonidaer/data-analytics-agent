"""
Planning Tools - Metrics Dictionary, Tracking Plans, SQL Templates, Dashboard Specs.

These tools design measurement and create the artifacts needed
to build analytics solutions.
"""

from langchain_core.tools import tool
from typing import Optional


@tool
def create_metrics_dictionary(
    goal: str,
    kpis_list: str,
    grain_hints: Optional[str] = None,
) -> str:
    """
    Create a metrics dictionary that defines KPIs for an analytics goal.
    
    Use this when a user wants to define KPIs and needs a structured
    metrics dictionary with formulas, grain, owners, and caveats.
    
    Args:
        goal: The business goal or objective
        kpis_list: Comma-separated list of KPIs to define
        grain_hints: Optional hints about data grain (user, event, account, etc.)
    
    Returns:
        Markdown table with metrics dictionary
    """
    kpis = [kpi.strip() for kpi in kpis_list.split(",")]
    
    metrics_dict = f"""
## Metrics Dictionary

### Goal
{goal}

### Metrics Definitions

| Metric Name | Formula | Grain | Owner | Data Source | Caveats |
|-------------|---------|-------|-------|-------------|---------|
"""
    
    for kpi in kpis:
        metrics_dict += f"""| {kpi} | [Formula to be defined] | {grain_hints if grain_hints else "[user/event/account]"} | [Owner TBD] | [Table/Event TBD] | [Caveats TBD] |
"""
    
    metrics_dict += f"""
### Grain Context
{grain_hints if grain_hints else "Grain not specified - will need to clarify: user, event, account, order, etc."}

### Next Steps
1. Fill in exact formulas for each metric
2. Identify data sources (tables, events)
3. Assign owners for each metric
4. Document caveats and edge cases
5. Use `draft_sql_query_pack` to create SQL templates for these metrics
"""
    return metrics_dict


@tool
def generate_tracking_plan(
    journey_description: str,
    entities: Optional[str] = None,
) -> str:
    """
    Generate an event tracking plan for a user journey.
    
    Use this to design event tracking for key user journeys,
    following Segment-style event naming conventions.
    
    Args:
        journey_description: Description of the user journey to track
        entities: Optional entities involved (user, account, order, etc.)
    
    Returns:
        Event tracking plan with events, properties, and examples
    """
    tracking_plan = f"""
## Event Tracking Plan

### Journey Description
{journey_description}

### Entities
{entities if entities else "Primary entity: user (assumed)"}

### Event Tracking Plan

| Event Name | Properties | Example Values | When to Fire |
|------------|------------|----------------|--------------|
| [Event 1] | [property_1, property_2] | [example values] | [Trigger condition] |
| [Event 2] | [property_1, property_2] | [example values] | [Trigger condition] |
| [Event 3] | [property_1, property_2] | [example values] | [Trigger condition] |

### Event Naming Convention
Following Segment-style naming:
- **Format**: `[Object] [Action]` (e.g., `User Signed Up`, `Order Completed`)
- **Past tense**: Use past tense for completed actions
- **CamelCase**: Use CamelCase for event names
- **Consistent**: Use consistent object names across events

### Property Guidelines
- **User properties**: user_id, email, plan_tier, signup_date
- **Event properties**: timestamp, session_id, device_type, referrer
- **Context properties**: page_url, feature_flag, experiment_id

### Example Events

**Sign-up Journey:**
- `User Viewed Signup Page` (properties: referrer, utm_source)
- `User Started Signup` (properties: email, signup_method)
- `User Completed Signup` (properties: user_id, plan_selected)

**Activation Journey:**
- `User Completed Onboarding` (properties: user_id, steps_completed)
- `User Performed First Value Action` (properties: user_id, action_type)

### Data Quality Considerations
- Ensure user_id is present on all user events
- Timestamp should be ISO 8601 format
- Validate required properties are not null
- Test event firing in staging before production
"""
    return tracking_plan


@tool
def draft_sql_query_pack(
    schema_hints: str,
    questions: str,
) -> str:
    """
    Draft SQL query templates for common analytics patterns.
    
    Use this to create SQL templates for funnels, retention, cohorts,
    and other common analytics queries. Always asks about table grain first.
    
    **CRITICAL: When this tool returns its output, you MUST display the COMPLETE output 
    to the user verbatim. Do NOT summarize or describe what it contains. Show all SQL 
    code blocks, all markdown, everything. The user needs the actual SQL to copy and use.**
    
    Args:
        schema_hints: Description of available tables/events (columns, grain, relationships)
        questions: Analytics questions to answer with SQL
    
    Returns:
        SQL query templates with comments explaining logic - SHOW THIS COMPLETE OUTPUT TO USER
    """
    sql_pack = f"""
## SQL Query Pack

**IMPORTANT: This entire output must be shown to the user verbatim. Do not summarize or describe - show the complete SQL code blocks.**

### Schema Context
{schema_hints}

### Questions to Answer
{questions}

### SQL Templates

#### Template 1: Activation Funnel
```sql
-- Analysis: Activation funnel
-- Grain: user
-- Time Window: Last 30 days
-- Assumes: events table with user_id, event_name, occurred_at

WITH funnel_steps AS (
  SELECT
    user_id,
    MAX(CASE WHEN event_name = 'signup_completed' THEN 1 ELSE 0 END) AS signed_up,
    MAX(CASE WHEN event_name = 'onboarding_completed' THEN 1 ELSE 0 END) AS onboarded,
    MAX(CASE WHEN event_name = 'first_value_action' THEN 1 ELSE 0 END) AS activated
  FROM events
  WHERE occurred_at >= CURRENT_DATE - INTERVAL '30 days'
    AND event_name IN ('signup_completed', 'onboarding_completed', 'first_value_action')
  GROUP BY user_id
)
SELECT
  COUNT(*) AS total_users,
  SUM(signed_up) AS signed_up_count,
  SUM(onboarded) AS onboarded_count,
  SUM(activated) AS activated_count,
  ROUND(100.0 * SUM(onboarded) / NULLIF(SUM(signed_up), 0), 2) AS signup_to_onboard_pct,
  ROUND(100.0 * SUM(activated) / NULLIF(SUM(onboarded), 0), 2) AS onboard_to_activate_pct
FROM funnel_steps;
```

#### Template 2: 7-Day Retention
```sql
-- Analysis: 7-day retention
-- Grain: user
-- Cohort: Users who signed up in the last 30 days
-- Retention Window: 7 days after signup

WITH cohorts AS (
  SELECT
    user_id,
    DATE_TRUNC('day', MIN(occurred_at)) AS cohort_date
  FROM events
  WHERE event_name = 'signup_completed'
    AND occurred_at >= CURRENT_DATE - INTERVAL '30 days'
  GROUP BY user_id
),
retention AS (
  SELECT
    c.cohort_date,
    c.user_id,
    CASE 
      WHEN EXISTS (
        SELECT 1 
        FROM events e
        WHERE e.user_id = c.user_id
          AND e.occurred_at BETWEEN c.cohort_date + INTERVAL '7 days' 
                                 AND c.cohort_date + INTERVAL '8 days'
      ) THEN 1 ELSE 0 
    END AS retained_7d
  FROM cohorts c
)
SELECT
  cohort_date,
  COUNT(*) AS cohort_size,
  SUM(retained_7d) AS retained_count,
  ROUND(100.0 * SUM(retained_7d) / COUNT(*), 2) AS retention_rate_7d
FROM retention
GROUP BY cohort_date
ORDER BY cohort_date DESC;
```

#### Template 3: Cohort Analysis
```sql
-- Analysis: Monthly cohort analysis
-- Grain: user
-- Metric: Active users per cohort

WITH cohorts AS (
  SELECT
    user_id,
    DATE_TRUNC('month', MIN(occurred_at)) AS cohort_month
  FROM events
  WHERE event_name = 'signup_completed'
  GROUP BY user_id
),
monthly_activity AS (
  SELECT
    c.cohort_month,
    DATE_TRUNC('month', e.occurred_at) AS activity_month,
    COUNT(DISTINCT e.user_id) AS active_users
  FROM cohorts c
  JOIN events e ON e.user_id = c.user_id
  WHERE e.occurred_at >= c.cohort_month
  GROUP BY c.cohort_month, DATE_TRUNC('month', e.occurred_at)
)
SELECT
  cohort_month,
  activity_month,
  active_users,
  DATE_PART('month', activity_month) - DATE_PART('month', cohort_month) AS months_since_signup
FROM monthly_activity
ORDER BY cohort_month DESC, activity_month;
```

### Grain Notes
**CRITICAL**: Always verify the grain of your tables:
- **Events table**: Usually grain = event (one row per event)
- **Users table**: Usually grain = user (one row per user)
- **Accounts table**: Usually grain = account (one row per account)

**Common Mistakes:**
- Joining events to users without aggregating events first
- Counting events when you meant to count users
- Mixing grains in the same query

### Validation Queries
```sql
-- Check for duplicates at grain
SELECT user_id, COUNT(*) 
FROM events 
GROUP BY user_id 
HAVING COUNT(*) > 1;

-- Check for nulls in key columns
SELECT COUNT(*) 
FROM events 
WHERE user_id IS NULL OR occurred_at IS NULL;

-- Check date ranges
SELECT MIN(occurred_at), MAX(occurred_at) 
FROM events;
```
"""
    return sql_pack


@tool
def create_dashboard_spec(
    metrics_list: str,
    audience: Optional[str] = None,
    update_frequency: Optional[str] = None,
) -> str:
    """
    Create a dashboard specification with chart recommendations.
    
    Use this to design dashboards that effectively communicate
    analytics insights to stakeholders.
    
    Args:
        metrics_list: Comma-separated list of metrics to include
        audience: Optional target audience (executives, product team, analysts)
        update_frequency: Optional update frequency (real-time, daily, weekly)
    
    Returns:
        Dashboard specification with chart types, filters, and layout
    """
    metrics = [m.strip() for m in metrics_list.split(",")]
    
    dashboard_spec = f"""
## Dashboard Specification

### Target Audience
{audience if audience else "General audience (will need to clarify)"}

### Update Frequency
{update_frequency if update_frequency else "Real-time (assumed)"}

### Metrics to Display
{', '.join(metrics)}

### Dashboard Layout

#### Section 1: Key Metrics (Top Row)
| Metric | Chart Type | Time Range | Notes |
|--------|------------|------------|-------|
"""
    
    for i, metric in enumerate(metrics[:4], 1):  # First 4 as key metrics
        dashboard_spec += f"| {metric} | Number/Sparkline | Last 30 days | Primary KPI |\n"
    
    dashboard_spec += f"""
#### Section 2: Trend Analysis
| Chart | Type | Metrics | Time Range |
|-------|------|---------|------------|
| Trend Over Time | Line Chart | {', '.join(metrics[:3])} | Last 90 days |
| Comparison | Bar Chart | {metrics[0] if metrics else 'Metric'} by Segment | Current period |

#### Section 3: Detailed Analysis
| Chart | Type | Purpose |
|-------|------|---------|
| Funnel | Funnel Chart | Conversion analysis |
| Cohort | Heatmap | Retention analysis |
| Distribution | Histogram | User behavior patterns |

### Chart Type Recommendations

**For {metrics[0] if metrics else 'Metrics'}:**
- **Trend**: Line chart (shows change over time)
- **Comparison**: Bar chart (compares segments)
- **Distribution**: Histogram (shows spread)
- **Funnel**: Funnel chart (shows conversion)
- **Cohort**: Heatmap (shows retention patterns)

### Filters & Drill-Downs
- **Time Range**: Last 7/30/90 days, custom range
- **Segments**: User type, plan tier, region
- **Dimensions**: Channel, feature, experiment

### Interactivity
- Click to drill down into details
- Hover for exact values
- Export to CSV/PDF
- Shareable links with filter state

### Next Steps
1. Build dashboard in BI tool (Tableau, Looker, Metabase, etc.)
2. Set up data refresh schedule
3. Add alerts for metric thresholds
4. Schedule regular review meetings
"""
    return dashboard_spec

