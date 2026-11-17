# A3 exact countdown and closing law: carrying review — GC2509/2510

GPT, 3 November 2026. **Mathematical/source fidelity PASS, hand/two-party.**
Read the complete L1406 source, then every L1408 addition, the complete
scalar replay source and all output. Also read the actual current kit
GateClocks/DifferenceOrder declarations and the relevant proofs, the
GC2008/GC2201/GC2205 carrying arguments, and the scoped public sources
listed below. No Intel compile or replay was run. Local reports a
Lean4.35 local compile; an unchanged official Check run and public
verification are separate, still outstanding in the reviewed record.

## 1. Exact artifact and scope

Final reviewed source: tests/probes/lean/ClosingLaw.lean,310lines,
SHA256 `cdf38552686f5a5ebc1c5b96d4016da100600b4bf26c76db2e988091d9c68548`.
The earlier236-line source was
`bfa4373878e383a6406c0895c2b578ffe843150924056cf4491db59a197744d1`.
The changed74lines were read, not assumed identical.

It imports Rule30GateClocks on kit main
`c42f6e5133f61a47e99289fd4b6e0536fd8a0453`.
The gates may vary with spatial depth, but are fixed in time. Seeds
x:Nat→Bool may be finite or infinite. Missing lower-index bits are
white. This is a triangular edge-clock theorem; no centre-column,
universal-capture or prize conclusion follows.

`Quadratic g` means `deriv g true != deriv g false`, where
`deriv g s = g(true,s) XOR g(false,s)` is the derivative in the FIRST,
newer input b. Thus the derivative is s or its complement. Equivalently
g(b,s)=b*s XOR alpha*b XOR beta*s XOR gamma over binary arithmetic.
It selects the eight gates with nonzero mixed coefficient, including
OR, AND, NAND and NOR. It does not cover every one of the16 Boolean
gates. This matches the older quadratic transfer convention.

The source uses g(k+1) to update col(k+2) from newer col(k+1) and older
col(k). That agrees with kit gateClock.gate j=g(j+1). No supplier or
spatial gate index is reversed.

## 2. The exact countdown carries, with its cap guard

Write M=2^v. The imported hypotheses give source s periodM, supplier b
antiperiodM and h(t+1)=h(t) XOR g(b(t),s(t)). The exact derivative
identity is

`Delta^(M+1)h = deriv(g)(s)`.

For a quadratic gate, taking at least one further difference removes
the optional complement. The draft proves precisely
`Delta^(M+k+2)h=Delta^(k+1)s`, for k>=0. This is the exact transfer
needed for the reverse countdown, rather than only a vanishing bound.

The kit's order is capped: order(s,M) is the largest r<=M−1 with
Delta^(M−r)s=0. Constants have orderM−1. The new theorem assumes
v>=1, h period2M, and

`order(s,M)+1<M`.

It concludes

`order(h,2M)+1=order(s,M)`.

The proof supplies the missing inequality and combines it with the
kit's existing order_countdown_gate. Its use of le_order_iff keeps
positive r, r<=L−1 and natural subtraction bounds explicit. The case
order(h)=0 is handled by order_pos_of_period; the positive case applies
the exact difference identity at its computed offset. The M=2 case
is not silently handled by underflow. These steps carry by hand.

The constant guard is essential. For M=2, s identicallytrue, any
anti2 supplier b, OR gate and alternating h, all period/recurrence
conditions hold. But order(s,2)=1 and order(h,4)=2, so the purported
unguarded equality would read3=1. The displayed guard excludes it.

Quadratic is also essential. With M=4, affine gate g(b,s)=b,
s alternating, b=00001111 repeated and h its running XOR, h has
period8. Here source order2 and output order2 would give the false
3=2 countdown. The gate derivative is constant, failing Quadratic.
These are hand adversarial controls, not new simulations.

## 3. Prefix orders and the closing indices match GC2201

Let E(j)=prefixExp(g,x,j), and define flag f(j)=E(j+1)−E(j).
It is always0 or1. Then the theorem's assumptions say exactly

`f(n)=1`,
`f(n+1+2i)=1, f(n+2+2i)=0` for0<=i<m,
`f(n+1+2m)=1`.

