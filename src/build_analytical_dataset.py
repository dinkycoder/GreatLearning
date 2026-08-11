"""
Build the FoodHub analytical dataset.

Reads the raw order file and engineers features needed for descriptive analysis
and later hypothesis testing. This step does NOT clean, drop, or impute any
values (that happens in the approval-gated cleaning step); it only ADDS derived
columns while preserving every original field.

Input : data/raw/foodhub_order.csv
Output: data/processed/foodhub_analytical.csv
"""

from pathlib import Path
import pandas as pd

RAW = Path("data/raw/foodhub_order.csv")
OUT = Path("data/processed/foodhub_analytical.csv")


def build() -> pd.DataFrame:
    df = pd.read_csv(RAW)

    # --- 1. Operational efficiency (KPI 1) --------------------------------
    # Total time the customer waits: kitchen prep + delivery.
    df["total_fulfillment_time"] = (
        df["food_preparation_time"] + df["delivery_time"]
    )
    # How the wait splits between kitchen and road (share of total).
    df["prep_time_share"] = (df["food_preparation_time"] / df["total_fulfillment_time"]).round(3)
    df["delivery_time_share"] = (df["delivery_time"] / df["total_fulfillment_time"]).round(3)

    # --- 2. Satisfaction (KPI 2) ------------------------------------------
    # rating is stored as text with a "Not given" placeholder. Create a numeric
    # version (placeholder -> NaN) and an explicit "did the customer rate?" flag.
    df["rating_given"] = df["rating"].ne("Not given")
    df["rating_value"] = pd.to_numeric(
        df["rating"].where(df["rating_given"]), errors="coerce"
    )
    # Promoter = rated 4 or 5 (only meaningful where a rating exists).
    df["is_promoter"] = df["rating_value"].ge(4)

    # --- 3. Time context --------------------------------------------------
    df["is_weekend"] = df["day_of_the_week"].eq("Weekend")

    # --- 4. Value / cost banding (KPI 3) ----------------------------------
    # Business-friendly price tiers using tertile cut points on order cost.
    df["cost_band"] = pd.qcut(
        df["cost_of_the_order"], q=3, labels=["Low", "Medium", "High"]
    )

    # --- 5. Customer behaviour --------------------------------------------
    # Order frequency per customer -> repeat vs one-time (proxy for loyalty,
    # since no time-based cohorts are possible without timestamps).
    order_counts = df.groupby("customer_id")["order_id"].transform("count")
    df["customer_order_count"] = order_counts
    df["is_repeat_customer"] = order_counts.gt(1)

    # --- 6. Popularity of restaurant / cuisine (KPI 3) --------------------
    df["restaurant_order_count"] = df.groupby("restaurant_name")["order_id"].transform("count")
    df["cuisine_order_count"] = df.groupby("cuisine_type")["order_id"].transform("count")

    return df


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df = build()
    df.to_csv(OUT, index=False)

    print(f"Wrote {OUT}  shape={df.shape}")
    print("\nColumns:")
    for c in df.columns:
        print(f"  - {c:<24} {str(df[c].dtype)}")
    print("\nEngineered-feature sanity checks:")
    print(f"  total_fulfillment_time: {df.total_fulfillment_time.min()}-{df.total_fulfillment_time.max()} "
          f"mean {df.total_fulfillment_time.mean():.1f}")
    print(f"  rating_given True: {df.rating_given.sum()} / {len(df)} "
          f"({df.rating_given.mean()*100:.1f}%)")
    print(f"  rating_value non-null: {df.rating_value.notna().sum()}")
    print(f"  is_repeat_customer True: {df.is_repeat_customer.sum()}")
    print(f"  cost_band counts: {df.cost_band.value_counts().sort_index().to_dict()}")


if __name__ == "__main__":
    main()
