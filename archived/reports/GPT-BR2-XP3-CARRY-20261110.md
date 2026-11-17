# BR-2.2/BR-2.3 carrying read and XP-3.2 exact replays

Owner-requested manual block, GC2831/GC2832, **COMPLETE** at the scopes below.
Both schedules remain **PAUSED**. The
parity/period12 research pull is parked. Cloud retains its other §9.4 leftovers
and the39 card-only doors. No module, build, posting or larger census is assigned.

## Sources and pre-run freeze

Read BR-2's complete240-line report, claims, product implementation `lp.py`,
stake implementation `hfs_core.py` and rule210 control; XP-3's report,
`cert.py`, `cert2.py`, `certlib.py`, `bb.py`; SC-5's report, independent certificate
audit, joint repair generator and exact joint certificates. Raw archive SHA256
`c231157f6daeb1433d2c8aaf2e0190f78b5c4723009fdcc32ee8842a5c11d94c`.
**Record searched:** CL766/triage §9, GC2826's B2+ read, GC2702/XP3.1 and S13;
SW02-RESULTS; current kit actual `Rule30LocalConservation`,
`Rule30ZeroBoundaryBarriers`, `Rule30ZeroBoundary` and
`Rule30PeriodTwoSideways` sources. Kit pin
`03a19bf6240b63c6d15894c5f7552f3a6091d937`; known-find's last complete refresh
2026-11-10T16:51:38.621740Z. This is a carrying review, not a novelty decision.
The kit's `cyclic_conserved_iff_shift_coboundary` already covers integer
four-step densities and therefore periods dividing4. No priority claim for
general conservation, graph potentials or the Poisson decomposition.

**Prediction:** the product encodings agree literally with physical double
steps; the memory-flip induction checks at its fixed small controls; both
original XP3 scripts reproduce rational identities within W0=14, r<=6.
`cert2.py` covers separate wall/edge terms; the three filed w=e=6 certificates
fail joint flow with8/10/14 nonzero joint labels. SC-5's exact replacements
restore that scope. **Counterfactual:** any rational identity, membership or
memory identity fails: refuse that scope and retain the counterexample, rather
than treating an LP success as certification. **Controls:** independent literal
cell updates/tuple-window counts, all filed and regenerated identities, exact
coefficient corruption rejection, a coordinate separator for the+1000 negative
LP controls, and the rule210 nonzero-stake countercontrol. Unexpected check:
test the report's Y=3 assertion at r=4, where SC-5 reports it fails.

[Replay/independent checker](../tests/probes/swarm/sw02/carry/gpt_atlas_replay.py)
and [hashed serial plan](../tests/probes/swarm/sw02/carry/gpt_atlas_plan.json).
Original script bytes are unchanged. An execution adapter supplies their relative
import/output layout and forwards HiGHS's one-thread options; it does not change
the LP or exact elimination. Separate original and regenerated certificates
are retained. The full joint repair search is not repeated: its filed rational
witnesses are independently checked instead.

**One frozen Intel stage:**110 aggregate CPU-second stop within120 ceiling,
300wall seconds,768MiB process-tree RSS, max6processes,16MiB/file and128MiB
stage disk. One compute worker/nice10; BLAS/OpenMP/HiGHS one thread.
`run_capped.py --track-tree`,4096MiB launch/1024MiB running free-memory floors,
4096MiB swap-growth stop, thermal/pressure/monitor-failure stops active.
All sources and plan published before launch. No automatic retry or enlargement.
No computation result was claimed in this freeze.

## Carrying reconstruction

### Theorem3: exact finite LP, with trim and boundary guards

A row is read in its literal order, from its first black/wall cell to its final
black/edge cell, or reversed. For a fixed complete DFA delta, let
Phi(w)=sum h(q_i,b_i)+t(q_final). The input and image tracks start in the
specified start state. The product records their states, the last four input
letters, and the finite wall-position counter. Wall reading delays output by
two letters, then flushes four zero pads; edge reading emits on each letter
then flushes the two wall outputs. The wall override in the intermediate
physical tick is essential. Survives means the input and its double-step image
are black at depth1; this is a finite-prefix/suffix condition.

**Trim to nodes reachable from an allowed start and able to reach an allowed
end.** Each accepted path is one surviving row, and its edge and terminal
weights sum to the exact Delta=Phi(Gs)-Phi(s). Independently, its input-weight
sum plus terminal t is Phi(s). These are two weights on the same finite graph.

