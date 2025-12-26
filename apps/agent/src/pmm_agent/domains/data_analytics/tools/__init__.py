"""
Data Analytics Agent Tools.

Tools are organized by workflow phase:
- INTAKE: Analytics intake and KPI clarification
- RESEARCH: Benchmark research and context gathering
- PLANNING: Metrics dictionary, tracking plans, SQL templates, dashboard specs
- RISK: Data quality checks and risk assessment
"""

from .intake import (
    capture_analytics_intake,
    clarify_kpi_and_decision,
)

from .research import (
    fetch_url,
    lookup_benchmark_ranges,
)

from .planning import (
    create_metrics_dictionary,
    generate_tracking_plan,
    draft_sql_query_pack,
    create_dashboard_spec,
)

from .risk import (
    assess_analytics_risks,
    create_data_quality_checklist,
)

# Tool categories for mode-based selection
INTAKE_TOOLS = [
    capture_analytics_intake,
    clarify_kpi_and_decision,
]

RESEARCH_TOOLS = [
    fetch_url,
    lookup_benchmark_ranges,
]

PLANNING_TOOLS = [
    create_metrics_dictionary,
    generate_tracking_plan,
    draft_sql_query_pack,
    create_dashboard_spec,
]

RISK_TOOLS = [
    assess_analytics_risks,
    create_data_quality_checklist,
]

ALL_TOOLS = INTAKE_TOOLS + RESEARCH_TOOLS + PLANNING_TOOLS + RISK_TOOLS

