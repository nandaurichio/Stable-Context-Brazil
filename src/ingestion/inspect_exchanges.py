import csv
from datetime import datetime, timezone
from pathlib import Path

import ccxt


EXCHANGES = {
    "Mercado Bitcoin": "mercado",
    "Foxbit": "foxbit",
}

STABLECOIN_PAIRS = {
    "USDT/BRL",
    "USDC/BRL",
}

TIMEFRAME = "1d"
CANDLES_PER_REQUEST = 1000

OUTPUT_PATH = Path("data/bronze/exchange_coverage.csv")


def inspect_exchange(name, exchange_id):
    exchange = getattr(ccxt, exchange_id)()
    markets = exchange.load_markets()

    results = []

    print(f"\n{name}")
    print("-" * len(name))

    for symbol in sorted(STABLECOIN_PAIRS):
        if symbol not in markets:
            print(f"{symbol}: not available")
            continue

        trades = exchange.has.get("fetchTrades")
        ohlcv = exchange.has.get("fetchOHLCV")

        print(
            f"{symbol}: "
            f"trades={trades} "
            f"ohlcv={ohlcv}"
        )

        first_date = None
        last_date = None

        if ohlcv:
            first_timestamp, last_timestamp = find_ohlcv_coverage(
                exchange,
                symbol,
            )

            first_date = format_date(first_timestamp)
            last_date = format_date(last_timestamp)

            print(
                f"  coverage: "
                f"{first_date} -> {last_date}"
            )

        results.append(
            {
                "exchange": name,
                "exchange_id": exchange_id,
                "symbol": symbol,
                "timeframe": TIMEFRAME,
                "trades": trades,
                "ohlcv": ohlcv,
                "first_available": first_date,
                "last_available": last_date,
            }
        )

    return results


def find_ohlcv_coverage(exchange, symbol):
    latest = exchange.fetch_ohlcv(
        symbol,
        timeframe=TIMEFRAME,
        limit=CANDLES_PER_REQUEST,
    )

    if not latest:
        return None, None

    latest_timestamp = latest[-1][0]

    first_timestamp = find_first_candle(
        exchange,
        symbol,
        latest_timestamp,
    )

    return first_timestamp, latest_timestamp


def find_first_candle(exchange, symbol, latest_timestamp):
    one_day_ms = 24 * 60 * 60 * 1000

    current_timestamp = latest_timestamp

    while True:
        candles = exchange.fetch_ohlcv(
            symbol,
            timeframe=TIMEFRAME,
            since=current_timestamp - (
                CANDLES_PER_REQUEST * one_day_ms
            ),
            limit=CANDLES_PER_REQUEST,
        )

        if not candles:
            return current_timestamp

        first_timestamp = candles[0][0]

        if first_timestamp == current_timestamp:
            return first_timestamp

        current_timestamp = first_timestamp


def format_date(timestamp):
    if timestamp is None:
        return None

    return datetime.fromtimestamp(
        timestamp / 1000,
        tz=timezone.utc,
    ).strftime("%Y-%m-%d")


def save_coverage(results):
    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    fieldnames = [
        "exchange",
        "exchange_id",
        "symbol",
        "timeframe",
        "trades",
        "ohlcv",
        "first_available",
        "last_available",
    ]

    with OUTPUT_PATH.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(results)

    print(f"\nCoverage saved to: {OUTPUT_PATH}")


def main():
    all_results = []

    for name, exchange_id in EXCHANGES.items():
        results = inspect_exchange(
            name,
            exchange_id,
        )

        all_results.extend(results)

    save_coverage(all_results)


if __name__ == "__main__":
    main()