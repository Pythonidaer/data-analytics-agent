"""
Intake Tools - Analytics Intake and KPI Clarification.

These tools help structure analytics requests and clarify
what decision the analysis should inform.
"""

from langchain_core.tools import tool
from typing import Optional


@tool
def capture_analytics_intake(
    goal: str,
    product_context: Optional[str] = None,
    constraints: Optional[str] = None,
) -> str:
    """
    Capture and structure an analytics request to understand the full context.
    
    Use this tool when starting any analytics project to structure the inputs,
    identify the decision being informed, and surface unknowns.
    
    Args:
        goal: The business goal or question that needs to be answered
        product_context: Optional context about the product/feature being analyzed
        constraints: Optional constraints (time, data availability, resources)
    
    Returns:
        Structured intake with decision statement, key questions, assumptions, and unknowns
    """
    intake = f"""
## Analytics Intake & Definition

### Business Goal
{goal}

### Product Context
{product_context if product_context else "No product context provided - will need to clarify"}

### Constraints
{constraints if constraints else "No constraints specified"}

### Decision Statement
**What decision will this analysis inform?**
[To be clarified - this is the most critical question]

### Key Questions to Answer
1. **Decision Question**: What action will be taken based on this analysis?
2. **Primary KPI**: What metric will we measure? (formula, grain, inclusion/exclusion)
3. **Data Sources**: What tables/events exist? At what grain?
4. **Time Window**: What timeframe matters? What segments?

### Assumptions
- [Assumption 1: To be documented]
- [Assumption 2: To be documented]

### Unknowns & Gaps
- [ ] Decision question not yet clarified
- [ ] KPI definition incomplete
- [ ] Data sources/grain unclear
- [ ] Time window/segments undefined
- [ ] Validation plan missing

### Recommended Next Steps
1. Use `clarify_kpi_and_decision` to nail down the decision question and KPI
2. Identify data sources and grain
3. Define time window and segments
4. Proceed to planning phase once intake is complete
"""
    return intake


@tool
def clarify_kpi_and_decision(
    decision_question: str,
    kpi_name: str,
    kpi_formula: Optional[str] = None,
    grain: Optional[str] = None,
) -> str:
    """
    Clarify the decision question and KPI definition.
    
    Use this tool to ensure the analysis has a clear "so what" and
    a well-defined metric before proceeding to measurement design.
    
    Args:
        decision_question: What decision will this analysis inform? (the 'so what')
        kpi_name: Name of the primary KPI
        kpi_formula: Optional formula for the KPI
        grain: Optional data grain (user, event, account, order, etc.)
    
    Returns:
        Clarified decision statement and KPI definition
    """
    clarification = f"""
## Decision & KPI Clarification

### Decision Statement
**What decision will this analysis inform?**
{decision_question}

### Primary KPI Definition

**KPI Name**: {kpi_name}

**Formula**: {kpi_formula if kpi_formula else "[To be defined - need exact calculation]"}
**Grain**: {grain if grain else "[To be defined - user/event/account/order]"}
**Inclusion Rules**: [What counts?]
**Exclusion Rules**: [What doesn't count?]
**Time Window**: [What timeframe?]
**Segments**: [What segments matter?]

### Validation Checklist
- [ ] Decision question is clear and actionable
- [ ] KPI formula is unambiguous
- [ ] Grain is explicitly stated
- [ ] Inclusion/exclusion rules are defined
- [ ] Time window is specified
- [ ] Segments are identified

### Next Steps
Once all items above are checked, proceed to:
- `create_metrics_dictionary` to formalize the KPI definition
- `draft_sql_query_pack` to design the measurement queries
"""
    return clarification

