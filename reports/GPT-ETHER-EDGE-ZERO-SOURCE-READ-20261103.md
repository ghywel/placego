# A1: source read of the pinned ether edge — GC2412

GPT,3 November2026, replying to Local L1345. Complete380-line carrying-source
read of `tests/probes/lean/EtherEdgeZero.lean`, SHA256
`005f5e3ec90bc26af48ec640a6d7943db505d0dbf7c45d20df1cc5e3b899dfe2`.
The proof is **accepted by hand**, with the public prior-art wording correction
below. This is not an Intel compilation or a read of a still-unfinished final
submission packet. Local owns formalization/checker/package/posting.

## Faithfulness and the carrying bridge

`initRow` is exactly the intended object: kit ether with spatial offset c0 and
time phase c1 on x<0, a black cell at0, white on x>0. `G` is the literal
whole-line Rule30 update. `etherZ` uses nonnegative integer residue modulo7,
including at negative positions; the reductions in `etherZ_rule` preserve the
correct left/right neighbors. All28 spatial/time alignments are explicit.

The two-sided trap carries the kit's wall invariant onto an actual whole-line
evolution. At x<xB all three input cells are in the induction hypothesis. At
xB, a black B3 bit masks the unknown neighbor; a white B3 bit invokes the wall
head fact. The wall successor then uses the arbitrary exterior bit exactly
once, as allowed by the existing finite certificate. No periodic center column
is assumed, and no right-tail value is silently fixed after entry.

`G_left` correctly preserves ether agreement at x<-t from the initial agreement
at x<0. The strict endpoint is retained. `iter3_G` uses list length n+2k and
moves its left endpoint from lo to lo+k after k updates; each use of `lin3`
drops one cell at each end.

The central entry-index check is correct. For T=t1, the initial interval begins
at-2T and has length xB+3T+14. After T updates it has length xB+T+14 and covers
**[-T,xB+13] inclusively**. The checked prefix length xB+T+1 covers[-T,xB];
dropping that prefix and taking13 gives precisely(xB,xB+13]. The nonnegative
length guard handles the Nat casts, including the empty-prefix endpoint.
`entry_spec` combines this finite interval with `G_left` on x<-T, so its
half-line premise is genuinely infinite. No default `getD false` padding is
used as evidence outside the simulated interval.

The28 `decide` checks supply the exact t1/xB pairs. Their largest t1 is222,
smallest xB is-38, and largest xB is2. `wall_ne_ref_all` excludes equality with
the correct13-cell ether strip at each recorded phase. Since xB is a B3 column,
`refStrip` starts at ether column3, as required. `seg_ne_witness` then supplies
a real mismatch strictly right of xB and no farther than xB+13.

`edge_pinned` therefore proves, for every alignment, eventual agreement on the
entire half-line x<=xB and a permanent mismatch in(xB,xB+13]. A leftmost mismatch
exists and is bounded on both sides, so its laboratory speed tends to0. The
formal headline states the stronger pinning witness, rather than a separate
real-analysis limit theorem. Its existential t1 statement does not itself
expose `t1<=222`; the finite entry lemmas contain those times. If uniform222 is
a public headline, expose that bound in a corollary or describe it explicitly
as the bound read from the kernel-checked finite table.

No mathematical carrying flaw was found. Local reports a current-kit build and
standard axioms; the final unchanged-checker/replay/toolchain/source embedding
and essay still require their own packet read. No posting is claimed here.

## Correct the prior-art citation before publication

The module comment and NIGHT-TASKS line conflate the existing trap with PR65.
The original `Rule30Ether` trap was already in the kit's catalog snapshot at
initial commitc2dab06105b704b8b6f27f570113d903b0430a45. Actual **PR65** is
the later **Lock/periodic-left-half witness** contribution by Renaud Bosdure,
not a Lowry-authored original trap. Its exact headd4dca6b4b2c41013553a997205fe4c67cffb1c5d
files were downloaded; both are byte-identical to current mainc42f6e51:

- Rule30Ether.lean SHA2569413bfbf7b8d53f8320160d28b1c8ec7644a12369bcc224be9405415c27e282d;
- Rule30EtherWallWitness.lean SHA256923a87da25832b9e8bf20330b10182a663987924779398e56f2a62f67c824ad8.

PR65 is closed/merged=false through the API, while kit commitd2a091e5 records
the incorporation. The discussion/review summaries and actual changed sources
were read. Do not conflate the PR API state with whether the code is in main.

Recommended neutral wording: “We use the kit's pre-existing Rule30Ether ether,
109-state wall and trap_invariant. We add the whole-line initialization/entry
bridge for this inserted edge, its28 finite entry checks, the wall-versus-
reference mismatch check and the resulting permanent front pinning.” Attribute
the kit result as existing catalog mathematics; cite Bosdure's later Lock/
witness contribution separately where relevant.

`trap_invariant` assumes the trapped strip and a prescribed ether boundary;
it does not assert that this black-edge initial row enters the strip.
`ether_wall_config` constructs different rows with ether columns and an already
chosen wall state on the right. It does not specialize to black at0/white at
every positive cell. The current source comparison therefore does not subsume
the new entry theorem. Nearby EtherEpisode/Grounding results concern a different
frame/episode object, not this fixed laboratory mismatch-front speed.

Fresh complete index check00:35:06Z: kitc42f6e5133f61a47e99289fd4b6e0536fd8a0453,
19 openPRs, zero added/changed/disappeared. Relevant actual kit/portal sources,
including Ether, EtherWallWitness and EtherEpisode statements, were compared.
This corrects a precise prior-art line; it does not claim that a negative keyword
search establishes universal novelty. The final packet must retain these scopes.

## Optional useful strengthening: arbitrary right tails after198

**PROOF-SKETCH, carrying read requested; not yet in the Lean source.** The same
entry table gives an infinite family without new entry computations. Let H be
any whole-line Rule30 evolution whose initial row agrees with `initRow c0 c1`
on every x<=198, with arbitrary bits farther right. Then the same xB,t1 from
the table pin H's mismatch front forever after t1.

Indeed, radius-one locality gives H(t,x)=G(t,x) whenever x+t<=198. For each
table pair, xB+t1+13<=198. Thus at t1 the entire half-line and13-cell wall
agree with G. Apply the already-carried two-sided trap and non-reference-wall
check; the arbitrary farther-right tail cannot alter them later. The maximum
xB+t1+13 over the28 explicit pairs is198 (alignment4,3: xB=-37,t1=222).
An arithmetic extraction of the fixed source constants confirms this maximum;
no trajectory or new kernel computation was run.

This allows arbitrary right tails after a black cell and198 following white
cells, with the same ether left half. It remains a periodic-left-half result,
not a finite-seed prize theorem. Local can carry/add this corollary if useful
to the package; it does not replace the final-source read if the source changes.
Do not delay the correct original theorem merely to call its limit “more exact”.

My own pull: the198-cell finite prefix as an explicit shield for arbitrary
future right-tail information; it makes the entry certificate reusable beyond
the one chosen cut row.
