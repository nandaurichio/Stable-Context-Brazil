<img width="2172" height="724" alt="stablecontexbr" src="https://github.com/user-attachments/assets/1b86545e-5760-427d-a3a5-129d86250e47" />

---

##  MVP Submission — Proof of the Central Question

> **How can observable stablecoin activity on Ethereum help us understand
> the evolving relationship between Brazil and decentralized finance?**

**Answer:** Yes — observable stablecoin activity produces measurable,
cross-validated signals: Brazilian-facing activity grew and broke out in
2026-07; global on-chain lending diverged from Brazilian measures; and
three independent sources converged on a USDC shift in 2026.

- Evidence figures → **`docs/figures/`**
- Findings (01–06) → **`docs/analysis-findings/`**
- 16 data-integrity tests → `python3 -m unittest discover -s tests`
- Reproducible notebook → `notebooks/01-exploratory-analysis.ipynb`

> Exploring how Brazil interacts with DeFi through stablecoin activity and economic context.

## About

Stable-Context: Brazil is an exploratory research project investigating
observable signals of DeFi adoption in Brazil through stablecoin activity
on Ethereum.

The study uses **USDT and USDC** as an initial observational lens,
examining activity from **2023 onward** alongside selected Brazilian
economic and regulatory context.

The goal is to identify observable patterns and generate hypotheses about
Brazil's evolving relationship with decentralized finance.

---

## Research Questions

### Central Question

> **How can observable stablecoin activity on Ethereum help us understand
> the evolving relationship between Brazil and decentralized finance?**

### Investigation Questions

- How does USDT and USDC activity evolve over time?
- How does on-chain lending activity change for these assets?
- How do different data sources compare?
- Which economic and regulatory events provide relevant context?

The questions are exploratory. No outcome is assumed in advance.

Observed relationships are treated as signals for further investigation,
not as proof of causality.

---

## Current Findings (V1)

Exploratory observations from the Gold datasets (2023-01 → 2026-09),
documented in `docs/analysis-findings/`:

- **Divergence:** global on-chain stablecoin lending (The Graph) peaked
  in mid-2025 and declined, while Brazilian-facing measures (Receita
  Federal, exchanges) kept growing into 2026.
- **Exchange regime change (2026-07):** stablecoin spot volume on
  Mercado Bitcoin + Foxbit jumped ~10× (14.4 bi BRL in one month,
  93% on Foxbit) — a sustained, multi-week step, not a single-day
  artifact.
- **USDC convergence (2026):** USDC share rose in all three independent
  sources — Receita (5% → 29.3% by 2026-06), exchanges (49.7% of 2026
  YTD notional) and on-chain deposits — in the same window.
- **Reported stablecoin growth:** declared stablecoin value grew from
  ~15 bi BRL/month (2023) to ~48-52 bi BRL/month (mid-2026).

All findings are signals for investigation, not conclusions. See
`docs/analysis-findings/` for details, `docs/context/` for the external
context registry and `docs/refresh.md` for the refresh procedure.

---

## V1 — Initial Research Prototype

The first version focuses on:

- **Ethereum**
- **USDT and USDC**
- **2023 onward**
- Selected Brazilian economic indicators
- Selected economic and regulatory events
- Exploratory temporal analysis

The purpose of V1 is to test a reproducible workflow for combining
onchain activity with Brazilian context.

---

## Methodology

```text
Ethereum
   ↓
USDT / USDC
   ↓
The Graph
   ↓
Python + SQL
   ↓
Data Processing
   ↓
Brazilian Context
   ↓
Exploratory Analysis
   ↓
Observations & Hypotheses
```

The project distinguishes between observed data, derived metrics,
contextual information and interpretation.

Observed relationships are treated as signals for further investigation,
not as proof of causality.

## Data Architecture

The prototype follows a simple Medallion Architecture:
```text
Bronze → Silver → Gold → Analysis
Bronze — raw data
Silver — cleaned and standardized data
Gold — analytical datasets
```

## Technology
```text
-Python
-SQL
-The Graph
-CCXT
-Banco Central do Brasil APIs
```

The technology stack is intentionally small. The focus is the research
workflow, not application complexity.

## Scope & Limitations

This project:
```text
does not identify individuals;
does not infer wallet nationality;
does not perform KYC;
does not create personal profiles;
does not predict markets;
does not provide investment recommendations;
does not establish economic causality.
```

Blockchain activity provides only a partial view of human behavior.
Findings are therefore exploratory and should be interpreted accordingly.

## Status

🚧 V1 — Initial Research Prototype

- Pipeline complete: ingestion → Bronze → Silver → Gold → Analysis
- Monthly cross-source context layer (2023-01 → 2026-09)
- Six exploratory findings documents (`docs/analysis-findings/`)
- External Brazilian context registry (`docs/context/`)

Developed for ETHOnline 2026.
