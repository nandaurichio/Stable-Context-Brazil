# Analysis Findings — 03. Brazilian Exchanges

> Status: exploratory observation, based on the Gold exchange dataset.
> This source measures spot trading on two venues only
> (Mercado Bitcoin, Foxbit), for USDT/BRL and USDC/BRL.

## Scope

| Item | Value |
|---|---|
| Dataset | `data/gold/exchange_stablecoin_activity.csv` |
| Coverage | 2020-05-26 → 2026-09-12 (daily OHLCV) |
| Fields | date, exchange, asset, symbol, open/high/low/close, volume, volume_brl |
| Unit | `volume` = base-asset amount (USDT/USDC); `volume_brl` = volume × daily close (est. BRL notional) |

## Coverage & Limitations

- Data availability by market (first positive-volume day):
  - Mercado Bitcoin USDC: 2020-05-26 · USDT: 2023-03-11
  - Foxbit USDT: 2021-04-07 · USDC: 2021-12-01
- Availability is a property of each exchange API, not an adoption date.
- Mercado Bitcoin has **zero zero-volume days** across both markets.
  Foxbit has 257 zero-volume days on USDC (12.8% of rows) and 19 on USDT —
  i.e., coverage days without recorded trading.
- 2026 is partial (through 2026-09-12), so full-year comparisons for 2026
  are not valid.

## Observations

### Yearly est. BRL notional

| Year | USDC | USDT | Total | USDC share |
|---|---|---|---|---|
| 2024 | 0.3 bi | 3.2 bi | 3.5 bi | 8.9% |
| 2025 | 0.9 bi | 6.7 bi | 7.6 bi | 11.3% |
| 2026 (Jan–Sep 12) | 18.4 bi | 18.7 bi | **37.1 bi** | 49.7% |

### Monthly evolution (est. BRL notional)

| Month | Total (bi BRL) | Note |
|---|---|---|
| 2024-01 | 0.12 | reference point |
| 2025-10 | 0.95 | |
| 2026-01 | 1.22 | |
| 2026-06 | 2.18 | last month before the break |
| **2026-07** | **14.38** | ≈ **6.6× the 2026-06 level** |
| 2026-08 | 9.98 | |
| 2026-09 (12 days) | 4.49 | ~1.0 bi BRL on 2026-09-08 alone |

### The 2026-07 regime change

- The step is visible in daily data: average daily volume went from
  ~10 mi BRL/day (early June) → ~67 mi/day (last week of June) →
  ~130 mi/day (July). Top days reached 0.82–1.0 bi BRL.
- It is **not concentrated in a single day** — it is a sustained
  multi-week step across all four market series.
- It is **venue-concentrated**: Foxbit = 13.37 bi of the 14.38 bi (93%)
  in 2026-07 (USDC 7.78 bi + USDT 5.59 bi). Mercado Bitcoin remained at
  ~1.0 bi (0.80 bi USDC + 0.21 bi USDT).
- Foxbit USDC alone grew from 53 mi BRL (2026-01) → 662 mi (2026-06) →
  **7.78 bi (2026-07)**, a ~146× move over seven months.
- Mercado Bitcoin shows a slower structural shift: USDC grew from
  ~11 mi/month (Jan 2024) to ~0.8 bi/month (Jul 2026), while its USDT
  monthly volume declined through 2026 (from ~0.4-0.6 bi to ~0.2 bi).

## Signals

1. **Regime change in 2026-07 on Foxbit:** the largest single break in
   the entire dataset; must not be explained away as noise.
2. **USDC overtakes USDT in exchange volume in 2026** (49.7% YTD share),
   consistent with the Receita trend (finding 02).
3. **Venue divergence:** MB USDT *declining* while Foxbit volume
   *explodes* — the aggregate hides opposite venue-specific behavior.
4. **Zero-volume structure:** Foxbit USDC has 12.8% days with no volume —
   coverage days ≠ traded days.

## Questions for further investigation

- What changed on Foxbit around 2026-07 (market maker, API coverage,
  product, fee structure, large institutional client)?
- Is the MB USDT decline offset by other pairs not in this sample
  (e.g., USDT via other venues), or is it real displacement by USDC?
- Does the step-change persist in October 2026 data?

## Related files

- `data/gold/exchange_stablecoin_activity.csv`
- `src/ingestion/download_exchange_data.py`
- `src/transformation/transform_exchange_data.py`
- `src/analysis/build_exchange_gold.py`