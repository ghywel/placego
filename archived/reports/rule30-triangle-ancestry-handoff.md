# Triangle ancestry: conversation and hand derivations for Local

GPT, 26 October 2026, GC1932. Owner-requested manual handoff.

**Status:** elementary hand derivations from the standard Rule 30 table; the new exposition and backward-pair tables await Local's independent read. Known ingredients and rediscoveries are not novelty claims. No simulation, census, training, solver, GPU job, portal submission or schedule restart was performed for this discussion. This records the conversation, not a newly approved experiment.

## 1. The owner's questions, preserved in ordinary language

- Why are solid downward white triangles so prominent? Are they pockets of order in the apparently chaotic region? Why do different snapshots retain the same recognisable texture?
- The owner noticed a black cap above each newly born white triangle: it extends one cell beyond the white run on the left, but ends above its rightmost cell or one cell earlier.
- Above the cap, the owner saw repeating 001 patterns. Is that universal, allowing phase and edge differences?
- Trace back another row: does the ancestry remain orderly, acquire a longer rhythm, or immediately lose coherence? How much of this can be answered by hand?
- The cap suggests a spike produced when preceding patterns align. Treat resonance as an analogy for coordinated output, not evidence of physical oscillation, energy accumulation or linear superposition.
- Tracing backwards encounters earlier triangles. How do their positions, sizes, spacing and phases relate to a later triangle? Can their visible shapes suffice, or do the intervening cells and boundaries carry indispensable information?
- Related graph question: how many histories can join a common future? Specify complete whole-line states, controlled-boundary states or observed windows before drawing the graph. Finite whole-line differences cannot vanish; their rightmost discrepancy moves right at each step. Boundary-controlled mergers and apparent window mergers are distinct.
- More cases can help discover families, mechanisms and counterexamples. Distance between pictures need not be distance between future behaviours. A learned grouping would be a hypothesis generator, not a proof or a demonstrated predictive representation.

## 2. Convention and the tip correction

Space runs left to right; time runs down. White=0, black=1. Standard whole-line local update:

    f(L,C,R) = L XOR (C OR R).

The outputs 0 have neighbourhoods 000,101,110,111; outputs 1 have 001,010,011,100.

A maximal zero run of length n>=2, bounded by ones, loses one cell at each end on the next step; its interior stays zero. This is the existing RULE30-PRIZE.md section 8.18 argument.

**Correction to GPT's conversational shorthand:** do not extend that erosion rule to n=1. The isolated zero has neighbourhood 101 and stays zero for one more step. Its surroundings may then extend or otherwise reorganise the zero run. Thus an odd-width shrinking core ending in one cell does not imply disappearance on the following step. Even width ends with a pair, whose two sites become ones. This hand check corrects the earlier phrase 'shrinks until it disappears'; it does not audit or amend the older triangle-counting software or its convention for assigning tips/births.

The same caution matters when defining triangle objects: a geometrical shrinking core, a maximal zero run at a time, and a connected white component through time are not interchangeable.

## 3. The black cap and its repeating parent

For the aligned output 100000001, the two non-inherited nine-cell parent windows are:

    111111110       111111101
    100000001       100000001

Both need an outside zero on the left; the first additionally needs an outside zero on the right, while the second permits either right outside bit. The owner's sketch with nine upper ones cannot produce the displayed final output one: its last cell has upper left=centre=1 and hence outputs zero for either right neighbour.

There is also the inherited case: nine upper zeros with outside ones. That is a wider existing white patch shrinking, not a new black-cap birth.

To produce consecutive output ones, overlap the allowed triples. In left-to-right pair notation the continuing cycle is:

    00 -> 01 -> 10 -> 00

corresponding to 001,010,100. The only other allowed edge is 01 -> 11 (triple011); it must terminate the output run because no following triple beginning11 outputs one. Consequently the parent of a long black run repeats 001 up to its phase, with a possible terminal departure at the right edge. This does not assert that every repeated001 patch has an independently specified full boundary or belongs to the single-seed orbit.

## 4. Backward reconstruction: carrying tables

Suppose the target output at position i is b and the known upper pair is (x_i,x_(i+1))=(u,v). The preceding upper bit is x_(i-1)=b XOR(u OR v). Define the right-to-left pair transition:

    T_b(u,v) = (b XOR(u OR v), u).

| Pair | T_0 | T_1 |
|---|---|---|
| 00 | 00 | 10 |
| 01 | 10 | 00 |
| 10 | 11 | 01 |
| 11 | 11 | 01 |

For a target block001 read right to left, apply T_1 then T_0 then T_0:

| Initial pair on right | Pair three positions left |
|---|---|
| 00 | 11 |
| 01 | 00 |
| 10 | 11 |
| 11 | 11 |

All four reach11 after at most two blocks. Further reconstructed blocks are identical. With output001 repeating at positions0,1,2,..., the aligned parent interior reads101 repeating. The rightmost two unknown parent cells create four candidates, but their effect is confined to a bounded right-edge part at this one backward step. Discarding the first two reconstructed blocks is sufficient before claiming the repeating continuation. This is not a uniform edge bound for arbitrarily many backward steps.

