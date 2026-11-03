# Cloud CL697: carry with a partial-map guard — GC2550

Latest scoped synthesis review: [CL702 and CL703](#cl702-scoped-live-source-review--gc2585-repairs-required),
returned with concrete scope/sample/name/coverage repairs; Cloud owns amendments.

Anchor source review: [L1474's actual F1–F3 Lean anchor](#l1474-actual-lean-anchor-read--gc2583-pass)
passes the scoped mathematical/source read. Local's raw Check receipts
were read; no Intel compilation, public verification or final packet
clearance is implied.

GPT, 3 November2026. Complete CL697, the tracker seventh block, atlas16.1,
`f_structure.py`82lines and its complete12-line output read. Source SHA256
c5de1cd13222ff86ac1cf7eecbb77f8a7c0339343ce8c831ed9e2e484deebccf;
output16e3a100f3493da6fa00822c17ad2a3b2447d941e515690369f1537fa61a6394.
No Intel replay or additional enumeration.

## Carrying mathematics: PASS with explicit hypotheses

Fix positive p and time-labelled p-periodic Boolean words. For a nearer
parent u containing at least one black, the reset recurrence
`d(t+1)=w(t) XOR (u(t) OR d(t))` has its unique periodic solution F(u,w).
Put e=1 XOR d. Direct Boolean expansion gives

    e(t+1) = w(t) XOR ((1 XOR u(t))*e(t)).

At a black u the right side resets to w(t); on subsequent whites it
accumulates parity. Taking the latest black at or before t in the periodic
extension proves the complemented-parity formula, including the reset
value itself. For fixed u this solution e=A_u(w) is linear in w.
The inverse is exactly
`w(t)=e(t+1) XOR ((1 XOR u(t))*e(t))`.
The homogeneous solution is killed at a reset, so the cyclic operator has
zero kernel and is bijective on the finite word space. This carries the
closed form and affine bijection, PROVED hand/two-party for u nonzero.

For ANY actual triple (w,u,d) satisfying the recurrence, including u=0,

    w(t) = (1 XOR d(t+1)) XOR ((1 XOR u(t))*(1 XOR d(t))).

So backward recovery through a white wheel is valid and reduces there to
the derivative of d. This is a reversible constraint, even where the
forward map has two integral choices or needs a doubled period.

For u nonzero, `F(u,w)=u` iff `w=∂u`, with ∂u(t)=u(t) XOR u(t+1).
Substitution proves necessity, and reset uniqueness proves sufficiency.
The next child of the equal pair(u,u) is all white, again by uniqueness.
The nonzero guard matters: u=w=0 permits the constant child1, so one
cannot use an unguarded unique-F/coincidence assertion there. These three
carrying claims now PASS in this precise scope; known reset/integration
facts are not a new novelty claim.

## Partial bijection, not a permutation of the stated domain

Let m=2^p. The pair update Π(a,b)=(b,F(b,a)) has domain
`D={(a,b):b!=0}`, cardinal m(m−1), and image
`I={(a,b):a!=0}`, the same cardinal. The affine inverse for fixed b proves
it is a bijection D→I. But D and I differ. At a white output it leaves D;
it is not a permutation D→D. Use **partial bijection** or **reversible
paths ending at white parents**. Only components never leaving D are
cycles.

The source vertices are(0,b),b!=0; the terminal vertices are(a,0),a!=0.
There are m−1 of each. A source has no incoming edge; injectivity prevents
its forward path from merging with another path or entering a cycle.
Finiteness therefore forces it to reach a terminal. The source paths are
disjoint, and the total number of domain vertices on them is at most
m(m−1). Consequently the mean source-to-terminal edge length, **uniformly
over all m−1 source words**, is at most m. This carries CL697's mean bound
with an exact ensemble and endpoint convention. It gives no bound m for
the particular seed path:367 is compatible with mean<=256 atp8.

At fixed u, one of m farther words is the coincidence predecessor. That
is an exact count, not a per-wheel hazard along one deterministic orbit.
Neither injectivity nor the uniform-source mean establishes a2^p spacing
law, the distribution of reached sources, or period growth along every
branch. An actual restart at(0,d),d!=0 avoids a closed cycle at that fixed
period; a white-parent branch can change period and must be treated by its
own integration/entry semantics.

## Source/output guards

P-F1 correctly skips white u. P-F2 checks the inverse on each true adjacent
pair, resetting to true data after each comparison; its report is not an
autonomous backward error-propagation run, although all11997 local checks
pass. No new Intel validation of those observations is claimed.

The pair enumeration correctly finds65280 distinct images. However its
`seen` loop appends an exploration fragment whenever it starts at an
unvisited vertex, including fragments ending in a previously seen vertex.
It never separately labels closed cycles and complete source-to-terminal
components. Thus the268 "orbits" and length histogram are traversal-order
fragments, not certified cycle/path decomposition. The output supplies no
cycle-length/marked-point statistic supporting P-F5's registered cycle
ratio test. Keep P-F5 **not established by this output**; the later exact
uniform-source mean is a different result.

The367-step coincidence endpoint is consistent: starting pair(29,30),
after367 updates gives(396,397), the coincidence predicate at k397; white
is at399. The script's comparison against369 and its printed "check the
offset" need that correction, already understood in CL697's prose.

For11997 independent uniform16-bit comparisons, the expected number of
exact complement coincidences is11997/65536, about0.183, not0.003. The
six observed complement hits are a descriptive exception; independence
and a uniform comparison model have not been proved. The central histogram
shape does not license that model at its extreme tail.

Concrete repair before another enumeration: start from each source, follow
to the first white-parent terminal, recording full path lengths and marking
all used vertices. Then enumerate cycles only in the remaining unmarked
nonwhite vertices, with explicit return-to-start tests. This produces the
decomposition and exact uniform-source mean without a larger period.
Existing p8 data/map suffice; no job or larger-p census is dispatched here.

Atlas16.1 should use the nonzero-u guard and partial-bijection wording.
The earlier §16 claims about a generic phase lock and the crystal carrying
no centre information remain under GC2541/GC2533's guards; this algebraic
carry does not clear those stronger statistical assertions.

Record/prior-art comparison: current kit c42f6e51 `Rule30LeftReset` generic
reset/accumulation equations and `Rule30LeftUnbounded.pairCode`,
`pairCode_inj`, `left_profile_bound`, `D_period_unbounded` read. The latter
is the seed-specific common-period pigeonhole bound; the partial-map
description must not silently broaden its hypotheses. Rowland2006§5 is
the already-read reset/doubling comparison. No novelty or submission
clearance. Cloud's bibliographic/adoption counts in its owner-facing
assessment were not audited in this mathematical review.

My own pull: preserve the exact source-to-terminal paths and their branch
entry data, rather than replace their inherited distribution by uniformity.

## CL698 synthesis: attribution audit and carrying guards — GC2565

Complete194-line essay draft,24-line plan and57-line original citation map
read. The owner's synthesis authorization and division are recorded in
CL698. GPT takes this audit; Cloud retains prose/map ownership and Local
the anchor/build after A5. No posting or new theorem clearance is given.

**All four November attribution placeholders are resolved.** Fresh public
metadata for all20 named entries says `G.P.J.W. Quint; Gemini (Google)`.
Their current status is Lean Verified. In particular, the five November
extensions of AIOvernight's left-side modules belong to Quint/Gemini, not
to the original module author. Original file-addition commits confirm
AIOvernight added LeftReset/LeftUnbounded/FrontLaw/SettledBarrier/WhiteSpacing
in37a3d844 on30 October. DefectClockBudget is different: Troyusrex added
it in a5ad97fa on31 October. Both actual addition commits were read.
The citation map has the20 exact portal ids, correct PR links and objects.
The former eight-entry PR105–108 group actually spans PR99–102 and105–108.
DefectClockBudget concerns the right-edge clock, not left settled diagonals.

The live listing at16:17:59Z has114 entries,112 Lean Verified and2 Lean
Unverified. Its fefa7e entry is now Lean Verified, not still checking.
Neither that count nor the source read makes every portal entry a checked
new theorem. Quote a dated count or omit the introductory number80.

**Integration is checked separately from PR status.** PR83/85/86/87 are
closed with merged=false, but each exact changed Lean module is byte-exact
on current kit main c42f6e51. Their portal entries carry Human Verified and
Kit Contribution. Thus they are adopted source, not pending open work;
GitHub's merged field alone would give the wrong research status. Closed
issue conversations and review-summary bodies were freshly read (empty
for those four). PR84 remains open. Its maintainer discussion and exact
current sources show the requested finite BWH checks have been removed;
SmallRW is proved, but the period-two theorem still explicitly takes hb:BWH.

Fresh exact heads and changed Lean sources were retained for PR83–87,
97–102 and105–113; discussions/review bodies were read. This is attribution
and targeted statement audit, not an independent full proof carry of all
those modules. PR101 now supplies inverse_uninverse and inverse_bijective
on all streams and word-length<=3 separators; do not attribute that new
right inverse to older PR86. PR110's current title/public abstract still
mention minus10, while the exact current head also states the stronger
minus27 onset for k>=5. Cite a specific declaration/snapshot if using the
number, rather than reading a title as its formal theorem.

### The anchor's hand read already exists, with guards

GC2550 above is the complete independent F1–F3 carry. It is PROVED
hand/two-party for positive common period and a nearer parent u containing
a black; not single-party as the new draft says. Time-labelled cycles and
cyclic wrap are required. At a black of u, e(t+1)=w(t), not0: the inclusive
running-parity formula counts that reset value. The inverse for an ACTUAL
triple remains valid when u is white; a unique forward periodic F there
does not. Coincidence/white-child equivalence uses the nonwhite guard.

The pair map is a bijection D→I with D={(a,b):b!=0} and I={(a,b):a!=0}.
It is not a permutation D→D. A fixed-u count of one predecessor among2^p
is exact counting, not a1/2^p hazard along a deterministic orbit. The
uniform-source mean bound is not a seed-path bound. Existing p8 exploration
fragments were not a cycle decomposition. These corrections from GC2550
are needed in essay sections2D,3.6,7 and the atlas; adding a family theorem
in Lean does not establish the statistical claims or novelty over the
known reset/integration literature and kit base.

### Other necessary prose repairs, with concrete alternatives

* Section0: some entries are unverified; say the portal collects submissions
  at different verification stages, not that every entry is a theorem with
  a certificate. Recent dates/counts should be pinned.
* Sections1/2E: exact rightward speed1 needs an actual rightmost discrepancy
  and agreement beyond it. A pair with arbitrary unbounded difference has
  no such edge. State that finite-edge guard explicitly.
* Sections2E/5: replace old A4 id37281a by87ba7a, preserve its alignments
  and closure-entry/arbitrary-tail guards. A1's public check still timed out;
  say locally kernel-checked, portal maintainer rerun pending, rather than
  present it with the same public status as A2/A4.
* Sections2F/4: the absence of additive conservation laws does not exclude
  monotone rank functions, non-additive potentials, clock-dependent ranks
  or proof-state refinements. DefectClockBudget itself uses such a rank.
  Describe the exact excluded conservation class and leave other potential
  methods open; do not infer that Q01 cannot have a local potential.
* Sections3.2/3.5: a shared numerical half-bit rate is not an equality of
  languages or of four information quantities. Supply the exact map and
  hypotheses for a comparison, and preserve the earlier audited capacity
  distinction. A finite14-cell upper bound is not an all-width rate.
* Sections3.6/4:0.41,2^p spacing, generic synchronization and a universal
  fair core remain observations/conjectures with specified sample regimes.
  Keep them separate from the proved periodic reset law and affine inverse.
  “Passed every generic tell” should name the finite tests and horizon.

The older generated citation table also contains truncated statements and
mixed column meanings; it is retained as a historical excerpt, not cleared
for publication. The checked November table is usable for attribution.
A whole-portal essay still needs source-level checks of each additional
statement it selects; this audit does not certify every older row.

[Attribution/source receipt](receipts/gc2565-synthesis-attribution.json)
pins the20 live portal reads,20 current PR heads and the actual addition
commits. Raw public responses/source files are retained in
`cited/gpt/gc2565-attribution-receipts.tar.gz`,836276bytes, SHA256
095647edca5f4c7770e6f15320af726ab9dcb6366b1b3c944202a3d3ff3afe3c,
with byte-exact upload/readback. The same live listing still shows A1 as
Lean Unverified/error. Last COMPLETE known_find refresh stays15:49:56Z;
this targeted audit does not advance that timestamp.

## CL700 revised synthesis read — GC2572

Read the complete revised essay and PLAN at `4f68478f`, not just CL700's
summary. The November credits and ids, adopted-source versus PR status,
A1 timeout, A4 guards, additive-conservation scope, finite-width capacity,
and positive-period/nonwhite/time-labelled F1–F3 guards are now faithful
to GC2565. The partial-bijection and fixed-parent count qualifications are
also present. These repairs are accepted within that audit's scope.

Three precise points remain, with small repairs:

1. PLAN's revised "Done when" removed "the two-party read of the anchor"
   while marking the hand guards done. Restore a separate **independent
   read of the actual Lean anchor and its hypotheses**, alongside its
   checker pass. GC2550 carries the hand argument; it cannot pre-clear an
   implementation that Local has not built. There is no need to repeat the
   same hand review.
2. Section 0 says the essay cites only Lean Verified entries or kit modules,
   but it also discusses A1's public timeout and prospective A5/the synthesis
   anchor. Say instead that public verification, local checks and planned
   results are labelled separately. The scoped A1 caveat in section 2E is
   correct and should remain.
3. Section 4 names the 12,000 left diagonals and the 8,192-cell centre test,
   but those samples do not specify the fair-row front-speed 0.246 or the
   right-edge doubling-density 0.41 measurements. Give a separate record
   pointer and sample/horizon for each, or omit those two numerical values
   until the corresponding older source audit. This is a documentation
   request, not a request to rerun or enlarge any experiment.

Cloud retains the older statement/source audit announced in CL700. The
twenty November metadata attributions are checked, not every proof in those
entries; the older generated map remains historical until checked. This
read clears neither all older claims, the new Lean artifact, novelty nor
posting. No additional compute or anchor build is dispatched.

My own pull: use the coloured obligations exposed by the root-only proof
to select a smaller boundary memory before considering a product graph.

## L1474 actual Lean anchor read — GC2583 PASS

Complete142-line probe,140-line portal form (exact transformation diff),
33-line assembler, actual kit c42f6e51 `Rule30LeftReset` and the carrying
`Rule30Diagonals.D_step` read. This is the requested **actual artifact
review**, distinct from GC2550's earlier hand carry. No code repair is
required for the stated Nat-time theorems.

Pinned sources: probe90d01cee6a5af73de495385eef9cbdf88c2c6e8478c7d26f7ac711c7eb41ddb3;
portaldd902de5e902e976cc2857c287634516ecb82803f7a9f3947243765f4783a80f;
kit formed by the complete assembler
ed9747a27f8dc2b6b074e95d96001caf81335b7d6002727a59e53b3fe92510af.
GPT reconstructed the latter without writing to or compiling the kit;
the portal transform matches every byte. Source declaration/proof bodies
are unchanged by the namespace/import/public-section transformation.

**F1:** `par` counts exactly n terms starting at r; `par_cons` peels the
first term. The reset gives x(r+1)=not a(r), including a(r), while
`accum_upto` uses only r<k<=r+n, not an infinite white-run assumption.
For t=r the result is precisely the reset step; for t=r+n the parity
has n+1 terms. The explicit r<=t guard prevents Nat subtraction from
silently replacing a negative length by0. The proof's induction and
rewrites preserve these endpoints.

**F2:** `farther_of_child` is cancellation of XOR for any actual triple;
there is no nonwhite or periodicity hypothesis. `farther_unique` is
pointwise recovery followed by extensionality. `solutions_agree` starts
at s0+1 after the black b(s0), then inducts on time with identical inputs.
It does not claim equality at s0 or unique forward behavior without a
reset. This matches the distinction carried in GC2550.

**F3:** the two ranges deliberately differ: child/nearer equality from
s0+1, derivative equality from s0. In the forward direction, the t=s0
case uses b(s0)=1 to mask x(s0); it never assumes x(s0)=b(s0). For t>s0
both child values are known. Conversely, the derivative at s0 and the
reset establish the first equality, then the recurrence proves the rest.
The all-white countercontrol remains excluded by the explicit black
hypothesis. No periodicity is needed for this theorem.

All three D instances substitute the exact child D(j+2), nearer D(j+1),
farther D(j) in `D_step`. These D definitions describe the single-cell
pattern; the generic recurrence theorems apply to arbitrary words. Do
not turn those particular D instances into an unstated arbitrary-seed
theorem in the essay.

**Cyclic corollary, with a precise boundary.** Fix positive common p and
time-labelled periodic a,b, with b nonwhite. Construct any Nat solution,
apply `reset_periodic`, and extend its settled p-block to all phases.
The periodicity of a,b makes that phase extension a cyclic solution.
`solutions_agree` plus periodicity makes it unique. Conversely, for any
p-word x, recovery defines a periodic a and makes the recurrence hold,
giving the bijection. One can translate F1 past a reset to handle cyclic
wrap. This elementary passage is the earlier carried hand argument;
`reset_periodic` itself states **eventual periodicity of a given child**,
not existence of a periodic child as one standalone theorem. No single
cyclic-bijection or affine-map theorem is exported by this module. The
source and L1474 already distinguish the cyclic phrasing from formalized
Nat-time statements; preserve that distinction in the synthesis essay.

**Raw receipts read:** `cited/l1474-f123/f123-checks.tar.gz`,1254bytes,
SHA256fc987fdbbcac7fc82d2b80b9b2f49b0c5a7fcbee0224108652edab152c0e9fea.
Both outputs report pass,30 replay constants, six exact headline matches,
statements imported, no new axioms or verified prize targets. The
recovery headline uses no axioms; the other five list only propext and
Quot.sound. Both contain the known Check.lean deprecation warning about
Environment.replay; this is distinct from the reported clean module build.
The output bodies do not cryptographically bind the source hash or give
a launcher/mutation log. The claimed first-try build and eight-error
mutation therefore remain Local-reported, not independently inspected
logs. No Intel compile or kernel replay was run.

[Read receipt](receipts/gc2583-f123-source-read.json) pins these materials.
**PASS** for exact source/proofs and the six stated headlines. This is
not yet a notebook/embedded-essay review, public Lean Verified outcome,
whole-synthesis citation clearance, novelty assessment or posting event.
Local owns packaging/build; Cloud owns the CL701 older-source audit and
abstract. The precise source-review gate requested in GC2565/2572 is now
met. Final packet correspondence remains a separate read when it exists.

## CL702 scoped live-source review — GC2585: repairs required

2026-11-03, GPT. Reviewed the appendix at 08e05805 and the relevant prose
through d5d900e4. This completes the requested placement, three-name and
twelve-repair review. It is not a fresh proof audit of all portal entries,
a whole-essay reread, an Intel compilation, or final packet clearance.
Cloud retains prose and appendix ownership; the concrete amendments below
are ready to apply. [Evidence receipt](receipts/gc2585-synthesis-source-review.json).

**Sources and freshness.** A complete `known_find.py --new` finished at
17:58:54.423124Z: kit c42f6e5133f61a47e99289fd4b6e0536fd8a0453,
119 current portal entries,38 open PRs. Twenty selected status pages were
then fetched directly with verified HTTPS at17:59:50–58Z, including all
three requested names; e67465's public notebook was also read for its
byline. The relevant exact declarations of the kit and portal sources,
PR65/PR46 metadata, and the original recorded measurement samples were
read. The receipt distinguishes live metadata, source statements, carrying
hand arguments and previously reported computation. No new dynamics run.

### Required mathematical and measurement wording

1. **Restore yingy's exception in §2B.** `stripe_four_tail` requires
   `v.val ≠ 13 ∨ m % 2 = 0`. The four-bit tail13 is `1011` when read
   outward from the stripe. The live abstract explicitly excludes that
   tail with odd m; the kit declaration has the same hypothesis.
   Write: “four-cell stripe tails have an even white depth-1 time
   t ≤ d−1+31 after first deviation depth d, except tail1011 with odd
   stripe length (yingy,81df0e).” Here1≤d≤m+6. This is not an
   unconditional31-step theorem; Quint's later unconditional mortality
   result017d83 is a separate citation and does not remove the earlier
   bound's guard. No new counterexample computation was run.

2. **Guard and identify the degree statement in §2F.** This is the
   Boolean function of an *arbitrary initial cone*, not the degree of
   a fixed single-seed bit. The current kit's
   `Rule30Equivalents.AlgebraicDegree.isGreatest_card_coef_center` assumes
   t≥2 and gives degree2t−1. Norris603218's combined headline
   `rule30_anf_degree_and_walsh_spectrum` assumes t≥3, because it also
   asserts uniqueness of the top monomial. At t=1 Rule30 has the
   quadratic term centre×right, so the unguarded formula is false.
   Suggested wording: “For t≥2 the t-step centre map, as a Boolean
   function of its initial cone, has degree2t−1 (the kit's
   `equivalents/AlgebraicDegree`; Norris603218 packages degree, unique
   top monomial and Walsh balance for t≥3).” Condrey's
   `Rule30TopCoefficient` is a distinct current contribution: it gives
   a parameterized top-coefficient identity for quadratic left-permutive
   rules. Do not present Norris's imported degree theorem as a newly
   established degree theorem of that submission, or infer that every
   such quadratic rule has the same nonzero top coefficient.

3. **Separate the two “free bit” statements in §2B.**
   `count_constrained W` counts width-W lists whose zero-boundary
   depth1 stays black at even t<W: exactly2^floor(W/2).
   `free_bits_no00_no11111` instead assumes the *actual seed centre*
   alternates black-first from T for all future times and concerns
   `cell (T+2k+1) (-1)`. It is not a restriction on every freely chosen
   bit of all the finite-horizon counted starts. Replace “and their
   free bits” by “separately, under an eventual alternating centre,
   the odd-time column−1 bits avoid00 and11111.” The opening clock
   context is helpful but does not equate these two quantified sets.

4. **Separate the speed samples in §2E.** Section8.66 reports0.2468
   over eight random single-flip trials of8192 steps. CL678's actual
   `speed_law.out` gives0.2457±0.0084 for five fair-row inserted-edge
   samples of6000 steps, measured over[3000,6000]; its five single-flip
   samples give0.2521±0.0045. The displayed uncertainty is computed by
   the script as population standard deviation divided by sqrt(5),
   not a proven asymptotic error bound or confidence interval.
   The draft must not attach0.246±0.008 to both sample sets together.
   Suitable short wording: “about0.246 on the recorded fair-row
   samples:0.2468 in eight8192-step single-flip trials (§8.66), and
   0.2457±0.0084 in five6000-step inserted-edge trials (CL678).”
   These remain finite measurements on the producing hosts.

5. **Keep the right-edge observable explicit in §§3.6/4.** The
   64-seed sample consists of *prefix block-exponent* increments for
   odd24-bit seeds, n=13..56,2816 positions. It is not a sample of
   every individual right diagonal's least period. CL642 gives the
   original0.407±0.009 report; CL645 cites it and supplies the run
   test. The single-seed figure is about0.42 through j=92, and the
   kit docstring says approximately0.43j. Keep these finite scopes
   separate from a uniform or asymptotic exponent law. No reproduction
   of that experiment was requested or performed.

### The twelve repairs, individually

| CL702 item | Verdict after the primary-source read |
|---|---|
|1, Lowry padding|PASS:8fe04c has r≥10·length(v)+41 for0^r v011;524848 has all16 six-bit black-ended cores at r≥74, for columns of leftmost-black configurations.|
|2, word lists|PASS as lists beyond the kit table, not blanket novelty:7a9ed3 lists87 words of lengths12–16;5e2b66 andf7ace9 cover11–18. Their correction abstracts explicitly retain earlier overlaps.|
|3, classic ether and PR65|PASS: the classic7×4 ether and109-state wall are `Rule30Ether`; PR65 is `Lock` and periodic-left/finite-right witnesses, matchingc137e0. The PR is closed unmerged, while adopted source is on main; do not call the PR merged.|
|4, G8|PASS for the new COMPUTED label and eight-tick background. The five6000-tick alignments all report0.5; an old ledger label “PROVED” is not a substitute for a carrying source. No uniform new speed theorem is certified here.|
|5, constrained counts/free bits|Names correct; the quantified scopes must be separated as above.|
|6, widths|PASS:52=96 and56=100 are publicly Lean Verified;60=114 remains publicly Lean Unverified at the live read. Widths64–76 are formal lower bounds, not public maximality certificates.|
|7, left diagonals|PASS for scope and dual credit:0616de covers leftmost-black configurations, after Rowland; `Rule30LeftUnbounded` uses the seed's D. Date precisely: PR46 opened28October; the current file's kit adoption is30October, commit37a3d844. “28October” should identify the PR, not the adoption date.|
|8, EdgeObservable|PASS: `HasLeftEdge`, finite configurations and equality of all centre-trace times imply equal left edges as an OPEN hypothesis; `problem1_of_edgeObservable` is the conditional theorem.|
|9, degree|Attribution needs the imported `equivalents/AlgebraicDegree` theorem and the time/function guards above. TopCoefficient is separate.|
|10, periodic points|PASS: `equivalents/Rule30Equivalents/PeriodicPoints.lean`, `Recurs`, `recurs_add_factorial`; recurrence F^k x=shift^d x with1−k≤d≤k gives spatial periodicity, velocity−d/k∈[−1,1). +1 is outside that range. a96cee's positive-period/positive-ring finite interpretation remains separate.|
|11, other names and Lee|PASS: Eric Elbaz, Jeongseop Lee, Emerson Villafuerte and giraudsa as displayed. Lee's theorem requires finite support, a32-step return and alternating shielding gates; it concludes a2-step return, not exclusion of a centre period. e34744 is current; the removed9d92a2 is not a current portal entry.|
|12, numerical sources|Correct source families; repair the combined speed sample and distinguish block exponents as above.12,000 left diagonals concern a different empirical law.|

For item7, the read establishes the chronology of these public artifacts,
not who first discovered a theorem. Rowland remains prior art. The
absence of a citation in a module header is not evidence of independent
discovery or an attribution allegation.

### The three requested names

- **29bcb9:** live authors field is “Leonardo Jiménez Martínez;
  Claude Opus 5.5 (Anthropic)”. Use Leonardo Jiménez Martínez.
- **81df0e:** live authors field is “yingy; Codex”. `yingy` is the
  published display name. No expansion to a personal name is justified.
- **e67465:** the live field remains literally `Matev~ Kova\ri\r;
  Claude(Anthropic)`. The public notebook's byline is still
  `By <your name> and Claude`, so it does not repair the encoding.
  **Kovačič is not independently confirmed.** Use the entry id/title
  in prose for now; the appendix can say “author name garbled on the
  public page” linked to e67465. This avoids a guessed spelling and
  does not block the mathematical map. No personal identity lookup or
  message to that contributor was made.

### Appendix: coverage and placements

All115 existing rows and their primary/secondary labels were read.
Title/object placement was checked throughout; ambiguous placements
were checked against the full abstract, and the four new entries against
their exact headline statements. This is a map review, not acceptance
of every proof or every empirical sentence in those abstracts.

The115 ids are distinct and all remain present in the current119-entry
portal. Four entries arrived after Cloud's113-entry snapshot plus our
two posts. Add these rows, with the current snapshot time rather than
claiming an undated exhaustive catalog:

| New id | Suggested placement | Statement and boundary read |
|---|---|---|
|b476c1|A/G|Exact disjoint cylinder count of white-centre/black-right times; generic trajectory cylinder identities, seed gap existence. No positive-density lower bound.|
|452bbf|A/G|5^j(b_j+20)≤20·8^j and the corresponding log-base8/5 black-count bound. Still logarithmic, not positive density.|
|4b2a58|F/G|Proper-marginal/nonnegative-observable obstruction with16-cell potentials, and no exact coboundary. The actual headline types are rational-valued; the abstract's real-valued wording is not itself a Lean theorem in this file. No wider/time-dependent-potential exclusion.|
|84a42c|D/G|Fresh right-diagonal binary digits and bijective staggered samples over each2^m-column block. No conclusion at the single centre phase or about centre density.|

All four are Lean Verified in the refreshed portal; this read adds no
independent compilation or Human Verified status. Their pinned source
hashes and the complete refresh digests are in the receipt. They touch
our open density, observer/potential and odometer questions, so should
also inform the next reading queue before any novelty decision.

Two primary-placement improvements are suggested:

- 60d213 Sparse16: **B/A**, rather than A/B. Its primary quantified
  object is the zero-boundary half-line surviving56 even observations;
  centre alternation is a corollary. The prose already treats it in B.
- 0ef9c8 Lee: **E/B**, rather than B/D. Its primary object is the
  finite moving-front state, with gated32→2 recurrence. B is a
  secondary connection; it proves no exclusion of centre period2.

These are navigational choices, not claims that Cloud's labels were
mathematical errors. The other113 primary placements are reasonable.
Add D as a secondary letter to e34744's A/C, and G to5da074's D, if
secondary letters are intended to record all principal bridges.
With the two moves and four additions the counts are
**A24,B42,C6,D22,E7,F9,G9,total119**. The appendix header should say
“first listed author; ‘ours’ as defined in the essay”, not “first name”.

### CL703's requested white-child direction — GC2586 hand carry

The requested completion is sound with its black guard. Suppose
`x(t+1)=a(t) XOR (b(t) OR x(t))`, a(t)=b(t) for t≥s,
and b(r)=1 for some r≥s. For t≥s the recurrence is
`x(t+1)=NOT b(t) AND x(t)`. Hence x(r+1)=0; induction
keeps x(t)=0 for every t≥r+1. Conversely, if x(t)=0 for
every t≥T, substitution at t≥T gives a(t)=b(t).
Without a black the forward assertion is false: a=b=0,x=1
is a permanent solution. No periodicity is needed for these Nat-time
claims. This carries Cloud's proposed step **PROVED by hand/two-party**;
the new declarations and their source/build checks still belong to
Local. GC2583 already passed the earlier actual F1–F3 anchor source;
the draft's “GPT read pending” should be replaced with that precise
scope. The final notebook/embedded essay remains a later packet read.

**Next executable step and ownership.** Cloud applies the cited scope,
name and119-row amendments. Local adds the two guarded white-child
declarations and packages the anchor. GPT reads those exact additions
and the final packet when available; independently, it can compile
the retained GC2570 root-forcing DAG with the already verified a10
template, after a source freeze. No new root search, graph census,
trajectory run or automatic cap enlargement is requested.

My own pull: the retained root-DAG certificate compiler; the scoped
Cloud review took precedence and is now returned with concrete repairs.
