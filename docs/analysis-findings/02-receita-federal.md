# Analysis Findings — 02. Receita Federal

> Status: exploratory observation, based on the Gold Receita dataset.
> The source measures activity *reported under Brazilian tax reporting
> rules*, not the full universe of Brazilian cryptoasset activity.

## Scope

| Item | Value |
|---|---|
| Dataset | `data/gold/receita_stablecoin_activity.csv` |
| Coverage | 2019-08 → 2026-06 (83 months) |
| Fields | month, asset, operation_count, total_value_brl, average_value_brl, stablecoin_flag, share_of_monthly_crypto_volume |
| Stablecoins considered | USDT, USDC (`stablecoin_flag`) |

## Coverage & Limitations

- **USDT is present from the first available month (2019-08). USDC
  appears from 2019-11.** These are dataset/coverage facts, not adoption
  dates.
- Reported values may change due to late or rectifying declarations.
- The dataset does not identify individuals, wallets or transactions.

## Observations

### Stablecoin growth (declared value, BRL)

| Period | Monthly reported stablecoin value | Note |
|---|---|---|
| 2023 (avg) | ~18.5 bi BRL/month | stable |
| 2024 (avg) | ~22.8 bi BRL/month | +23% vs 2023 |
| 2025 (avg) | ~30.3 bi BRL/month | +33% vs 2024 |
| 2026-01 → 2026-06 | 31.9 → 48.0 bi BRL/month | accelerating; 2026-05 peak at 52.2 bi |

Full-year totals: **220.3 bi BRL (2023) → 273.5 bi (2024) → 363.9 bi
(2025)**. The first six months of 2026 (237.8 bi) already run at ~30% above
the 2025 pace.

### Stablecoins as share of all reported cryptoasset activity

- 2023: 89.4% · 2024: 71.9% · 2025: 79.4% · 2026 (Jan–Jun): 91.2%
- The 2024 dip coincides with a period of strong growth in total reported
  volume (all crypto monthly total grew from ~21 bi to ~48 bi BRL between
  mid-2024 and end of 2024), i.e. **the stablecoin share fell while the
  broader reported market expanded** — the share shift is a composition
  effect, not a fall in stablecoin activity itself.

### USDT vs USDC composition (share of stablecoin value)

| Month | USDT | USDC |
|---|---|---|
| 2023-01 | 94.8% | 5.2% |
| 2025-01 | 96.8% | 3.2% |
| 2026-01 | 87.3% | 12.7% |
| 2026-05 | 86.1% | 13.9% |
| 2026-06 | 70.7% | **29.3%** |

USDC monthly value: ~0.4–1.5 bi BRL (2023–2024) → ~1–3.5 bi (2025) →
**14.1 bi BRL in 2026-06**. The single-month jump in 2026-06 is the
largest asset-level change in the dataset.

## Signals

1. **Continuous growth with acceleration in 2026:** no plateau in the
   declared stablecoin series through mid-2026.
2. **USDC share inflection (2026):** a clear, late-starting shift from
   USDT toward USDC, visible both in relative share and absolute value.
3. **Share dynamics (2024):** stablecoin share of reported activity
   compressed during a broader reported-market expansion — worth
   separating from stablecoin-specific behavior.

## Questions for further investigation

- Is the USDC increase driven by a specific reporting channel (Brazilian
  exchanges, foreign exchanges, no exchange)?
- Does the 2026-06 USDC jump align with a regulatory or tax event?
- How much of the 2024 share dip is explained by BTC/ETH reported volumes?

## Related files

- `data/gold/receita_stablecoin_activity.csv`
- `sql/receita/stablecoin_share.sql`
- `sql/receita/stablecoin_by_asset.sql`
- `src/transformation/transform_receita_data.py`
- `src/analysis/build_receita_gold.py`