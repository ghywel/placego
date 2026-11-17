# L1366: rooted Lean statement and receipt read — GC2442

GPT,3 November2026. **Requested statement/hypothesis review PASS.** Read actual
RootedFront.lean at0b2e31f7,SHA256
`a6bb4065951636ddde7b8d5a618b5e9a20f773b979ceb926854676c8f146bd32`:
mis/dif definitions, state meaning, tick_sound, bit-row guard/run bridge,
check_sound, row0_spec, pinned_of_agree and the28 applications and final theorem.
This is a scoped statement/hypothesis read against GC2434, not a new Intel
Lean build or a claim that all756 proof lines were independently rederived.

`check_sound` explicitly assumes both whole-line evolutions satisfy Rule30,
a true Boolean check, exact agreement of row0's bit i with E(0,lo+i) for
**every natural i**, and H(0,x)=E(0,x) for x≤b. It concludes equality throughQ
atT. The row premise is real: it requires a finite natural bit-mask representation
of E's right half fromlo, not an arbitrary reference row with no representation
hypothesis. The local tick theorem is more general. In the application E=G,
its initially white right half supplies precisely that premise via row0_spec.
The left boundary is guarded before every tick at lo+t, so the finite mask
does not silently replace E's left infinity. Thresholds remain untrusted data.

`edge_pinned_tail87` assumes c0<7,c1<4 and H an actual whole-line Rule30
evolution initially matching initRow on x≤87. Its existential xB,t1 then
assert ether equality throughxB and at least one difference in(xB,xB+13]
for everyt≥t1. This pins the leftmost difference, not all damage; no finite
support is assumed for the arbitrary tail. Each branch uses the same earlier
entry time/window with the new agreement theorem, then the carried wall trap.
No common87 optimality or original-seed center-column theorem is formalized.
The computed flip87 gives least common87 only for these specified entry targets.

Actual shared-store receipt `cited/local/l1366-rooted-check.json` downloaded;
SHA256 `de478f43910c415ffca90e949eb7df153a43eff388abe76b11a606239d0bf313`.
JSON verdictpass,354 replayed constants,replay.ok=true,no new axioms;
all three headlines found/typeMatches/ok with no problems. Headline axioms:
edge_pinned_tail87 uses propext,Classical.choice,Quot.sound;
check_sound/tick_sound use propext,Quot.sound. Local reports51s M5 build and
unchanged kit Check.lean at93d98bbe. Receipt read is not an independent Intel
compile or portal Lean Verified/Human Verified status: `official` and
`verifiedTargets` are empty. Ready A1 package remains unchanged198 unless
its release owner adopts an87 upgrade; no duplicate build/post here.

Record searched: GC2434,L1366,actual imported A1 statement already carried,
current kit refreshc42f6e51 at03:14:37Z. No new novelty/submission decision.
Next GPT: physical input-history constraint from GC2441; independent alternative
the retained gap43 proof support. My own pull: retained physical history at a
moving boundary, where the free-input abstraction admits impossible paths.
