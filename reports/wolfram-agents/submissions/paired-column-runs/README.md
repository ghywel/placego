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

## External replay report, read in GC2070

A [public PR49 replay comment](https://github.com/WolframInstitute/Rule30PrizeKit/pull/49#issuecomment-6486666534)
reports a fresh dependency build and unchanged official checker accepting both headlines/81 declarations. Its
full module digest72839fb64b4314f4d362689503ae0cdff154859aaafffb8b8471449cf80a8469 matches our retained
catalog bytes. GPT read the complete comment and independently compared the digest; the external build itself
was not rerun here or audited file by file. This corroborates the existing Lean Verified outcome, not a human
carrying read or new mathematics. L1102 records the report; no reply or external message was sent.
