# BR-2.2/BR-2.3 carrying read and XP-3.2 exact replays

Owner-requested manual block, GC2831. Both schedules remain **PAUSED**. The
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
`Rule30ZeroBoundaryBarriers`, `Rule30PeriodTwoSideways` sources. Kit pin
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

The prefix shared by y' and G^p y' reaches B on both product tracks, and can
be extended arbitrarily while surviving p double steps. It reaches a bottom
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
by summing the remaining nonbottom counts. If z occurred anywhere in a K row,
that row would reach a bottom component, a contradiction. Its prefixes lie in
the proper regular language of paths avoiding bottom components. This is the
conditional dichotomy, not a proof of H_FS, factor completeness, or Q01.

## Replay result

Pending the separately frozen bounded stage. Do not read the predictions above
as executed checks or a finite-certificate carry.
