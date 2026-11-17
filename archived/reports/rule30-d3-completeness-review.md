# D3 and finite-word safety completeness: the exact equivalence

GC2248, 30 October2026. The existing external implication and converse are
**carried in their stated conditional scope**. The carrying induction,
semantics and finite dispatch were read; the generated trajectory branches
are supported by retained author kernel replay, not a new GPT replay or
an individual hand recomputation of every branch. Neither side of the
equivalence has been proved here.

## Exact statements and boundary

Use older-first finite Boolean words, with two missing older cells fixed
white. The simultaneous update sends each cell x to x XOR(p OR r), where
p,r are its two old older neighbours. Safe(xs) means that the newest cell
of this actual finite-white evolution never has two consecutive white
values, over all times. The empty word is unsafe by its white default.

The two statements are:

- **D3Star:** every safe word beginning with its first black cell and having
  length at least4 has a safe proper prefix obtained by deleting1,2 or3
  newest cells. There is no return hypothesis in this statement.
- **ReturnComplete:** every safe finite word returns as a whole after8
  actual updates.

At immutable archive commit
`0cbc49ef30888b32760def46ec31f954626192ff`,
[RootD3Reduction](https://github.com/Troyusrex2/Rule30PrizeKit/blob/0cbc49ef30888b32760def46ec31f954626192ff/research/agent-experiments/coordinator/20261026-short-extension-proof/work/root/RootD3Reduction.lean)
proves the forward implication, and
[CedarD3Converse](https://github.com/Troyusrex2/Rule30PrizeKit/blob/0cbc49ef30888b32760def46ec31f954626192ff/research/agent-experiments/coordinator/20261026-height-and-cylinder/work/root-height/CedarD3Converse.lean)
proves the reverse. Source digests are respectively
`013b6889de1e3aa1207b2c306a80e911d23db55f90af1a1928dabc8cc4230d66`
and
`1db70283df1d9b352e3f4d956fdc9f5079bbf89c7e4138a05521ac6772ebe57e`.

This is an equivalence of open finite-word statements. It is not the
free-partner height converse of GC2243, a safety statement for arbitrary
boundary drivers, or an equivalence to a fixed-centre prize assertion.

## Forward direction: the unproved step is exactly D3

The proved short-extension theorem says: if u is safe and returns after8,
v has length at most3, and u++v is safe, then u++v returns after8. Its proof
does not assume that the extension has period8.

The mechanism is explicit in RootShortExtensionCore and RootShortExtension.
Acceptance of u in the existing thirteen-state reader gives a returning
eight-profile history. The phase7-to0 wrap is justified by the profile's
return equation. Spatial induction then transports the actual driven
history and the all-time newest safety through u. At its end there are15
possible accepted profile pairs. For each, the15 words of length0–3 are
covered by an exact finite certificate: either the extension returns after8,
or an explicit later pair is white. All-time safety rejects the second
alternative. The helper's empty-tail default uses the supplied previous
history, so dropping the last cell in this induction does not silently
change the observed trace.

RootD3Reduction now applies strong induction on the actual word length.
All words of length at most3 return after8, by the finite base certificate.
A leading white cell can be removed because evolution(false::xs) equals
false::evolution(xs) at every time. This preserves both safety and return;
it is not permission to remove an arbitrary older prefix. For a longer
word beginning black, D3 supplies u++v with u safe and1<=length(v)<=3.
Induction gives return8 for the strictly shorter u. The proved extension
theorem supplies return8 for the full word.

Thus the proof does not hide a periodicity premise in D3, and does not
establish D3 by invoking the desired return conclusion.

## Reverse direction: why the normalization matters

CedarSafetyBridge's exact existing equivalence is

```
Safe(xs) AND evolution(8,xs)=xs  iff  accepted(read(0,xs)).
```

Safe alone is not placed on its left. Assuming ReturnComplete makes a safe
word accepted. After reading its first black cell, the automaton is at
positive state1. Positive states stay in1..12, never returning to the
leading-white state0.

The finite table then supplies an accepted prefix within three cells of
any sufficiently long accepted word. Its carrying certificate can be
checked directly: accepting states are1,2,3,4,5,12. The other positive
states are6,7,8,9,10,11. States6,7,8 move to9 or10;9 and10 move either to
accepting12 or dead11;11 remains dead. Consequently a three-step path ending
accepted must have been accepted at one of its first three vertices.
Induction transports this terminal observation through an arbitrary word.
The accepted prefix is safe by the sound language bridge, giving D3.

State0 cannot be included in that terminal certificate: the three letters
001 lead from0 to accepting1, while the preceding states are all0 and
unaccepted. This explains the first-black normalization; it is not a
cosmetic restriction.

## A retained exact control against replacing all-time safety

The accepted prefix u=100001 reaches profile-pair state20 of the soundness
certificate. Appending v=0 gives the genuine finite-white word1000010.
The author's case_20_1 proves its newest trace at times0 through12 to be

```
0 1 0 1 1 0 1 0 1 0 1 0 0.
```

It has no adjacent whites in the eight transitions checked by EightWindow,
but fails safety at times11–12 and does not return at8. This is an explicit
known certificate branch, inspected here; no new trajectory was run. The
whole-word return premise in safe_iff_window_of_return8 is essential.
This unsafe word is not a D3 counterexample.

## Retained validation and its limits

The following exact source-bound author reports equal their raw checker
JSON. They import the required statement module, use the unchanged checker
`b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905`
at kit pin`5473ffd075f63c9d626e63b8455805d4831b39ca`, and report partial pass,
full replay, no new axioms and only standard axioms in all20 headlines.

| Module | Replayed | Declared | Headlines |
|---|---:|---:|---:|
| CedarSafetySoundness | 137 | 89 | 1 |
| CedarSafetySemantics | 75 | 36 | 1 |
| CedarSafetyBridge | 8 | 8 | 1 |
| CedarWhiteTransport | 18 | 14 | 2 |
| RootShortExtensionCore | 36 | 22 | 3 |
| RootShortExtensionCases | 232 | 231 | 2 |
| RootShortExtensionCertificate | 1 | 1 | 1 |
| RootShortExtension | 4 | 4 | 2 |
| RootD3Reduction | 10 | 6 | 3 |
| CedarD3Converse | 8 | 6 | 4 |
| Total | 529 | 417 | 20 |

The first nine modules are the author's521-declaration checkpoint. The
converse later reuses its own exact source/compiled dependencies and adds8
freshly replayed declarations; this is not a single new529-declaration run.
The dependency source and compiled hashes agree across the retained records.
The225 case headers cover exactly15 accepted profile states times15 short
words. Their exhaustive dispatch and proof schema were inspected;113
branches return at8 and112 give an explicit unsafe pair, with latest
displayed pair starting at20. Those are classifications of saved proof
branches, not fresh measured trajectories. Their kernel reduction is the
author's retained evidence. No GPT compile, backend verification or portal
status change is asserted.

All ten author guards report exit0/no stop, with300wall seconds,8GiB owned
RSS,2GiB available and0.1second sampling. RootD3Reduction records5.4659550s
and1373143040bytes peak owned RSS; CedarD3Converse records5.4283327s and
1373413376bytes. These are author-host measurements. The guard source does
not enforce aggregate CPU, disk/output, swap or thermal limits, and raw
periodic sample series are absent. No such enforcement is inferred.

Selected packet `cited/gc2248-d3-review/review-manifest.json`, SHA256
`54aafa9405ca1bb18e8714dcf2ee4721d022e5fbee8ac7cc97feceea7c007096`:
60payloads560697bytes plus manifest. Original manifests, selected exact
sources, raw reports/logs/guards and the source/evidence audit are retained.
This does not claim an audit of every file in both parent archives.

## Disposition and next executable step

**Record/source comparison:** GC2232 already carried the safe-return language
bridge for the finite eight-return review; these dependency bytes match.
GC2237's reset witness and GC2239's transition-cover control already explain
why a locally valid strip or an arbitrary supplied driver does not establish
finite-white ancestry. The current kit932cf8dd and04:53:47Z portal/PR index
were searched during this block; the exact linked fork sources above are
the carrying prior art, beyond the index's coverage. This is recovery and
review of existing results, with no additionality claim or new literature
theorem imported.

The reduction identifies a precise remaining obstruction: if D3 fails,
there is a safe normalized word with no safe prefix among its three immediate
predecessor widths. Treating those three failures at unrelated times as
one simultaneous local failure is unjustified. The finite certificate only
handles an already-safe returning prefix; it does not create that prefix.

Next inspect the known D/three-unsafe-predecessor record for an existing
joint-time invariant before attempting such an argument. A useful next
hand step must either specify a genuine joint-time identity for those three
unsafe traces or identify the exact existing obstruction and park it.
Independent alternative: compare a proposed guarded run-count formal
wrapper with actual kit inp_least_period/S_rule before writing redundant
formalization. No new width/clock census or compile is queued.


## GC2249: the free-boundary obstruction survives simultaneous failure

The earlier hand-D route is a different statement. L1038/GC1994 in
[the hand record](rule30-disappearing-words-hand.md) concerns alternating-wall
two-tick reset gaps4,3 forcing the patch000100111. Its finite audit is already
complete, and its repeated hand expansion is parked. D3 instead concerns
finite-white moving-frame safe prefixes. Neither result can be transferred
merely because both were called D.

The existing free-strip witness at immutable0cbc49ef gives a stronger
objection to a local D3 argument than unrelated unsafe times. Its
[exact JSON](https://github.com/Troyusrex2/Rule30PrizeKit/blob/0cbc49ef30888b32760def46ec31f954626192ff/research/agent-experiments/coordinator/20261026-height-and-cylinder/work/diagnostics/free_strip_safety.json)
(SHA2563bcc3f601b9652f41cc4918c9a758af3f543ac889ce957b73dd690eb18d3f0c4)
has width10 and period32, with its two oldest columns freely supplied.
The newest trace is safe and has least period32, while its three immediate
predecessor columns6,7,8 are all white at phases14 and15. Thus even a common
unsafe time for all three predecessors is compatible with every interior
Rule30 equation and a safe newest trace.

Rephasing at phase1 gives the normalized older-first row1000000111. A first
black cell at the initial time and a dyadic temporal period therefore do
not rescue this free-boundary implication. The missing condition is real:
from phase1 to2 both oldest columns should become1 under the literal white
boundary but instead become0. This is **not** a finite-white counterexample
to D3Star or ReturnComplete.

A fixed retained-data audit, with prediction/counterfactual written before
inspection, checked all256 interior equations against an independent
eight-entry truth table, the supplied newest trace, its cyclic safety and
least period, the common white pair and these two boundary violations.
It passed. No search, new trajectory or larger horizon was run. The result
is a known witness specialized to the proposed inference, not a novelty
claim. Shared-store packet `cited/gc2249-d3-strip/manifest.json`, SHA256
`497880d893ed20541b9f81b3c9ac3ee858d75b0b784661bf7465dc38a4193926`,
holds three payloads4741bytes plus manifest, four verified raw uploads.

**Disposition:** park local simultaneous-event/finite-strip D3 shortcuts.
Reopen only with a genuinely white-boundary-history or jointly rooted law,
not more ancestor layers or more strip samples. The D3 equivalence remains
useful and open.

The independent formal-wrapper check also has a scoped disposition: actual
kit Rule30RightPeriods.inp_period/inp_least_period/inp_no_smaller_period and
S_rule already supply the root-specific input-period and parity conclusion.
GC2238's arbitrary coupled-fragment shape statement is broader and is not
literally subsumed; its Boolean inverse already has the GC2241 development
check. An extra generic shift-equivariance wrapper has no concrete delivery
need now. Do not launch a redundant build while independent review remains
pending.

**Next pull:** carry PR52's exact arbitrary-future gate-past closing and
conditional unbounded reduction. What would a compression theorem actually
need to preserve? Its finite7-bit covers must be kept distinct from closing
for every past length. Exact current head64003389e169db91b80a17b60670afb2eb22b87f
and all three discussion channels were freshly read at metadata level;
source/evidence carrying review is the next work, not yet accepted.
