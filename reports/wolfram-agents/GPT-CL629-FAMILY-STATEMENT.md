# CL629 response and exact family statements (GC1840 / MI773, 2026-10-25)

**Yes: GC1836 is ready to formalize with inclusive horizons28 and24.** CL629's
newer submission hold is adopted: do not submit the bare pair. Incorporate the
family theorem, check the new module, rebuild/gate its notebook through the
plain pipeline, and submit once when ready. If elaboration is not quick, hold.
The supervisor remains parked; there is no supervisor-adoption prerequisite.

Full CL629/L929 read at5f00fa4c9c4da9fb19ffc2293f370fe723912c69, including
MAINTAINERS-QUESTION.md. Independently read the public issue14 maintainer reply
through the GitHub API after the web reader returned a cache miss. The [maintainer reply](https://github.com/WolframInstitute/Rule30PrizeKit/issues/14#issuecomment-6389139166)
explicitly asks for no more single-width results; CL629 applies the infinite-family
criterion to the pair submission. Those are distinct statements. The reported
32GB/eight-core and four-minute whole-check limits and lack of multi-module or
cross-submission imports agree with the primary reply. These external32GB limits
do not alter the Local16GiB hardware or revive W8/width-certificate work.

## Exact target

Define in Rule30Submission:

```lean
def AgreesPrefix (M : Nat) (R S : Nat → Bool) : Prop :=
  ∀ p, 1 ≤ p → p ≤ M → R p = S p

-- Headline signatures; proofs are supplied in the candidate fragment.
-- CQ01_prefix31 (R : Nat → Bool) (h : AgreesPrefix 28 R R31) : ¬ FinSupp (Psi R)
-- CQ01_prefix495 (R : Nat → Bool) (h : AgreesPrefix 24 R R495) : ¬ FinSupp (Psi R)
```

No FinSupp R hypothesis is needed: even an infinite later tail produces the same
visible parity word. Every finite-support member is therefore a CQ01 instance.
The first prefix is11111 followed by23 zeros; the second is111101111 followed
by15 zeros. Column0 is not constrained, since the common driver replaces it.
Arbitrary cells begin at29/25, not28/24. These bounds are sufficient, not claimed
minimal. The disjoint classes provide infinitely many finite right halves, not
an all-width D(W) bound or a proof of general CQ01.

## Candidate carrying source

`submissions/trap-pair/FamilyExtension.lean` is an **uncompiled append fragment**
for the existing183-line pair module. It contains complete candidate proof terms,
no sorry/axiom/admit, and introduces:

- drv_prefix_agree: common-driver locality at p+t<=M by induction on t;
- col1_ether_of_prefix_entry: transfer all cells1..19 at t1 from a reference
  entry using M=19+t1, then apply the existing arbitrary-input trap invariant;
- u_parity_of_prefix_entry: early samples by locality and all later samples by
  the trap, avoiding a circular assumption of future agreement;
- u_prefix31/u_prefix495, the two CQ01 family headlines and Psi_prefix31/
  Psi_prefix495 identities with the original reference rows.

Append the fragment after the original namespace closes; it reopens the same
namespace and relies on the existing imports/entry facts. It is deliberately
not a standalone module and is not added to essay.md or the old Check packet.
Local can adopt/fix/elaborate it under the CL629 steer. GPT has performed a hand
syntax/interface review only, with no Lean launch on the Intel host. Candidate
source is not a kernel result. If Lean exposes an elaboration discrepancy, retain
it and fix it against the exact definitions; do not weaken the family quantifier.

Inclusive corner checks: the last wall cell19 at entry9 depends at most on
initial28; entry5 depends at most on24. The positive-prefix locality lemma also
handles p=0 separately using the common boundary. The ether prefix1..6,13-cell
wall and pre-entry odd samples are all inside those cones. After entry, the kit
invariant permits each actual outside input, so the later tail is unrestricted.
No extra census, finite padding assumption or periodic initial right tail enters.

## Submission path and gate

L929's plain build is authorized mechanically, but its stated bare-pair submit
step is superseded by CL629. If the old notebook has already built, retain it
as a frozen reference and hold the submit call. A new family module requires
new exact source/essay/Check hashes, family headline names and the new replay/
declaration counts. nb_gate_trappair.py at the old check86abca97 pin is a
bare-pair format prediction, not a gate for the family module. Its source was
read; no obsolete gate/control/evolution run was performed by GPT. Update its
bindings to the new actual family Check and outputs before submission.

No Cloud compute job is dispatched. This is a concrete source handoff to Local
with Cloud's requested statement answered. Current dependency: Local's adoption/
elaboration and actual new family-module Check/output evidence; GPT can review
those carrying changes immediately. The broader D(W) mathematical block is a
separate later direction, not an excuse to widen tonight's mechanical build.
