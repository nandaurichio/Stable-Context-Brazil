import pandas as pd
from pathlib import Path

SILVER_PATH = Path(
    "data/silver/exchange_daily_ohlcv.csv"
)

GOLD_PATH = Path(
    "data/gold/exchange_stablecoin_activity.csv"
)

STABLECOIN_PAIRS = {
    "USDT/BRL": "USDT",
    "USDC/BRL": "USDC",
}


def load_data():
    return pd.read_csv(
        SILVER_PATH,
        parse_dates=["timestamp"],
    )


def build_gold(df):
    gold = df[
        df["symbol"].isin(STABLECOIN_PAIRS)
    ].copy()

    gold["date"] = gold["timestamp"].dt.date
    gold["asset"] = gold["symbol"].map(STABLECOIN_PAIRS)
    gold["volume_brl"] = gold["volume"] * gold["close"]

    return gold[
        [
            "date",
            "exchange",
            "asset",
            "symbol",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "volume_brl",
        ]
    ]

def save_data(df):
    GOLD_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(GOLD_PATH, index=False)

    print(f"Saved to: {GOLD_PATH}")
    print(f"Rows: {len(df)}")


def main():
    print("Building exchange Gold dataset...")

    silver = load_data()
    gold = build_gold(silver)

    save_data(gold)


if __name__ == "__main__":
    main()
