"""
Risk Tools - Data Quality Checks and Risk Assessment.

These tools ensure trust in data and identify potential issues
before shipping insights.
"""

from langchain_core.tools import tool
from typing import Optional


@tool
def assess_analytics_risks(
    analysis_description: str,
    kpi: Optional[str] = None,
) -> str:
    """
    Assess risks and potential issues with an analytics analysis.
    
    Use this tool to identify bias, confounding variables, data quality issues,
    and other risks that could invalidate insights.
    
    Args:
        analysis_description: Description of the analysis being performed
        kpi: Optional KPI being measured
    
    Returns:
        Risk assessment with warnings and mitigation strategies
    """
    risk_assessment = f"""
## Analytics Risk Assessment

### Analysis Description
{analysis_description}

### KPI Being Measured
{kpi if kpi else "KPI not specified"}

### Risk Categories

#### 1. Data Quality Risks
- [ ] **Uniqueness**: Are there duplicate records at the grain?
- [ ] **Completeness**: Are there unexpected nulls?
- [ ] **Freshness**: Is data updated within SLA?
- [ ] **Validity**: Are values within expected ranges?
- [ ] **Consistency**: Do joins produce expected row counts?

**Mitigation**: Use `create_data_quality_checklist` to design tests.

#### 2. Bias & Confounding Risks
- [ ] **Selection Bias**: Is the sample representative?
- [ ] **Time-based Bias**: Are we comparing apples to apples?
- [ ] **Confounding Variables**: Are there hidden factors affecting results?
- [ ] **Survivorship Bias**: Are we only looking at successful cases?

**Example Confounders:**
- Seasonality (holidays, weekends)
- External events (marketing campaigns, product launches)
- User segments (new vs returning, plan tiers)
- Platform differences (web vs mobile)

#### 3. Interpretation Risks
- [ ] **Correlation vs Causation**: Are we inferring causality incorrectly?
- [ ] **Statistical Significance**: Is the sample size sufficient?
- [ ] **Edge Cases**: Are we handling nulls, duplicates, outliers correctly?
- [ ] **Context Missing**: Do stakeholders understand limitations?

#### 4. Implementation Risks
- [ ] **SQL Logic Errors**: Are joins and aggregations correct?
- [ ] **Grain Mismatch**: Are we mixing grains incorrectly?
- [ ] **Time Window Issues**: Are date filters correct?
- [ ] **Segment Definitions**: Are segment filters consistent?

### High-Risk Scenarios

**🚨 High Risk:**
- Making product decisions based on unvalidated data
- Comparing metrics with different definitions
- Ignoring confounding variables in experiments
- Shipping insights without data quality checks

**⚠️ Medium Risk:**
- Metrics without clear definitions
- Analysis without context (benchmarks, trends)
- Missing edge case handling
- Unclear grain or time windows

**✅ Low Risk:**
- Well-defined metrics with documented caveats
- Data quality tests in place
- Confounding variables identified
- Clear interpretation guidelines

### Recommended Mitigations
1. Run data quality tests before shipping
2. Document all assumptions and caveats
3. Identify and control for confounding variables
4. Validate SQL logic with edge cases
5. Provide context (benchmarks, trends) with insights
6. Set up alerts for data quality issues

### Next Steps
1. Use `create_data_quality_checklist` to design specific tests
2. Review SQL queries for grain consistency
3. Document assumptions and limitations
4. Set up monitoring for identified risks
"""
    return risk_assessment


@tool
def create_data_quality_checklist(
    dataset: str,
    kpi: Optional[str] = None,
) -> str:
    """
    Create a data quality checklist and dbt-style test ideas.
    
    Use this to design data quality tests that ensure trust in data
    before shipping insights. Follows dbt testing mindset.
    
    Args:
        dataset: Description of the dataset/table being tested
        kpi: Optional KPI that depends on this dataset
    
    Returns:
        Data quality checklist with dbt-style test recommendations
    """
    dq_checklist = f"""
## Data Quality Checklist

### Dataset
{dataset}

### KPI Dependency
{kpi if kpi else "No specific KPI - general data quality checks"}

### Data Quality Tests

#### 1. Uniqueness Tests
```sql
-- Test: No duplicate records at grain
-- dbt test: unique
SELECT 
  user_id,  -- or event_id, account_id, etc.
  COUNT(*) as count
FROM {dataset}
GROUP BY user_id
HAVING COUNT(*) > 1;
-- Expected: 0 rows
```

#### 2. Not Null Tests
```sql
-- Test: Required columns are not null
-- dbt test: not_null
SELECT COUNT(*) 
FROM {dataset}
WHERE user_id IS NULL 
   OR occurred_at IS NULL;  -- adjust columns as needed
-- Expected: 0 rows
```

#### 3. Accepted Values Tests
```sql
-- Test: Values are within expected ranges
-- dbt test: accepted_values
SELECT DISTINCT status
FROM {dataset}
WHERE status NOT IN ('active', 'inactive', 'pending');
-- Expected: 0 rows (or handle expected values)
```

#### 4. Relationships Tests
```sql
-- Test: Foreign key relationships are valid
-- dbt test: relationships
SELECT e.user_id
FROM events e
LEFT JOIN users u ON e.user_id = u.user_id
WHERE u.user_id IS NULL;
-- Expected: 0 rows (all events have valid users)
```

#### 5. Freshness Tests
```sql
-- Test: Data is updated within SLA
-- dbt test: custom (check max timestamp)
SELECT 
  MAX(updated_at) as last_update,
  CURRENT_TIMESTAMP - MAX(updated_at) as age
FROM {dataset};
-- Expected: age < SLA threshold (e.g., 1 hour, 1 day)
```

#### 6. Custom Business Logic Tests
```sql
-- Test: Business rules are enforced
-- Example: No negative values for revenue
SELECT COUNT(*) 
FROM orders
WHERE revenue < 0;
-- Expected: 0 rows
```

### dbt Test Configuration

```yaml
# models/schema.yml
models:
  - name: {dataset}
    tests:
      - unique:
          column_name: user_id
      - not_null:
          column_name: user_id
      - not_null:
          column_name: occurred_at
      - relationships:
          to: ref('users')
          field: user_id
      - dbt_utils.accepted_range:
          column_name: revenue
          min_value: 0
          max_value: 1000000
```

### Test Execution Strategy

**Before Shipping Insights:**
1. ✅ Run uniqueness tests
2. ✅ Run not_null tests on required columns
3. ✅ Run freshness tests
4. ✅ Run relationship tests (if applicable)
5. ✅ Run custom business logic tests

**Ongoing Monitoring:**
- Schedule tests to run daily/hourly
- Set up alerts for test failures
- Document test results in data quality dashboard
- Review and update tests as data evolves

### Edge Cases to Test

- **Null Handling**: What happens with NULL values in aggregations?
- **Duplicate Handling**: Are duplicates filtered or counted?
- **Time Boundaries**: Are date filters inclusive/exclusive?
- **Empty Results**: What if no data matches the filter?
- **Data Type Mismatches**: Are joins on compatible types?

### Next Steps
1. Implement tests in dbt (or your testing framework)
2. Set up automated test runs
3. Create data quality dashboard
4. Document test results and SLAs
5. Set up alerts for test failures
"""
    return dq_checklist

