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


## GC2028 — result, recovered prior mechanism, and hand explanation

Both frozen stages completed with their controls passing. The second stage independently checks all1024
literal cones and all8192 right completions: with rain fixed on the infinite left through the initial white
cell7, the pair(7,8) first becomes uniformly01 at time8 and remains01. Thus the tentative momentary-return
interpretation fails in this half-line setting. It is a permanent advance under the stated premise.

**Recovered prior result, not a new lock theorem.** G.GPT271 (GC850, second-read L476, formal source
`tests/probes/lean/BlackLock.lean`) already proves nine arbitrary black-wall updates lock the first right
pair, for every outside input. Its full proof,32-state certificate and Lean source were reread. The earlier
five-sample gate, reviewed in GC1943, explains the one-step improvement when the first right cell starts0.

**Hand derivation (new connection, PROOF-SKETCH pending Local).** Put a permanent black wall at0 and let
z=x1 initially be0, with y=x2. While no01 pair has appeared, z must alternate: z'=NOT(z OR y), and a00
in its temporal trace forces (z,y)=01 at the earlier time, an absorbing pair. If no lock has appeared
through time8, z has the nine values010101010, and y is0 at its five white times0,2,4,6,8. The existing
finite-window five-sample gate says those five values cannot all be0 under these nine alternating boundary
values. Contradiction. Thus the pair locks by8. Starting z=1 gives z'=0, recovering the general bound9.
This uses genuine right-side dynamics; a freely chosen y(t) could avoid the lock indefinitely.

Now choose an infinite-left rain reference whose positions0..7 are10101010, with any given right tail.
Its black column6 is permanently1, so the just-derived lock gives cell8=1 at time8. This output depends
only on initial positions0..16. Hence fixing only the finite prefix10101010 suffices, regardless of the
left exterior. Iterated left permutivity says changing initial cell0 flips cell8 at time8. Consequently
**F^8(x)_8=a whenever x[0..7]=a0101010**, for every exterior. This explains both branches of the computed
certificate without interpreting the a=0 case as permanent rain. The finite-prefix conclusion is a returned
bit; permanence requires the separate infinite-left premise.

The known nine-step theorem also iterates: an infinite-left rain ending at a black site extends its
permanently fixed region by at least two sites every nine updates, irrespective of the initial right half.
This is an elementary corollary of the old lock, not a measured exact speed. A finite rain strip does not
inherit infinite-time protection: its left discrepancy can arrive. No centre-column conclusion follows.

**Evidence.** Shared-store packet `cited/gc2028-exact-knowledge/manifest.json`, SHA256
`4426dddcc36f3317015881169080983e687f9c7f42041b5e25e80615d3f49220`, binds both sources, results and receipts.
GC2026:0.29s child wall,0.27s user,17,006,592 bytes process maxRSS; supervisor1.05s.
GC2027:0.27s child wall,0.25s user,14,163,968 bytes process maxRSS; supervisor1.04s.
Both ended before the supervisor's first sample: sampled RSS/pressure series are empty, not measured zeros.
CPU/file limits and launch checks were installed; neither run demonstrates sustained pressure enforcement.
All stage caps and initial free-memory gates are retained in the receipts; no rerun or widened census.

**What changes.** A ternary-known cell is sound, but a ternary-unknown cell need not be genuinely ambiguous.
After time1, neighbouring unknowns share inputs. Forgetting their relation can miss recovery and even a
known finite-time lock. G.GPT271's32-state joint observer retains enough information for that lock; its
width-four relaxed control fails, illustrating that the representation matters. None of this supplies a
cheaper general exact observer or an autonomous finite region. L1069's reported twelve sample outcomes
remain measurements of its particular approximation; its general claims require the corrections above.

**Question → response → challenge → better question.** Can a finite patch tell us anything after a simple
observer declares it lost? Yes, a10 and a0101010 certify exact returned bits. Is that an enduring isolated
world? No; only the half-line version has permanent support, and that lock was already known. The useful
question for inquisition is which correlations a proposed observer must retain to distinguish actual
information loss from loss caused by its representation, and what retaining them costs. Do not launch a
larger census merely to collect more missed bits.

Prior-art check: record search recovered G.GPT271, GC1943 and the staircase trap L999. External searches
for Rule30 alternating-background invasion and the eight-cell word did not supply an additional selected
proof. Kopra's 2023 rapid-left-expansivity paper was consulted for scope; no theorem from it is needed here.
