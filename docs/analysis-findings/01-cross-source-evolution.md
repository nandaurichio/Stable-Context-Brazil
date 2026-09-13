# Analysis Findings — 01. Cross-Source Evolution

> Status: exploratory observation, based on the Gold datasets.
> Observed data and derived metrics only. No causal interpretation.

## Scope

This document compares the temporal evolution of the four sources
assembled in the monthly context layer:

| Source | Measure used | Dataset |
|---|---|---|
| Receita Federal | Declared stablecoin transaction value (BRL) | `data/gold/receita_stablecoin_activity.csv` |
| Exchanges (Mercado Bitcoin + Foxbit) | Est. BRL notional of USDT/USDC spot trading | `data/gold/exchange_stablecoin_activity.csv` |
| The Graph (Aave, Compound, Spark) | On-chain stablecoin deposits/borrows (USD) | `data/gold/ethereum_lending_activity_monthly.csv` |
| Banco Central do Brasil | Selic target rate; USD/BRL monthly average | `data/silver/bcb_monthly.csv` |

The consolidated monthly view is `data/gold/monthly_context.csv`.

## Coverage Caveat

- The monthly context layer covers **2023-01 → 2026-09** (45 months).
- Receita Federal data ends at **2026-06**; from 2026-07 onwards the
  Receita column is missing in the context (NaN) until the next
  monthly publication is ingested.
- The 2026-09 row contains a partial month (through 2026-09-13 for
  exchanges and The Graph).
- The sources measure different phenomena and different universes
  (declared operations in Brazil vs. spot trading on two venues vs. global
  on-chain lending). Values are compared temporally, not as equivalents.

## Observations

### Each source grew — but on different schedules

Monthly stablecoin activity, selected reference points:

| Month | Receita (R$ bi) | Exchanges (R$ bi est.) | The Graph deposits (US$ bi) |
|---|---|---|---|
| 2023-01 | 15.3 | 0.03 | 0.06 |
| 2024-01 | 22.9 | 0.12 | 1.67 |
| 2025-01 | 30.1 | 0.53 | 8.23 |
| 2025-07 | 30.4 | 0.57 | **23.28** ← on-chain peak |
| 2026-01 | 33.1 | 1.22 | 13.17 |
| 2026-06 | 48.0 | 2.18 | 9.87 |
| 2026-07 | n/a* | **14.38** ← exchange break | 11.44 |
| 2026-08 | n/a* | 9.98 | 10.41 |
| 2026-09** | n/a* | 4.50 | 4.16 |

\* Receita dataset ends 2026-06. \*\* 2026-09 is a partial month
(through 2026-09-13).

### Timing divergence between global on-chain and Brazilian sources

- **The Graph (global lending) peaked in mid-2025** and declined afterwards:
  deposits reached 23.3 bi USD in 2025-07 and fell to ~9.9 bi USD in 2026-06.
- **Receita and the Brazilian exchanges continued to grow into 2026**, and the
  exchange series broke upward sharply in 2026-07.
- This is the main cross-source divergence in the current data:
  the Brazilian-facing measures and the global on-chain measure moved in
  opposite directions from mid-2025 to mid-2026.

### Composition convergence around USDC in 2026

USDC share of stablecoin activity, by source:

| Period | Receita (declared value) | Exchanges (est. BRL notional) | The Graph (deposits) |
|---|---|---|---|
| 2024 | ~5% | 8.9% | ~50% (mix) |
| 2025 | ~5% | 11.3% | USDT-led |
| 2026 | 29.3% (2026-06) | 49.7% (YTD) | USDC-led from 2026-05 |

All three independent sources show USDC gaining share in 2026.
This is a convergence signal, not a causal statement.

## Signals

1. **Divergence signal (mid-2025 → 2026):** global on-chain stablecoin
   lending declined while Brazilian declared and exchange activity kept
   growing. Deserves investigation before any joint narrative is built.
2. **On-chain partial rebound (2026-07/08):** deposits recovered to
   11.4 bi / 10.4 bi USD after the 2026-05/06 trough (~9.9 bi), while
   still far below the 2025-07 peak (23.3 bi). The "decline" is not a
   monotonic trend.
3. **Regime-change signal (2026-07):** a step-change in exchange volume of
   roughly 10× between June and July 2026, concentrated on Foxbit.
   See finding 03.
4. **USDC convergence signal (2026):** USDC share increased across all
   three sources in the same period.

## Questions for further investigation

- What explains the on-chain peak of mid-2025 and the subsequent decline?
  Is it protocol-specific, asset-specific, or market-wide?
- Do the Brazilian-facing series decouple from global on-chain trends, or
  is the divergence an artifact of the narrow exchange sample?
- Which events or structural changes overlap with the 2026-07 exchange
  step-change?

## Related files

- `data/gold/monthly_context.csv`
- `data/gold/monthly_exploration.csv` (MoM % variations)
- `src/analysis/monthly_exploration.py`
- `src/transformation/build_monthly_context.py`

## Open items

- Rebuild the monthly context again after the next Receita Federal
  monthly publication (currently ends 2026-06) to remove the NaN tail.
- The Graph monthly layer now follows the raw data to 2026-09; re-run
  `src/analysis/build_graph_monthly.py` after each ingestion refresh.