"""
Research Tools - Benchmark Research and Context Gathering.

These tools gather external context, benchmarks, and comparable
definitions for analytics work.
"""

from langchain_core.tools import tool
from typing import Optional

# Reuse fetch_url from PMM tools since it's domain-agnostic
from ....tools.research import fetch_url


@tool
def lookup_benchmark_ranges(
    metric_name: str,
    industry: Optional[str] = None,
    company_stage: Optional[str] = None,
) -> str:
    """
    Look up industry benchmark ranges for a metric.
    
    Use this tool to understand what "good" looks like for a metric
    before designing the measurement. Helps set expectations and
    identify outliers.
    
    Args:
        metric_name: The metric to look up benchmarks for (e.g., "activation_rate", "retention_7d")
        industry: Optional industry filter (SaaS, e-commerce, marketplace, etc.)
        company_stage: Optional company stage (startup, growth, enterprise)
    
    Returns:
        Benchmark ranges and context for the metric
    """
    benchmarks = f"""
## Benchmark Research: {metric_name}

### Industry Context
{industry if industry else "General benchmarks (not industry-specific)"}
{company_stage if company_stage else "General benchmarks (not stage-specific)"}

### Benchmark Ranges

**Typical Range**: [Range based on metric type]
**Good**: [Above-average threshold]
**Excellent**: [Top-quartile threshold]
**Concerning**: [Below-average threshold]

### Metric-Specific Benchmarks

**For {metric_name}:**
- **SaaS B2B**: [Typical range]
- **SaaS B2C**: [Typical range]
- **Marketplace**: [Typical range]
- **E-commerce**: [Typical range]

### Sources & Notes
- Industry reports and surveys
- Public company metrics (where available)
- Analyst benchmarks
- Community benchmarks (Reddit, forums)

### Caveats
- Benchmarks vary widely by business model
- Stage of company matters significantly
- Geography can affect benchmarks
- Use as directional guidance, not absolute targets

### Recommended Next Steps
1. Compare your current metric to these benchmarks
2. Identify if you're in a "good" range or need improvement
3. Set realistic targets based on benchmarks and business context
"""
    return benchmarks

