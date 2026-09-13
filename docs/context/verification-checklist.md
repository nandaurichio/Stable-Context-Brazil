# Context Verification Checklist

> How to confirm the `to_verify` / `medium` rows of the Brazilian
> context registry (`data/context/brazil_events.csv`) against primary
> sources, and how to collect the missing facts for the two 2026
> investigation windows.
>
> Method: **confirm → record → update**. Never update a row's confidence
> without a primary source and a URL/identifier recorded in this log.

## How to use

1. Pick one item below.
2. Consult the **primary sources** listed (documents of record, not
   news summaries alone).
3. In the **verification log** at the end, record: date verified,
   source URL / document identifier, what was confirmed, and the exact
   date/number corrected.
4. Update `data/context/brazil_events.csv` (title/detail/date) and set
   `confidence` to `high` (or `medium` if only a secondary source was
   found).
5. If a finding doc cites the item, update the citation.

---

## Part 1 — Confirmation of registry rows (5 items)

### 1. VASP public consultations (2023-10-11, `to_verify`)

- **Claim:** BCB opened public consultations on VASP regulation (licensing + risk management).
- **Primary sources:** BCB website (`bcb.gov.br`), "Consultas Públicas" page; edital numbers; Diário Oficial da União (DOU).
- **Questions:** Exact consultation numbers and dates? Topics covered? Closed or open?
- **Why it matters:** First formal step toward licensing VASPs — relevant baseline for all 2024-2026 exchange activity.

### 2. Fiscal-package announcement and FX stress (2024-11-27, `medium`)

- **Claim:** late-Nov-2024 fiscal announcement triggered market repricing; USD/BRL accelerated into the Dec-2024 peak (6.10 monthly mean, window maximum).
- **Primary sources:** DOU (medida provisória / decreto text), Ministry of Finance announcements, COPOM minutes (Dec 2024), BCB market reports.
- **Questions:** Exact announcement date/time? Which instruments? Sequence of events vs. the USD/BRL daily path in late Nov / early Dec?
- **Why it matters:** This window overlaps the first exchange volume acceleration and the Nov-2024 on-chain borrow spike.

### 3. Lei 14.973/2024 — foreign-income taxation (2024-12-19, `to_verify`)

- **Claim:** law on foreign-income taxation includes digital assets held abroad.
- **Primary sources:** DOU (official text), website of the Brazilian Senate/Câmara (PL number, processing).
- **Questions:** Correct law number and date? Does the text actually cover cryptoassets? Effective date?
- **Why it matters:** If it affects crypto held abroad, it may relate to reporting channels in the Receita data (foreign exchanges channel).

### 4. FX stress + BCB spot interventions (2025-01-15, `medium`)

- **Claim:** Jan-2025 FX stress; USD/BRL above 6.20 intraday; BCB sold USD in the spot market.
- **Primary sources:** BCB press releases on interventions (leilões), Ptax records, COPOM minutes (Jan 2025).
- **Questions:** Exact intervention dates and sizes? USD/BRL intraday high and closing dates in Jan 2025?
- **Why it matters:** Context for the top of the USD/BRL window just before the 2025 stablecoin rulemaking debate.

### 5. BCB stablecoin rulemaking draft (2025-01-31, `to_verify`)

- **Claim:** reports (Jan/Feb 2025) of a BCB draft regulating stablecoins, incl. possible restrictions on transfers to self-custody wallets; BCB later clarified no ban.
- **Primary sources:** BCB press notes and public statements; published consultation/minuta if any; press from Reuters/Valor for the timeline.
- **Questions:** Was there an official draft or only reports? What did the final public position say? Timeline of publications through 2025-2026?
- **Why it matters:** Stablecoin regulation directly conditions the composition signal (USDT→USDC shift) observed in all three sources in 2026. This is the **most important regulatory item** to confirm.

---

## Part 2 — Incomplete track (3 items, need 2025 status)

### 6. Pix Automático / Pix por aproximação (2025-06-30, `to_verify`)

- **Primary sources:** BCB "Pix" official page; BCB news.
- **Questions:** Actual launch dates in 2025? Did they land before the on-chain peak window (Jun-Aug 2025)?
- **Why it matters:** Payments rail modernization is background context for stablecoin use cases in Brazil.

### 7. Stablecoin rulemaking progress 2025 (`to_verify`)

