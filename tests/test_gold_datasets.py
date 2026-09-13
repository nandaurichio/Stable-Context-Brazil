"""Data integrity tests for the Gold datasets and context layer.

Run from the repository root:

    python3 -m unittest discover -s tests -v

These tests validate the assumptions the analysis findings rely on:
schemas, coverage windows, derived-field math and cross-source
consistency. They do not require network access.
"""

import json
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

GOLD = ROOT / "data" / "gold"
SILVER = ROOT / "data" / "silver"
BRONZE = ROOT / "data" / "bronze"
CONTEXT = ROOT / "data" / "context"

RECEITA_PATH = GOLD / "receita_stablecoin_activity.csv"
EXCHANGE_PATH = GOLD / "exchange_stablecoin_activity.csv"
GRAPH_PATH = GOLD / "ethereum_lending_activity.csv"
GRAPH_MONTHLY_PATH = GOLD / "ethereum_lending_activity_monthly.csv"
CONTEXT_PATH = GOLD / "monthly_context.csv"
EXPLORATION_PATH = GOLD / "monthly_exploration.csv"
BCB_PATH = SILVER / "bcb_monthly.csv"
EVENTS_PATH = CONTEXT / "brazil_events.csv"


class TestDatasetPresence(unittest.TestCase):

    def test_gold_files_exist(self):
        for path in [
            RECEITA_PATH,
            EXCHANGE_PATH,
            GRAPH_PATH,
            GRAPH_MONTHLY_PATH,
            CONTEXT_PATH,
            EXPLORATION_PATH,
        ]:
            self.assertTrue(path.exists(), f"missing {path}")

    def test_context_files_exist(self):
        self.assertTrue(BCB_PATH.exists(), "missing bcb_monthly.csv")
        self.assertTrue(EVENTS_PATH.exists(), "missing brazil_events.csv")


class TestSchemas(unittest.TestCase):

    def test_exchange_schema(self):
        df = pd.read_csv(EXCHANGE_PATH)
        expected = {
            "date", "exchange", "asset", "symbol",
            "open", "high", "low", "close", "volume", "volume_brl",
        }
        self.assertTrue(expected.issubset(set(df.columns)))

    def test_receita_schema(self):
        df = pd.read_csv(RECEITA_PATH)
        expected = {
            "month", "asset", "operation_count", "total_value_brl",
            "average_value_brl", "stablecoin_flag",
            "share_of_monthly_crypto_volume",
        }
        self.assertTrue(expected.issubset(set(df.columns)))

    def test_graph_schema(self):
        df = pd.read_csv(GRAPH_PATH)
        expected = {
            "date", "protocol", "asset", "market", "market_name",
            "tvl", "deposits", "borrows", "withdrawals", "repayments",
            "active_users",
        }
        self.assertTrue(expected.issubset(set(df.columns)))

    def test_context_schema(self):
        df = pd.read_csv(CONTEXT_PATH)
        expected = {
            "month", "receita_stablecoin_brl",
            "exchange_volume_brl_estimated", "deposits_usd",
            "borrows_usd", "selic_meta", "usd_brl",
        }
        self.assertEqual(set(expected), set(df.columns))


class TestDerivedMath(unittest.TestCase):

    def test_exchange_volume_brl(self):
        df = pd.read_csv(EXCHANGE_PATH)
        computed = df["volume"] * df["close"]
        self.assertTrue(
            (df["volume_brl"] - computed).abs().max() < 1e-6,
            "volume_brl must equal volume * close",
        )

    def test_receita_share_bounds(self):
        df = pd.read_csv(RECEITA_PATH)
        share = df["share_of_monthly_crypto_volume"]
        self.assertTrue((share >= 0).all())
        self.assertTrue((share <= 100).all())

    def test_graph_monthly_matches_daily(self):
        daily = pd.read_csv(GRAPH_PATH)
        monthly = pd.read_csv(GRAPH_MONTHLY_PATH, parse_dates=["month"])

        daily["month"] = pd.to_datetime(daily["date"], unit="s").dt.to_period("M")

        sample = monthly.iloc[0]
        row = daily[
            (daily["month"] == sample["month"].to_period("M"))
            & (daily["protocol"] == sample["protocol"])
            & (daily["asset"] == sample["asset"])
        ]
        self.assertTrue(
            abs(row["deposits"].sum() - sample["deposits_usd"]) <= 1.0,
            "monthly deposits must match daily sum",
        )


