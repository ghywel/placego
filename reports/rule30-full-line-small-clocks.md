# Full-line clocks, transient connections, and a hand period-four reduction

GC2231, GPT,30 October2026. **PROOF-SKETCH**, solo hand argument, independently
unread. The period-four conclusion already follows from the retained complete
period-four profile core; this is an explanatory reproof, not a new census or
novelty claim. No computation or compiler was run.

The pull was the full-bi-infinite scope of PR58's dyadic-background conjecture.
A ring census sees closed spatial paths. Could a higher temporal clock live
only on a connection between lower-clock recurrent backgrounds? The cheap
objection is that finite graphs can have transient connections; one must keep
their vertices, not just classify their cycles. The bounded hand discriminator
here settles clock four, without pretending to settle clocks16and higher.

## Coordinates and the known evidence

Use depth coordinates on the full spatial line of integers:

    Phi(x)_j = x_j XOR (x_(j-1) OR x_(j-2)).
    D_j(t) = Phi^t(x)_j; Delta D_j = D_(j-1) OR D_(j-2).

This is the reflection of G in [G258](../proofs/G258-four-forbidden-words-in-every-forward-right-moving.md).
It is the moving-right Rule30 frame, not the fixed physical centre column.
All profiles below are actual profiles of this same row, not independently
chosen temporal controls. Phi^q(x)=x makes every profile q-periodic from time0.

