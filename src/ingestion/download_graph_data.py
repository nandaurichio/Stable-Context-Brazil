import json
import os
from pathlib import Path

import requests


PAGE_SIZE = 1000
START_TIMESTAMP = 1672531200  # 2023-01-01 00:00:00 UTC


SOURCES = {
    "aave": {
        "url": (
            "https://gateway.thegraph.com/api/subgraphs/id/"
            "JCNWRypm7FYwV8fx5HhzZPSFaMxgkPuw4TnR3Gpi81zk"
        ),
        "output_path": Path(
            "data/bronze/aave_stablecoin_snapshots.json"
        ),
        "markets": {
            "USDT": "0x23878914efe38d27c4d67ab83ed1b93a74d4086a",
            "USDC": "0x98c23e9d8f34fefb1b7bd6a91b7ff122f4e16f5c",
        },
    },
    "compound": {
        "url": (
            "https://gateway.thegraph.com/api/subgraphs/id/"
            "AwoxEZbiWLvv6e3QdvdMZw4WDURdGbvPfHmZRc8Dpfz9"
        ),
        "output_path": Path(
            "data/bronze/compound_stablecoin_snapshots.json"
        ),
        "markets": {
            "USDT": (
                "0x3afdc9bca9213a35503b077a6072f3d0d5ab0840"
                "dac17f958d2ee523a2206206994597c13d831ec7"
            ),
            "USDC": (
                "0xc3d688b66703497daa19211eedff47f25384cdc3"
                "a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
            ),
        },
    },
    "spark": {
        "url": (
            "https://gateway.thegraph.com/api/subgraphs/id/"
            "GbKdmBe4ycCYCQLQSjqGg6UHYoYfbyJyq5WrG35pv1si"
        ),
        "output_path": Path(
            "data/bronze/spark_stablecoin_snapshots.json"
        ),
        "markets": {
            "USDC": "0x377c3bd93f2a2984e1e7be6a5c22c525ed4a4815",
            "USDT": "0xe7df13b8e3d6740fe17cbe928c7334243d86c92f",
        },
    },
}


# The Graph — Standardized Lending/CDP Schema query
def build_query(markets, timestamp):
    market_ids = ", ".join(
        f'"{market_id}"'
        for market_id in markets.values()
    )

    return f"""
    {{
      marketDailySnapshots(
        first: {PAGE_SIZE}
        orderBy: timestamp
        orderDirection: asc
        where: {{
          market_in: [{market_ids}]
          timestamp_gt: {timestamp}
        }}
      ) {{
        timestamp

        market {{
          id
          name

          inputToken {{
            id
            symbol
            decimals
          }}
        }}

        inputTokenBalance
        inputTokenPriceUSD
        totalValueLockedUSD
        dailyDepositUSD
        dailyBorrowUSD
        dailyWithdrawUSD
        dailyRepayUSD
        dailyActiveUsers
      }}
    }}
    """


def fetch_data(url, markets):
    api_key = os.environ["THE_GRAPH_API_KEY"]

    all_rows = []
    last_timestamp = START_TIMESTAMP

    while True:
        query = build_query(markets, last_timestamp)

        response = requests.post(
            url,
            json={"query": query},
            headers={
                "Authorization": f"Bearer {api_key}",
            },
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        if "errors" in data:
            raise RuntimeError(data["errors"])

        rows = data["data"]["marketDailySnapshots"]

        if not rows:
            break

        all_rows.extend(rows)
        last_timestamp = int(rows[-1]["timestamp"])

        print(
            f"Fetched {len(rows)} rows "
            f"(total: {len(all_rows)})"
        )

        if len(rows) < PAGE_SIZE:
            break

    return {
        "data": {
            "marketDailySnapshots": all_rows
        }
    }


def save_data(data, output_path):
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            data,
            file,
            indent=2,
        )

    print(f"Saved to: {output_path}")


def main():
    for protocol, source in SOURCES.items():
        print(
            f"\nFetching {protocol.capitalize()} "
            "stablecoin data from The Graph..."
        )

        data = fetch_data(
            source["url"],
            source["markets"],
        )

        save_data(
            data,
            source["output_path"],
        )


if __name__ == "__main__":
    main()