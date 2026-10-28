# What remains after a visible structure — GC2034

Owner-requested exploration, 28 October2026. Take the familiar structures to their apparent ends and keep
relations between changing cells. Local is handling the newly surfaced paper; GPT takes this bounded comparison.
No prize test or parallel paper review. Hand background: rain and staircases are the same family; odd triangle
tips can hang another triangle, so disappearance of a shrinking core is not disappearance of its white lineage.

## Frozen question and diagnostic

Record searched: staircase/triangle/correlation/forbidden pair (conjunctive search unhelpful); then
hidden.*relation|forbidden.*pair|staircase.*front|white.*triangle. Read GC2026–2029 exact-strip report, L999
staircase review and GC1935 qualifications. Prior art includes the owner's newly supplied function-valued
CA paper (GC2033); its comparison is Local's work. No novelty claim for Boolean relations or symbolic evolution.

Six fixed initial words at sites0..7: even triangle10000001, odd triangle11000001, maximal six-cell rain/staircase
00101011, period-three precursor10010010, black cap01111110, irregular control01101001. Evolve through8 updates.
Follow the eight-site observation window[t,t+7], whose leftmost causal input is0. Its exact causal cone uses
only the fixed word and2t right exterior bits; the entire left exterior is arbitrary and irrelevant here.
Enumerate all2^16 right completions once as bitsets, keeping their shared assignments through time. This is a
moving observation window, not a claim that the whole structure moves at that speed.

Record fixed cells, exact support of the eight-cell word, and its size versus the Cartesian box allowed by
individual fixed cells. Strictly smaller support means a joint restriction missed by separate-cell colours.
Also record minimal forbidden patterns on2–4 selected sites and affine parity equations on nonconstant cells.
A minimal forbidden pattern is absent although each one-site deletion occurs. No probability or entropy claim
is inferred from a support count; assignment multiplicities are retained separately. Complete support means
no forbidden same-row eight-cell patterns in this window, not lost correlations everywhere or across time.

Prediction: some structured families retain joint restrictions after individual colours become unknown;
rain may recover forced colours, while the triangle cases need not have the same fate. Counterfactual:
all supports equal their independent boxes once colours disappear, or irregular control performs equally:
retain that finding and narrow the interpretation. Unexpected check: a relation invisible to every pair may
still exclude a three- or four-cell pattern. This distinguishes relational structure from merely more known bits.

Independent controls: literal Rule30 replay of every observed support's representative; every completion for
t<=3; established a10 two-step recovery; inverse one-step construction realizes every unconstrained eight-cell
word. Freeze source tests/probes/wolfram/structure_afterlife.py. One Intel process,30CPU/45wall seconds,
256MiB sampled process-group RSS,4MiB/file,12MiB stage disk; launch free+inactive1024MiB, ongoing512MiB,
swap growth128MiB. Stop on any failed assertion or cap; retain failures, no automatic widening/rerun.
After execution: derive a few short relations by hand and explain differing fates, rather than enlarge the census.

## GC2035 — results: colour certainty ends before joint restrictions

**COMPUTED, exact finite-completion results.** The frozen experiment passed once. Every right completion in the
causal cone was included, not sampled;510 exhaustive short-cone literal controls,2077 literal representative
checks,1024 inverse controls and the eight a10 controls passed. No horizon extension. The visualisation and the
minimum-arity analysis use retained supports only, not additional evolution.

| Initial family (word at0..7) | First time with no fixed cell | Allowed eight-cell words at t8 | Smallest group with a forbidden assignment at t8 |
|---|---:|---:|---:|
| Even white triangle10000001 | 6 | 137 of256 | 4 |
| Odd white triangle11000001 | 6 | 140 of256 | 4 |
| Rain/staircase00101011 | 8 | 99 of256 | 2 |
| Period-three precursor10010010 | 5 | 144 of256 | 4 |
| Black cap01111110 | 5 | 165 of256 | 5 |
| Irregular control01101001 | 6 | 135 of256 | 3 |

“No fixed cell” means across all completions of the initial word. Indeed, iterated left permutivity puts every
possible fixed cell inside[t,t+7], so there are no individually forced cells elsewhere at these times either.
It does not mean a realised diagram has no visible shapes. Every actual completion is an ordinary binary image.
Each row of the figure displays the moving window[t,t+7] in its actual horizontal position; blue marks a cell
that takes both values across completions. It is not a colour of Rule30 and does not mean independent fair noise.

**The control refutes any inference that hidden constraints belong exclusively to conspicuous initial shapes.**
One irregular control is not a population comparison, but its135 possibilities and three-cell restriction are
comparable to these structured examples. The mechanism is relational dependence, not visual attractiveness.

### 1. The triangle leaves its origin in a two-cell parity

**PROOF-SKETCH, carrying read requested; exact instances independently computed above.** Consider the one-bit
family x[0..7]=1 b 00000 1, with arbitrary exterior. b=0 is the six-white-cell case; b=1 has five white cells.
At time6,

    x_6(6) XOR x_6(7) = 1 XOR b.

Neither cell is individually fixed. In the first case they are always opposite; in the second always equal.
This is a statement about these two specified initial fragments, not every odd/even triangle in every context.

Here is a short carrying derivation. Put e=1 XOR b. Direct local updates give, at time3 and sites3 onward,

    e, e, 1, 0, r, s, u, v, ...        with r OR s = 1.