For a fixed q, the unrestricted pair graph has vertices(a,b) of q-bit temporal
profiles and edges(a,b)->(b,c) when Delta c=a OR b. A full-line q-return is
exactly a bi-infinite path, by the local recurrence and forward uniqueness.
Ring returns correspond to closed paths, as the already carried Lemma R in
[periodic edges section3](rule30-periodic-edges.md#3-cycles-are-ring-orbits-proved-by-hand-the-ring-census-computed)
proves. Rooted profile graphs impose an additional eventually-white past and
are a third boundary problem.

The complete retained PR58 `profile_core_probe.py` and
`profile-core-result.json` were read: the unrestricted bi-infinite cores have
6,6,46 vertices at q2,4,8. Their algorithm repeatedly removes vertices with
zero incoming or outgoing degree. The period-eight carrier-to-rain path is
also explicitly proved in [PR48's carried source](rule30-edge-clock-drop-review.md).
Its clock eight comes from the carrier itself; it does not exhibit a
higher-clock transient between lower-clock tails. The distinct left-only
core has8,12,132 vertices: it does not require an infinite continuation on the
newer side. These are retained author computations, not a GPT rerun.

The archive's ring tests at widths17–24 with clocks8,16,32 and its two timed-out
SAT targets do not settle the full-line conjecture. The complete archive and
source identities are retained in the [GC2229 packet](rule30-group-cocycle-review.md#gc2229-complete-archive-and-replay-review).
No UNKNOWN result is treated as UNSAT.

## A hand proof that Fix(Phi^4) equals Fix(Phi^2)

Suppose Phi^4(x)=x. G258 already forbids00100and11011 in every forward profile,
without a root or periodicity assumption. Consequently a four-periodic profile
cannot have one or three black bits per period: its cyclic repetition would
contain one of those two words. If its least period is four, it must therefore
be a rotation of0011. The only other possibilities are constants or alternating
profiles, all of period dividing two.

Assume for a contradiction that C=D_j has least period four. Shift the time
origin forward to write C=0011 repeated, so F=Delta C=0101 repeated. Put
A=D_(j-2), B=D_(j-1). Then A OR B=F. Both A and B are supported on the two
black positions of F. A one-position support was just excluded by G258, so
each is either0orF.

If B=0, the identity Delta B=A OR D_(j-3) forces A=0, contradicting
A OR B=F. If A=0, Delta A=D_(j-3) OR D_(j-4) forces D_(j-3)=0; then
Delta B=A OR D_(j-3)=0. Thus B is constant, whereas B=F would be required.
The only remaining case is A=B=F.

Now use the next newer profile E=D_(j+1). It satisfies

    Delta E = B OR C = 0101 OR 0011 = 0111.

The XOR of the four bits on the right is1. The XOR of four consecutive
differences of a four-periodic E telescopes to0. This contradiction eliminates
every primitive four-profile. Therefore each D_j has period dividing two,
and Phi^2(x)=x. The converse follows immediately by iteration.

This is a full-line statement with no finite-support or spatial-periodicity
hypothesis. In particular a transient bridge cannot create clock four from
clock-one/two backgrounds. It is **not** a period-four centre-column exclusion.

### Why the newer neighbour is essential

G258 itself retains the legitimate older-side profile chain

    ...,1010,0101,1010,0101,0101,0011

in increasing depth order, with the displayed0011 as its endpoint and the
earlier alternating part continuing indefinitely. Every recurrence up to the
endpoint holds. The next forcing has odd parity and its integral is
anti-periodic after four ticks, hence has least period eight. Thus a finite
prefix can reach clock four; an everywhere four-periodic extension cannot.
This is the precise distinction between the left-only and full-line cores.

The known period-eight0001 ring carrier is a separate guard against extending
the conclusion to Fix(Phi^8)=Fix(Phi^2). No such extension is claimed.

## The already-known two-step classification

The elementary identity in GC732, in these reflected coordinates, is

    Phi^2(x)_j XOR x_j
      = [x_(j-1)=x_(j-2)] AND (x_(j-3) OR x_(j-4)).

Thus an equal adjacent pair forces the two preceding older cells white.
A00pair propagates white forever in the older direction. A11pair first
forces an older00pair and hence the same white half-line. If a nonwhite row
has no first black cell, neither equal pair can occur, so the row alternates
everywhere. If its first black cell is k, all cells below k are white, x_k=1,
x_(k+1) is either0or1, and the row alternates from k+1 onward. A later00pair
would erase the earlier black cell; a later11pair would force such a00pair.
Conversely each of these rows satisfies the displayed identity.

Therefore the full-line two-return rows are all white, the two alternating
rows, and these white-to-alternating interfaces. This recovers GC732's known
interface, not spatial periodicity of every full-line return. Together with
the preceding argument it classifies the full-line four-return rows too.

## What a larger-clock result would still need

Standard finite-graph pumping applies on both sides of any chosen vertex of
a bi-infinite path: repeat a cycle somewhere in its infinite past, retain the
finite segment through the vertex, and repeat a cycle somewhere in its future.
This yields a path with spatially periodic tails. For q=2^k, an actual point
of least temporal period q has at least one profile of least period q;
otherwise all profiles have period dividing q/2. Keeping such a profile in
the finite segment preserves the full point's least period q after pumping.

This is the two-sided version of the standard argument already used in GC759.
It does not join the two tail cycles to each other. Consequently a ring-only
classification at a proposed q would still need to exclude primitive-q
profiles on transient connections. The current hand result does that at q4.
No primitive16or32 bridge was constructed or excluded in this block.

Record searched: GC732/GC759/G258 and their carrying source; L1066's complete
q8 ring components; GC2014's rooted q32 graph; PR48; PR55's actual WordStep
and realization interfaces; PR58's exact head70ca1830/archive87ba7661;
kit932cf8dd actual PeriodicPoints Recurs and velocity hypotheses, plus current
03:06:23Z portal/open-PR index and exact finite-return source headings. The
PeriodicPoints spatial-periodicity theorem excludes the light-speed boundary
used here and supplies no shortcut. The initial candidate ban was exactly
G258, found before any new computation. Urías–Salazar-Anaya–Ugalde–Enciso1996,
[Traveling patterns in cellular automata](https://pubmed.ncbi.nlm.nih.gov/12780279/),
abstract, already treats finite automata and travelling patterns; the full
paper was not read and no theorem is imported from it. No literature priority
or additional-submission disposition follows from these searches.

**Next step:** read PR33's exact finite eight-return theorem and its certificate
induction. Its finite newest-first state, with three cells dropped before the
two-return test, is different from the full-line problem above. Determine the
carrying invariant and boundary role before attempting any transfer. The old
GC1996 hand-D alternative is withdrawn: L1038/GC1994 already recorded repeated
failed hand attempts, followed by a completed computer-assisted proof. Reopen
that hand route only with a new compression identity, not another identical
two-tick expansion. No larger graph, seed census or compiler job is queued.

## GC2233: an even two-run profile forces the next period to double

30 October2026, solo **PROOF-SKETCH**, independent carrying read pending.
This is a bounded structural consequence of the already carried GC798
projection and G258 word bans. It arose while seeking a hand explanation of
the retained q8 core. No temporal-word enumeration or new computation ran.

**Claim.** In any actual forward Phi spacetime, suppose a profile C=D_j is
q-periodic from time0, with q even and at least4, and has exactly one white
run and one black run in a q-cycle. Then D_(j+1) has least period2q. Moreover
D_(j-1)=D_(j-2)=Delta C at every nonnegative time. For q>4 these three older
profiles have equal least period q, so the two non-doublings are necessarily
followed by a doubling. The claim supplies a conditional profile-shape law;
it supplies no occurrence or white-root realization of that shape.

Write C as a cyclic rotation of0^a1^b with a+b=q and a,b positive. G258
excludes a1 or b1, since the cyclic word would contain11011or00100.
It also excludes a,b both at least3 by000111. Hence the two lengths are
2and q-2, in either order. Both are even and at least2.
Exactly two transitions also imply that C's least period is q: a proper
repetition would repeat the transitions.

Set T=Delta C, B=D_(j-1), A=D_(j-2), D=D_(j-3), H=D_(j-4). The actual
equations are

    T=B OR A,    Delta B=A OR D,    Delta A=D OR H.

T has exactly two isolated black ticks per q-cycle. The known GC798
projection forces B=T: if T(r)=1 but B(r)=0, then A(r)=1 and the second
equation forces B(r+1)=1, contrary to B(r+1)<=T(r+1)=0. Next A=T as well.
If T(r)=1 but A(r)=0, then B(r)=1,B(r+1)=0, so D(r)=1. But A(r+1)=0,
making Delta A(r)=0 contrary to the third equation. Outside T's support,
both A and B are zero by the first equation. These forward arguments also
handle r0; no negative-time value or unproved ancestor periodicity is used.

For the next newer profile E=D_(j+1),

    Delta E=C OR B=C OR Delta C.

Over one cycle this forcing extends the black run by one tick and shortens
the white run by one: its run lengths are b+1and a-1. Its black weight b+1
is odd. Telescoping therefore gives E(t+q)=NOT E(t) for every t>=0 and
E(t+2q)=E(t). The forcing has exactly two transitions in its q-cycle, hence
least period q: a proper repetition would repeat those transitions too.
Any period of E is a period of its difference, so its least period is2q.

For q>4, T's two gaps have unequal lengths2and q-2; its least period is q.
Thus the consecutive least periods are q,q,q,2q, yielding the flag pattern
001. At q4, T instead has period2 and the consecutive periods are2,2,4,8;
this exception is explicit. The ordinary period-two rain profile is outside
the q>=4 hypothesis. A fixed physical centre is a different observation.

**What this settles.** No full-line q-return with even q>=4 can contain a
profile with exactly two runs in that q-cycle: its next profile would have
least period2q. In particular the proposed two-run primitive-eight classes
cannot belong to the full q8 core, although a finite older-side prefix need
not have a q-periodic newer extension. This generalizes GC2231's final
parity step while retaining its boundary distinction.

**What remains.** Many primitive-eight words have four or six runs, and
the carried PR48 carrier-to-rain connection already survives the word bans.
No all-profile classifier, frequency bound, arbitrary00 closure or
higher-clock bridge exclusion follows. At q>4, white-root occurrence of the
two-run shape has not been proved. Do not start a larger search to make that
conditional class look nonempty.

Record searched: GC798's complete projection, GC799–802/G258, GC821/G261's
different proper-odd-period/joint-period hypothesis, G267/G268 and the exact
PR48 carrier. Fresh known_find completed04:17:45Z, kit932cf8dd unchanged,
23openPRs, zero added/changed/removed records. Actual kit temporal/diagonal
and finite-clock scopes were checked; finite-clock detection needs a full
return and does not prove the shape's occurrence. A bounded literature
search returned centre-column block exclusions and standard diagonal
period statements, which have different hypotheses; no priority inference
is made from the lack of an exact hit. The useful new deduction is kept as
a solo sketch, with the older projection and word restrictions credited.

The nearest delivered name `Rule30TemporalProfiles.heavy_source_two_runs`
was also read with its `Child` and `profileSource` definitions. It concerns
recovering a parent under a prescribed pulse in the left-diagonal recurrence
and concludes at least two black runs from source weight greater than three.
Its hypotheses and frame do not state the right-moving doubling law here.

The general q8 case list is parked unless another structural identity
distinguishes its remaining classes; no unstructured hand census is queued.
Next change representation: carry the linked RootOrientedHeight proof of
the signed two-level condition for a safe newest trace, checking its initial
orientation and finite-ancestry hypothesis separately. That is an available
source read, not an assumption that safety implies eight-return.


## GC2235: one frozen core-only ancestor check

The new [core-only draft](../lean/Rule30IsolatedTransitionCore.lean) formalizes
only the local step in GC2233: three actual temporal recurrences and isolated
black transitions of C imply both older profiles equal Delta C, at every
nonnegative time. It does not formalize the two-run period count, G258,
period minimality, root occurrence, or a prize claim. Status at freeze:
UNCOMPILED; the hand theorem remains solo PROOF-SKETCH.

This is a changed dependency plan, not a retry of the GC2228 Window failure.
It imports only Init, with no kit/Mathlib build or downloads. The local
six-Boolean implication is proved by ordinary kernel decide and lifted to
arbitrary histories. Three fixed controls omit isolation or either older
recurrence and exhibit the failed conclusion. No initial time is excluded.

**Prediction:** one development check on installed Lean4.33.1 compiles all
eight theorem heads with empty axiom lists; a separate false proposition is
rejected; a literal eight-entry Rule30 table agrees on all16 local inputs.
**Counterfactual:** a positive diagnostic, nonempty axioms, wrong rejection,
source/toolchain mismatch or oracle discrepancy stops the stage. Preserve
failure; no automatic repair/retry or cap increase. **Unexpected check:**
all three omitted-hypothesis countercontrols are kernel-checked, so none of
the actual equations is silently dropped. This validates a carrying Boolean
step, not its integration into the current official4.35 checker.

Record searched: GC2233's full kit932cf8dd/portal23PR/primary-source scope
comparison and complete GC798 projection, plus fresh record_find
`isolated.*transition|GC798` (44record hits; no exact indexed external hit).
The known machinery is credited. This is formal preparation of that stated
step, not a newly claimed result or a negative-search novelty inference.

Freeze source SHA256
`92f49a07fd732c46ccfde7565bb7578d4d46777cef8ea8fa39b9a57d44d169f2`,
[driver](../tests/probes/wolfram/check_isolated_transition_core_dev.py) SHA256
`b84a38e7b084521b0a606576df8529301aff3d035649c0241245e2a51c21106a`,
and unchanged run_capped SHA256
`c8c58b49e032fc4c20b61675adc4194646713e692a51815996791ac8943ffc56`.
Exactly three possible sequential compiler calls: version, positive source
with axiom/type printout, and false negative control. Each gets a verified
20CPU-second hard limit; driver gets4CPU seconds soft, with no signal handler.
Their assigned computation budgets sum to64seconds, below120aggregateCPU.
Per-process limits alone are not called aggregate enforcement: the fixed
call count and single-thread non-spawning compiler plan supply this bound;
outer supervisor CPU is measured separately. No lake or descendant jobs.

Outer caps:120CPU/300wall/768MiB owned RSS, one job/one Lean thread, nice10,
tree tracking/max3processes,16MiB/file128MiB/stage, launch4096MiB and running
3072MiB free+inactive, swap growth64MiB. Actual preflight:6541MiB headroom,
193.25MiB swap, load2.45. Sandbox denied the first swap read; unrestricted
read succeeded before any job launch. Thermal sensor unavailable; no normal
temperature reading is inferred. Keep per-call CPU/limit receipts, raw
compiler output, oracle, outer pressure/cleanup receipt and source hashes
outside git. This stage is permitted once after its freeze is pushed.


## GC2236: the core check stopped on an elaboration error

Freeze93e48bb1/source92f49a07/driverb84a38e7 ran once at04:43:49Z. Outcome
CHILD_FAILED rc1. The version check passed, but the positive source failed at
line45: rewriting `b t || a t` did not reduce the applied lambda in the
Isolated hypothesis. Seven helper/control heads report no axioms; the final
`isolated_transition_forces_ancestors` head reports sorryAx because elaboration
failed. It is not a passing theorem/module. The driver stopped as frozen;
negative control and literal oracle were not reached. No repair or rerun.

The diagnosed candidate repair is to expose both Boolean expressions with
`change` before rewriting. It is **not applied or tested**. A future repair
would need a new source, separate justified freeze and explicit decision;
it is not queued automatically. The Boolean helper itself compiled, but the
period theorem and official4.35 integration remain unvalidated.

Actual Intel launch headroom6508MiB/swap193.25MiB, minimum sampled headroom
6264MiB, three monitor samples, zero observed swap growth. Peak sampled
owned RSS262800KiB, at most3processes; outer wall2.18seconds, supervisor0.119CPU.
Two compiler calls used0.711504CPU in total; outer time reports0.40user+0.37system,
1.73wall and269176832bytes maximum RSS. These are distinct measurement scopes.
Per-call20CPU hard limits and16MiB file limits are retained. Normal final
owned/group check completed; no cleanup signals or remaining job. Data volume
was6386bytes at the runner's final inventory, before evidence packaging.

Immutable14-payload failure packet plus manifest:
`cited/gc2236-isolated-core-failure/manifest.json`, SHA256
`32abff7bd4b8750a9275ad536915746915ad8504f3ce4b334c39cd3a60028371`.
Includes exact frozen source, print-augmented compilation input, driver,
runner, preflight, version/compiler digest, call/limit/error outputs and
actual launcher/time receipts. All15raw uploads verified. Do not interpret
this light resource use as a reason to relax the failed Window stage's cap.
