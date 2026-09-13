"""Build the monthly on-chain lending dataset from daily observations.

Aggregates the daily Lending/CDP observations (Aave, Compound, Spark)
into monthly rows by protocol and asset.

The aggregation follows the documented working query in
`docs/working/analysis_queries.md`, without a fixed upper cutoff:
the monthly layer extends to the last available daily observation.
"""

import duckdb
from pathlib import Path


INPUT_PATH = Path("data/gold/ethereum_lending_activity.csv")
OUTPUT_PATH = Path("data/gold/ethereum_lending_activity_monthly.csv")

QUERY = """
SELECT
    DATE_TRUNC('month', to_timestamp(date))::DATE AS month,
    protocol,
    asset,
    ROUND(SUM(deposits), 2) AS deposits_usd,
    ROUND(SUM(borrows), 2) AS borrows_usd,
    ROUND(SUM(withdrawals), 2) AS withdrawals_usd,
    ROUND(SUM(repayments), 2) AS repayments_usd,
    ROUND(AVG(tvl), 2) AS avg_tvl_usd,
    SUM(active_users) AS active_user_days
FROM read_csv_auto(?, types={
    'date': 'BIGINT',
    'protocol': 'VARCHAR',
    'asset': 'VARCHAR',
    'market': 'VARCHAR',
    'market_name': 'VARCHAR',
    'tvl': 'DOUBLE',
    'deposits': 'DOUBLE',
    'borrows': 'DOUBLE',
    'withdrawals': 'DOUBLE',
    'repayments': 'DOUBLE',
    'active_users': 'BIGINT',
})
GROUP BY 1, 2, 3
ORDER BY 1, 2, 3
"""


def build_monthly():
    return duckdb.sql(QUERY, params=[str(INPUT_PATH)]).df()


def save_data(df):
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved: {OUTPUT_PATH}")
    print(f"Rows: {len(df)}")
    print(f"Coverage: {df['month'].min()} -> {df['month'].max()}")


def main():
    print("Building monthly on-chain lending dataset...")

    result = build_monthly()
    save_data(result)


if __name__ == "__main__":
    main()