For target101 repeated, apply T_1,T_0,T_1:

    00 -> 01; 01 -> 10; 10 -> 01; 11 -> 01.

The persistent pair cycle is01 <->10. Thus, after the possible entry block, the reconstructed interior has a six-cell rhythm. Aligned alternatives include101000 repeating and its three-cell shift000101 repeating. One must not silently choose the actual phase without boundary information.

For target101000 repeated, the block map applies T_0,T_0,T_0,T_1,T_0,T_1 and sends all four pairs to01. Its repeating parent interior is101110. Shifted targets have correspondingly shifted ancestors.

These tables distinguish a forced periodic interior from merely constructing a convenient periodic preimage. Exact finite interval endpoints, phase choices and accumulated uncertain margins for an arbitrary triangle have NOT been packaged into a general multi-step theorem here.

## 5. An exact interior chain and the smaller white patches

The following are periodic templates, with boundaries omitted. Each complete periodic row evolves to the next. For finite patches, use only cells whose necessary parents are present and treat the edges separately.

    101110 101110 101110 ...
    101000 101000 101000 ...
    101101 101101 101101 ...
    001001 001001 001001 ...
    111111 111111 111111 ...
    000000 000000 000000 ...

Direct hand check of the first three transitions, listing the successive parent neighbourhoods in a six-cell period:

- 101110: 010,101,011,111,110,101 -> 101000.
- 101000: 010,101,010,100,000,001 -> 101101.
- 101101: 110,101,011,110,101,011 -> 001001.
- Repeating001 uses100,001,010 and gives all ones; 111 gives zero.

In the second row, white triples shrink to single white cells in the third. Those single cells remain white and acquire a white neighbour on the left in the fourth, forming pairs. Those pairs then give way to the black band, followed by the white band. This exact example supplies a relationship between earlier small white patches and the later large patch; it is not evidence that arbitrary triangles are interacting particles or that their size alone predicts their descendants.

In a region already forced to be001-periodic, zero runs have length at most2; in101-periodic interior, at most1; in101000-periodic interior, at most3. A claimed larger white patch crossing those specified rows of the forced interior would contradict those templates. Patches outside the forced interval, near its uncertain edge, or further back are not excluded.

## 6. What remains open for Local

1. Independently check the pair tables, aligned chain and singleton correction; identify which statements are already covered by older results. No new computation is needed to read these carrying steps.
2. Choose an exact triangle/birth convention that handles odd tips and inherited runs. Do not count the same connected white structure as a new independent object without stating the convention.
3. For a finite triangle of specified width and position, how much of each ancestral row is forced, and how much depends on the right-edge pair/phase? Does a useful forced strip persist as the repeating unit grows?
4. Can positions and phases of earlier small patches plus a modest boundary description predict the cap? Or can two histories share that visible patch description while producing different caps? A hand pair would answer a proposed compression before a census.
5. Overlapping ancestry regions share consistency conditions. Distinguish shared causes from a demonstrated influence of one triangle on another, and geometric ancestry from a globally realizable single-seed history.

The current pull is the relationship between forced repeating interiors, uncertain margins and earlier white patches. No experiment, general hierarchy closure, bound on all backward depths, prize bridge or portal contribution is claimed.

## 7. Method agreed with the owner before this discussion

The certificate episode requires separating an avoidable hand-answerable mistake from a legitimate failed hypothesis. H3 was refuted before execution because its compulsory reads already visited every starting cell. H1's strict median advantage failed by a tie at W20, not a total absence of advantage. H2's finite median-ratio prediction failed; no asymptotic impossibility followed. Offline minimum certificates are not adaptive discovery costs. The later shuffle discrepancy and exact merger do not retroactively turn those failed predictions into successes.

Before a future experiment: translate the pull and disclose any narrowing; attempt a small hand answer and search the record; attack both the preferred conclusion and premature closure; state 'the hand work establishes X, leaves Y unresolved, and this test distinguishes A from B'; retain the original question and its actual outcome. Several analogies for the same mathematical object are communication aids, not several independent leads. Evidence gathering is useful when it discriminates mechanisms, finds counterexamples or tests whether a description transfers, not simply because a larger count is available.

## 8. Sources and limits of this handoff

Read the Rule30 update page at https://mathworld.wolfram.com/Rule30.html; the relevant older record at RULE30-PRIZE.md sections8.18 and8.82 (the latter already traces black-run births to period-three patterns); targeted record searches for triangle, black runs,001001,101000,101110 and period-three ancestry. Rowland's publisher abstract, https://www.complex-systems.com/abstracts/v16_i03_a04/, was consulted for known local nested structure; this was not a full-paper audit. No claim that the ancestry derivations are new to the literature.

L997 was read on the final fetch. Its separate funnel-count identity question is received, not independently resolved by this handoff; nor is its new script independently reviewed here. Preserve its analysis for a separate targeted comparison if the owner chooses it. GPT's schedules remain deleted, and this document launches nothing.
