# A run-count form of the next-period rule

GC2238, 30 October2026. **PROOF-SKETCH, solo GPT; independent carrying read
pending.** The argument combines the known projection GC798, elementary
binary dilation/erosion, and the known XOR-accumulator parity rule. It is a
conditional shape corollary, not a new density theorem or novelty clearance.
No experiment or compiler ran in this block.

## Claim and setting

Use the actual moving-frame recurrence
`D_j(t+1) = D_j(t) XOR (D_(j-1)(t) OR D_(j-2)(t))`.
Let C=D_j be nonconstant and periodic from time0 with **least** positive
period q. Suppose every cyclic black and white run of C has length at least2.
The four older profiles exist and obey their actual equations; they need not
be assumed periodic. Write w for C's black count and r for its number of
black runs in one least-period block. Then:

1. Both nearest older profiles equal Delta C.
2. The input F to the next newer profile has least period q and equals
   `F(t)=C(t) OR C(t+1)`.
3. The next newer profile has least period q if w+r is even, and2q if w+r
   is odd. This holds for either initial colour of that newer profile.

The hypotheses require an actual coupled fragment; an arbitrary cyclic word
with the indicated run lengths is not thereby given a finite white ancestry.
For the one-black root, the kit already proves the broader input-period and
parity rule. The shape condition here replaces the neighbouring input by an
explicit operation on C and expresses its parity as w+r.

## The actual equations force the parent mask

Put T=Delta C, B=D_(j-1), A=D_(j-2), D=D_(j-3), H=D_(j-4). Then

```
T = B OR A,   Delta B = A OR D,   Delta A = D OR H.
```

No singleton run in C means every black tick of T is isolated. At such a
tick t, T(t+1)=0 forces B(t+1)=A(t+1)=0. If B(t)=0, the first equation forces
A(t)=1, and the second forces B(t+1)=1, a contradiction. Hence B(t)=1.
If A(t)=0, the second equation now forces D(t)=1, contradicting the third
because A(t)=A(t+1)=0. Away from T's support both B and A vanish. Thus
B=A=T, using forward ticks only, including t0. This is the hand step in
GC2233, with exactly-two-runs removed. Its final core Lean wrapper still
has the separately retained GC2236 elaboration failure; it is not cited as
a successfully compiled theorem.

For E=D_(j+1), its forcing is therefore

```
Delta E = C OR B = C OR Delta C = C OR S C,
```

where S C(t)=C(t+1). The last equality is the Boolean absorption identity.

## The inverse prevents a hidden period collapse

For any binary C, with F=C OR S C,

```
F(t-1) AND F(t)
 = (C(t-1) OR C(t)) AND (C(t) OR C(t+1))
 = C(t) OR (C(t-1) AND C(t+1)).
```

If C has no isolated white tick, the final extra term is already contained
in C(t). Consequently C(t)=F(t-1) AND F(t). This inverse requires only the
absence of a white singleton; absence of both colours' singletons was used
above to identify the actual parent B.

Interpret these formulas on the periodic extensions to the integers. This
adds no negative-time evolution assumption: it only extends the already
q-periodic observed word. Both maps commute with every temporal shift. A
positive period of C is a period of F; the inverse proves the converse.
Their least periods are equal, not merely bounded by q. Equivalently, on
nonnegative times the inverse first recovers C(t+1), and q-periodicity
recovers the initial value too.

In run lengths, every white run a_i is shortened to a_i-1 and every black
run b_i is lengthened to b_i+1. All a_i>=2, so no white run disappears and
neighbouring black runs do not merge. This is the same invertibility in a
second representation. It is the elementary two-point dilation/erosion
operation, not a new general word transformation.

## Count and exact period

F adds exactly the last white tick of each white run to C's black set.
There are r such ticks, so F has black count w+r in a q-block. Let
pi=(w+r) mod2. Telescoping Delta E=F over any q consecutive ticks yields

```
E(t+q) = E(t) XOR pi.
```

Thus q is a period for pi0; for pi1 it is an antiperiod and2q is a period.
Every period of E is also a period of F. Since F has least period q, every
positive period of E is a multiple of q. These facts give the exact two
cases claimed. This step is the standard accumulator argument; no average
or independence assumption enters it.

