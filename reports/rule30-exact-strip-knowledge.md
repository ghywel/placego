# What a strip knows: exact completion versus independent unknowns

GC2026, 28 October 2026. Owner-requested sustained research block begins 19:56 UTC. L1070's carrying reads of
GC2019, GC2022 and GC2024 accepted: right-front proof, seam/jump interpretation and period-three hand closure are
two-party results. No new claims about unreviewed L1066 numerical evidence.

## Pull and question

Local L1069 correctly distinguishes left XOR transfer from right OR masking, but "an unknown cannot heal" feels
in tension with our exact erasure calculation. Does three-valued loss of knowledge represent genuine ambiguity,
or loss of correlations in the observer? This is a cheap hand objection before a larger run.

Record searched: L1069 report and full 34-line source; GC1997/GC2001's three-valued dependency audit; run-rule
Theorem P; GC2022; G121/G122. None makes independent unknowns an exact description after repeated forward steps.
No novelty claim for elementary Boolean simplification or abstract interpretation.

## Hand counterexample and review qualification

Fix x[0..2]=a10 and leave every exterior cell arbitrary. Set x3=r,x4=s. The three cells entering F²(x)_2 are

    F(x)_1 = NOT a,
    F(x)_2 = NOT r,
    F(x)_3 = r OR s.

Thus F²(x)_2 = NOT a XOR ((NOT r) OR r OR s) = a. At time 1 that same cell is NOT r and truly unknown.
At time 2 it is known again. Independent ternary symbols for NOT r and r OR s lose the identity that their OR
is 1. This is genuine healing of uncertainty under the complete family of initial completions, not merely
a single damage pair healing. Status PROOF-SKETCH pending Local's read; eight scalar choices suffice to check it.

The larger two-step identity is F²(x)_i=x_(i−2) whenever x_(i−1) != x_i; the 01 orientation is seen by ordinary
ternary masking, whereas the 10 orientation requires the relation above. No finite isolated perpetual shield
follows. For the interval 010, ternary evaluation loses every known cell at time 2, yet exact completion fixes
cell 2 to 0 at that time.

L1069's universal centre-lifetime gloss needs a boundary condition: a known width-two interval 00 already has
an unknown right-hand centre after one step, versus W/2=1 known future steps. Its twelve reported samples may
still attain the upper bound; left permutivity alone does not prove attainment. With [a,b] known, F^t(x)_i is
permutive in the initial bit x_(i−t), so i−t<a guarantees ambiguity. This proves an upper deadline independent
of the right inputs, not a universal exact lifetime. Statements about arbitrary completions must also be
separated from the one fixed singleton row, for which all exterior bits are already determined by its seed.

"Only light-speed closure" needs a defined class of admissible exteriors and boundary generators. One-step
sensitivity over all completions is correct. It does not classify every invariant constrained world or every
possible internally generated boundary law; a ring is a particular feedback convention. Closed finite
autonomous states are eventually periodic; this finite-state conclusion carries in its explicit scope.

## Frozen diagnostic

For every binary known interval of widths 1..8, evolve to times 1..8 with every right completion, exactly.
Use one bitset truth table over all 16 right exterior bits, not sampling. Cells left of a+t are genuinely
ambiguous by iterated left permutivity and excluded from this evaluation; the right margin contains every
causal input of evaluated cells. Compare ordinary ternary evaluation, retain all counts and first witnesses,
look for cells that become known after being unknown and known cells beyond the initial right endpoint.
Independent literal scalar controls cover the selected small words and all their short exterior assignments.

Prediction: ternary misses real determined cells, already witnessed by a10. Counterfactual: any ternary-known
cell disagrees with exact completion, or scalar controls disagree, stops the result. Unexpected check: whether
exactly determined cells can appear beyond the original right endpoint; no all-width exclusion inferred if none.
One Intel process, no local job duplication. Caps: 30 CPU/45 wall seconds, 256 MiB sampled group RSS, 4 MiB/file,
8 MiB output; launch free+inactive 1024 MiB, ongoing 512 MiB, swap growth 128 MiB, under run_capped.py with monitor
access. Source strip_exact_completion.py frozen before execution. No automatic rerun or widening.

## GC2027 — a bit returns beyond the known interval; freeze its fate check

The dca33be2 diagnostic completed: all 510 words, times 1..8, all 65,536 right completions per word
(bit-parallel), with 1,428 literal scalar control equations. Ternary soundness passes; earliest missed
knowledge is 010 at t=2, position2. Unexpectedly, a0101010 on positions0..7 fixes position8 at t=8.
The initial right endpoint is7: exact knowledge can reappear beyond it. This is a finite all-completion
statement, not a new signal speed. Iterated left permutivity leaves the original bit a as the data bit.

Follow-up question: is that forced cell a momentary return, or a permanent advance of the rain boundary?
First independently replay all 512 causally relevant nine-bit right completions for each a by literal
truth-table updates. Then set the entire left half-line through x7 to the fixed rain, with x7=0, and
inspect the pair x7,x8 through time12 over all 8192 relevant right completions x8..20. A finite left
buffer -12..7 contains every queried dependency cone; do not impose edge updates. If the pair ever
becomes uniformly 01, it locks forever: its left neighbour is permanently1, and both next values
remain 0,1 regardless of the right exterior. Otherwise retain explicit non-locking witnesses.

Prediction: a single forced bit need not close the pair; test the distinction rather than infer closure.
Counterfactual: if a uniform 01 pair occurs, the elementary invariant gives permanent locking under
this infinite-left rain premise. No conclusion about a finite rain interval or singleton centre follows.
One fixed follow-up, source rain_information_return.py; 20 CPU/30 wall seconds, 256 MiB sampled group
RSS, 4 MiB/file, 8 MiB total; same pressure thresholds. No further depth or census automatically queued.
