"""
Clean the FoodHub analytical dataset (approved cleaning plan, Section 2.6).

Actions (no rows dropped; row count stays 1,898):
  1. Missing ratings   -> KEEP as NaN (rating_value); never imputed.
  2. Garbled names      -> fix mojibake/encoding corruption to intended names.
  3. Whitespace         -> strip all restaurant names.
  4. Rare cuisines      -> ADD cuisine_grouped (<20 orders bucketed as "Other").
  5. Long-tail venues   -> KEEP all; ADD is_low_volume_restaurant flag (<=3 orders).
Popularity counts are recomputed AFTER name fixes so merged names aggregate
correctly. Original columns are preserved.

Input : data/processed/foodhub_analytical.csv
Output: data/processed/foodhub_analytical_clean.csv
"""

from pathlib import Path
import pandas as pd

IN = Path("data/processed/foodhub_analytical.csv")
OUT = Path("data/processed/foodhub_analytical_clean.csv")

RARE_CUISINE_THRESHOLD = 20      # cuisines with fewer orders -> "Other"
LOW_VOLUME_THRESHOLD = 3         # restaurants with <= this many orders -> flagged

# Explicit corrections for corrupted/garbled restaurant names.
NAME_FIXES = {
    "Big Wong Restaurant \x8c_¤¾Ñ¼": "Big Wong Restaurant",
    "Joe's Shanghai \x8e_À\x8eü£¾÷´": "Joe's Shanghai",
    "CafÌ© China": "Café China",
    "DespaÌ±a": "Despaña",
}


def clean() -> tuple[pd.DataFrame, dict]:
    df = pd.read_csv(IN)
    report = {"rows_in": len(df)}

    # --- 3. Whitespace on restaurant names --------------------------------
    df["restaurant_name"] = df["restaurant_name"].str.strip()

    # --- 2. Fix garbled names (apply after strip; keys already stripped) ---
    fixes = {k.strip(): v for k, v in NAME_FIXES.items()}
    n_before = df["restaurant_name"].nunique()
    df["restaurant_name"] = df["restaurant_name"].replace(fixes)
    report["names_before"] = n_before
    report["names_after"] = df["restaurant_name"].nunique()
    report["names_fixed"] = list(fixes.values())

    # --- 6. Recompute popularity counts AFTER name cleaning ---------------
    df["restaurant_order_count"] = df.groupby("restaurant_name")["order_id"].transform("count")
    df["cuisine_order_count"] = df.groupby("cuisine_type")["order_id"].transform("count")

    # --- 4. Rare cuisines -> grouped helper column ------------------------
    cuisine_counts = df["cuisine_type"].value_counts()
    rare = cuisine_counts[cuisine_counts < RARE_CUISINE_THRESHOLD].index.tolist()
    df["cuisine_grouped"] = df["cuisine_type"].where(~df["cuisine_type"].isin(rare), "Other")
    report["rare_cuisines_bucketed"] = rare

    # --- 5. Long-tail restaurants -> flag only ----------------------------
    df["is_low_volume_restaurant"] = df["restaurant_order_count"].le(LOW_VOLUME_THRESHOLD)
    report["low_volume_restaurants"] = int(
        df.loc[df["is_low_volume_restaurant"], "restaurant_name"].nunique()
    )

    # --- 1. Ratings: confirm kept as NaN (no imputation) ------------------
    report["ratings_missing_kept_nan"] = int(df["rating_value"].isna().sum())
    report["rows_out"] = len(df)
    return df, report


def main() -> None:
    df, rep = clean()
    df.to_csv(OUT, index=False)
    print(f"Wrote {OUT}  shape={df.shape}\n")
    print("Cleaning summary")
    print("-" * 50)
    print(f"  rows in / out           : {rep['rows_in']} / {rep['rows_out']}  (none dropped)")
    print(f"  unique names before/after: {rep['names_before']} -> {rep['names_after']}")
    print(f"  garbled names fixed     : {rep['names_fixed']}")
    print(f"  rare cuisines -> 'Other': {rep['rare_cuisines_bucketed']}")
    print(f"  low-volume restaurants flagged (<=3 orders): {rep['low_volume_restaurants']}")
    print(f"  missing ratings kept as NaN: {rep['ratings_missing_kept_nan']}")
    # Post-clean integrity: only legitimately-accented names should remain.
    print("\nRemaining non-ASCII names (expected: only Café China / Despaña):")
    mask = df["restaurant_name"].apply(lambda s: any(ord(c) > 127 for c in s))
    print("  ", sorted(df.loc[mask, "restaurant_name"].unique().tolist()))
    print(f"\n  cuisine_grouped counts: {df['cuisine_grouped'].value_counts().to_dict()}")


if __name__ == "__main__":
    main()