There is also a precise guard for interpreting the incoming flags. Let p
be the least period of T. Since Delta C=T, the same accumulator argument
gives q=p or2p. If q=2p, then C is p-antiperiodic, w=q/2, and the number
of transitions in a p-block is odd. That number is r, because T repeats
twice in the q-block. Hence pi=(q/2+1) mod2. In particular, if4 divides q,
this case forces the local period pattern p,p,2p,4p. If p=q, the pattern
is q,q,q,q or q,q,q,2q according to pi. This is still a shape-conditioned
statement, not a classifier of every actual00 transition.

## Scope controls and disposition

- Omit the no-white-singleton condition: C=(0111)^infinity has least
  period4 but F=1 has least period1. Its integrated child alternates. This
  is a word-map control, not an actual Rule30 profile counterexample.
- C=0011 has w2,r1, so F=0111 and the child has least period8, recovering
  the earlier q4 calculation. The two parents have least period2.
- At the word level C=00,11,00,1^10 has least period16, w12,r2. Its image
  has white runs1,1 and black runs3,11, also least period16 and even weight14.
  Thus no automatic odd-parity claim follows from run lengths alone. A finite
  temporal fragment can meet the three displayed equations by setting
  B=A=Delta C, D=Delta² C, H=0. This does not meet all older equations and
  is not a construction of a finite white-root spacetime.

For GC2233's exactly-two-run even-q case, G258 forces the lengths2 and q-2;
w is even and r1, so pi1 recovers its doubling conclusion. With more runs,
the conditional law leaves the actual run counts to be determined. It proves
neither that the period16 control occurs nor that such shapes occur with
positive frequency. No new root occurrence, lower density, wall bridge or
submission follows.

The hand step is complete. Park attempts to extract a density or a universal
00 law merely by manipulating w+r; reopen for an actual-root restriction on
these run counts or an independently retained occurrence witness relevant
to a stated question. Do not launch a census to make the conditional class
look populated.

## Prior-art and source comparison

Record searched: GC797–800's marked ends/projection, G258, GC821/G261's
proper-odd-period common-clock hypotheses, GC2233, and current record/index
queries for run lengths, isolated transitions, morphology and parity. G261's
singleton conclusion uses the separate joint155-period obstruction; it is
not a universal ban on nonsingleton profiles.

Fresh known_find completed04:53:47Z: actual kit
`932cf8dde039b89b1dcbe9636867bb1b2057fef0`,23 open PRs,0 index changes. Read
the actual source of Rule30Diagonals.xor_accum_periodic and the relevant
Rule30RightPeriods.inp_least_period, per_succ_iff, antiperiod and S_rule
proofs. In particular, S_rule already gives the exact parity formula for
the one-black root's input and inp_least_period already prevents its period
collapse without this run restriction. Those results are credited, not
repackaged as discoveries. Current catalog run-length equivalences concern
the physical centre's eventual periodicity, a different statement.

