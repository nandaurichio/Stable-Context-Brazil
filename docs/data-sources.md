# Data Sources

Stable-Context: Brazil uses multiple independent data sources.

Each source has a specific analytical role. The project does not assume that different sources measure the same phenomenon.

## Receita Federal

### Role

Brazilian cryptoasset activity reported under Brazilian tax reporting rules.

### Data

The project uses the open dataset published by Receita Federal containing reported cryptoasset operations.

The dataset includes monthly information by cryptoasset, including:

- Number of operations
- Total value of operations
- Average value per operation

It also provides aggregated information according to the reporting channel, including Brazilian exchanges, foreign exchanges and operations without exchanges.

### Current Bronze Source

File:

`data/bronze/criptoativos_dados_abertos_20260826.xls`

Ingestion script:

`src/ingestion/download_brazil_data.py`

### Important Limitations

The dataset represents reported activity under the applicable reporting rules.

It does not provide a complete representation of all cryptoasset activity in Brazil.

The aggregate data does not identify individual users, wallets or specific transactions.

The first observation of an asset in the dataset must not automatically be interpreted as the beginning of adoption.

Reported values may also change because of late or rectifying declarations.

## Brazilian Exchanges

The project uses Brazilian exchange APIs to observe stablecoin activity in Brazilian fiat markets.

### Exchanges

- Mercado Bitcoin
- Foxbit

### Markets

The initial analysis focuses on:

- USDT/BRL
- USDC/BRL

Other stablecoin or crypto pairs are not automatically combined with these markets because they represent different market relationships.

### Coverage Inspection

The project uses CCXT to inspect exchange market availability and historical OHLCV coverage.

Script:

`src/ingestion/inspect_exchanges.py`

Output:

`data/bronze/exchange_coverage.csv`

### Important Limitations

The first available historical candle is treated as API/data coverage, not automatically as the beginning of market adoption or the date a market was created.

Exchange datasets represent activity within a specific trading venue and should not be interpreted as the entire Brazilian market.

## The Graph

The Graph is used as an on-chain data source.

The project uses Standardized Subgraphs with the Lending/CDP schema to enable comparable data across protocols.

### Protocols

- Aave
- Compound
- Spark

### Assets

The initial analysis focuses on:

- USDC
- USDT

### Standardized Data

The project uses daily market snapshots containing fields such as:

- Timestamp
- Protocol
- Market
- Asset
- Input token balance
- Input token price
- Total value locked
- Daily deposits
- Daily borrows
- Daily withdrawals
- Daily repayments
- Daily active users

### Current Bronze Sources

Files:

`data/bronze/aave_stablecoin_snapshots.json`

`data/bronze/compound_stablecoin_snapshots.json`

`data/bronze/spark_stablecoin_snapshots.json`

Ingestion script:

`src/ingestion/download_graph_data.py`

### Current Observed Coverage

Aave:

- USDC: 2023-01-27 → 2026-09-11
- USDT: 2023-02-13 → 2026-09-11

Compound:

- USDC: 2023-01-01 → 2026-09-11
- USDT: 2024-07-06 → 2026-09-11

Spark:

- USDC: 2023-03-07 → 2026-09-10
- USDT: 2023-10-19 → 2026-09-11

The common period across the six selected markets begins on 2023-10-19.

These dates describe the available observations in the selected datasets. They are not interpreted as adoption start dates.

### Important Limitation

On-chain activity does not establish that a wallet or address belongs to a Brazilian user.

The Graph therefore provides on-chain context for the research rather than a direct measure of Brazilian users.

## Banco Central do Brasil

Banco Central do Brasil is used as an economic, foreign-exchange and regulatory context source.

### Potential Data

The project may use:

- Exchange-rate data
- Economic indicators
- Regulatory information
- Foreign-exchange context

### Analytical Role

BCB data is contextual.

It is not treated as a direct equivalent to the cryptoasset activity reported by Receita Federal or the market activity observed on exchanges.

## Source Combination

The project uses the sources in complementary roles:
```text
Receita Federal
    ↓
Brazilian reported activity

Mercado Bitcoin + Foxbit
    ↓
Brazilian fiat market activity

The Graph
    ↓
On-chain lending activity

Banco Central do Brasil
    ↓
Economic and regulatory context
```

The sources are combined only after their scope and limitations are understood.

Cross-source relationships are treated as signals for investigation, not as proof of causality.

## Source Selection Principle

A source is included when it contributes an observable dimension of the research question.

The project avoids forcing different datasets into a single metric when their underlying meanings are different.

The goal is not to find one definitive source.

The goal is to build an evidence trail from independent observations.
