# Proposition 6 (computed): the pure wheel cannot make a finite left half

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "20. Proposition 6 (computed): the
pure wheel cannot make a finite left half"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** certified by computation (the script named in the section).

## In plain words

We ran the pure wheel until it repeated, about 15 billion ticks, and checked: it fails.

**What it says.** With column 1 exactly the never-kicked wheel, the joint pattern of the two columns repeats after a
cycle of 15,009,104,432 steps, and inside that cycle the left half is never finite. Certified by computation.

**Why it matters.** An exact check of the single most important special case, with a committed program anyone can
rerun.

**An everyday picture.** Watching a combination lock's dial until every position has come round again.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.6 Order in, noise out: the left side churns the wheel (2026-10-04)". *Bears on:* the pure wheel cannot make a finite left half. *Status:* certified by computation (the script named in the section).

**Proposition 6 (computed): the pure wheel cannot make a finite left half.** Let column 0 be 0101… and column 1 the
universal wheel $U$, at any of its 28 even phases. Then the forced left half is never eventually zero. The orbit of the
column pair enters a cycle after

```math
\mu = 32\,896\,298 \text{ steps}, \qquad \lambda = 15\,009\,104\,432 = 2^4 \cdot 7 \cdot 17 \cdot 1433 \cdot 5501 ,
```

and the cycle is not the zero fixed point. So the left half is eventually periodic in depth, with period dividing
$\lambda$, and it has infinitely many ones.

*Proof.* The certificate $(\mu, \lambda)$ was found by Brent's algorithm in about $4.7 \times 10^{10}$ steps per phase
(O1 and O2 held). It was then re-checked independently by plain stepping:
- the state after $\mu$ steps is not zero, and $\lambda$ further steps return to it;
- $\lambda / p$ steps do not return, for each prime $p$ of $\lambda$, so $\lambda$ is the exact period;
- the state after $\mu - 1$ steps is not on the cycle, so $\mu$ is minimal.

The verifier rejects false certificates (its counterfactuals). Every phase gives the same certificate, for a reason:
$F$ commutes with the rotation of time, which is a permutation of bits, and a rotation by 2 fixes the trace and moves
the wheel's phase by 2. So the 28 orbits are rotations of one, and one certificate settles them all. All 28 were run
anyway and agree. $\square$
