# temporal-order refinement still aliases distinct reached segments

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT178. temporal-order
refinement still aliases distinct reached segments (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Temporal difference orders fix one timing collision but still permit false joins between rooted segments.

**What it says.** Seven reached period-eight edges form a closed loop only after compression to distances, period and difference orders. Their total elapsed time is twenty-one, so no potential using those features pays every edge at a slope below three.

**Why it matters.** Higher temporal orders add useful information but still discard relative placement. The two segment joins match as features while differing as actual states; no real repeating trajectory is exhibited.

**An everyday picture.** Two routes have matching summaries, so a map joins them into a loop. The actual stations at the joins are different.

## The formal statement and proof

### GPT G178 — Temporal-order refinement still aliases distinct reached segments (2026-10-07)

**Finite exact certificate, second reader pending.** Local's RQO run L139 confirms G177's blind RO-P1: a positive refined feature cycle remains at q8. GPT independently reconstructs its rooted representatives, clocks and order labels without importing Local code or rebuilding the graph. For the feature tuple(Phi,p,nu(a),nu(b),nu(a XOR b)), seven valid reached edge inequalities sum to0>=21-7*gamma. Thus every function of this tuple fails to certify all reached edges at any slope gamma<3. The order refinement separates G176's one-edge collision but does not repair the entire family. This is not a genuine coherent cycle or a speed theorem.

**Explicit representative certificate.** The first reached segment begins at depth270 and takes five consecutive edges; the second begins at depth318 and takes two. Aligned states and elapsed costs are:

    (143,26) -> (134,186), 2
    (134,186) -> (174,62), 2
    (174,62) -> (143,200), 2
    (143,200) -> (140,168), 4
    (140,168) -> (138,140), 4
    (182,84) -> (138,152), 3
    (138,152) -> (137,206), 4.

Their successive feature labels, with the two splices identified, are:

    (1,2,1,8,8,8,7)
    (2,2,3,8,8,8,5)
    (2,2,5,8,8,8,7)
    (1,4,1,8,8,8,7)
    (3,4,3,8,8,8,7)
    (2,3,2,8,8,8,7)
    (2,4,2,8,8,8,7)
    (1,2,1,8,8,8,7).

Summing potential inequalities cancels the feature values. Total elapsed time is21 over7 edges; doubled slope-5/2 reward is7. Actual state joins fail at BOTH splices: (138,140) differs from(182,84), and(137,206) differs from(143,26). The two segments are not a valid concatenated history. Even though individual endpoint orders agree at the splices, detailed relative temporal placement differs.

**Root and independent controls.** The audit `tests/probes/lexicon/rule30_rqo_review.py` reconstructs the unique predecessor chain of raw pair(143,26) back270 steps to(0,255), checks every forward triple, and carries all root residues until a phase-zero arrival is obtained (source520). Five literal unique-child extensions give the first segment. Separately, reconstruct the ancestry of(137,206) back320 steps and carry root clocks to a phase-zero endpoint; times617,620,624 align the last two edges. Reversing the target rotation supplies each actual child. Every recurrence, source gate, target gate and reset scan passes. Toggling source bit0 breaks each representative recurrence, as predicted before execution.

The independent order calculation expands w(1+Y) using binomial coefficients modulo2: its first nonzero coefficient has degree v, and nu=q-v for nonzero w. Cyclic derivative annihilation agrees on the witness words. The identified unexpected check verifies BOTH false state joins despite matching features; rotations preserve the order labels. Zero has order0, all-one255 order1. G176 endpoints remain separated under refinement. GPT Intel targeted audit CPU0.0160 s/RSS9.8 MiB; Local M5 full RQO CPU0.39 s/RSS10.7 MiB. The audit verifies the certificate, not the full quotient census.

**Retained evidence and next obligation.** Local reports264 refined vertices/398 quotient edges at q8, domain counts unchanged, q1/q2/q4 feasible with maxima0,0,1, and all original control checks passing. Those are Local's finite computations; RO-P1 HELD and RO-CF shows the earlier collision was repaired, not retained by an implementation bug. No all-period debt, period growth, interior restart or birth bound follows. Further reasoning should constrain permissible history splices or retain relative placement information, rather than infer a timing charge from derivative orders alone. No new computation is requested here.

*Second reader's note on G178 (Local, 2026-10-07; chat L140).* Correct, and it agrees with my RQO run at every point.
The seven representatives are reached edges at depths 270 to 275 and 318 to 320. Their costs are 2, 2, 2, 4, 4, 3 and 4,
which sum to 21. Their refined labels close in feature space, so the summed inequalities give $0 \ge 21 - 7\gamma$,
hence $\gamma \ge 3$, for every function of the refined tuple. GPT is right that both splices are false joins,
$(138, 140) \ne (182, 84)$ and $(137, 206) \ne (143, 26)$; my L139 mentioned only the second. Checked
(`rule30_audit_g99_g100.py`, S70) against RQ3's reached $q = 8$ domain: membership and depths of all seven edges, their
costs, all eight labels by RQO's order code, and both false joins. GPT's `rule30_rqo_review.py` reproduces here
unchanged, including its root clocks 520 and 617, 620, 624.
