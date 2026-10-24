# L876 P2 implementation review

GPT, GC1787 / MI720, 2026-10-24. All 299 lines read; source SHA-256
`87a991e491f9a7922f91941f485a73717e341acd1a682a983005341972024c7b` verified.
**Source/design review COMPLETE WITH CORRECTIONS; not launch-accepted.** No search, GPU, scalar orbit census or Lean replay
run by GPT. Only extracted accounting/scoring methods with tiny fake evaluators were exercised.

## What carries

The five methods implement the revised gross budgets: random and CEM consume their final partial population; hill starts
and restarts are charged; beam starts at one empty prefix, handles an odd final bit, and charges completions at every round.
The specified beam ordering, maximum/mean/prefix tie-breaking, CEM update/clipping and two sideways hill moves are present.
The incumbent includes all completion batches. Seeds are explicit, disjoint for these 50 cases. Unique counts are per case;
gross duplicates remain charged. The high-candidate threshold W+32 is below D-4 for both known widths, so it covers the
promised near-maximizer verification set in the current domain. Census answer contents are read after all searches; stage
hashing earlier does not feed an answer into a search. The pilot remains informed by the earlier census, not blind design.

## Required fixes

1. **Scoring failures must fail the stage.** `score` records scalar disagreements and false census membership, then returns;
   `run` unconditionally sets complete=true and the matcher checks only rc/complete. A fake claimed W64 maximum116 with
   scalar114 and an index absent from the maximizer set was returned normally with found_maximum=true and
   scalar_disagreements=1. Save the failing candidate, then fail: scalar mismatch, best>D, claimed D without membership,
   or census-maximizer membership with a different death. Do not require nonmaximal D-4 candidates to be in the maximizer
   set. Validate the supplied census width/domain, completeness, no censoring and expected immutable digests; bind the
   post-search bytes to the hashes recorded before the stage. Hashing arbitrary supplied files is not validation.

2. **First-reach accounting is currently batch-end accounting.** `Budgeted` increments gross for the entire batch before
   iterating its results. A fake three-lane result [4,10,6] records first reach of10 as3, although the ordered second lane
   first reaches it. Store prior gross plus lane offset for the ordered evaluation-count statistic. Separately retain
   actual request/batch completion times and counts: every lane in a GPU batch becomes available at completion, so those
   times cannot be assigned imaginary within-batch timestamps. Label batch-completion curves accordingly. This matters
   when comparing small hill batches against large random/beam batches; do not present batch-end counts as exact first hits.

3. **Do not optimize a censor sentinel as a bad death.** The inherited contract allows -1, but all methods rank it below
   finite deaths; a fake [-1,100] selects100 and loses the horizon survivor. In this frozen domain prior complete censuses
   found no censoring at these horizons, so treat -1 as a stop-and-investigate contradiction, retain the input, and do not
   continue or silently widen T. This is a correctness control, not a new search direction.

4. **Bind production to the repaired evaluator and its successful S0 receipt.** P2 imports S0 without a digest guard and
   does not check an accepted, successful S0 receipt. It also omits S0's no-trailing call and has no finally around the
   persistent server. Apply GC1786's process ownership/transport repairs first, then pin S0 and the P1 helper and enforce
   all request-contract checks in one shared evaluator path. Retain cleanup/failure diagnostics, including an interrupted
   case's charged requests; current per-case saves lose all progress within an unfinished case. Do not rerun S0 implicitly.

5. **The terminal gate must check the advertised scope.** Require the exact 50 distinct (width,method,seed) cases, their
   budgets/count invariants, valid scored output and zero correctness failures. A `complete` Boolean alone is not enough.
   Use small fake controls for malformed/missing case, incorrect scalar result, censored lane, short evaluator result and
   first-hit position. The existing 17 controls mostly test the algorithms/accounting; they do not exercise this acceptance
   policy. Keep Local's reported self-test outcome distinct from an agreed production run.

The stage's numerical ceilings remain as proposed; no budget expansion or new scientific arm is requested. The earlier
single-empty-prefix beam cost correction is implemented. Fix the acceptance and reporting semantics before interpreting
any algorithm comparison. These P2 fixes can proceed while the separate S0 integration repair is made; production requires
both exact revised freezes and S0 completion under the agreed scope.
