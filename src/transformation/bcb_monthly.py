import json
from pathlib import Path

import pandas as pd


INPUT_DIR = Path("data/bronze/bcb")
OUTPUT_PATH = Path("data/silver/bcb_monthly.csv")


def load_series(filename, column_name):
    path = INPUT_DIR / filename

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    df = pd.DataFrame(data)

    df["date"] = pd.to_datetime(
        df["data"],
        dayfirst=True,
    )

    df[column_name] = pd.to_numeric(
        df["valor"],
        errors="coerce",
    )

    return df[["date", column_name]]


def build_monthly():
    selic = load_series(
        "selic_meta.json",
        "selic_meta",
    )

    usd_brl = load_series(
        "usd_brl.json",
        "usd_brl",
    )

    selic["month"] = selic["date"].dt.to_period("M")
    usd_brl["month"] = usd_brl["date"].dt.to_period("M")

    selic_monthly = (
        selic
        .groupby("month")["selic_meta"]
        .last()
        .reset_index()
    )

    usd_brl_monthly = (
        usd_brl
        .groupby("month")["usd_brl"]
        .mean()
        .reset_index()
    )

    result = selic_monthly.merge(
        usd_brl_monthly,
        on="month",
        how="outer",
    )

    result["month"] = result["month"].dt.to_timestamp()

    return result.sort_values("month")


def save_data(df):
    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        OUTPUT_PATH,
        index=False,
    )

    print(f"Saved: {OUTPUT_PATH}")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")


def main():
    print("Building BCB monthly dataset...")

    result = build_monthly()

    save_data(result)


if __name__ == "__main__":
    main()
