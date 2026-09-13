# Demo Video Guide (2–3 minutes)

Record screen + mic. The notebook is the star: reproducibility is the
point. Share screen in the repo (or run the notebook live).

---

## Script

### 0:00–0:15 — Hook (voiceover over the README title)

> "Brazil is one of the largest stablecoin markets in the world — but
> how do we actually *measure* its relationship with DeFi?"

### 0:15–0:45 — The question + the method

Show `README.md` (Central Question). Then:

> "My project, Stable-Context: Brazil, answers this with data — not
> opinions. Four independent sources — Receita Federal, Brazilian
> exchanges, on-chain lending via The Graph, and Banco Central — cleaned
> into one reproducible pipeline: Bronze, Silver, Gold."

Mouse-over the tech/files briefly (docs/analysis-findings/, src/).

### 0:45–1:25 — The three signals

Flip to `notebooks/01-exploratory-analysis.ipynb` (already executed —
just scroll). Or show the three figures in `docs/figures/`.

- **Figure 2 (exchange breakout):** → "Signal one: a 10× regime change
  in July 2026 — stablecoin spot volume jumped to 14.4 billion reais in
  a single month, 93% on Foxbit."
- **Figure 1 (cross-source index):** → "Signal two: divergence — global
  on-chain lending peaked in mid-2025 and fell, while Brazilian
  measures kept climbing."
- **Figure 3 (USDC shift):** → "Signal three: three independent sources
  converged on a USDT-to-USDC shift in 2026 — Receita went from 5% to
  29% USDC share."

### 1:25–1:55 — Reproducibility (the differentiator)

Run in terminal:

```bash
python3 -m unittest discover -s tests -v
```

Show "16 tests OK". Then scroll `docs/refresh.md`:

> "Everything regenerates from source. Here's the refresh runbook —
> ingestion, transformation, analysis — and 16 tests that validate the
> data before I trust it."

### 1:55–2:25 — Honesty + next steps

> "What I'm NOT claiming: no causality, no wallet identification. The
> July breakout is concentrated on one venue — I don't know yet why.
> That's exactly what my research pipeline is built to investigate
> next, using the external-context registry and this verification
> checklist."

Show `docs/context/verification-checklist.md` briefly.

### 2:25–2:45 — Close

> "Stable-Context: Brazil — observable signals, reproducible evidence,
> honest scope. Thank you."

---

## Practical tips

- Keep the mouse steady; zoom in (OS zoom, not browser zoom) on the
  figures.
- If recording on a laptop: `⌘⇧5` (macOS) or Game bar (`Win+G`) — screen
  + mic.
- The notebook cells are already executed; just scroll, don't re-run
  (avoids long cells).
- 1080p, landscape. Add captions if your platform supports them.