# Analysis Findings — 05. Brazilian Context

> Status: exploratory observation, based on Banco Central do Brasil
> series. Context is used to *investigate* signals, not to explain them.

## Scope

| Item | Value |
|---|---|
| Dataset | `data/silver/bcb_monthly.csv` (bronze in `data/bronze/bcb/`) |
| Series | Selic target rate (sgs 432, monthly last), USD/BRL mean (sgs 10813, monthly avg) |
| Coverage | 2023-01 → 2026-09 (BCB series) |
| Role | Economic and foreign-exchange context for the observed signals |

## Observations

### Selic target rate

| Period | Selic | Note |
|---|---|---|
| 2023 (until 2023-08) | 13.75% | cycle high |
| 2023-08 → 2024 | lowered to **10.50%** (Jun–Oct 2024) | easing cycle |
| 2025 | hiked to **15.00%** (Jun 2025) | highest in the window |
| 2026 (through Jun) | 15.00% → **14.25%** | first cuts |

### USD/BRL monthly mean

| Period | USD/BRL | Note |
|---|---|---|
| 2023-07 | 4.80 | weakest dollar in the window |
| 2024-12 | **6.10** | strongest dollar in the window |
| 2025-01 | 6.02 | still stressed |
| 2026-05 | 4.98 | BRL regained 2023 levels |
| 2026-06 | 5.13 | |

The 2024 path is notable: the central bank was cutting Selic (to 10.5%)
while USD/BRL rose to its window maximum (6.10) — an FX stress period.
In 2025 the FX eased while Selic was hiked to 15%. From early 2026,
USD/BRL fell toward ~5.0 while Selic began to be cut.

## Signals

The following temporal overlaps are *candidates for investigation* —
they are coincidences in time, not causal statements:

1. **2024-11/12 FX stress + exchange ramp-up:** the first exchange
   volume acceleration (0.54 bi → 0.72 bi BRL in 2024-10/11) and the
   on-chain borrow peak (7.4 bi USD in 2024-11) coincide with USD/BRL
   at its maximum (6.10 in 2024-12).
2. **2025 mid-year on-chain peak at cycle-high Selic (15%) and
   USD/BRL ~5.5:** deposits/borrows/TVL/user peaks on-chain occurred
   while domestic rates were at their highest in the window.
3. **2026-07 exchange regime change during BRL strength and first Selic
   cuts:** the largest exchange break in the dataset happens while
   USD/BRL sits around 5.0–5.1 and the easing cycle has begun.
4. **USDC share growth (2026) on all sources coincides with the start of
   the monetary easing window.**

## Questions for further investigation

- Does the 2024-12 FX peak align with a specific regulatory/balance-of-
  payments event (to be collected from external context, not inferred)?
- Is there a relationship between USD/BRL direction and exchange
  stablecoin volume growth, or do the series simply share a trend?
- Which Brazilian regulatory milestones (tax framework, Pix automation,
  stablecoin regulation draft, exchange certifications) fall inside the
  2025-2026 window? These are external facts to be collected, not
  derived from the data.

## Related files

- `data/bronze/bcb/selic_meta.json`, `data/bronze/bcb/usd_brl.json`
- `data/silver/bcb_monthly.csv`
- `src/ingestion/fetch_bcb.py`
- `src/transformation/bcb_monthly.py`
- `src/analysis/plot_monthly_context.py` → `docs/working/monthly_context_index.png` (local, gitignored)