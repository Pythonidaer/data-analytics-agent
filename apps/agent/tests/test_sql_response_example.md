# Example Response for SQL Template Request

## Good Response Structure

When the agent asks about your data structure for SQL templates, provide:

1. **Tables Available:**
   - List each table and its grain
   - Describe key relationships

2. **Key Columns:**
   - For each table, list important columns
   - Note data types if relevant (especially for timestamps, JSON fields)

3. **Funnel Events:**
   - List the ordered sequence of events
   - Note any alternative paths

4. **Retention Definition:**
   - What defines an "active" user
   - Time windows you care about (D1, D7, D30, weekly, monthly)

## Example Response

Here's a well-structured response:

---

**Tables and Grain:**

1. **events table** - Grain: **event-level** (one row per user action)
   - Key columns: `id`, `user_id` (nullable for anonymous), `session_id`, `occurred_at` (timestamp), `event_name` (string), `properties` (JSONB with metadata like `analysis_id`, `posting_count`, `source`), `anonymous_id` (optional, for pre-signup tracking)
   
2. **users table** - Grain: **user-level** (one row per user/account)
   - Key columns: `id`, `created_at` (timestamp), `plan` (string), `activated_at` (timestamp, first "aha" moment), `last_active_at` (timestamp, optional), plus auth identifiers
   
3. **Domain tables** (job_postings, analyses) - Exist separately, linked to users via foreign keys

**Funnel Progression Events (in order):**
1. `signup_completed`
2. `uploaded_job_postings` OR `viewed_demo` (alternative paths)
3. `analysis_started`
4. `analysis_completed`
5. `viewed_insights_dashboard`
6. `exported_report` OR `saved_filter` (alternative paths)

**Retention Definition:**
- **Active user**: User who returns and performs key events (`viewed_insights_dashboard` OR `analysis_completed`)
- **Time windows**: D1 (day 1), D7 (7 days), D30 (30 days), and weekly cohorts
- **Cohort basis**: Users grouped by signup date (from `users.created_at` or first `signup_completed` event)

**Notes:**
- Analytics is primarily driven by the events stream
- Some events may have `user_id` as NULL (anonymous users)
- Event properties in JSONB contain additional context (analysis_id, posting_count, source)

---

This structure makes it easy for the agent to:
- Understand your schema
- Generate accurate SQL queries
- Handle edge cases (null user_ids, JSON properties)
- Create funnel queries with the correct event sequence
- Build retention queries with the right time windows