Thus the assumed word is1(10)^m1, and the next flag is f(n+2m+2).
Put q0=2^E(n), the prefix period BEFORE its first1. The conclusion is

`m+1<=q0`,
`f(n+2m+2)=1 iff m+1=q0`.

This is GC2201/GC2205's convention, not the period after the initial
11. In the literal OR edge embedding D_j=col(j+1), the old physical
prefix period Q_j is2^E(j+1), and the old flag x_j is f(j). Hence
n=s in GC2201 and q0=Q_(s−1), with no one-column offset hidden.

At the start, antiperiodicity gives order(col(n+1),2q0)=q0−1.
After i completed10pairs, closing_run proves

`E(n+1+2i)=E(n)+1+i`,
`order(col(n+1+2i),2^E(n+1+2i))+i=q0−1`.

Every induction step has source periodM and output period2M from
WHOLE-prefix clocks. No individual-period nonloss is used. The
nonconstant guard is preserved because the source order plus1 is
at mostq0, strictly below M=2^(E(n)+1+i). The terminal iff uses
reset-before for necessity and order_pos_of_period plus the two
prefix extension cases for sufficiency. This carries the crucial
step, including m=0.

It remains conditional on the stated1(10)^m1 history. It does not
say every alternating run must reach that length, or that every
arithmetically permitted length is realized by some seed.

## 4. Word consequences and small-exponent controls

`no_1101011` is correctly the m=2 consequence: a closing1 would
require q0=3, impossible for a dyadic prefix period. It concerns growth
flags, not a physical spatial or temporal colour word.

The L1408 additions are faithful:

- no_three_at requires E>=1 and excludes111 by m=0.
- no_11011_at requires E>=2 and excludes11011 by m=1.
- five_letter requires E>=2 and gives E(n+5)<=E(n)+3.

The five-letter proof uses the five exact0/1 extension choices and
excludes triples at the three possible starts plus11011. A five-bit
word with at least four1s contains111 or is11011. The32-branch
calculation therefore expresses this elementary finite implication;
it adds no unstated seed premise.

The guards are real. For the NOR family at the all-white seed,
the first bit toggles; the force on the second bit has odd parity
over2ticks, and the third bit's NOR force is1 once over the4tick
prefix cycle. The first three prefix flags are111, starting E=0.
So the quadratic family has no unconditional111 ban. Rule30's OR
boundary is different; an OR-only boundary corollary needs its own
argument rather than dropping the exponent guard in the generic one.

Likewise the recorded single-cell OR flags0101101101... contain
11011 starting at n=3 with E(3)=1. That five-letter window has four
doublings, so five_letter's E>=2 cannot be weakened to E>=1.
The phrase "11011 only at the universal start" should be stated in
release prose at the proved scale q0=2 unless a further position
classification is supplied. The audited theorem itself has the
correct scale guard.

This local five-letter statement does not improve the kit's known
asymptotic half-rate bound. Its purpose is an exact finite-word
restriction and a reusable formal closing law.

## 5. Replay read and evidence states

Final replay source SHA256
`f3d4267c6f3910c9335e7f9ca0fdb05dff86343bb4b850aaab50611e6cf4105e`;
output SHA256
`3f95acf2a3d6c1833df4e18a5216b15caedcbba8d2dd8207f7c5169891830782`.

The simulator matches OR's white lower boundary and gate-clock column
indexing. It checks EVERY admitted m at each start, including m=0,
and checks either nextflag, rather than only maximal alternating runs.
The final output reports5 single-seed occurrences,2153 occurrences on
400 random seeds, and4743 five-letter windows on a separate sample
(single seed plus399 random seeds), all without violations. These
are finite M5 computations read here, not an Intel replay or proofs
for all quadratic gates. The proof of that family is the Lean source
and its hand carrying argument. The random loop uses22flags even if
one changes the CLI J argument; the reported configuration is22, so
this is not a defect in the stated run.

Local's reported compile/no-sorry/standard-axiom result is credited
to Local. The source contains the corresponding #print axioms calls,
but no raw compiler transcript was independently replayed here. The
official Check tool, release essay/notebook, source embed and public
receipt have not been supplied in this review. Hand acceptance,
local compilation and public Lean Verified remain separate states.

## 6. Prior art and public carrying-source comparison

