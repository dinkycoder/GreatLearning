# Key Observations — FoodHub Order Analysis

*A narrative synthesis of the univariate, bivariate, and multivariate analyses.*
*These are qualitative observations from the exploratory visuals; formal statistical
confirmation follows in the hypothesis-testing step.*

---

## The story in one paragraph

FoodHub's order book tells a story of **concentrated demand, uniform operations, and
quietly positive — but poorly measured — satisfaction.** A handful of restaurants and
two cuisines carry most of the business; the delivery machine runs at a remarkably
consistent ~51-minute pace regardless of when, what, or how much is ordered; and
customers who bother to rate are happy, but nearly four in ten never rate at all. The
levers that *look* like they should matter for satisfaction and loyalty — speed, day of
week, basket size — barely move the needle in this data. What matters is **who you
order from and how often you come back**, not how fast or how much.

---

## 1. The demand picture — a top-heavy marketplace

The single most striking pattern is **concentration**. Across 1,898 orders from 178
restaurants:

- **Two cuisines dominate.** American (584 orders) and Japanese (470) alone make up
  ~56% of all orders; adding Italian and Chinese brings the top four to ~83%. The
  remaining ten cuisines are a long tail, six of them with fewer than 20 orders each.
- **A few restaurants carry the business.** Shake Shack (219 orders) leads by a wide
  margin, and the **top 5 restaurants account for ~33% of all orders**. Meanwhile
  **96 of 178 restaurants have 3 or fewer orders** — a very long tail of low-volume
  venues.
- The Pareto curve makes it explicit: a **minority of restaurants generate ~80% of
  orders.**

The multivariate view sharpened this: when cuisines are plotted by demand versus
average cost, **average order cost is nearly identical across cuisines (~$15–18)**.
Revenue leadership is therefore driven by **volume, not premium pricing** — American
and Japanese win because more people order them, not because those orders are bigger.

> **Business meaning:** FoodHub's revenue rests on a small set of partners. Those
> partners are both its greatest asset and its greatest concentration risk.

---

## 2. The operations picture — impressively, almost suspiciously, uniform

The end-to-end wait — **total fulfillment time = preparation + delivery** — averages
**~51.5 minutes** (prep ~27 min, delivery ~24 min), and its most notable feature is how
*little it varies with anything*:

- **Weekends are not slower.** Despite weekends carrying ~71% of all orders
  (2.5× weekday volume), weekend and weekday fulfillment times are nearly identical
  (~51–52 min). The bivariate boxplots and the multivariate cuisine-by-day view agree:
  there is **no cuisine and no day where fulfillment clearly slows down.**
- **Cost and time are unrelated.** Bigger orders are not slower orders.
- **The correlation heatmap confirms it:** aside from the mechanical link between prep,
  delivery, and their sum, every numeric measure is essentially **uncorrelated** with
  every other. The operation behaves like a well-buffered, capacity-managed system.

> **Business meaning:** Operational performance is stable and does not degrade under
> weekend load — a genuine strength. It also means "speed" is unlikely to be the lever
> that differentiates good and bad experiences here.

---

## 3. The satisfaction picture — happy raters, but a measurement blind spot

Customer rating is the headline *data-quality* story as much as a satisfaction story:

- **~39% of orders were never rated** ("Not given"). This is the largest single bar in
  the entire analysis.
- **Among the 1,162 who did rate, sentiment is strongly positive:** ~51% gave 5, ~33%
  gave 4, ~16% gave 3 — and **no 1s or 2s appear at all.** Scores only span 3–5.
- Crucially, **rating does not move with the experience variables.** Mean rating holds
  flat at ~4.3 across fast/medium/slow deliveries, across weekdays and weekends, and
  across cost bands — a result that survived every conditioning we tried in the
  multivariate view.

> **Business meaning:** The service *appears* excellent, but this is measured on a
> self-selected minority with a compressed 3–5 scale. The absence of low scores likely
> reflects **who chooses to rate**, not the absence of bad experiences. The biggest
> satisfaction opportunity may be **measuring it better**, not just improving it.

---

## 4. The loyalty picture — loyalty is frequency, not spend

With no time axis available, "retention" was examined through its nearest proxy —
**repeat versus one-time customers**:

- **~65% of customers order once; ~35% return.** Yet the returning minority is
  disproportionately valuable, generating **~59% of all orders.**
- **Loyalty is weakly tied to delivery experience:** repeat-customer share drifts down
  as delivery slows (61% → 59% → 55% from fast to slow) — directionally sensible but a
  small effect.
- **Loyalty is *not* tied to spending.** Average order value is essentially identical
  for one-time ($16.52) and repeat ($16.34) customers, and the correlation between a
  customer's AOV and how often they order is ~0. Repeat customers spend more in
  *total* only because they place **more orders, not bigger ones.**

> **Business meaning:** Growing the business is about **converting one-time customers
> into repeat customers** (frequency), not about pushing larger baskets. The loyal core
> is where the value compounds.

---

## 5. How the three hypotheses look going into testing

| Hypothesis | What the visuals suggest | Confidence |
|---|---|---|
| **H1** — Weekend orders take longer to fulfill | Times are ~equal on weekends and weekdays | Looks **weak / likely null** |
| **H2** — Faster fulfillment → higher rating | Rating flat across speed tiers, even conditioned | Looks **weak / likely null** |
| **H3** — Demand & revenue concentrated in few restaurants/cuisines | Clear Pareto concentration; volume drives revenue | Looks **strong / likely supported** |

The exploratory evidence points to a clean split: the two *operational-experience*
hypotheses (H1, H2) appear weak, while the *market-structure* hypothesis (H3) appears
robust. The formal statistical tests will confirm or refute H1 and H2.

---

## 6. Caveats that shape every conclusion above

- **No order timestamps** — no true time trends, cohorts, or retention curves; all
  "retention" here is a lifetime-frequency proxy.
- **Rating non-response (~39%) and a compressed 3–5 scale** — satisfaction findings
  describe self-selected raters and may overstate true satisfaction.
- **No basket detail, delivery distance, or SLA target** — "items per order",
  "delivery delay", and "on-time rate" cannot be computed; revenue is a proxy via order
  cost.
- **Category imbalance** — small cuisines and single-order restaurants are unreliable
  individually and were grouped or flagged accordingly.

These do not block the core analysis, but they define its honest boundaries — and they
double as FoodHub's **data-collection wish list** for the next iteration: order
timestamps, delivery distance/SLA, basket contents, and a higher rating-response rate.
