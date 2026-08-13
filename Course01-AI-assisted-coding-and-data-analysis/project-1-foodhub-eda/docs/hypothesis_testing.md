# Hypothesis Testing — Plan

*Prepared after reviewing `docs/problem_definition.txt`. This document is a **plan
only** — it specifies how each hypothesis will be tested. **No tests are run until this
plan is reviewed and approved.***

**Global settings**
- Significance level: **α = 0.05**
- Data source: `data/processed/foodhub_analytical_clean.csv` (1,898 orders)
- For each test we report the test statistic, p-value, the effect size / practical
  magnitude, and a plain-language decision (reject / fail to reject H₀).
- Where a parametric test's assumptions are doubtful, a non-parametric equivalent is
  run as a robustness check and both are reported.

---

## Hypothesis 1 — Weekend orders take longer to fulfill

- **Business claim:** Mean total fulfillment time is higher on weekends than weekdays.
- **Variables:** `total_fulfillment_time` (numeric, minutes) vs `day_of_the_week`
  (Weekend / Weekday).
- **Data subset:** All 1,898 orders (Weekend n=1,351; Weekday n=547). No rows excluded.
- **Hypotheses (one-tailed, directional):**
  - H₀: mean_weekend ≤ mean_weekday
  - H₁: mean_weekend > mean_weekday
- **Primary test:** **Welch's two-sample t-test** (independent samples, unequal
  variances not assumed), one-sided.
- **Robustness test:** **Mann–Whitney U** (one-sided) — distribution-free, in case
  normality is questioned.
- **Assumptions & checks:**
  - Independence of orders — assumed by design.
  - Approximate normality of the group means — justified by large n (CLT); the
    distributions are also roughly symmetric. Verified visually.
  - Welch's t-test does not require equal variances.
- **Metric reported:** difference in mean total fulfillment time (minutes) + Cohen's d.

---

## Hypothesis 2 — Faster fulfillment is associated with higher rating

- **Business claim:** Shorter total fulfillment time is associated with higher customer
  ratings (an inverse relationship).
- **Variables:** `total_fulfillment_time` (numeric) vs `rating_value` (ordinal: 3, 4, 5).
- **Data subset:** **Rated orders only** — `rating_value` not null (n = 1,162). The 736
  "Not given" orders are excluded, and this response-bias limitation is reported with
  the result.
- **Hypotheses (one-tailed, directional):**
  - H₀: no negative association (ρ ≥ 0) between fulfillment time and rating.
  - H₁: negative association (ρ < 0) — faster orders rate higher.
- **Primary test:** **Spearman rank correlation** (ρ) between `total_fulfillment_time`
  and `rating_value` — appropriate because rating is ordinal.
- **Robustness test:** **Kruskal–Wallis** comparing `total_fulfillment_time`
  distributions across the three rating groups (3 vs 4 vs 5).
- **Assumptions & checks:**
  - Spearman needs only a monotonic relationship + ordinal/continuous data — satisfied.
  - Kruskal–Wallis is non-parametric (no normality assumption).
- **Metric reported:** Spearman ρ (and its p-value); group median fulfillment times.

---

## Hypothesis 3 — Demand & revenue are concentrated in a few restaurants / cuisines

- **Business claim:** A small subset of restaurants and cuisines accounts for a
  disproportionate share of orders and revenue (Pareto-style concentration).
- **Variables:** `restaurant_name`, `cuisine_type`, `cost_of_the_order`.
- **Data subset:** All 1,898 orders.
- **Nature of the analysis:** This is a **concentration / distributional** claim, not a
  two-group comparison, so it is assessed descriptively rather than with a classic
  significance test:
  - Cumulative share of orders and revenue by ranked restaurant and cuisine (Pareto).
  - **Gini coefficient** of the order-count distribution across restaurants as a single
    concentration score.
  - Optional supporting test: **chi-square goodness-of-fit** that orders are *not*
    uniformly distributed across cuisines (H₀: uniform; H₁: non-uniform).
- **Metric reported:** % of orders/revenue from the top-k restaurants and cuisines;
  Gini coefficient; chi-square statistic and p-value (if run).
- **Note:** Because H3 is descriptive and already strongly evidenced by the EDA, it is
  the natural candidate to de-scope if a leaner, purely inferential testing set is
  preferred.

---

## Summary table

| # | Hypothesis | Primary test | Data subset | Tail |
|---|-----------|--------------|-------------|------|
| H1 | Weekend fulfillment slower | Welch's t-test (+ Mann–Whitney) | All 1,898 | One-sided |
| H2 | Faster → higher rating | Spearman ρ (+ Kruskal–Wallis) | Rated only (1,162) | One-sided |
| H3 | Demand/revenue concentrated | Pareto + Gini (+ chi-square GoF) | All 1,898 | n/a (descriptive) |

---

**Awaiting approval.** On approval I will run these tests, report results with effect
sizes and clear decisions, and honor any scope change (e.g., testing only a subset of
the hypotheses).
