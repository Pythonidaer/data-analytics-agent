/**
 * Test file to verify analytics frontend configuration
 * 
 * This file documents the expected changes:
 * 1. Quick actions should match data_analytics.json
 * 2. Colors should change from violet/purple to analytics theme
 * 3. App title should be "Data Analytics Expert Agent"
 * 4. Welcome message should reflect analytics domain
 */

// Expected analytics quick actions (from config/domains/data_analytics.json):
export const EXPECTED_ANALYTICS_QUICK_ACTIONS = [
  {
    label: "Create a metrics dictionary",
    message: "Help me define KPIs for this goal and produce a metrics dictionary.",
    icon: "📊"
  },
  {
    label: "Generate an event tracking plan",
    message: "Create a tracking plan for the key user journey. Assume Segment-style events.",
    icon: "📈"
  },
  {
    label: "Draft SQL for funnel + retention",
    message: "Draft SQL templates for a funnel and retention analysis. Ask about table grain first.",
    icon: "💾"
  },
  {
    label: "Data quality checklist",
    message: "Create a data quality checklist and tests for this dataset and KPI.",
    icon: "✅"
  }
];

// Analytics color theme (blue/teal instead of violet/purple)
export const ANALYTICS_COLORS = {
  primary: "from-blue-500 to-cyan-600",
  primaryHover: "from-blue-600 to-cyan-700",
  accent: "blue",
  iconGradient: "from-blue-500 to-cyan-600",
};

// PMM color theme (current)
export const PMM_COLORS = {
  primary: "from-violet-500 to-purple-600",
  primaryHover: "from-violet-600 to-purple-700",
  accent: "violet",
  iconGradient: "from-violet-500 to-purple-600",
};

