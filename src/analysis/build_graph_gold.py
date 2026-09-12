import json
from pathlib import Path

SILVER_PATH = Path("data/silver")
GOLD_PATH = Path("data/gold/ethereum_lending_activity.csv")


PROTOCOLS = ["aave", "compound", "spark"]


def load_data(protocol):
    path = SILVER_PATH / f"{protocol}_stablecoin_snapshots.json"

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_gold():
    rows = []

    for protocol in PROTOCOLS:
        data = load_data(protocol)

        for row in data:
            rows.append(
                {
                    "date": row["timestamp"],
                    "protocol": row["protocol"],
                    "asset": row["asset"],
                    "market": row["market"],
                    "market_name": row["market_name"],
                    "tvl": row["total_value_locked_usd"],
                    "deposits": row["daily_deposit_usd"],
                    "borrows": row["daily_borrow_usd"],
                    "withdrawals": row["daily_withdraw_usd"],
                    "repayments": row["daily_repay_usd"],
                    "active_users": row["daily_active_users"],
                }
            )

    return rows


def save_data(rows):
    GOLD_PATH.parent.mkdir(parents=True, exist_ok=True)

    columns = [
        "date",
        "protocol",
        "asset",
        "market",
        "market_name",
        "tvl",
        "deposits",
        "borrows",
        "withdrawals",
        "repayments",
        "active_users",
    ]

    with GOLD_PATH.open("w", encoding="utf-8", newline="") as file:
        file.write(",".join(columns) + "\n")

        for row in rows:
            file.write(
                ",".join(
                    str(row[column])
                    for column in columns
                )
                + "\n"
            )

    print(f"Saved to: {GOLD_PATH}")
    print(f"Rows: {len(rows)}")


def main():
    print("Building Ethereum lending Gold dataset...")

    gold = build_gold()
    save_data(gold)


if __name__ == "__main__":
    main()
