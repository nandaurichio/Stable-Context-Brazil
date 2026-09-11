<img width="2172" height="724" alt="stablecontexbr" src="https://github.com/user-attachments/assets/1b86545e-5760-427d-a3a5-129d86250e47" />


> Exploring how Brazil interacts with DeFi through stablecoin activity and economic context.

## About

Stable-Context: Brazil is an exploratory research project investigating
observable signals of DeFi adoption in Brazil through stablecoin activity
on Ethereum.

The study uses **USDT and USDC** as an initial observational lens,
examining activity from **2024 onward** alongside selected Brazilian
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

## V1 — Initial Research Prototype

The first version focuses on:

- **Ethereum**
- **USDT and USDC**
- **2024 onward**
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
he project distinguishes between observed data, derived metrics,
contextual information and interpretation.

Observed relationships are treated as signals for further investigation,
not as proof of causality.
```

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
-Web3.py
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

Developed for ETHOnline 2026.
