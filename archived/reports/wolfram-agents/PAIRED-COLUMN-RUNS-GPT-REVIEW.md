# GPT carrying review of paired-column runs (GC2050)

29 October 2026. Read complete L1084 and the274-line catalog source at9efcfeb3, both submission headlines,
proof and scope sections of the essay, and the retained census source. Catalog, submission and embedded essay
proof bodies are identical after their wrappers. **The carrying proof is accepted. The essay needs an
orientation correction before posting.** Local's current-kit compiler/checker claims remain producer-reported;
this review did not rerun that build or the full census.

## Why the proof carries

- left_periodic uses the inverse XOR identity and retains periodicity from time0. Its iteration supplies both
  columns at each negative depth; this does not assume finite support.
- triangle's depth inequalities cover all three parents, including the natural-subtraction boundary. At
  depth d+P−1, a run R>=2P−1 supplies the first P white times; per_first then supplies every time.
- white_of_latch returns a hypothetical black cell at time t to the sample tP, using tP−t>=0 for P>=1 and
  periodicity to contradict initial whiteness. It does not assume that periodicity alone makes a latch white.
- push_to_zero shifts an adjacent always-white pair right until column0; hnz supplies the contradiction.
- shrink preserves black boundaries: the inward boundary triples are001 and100, both output1. At the last
  singleton the triple101 outputs0 for the extra tick. Thus m+2 white samples cover any P<=m+2. The neighbouring
  initially white cell really lies in the run because m>=1; the premises include both black ends and d>=1.

The conclusions are for arbitrary configurations with the stipulated common column period. The left-bounded
finite-seed version alone is vacuous by Jen, correctly stated in the essay. This neither proves eventual
aperiodicity of the singleton centre nor supplies a finite-left witness. The time0 assumption is explicit.

## Concrete essay correction: the printed period3 ether is reversed

A tiny literal left-to-right Rule30 check of the two named examples gives:

| Left-to-right cyclic word | Return times among1..claimed P |
|---|---|
| 000011111001 | none among1..3 |
| reverse of000011111001, or its rotation000010011111 | 3 |
| 0000001 | 4 |

The census bit encoding regards bit0 as the first spatial cell. FromDigits followed by the essay's ringStep
uses the opposite display order. The printed12-cell word and the direct CellularAutomaton[30,...] visualization
therefore disagree with the bit-coded calculation. This is a convention error in the example, not a failure
of the proof or of ring statistics (reflection conjugates the two orientations).

Fix options: retain the numeric bit-map and clearly label its strings as little-endian, reversing the string
passed to the direct CellularAutomaton plot; or use consistent left-to-right words000010011111 and0000001 and
swap the two spatial rotations in ringStep accordingly. Do not change just the displayed string while leaving
its FromDigits return check in the old orientation. Preserve the old outputs and regenerate the corrected
notebook cells through the established workflow. No new large census is needed to diagnose this.

Also replace 'every column ... shares its least period' by 'the global orbit period is a common period of
every column; a column may have a smaller least period'. The proof needs a common period only. For a nonzero
ring state, choose a black cell as the origin before applying the row bound to a neighbouring white run;
the theorem's nonwhite-column premise must not be dropped. These corrections do not change either headline.

**Next:** Local repairs the example/encoding wording and notebook, supplies the final source and checker receipts,
then proceeds with the kit PR and portal workflow under the owner's authorization. GPT accepts the hand/formal
carrying steps now; the corrected final artifact still needs its numerical/prose consistency check.
