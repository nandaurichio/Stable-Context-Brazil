# Analysis Findings — 04. On-Chain (The Graph)

> Status: exploratory observation, based on the standardized Lending/CDP
> subgraphs for Aave, Compound and Spark.
> On-chain activity does **not** establish that a wallet belongs to a
> Brazilian user. This source provides global on-chain context only.

## Scope

| Item | Value |
|---|---|
| Datasets | `data/gold/ethereum_lending_activity.csv` (daily), `..._monthly.csv` (monthly) |
| Protocols | Aave, Compound, Spark (standardized schema) |
| Assets | USDC, USDT |
| Fields | deposits, borrows, withdrawals, repayments, tvl, active_users |

## Coverage & Limitations

- Market availability (first observation):
  - Aave: USDC 2023-01-27, USDT 2023-02-13
  - Compound: USDC 2023-01-01, **USDT only from 2024-07-06**
  - Spark: USDC 2023-03-07, USDT 2023-10-19
- The common period across all six market/asset series starts
  2024-07. Earlier months are unbalanced.
- Spark is negligible in size until 2025; the aggregate picture is
  essentially Aave + Compound.
- The monthly layer is currently cut at 2026-06-30 (raw data to 2026-09).

## Observations

### Deposits (all protocols/assets, USD)

| Year | Deposits | vs previous |
|---|---|---|
| 2024 | ~40 bi (1.7 bi/month at start) | — |
| 2025 | ~160 bi (monthly peak 23.3 bi in Jul) | ~4× 2024 |
| 2026 (Jan–Sep) | ~110 bi (9.9 bi/month by Jun) | declining |

Monthly deposits: 1.67 bi (2024-01) → 8–9 bi (early 2025) → **peak
23.3 bi (2025-07)** → trough ~9.9 bi (2026-05/06) → partial rebound
11.4 bi / 10.4 bi (2026-07/08) → 3.4 bi (2026-09, partial month).

### Borrows, TVL, users

- Borrows: peak **21.4 bi USD (2025-08)**; secondary peak 19.6 bi
  (2025-07); earlier spike 7.4 bi (2024-11).
- Average TVL: peak **2.38 bi USD (2025-09)**, ~1.0 bi (2026-06) — down
  ~58% from peak.
- Active user-days: 11.3k (2024-01) → ~61k (2025-08) → peak ~64.7k
  (2025-11) → ~47k (2026-06).

### Protocol structure

| Protocol | Role |
|---|---|
| Aave | Dominant — ~97% of the observed deposits/borrows across the period |
| Compound | Marginal second; USDT market exists only from 2024-07 |
| Spark | Negligible until 2025; meaningful only in the 2025-2026 window |

### Asset mix in 2026

USDT led deposit flows through late 2025 (e.g., 10.8 bi vs 6.7 bi USDC
in 2025-10). From 2026-05 the mix flips: USDC 5.7 bi vs USDT 4.2 bi
(2026-05), USDC 6.1 bi vs USDT 3.8 bi (2026-06).

### Data-quality observation (Spark USDT) — resolved

Spark USDT shows 9.66 bi USD of borrows in 2025 against ~0.19 bi USD of
average TVL. Daily inspection explains this: **borrows and repayments are
almost perfectly matched** (borrow/repay ratio ~1.01 in the Sep–Nov 2025
window where most activity occurred), with daily flows of 100–350 mi USD
against a TVL of 300–900 mi USD. This is a **high-churn market** (capital
borrowed and repaid in rapid cycles), not a data error.

Interpretation caveat: cumulative borrow/deposit flows are **not
comparable to TVL levels** or to declared/spot volumes in other sources
for this market. The behavior suggests systematic or automated flows
(active users are in the tens per day) and should be reported as flow
activity, not as outstanding market size.

## Signals

1. **Mid-2025 peak and 2026 decline:** deposits, borrows, TVL and users
   peaked between 2025-07 and 2025-11 and declined through mid-2026,
   with a partial rebound in 2026-07/08.
2. **USDC/USDT mix flip (2026):** the on-chain mix shifts toward USDC in
   the same period the Brazilian sources do (findings 02-03).
3. **Compound USDT late entry:** coverage starts 2024-07; earlier USDT
   "absence" is coverage, not activity.
4. **Spark USDT high-churn flow:** gross borrows exceed average TVL by a
   large factor because of rapid borrow/repay cycles; flow values for
   this market must be interpreted with this characteristic in mind.

## Questions for further investigation

- Is the 2026 decline a general DeFi-lending contraction or specific to
  these protocols/assets?
- Does the mid-2025 peak coincide with a specific yield/risk regime in
  stablecoin lending (e.g., funding, base rates)?
- Which markets drive the 2026 USDC shift — Aave v3 vs v2, or others?
- Who (type of user) drives the Spark USDT high-churn flow pattern?

## Related files

- `data/gold/ethereum_lending_activity.csv`
- `data/gold/ethereum_lending_activity_monthly.csv`
- `src/ingestion/download_graph_data.py`
- `src/transformation/transform_graph_data.py`
- `src/analysis/build_graph_gold.py`