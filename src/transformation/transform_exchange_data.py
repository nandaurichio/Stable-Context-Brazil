import pandas as pd
from pathlib import Path


BRONZE_PATH = Path(
    "data/bronze/exchange_daily_ohlcv.csv"
)

SILVER_PATH = Path(
    "data/silver/exchange_daily_ohlcv.csv"
)


def load_data():
    return pd.read_csv(BRONZE_PATH)


def transform_data(df):
    transformed = df.rename(
        columns={
            "timestamp": "timestamp_ms",
        }
    )

    transformed["timestamp"] = pd.to_datetime(
        transformed["timestamp_ms"],
        unit="ms",
        utc=True,
    )

    transformed["open"] = transformed["open"].astype(float)
    transformed["high"] = transformed["high"].astype(float)
    transformed["low"] = transformed["low"].astype(float)
    transformed["close"] = transformed["close"].astype(float)
    transformed["volume"] = transformed["volume"].astype(float)

    return transformed[
        [
            "exchange",
            "symbol",
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume",
        ]
    ]


def save_data(df):
    SILVER_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        SILVER_PATH,
        index=False,
    )

    print(f"Saved to: {SILVER_PATH}")
    print(f"Rows: {len(df)}")


def main():
    print("Transforming exchange data...")

    bronze = load_data()
    silver = transform_data(bronze)

    save_data(silver)


if __name__ == "__main__":
    main()
