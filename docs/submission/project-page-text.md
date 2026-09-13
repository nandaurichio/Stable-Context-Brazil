# Project Page Text (paste-ready)

Two versions — English (recommended for ETHOnline) and Portuguese.

---

## English (short, 100–140 words)

**Stable-Context: Brazil — Does stablecoin activity on Ethereum reveal how Brazil relates to DeFi?**

An exploratory data research project. We combine four independent sources
— Receita Federal (declared cryptoasset activity), Brazilian exchanges
(Mercado Bitcoin + Foxbit), The Graph (Aave/Compound/Spark lending) and
Banco Central do Brasil (Selic, USD/BRL) — into a reproducible
Bronze→Silver→Gold pipeline.

Findings (2023–2026): (1) Brazilian-facing stablecoin activity grew
steadily and broke out ~10× in July 2026; (2) global on-chain lending
diverged — it peaked in mid-2025 while Brazilian measures kept rising;
(3) three independent sources converged on a USDT→USDC shift in 2026.

All results are signals for investigation, not causal claims. The whole
pipeline is reproducible (16 tests, refresh runbook, context registry).

---

## Português (versão curta)

**Stable-Context: Brazil — A atividade de stablecoins na Ethereum revela como o Brasil se relaciona com DeFi?**

Pesquisa de dados exploratória. Combinamos quatro fontes independentes —
Receita Federal (atividade declarada), exchanges brasileiras (Mercado
Bitcoin + Foxbit), The Graph (empréstimos on-chain em Aave/Compound/Spark)
e Banco Central do Brasil (Selic, USD/BRL) — em um pipeline reproduzível
Bronze→Silver→Gold.

Achados (2023–2026): (1) a atividade de stablecoins em canais brasileiros
cresceu e teve salto de ~10× em jul/2026; (2) o empréstimo on-chain global
divergiu — pico em meados de 2025 enquanto as medidas brasileiras
continuavam subindo; (3) três fontes independentes convergiram em uma
mudança USDT→USDC em 2026.

Tudo é sinal para investigação, não causalidade. Pipeline reproduzível
(16 testes, runbook de atualização, registro de contexto).

---

## English (long, ~250 words, for detail boxes)

**Problem.** Brazil is one of the largest markets for stablecoins in the
world, yet measuring its relationship with decentralized finance is
methodologically hard: on-chain data does not identify nationality, and
each data source measures a different phenomenon.

**Approach.** Stable-Context: Brazil treats stablecoin activity as an
observable lens and combines independent sources — declared activity
(Receita Federal), spot trading in local pairs (Mercado Bitcoin, Foxbit),
standardized on-chain lending (Aave, Compound, Spark via The Graph) and
macro context (BCB Selic and USD/BRL) — through a reproducible
Bronze→Silver→Gold pipeline. Interpretation is kept strictly separate
from observation.

**Signals (2023–2026).**
1. **Growth:** declared stablecoin value tripled from ~15 bi BRL/month
   (2023) to ~48–52 bi BRL/month (mid-2026).
2. **Regime change:** exchange spot notional jumped ~10× in July 2026
   (14.4 bi BRL/month, 93% on Foxbit), sustained across days.
3. **Divergence:** global on-chain lending peaked in July 2025
   (23.3 bi USD deposits) and declined ~57% while Brazilian measures
   kept rising.
4. **Composition:** USDC share rose in all three sources in 2026 —
   Receita 5%→29.3%, exchanges 49.7% YTD, on-chain mix flip.

**Honesty constraints.** No wallet identification, no inferred
nationality, no causality claims. Overlaps with macro events (Selic 15%
peak, USD/BRL at 6.10) are registered as candidate context for
investigation. Reproducible: 16 data-integrity tests, a refresh runbook,
and a verification checklist for external facts.