class TestCoverage(unittest.TestCase):

    def test_receita_coverage_end(self):
        df = pd.read_csv(RECEITA_PATH, parse_dates=["month"])
        self.assertEqual(df["month"].max().date().isoformat(), "2026-06-01")

    def test_exchange_coverage(self):
        df = pd.read_csv(EXCHANGE_PATH, parse_dates=["date"])
        self.assertGreaterEqual(df["date"].max().date().isoformat(), "2026-09-01")

    def test_context_window(self):
        df = pd.read_csv(CONTEXT_PATH, parse_dates=["month"])
        self.assertEqual(df["month"].min().date().isoformat(), "2023-01-01")
        self.assertEqual(len(df), 45, "context must span 2023-01 .. 2026-09")
        self.assertEqual(df["month"].max().date().isoformat(), "2026-09-01")

    def test_context_receita_nan_after_june_2026(self):
        df = pd.read_csv(CONTEXT_PATH, parse_dates=["month"])
        tail = df[df["month"] >= "2026-07-01"]
        self.assertTrue(
            tail["receita_stablecoin_brl"].isna().all(),
            "Receita ends 2026-06; later months must be NaN, not 0",
        )

    def test_bcb_coverage(self):
        df = pd.read_csv(BCB_PATH, parse_dates=["month"])
        self.assertEqual(df["month"].min().date().isoformat(), "2023-01-01")


class TestContextConsistency(unittest.TestCase):

    def test_context_matches_sources(self):
        context = pd.read_csv(CONTEXT_PATH, parse_dates=["month"]).set_index("month")

        receita = pd.read_csv(RECEITA_PATH, parse_dates=["month"])
        receita = (
            receita.loc[receita["stablecoin_flag"]]
            .groupby("month")["total_value_brl"]
            .sum()
        )

        exchange = pd.read_csv(EXCHANGE_PATH, parse_dates=["date"])
        exchange["month"] = exchange["date"].dt.to_period("M").dt.to_timestamp()
        exchange = exchange.groupby("month")["volume_brl"].sum()

        bcb = pd.read_csv(BCB_PATH, parse_dates=["month"]).set_index("month")

        for month in ["2023-01-01", "2024-06-01", "2025-12-01"]:
            m = pd.Timestamp(month)
            self.assertAlmostEqual(
                context.loc[m, "receita_stablecoin_brl"],
                receita.loc[m],
                places=1,
            )
            self.assertAlmostEqual(
                context.loc[m, "exchange_volume_brl_estimated"],
                exchange.loc[m],
                places=1,
            )
            self.assertEqual(
                context.loc[m, "selic_meta"],
                bcb.loc[m, "selic_meta"],
            )
            self.assertAlmostEqual(
                context.loc[m, "usd_brl"],
                bcb.loc[m, "usd_brl"],
                places=6,
            )


class TestContextEvents(unittest.TestCase):

    def test_events_schema_and_dates(self):
        df = pd.read_csv(EVENTS_PATH, parse_dates=["date"])
        expected = {"date", "category", "title", "detail", "source", "confidence"}
        self.assertEqual(set(expected), set(df.columns))
        self.assertGreaterEqual(len(df), 20)
        self.assertTrue(df["confidence"].isin(
            {"high", "medium", "to_verify"}
        ).all())
        self.assertTrue(df["date"].notna().all())


if __name__ == "__main__":
    unittest.main()