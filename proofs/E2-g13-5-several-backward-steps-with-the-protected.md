# G13.5. Several backward steps, with the protected window's exact cost

*Theorems proved by GPT. Derived from [PROOFS.md](../PROOFS.md), entry "E.2. G13.5. Several backward steps, with the
protected window's exact cost"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary
in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT (statement in PROOFS.md; the proof is copied below from RULE30-GPT.md).

## In plain words

A single changed bit from the right side is forgotten at a steady rate as you go back in time: three squares per step.

**What it says.** Take a wall with one white beat (a "hole") followed by a long run of black. Change column 1 only
at that hole. Going back r rows, the two versions of the left half agree everywhere from depth 4r + 4 on, and the
first part of that agreement is a shared checkerboard. Each step back costs the protected checkerboard three
squares.

**Why it matters.** It measures exactly how quickly one bit of news from the right fades in the left half, a precise
piece of the "how much can get through" accounting.

**An everyday picture.** A footprint on a beach: each wave narrows it by the same amount, until it is gone.

## The formal statement and proof

*Where:* RULE30-GPT.md, "G13.5. Several backward steps, with the protected window's exact cost". *Status:* proved by GPT (proof there).

**Theorem.** Suppose a wall has a hole at q and then p−1 black cells, with no premise on its
values outside that window. Compare two right columns differing only at q. For any integer
r with $0\le r\le q$ and $p\ge3r+5$, their rows at q−r agree at **every** depth≥4r+4. In
addition their common cells in the interval

*Correction (Cloud, 2026-10-06): the copy above was cut off mid-sentence. The statement in RULE30-GPT.md G13.5 continues:*

```math
 [4r+4,\ p-1+r]
```

*are the checkerboard: black at even depths and white at odd depths. The interval's length is p−4−3r; each
backward step consumes three cells of this protected window. All other right-column inputs, and the wall before
and after the specified window, are arbitrary and common to the two constructions.*

## The proof, copied from RULE30-GPT.md

*Verbatim from [RULE30-GPT.md](../RULE30-GPT.md), the section named above; the master PROOFS.md holds the statement only.*

**Follow-up block, 2026-10-06 07:44 BST.** The one-step theorem has a bounded iteration.
Predictions MS0–MS2 and CF were pushed inc0c27f0 before the `multistep` check. This extends
G13's proved reset mechanism; no new literature theorem or Local computational job was used.

**Theorem.** Suppose a wall has a hole at q and then p−1 black cells, with no premise on its
values outside that window. Compare two right columns differing only at q. For any integer
r with $0\le r\le q$ and $p\ge3r+5$, their rows at q−r agree at **every** depth≥4r+4. In
addition their common cells in the interval

```math
 [4r+4,\ p-1+r]
```

are the checkerboard: black at even depths and white at odd depths. The interval's length
is p−4−3r; each backward step consumes three cells of this protected window. All other
right-column inputs, and the wall before and after the specified window, are arbitrary
and common to the two constructions.

**Proof.** At r0, G12 gives agreement at every depth≥4, and G11 gives the checkerboard
through p−1. Inductively, at row q−s let

```math
 A=4s+4,\qquad B=p-1+s.
```

The rows agree at all depths≥A and are the checkerboard on[A,B]. To step back once, use
these rows as the common driver y beyond A−1. If $p\ge3(s+1)+5$, then B≥A+3. Since A is
even, the three drivers at A+1,A+2,A+3 are010. The next driver, at A+4, is common even if
outside the known checkerboard interval. The reset010z gives a common state at depths
A+4,A+5. Its first component, x(A+4), is1 for either z. All later drivers are common,
so agreement continues forever from depth A+4.

Where the driver remains checkerboard, the reset gives the correctly phased earlier-row
checkerboard: if y(A+4) is known, it is1, giving x(A+5)=0; thereafter each adjacent pair
contains a1, so $x(j+1)=1-y(j)$ preserves black even depths and white odd depths. This
continues through depth B+1. If B=A+3, the new protected interval is just the black
anchor at A+4, already proved. Thus both inductive claims hold for s+1, finishing the proof.

**What was checked.** Argument `multistep` exited0 and printed ALL MULTISTEP CONTROLS PASS:
p5..64, four seeded arbitrary sigma columns each, q=p, every allowed r, through depth96;
**2520** row comparisons checked both all tested tail agreement and every protected
checkerboard cell. Seed2026100614. **Unexpected check MS2:**48 additional comparisons on
nonperiodic walls with arbitrary values before and after the black window, q1..6,
p=3q+5, eight backgrounds each, through depth64 at time0. Every predicted tail agreement
held. This checks that periodicity is not being smuggled into the local theorem.

The counterfactual dropping p≥3r+5 was rejected: for wall01111111, sigma all0 except the
changed bit at q8, row0 has a change at depth36, beyond the proposed unrestricted cutoff
4r+3=35 at r8. This is Local C024's spreading example with an explicit cutoff witness,
not an infinite-influence or LR counterexample.

**Limit and next intention.** The result covers at most floor((p−5)/3) steps back from an
injection. For a later hole q=p, it therefore does not reach row0. Additional reset factors
outside the guaranteed checkerboard window could extend the certificate, but their gaps
are not bounded here. The lead remains PART. C027 passes Local the exact window cost and
records this limit; the next reasoning target is what replaces the protected window after
it expires, rather than extrapolating the local bound to all earlier times.
