# Brazilian Context Events

> Curated chronology of external Brazilian (and selected international)
> events used to *investigate* the signals observed in the Gold datasets.
>
> **Use policy:** events are context, not explanations. Coincidence in
> time is not causality. Rows marked `to_verify` must be confirmed
> against primary sources before being cited in any analysis.

Structured data: `data/context/brazil_events.csv`
(columns: date, category, title, detail, source, confidence).

Confidence levels:

- `high` — fact confirmed by a primary source or by the project's own
  datasets (e.g., Selic/USD series from BCB).
- `medium` — event well documented, exact dates/details pending.
- `to_verify` — fact or date not yet confirmed; investigation target.

## Chronology

### 2019 — Reporting framework begins

- **2019-05-21** — `regulatory` · IN RFB 1888/2019 creates the monthly
  cryptoasset reporting obligation (from 2019-08). Coincides with the
  start of the Receita Federal open dataset used in this project.

### 2022–2023 — Legal framework

- **2022-12-22** — `regulatory` · Lei 14.478/2022 (Marco Legal dos
  Criptoativos): defines VASPs and designates the Banco Central as
  regulator. In force from **2023-06-20**.
- **2023-08-10** — `regulatory` · BCB announces the Drex (digital real)
  pilot.
- **2023-10-11** — `regulatory` · BCB opens public consultations on VASP
  regulation (licensing, risk management) *[numbers/dates to verify]*.

### 2024 — Macro stress and the reported-market inflection

- **2024-01-10** — `international` · US SEC approves spot Bitcoin ETFs.
- **2024-06-19** — `monetary` · COPOM ends the easing cycle; Selic at
  10.50% (window minimum).
- **2024-11-27** — `fiscal` · Fiscal-package announcement triggers market
  repricing; USD/BRL accelerates *[date to verify]*.
- **2024-12-11** — `monetary` · COPOM resumes hikes: Selic 12.25%.
- **2024-12-18** — `fx` · USD/BRL at window highs (~6.10–6.20); project
  series shows Dec-2024 monthly mean of **6.10** (window maximum).
- **2024-12-19** — `fiscal` · Lei 14.973/2024 on foreign-income taxation
  (incl. digital assets held abroad) *[scope to verify]*.

### 2025 — Hikes to 15%, FX normalization, stablecoin rulemaking

- **2025-01-15** — `fx` · FX stress; BCB sells USD in the spot market
  *[dates to verify]*; USD/BRL above 6.20 intraday.
- **2025-01-29** — `monetary` · Selic 13.25%.
- **2025-01-31** — `regulatory` · Reports of a BCB draft on stablecoin
  regulation (possible restrictions on transfers to self-custody
  wallets); BCB clarifies no ban is planned *[final mechanism to
  verify]*.
- **2025-03-19** — `monetary` · Selic 14.25%.
- **2025-05-07** — `monetary` · Selic 14.75%.
- **2025-06-18** — `monetary` · Selic 15.00% (cycle and window peak);
  held at 15.00% into early 2026.
- **2025 (dates TBD)** — `payments/regulatory/industry` · Pix
  Automático/Por Aproximação rollout; stablecoin rulemaking agenda;
  USDC distribution expansion in Brazil *[all to verify]*.

### 2026 — Easing begins; unresolved investigation windows

- **2026-03/04/05/06/08** — `monetary` · Selic cuts: 14.75% → 14.50% →
  14.50% → 14.25% → 14.00% (from the project's own BCB series; meeting
  dates to confirm).
- **2026-06** — `industry` · **INVESTIGATION WINDOW** · USDC share jumps
  to 29.3% of declared stablecoin value (14.1 bi BRL in one month).
  External cause not yet collected.
- **2026-07** — `industry` · **INVESTIGATION WINDOW** · Exchange stablecoin
  volume breaks out (~10×, 14.4 bi BRL; Foxbit ≈ 93%). External cause
  not yet collected.

## Mapping to observed windows

| Observed signal (finding) | Window | Relevant context rows | Status |
|---|---|---|---|
| Exchange volumes first accelerate; on-chain borrows spike | 2024-10 → 2024-12 | Fiscal package; COPOM hike; USD/BRL 6.10 | Context collected (dates partly `to_verify`) |
| On-chain deposits/borrows peak; Selic at 15% | 2025-06 → 2025-09 | COPOM to 15%; stablecoin rulemaking debate; FX normalization | Context collected (rule-making details `to_verify`) |
| USDC share rises in all three sources | 2026-01 → 2026-06 | Monetary easing begins; **no external fact collected yet** | **Open — priority** |
| Exchange regime change (Foxbit) | 2026-07 | **No external fact collected yet** | **Open — priority** |

## Next actions

1. Work through `docs/context/verification-checklist.md` — it lists, for
   each pending item, the primary sources to consult, the exact
   questions to answer and a verification log to complete.
2. Collect facts for the two 2026 investigation windows (June and July):
   regulatory milestones, exchange announcements, institutional moves,
   tax-rule changes, FX policy.
3. Keep the registry in `data/context/brazil_events.csv` and re-map
   windows after each data refresh.