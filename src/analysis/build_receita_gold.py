import pandas as pd
from pathlib import Path

SILVER_PATH = Path(
    "data/silver/receita_stablecoin_activity.csv"
)

GOLD_PATH = Path(
    "data/gold/receita_stablecoin_activity.csv"
)

STABLECOINS = {"USDT", "USDC"}


def load_data():
    return pd.read_csv(
        SILVER_PATH,
        parse_dates=["month"],
    )


def build_gold(df):
    gold = df.copy()

    gold["stablecoin_flag"] = gold["asset"].isin(STABLECOINS)

    monthly_total = (
        gold.groupby("month")["total_value_brl"]
        .sum()
        .rename("monthly_crypto_volume_brl")
    )

    gold = gold.merge(
        monthly_total,
        on="month",
        how="left",
    )

    gold["share_of_monthly_crypto_volume"] = (
        gold["total_value_brl"]
        / gold["monthly_crypto_volume_brl"]
    )

    return gold[
        [
            "month",
            "asset",
            "operation_count",
            "total_value_brl",
            "average_value_brl",
            "stablecoin_flag",
            "share_of_monthly_crypto_volume",
        ]
    ]


def save_data(df):
    GOLD_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(GOLD_PATH, index=False)

    print(f"Saved to: {GOLD_PATH}")
    print(f"Rows: {len(df)}")


def main():
    print("Building Receita Federal Gold dataset...")

    silver = load_data()
    gold = build_gold(silver)

    save_data(gold)


if __name__ == "__main__":
    main()
