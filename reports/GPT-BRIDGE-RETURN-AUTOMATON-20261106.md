# The bridge return automaton

GPT GC2705, 6 November 2026. Owner-requested continuation of
[GC2698](GPT-BLOCK4-BRIDGE-HISTORY-20261106.md). GPT owns construction and checking;
Local's submission work and both paused schedules are unchanged.

## Question and test, before execution

Let A=25 and E=33535555. Starting after a complete E in the retained X gap
DFA, retain the state after each word A^n E. Compute each state's exact unary
A orbit, including its preperiod and cycle, so every exponent n>=0 is covered.
Minimize by equality of **all future sequences of exponents**, not just equality
of the next allowed exponents. Preserve the rejecting state and distinguish
total resets from synchronizing only the histories that survive a word.

Prediction: this gives a small return graph which explains the forbidden
successions 4,4 and 4,6, and sufficiently long separations synchronize its
surviving states. Counterfactual: a larger graph or persistent long-separation
memory. Both outcomes are useful. The next question is which of its states has
a meaning in an actual shared boundary history; a finite-language quotient alone
does not settle that question.

Inputs are the existing X DFAs at widths 38,39,40,41, from Local's digest-bound
bridge archive. No new windows, seeds, SAT queries or horizons. Exact finite
quotients, distinguishing suffixes, return-cycle costs and reset tests are the
whole computation. Controls: tiny known return machines; raw-vs-quotient
commutation for every transition type; distinct classes have separating future
words; GC2698 counterwords reproduced; width39–41 return languages compared;
an independent literal-word replay checks all exponent representatives and their
first repeated cycle. A corrupted transition must fail this replay.

The generic construction and any hand consequences remain PROOF-SKETCH until
Local carries them. Computational claims are conditional on the supplied DFA
tables: their earlier subset-hash/original-graph-completeness caveat remains.
The exact language under review is E(A*E)*, not all partially parsed gap words.

Record searched: GC2698/GC2699, L1569 and the retained scripts/packets;
record_find return-automaton search finds only this existing queue. The current
kit/portal/PR refresh and relevant primary-source check are recorded below at
closeout. No claim to invent return automata or finite-state minimization.

## Resource freeze

One serial Python worker on Intel, one thread, nice10. Stage ceiling120 aggregate
CPU seconds/300 wall seconds, worker stop105, individual worker100CPU/240wall;
reserve15CPU for supervision. Tree RSS8192MiB, launch headroom4096MiB,
running floor1024MiB, swap-growth4096MiB, at most6 processes including wrappers
and monitors. At most16MiB/file and128MiB/stage. Use run_capped.py plus the
existing serial stage driver, with real aggregate worker accounting. All source,
input and plan digests are frozen before launch. A pressure, thermal, monitor or
control failure stops the stage; no dependent retry or size enlargement.

## Outcome — GC2706

**COMPUTED, exact relative to the supplied DFA tables:** X has only two
nondead predictive states at complete E boundaries. The raw boundary subsets
number6,5,5,6 at widths38,39,40,41 respectively; their quotients all have two.
Widths39–41 give the same machine. Call its states R and S, with R the state
after the initial E:

| Current state | Number n of A blocks before the next E | Next state |
|---|---|---|
| R | 4 | S |
| R | every n>=6 | R |
| S | every n>=7 | R |
| Either | all other n | reject |

Thus S records exactly that the preceding separation was4. The future word
A^4 E distinguishes R from S, so one nondead state cannot suffice. Every n>=7
is a **total reset of this predictive quotient**. Length6 is different: it
rejects S and sends R to R. It filters possible histories; it does not reset
both. At width38 the only change is that S also admits6. This locates exactly
the lost word in the earlier38-to39 comparison.

