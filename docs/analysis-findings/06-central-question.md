# Analysis Findings — 06. Central Question

> How can observable stablecoin activity on Ethereum help us understand
> the evolving relationship between Brazil and decentralized finance?

> Status: synthesis of findings 01–05.
> This document assembles the evidence trail; it does not assert causality.

## What the data shows (observed signals)

### 1. Brazilian-facing stablecoin activity grew steadily — and broke out in July 2026

- Declared stablecoin activity (Receita Federal): ~15 bi BRL/month in
  early 2023 → 48–52 bi BRL/month by mid-2026, no plateau.
- Exchange spot notional (MB + Foxbit): ~0.12 bi BRL/month (Jan 2024)
  → ~2.2 bi (Jun 2026) → **14.4 bi in Jul 2026** (Foxbit-driven;
  sustained across days, not a one-day artifact).
- The 2026-07 exchange step is the single largest structural break
  observed in any source of this project.

### 2. Global on-chain lending tells a different story — and that divergence is itself a finding

- Ethereum stablecoin deposits (Aave/Compound/Spark): peak 23.3 bi USD
  (Jul 2025) → ~9.9 bi (Jun 2026), a ~57% decline; TVL peaked Sep 2025
  and users peaked Nov 2025.
- Brazilian-facing measures kept rising through the on-chain decline.
- Therefore: a joint "stablecoin growth" narrative cannot be applied to
  both universes. The relationship between Brazil and DeFi is not
  observable through a single global stablecoin lens.

### 3. A three-source USDC shift appears in 2026

- Receita: USDC went from ~5% of stablecoin declared value (2023-2025)
  to **29.3% in Jun 2026** (14.1 bi BRL in one month).
- Exchanges: USDC share of est. BRL notional reached **49.7% YTD 2026**
  (vs 8.9% in 2024).
- On-chain: the USDT/USDC deposit mix flipped toward USDC from 2026-05.
- Three independent sources showing the same compositional change in
  the same window is the strongest convergence signal in the project.

### 4. Contextual overlaps (to investigate, not to infer)

- 2024-11/12: exchange volumes first accelerate and on-chain borrows
  spike while USD/BRL hits its window maximum (6.10) and Selic is at
  10.5%.
- 2025 mid-year: on-chain peaks coincide with Selic at the window
  maximum (15%) and USD/BRL ~5.5.
- 2026: the exchange breakout and USDC shift happen while BRL is strong
  (~5.0) and the easing cycle has begun.

## Interpretation (cautious, exploratory)

- Stablecoin use in a Brazilian lens is **observable and growing**, but
  the growth is **not uniform across venues or markets**: Foxbit
  concentrated the 2026 break; MB USDT declined while MB USDC grew.
- The **coverage of two exchanges captures only part** of Brazilian
  market activity; the 2026-07 break may reflect venue-level factors
  (liquidity provision, institutional flows, product changes) as much as
  aggregate Brazilian demand.
- The **USDC convergence across three sources** suggests a real
  compositional shift (not a single-source artifact) and is a priority
  for external-context research.
- The **divergence between global on-chain and Brazilian sources**
  underlines the project premise: Brazil's evolving relationship with
  DeFi must be read through Brazilian-facing measures combined with
  on-chain context — not through global aggregates alone.

## Hypotheses generated (to be tested, not assumed)

1. H1: A structural (venue or market) change around 2026-07 explains the
   Foxbit volume break better than a demand shock.
2. H2: The 2026 USDC shift is associated with regulatory, institutional
   or product events that affect USDC availability/distribution in
   Brazil (external facts to be collected).
3. H3: Brazilian stablecoin activity moves with domestic macro/FX
   conditions (BRL strength/easing) differently from global on-chain
   lending.

## Recommended next steps

1. Collect external Brazilian context for the observed windows
   (2024-11/12, 2025-07/09, 2026-07): regulation, tax rulings, FX
   interventions, exchange announcements.
2. Investigate Foxbit's 2026 data properties (API coverage, market
   makers, fee/wallet features) before assuming user-level demand.
3. Re-run the monthly context layer after the next Receita Federal
   monthly publication to confirm the 2026-05/06 acceleration is
   sustained (Receita currently ends 2026-06; the context layer now
   extends to 2026-09 via the other sources).
4. Re-run the pipeline after the next ingestion refresh and document
   coverage changes between cycles.

## Resolved items

- Monthly context extended to 2026-09 (finding 01 open item).
- Spark USDT borrows/TVL inconsistency: resolved as a high-churn flow
  pattern, not a data error (finding 04).

## Related documents

- Findings: `docs/analysis-findings/01` … `05`
- Method: `docs/methodology.md`
- Sources: `docs/data-sources.md`
- Questions: `docs/research-questions.md`