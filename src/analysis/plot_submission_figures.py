"""Generate submission figures for the MVP.

Produces three evidence figures into docs/figures/:

1. fig_cross_source_index.png  — normalized monthly index (all sources)
2. fig_exchange_breakout.png   — monthly exchange BRL notional, 2024+
3. fig_usdc_shift.png          — USDC share of declared stablecoins

Run: python3 -m src.analysis.plot_submission_figures
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTEXT_PATH = ROOT / "data" / "gold" / "monthly_context.csv"
EXCHANGE_PATH = ROOT / "data" / "gold" / "exchange_stablecoin_activity.csv"
RECEITA_PATH = ROOT / "data" / "gold" / "receita_stablecoin_activity.csv"
OUTPUT_DIR = ROOT / "docs" / "figures"

METRICS = [
    "receita_stablecoin_brl",
    "exchange_volume_brl_estimated",
    "deposits_usd",
    "borrows_usd",
    "selic_meta",
    "usd_brl",
]

METRIC_LABELS = {
    "receita_stablecoin_brl": "Receita (declared, BRL)",
    "exchange_volume_brl_estimated": "Exchanges (BRL est.)",
    "deposits_usd": "On-chain deposits (USD)",
    "borrows_usd": "On-chain borrows (USD)",
    "selic_meta": "Selic target",
    "usd_brl": "USD/BRL",
}


def fig_cross_source_index(context):
    idx = context[["month"] + METRICS].copy()
    for m in METRICS:
        idx[m] = idx[m] / idx[m].iloc[0] * 100

    plt.figure(figsize=(14, 8))
    for m in METRICS:
        plt.plot(idx["month"], idx[m], label=METRIC_LABELS[m], linewidth=2)

    plt.axvline(pd.Timestamp("2026-07-01"), color="red", alpha=0.4, linestyle="--", label="2026-07 (exchange regime change)")
    plt.title("Stable-Context: Brazil — Monthly Context Index (2023-01 = 100)")
    plt.xlabel("Month")
    plt.ylabel("Index")
    plt.legend(fontsize=9)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    path = OUTPUT_DIR / "fig_cross_source_index.png"
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Saved: {path}")


def fig_exchange_breakout(exchange):
    df = exchange.copy()
    df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()
    monthly = df.groupby("month")["volume_brl"].sum() / 1e9  # BRL billions

    monthly = monthly.loc["2024-01":]

    colors = ["#c0392b" if m == pd.Timestamp("2026-07-01") else "#2c6fbb" for m in monthly.index]

    plt.figure(figsize=(13, 6.5))
    plt.bar(monthly.index, monthly.values, color=colors, width=22)

    peak = monthly.loc[pd.Timestamp("2026-07-01")]
    plt.annotate(
        f"2026-07: {peak:.1f} bi BRL (~10x step)",
        xy=(pd.Timestamp("2026-07-01"), peak),
        xytext=(pd.Timestamp("2025-06-01"), peak * 0.95),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="black", alpha=0.6),
    )

    plt.title("Stablecoin USD/BRL spot volume — Mercado Bitcoin + Foxbit (est. BRL)")
    plt.xlabel("Month")
    plt.ylabel("BRL billions per month")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()

    path = OUTPUT_DIR / "fig_exchange_breakout.png"
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Saved: {path}")


def fig_usdc_shift(receita):
    df = receita.copy()
    stable = df[df["stablecoin_flag"]]
    total = stable.groupby("month")["total_value_brl"].sum()
    usdc = stable[stable["asset"] == "USDC"].groupby("month")["total_value_brl"].sum()
    share = (usdc / total * 100).loc["2023-01":]

    plt.figure(figsize=(13, 6.5))
    plt.plot(share.index, share.values, color="#16a085", linewidth=2.5)
    plt.scatter(share.index[::6], share.values[::6], color="#16a085", s=20, zorder=3)

    last = share.loc[pd.Timestamp("2026-06-01")]
    plt.annotate(
        f"2026-06: {last:.1f}%",
        xy=(pd.Timestamp("2026-06-01"), last),
        xytext=(pd.Timestamp("2024-10-01"), last + 6),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="black", alpha=0.6),
    )

    plt.title("USDC share of declared stablecoin value — Receita Federal")
    plt.xlabel("Month")
    plt.ylabel("USDC share (%)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    path = OUTPUT_DIR / "fig_usdc_shift.png"
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Saved: {path}")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    context = pd.read_csv(CONTEXT_PATH, parse_dates=["month"])
    exchange = pd.read_csv(EXCHANGE_PATH, parse_dates=["date"])
    receita = pd.read_csv(RECEITA_PATH, parse_dates=["month"])

    fig_cross_source_index(context)
    fig_exchange_breakout(exchange)
    fig_usdc_shift(receita)


if __name__ == "__main__":
    main()