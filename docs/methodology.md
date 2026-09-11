# Methodology

Stable-Context: Brazil is an exploratory data research project focused on observing stablecoin activity through a Brazilian lens.

The project follows a data-first approach:
```text
SOURCE
  ↓
INGEST
  ↓
UNDERSTAND
  ↓
TRANSFORM
  ↓
OBSERVE
  ↓
DATA SIGNALS
  ↓
INVESTIGATE
  ↓
CONTEXT
  ↓
EXPOSE
```

## Research Principles

- No predefined hypothesis.
- No assumptions about what the data should show.
- Observations come before interpretation.
- Signals are investigated rather than treated as conclusions.
- Observed relationships are not treated as proof of causality.
- Different sources are analyzed according to what they actually measure.
- On-chain data is not used to identify Brazilian individuals or wallets.
- The absence of a signal is also a valid research result.

## Data Architecture

The project follows a Medallion-style architecture:
```text
Bronze → Silver → Gold → Analysis
```

### Bronze

Raw data collected from external sources with minimal modification.

### Silver

Cleaned and standardized data with explicit types, timestamps, units, identifiers and common field definitions.

### Gold

Analytical datasets derived from the Silver layer for comparison and exploratory analysis.

### Analysis

Exploratory analysis used to identify observations, signals, divergences and areas for further investigation.

## Research Workflow

The project separates data processing from interpretation:

Observed Data
    ↓
Derived Metrics
    ↓
Data Signals
    ↓
Investigation
    ↓
Context
    ↓
Interpretation

The pipeline does not encode a predefined narrative.

Its purpose is to prepare and organize the data so that relevant patterns can be observed before possible explanations are investigated.

## Data Sources

Each source has a specific analytical role.

### Receita Federal

Provides declared cryptoasset activity reported under Brazilian tax reporting rules.

It is used as a Brazilian activity source and should be interpreted according to the scope and methodology of the underlying reporting system.

### Brazilian Exchanges

Market data from Brazilian exchanges is used to observe stablecoin activity in Brazilian fiat markets.

The project currently investigates USDT/BRL and USDC/BRL markets through exchange APIs.

Exchange API coverage is treated as a property of the available dataset and not automatically as the beginning of market adoption.

### The Graph

The Graph provides on-chain data used to observe stablecoin activity in standardized lending markets.

The project currently uses standardized Lending/CDP data across:

- Aave
- Compound
- Spark

The Graph is an on-chain context source. It is not used to determine whether a specific wallet or address belongs to a Brazilian user.

### Banco Central do Brasil

Banco Central do Brasil data is used as economic, foreign-exchange and regulatory context.

It is not assumed to be a direct equivalent to the cryptoasset activity datasets.

## Cross-Source Analysis

The project combines independent sources only after understanding what each source measures.

Cross-source comparisons are used to investigate temporal relationships, convergences and divergences.

They are not treated as proof of causality.

## Temporal Analysis

When sources have different historical coverage, the available period is documented explicitly.

A dataset's first available observation is not automatically interpreted as:

- the beginning of adoption;
- the beginning of market activity;
- the date a token was launched;
- or the date a protocol became available.

Coverage is treated as a characteristic of the source and its available historical data.

When comparability requires a common period, the analysis uses the intersection of the available coverage of the selected datasets.

## Interpretation Principles

The project distinguishes between:

- Observed data — values directly obtained from a source.
- Derived metrics — values calculated from observed data.
- Data signals — patterns or changes that deserve attention.
- Context — external information that may help investigate a signal.
- Interpretation — explanations considered after observing the data.

A signal is not a conclusion.

A correlation is not automatically a causal relationship.

An absence of evidence in a specific dataset is not automatically evidence that an event did not occur.

## Reproducibility

Data ingestion, transformation and analytical steps are implemented as code whenever possible.

The repository maintains a separation between:
```text
Ingestion
    ↓
Transformation
    ↓
Analysis
    ↓
Interpretation
```

Scripts are responsible for making data processing reproducible and explicit.

Documentation records the reasoning, scope and limitations of the research.

The project is designed to evolve as new data becomes available without requiring the research methodology to be rewritten around a predetermined conclusion.
