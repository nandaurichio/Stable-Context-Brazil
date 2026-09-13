import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

INPUT_PATH = Path("data/gold/monthly_context.csv")
OUTPUT_PATH = Path("docs/working/monthly_context_index.png")


def load_data():
    return pd.read_csv(INPUT_PATH, parse_dates=["month"])


def build_index(df):
    metrics = [
        "receita_stablecoin_brl",
        "exchange_volume_brl_estimated",
        "deposits_usd",
        "borrows_usd",
        "selic_meta",
        "usd_brl",
    ]

    indexed = df[["month"] + metrics].copy()

    for metric in metrics:
        indexed[metric] = (
            indexed[metric] / indexed[metric].iloc[0]
        ) * 100

    return indexed


def plot_data(df):
    metrics = [
        "receita_stablecoin_brl",
        "exchange_volume_brl_estimated",
        "deposits_usd",
        "borrows_usd",
        "selic_meta",
        "usd_brl",
    ]

    plt.figure(figsize=(14, 8))

    for metric in metrics:
        plt.plot(df["month"], df[metric], label=metric)

    plt.title("Stable-Context: Brazil — Monthly Context Index")
    plt.xlabel("Month")
    plt.ylabel("Index (first month = 100)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUTPUT_PATH, dpi=150)
    plt.close()

    print(f"Saved: {OUTPUT_PATH}")


def main():
    df = load_data()
    indexed = build_index(df)
    plot_data(indexed)


if __name__ == "__main__":
    main()
