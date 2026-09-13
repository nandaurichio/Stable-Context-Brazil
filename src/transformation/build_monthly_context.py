"""Build the consolidated monthly context dataset.

Assembles the four sources into a single monthly frame:

- Receita Federal: reported stablecoin value (BRL)
- Exchanges (MB + Foxbit): estimated BRL notional of stablecoin spot trading
- The Graph (Aave/Compound/Spark): monthly on-chain deposits and borrows (USD)
- Banco Central do Brasil: Selic target rate and USD/BRL monthly mean

The window starts at 2023-01-01, the common start of the BCB and
The Graph coverage. It extends to the last month with any observation.

Sources have different end dates: Receita Federal currently ends at
2026-06; the other sources extend to 2026-09. Months without a value in
a given source are represented as missing (NaN), not as zero.
"""

import pandas as pd
from pathlib import Path


RECEITA_PATH = Path("data/gold/receita_stablecoin_activity.csv")
EXCHANGE_PATH = Path("data/gold/exchange_stablecoin_activity.csv")
GRAPH_MONTHLY_PATH = Path("data/gold/ethereum_lending_activity_monthly.csv")
BCB_PATH = Path("data/silver/bcb_monthly.csv")
OUTPUT_PATH = Path("data/gold/monthly_context.csv")

ANCHOR_START = "2023-01-01"

COLUMN_ORDER = [
    "month",
    "receita_stablecoin_brl",
    "exchange_volume_brl_estimated",
    "deposits_usd",
    "borrows_usd",
    "selic_meta",
    "usd_brl",
]


def load_receita():
    df = pd.read_csv(RECEITA_PATH, parse_dates=["month"])

    stable = df.loc[df["stablecoin_flag"], ["month", "total_value_brl"]]

    return (
        stable
        .groupby("month")["total_value_brl"]
        .sum()
        .rename("receita_stablecoin_brl")
    )


def load_exchange():
    df = pd.read_csv(EXCHANGE_PATH, parse_dates=["date"])

    df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()

    return (
        df
        .groupby("month")["volume_brl"]
        .sum()
        .rename("exchange_volume_brl_estimated")
    )


def load_graph():
    df = pd.read_csv(GRAPH_MONTHLY_PATH, parse_dates=["month"])

    return df.groupby("month")[["deposits_usd", "borrows_usd"]].sum()


def load_bcb():
    df = pd.read_csv(BCB_PATH, parse_dates=["month"])

    return df.set_index("month")[["selic_meta", "usd_brl"]]


def build_context():
    receita = load_receita()
    exchange = load_exchange()
    graph = load_graph()
    bcb = load_bcb()

    frame = receita.to_frame().join(
        [exchange, graph, bcb],
        how="outer",
    )

    frame = frame.loc[frame.index >= pd.Timestamp(ANCHOR_START)]
    frame = frame.sort_index().reset_index()

    return frame[COLUMN_ORDER]


def save_data(df):
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved: {OUTPUT_PATH}")
    print(f"Rows: {len(df)}")
    print(f"Coverage: {df['month'].min()} -> {df['month'].max()}")
    print(f"Columns: {list(df.columns)}")


def main():
    print("Building monthly context dataset...")

    result = build_context()
    save_data(result)


if __name__ == "__main__":
    main()