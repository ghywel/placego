# Submission draft: white runs beside two periodic columns (Theorem B)

Local, 2026-10-29 (L1084). Theorem B of PROOFS.md entry 6, with GPT's odd-run refinement, ported to the kit's
core Lean on `Rule30Realization.evol`.

- `Rule30PairedColumnRuns.lean`: the kit catalog module, committed on a local kit branch `paired-column-runs`
  (not pushed). The kit's `Check.lean` passes (`--claim partial`, both headlines, 81 constants replayed,
  standard axioms: propext and Quot.sound).
- `Rule30Submission.lean`: the same proof as the essay's module, which compiles against the verifier's kit with
  the same axioms.
- `essay.md`: the draft essay. Its census cell was run separately (rings of 3 to 14 cells in the Wolfram
  Language, and 3 to 18 in Python), with no violations and the bound attained at P = 3 and P = 4.

**Status (L1086):** GPT's carrying read accepts both theorems (GC2050). Its two artifact corrections are made:
the period-3 ether is written left to right as (000010011111)^∞ and checked with `CellularAutomaton` itself, and
"common period" replaces "least period". Kit pull request: https://github.com/WolframInstitute/Rule30PrizeKit/pull/49.
Portal: R30-20261029-8131b1, uploaded under the owner's permission of 2026-10-29.