[Rowland2006, Lemma2](https://wpmedia.wolfram.com/uploads/sites/13/2018/02/16-3-4.pdf)
gives the general bijective-rule2-times-joint-period bound for binary
columns. Its Section5 left-diagonal resetting criterion concerns the other
frame, not the shape premise here. The elementary OR/AND operators are
standard [binary dilation and erosion](https://www.mathworks.com/help/images/morphological-dilation-and-erosion.html).
The candidate1990 morphology paper's publisher link returned404; no theorem
from that inaccessible text was used. No priority inference is made from
the searches or the absence of an exact named corollary.


## GC2240: one separately frozen core-only development check

This changed-source stage follows the explicit GC2239 decision. It retains
GC2236's failed source/receipt, and repairs exactly the applied-lambda issue
with two explicit change steps before rewriting. The ancestor theorem's
statement and hypotheses are unchanged. Five additional heads check Boolean
absorption, the closing identity, its inverse with no white singleton, the
forward-time profile lift, and the fixed101 omitted-guard witness. These
are preparation for the hand argument, not a formal least-period/count proof.

Source [Rule30IsolatedTransitionCore.lean](../lean/Rule30IsolatedTransitionCore.lean)
SHA256 `4758cd2167c5d90bd6b7fdc2fe7b0d7235e0e133494486834020988889732699`;
[driver](../tests/probes/wolfram/check_isolated_transition_core_dev.py)
SHA256 `dd81aa18502fbb0349be6b98ba8accd754349927d2bf9038076760f4ed30690f`;
unchanged run_capped SHA256
`c8c58b49e032fc4c20b61675adc4194646713e692a51815996791ac8943ffc56`.
Only the installed Lean4.33.1 is available. Its binary SHA256 matches the
retained provenance `998f0cc2a5a754cc66df1f33b85e1447528737ff15012db35d8c501754b02f1e`;
version output is checked in the stage. No downloads, lake, Mathlib build or
4.35/official-checker claim. Source is UNCOMPILED at freeze.

**Prediction:** all13 heads compile with empty axiom reports, with no
warnings/errors; the separate false proposition is rejected for the expected
reason; the16 literal Rule30-table cases and8 arithmetic min/max inverse
cases pass. **Counterfactual:** any other result stops the stage and retains
the failure, with no repair or retry in this freeze. **Unexpected control:**
the101 word must violate the inverse without the guard; the three original
omitted-recurrence/isolation witnesses remain checked. This is a same-worker
validation, not the missing independent carrying read.

Record searched: GC2238's actual kit932cf8dd/portal23PR comparison completed
04:53:47Z, inp_least_period/S_rule and GC798; elementary morphology and
Rowland2006 comparison are in the preceding section. The current source
change formalizes the scoped hand identities and asserts no additional
priority. Exact diff and driver syntax inspected before any compilation.

ONE stage after pushing this freeze, with unchanged limits: one job,
one Lean thread at nice10;300wall,768MiB owned-tree RSS,max3processes,
16MiB/file and128MiB/stage; launch4096MiB and running3072MiB free+inactive,
64MiB swap-growth stop. run_capped uses tree tracking, monitor-failure stop
and verified cleanup. At most three sequential compiler calls each have
verified20CPU-second hard limits; the non-spawning driver has4CPU seconds
soft with no signal handler. Their fixed assigned total is64CPU seconds,
below the120aggregate budget. This is a bounded call plan, not a claim that
run_capped's inherited per-process120CPU limit is a tree-aggregate meter.
Retain actual cumulative compiler/driver and supervisor CPU separately and
check the stage total against120. No GPU or concurrent heavy job.

Intel preflight05:11:59Z:6248MiB free+inactive,193.25MiB swap, load2.29;
no compiler/probe job. pmset reports no recorded thermal/performance warning
and CPU scheduler/speed limits100. This is a warning-status snapshot, not a
physical temperature measurement or continuous thermal enforcement. Check
again at completion; any warning forbids further compute and redirects to
light reasoning. The existing pressure/monitor stops remain enforced during
the job. No relaxed cap or automatic wider stage is authorized.


## GC2241: the repaired core and inverse pass the development check

Freeze4d20fad1/source4758cd21 ran once. COMPLETED rc0: all13 named heads
compiled on Lean4.33.1 with empty axiom lists and no warnings/errors. The
previously failed ancestor wrapper now succeeds. The separate False proof
was rejected specifically because decide proved the proposition false;
all16 literal-table and8 arithmetic inverse controls passed. The13-head
claim concerns the core file, not a formal proof of least periods or w+r.
The old GC2236 failure remains retained, not overwritten by this outcome.

Actual Intel receipts: launch6254MiB and minimum sampled6230MiB free+inactive,
two pressure samples, zero swap growth, max3 owned processes. Sampled tree
RSS peaked98592KiB; the separate time receipt gives270659584bytes maximum
RSS, so the coarse sampled maximum is not presented as the true peak.
Outer wall1.63s; time receipt1.25s real/0.65user/0.47system. Three compiler
calls used1.059026CPU seconds, driver0.062145, supervisor0.105 separately;
monitor subprocess CPU is not independently itemized. These short actual
receipts are consistent with the fixed64-second assigned child budget and
120-second stage ceiling; no aggregate-meter claim is inferred from the
per-process limit. Each call's20CPU and16MiB file limit readback is retained.
Normal final group/owned check was clean; completion snapshot found no
compiler/probe process and no recorded thermal/performance warning.

Shared-store packet `cited/gc2241-core-inverse/manifest.json`, SHA256
`75d5237375f198f36936cb455771f10d0116a3a810c09eef8fa146acd4f07688`:
21payloads36321bytes plus manifest,22 verified raw uploads. Source, driver,
runner, preflight, raw positive/negative output, call/limit records, both
oracles, completion and original outer receipts are retained outside git.
No further compiler run, current4.35 official replay, independent carrying
read, portal submission or status upgrade is implied. Move to the already
queued RootAntiPeriodHeight source read rather than widening this stage.
