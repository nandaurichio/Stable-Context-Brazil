import csv
import time
from datetime import datetime, timezone
from pathlib import Path

import ccxt


OUTPUT_PATH = Path("data/bronze/exchange_daily_ohlcv.csv")

CANDLES_PER_REQUEST = 1000

SOURCES = [
    {
        "exchange": "Mercado Bitcoin",
        "exchange_id": "mercado",
        "symbol": "USDT/BRL",
        "start_date": "2023-03-11",
    },
    {
        "exchange": "Mercado Bitcoin",
        "exchange_id": "mercado",
        "symbol": "USDC/BRL",
        "start_date": "2020-05-26",
    },
    {
        "exchange": "Foxbit",
        "exchange_id": "foxbit",
        "symbol": "USDT/BRL",
        "start_date": "2021-03-19",
    },
    {
        "exchange": "Foxbit",
        "exchange_id": "foxbit",
        "symbol": "USDC/BRL",
        "start_date": "2021-03-19",
    },
]


def date_to_timestamp(date):
    return int(
        datetime.strptime(
            date,
            "%Y-%m-%d",
        )
        .replace(tzinfo=timezone.utc)
        .timestamp()
        * 1000
    )


def fetch_history(exchange, symbol, start_date):
    since = date_to_timestamp(start_date)
    rows = []

    while True:
        candles = exchange.fetch_ohlcv(
            symbol,
            timeframe="1d",
            since=since,
            limit=CANDLES_PER_REQUEST,
        )

        if not candles:
            break

        rows.extend(candles)

        print(
            f"  {symbol}: "
            f"{len(candles)} candles "
            f"(total: {len(rows)})"
        )

        last_timestamp = candles[-1][0]

        if last_timestamp <= since:
            break

        since = last_timestamp + 24 * 60 * 60 * 1000

        time.sleep(exchange.rateLimit / 1000)

    return rows


def save_data(rows):
    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_PATH.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)

        writer.writerow(
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
        )

        writer.writerows(rows)

    print(f"\nSaved to: {OUTPUT_PATH}")
    print(f"Rows: {len(rows)}")


def main():
    all_rows = []

    for source in SOURCES:
        print(
            f"\nFetching {source['exchange']} "
            f"{source['symbol']}..."
        )

        exchange = getattr(
            ccxt,
            source["exchange_id"],
        )()

        candles = fetch_history(
            exchange,
            source["symbol"],
            source["start_date"],
        )

        for candle in candles:
            all_rows.append(
                [
                    source["exchange"],
                    source["symbol"],
                    candle[0],
                    candle[1],
                    candle[2],
                    candle[3],
                    candle[4],
                    candle[5],
                ]
            )

    save_data(all_rows)


if __name__ == "__main__":
    main()
