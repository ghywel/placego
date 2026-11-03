# Cloud review return: CL676–CL684 — GC2404

Owner-requested review, completed by GPT on2 November2026. All nine entries and
their carrying sources have been read. This clears the **read requests**, with
the verdicts below; it does not silently accept every conjecture or statistical
interpretation. Cloud's generic `flags/cloud/REVIEW-REQUEST` explicitly asks for
CL676§38.2, CL681's two-sided corollary, and CL682's closed-set soundness. All
three now have carrying reads. Local had already carried the first two in
L1310/L1320; they were not waiting for a first independent reader.

## Forward correction — GC2526, 3 November 2026

My CL678 retention of M5 as finite single-seed evidence below was incorrect.
The exact `parity_census.py` source in this review's manifest fixes x=+2
white and changes the centre at tick 7. Its printed values remain a
historical clamped-model failure, not measurements of the intended seed.
[Source audit and hand trace](GPT-PARITY-CENSUS-BOUNDARY-AUDIT-20261103.md).
The generic parity identity and independent closed-set carries are unchanged.
No replacement census was run.

## Verdict register

| Entry | Verdict after carrying-source read |
|---|---|
| CL676 | Episode bridge accepted; G8 consequence is the existing kit theorem. G16 bounded-depth enumeration remains COMPUTED. SAT results are per searched lag, not a complete enumeration of phase orbits. |
| CL677 | Exact diagonal parity identity accepted. Finite segment/periodic-key observations retained. The atlas is a synthesis; uniform measure, fixed segment proportions, and attribution of the prize obstruction solely to the core remain hypotheses. |
| CL678 | Finite velocity/parity measurements retained. Fixed-background exact laws use the later proofs. Stationary fair-row speed, parity fairness and independence are not established. Recruitment numbers introduced later need the correction below. |
| CL679 | Exact mask identity accepted. Band/front distribution comparison retained as finite evidence. Finite Markov closure and “one measured input” conclusion NOT SHOWN. The0.647 conditioning has an extra lag. |
| CL680 | Autonomous-prefix return supports genuine eventual32-periodicity through the tested depth, conditional on the recorded equality. Integration-parity rule accepted as known mathematics. Binomial-distance fit retained; independence, absence of constraints and a known next-doubling hazard NOT SHOWN. |
| CL681 | Two-sided trap corollary accepted; Lean source and independent finite replay read. Exact zero front speed follows with the finite wall-mismatch check below. Eight observed period8 columns and the untested region labelled chaos remain finite observations. Recruitment-bound proof is accepted with a properly initialized frontier, but two numerical families use an incomplete phase key. |
| CL682 | Corrected by CL683–684. Abstract closed-set soundness ACCEPTED for matching half-line plus mismatch-containing strip, giving bounded-error front motion and limiting speed. The old(9,57) negative result is withdrawn. Exact front recurrence is a separate offset check. |
| CL683 | Corrected closed-set phase implementation accepted at GC2402's initialization/observable scope. Finite bounded-depth episode exclusions accepted conditionally on the enumerations;960 representatives for480 are justified below. Discarded strip graph has a boundary-sign error, so its numbers cannot diagnose the intended abstraction. |
| CL684 | Provenance correction accepted: failed controls preserved and passing summaries present; corrected long-run onsets and sum14 checked in source/output. CL676 and CL681 prior carries confirmed. Scope qualifications remain explicit. |

No census, long trajectory or Lean rebuild was repeated on Intel. Existing
kernel/checker receipts retain their original host attribution. The small exact
countercontrols in `cloud_review_controls.py` all pass; their role is to audit
logic/conventions, not enlarge any experiment. The source-hash inventory records
the precise files read in [this manifest](GPT-CLOUD-REVIEWS-CL676-CL684-sources.json).

## Accepted proof steps, spelled out

### CL676: episode bridge

For fixed depth there are finitely many black-edge prefixes and finitely many
phase alignments. An infinite maximum episode therefore supplies a prefix with
permanent pair agreement. Initialize the deeper tail to E; its one-sided update
preserves it. The autonomous finite prefix is eventually periodic (indeed its
triangular update is a permutation), and a common multiple with E's period
gives a recurring whole row. Conversely an eternal row with tail E supplies
infinite pair episodes at every deeper cutoff. The non-rain hypothesis excludes
calling the rain a counterexample. This proves the stated equivalence.

The actual kit `Rule30EtherEpisode.episode_bound` quantifies over black-edge
codes, all onsets and phases. Its G8 consequence is known, not a new submission.
The exhaustive finite traces in `g16_episode.py` correctly enumerate every prefix
and report a mismatch before the horizon; this excludes permanent agreement at
those depths for any period. `phase_family_sat.py`, however, skips lags with
time period<8 and takes just one SAT model per remaining lag. “One SAT lag at128”
does not prove that lag has only one rotation orbit. Retain its verified witness,
solver-reported negatives and UNKNOWNs; do not call it a full phase catalogue.

### CL677: diagonal XOR identity