The explicit two-state rule was independently expanded into a46-state gap NFA,
with every state initial and accepting for factor words. All states belong to
one strongly connected component, so this convention introduces no orphan
finite paths. Determinization has89 nonempty subsets. Exhaustive product
comparisons with X38,39,40,41 pass at291,257,299,354 reachable pairs. Hence
**the complete factor language**, not merely words aligned with E boundaries,
is exactly this grammar, with the width38 amendment where appropriate. Pure
A tails and words beginning or ending inside E are included by that comparison.
Infinite paths with finitely many E's can still have an A-only tail.

There is no further restriction in longer exponent histories at these widths:
each n is4 or>=6, and4 forbids the following4 or6, with no other constraint.
That conclusion concerns these finite abstractions. It does not identify the
intersection over all widths with this language, prove actual-history lifting,
or show that any finite right half crosses infinitely often.

### Why the construction is exact

**Generic hand argument, PROOF-SKETCH pending Local's carry.** Complete the
input DFA with a rejecting sink. If q is the state after an E, define
f_n(q)=delta(q,A^n E). Iterate delta(-,A) until its first repeated state, retaining
every intermediate state and its E-image. This is a finite prefix followed by
a cycle and therefore describes f_n for every n, without a cutoff. Closing the
initial state delta(q0,E) under all its nondead E-images yields precisely the
reachable boundary states. Induction on the number of excursions proves that
this induced machine recognizes exactly E(A*E)* in the original DFA.

Partition refinement begins with accepting versus rejecting. A refinement
compares the entire ultimately periodic sequence of successor classes for
n>=0; its canonical shortest preperiod and primitive period uniquely encode
that sequence. The stable partition is a right congruence. Induction on future
exponent-word length gives language equivalence within each class, while the
recorded distinguishing suffixes separate distinct classes. This preserves
every complete future excursion sequence. The independent factor-language
comparison above is the additional check needed for unfinished blocks.

For this data the evidence is especially small: each raw boundary state's
entire unary orbit, its E-images and its map to R/S are exported. A separate
reader checks every step and the closing edge of each orbit directly against
the original tables, then checks the displayed formula for all exponents via
the prefix/cycle. Altering an E-image to rejection fails that checker. This
second implementation is a GPT self-check, not a second worker's carrying read,
and does not remove Local's original subset-hash caveat.

### The sharp clock, with its endpoint correction

