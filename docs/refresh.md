# Refresh Procedure

How to refresh the V1 data pipeline from source to analysis.

> Context: each source publishes at its own cadence. Receita Federal
> publishes monthly; exchanges and The Graph can be pulled at any time;
> BCB series update daily. The refresh is therefore a **partial
> pipeline**: run all steps, but only the sources that actually changed
> will produce new observations.

## Prerequisites

- Network access.
- `THE_GRAPH_API_KEY` environment variable for The Graph step:
  ```bash
  export THE_GRAPH_API_KEY=your_key_here
  ```
- Python dependencies: `pip install -r requirements.txt`.

## Order of execution

Run from the repository root.

### 1. Ingestion (Bronze)

```bash
# Receita Federal — check the publication URL first!
# The file name encodes the publication date (criptoativos_dados_abertos_YYYYMMDD.xls).
# Update the SOURCE_URL in src/ingestion/download_brazil_data.py
# when a new monthly publication exists, then:
python3 -m src.ingestion.download_brazil_data

# The Graph (Aave, Compound, Spark) — needs THE_GRAPH_API_KEY
python3 -m src.ingestion.download_graph_data

# Exchanges (Mercado Bitcoin, Foxbit) via CCXT
python3 -m src.ingestion.download_exchange_data

# Banco Central do Brasil (Selic, USD/BRL) — end date is dynamic (today)
python3 -m src.ingestion.fetch_bcb
```

### 2. Transformation (Silver)

```bash
python3 -m src.transformation.transform_graph_data
python3 -m src.transformation.transform_receita_data
python3 -m src.transformation.transform_exchange_data
python3 -m src.transformation.bcb_monthly
```

### 3. Analysis (Gold + context)

```bash
python3 -m src.analysis.build_graph_gold
python3 -m src.analysis.build_receita_gold
python3 -m src.analysis.build_exchange_gold
python3 -m src.analysis.build_graph_monthly
python3 -m src.transformation.build_monthly_context
python3 -m src.analysis.monthly_exploration
python3 -m src.analysis.plot_monthly_context   # writes docs/working/ (gitignored)
```

### 4. Validation

```bash
python3 -m unittest discover -s tests -v
```

### 5. Review what changed

```bash
git status --short
git diff --stat
```

Groups of files to expect after a partial refresh:

| Source refreshed | Expected changed files |
|---|---|
| Receita | bronze XLS path, silver `receita_*`, gold `receita_*`, `monthly_context.csv` |
| The Graph | bronze/silver snapshots json, gold `ethereum_lending_activity*` |
| Exchanges | bronze/silver `exchange_daily_ohlcv.csv`, gold `exchange_stablecoin_activity.csv`, `monthly_context.csv` |
| BCB | `data/bronze/bcb/*.json`, `data/silver/bcb_monthly.csv`, `monthly_context.csv` |

## Semantics to respect

- A new first observation in any source is **coverage**, not adoption.
- Do not replace missing values with zero across sources with different
  end dates (see `src/transformation/build_monthly_context.py`).
- After a Receita update, re-check the coverage tests
  (`tests/test_gold_datasets.py` contains the current assumptions:
  Receita ends 2026-06, context spans 2023-01 → 2026-09).
- Update the analysis findings and the context registry
  (`docs/context/`) with any new coverage or observed changes.