For the last relation, time1 at sites6 onward begins1,1,A,B,..., so time2 at sites6 onward begins1,0,C,D,...,
where C=NOT(A OR B). Thus r=NOT C and s=C OR D, giving r OR s=1. These preceding local statements use only
initial sites4..7=0001 and arbitrary right cells; the values of b and the left exterior do not affect them.
Define h=r XOR(s OR u), k=s XOR(u OR v), and w=NOT(h OR k). Successive rows begin:

    time4, sites4.. : NOT e, NOT e, NOT r, 1, h, k, ...
    time5, sites5.. : e AND NOT r, e, r, w, ...
    time6, sites6.. : r, e XOR r, ...

For the last line, (e AND NOT r) XOR(e OR r)=r. Also r OR w=r: if r=0 then s=1, hence h=1 and w=0;
if r=1 it is immediate. This proves both output identities. The arbitrary variable r is a cell at time3,
so the relation genuinely transports an earlier distinction through changing colours.

**Follow the relation, not just the pair.** One step later, opposite adjacent cells (r,NOT r) force the next
first pair to avoid00; equal adjacent cells (r,r) force it to avoid10. This follows directly by writing the next
pair as r XOR((e XOR r) OR q), (e XOR r) XOR(q OR z). The equality/inequality distinction has weakened.
The computed full eight-cell supports at t7 already overlap in9 words, including01000001. Consequently no
function of this eight-cell observation can always recover b then: it is compatible with both origins under
different exteriors. At t8 the overlap is58 words, and every assignment on any three selected cells is possible
in each triangle family, while some four-cell assignments remain forbidden. We have a precise local end to
perfect origin decoding, not a claim that all global memory has vanished.

### 2. Rain/staircase: an uncertain cell becomes certain again

The frozen staircase word gives110 at sites5..7 at time5. Write the next two cells A,B. The a10 identity now
applies with a=1:

    time6 at sites6..8: 0, NOT A, A OR B
    time7 at site7:    (NOT A) OR A OR B = 1.

So the cell at site7 is genuinely variable at time6 and fixed black at time7. The newly visible colour was
carried in the relation that its two changing parents cannot both be white. This is the existing a10 recovery
mechanism, now located in a tracked staircase example; no new general recovery theorem is claimed.
By time8 every individual colour is variable, but sites8,9 cannot both be black (COMPUTED); only99 of256 full
words occur. Rain and staircase are one family, not two independent discoveries. No permanent finite shield follows.

### 3. Period-three precursor: a relation supplies an extra white cell

For10010010, time1 at sites1 onward is

    1,1,1,1,1,1, NOT a, a OR b, ...

where a,b are the first two right exterior cells (unrelated to the triangle family's b). The last pair has OR1.
At time2, sites2..7 are therefore all0. In particular site7 is fixed white even though the two corresponding
parents were individually variable. That is an exact instance of hidden joint structure becoming part of a
visible triangular region. Its fixed core shrinks, and at time5 no individually forced cell remains.
At time8, every triple projection is unrestricted but some four-cell patterns are still absent (COMPUTED),
including0101 at sites8..11. The finite case supplies a continuation of constraints, not perpetual period three.

### 4. Black cap: a five-cell constraint invisible to smaller forbidden-pattern tests

For01111110 at time8, all projections onto any four of the eight sites[t,t+7] contain all16 assignments.
Yet the first five sites8..12 cannot read00010. Removing any one of its five requirements makes it attainable.
For example, the following full eight-cell words witness the five respective deletions:

| Requirement omitted (index within window) | An allowed full word matching the other four requirements |
|---|---|
| 0 | 10010100 |
| 1 | 01010000 |
| 2 | 00110000 |
| 3 | 00000000 |
| 4 | 00011000 |

Only165 of256 complete eight-cell words occur. This is a genuine higher-order support constraint: any detector
limited to forbidding assignments on four or fewer cells misses it. This does NOT establish four-wise statistical
independence; frequencies need not be equal. There is no nontrivial affine parity equation on the eight cells
in this case, as checked by the frozen probe. The five-cell exclusion is nonlinear.

## Scope and the next question

The evidence supports “fixed colours can turn into relations; relations can produce fixed colours again”.
It also distinguishes loss of a particular decoder (triangle-origin b at t7 in this window) from loss of all
restrictions (not reached by any of the six cases through t8). We did not prove eventual full support or follow
these families indefinitely. The cap's five-cell constraint is computationally certified here, not yet explained
by a compact hand propagation argument. Neither its frequency in the single-seed image nor a generic superiority
of visible motifs has been measured. No global conservation of information is inferred.

Question → response → challenge → better question: Does a shape disappear when its fixed colours do? No:
triangles leave a parity and a cap leaves a five-cell exclusion. Is the invisible remnant unique to a familiar
shape or always a simple parity? No: the irregular control also retains restrictions, and the cap's surviving
constraint is nonlinear. The warm next question is whether a small set of relational update rules can explain
how those exclusions grow in arity, without carrying an entire truth table. The present concrete target is the
cap's00010 exclusion, not a larger horizon census. The origin-decoding question already has a scoped negative
answer after t6 in this eight-site window.

## Retained evidence and actual resource use

Shared store: `cited/gc2035-structure-afterlife/manifest.json`, SHA256
`93a011b8b7798308190b0a899f0bd82f2345ec9101339ee2fc6d2ad9fc539b1b`.
This binds frozen experiment source, raw result, stdout, launcher/time receipts, retained-data analysis,
renderer and inspected PNG. Upload/stat hashes verified. Frozen experiment commit28bd2072.
One Intel child:0.49s elapsed,0.46s user/0.02s system; maximum process RSS39,337,984 bytes. Supervisor1.05s;
launch free+inactive5902MiB, swap184MiB. CPU/file limits installed and launch pressure checked; the child ended
before any periodic monitoring sample, so no sustained RSS/pressure assurance is inferred from the zero sampled
maxima. Output185950 bytes before launcher. No retry, no horizon extension, no M5 job.
