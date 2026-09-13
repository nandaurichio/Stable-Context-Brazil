import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/gold/monthly_context.csv")
OUTPUT_PATH = Path("data/gold/monthly_exploration.csv")


def load_data():
    return pd.read_csv(INPUT_PATH, parse_dates=["month"])


def calculate_monthly_variation(df):
    metrics = [
        "receita_stablecoin_brl",
        "exchange_volume_brl_estimated",
        "deposits_usd",
        "borrows_usd",
        "selic_meta",
        "usd_brl",
    ]

    result = df.copy()

    for metric in metrics:
        result[f"{metric}_mom_pct"] = result[metric].pct_change() * 100

    return result


def save_data(df):
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved to: {OUTPUT_PATH}")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")


def main():
    print("Building monthly exploratory dataset...")

    df = load_data()
    result = calculate_monthly_variation(df)

    save_data(result)


if __name__ == "__main__":
    main()