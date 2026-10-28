# Two crystal boundaries and the irregular wedge

GC2020, 28 October 2026. Owner requests a wider A/B view and an explanation of the irregular crystallisation
boundary's jumps. Curiosity is the objective; no prize claim or large census. No new ancestry choices.

Record searched: L1049–51 in archive/ledgers/CHAT-LEDGER.18.md; white_right_front.py; GC2019 exact rightmost
defect; GC2016–18 retained histories. The earlier A front measurement at depth 512 is -3146, outside the prior
display and generation width. Earlier finite-string period detection is not used as the new certificate.

## Hand mechanism to test

Extend each row's eventual left crystal periodically across the whole line, writing C for that background
and X for the actual row. Let s be their first discrepancy from the left. The discrepancy after one update is

    delta'_i = delta_(i-1) XOR ((X_i OR X_(i+1)) XOR (C_i OR C_(i+1))).

At i=s-1, delta' is 1 exactly when C_(s-1)=0. A white neighbour therefore exposes the difference one cell
leftwards. A black neighbour masks it. Following differences can also be masked, or cancel when both XOR
terms equal 1. A run of zero output discrepancies moves the first surviving difference to the right.
Read backwards, this disappearance becomes a leftwards jump of the irregular region. It is not transmission
of a signal faster than the rule's causal speed. Hand identity; carrying interpretation remains reviewable.

Prediction: jumps are explained by these exact local discrepancy cancellations, and some jumps occur without
a change of the crystal's spatial period. Counterfactual: a failed identity or a frontier outside the fixed
window stops the claim; if every jump coincides with a period change, that simpler explanation survives.

## Frozen reconstruction and validation

Read digest-bound GC2016 view and selected tail periods. Reconstruct precisely the same A and B rows to
x=-8192..320, 512 past rows plus the existing 64 future rows. B remains unconstrained older than its failed
period-2 trace; no branch is silently replaced. Verify every overlapping old cell and every interior update.

Certify the eventual LEFT period by the orbit of the four inverse pair states, sampled once per certified
child-period block in the child's left crystal. A repeated pair gives an exact infinite-left cycle, not a
finite fit. Extend that period rightwards until the first discrepancy; this defines the left boundary.
Verify background-to-background updates over a common period, and the straight right boundary x=t against
its periodic right extension. Check every jump's discrepancy identity and retain all cancelling/masking
counts. If a front or its certificate leaves the window, report incomplete and stop, without widening.

Caps: one Intel CPU worker, run_capped.py; 120 CPU seconds, 180 wall seconds, sampled group RSS 384 MiB,
16 MiB/file, 48 MiB total output. Launch free+inactive 1024 MiB, ongoing 512 MiB, swap growth 128 MiB.
Left/right period cap 4096, depth fixed 512, no automatic rerun. Input SHA-256s are fixed in source
past_crystal_boundaries.py. Output includes per-row certificates, exact boundaries, top jumps and packed
compressed visual data. A separate finite-certificate audit will precede strong claims if needed.

## GC2021 — measured fronts, fixed-period jumps, and frozen seam audit

The frozen 5177dcf1 run completed. Exact A left endpoints reproduce the earlier values -640, -1542, -2373,
-3146 at depths 128,256,384,512; B's selected history gives -700,-1554,-2385,-3350. At depth 512 the transition
widths are 2634 and 2838. Both have a 50-cell backward jump at depth 172, with left period 48 on both sides
of that step. A: first defect -934 to -884 forward; B: -946 to -896. Both transitions have 12 masked and
39 cancelled output comparisons before the first surviving difference. A 50-cell displacement spans 51
potential output sites because the earliest possible new discrepancy is one cell left of the old one.

There are 393 (A) and 398 (B) jumps greater than one at unchanged left period. Thus period change is not a
necessary cause. Construction checked 1,967,104 old overlapping cells, 8,715,264 update equations, 45,494
background equations and 8,542 jump sites. Child: 5.02 real seconds, 4.94 user, 0.05 system; maximum RSS
31,961,088 bytes. The window contained every certified front with ample left margin. No bound was widened.

Freeze one separate certificate audit before delivery: fixed retained-data SHA-256s in check_crystal_boundaries.py;
no generator import. Check the whole-line extension by periodic-background equations plus the leftmost stored
seam, all matches through the claimed first difference, both fronts, and every jump by the literal truth table.
This avoids relying on finite-string period fitting or on the constructor's cycle-finding routine. Also compare
only the two-row 100-cell patches around the three largest shared jumps (depths 172,185,213) after aligning their
fronts. Prediction: equal jump counts may reflect translated copies of a local event; disagreement is retained.
Single worker, 30 CPU/45 wall seconds, 256 MiB RSS, 4 MiB/file, 8 MiB output; unchanged pressure gates. No rerun.
