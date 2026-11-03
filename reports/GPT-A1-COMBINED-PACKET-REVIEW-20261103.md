# Combined A1 packet: scoped proof read and two scope fixes — GC2486

GPT, 3 November 2026. Response to Local L1390/4878d57f. **Lean-source
change PASS by comparison; prose needs the two precision fixes below.**
This is the requested scoped packet read against GC2434/GC2442, not an
Intel build, notebook check, or public verifier verdict. Local remains
the sole build/posting owner. No duplicate submission is created.

## What was read and checked

Read the full new186-line prose and245-word abstract, the complete source
diff, the actual check_sound/row0_spec/pinned_of_agree/tail87 bridge and
the essay assembler. The entry-source substitution is mechanical:
normalizing `by decide +kernel` to `by decide` and removing the old
`maxRecDepth` wrappers makes the ENTIRE module byte-identical to the
previous combined source. All28 checkEntry statements, data, observer
proofs, hypotheses and conclusions are unchanged. This agrees with the
earlier GC2434 soundness and GC2442 statement/hypothesis reviews.

The embedded Lean string in essay.md is byte-identical to the actual
module. Both assembler input pins match. SHA256 values read:

- module: `d583be068ba7e92ea8ad5a542f7af1db37306e1e1ea13ec704948e0ade2c9da4`;
- prose: `07602b5583ca6cfb2e36efa0d0aa076a7666f779e38b5ec71ce0ad27f9a6e2a2`;
- essay: `67eb29ff1ed91370a5b512aef3bf7ce4534fc18d7fba7f398271edb363e4e8ed`;
- abstract: `e0e18c38aa3c1950c7444640d60e97b94a7ae05e4e93a2ce1581af6cdb019ca9`.

The exact difference rule in the prose has the correct signs and mixed
term. Untrusted thresholds are correctly distinguished from the checked
run. The finite bit-mask hypothesis of check_sound is supplied by row0_spec
for the actual initially white reference right half; the final theorem
does not generalize that representation to arbitrary reference rows.
The left-front/window statement, the infinite family of arbitrary right
tails and the exclusion of a centre-column conclusion are correctly stated.

L1390 reports an official-check pass with522 constants and six headlines.
That is Local's receipt report here: I have not read the new522-constant
receipt itself or run a new checker. The planned notebook's nine outputs
and KernelChecked522 are still Local's pending gates in that entry.

## 1. Unbounded rightward damage applies to the original white right half

The Description ends with an unqualified statement that the difference
stays unbounded to the right after stating the arbitrary-tail extension.
That reading is false for arbitrary tails. Set H(0,x)=initRow(x) through87
and equal to the ether for x>87. Its initial difference from the ether
is confined to[0,87]. Finite propagation confines the difference at each
time t to[-t,87+t]. It still has the proved pinned LEFT front, but no
unbounded rightward difference at a fixed time.

Concrete replacement for that last Description clause:
“For the original white right half, differences extend arbitrarily far
to the right.” The corresponding body statement is already specifically
about the original white right half and can remain.

## 2. Sharp87 is an agreement cutoff for fixed targets

The single-flip comparison proves that agreement only through86 does not
guarantee the SAME reference values in the prescribed window at the
prescribed entry time. This is the GC2434/GC2442 guard. A changed window
is not by itself a proof that it is outside wallStates; the comparison
does not test wall-state membership. Nor does it exclude a different
entry or eventual pinning.

Replace the opening sharpness sentence with:
“For exact agreement with the reference trajectory at these entry-time
targets,87 is the least uniform initial cutoff.”

Use that same scope in the Description and prior-art bullet. In the
abstract a short replacement is:
“The cutoff is sharp for reference agreement at those entry times.”
This does not increase its245-word count. The existing final warning
about other entries is useful; make clear the witness tests reference
agreement, rather than wall-state membership or optimal eventual pinning.

No change to a Lean statement or proof is requested. After these prose
precision fixes, update pins, rebuild the source-embedded essay/notebook
and complete Local's existing checker/output/privacy gates. No additional
owner permission round or independent rebuild is requested by this review.

A2 posting R30-20261103-e660e4 is reported in L1390 under fresh explicit
owner authorization; this supersedes the previous voluntary hold. Its
reported queued/Lean Unverified status is not a public verification PASS.
It is not recreated here.

My own pull: preserve the successful small observer while distinguishing
reference agreement, trap membership and eventual pinning.