For t>=1, follow x_(s-t)(s) from s=0 to t. Each tick adds the OR of the cells at
positions s-t+1 and s-t+2 at time s. The starting cell x_(-t)(0) is white for the
single seed, so the terminal center cell is precisely their XOR. This matches
the code's +1/+2 offsets; its comment without those offsets is informal.
The t=0 seed cell is an explicit exception to the zero-initial-term formula.
Segment density/periodic-key samples do not prove asymptotic proportions or
independence of segment parities. In particular, two fair components can have
constant XOR when they are equal; fairness of pieces cannot establish fairness
or nonperiodicity of their sum. The ordered growing component need not itself
be periodic, so the prize obstruction cannot yet be assigned only to the core.

### CL680: why the64-row test actually certifies this prefix

The left-frame map at position e uses only e,e-1,e-2. Its first E cells therefore
form an autonomous finite system. The source checks that every one of those
cells agrees32 ticks apart over a full32-row block. In particular the entire
prefix row at the block's start equals the prefix row32 ticks later. Determinism
then proves repetition forever on that prefix. This is stronger than a mere
two-period observation of an individual column with an unknown future driver.
Retain the exact checkpoint/digest to replay that finite return certificate.

The white-stripe/integration result is known (Rowland2006§5): after a white
column, the next column is a running XOR; odd forcing weight gives anti-period
and a doubled period, even weight preserves a period-dividing block with its
integration constant. In the generic “white iff two parents coincide” shorthand,
the reverse implication needs a nonzero recurring common word: if both parents
are permanently zero, the child may remain either constant. The recorded events
have positive forcing weight, so this qualification does not undo their checks.
The current primary paper was read: [Rowland's author PDF](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf), §5, Proposition2.

### CL681: both sides of the zero-speed bound

`EtherTwoSided.lean` proves the inclusive matching-half-line and wall-state
invariant using `ether_rule`, `wall_facts` and the kit's finite closure. The
induction is correct. The independent `ether_trap_replay.py` checks all28 kit
alignments with causal margins and resolves Cloud's original narrow[-40,59]
search-window concern. This is the existing two-party/Lean result, not a new
Intel compilation claim.

A bounded lower position alone would not establish zero *current-front* speed.
Here the upper bound is also available: none of the109 wall states equals its
13-cell reference strip at that phase (direct complete finite table check,
zero matches). Thus at every later tick there is a mismatch in the strip,
and x_B+1<=F(t)<=x_B+13. Both bounds are constant, hence F(t)/t tends to0.
Finite entry before222 plus the recorded worst earlier position gives the
uniform left-protection result. A512-row column-period test alone does not prove
eternal period8 columns or that the remaining wake is aperiodic/chaotic.

### CL682–684: abstract soundness request is CLOSED

The corrected state keeps `(t mod q,(t-A) mod N,strip)`. On a retreat it advances
the second residue by2; on a stay by1. The inclusive left half-line is preserved,
one successor is the real one, and every successor strip retains a mismatch.
The forward-closed tail set contains every real path after its declared K steps;
all-P-path anchor weight S-P gives an exact anchor clock. The endpoint identity
F=A+d,1<=d<=W gives bounded-error front motion and limiting speed. This is the
carried theorem. The exact front clock additionally requires d(t+P)=d(t), or
the endpoint-corrected path-score check. GC2402 specifies the finite start
guards/receipts; those are implementation premises, not an unread soundness proof.

The reported513/513 and28/441 remain Cloud's COMPUTED enumerations; this review
is not an independent graph reconstruction. No assertion of all413 failures
being impossible walls. Failed controls and source corrections are preserved.
The corrected long-run source checks periodic increments and sum14 separately;
its printed True values are read, with finite onsets8,165,48,259.

For CL683's bounded-depth episode computations, `phase_episode.py` correctly
enumerates black-edge prefixes. P1024's one-step rotator collapses time into
spatial alignment. For480, a direct tiny profile check gives c²(y)=rho^270(y);
all time phases therefore reduce to even/odd representatives and a spatial
rotation. Its960 representatives cover the full480*32 alignment set. Reading
the newer column instead of the older only rotates that cyclic reference.
Consequently zero surviving prefixes through the tested horizon establishes
the finite-depth exclusions uniformly over recurring periods. It does not
exclude arbitrary greater wall depth.

## Corrections returned to Cloud

### 1. `healing_bound.py` still has the lost-phase defect

The source's cycle key is `(x mod N,t mod q)`, while E uses `(t-x) mod N`.
Replace it by `(t mod q,(t-x) mod N)`. Divisible-period controls hide the error.
The tiny exact r=s=0 control on(9,57) gives:

- old key: first declared cycle times1..58, rate9/19;
- correct key: actual state cycle times0..114, rate1/2.

Thus the old9/19 recruitment rate is not certified. The(12,68) key is affected
as well; equality in one tested example would not validate its full table.
The generic recruitment proof is still useful. Initialize the *last known*
diagonal at lab x=-1 for perturbations allowed at x>=0 (or supply equality at0).
Black at the last known diagonal masks the next input and recruits one diagonal;
otherwise the known diagonal's lab coordinate shifts left. The fixed-start
change permutes spatial alignments in a full alignment enumeration, but matters
for per-alignment statements. Fix the key and retain the cycle witnesses before
using the numerical bounds. No larger trajectory run is needed.

Source under review SHA256:
`aea97c35105ffdc282e0a09cfc154debe9a04758601621304021c2a2e8145547`.

### 2. `front_markov.py`:0.647 is shifted, and Markov closure is unproved

Let J_t be the recorded jump from t-1 to t, and A_t the current white-ahead bit.
The source records both in one row. Its conditioning uses `a1[1:]` against
`jump[:-1]`: it measures P(A_(t+1)=white | J_t=0), not the immediate
P(A_t=white | J_t=0). Use contemporaneous fields for the latter and name both
lags explicitly. The mask identity equates A_t white with J_(t+1)=0, so the
already printed one-step transition table implies immediate probabilities about
0.4912 after J_t=0 and0.7347 after J_t>0 (up to joins/endpoints). Those cannot
be described by the0.647/0.510 pair. Four inter-trial joins are also treated as
adjacent observations; keep trial IDs and exclude joins in transition counts.

Different one-step conditionals refute independence; they do not prove a finite
Markov chain. Conditional jump **means** near1,2,3 do not prove deterministic
jump tables, let alone close the future distribution. Retain the measured
distributions and the exact mask identity; downgrade “finite object with one
unknown input” and the closed-form reduction to CONJECTURE/NOT SHOWN. Concrete
route: correct lags, report complete conditional distributions and test whether
the same proposed state has distinct next outcomes because of a retained deeper
context. A proof needs state closure or a justified conditional-independence law.

Source SHA256 `9e8b19415bc294b08a1123ce0079a56e1c12701f6ab72aad053bcea2c32c7f8a`.

### 3. `strip_graph.py`: lower-boundary sign is reversed

The source correctly defines depth of diagonal k_min+i as j0-i. Therefore
diagonal k_min-1 is at depth j0+1. `Ebelow(ph,i,...)` currently uses j0-i,
where it needs j0+i. At G8,tq0,j0=1 with valid strip head(1,0), the next cell
at k_min+1 is1 from the real row rule but0 from the coded boundary. This is an
explicit local countercontrol; no graph reconstruction is needed.
Repair the reference access and run a direct transition replay before using
the graph as evidence about the intended abstraction. The4.5/6.5 values were
finite value-iteration slopes, not exported exact cycle witnesses; no separate
`strip_graph.out` is committed at the named location. Preserve them as results
of the old implementation, not a theorem that the intended graph is uninformative.

Source SHA256 `b6d5fd3131f8e63061b2bf641fe37c5e636e93c30419bfc7d76ba26a71c4e500`.

### 4. Binomial distance and growing parity do not supply stochastic laws

Two uniform2-bit words can have exactly Binomial(2,1/2) Hamming distance while
being dependent: choose uniform A and an independent mask V taking00,01,11 with
probabilities1/4,1/2,1/4; put B=A xor V. Both marginals are uniform, the distance
is exactly binomial, but B=A xor10 is impossible. Thus a Hamming histogram does
not prove independence or absence of constraints. In the period32 tail, fewer
than a million pairs yield only about0.00021 expected coincidences under the
proposed independent law; zero observed coincidences cannot validate its rare
hazard. The next event near c*2^32 is a heuristic, not a computed known rate.

Similarly, U,V,U xor V are pairwise independent fair bits with parity always0.
Growing sums of periodic terms can be constant or arbitrary; growth alone is
not a fairness theorem. The needed quantity is a bound on the actual parity
correlation/bias, or a real mixing/independence statement that implies one.
Retain the observed densities/autocorrelations/run frequencies. The printed
iid-style error bars are reference scales, not established confidence intervals
for this deterministic dependent sample. Fairness and limiting distributions
remain open. No empirical coincidence fit closes the algebraic doubling question.

## External refresh, provenance, and next step

known_find --new completed at23:25:18Z, kit
c42f6e5133f61a47e99289fd4b6e0536fd8a0453,19 open PRs;11 additions, no changes
against GPT's previous complete index. The earlier sandbox-limited refresh was
incomplete and did not advance its checkpoint. No authentication failure.
New PR97/head15d6b3d26e8c1c62ba55c16bfbe1894f5980125f and portal75bd53 are
Lean Verified; its even-germ/corridor/drought statements were screened in actual
source. They concern coupled driven half-lines, not a proof of finite front
memory or independent parity in the single seed. PR96 was already noted by Local;
the rebased84/88–91 entries do not change these review verdicts. No new package
or submission decision; no closed-PR novelty clearance claimed.

Later CL685/CL686 material arrived during publication; it is a separate queued
review and is not covered by this CL676–CL684 verdict register.

The owner request is discharged: the three carrying read requests are complete,
and all nine entries have explicit verdicts and repair routes. Cloud retains
source/experiment ownership for the returned fixes; no new job or enlarged
census is dispatched. Next GPT can review returned repairs or resume the already
recorded original-clause LRAT dependency inspection. Both schedules remain active.

My own pull: the corrected lag question is a sharper target than assuming a
finite Markov model; it asks exactly which part of the front's past selects the
incoming bit.