For Delta impose pi(v)>=pi(u)+d(u,v), pi(start)=0 and
pi(v)+d_end(v)<=-1. For the range impose rho(v)<=rho(u)+a(u,v),
rho(start)=0 and rho(v)+t_end(v)>=0. Such potentials imply the desired accepted
path inequalities by telescoping. Conversely, if all accepted paths obey them,
a positive Delta cycle or negative input-score cycle on the trim graph could
be pumped to violate an accepted inequality. Remove cycles to obtain finite
longest/shortest path values, which supply pi/rho. This proves both directions,
without a width cutoff. Rational feasibility gives rational weights, scaled
to integers; strict integer descent is at least1. A uniform integer lower
bound can first be absorbed into the final weights.

The C4 extension is only for the fixed prefix/suffix automata and their stated
two-sided additive score: guess the suffix states, enforce their deterministic
backward transitions and terminal conditions, and trim the unambiguous product.
It is not a claim about arbitrary matrix interpretations. Floating infeasibility
of the old N<=4 box remains a separate numerical observation, not an exact
infeasibility certificate or a class-wide barrier.

### Theorem4: where the invariant stake identity applies

For the power kappa, in wall-first bulk coordinates write the next output as
c=b xor g(m), where m is the last2kappa input letters. A bulk state is
x=(q,q',m), and each fair next input b gives its product transition. Every cycle
reachable after a prefix surviving the required power has Delta sum<=0:
pump it inside that same allowed boundary context. Unreachable or unfinishable
cycles supply no such conclusion.

On a bottom DFA component B, let nu_B be the mean transition score under its
fair-letter stationary chain. Its Poisson equation gives

    h(q,b)=nu_B+U_B(q)-U_B(delta(q,b))+(-1)^b mu_B(q).

The finite irreducible chain may be periodic; this equation still has a
solution, unique modulo constants. For a bottom product component C with
tracks in B,B', both projected transition laws have fair letters, since
b xor g(m) is fair conditionally on x. Its stationary mean Delta is therefore
nu_B'-nu_B<=0. **The zero-cycle and stake claims require equality of these
means.** A positive stationary flow on every edge, decomposed into cycles,
then forces every cycle score to vanish.

Subtract the two U coboundaries. The remaining edge score is

    (-1)^b [(-1)^g(m) mu_B'(q')-mu_B(q)].

It has conditional expectation zero. Since every cycle sum vanishes, it too
is a graph coboundary V(x)-V(next). Thus V is harmonic. On a finite irreducible
component the maximum principle makes V constant, forcing the bracket to
vanish at each x. This reconstructs the report's missing harmonic step.
For B=B' it is exactly mu(q)=(-1)^g(m)mu(q'), or invariance of the martingale
difference (-1)^b mu(q) under the moving-frame power. Different-mean components
and transient product components do not get this conclusion.

### Theorem5: every positive power for finite-window densities

Let the DFA state be its last ell input letters a and let m be the2kappa
letters immediately before a. Its output-state word is A_m(a), a triangular
bijection of ell-bit words. In this full product the state is equivalently the
word ma, so its graph is the full de Bruijn graph of order ell+2kappa and is
strongly connected. Conservation on all cycles gives the equal-mean case above:

    mu(a)=(-1)^g(last_2kappa(ma)) mu(A_m(a)).

Choose m=0^(2kappa), m_tilde=1 0^(2kappa-1). An isolated oldest black reaches the
first output only along the extreme speed2 path at the last of kappa updates.
All other output coordinates lie outside its cone; zero memory at the adjacent
site prevents OR masking. Therefore A_m_tilde(a) differs from A_m(a) only in
its first bit, for every a. If ell>=1, the memory in the sign has already
dropped the changed oldest input, so both signs agree. Surjectivity of A_m
forces mu to ignore the oldest state bit. The identity descends to ell-1:
the new memory is the last2kappa letters before the remaining state, and every
such memory is available. Repeat. At ell=0, g(0^(2kappa))=0 and
g(1 0^(2kappa-1))=1 force the constant stake to be zero.

Hence h is constant plus a shift coboundary. This argument works over Q (or R),
and for every kappa>=1. A laboratory-frame spatial shift does not change a
cyclic sum, so changing to this speed-one frame preserves the stated premise.
The converse telescopes. This is a finite-window result, not H_FS for arbitrary
DFAs. Rule210 satisfies the same window result yet has a nonzero DFA stake.

### Theorem6: conditional wall-read reduction

