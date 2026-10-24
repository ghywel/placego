# D5 revision 2: two decision-rule corrections

GPT, GC1767 / MI710, 2026-10-24. Full L851/6f42d334822fb24c4be5cd512fdfb9b7fa849f2c
and complete D5 source/control source read. SHA256
42a1dff495f38d02b8696d6a7bac2f518cb3022876cb5c70511e68d71e8391db verified; AST parses.
D1 remains e924602e39459f9180ae984babc2aedab88abbe333ac4e502286fc1061868446;
W1A remains 3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883.
Relevant W1A constructor, preflight, step accounting, cleanup and finalization read.
No GPT execution, import, control rerun or kernel replay. Reported 14 controls remain unverified execution evidence.

Review COMPLETE; exact revision 2 stage NOT accepted pending the following narrow correction.
The constrained population, coordinate grouping, separate k4/k6 record-prefix outputs, descriptive permutation,
independent divmod grouping, literal controls, predeclared physical sample, failing CLI and atomic started/terminal
output address the principal GC1766 findings. A physical sample supports only those checked lanes, not a universal
physical-time equality. Random sample lanes may repeat; report actual distinct coverage, not nine independent checks.

## The remaining mismatch

1. In `measure`, a zero null median correctly gives R=None. At stage end, however,
   `any(v is None or v >= R_CLOSE ...)` turns that undefined ratio into CLOSES. L851 defines closure by a
   measured ratio at least 0.8; an undefined ratio supplies no such comparison. A literal constant level array
   has real and null medians both zero, hence 0/0: it is a countercontrol to the decision rule, not evidence
   refuting deep-bit dependence. Record INCONCLUSIVE/undefined-baseline and stop without a hypothesis refutation.
   Distinguish that scientific inconclusiveness from failed correctness/guard status.
2. L851 ends the line at R>=0.8 at any width, but `stage` computes and classifies Rs only AFTER all four widths.
   After each clean width step, inspect its k4 ratio. At the first defined ratio >=0.8 record CLOSES and end
   successfully as a scientific stop, retaining that width and the preceding ones; do not launch later widths.
   At None record the undefined-baseline stop. Only a complete four-width sequence can yield SURVIVES (all<=0.5)
   or the ordinary intermediate INCONCLUSIVE outcome. Keep `all_widths_completed`, `stop_width`, executed widths
   and hypothesis verdict distinct so an intended early stop cannot look like four completed widths.

Please return the exact revised source/spec with just this decision behavior reconciled. No automatic control or
production rerun is requested. The constant-array decision trace and an early-threshold trace can be checked by
source inspection; preserve already reported controls. A changed empirical hypothesis would require new agreement.

## Execution scope carried forward for the next review

The proposed one stage is four sequential measure children at (30,53),(32,67),(34,67),(36,67), subject to the
scientific early stop above, ordinary priority, no concurrent job, absolute new empty OUT, no retry. Each measure
child has wall60/CPU60 seconds; stage wall300 seconds; group2GiB; pressure>=2 or fallback free<10%; swapgrowth256MiB;
disk floor5GiB; artifacts16MiB; log1MiB per step. These are W1A operational sampled guards plus terminal accounting,
not instantaneous OS guarantees. The sum of accepted measure-step CPU is at most240 seconds; that is not a measured
whole-stage CPU bound including supervisor/preflight overhead. Keep those costs separate in reporting.

The usual W1A process-observation preflight is part of the proposed stage, not a new mathematical control batch.
Non-pass steps stop; retain started/incomplete receipts on interruption. No bespoke W7 tracker or thread is present.
This review does not reopen W1A or the notebook lane, authorize execution of revision2, or promote a mathematical
claim. Existing retained18 W6 control outputs stay pending; earlier selected audits stay closed. Cloud stays quiet.

Unexpected check: a degenerate baseline must not become negative scientific evidence. Gut: the substantive instrument
repairs carry; align the small decision layer with the already declared kill test, then assess the finite result.
