import json
from pathlib import Path


BRONZE_PATH = Path("data/bronze")
SILVER_PATH = Path("data/silver")


def load_snapshots(file_path):
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)["data"]["marketDailySnapshots"]


def transform_snapshots(rows, protocol):
    transformed = []

    for row in rows:
        market = row["market"]
        token = market["inputToken"]

        transformed.append(
            {
                "protocol": protocol,
                "market": market["id"],
                "market_name": market["name"],
                "asset": token["symbol"],
                "token_address": token["id"],
                "token_decimals": int(token["decimals"]),
                "timestamp": int(row["timestamp"]),
                "input_token_balance": float(row["inputTokenBalance"]),
                "input_token_price_usd": float(row["inputTokenPriceUSD"]),
                "total_value_locked_usd": float(row["totalValueLockedUSD"]),
                "daily_deposit_usd": float(row["dailyDepositUSD"]),
                "daily_borrow_usd": float(row["dailyBorrowUSD"]),
                "daily_withdraw_usd": float(row["dailyWithdrawUSD"]),
                "daily_repay_usd": float(row["dailyRepayUSD"]),
                "daily_active_users": int(row["dailyActiveUsers"]),
            }
        )

    return transformed


def save_data(rows, protocol):
    SILVER_PATH.mkdir(parents=True, exist_ok=True)

    output_path = (
        SILVER_PATH / f"{protocol}_stablecoin_snapshots.json"
    )

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(rows, file, indent=2)

    print(f"Saved to: {output_path}")


def main():
    for protocol in ["aave", "compound", "spark"]:
        bronze_path = (
            BRONZE_PATH / f"{protocol}_stablecoin_snapshots.json"
        )

        print(f"\nTransforming {protocol}...")

        rows = load_snapshots(bronze_path)
        transformed = transform_snapshots(rows, protocol)

        save_data(transformed, protocol)

        print(f"Transformed {len(transformed)} rows")


if __name__ == "__main__":
    main()