Known hand mechanism: GC2008/L1195 exact Newton countdown and
GC2197/GC2201/GC2205/CL645 closing composition. The OR no11011
corollary is ALREADY formalized in Lowry's
[PR55](https://github.com/WolframInstitute/Rule30PrizeKit/pull/55),
head918284e3b0097b7a6e896d56506f86a1cc813128, with E>=2 and prefix
periods. Read the actual no_11011 statement/proof and the prefix-bound
countdown application. The latter uses the existing inequality, not
the all-m exact-closing theorem proved here.

The fresh closed
[PR51 discussion](https://github.com/WolframInstitute/Rule30PrizeKit/pull/51)
was read, including the linked single-cell and arbitrary-seed bridges;
PR51 and PR55 review-summary lists were empty at the read. The fresh PR55
conversation was also read: its current maintainer reply asks for the
unbounded analytic modules, omits the clock32 certificate pool and
notes the data-module compile limit. That is relevant catalog guidance,
not acceptance of this new package or a changed A1 verdict. Exact linked
proof sources were fetched at their frozen commits and relevant
carrying portions read:

- ba4913a90bda28a1ce8f4c17e8b7a5f5110d9845,
  [Rule30RightProfileSeed.lean](https://github.com/Troyusrex2/Rule30PrizeKit/blob/ba4913a90bda28a1ce8f4c17e8b7a5f5110d9845/research/right-profile-seed/seed-bridge-replay/sources/Ruliology/CellularAutomata/Rule30RightProfileSeed.lean), SHA
  e3f30d05550184aa4f3878625f8004580726976c8e5ca3d422ee5f8e5f4084bb.
- e1ff89b9cd0059082ea0126e35414dc8a4a11d9c,
  [archived Rule30RightPrefixClock.lean](https://github.com/Troyusrex2/Rule30PrizeKit/blob/e1ff89b9cd0059082ea0126e35414dc8a4a11d9c/research/right-prefix-clock/clock-replay/sources/Ruliology/CellularAutomata/Rule30RightPrefixClock.lean), SHA
  2b74c47ffc22f6f7cf8ad9c912ab389cffb182db4137ca2571590c961c35a2c6;
  [archived Rule30RightPrefixBound.lean](https://github.com/Troyusrex2/Rule30PrizeKit/blob/e1ff89b9cd0059082ea0126e35414dc8a4a11d9c/research/right-prefix-clock/bound-replay/sources/Ruliology/CellularAutomata/Rule30RightPrefixBound.lean), SHA
  67cf1bb230eaf01631d757ce05c88a44473ebbe4ba1d5f6dc5e4ac6efe408c4e.

These provide existing OR prefix bridges and the reused inequality
accounting. They prevent the broad claim "formalized nowhere" from
following merely from an indexed name search. This is a scoped source
comparison, not a complete audit of every linked archive or source of
priority clearance. Rowland2006 section5 is the already listed related
literature; no new full-paper audit or novelty conclusion is claimed.

Imported current main hashes: GateClocks
`f3ef8a0aa8c3af7f08fd7567cc6931e37a0c66ee88f2f59ee9cc198e343c733c`,
DifferenceOrder
`96f50d141b6631838fe61caf0d81a56a36bb89e171e21d3fea926cdd8f271224`.
Actual PR55 prefix-clock source hash
`df313348868140e2b7f0a3f87df075e65baa2fe53c60fdb4bf97aee77512f43b`;
prefix-bound source
`8b7e3e1a37ac77d92ca86a1c7d71dad3c03ff81a348edd94819aa5e19b714840`.
Last complete external index remains10:21:10Z; the fresh PR discussion
reads above do not reset that complete timestamp. No submission or
novelty decision is made in this review.

## 7. Verdict and executable handoff

The final cdf38552 source is faithful and its crucial mathematics
carries. No source correction is required by this review. Keep its
Quadratic, time-independent-gate and exponent/order guards in all
release statements. Cite known OR no11011 and the reused hand/source
machinery. Do not advertise unconditional generic111 exclusion,
individual-period monotonicity, new asymptotic rate or occurrence of
every allowed closing length.

Local remains the formalization/posting owner. Next executable steps:
run the unchanged official checker on the final module and chosen
headlines; retain exact source/toolchain/check output; prepare the
reviewable essay/abstract and source embedding with these scopes.
Posting still requires those checks and the current owner instructions;
this hand review introduces no additional routine permission round.
No duplicate build, public message or posting was done by GPT.

My own pull: the eight-gate formulation makes the algebraic mechanism
clearer than an OR-only corollary, provided its genuine small-clock
exception remains visible.

## 8. L1411 concrete portal source — GC2513, 11:40Z

Read the complete assembler, package README and portal source. Portal form
`reports/wolfram-agents/submissions/closing-law/Rule30Submission.lean`,
331 lines, SHA256
`10812b8961b062c98656c12a1be52a87c44269ae60e22096311a405dd5c69a94`.
After separating imports, namespace, header and open context, its declarations
and proofs match the reviewed cdf38552 source byte for byte (outer whitespace
apart). The added statement-module import and fully qualified open context
are explicit; this is not a claim that the complete files are identical.
The header preserves the order guard and says q0=2 for the 11011 exception.
**Concrete mathematical source fidelity PASS.** No Intel compilation performed.

Local L1411 reports unchanged Check on verifier kit
`93d98bbe049177d2c1546b6b0714aa33703ae13d`: replay97 constants, five headlines,
standard axioms only; build0.6s. The README pins raw output
`fdf966cf9cc280b2a7af14943593172dab91c5f8c07058a5d670ee147e9bda17`.
That output has not yet been read by GPT. A shared-store pointer was requested
without requesting a rebuild. A sandboxed fresh listing failed DNS resolution; an approved network listing
then succeeded, without an authentication failure or certificate bypass. The raw
receipt pointer is still absent from the freshly listed flags. Thus Local's checker
report, GPT's source review, and GPT's receipt inspection remain distinct.

Essay, abstract and notebook remain unfinished in the committed packet.
This is not a submission-ready verdict. Local owns completion; GPT's next
delivery read is the retained raw receipt plus the actual completed packet.
The last GPT complete external refresh remains10:21:10Z. L1412 reports a newer
refresh; it is not represented here as a new GPT source audit.


## 9. L1413 actual essay packet — GC2516, 11:47Z

Read the complete104-line prose, abstract,67-line assembler and95-line release
notebook driver. The complete appended formal section was read through its
assembler; the embedded331-line source was verified BYTE-EXACT against10812b89.
Essay f1a7dad684a8ea0958bf1abf4dfe3ae5104baccd2ac0f9d728f9f6ad8595a039;
prose cfa9c4df01e95272c7beaae7aae77b61de7d819bf3333f043613ee19eafc9a6d;
abstract4677ae62683d772560ea6f9bbd8794b339361085c9f8b91e44adbb2f11695a6e.
Prior-art paragraph credits PR55 and the kit's inequality correctly; no new
whole-literature priority clearance is inferred. **Lean-source embed PASS.**

Two substantive prose corrections before release:

1. The abstract/description/countdown section say that one non-doubling step
   lowers order exactly one. That is not a theorem about arbitrary00 steps.
   State the actual geometry: older input s is M-periodic, newer input b is
   antiperiodic at M, h integrates g(b,s) and keeps period2M, M>=2, and
   order(s,M)+1<M. In the closing-law application this is the10 pair.
   The kit gives source order<=output order+1 (drop AT MOST one); the new
   reverse inequality gives equality. Keep that direction. Replace "the only
   guard" by the actual assumptions rather than suppressing the antiperiod
   and output-period hypotheses. The polynomial description of order should
   also mention its cap at M-1, particularly for the zero polynomial.
2. The picture says "The single cell's letters close with a doubling only
   once". Its computation covers22 letters. Say "In this displayed22-letter
   prefix, the run closes with a doubling only once, at q0=2." The formal
   all-m theorem does not exclude later longer closing runs.

Also make the abstract's "after a doubling at period q0" explicitly mean
"with period q0 BEFORE the first doubling", as the main statement already
correctly does. These are prose/source-header clarifications; no mathematical
proof change or new search is requested. Local owns the pinned reassembly.

The release driver checks the expected7 outputs, environment, standard-axiom
sets, source icon and97-declaration KernelChecked object. Its source was read;
Local's24s RESULT OK/notebook2509ad98 remains a reported result until the
notebook and raw summary/output receipts are available for GPT to inspect.
A fresh workers/local listing has no closing-law receipt pointer; the
addressed L1413 flag is read. Requested checker and notebook receipt pointers,
not a new build. No public receipt/Lean Verified claim exists for this packet.

Verdict: mathematical source and embedding PASS; final release prose needs
these repairs and retained receipt inspection remains open. A3 is not yet
cleared for posting by this packet read. No additional permission gate is
introduced. Both schedules remain active; GPT continues B2 independently.


## 10. L1414–1416 retained receipt read — GC2518

L1414 repaired passages/abstract/assembler/driver read in full. The main
countdown section now includes M>=2, s periodM, b antiperiodM, h period2M,
recurrence and source-order guard; the picture's only-once claim is now
explicitly limited to22letters. q0 is BEFOREfirstdoubling. Source10812b89
is unchanged and the repaired essay embeds it byte-exactly.

Downloaded immutable `cited/l1414-closing-law/a3-receipts-l1414.tar.gz`,
25555bytes, SHA256
`8c518ed016b6cbafac92f231c9956c80de704e0cd0a3b11fd1f862cda68388f5`.
Safe regular-file extraction only; every MANIFEST hash verified. Read the
ENTIRE raw Check output, seven output cells, summary JSON/raw WL, DONE,
manifest and time receipt. Actual notebook text read by a literal path scan;
notebook/proof-source pins and current essay/driver hashes verified.
No Intel build/replay is claimed.

Raw Check fdf966cf verdictPASS:97replayed constants, no new axioms, imported
statements, all five headlines found/type-matched/ok,18declared items on
standard axioms. The deprecated replay API warning is retained, not a kernel
error. The notebook's17visible constants exclude a generated auxiliary;
the97declaration kernel replay is the relevant replay count, not17.

Rebuilt notebook SHA256
`8247707432f45ffabb4b41867a02f41ed64337d7b500c3745438435ff1d9f169`,
107083bytes. Seven outputs read: exact22letters/five-run table, True kit
cell, LeanEnvironment, all five complete headline types, standard-axiom
sets, Quadratic term and the actual KernelChecked97 object. Summary pins
current essaycda79713 and driver1591a3c5; reasons empty, zero MESSAGE CELLS.
The handler recorded15165events, so this is not a claim of zero handler
events. Internal build19.8s; outer time30.83s, user22.50/sys1.97, maxRSS
1332920320bytes on Local. This is receipt inspection, not an independent
stage-wide resource-monitor audit. No literal local path patterns from
usual user/temp/application roots were found in the released notebook.

**Receipt/source/embed inspection PASS.** Two remaining literal wording
fixes were sent immediately through the review flag, without another
permission request:

- Change "the equality fails there" for constant streams to "the equality
  CAN fail there". Countercontrol: M2,s=false,OR,b=0011,h=0001 satisfies
  the other recurrence/period assumptions and has sourceorder1, outputorder0,
  so the equality actually HOLDS despite the excluded constant source. The
  true-constant counterexample in §2 shows it is not universally guaranteed.
- The abstract's "under the periods that pair carries" must also mention
  the nonconstant-source guard; the Description should say "under the
  stated hypotheses". Those guards are already correct in the main prose
  and Lean source. Local owns the minimal pinned prose repair/rebuild.

L1415 and L1416 complete owner instructions read: Local is authorized to
post to the PORTAL after the review passes, then open the KIT PR citing
that receipt. No fresh owner permission is required. The code/checker gates
are clear; final prose repair/rebuilt artifact pin remains the only current
packet issue. No public A3receipt or public-verifier status is invented.


### L1417 outcome: final prose PASS; current notebook rebuild blocked by licence

L1417 complete entry and ALL changed prose/abstract/assembler pins read.
Both final wording repairs are applied. Current prose
`faab16d44fb0973b7230393623662b862e37ec736af30daa34d2887ec4b71738`,
essay `274ed1c5e003db9b108e50fe1c9a3b86f2747f9f867d8f084ffb86f6609aeb96`,
abstract `d5d13b23295f81cee3e52a27fd8effc75b4850f4c0c432adffb48ec22db154b6`.
Exact unchanged source embed rechecked. **Final mathematical/prose review PASS.**

Local reports the new notebook rebuild fails immediately with a Wolfram
Engine activation/licence error, twice with preserved failures. The owner
has already been asked. No current-prose notebook exists yet; the previously
passed82477074 notebook belongs to the earliercda79713 essay and must not
be presented as the current rebuilt artifact. The portal submit step also
needs the licensed kernel. A3 therefore remains NOT POSTED. This is a
licence-dependent release obstruction, not a new proof or permission issue.

Full54-line kit-module generator read. Read-only reconstruction gives
`04d4e03191c4822407109806de2a6a986cc1abfe65e953940741b40a423d5076`,
matching Local's reported module; its declaration/proof body equals carried
cdf38552. No generator execution against a kit checkout or Intel build.
Local reports kit Check PASS97 and full Ruliology build199jobs; those raw
new kit receipts have not been independently inspected here. Local owns
portal post followed by kit PR, both owner-authorized L1415/L1416. Once the
licence is restored, the next gate is the exact current-essay rebuilt
notebook/receipts, then the authorized post and public receipt inspection.
No additional routine owner permission round is introduced by this review.


## 11. L1419 release and independent public verification — GC2523

L1419 complete outcome read: owner-authorized cleanup of stale Wolfram MCP
kernels restored the licence; Local rebuilt the exact274ed1c5 essay,
posted the portal package, and opened kit PR114. No GPT kernel cleanup,
Wolfram invocation, posting or external comment was performed.

Independent verified-TLS read of the official submissions JSON confirms
[the public A3 submission](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-20f058),
R30-20261103-20f058: **Lean Verified**, claim partial, submitted12:26Z,
checked12:27:09Z. Replay97constants/ok, fiveheadline names/typeMatches/ok,
nonewaxioms, standard axioms only; Lean4.35.0/verifier kit93d98bbe.
No official prize target is verified. The status carries no Human Verified
badge in this snapshot. The public extracted Lean is EXACTLY the reviewed
10812b89 source,18407bytes. Web rendering failed; the official JSON/file
API reads succeeded with certificate verification, not a substitute source.

Final immutable receipts `cited/l1414-closing-law/a3-receipts-l1419.tar.gz`,
SHA256 `68282ab04fe60426b44653ebf442af23c0145f103e92cddd7abda3cd78cd3299`,
were downloaded and every manifest entry hash-verified. The current essay/
updated driver pins match. Outputs1–6 are byte-identical to the fully read
L1414 receipts; output7 differs only in the fresh LeanLinkTmp module name,
whose actual KernelChecked97 object was read. Final summary reasons empty,
seven outputs, zeroMESSAGECELLS,15165handler events. Internal build27s;
outer receipt45.16wall/27.42user/2.60sys on Local, not an Intel measurement
or fresh stage-wide monitoring audit.

The ACTUAL public notebook was downloaded as well:107086bytes, SHA256
`4a87b0730f122b84e14e639438e979c259f43863bd9e194c61009defedd18d30`,
byte-identical to the final receipt notebook. Its literal local-path scan
passes. Thus source, completed prose, final notebook receipt and public
publication are now independently tied together; the old82477074 artifact
is superseded and is not used to claim this release passed.

[Kit PR114](https://github.com/WolframInstitute/Rule30PrizeKit/pull/114)
is OPEN, exact head `f76bf713b35f90cdc200c57ac0fa55ff9b16060b`.
Read current description, changed-file list, README/import diff and actual
module at that head; fetched SHA256
`04d4e03191c4822407109806de2a6a986cc1abfe65e953940741b40a423d5076`
matches the reviewed generator reconstruction and declaration/proof body.
Comments/reviews/check-rollup are empty in this snapshot. This is an open
contribution, not kit acceptance or merger. No new full-kit build was run.

Independent public receipt/source pins/metadata retained in
`cited/gpt/gc2523-a3-public-receipt-20261103.json`,47469bytes, SHA256
`d4a73f155aff218dd444f9112833b0c73f60583f980957773c1ee0e4b18c5d8d`.
This targeted public read does NOT reset the last COMPLETE global external
index timestamp11:50:45Z. Local owns PR follow-up and A4; A1 maintainer-WAIT
remains separate. No owner activation action is now required for A3.
