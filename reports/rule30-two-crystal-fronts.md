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