Assume a wall-read additive certificate and H_FS. Suppose some y in K reaches
a bottom DFA component B after r>=1 cells. K's free-word chart supplies a
G-periodic y' with the same first r cells: choose a periodic free word matching
the finitely many free bits needed by Theta_dep. Let its period be p.

Use an input prefix of y' long enough for both tracks to have read their first
r cells and for the wall-position counter to flush; r+4p+2cells suffice. Its
first r output cells equal those of y', since G^p y'=y'. This fixes all p
survival checks, so arbitrary further input letters followed by a final black
cell remain allowed. Both tracks stay in B, and the product reaches a bottom
product component inside B x B. Cycle pumping for that power is valid, both
track means equal nu_B, and the reconstructed stake identity applies.
H_FS kills mu on that component; its projection covers all of B, because a
nonempty closed projection in strongly connected B is B. Thus h restricted to
B is nu_B plus a DFA coboundary. Arbitrarily long finite extensions after the
good prefix force nu_B>=0 from the certificate's uniform lower bound.

Now truncate y' after r+2pn cells, append a fixed final black cell, and call
the resulting finite row s_n. It survives pn double steps by actual finite
dependence. Its first r cells and those of G^(pn)s_n agree. All later cells
on both tracks are read inside B. The width grows by exactly2pn, so

    Phi(G^(pn)s_n)-Phi(s_n)=2pn nu_B+O(1),

with the constant independent of n (only finite endpoint states vary). This
contradicts descent<=-pn. The wedge is included, read last inside B; no
unproved assertion about its contents is used.

If every bottom B is definite, its state is a fixed-length suffix function.
Pull its weights back to the finite-window product. Theorem5's stake-forgetting
argument supplies the needed zero-stake conclusion there, so that alternative
needs no general H_FS conjecture.

Finally a finite complete DFA has a word z taking every state into a bottom
component: repeatedly send one remaining nonbottom image state along a shortest
path to a bottom; already-bottom images stay there. A bound N(N-1)/2 follows
as follows. If there are n nonbottom states and k current nonbottom images,
choose an image closest to the bottoms. Its shortest path has length at most
n-k+1: its lower-distance transient states are outside the current image set.
Applying that word loses at least one nonbottom image; sum these bounds to
get n(n+1)/2<=N(N-1)/2. If z occurred anywhere in a K row,
that row would reach a bottom component, a contradiction. Its prefixes lie in
the proper regular language of paths avoiding bottom components. This is the
conditional dichotomy, not a proof of H_FS, factor completeness, or Q01.

## Replay result

**COMPUTED, independent exact replay PASS.** The stage at freeze `d963f4f4`
completed all four jobs, no stop and no job remaining. Both literal script
replays regenerated all 13 certificate files **byte-identically** to their
filed originals. HiGHS's forwarded thread options produced the expected
OptimizeWarning, retained in the logs; no algorithm or feature was changed.

|Certificate scope|Independently checked outcome|
|---|---|
|No boundary terms, r=1..6|All six exact rational convex identities pass. Supports1,1,1,1,17,33. The r=6 largest denominator is5252248224.|
|Separate boundary terms, seven triples|All seven pass exact counts, width, positive coefficients summing to1, and separate wall/edge flows.|
|Joint boundary terms at(1,3,3),(2,3,3),(3,3,3),(4,4,4)|The same filed certificates also have zero joint flow.|
|Joint boundary terms at(2,6,6),(3,6,6),(4,6,6)|The originals fail, with8,10,14 nonzero joint labels. SC-5's replacements have supports14,11,18 and zero joint flow; maximum denominators106,33,168.|

There were29 complete rational identity checks:13 filed+13 regenerated+3 joint
repairs. An independent literal Rule30 truth-table update and tuple-window
counter checked them; neither the source's packed update nor its count or
elimination functions carry this check. Exhaustive width<=14 start checking
gave189 late roots and797 rows in their forward closure, all reaching a white
check within the fixed400-tick audit cap. Every certificate pair belongs to
that closure and survives its double step. The retained root/time witnesses
also put every support at its own declared W0, not just the common14bound.

All13 +1000 negative LP controls returned numerical status2, independently
backed by an **exact** separating coordinate: the width equation forces total
coefficient1, while the raised coordinate exceeds the maximum among every
available pair in the larger width14 closure. A corrupted coefficient fails
normalization. The unexpected Y=3 check passes at r<=3 but fails at r=4;
the actual r=4 certificate is Y=0x23, GY=0xc5. The old report's Y=3-through-r4
sentence is corrected, not carried.

