# Phase pumping excludes right backgrounds from the reference orbit at period 310

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT270. Phase pumping excludes right
backgrounds from the reference orbit at period 310 (second-read, 2026-10-09)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A hypothetical bridge in the critical case cannot end by settling into a shifted or time-delayed copy of the reference pattern it started from, at the period under study.

**What it says.** Suppose a pattern starts as the repeating reference on the left and ends as a shifted or time-delayed copy of the same reference on the right. Its middle can then be cut out and looped back into the reference, repeated just enough times to line the copies up exactly. That gives a pattern that differs from the reference in only a finite stretch, and a finite change of that kind was already shown to need a much longer period.

**Why it matters.** It closes one of the escape routes left open in the main critical case. The other backgrounds stay open.

**An everyday picture.** A detour that leaves a ring road and rejoins it further round can be driven again and again until the laps add up to whole circuits, which shows the detour is a real change to the road.

## The formal statement and proof

*Where:* RULE30-GPT.md GC848 (GC747, GC749, GC751, GC758, GC759; GC845's route map). *Credit:* GPT's hand proof.
Independently read by Local (chat L474), with the phase return and the gcd alignment checked step by step. The stated
reference facts were checked literally on the CX ring: least G period 310; G^2(R) a spatial shift by 29 (126 in the
other convention); 68 and 88 black cells; G(R) is not a spatial shift of R. The finite-defect input is GC751/GC758,
read by Local earlier the same day (L394, L397). *Status:* proved by hand. Not a prize claim. *Filed by:* Local.

**Statement.** Let R be the aligned reference row of spatial period 155, with G^2(R) = σ^29(R) and least G period
310. Let p > 0 with 310 dividing p and 1240 not dividing p. If G^p(y) = y, y agrees with R far enough left, and y
agrees far enough right with σ^a G^j(R) for some a and j, then y = R. So at such p, and in particular at p = 310,
no non-ring bridge reaches any spatial or temporal phase of the reference orbit.

**Proof (GC848).**
1. Profiles. Columns' p-periodic temporal profiles satisfy ΔV_i = V_(i+1) OR V_(i+2), the edge (X, Y) -> (Y, Z) of
   the pair graph. Conversely, any such profile sequence is a G^p-periodic diagram. R's profiles form a cycle C of
   length 155.
2. Phases. Tick rotation T is a graph automorphism. G^2(R) = σ^29(R) gives T^2 V_i = V_(i+29), so T^2(C) = C. Even
   time phases of R lie on C, and odd ones on C' = T(C).
3. Closing. Suppose y != R at some site b. Take y's path P from a reference vertex v far left to its right
   background, through b's column.
   - If P ends on C, close it along C to v.
   - If it ends on C', follow C' to T(v), then T(P) (which ends on C), then C back to v.
   The result is a closed walk W of H edges through v; every seam is an identical pair vertex.
4. Alignment. Repeat W r = 155/gcd(155, H) times, so the inserted length is a multiple of 155. Attach R's own profile
   sequence on both sides.
   - The resulting z satisfies G^p(z) = z, agrees with R outside a finite interval, and has z(b) = y(b) != R(b) from
     the unchanged first copy of P.
   - GC758 (GC751's parity obstruction) then forces 1240 to divide p, a contradiction. ∎

*Scope (GC848).* The q = 155 retained template, the other q = 310 background orbits, higher periods allowed by the
finite-defect guard, and p divisible by 1240 remain open. Returning to a vertex alone is not enough: the gcd
repetition is what removes the phase slip, and an unrelated right background has no automorphism giving a return.

*Near-entry gate (Local, at filing).* `--near G270` gives G252 (a period-155 right background in a period-310 bridge;
the other branch), G198 (a phase-mismatch return in Q7's components; a different graph) and G164, all read. None
is restated. Hard checks pass.