- **Primary sources:** BCB website, COPOM/agenda statements, DOU.
- **Questions:** Any official consultation published in 2025 (numbers, dates)? Any resolution/turno? Status entering 2026?
- **Why it matters:** Determines whether the 2026 USDC shift aligns with a regulatory milestone.

### 8. USDC distribution expansion in Brazil (2025, `to_verify`)

- **Primary sources:** Circle announcements; Brazilian exchange/issuer press releases (Mercado Bitcoin, Foxbit, other VASPs); issuer banking partnerships.
- **Questions:** Which partnerships/launches happened, with which dates in 2025 and H1-2026?
- **Why it matters:** Supply-side explanation candidate for the USDC share jump (HOOK into Part 3, window A).

---

## Part 3 — The two investigation windows (priority — no external facts collected yet)

### Window A — USDC share jump in Receita data (2026-06)

Observed: USDC declared value 14.1 bi BRL in one month (29.3% of stablecoins, vs ~5% in 2023-2025).

Facts to hunt (each = one log entry):

| # | Question | Where to look | Directs to hypothesis |
|---|---|---|---|
| A1 | Did a regulatory/tax change effective around 2026-06 alter how USDC operations are reported? | DOU, Receita Federal normas (IN), IRS announcements | H2 |
| A2 | Did an exchange/issuer launch USDC on/off ramps or promos in Brazil in H1-2026? | Exchange press releases, Circle/Coinbase LatAm news | H2 |
| A3 | Did the Receita dataset publication (month file) change scope/coverage in 2026? (e.g., new reporting channels) | Receita open-data portal, official documentation, notes in the XLS | H1/H2 |
| A4 | Did a large institutional program move USDC volume into Brazil-flagged channels? | Industry press, on-exchange announcements | H1/H2 |

### Window B — Exchange regime change (2026-07)

Observed: ~10× step in stablecoin BRL notional (14.38 bi in Jul, 93% Foxbit; sustained across days).

Facts to hunt:

| # | Question | Where to look | Directs to hypothesis |
|---|---|---|---|
| B1 | Foley exchange-level change on Foxbit around 2026-07: market maker entry, fee change, new product, wallet feature, institutional client | Foxbit announcements, press, CCXT market metadata changes | H1 |
| B2 | Did Foxbit's API OHLCV coverage change (new data source, backfilled history, different aggregation)? | Compare bronze CSV coverage gaps; Foxbit API docs/changelog | H1 |
| B3 | External shock (FX policy, tax, regulation, or macro event) in late Jun / early Jul 2026? | BCB, DOU, COPOM minutes, Ministry of Finance, press | H3 |
| B4 | Did CNY/BRL, PIX-related flows or wholesale activity shift toward stablecoin-BRL markets? | Exchange statements, market reports | H1/H3 |

### Method for both windows

1. Collect **dated facts** only (no opinions): date, actor, action, source URL.
2. Plot the fact date against the daily series (`data/gold/exchange_stablecoin_activity.csv` around 2026-06-20 → 2026-07-31).
3. Record which hypothesis (H1 venue-level, H2 regulatory/product/institutional, H3 macro) each fact **narrows**, not proves.
4. Add confirmed facts as new rows in `data/context/brazil_events.csv` (category `industry` or `regulatory`, confidence `high`) and remap windows in `docs/context/brazil-context-events.md`.

---

## Verification log

| # | Item / question | Date verified | Source (URL / doc ID) | Confirmed fact (correction) | New confidence | Notes |
|---|---|---|---|---|---|---|
| 1 | VASP consultations | | | | | |
| 2 | Fiscal package + FX stress | | | | | |
| 3 | Lei 14.973/2024 | | | | | |
| 4 | FX interventions Jan 2025 | | | | | |
| 5 | BCB stablecoin draft | | | | | |
| 6 | Pix rollout 2025 | | | | | |
| 7 | Stablecoin rulemaking 2025 | | | | | |
| 8 | USDC distribution 2025/H1-2026 | | | | | |
| A1 | USDC reporting change | | | | | |
| A2 | USDC on/off ramp launch | | | | | |
| A3 | Receita dataset scope change | | | | | |
| A4 | Institutional USDC move | | | | | |
| B1 | Foxbit market structure | | | | | |
| B2 | Foxbit API/coverage change | | | | | |
| B3 | External shock Jul 2026 | | | | | |
| B4 | Wholesale/PIX shift | | | | | |