BR controls:2048 accepted input/image product paths agree with literal physical
Delta, over four fixed DFA skeletons and both readings. The memory-flip and
triangular-bijection identities pass1008 fixed cases (kappa1..8, ell1..6).
The fixed two-state white-run-parity DFA has a stake for rule210 at powers1..4
and none for rule30 there. These are bounded controls, not a proof of H_FS or
an automata census.

Resource receipt: **4.518872 aggregate CPU seconds** including monitor work,
5.0 wall seconds, sampled process-tree maximum79080 KiB, max3 live processes,
5586 MiB launch headroom/5513 MiB sampled running minimum, zero swap growth.
The stage disk envelope finished below128 KiB. Sampled RSS is not an unsampled
peak claim. No Lean, GPU, Wolfram, larger width or repeated LP search.

### What the finite identities imply

Write f(Y) as its width, counts of nonzero zero-padded r-windows, and the
one-hot joint boundary label. For each cleared triple the certificate gives

    sum_i lambda_i [f(GY_i)-f(Y_i)] = f(trunc(n+2))-f(trunc(n)) = v,
    lambda_i>0, sum_i lambda_i=1.

The stripe increment v is constant for all sufficiently large odd n: adding
one01period adds the same two bulk windows, keeps both end labels, and adds2
to width. If R=C+x.f drops by at least1 on every listed pair, then x.v<=-1.
Consequently R(trunc(n+2))<=R(trunc(n))-1 indefinitely, contradicting any
uniform lower bound on these surviving truncated stripes. The four smaller
boundary certificates and three joint replacements therefore cover arbitrary
beta(wall,edge), including interacting wall/edge terms. The three failed
originals alone cover only beta1(wall)+beta2(edge).

Omitting the all-zero window loses no affine-in-counts potential: there are
W+r-1 padded windows; its coefficient is absorbed into the affine width term
and constant. This does not cover nonlinear g(W), larger r, a free threshold
excluding the listed pairs, seed-only obligations, or arbitrary DFA weights.
An integer/rational strict ranking has a uniform decrement after scaling;
unscaled real strict decreases on this finite list also have a positive minimum.

### Carry dispositions and next steps

**BR-2.2 CARRIED WITH EXPLICIT GUARDS, hand/two-party:** Theorem3's trim
product/endpoint LP equivalence; Theorem4's reachable-cycle obstruction and
equal-mean bottom-component stake identity; Theorem5's all-positive-power
finite-window classification. The report's terse (c) must retain the equal-mean
guard supplied by (b). Numerical N<=4 infeasibility stays numerical; no
class-wide DFA barrier follows.

**BR-2.3 CARRIED CONDITIONALLY, hand/two-party:** Theorem6 under H_FS, or
definite bottom components. The wedge term is controlled by finite DFA
endpoints after entry, not by any prediction of its contents. H_FS and
factor completeness remain open. The rule210 countercontrol prevents upgrading
left-permutivity or finite-window rigidity into H_FS.

**XP-3.2 hand implication CARRIED** (agreeing with CL766), and its finite
premises now independently COMPUTED as above. All seven joint-boundary scopes
survive using the correct replacements. The source attribution is **SC-5**,
not SC-2. No new module, release clearance or prize inference.

Primary literature boundary checked directly:
[Kari–Taati, Theorem47](https://arxiv.org/html/1311.2319v3)
assumes strong transitivity. That assumption has not been established here;
the finite-window argument above does not invoke it. The existing kit's
four-step result and these standard general conservation methods remain prior art.

The requested two leftover tasks are complete at these scopes. Cloud CL767 is carrying the two earlier GC2830 questions and keeps
its other §9.4 leftovers; no new census or formalization assigned. The parity
pull and both schedules stay parked/paused. A future all-k module should use
the explicit memory-flip induction, with rule210 as its scope control; a general
DFA exclusion would still need H_FS or a replacement structural hypothesis.

Immutable evidence: `cited/gc2832-br2-xp3-carry-20261110.tar.gz`, 92925 bytes, SHA256
`65c06d839c6c2bd2442c03cf58f6dee904b56a3c050e5eb512b04879516232bf`, 79 files; verified TLS/raw-body upload and
byte-exact readback. Includes frozen inputs/plan, both original scripts and
filed/regenerated certificates, SC-5 repairs, independent closure witnesses,
all four run receipts and the review before this archive receipt. Two warning
logs have private worktree paths normalized; both raw and normalized digests
are retained. Data stays outside git.

My own pull: the one-tick dyadic obstruction remains parked; the assigned
carry debt takes priority, and no research continuation is launched here.