**Conditional hand consequences, PROOF-SKETCH pending Local's carry.** One
return takes c(n)=34+7n sampled steps, twice that many physical ticks. The three
least-cost edges at39–41 have costs62 (R to S),76 (R to R),83 (S to R).
Set h(R)=0, h(S)=-21/2. Every allowed edge q to q' satisfies

    c(n) - 145/2 >= h(q') - h(q).

The R-to-S and S-to-R inequalities are equalities at n4 and7; the R-to-R
inequality has slack7/2 at n6. Larger n only increase the cost. Summing gives
cost >=145k/2 -21/2 for any k consecutive returns. Alternating4,7 follows a
cycle and attains mean145/2 sampled steps per excursion. Thus GC2698's
asymptotic bound2/145 per sampled step, or1/145 per physical tick, is sharp
**within this finite language**. The two-excursion word A^4 E A^7 E lasts145
sampled steps,290 physical ticks. This is a periodic word in the abstraction,
not a periodic physical row or a constructed finite-support orbit.

The asymptotic value is not a sharp zero-offset finite bound. Starting at R,
the exact minimum over k intervals is

- k=0:0;
- k=2m+1:145m+62;
- k=2m>=2:145m-7.

To check it, let r_k,s_k be the least costs ending at R,S. Then
r_(k+1)=min(r_k+76,s_k+83), s_(k+1)=r_k+62, with r_0=0 and s_0=infinity.
Induction gives r_(2m)=145m, r_(2m+1)=145m+76,
s_(2m)=145m-7 for m>=1, and s_(2m+1)=145m+62. In particular6,4 costs138
sampled steps, less than the145 of4,7. At38 the asymptotic minimum is69,
attained by4,6; the corresponding two-excursion word lasts276 physical ticks.

### What this changes, and the next physical question

The obstruction is now a single bit of predictive memory in the finite X
language, not an unknown hierarchy of restrictions on longer gap words at
width41. It does **not** say that the underlying row, its exterior inputs or
the compatible initial conditions have been reset. Several distinct raw
window subsets already merge into R. Their equal projected future languages
are weaker than equality of physical histories.

The warm continuation is the guarded physical composition for4 followed by7.
At the odd observation phase, define

    B_b(R) = ((R << 1) | b) XOR (R | (R >> 1)),
    F(R) = B_1(B_0(R)).

For a finite right half represented by a nonnegative integer, this is exactly
two physical ticks beginning with a white center. Let D_n(R) require that the
sampled bit F^j(R) mod2 has precisely the black times given by the partial sums
of A^n E, including time0 and the final black time. If working inside X, also
retain the condition that the intervening windows stay in the specified X
component. The next relation to construct is

    D_4(R) AND D_7(F^62(R)),     R' = F^145(R).

The **same intermediate row F^62(R)** must serve both segments. Separate
existence of their two projected words is insufficient. The next executable
step is to encode this composition with an explicit shared interface and track
which root/exterior constraints survive the predictive reset, using the
retained graph rather than a larger window. First inspect those constraints;
do not simply repeat the old all4/all6 full-cone SAT calls with more conflicts.
Nor require R'=R: equality of the entire finite row is stronger than repeated
column excursions and can fail from distant support growth alone. Resolving
this one cycle would not by itself exclude all aperiodic excursion itineraries.

### Verification, resource receipts and searches

Both frozen stages completed with all controls passing. Accounted worker CPU:
0.487059s and0.292581s; outer-supervisor CPU0.120s and0.094s, total0.993640s.
Worker wall times0.492s and0.195s. First-stage sampled peak tree RSS48.05MiB;
second stage finished before a nonzero tree sample, so no zero-RSS measurement
is claimed (worker receipt max RSS17.73MiB). Minimum measured free+inactive
headroom6,502MiB, zero swap growth, no pressure/thermal/monitor stop. No job
remains running. No Lean build, new SAT attempt, new window or seed census.

Evidence: shared-store `cited/gpt/gc2706-bridge-return-20261106.tar.gz`,29,313
bytes, SHA256 `1d7e054c719ac50abab76801213aef93c59524d7670bfb220bf6eb5bfde03243`.
Raw upload/readback is byte-verified. It contains all four original input tables,
both probe sources, exact return-orbit/class certificates, independent factor
checks, normalized resource receipts, original/raw receipt digests and the
source-search records. Data remain outside git. Source pins below are the
pre-execution originals; normalized receipt copies preserve their raw digests.

Complete index refresh21:02:12Z: kit9d837cd5e5ac447cd868c20aebf49a1b4cfa866e,
33 open PRs,8 additions. S-03's public entry is Lean Verified. New PR208's
statement transports finite ancestry under **both** equal center traces and
controlled-response equivalence of center-including right tails (possibly
after finitely many actual steps). It does not identify trace equivalence with
that physical response relation; it is a relevant distinction for the next
interface question, not a carrying read or a theorem used here. Primary source:
[PR208 at head d6be7193](https://github.com/WolframInstitute/Rule30PrizeKit/blob/d6be7193814f1b6ddd4e4379b66426537f091482/lean/Ruliology/CellularAutomata/Rule30ResponseAncestry.lean).

Record/index searches for return automaton,33535555 and game-residue find the
existing queue and one unrelated decimal certificate substring. The primary
`lhallee/rule30-open` source is still f877f5afd5609373e2df1639e943d04e3a56e83b;
its `game-residue.md` and `three-set-game.md` retain the fixed-window forced-basin
barrier and computed smaller-window residue ([barrier source](https://github.com/lhallee/rule30-open/blob/f877f5afd5609373e2df1639e943d04e3a56e83b/negative-results/period-two/game-residue.md),
[game source](https://github.com/lhallee/rule30-open/blob/f877f5afd5609373e2df1639e943d04e3a56e83b/findings/period-two/three-set-game.md)). They do not state this excursion
quotient. The exact-result web queries returned no relevant outside source;
that is not an exhaustive literature novelty certificate. Finite-state
minimization and minimum-cycle-mean reasoning are standard methods, not novelty
claims. No outward submission is proposed here.

Frozen source/input digests:

| File | SHA256 |
|---|---|
| return_automaton.py | aa3d06aa249f4efc3bbaaafc3000c62dfe0af1d570cbb0f46a8dcdc006c5cdb8 |
| intel_worker.py | 2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94 |
| stage.py | ba9696782abbee65ffcd3433e78848f1de82647a4f8033ab1e6a5c6cbdaaa09a |
| run_capped.py | 26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b |
| dfa_xx_W38_c0.txt | 465c2cfd8b303db816c439d237c760c1a28f6766fdda10e56a8df37cbcde68e4 |
| dfa_xx_W39_c0.txt | 7972a731983ef9baa397a9107283f5e34b4b6429e091bf24c08e673c7f089aaf |
| dfa_xx_W40_c0.txt | 0323f4a3bb60717f97c432c378e61cd85feacd1a9097ce667396de58d196167a |
| dfa_xx_W41_c0.txt | 0d0231db4179ab4ac79eb9409933beefe313d9c4a1473cffcbe7ee6bd0b9593c |
| gc2705-plan.json | 068cad1c98a269d85fbb5bf4eabb7c5fa223e9ed4d26f4d259d44372c84bda11 |

## Completed first stage; frozen factor-language check

The first stage completed in0.487059 accounted worker CPU seconds, all controls
passed. All four inputs give exactly two nondead return classes. At39–41 they
are R (4 goes to S, every n>=6 goes to R) and S (only n>=7, to R). A one-letter
future exponent4 distinguishes them. At38 the second threshold is6. Thus every
n>=7 is a total reset of the predictive quotient, not a claimed physical reset.
The minimum mean return cost is145/2 sampled steps at39–41, attained by4,7.

A separate small check is now frozen: replay the raw unary cycles and their
class map with an independent reader, deliberately corrupt a certificate edge,
then expand the explicit two-state rule into an ordinary gap NFA. Start/end at
every recurrent state and determinize it. Compare the entire factor language
with each input by exhaustive product BFS. Prediction: equality at every width
with its proper threshold; counterfactual is a separating partial gap word.
This tests the previously explicit partial-excursion limitation, not a new
window or retry. Second stage ceiling30 aggregate CPU/90wall, worker stop20,
individual15CPU/60wall; same memory/process/disk/pressure gates. Together with
the completed first stage this stays far below the original120CPU budget.

| Second-stage binding | SHA256 |
|---|---|
| return_factor_check.py | ff03d569c798eee8495a71acb86d83ea49b285fab1398da46a2aa61cfe14c75f |
| intel_worker.py | 2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94 |
| stage.py | ba9696782abbee65ffcd3433e78848f1de82647a4f8033ab1e6a5c6cbdaaa09a |
| run_capped.py | 26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b |
| return.json | 6e084d181ba22f95edab459ebed46f6fad8673301347ea76940180c7e6a0a8dd |
| dfa_xx_W38_c0.txt | 465c2cfd8b303db816c439d237c760c1a28f6766fdda10e56a8df37cbcde68e4 |
| dfa_xx_W39_c0.txt | 7972a731983ef9baa397a9107283f5e34b4b6429e091bf24c08e673c7f089aaf |
| dfa_xx_W40_c0.txt | 0323f4a3bb60717f97c432c378e61cd85feacd1a9097ce667396de58d196167a |
| dfa_xx_W41_c0.txt | 0d0231db4179ab4ac79eb9409933beefe313d9c4a1473cffcbe7ee6bd0b9593c |
| gc2706-plan.json | dfee18e03ae7d1de8a3dab964e6774d9e7d52266cf991f51eb6995eaf7193696 |
