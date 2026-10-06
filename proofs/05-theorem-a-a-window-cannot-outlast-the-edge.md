# Theorem A (a window cannot outlast the edge)

*Windows, zero runs and the left band. Derived from [PROOFS.md](../PROOFS.md), entry "5. Theorem A (a window cannot
outlast the edge)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

A steady rhythm in two neighbouring columns cannot last once news from the edge arrives.

**What it says.** Any finite seed has a leftmost black square, and its influence travels inward at full speed. If
two neighbouring columns repeat with period P over a stretch of time, the stretch must end within a short time
after that influence arrives: roughly the distance to the edge plus two periods.

**Why it matters.** It is the classic Jen theorem with a stopwatch attached. It turns "periodicity is impossible
for ever" into "periodicity must break by this time", which is the kind of bound a proof can use.

**An everyday picture.** A ripple from the edge of a pond: you can bob in a steady rhythm only until the wave
reaches you.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.54 Jen's theorem with a clock: a window of periodicity cannot outlast the left edge (2026-10-05)". *Bears on:* question 2 of PERIOD-TWO.md §7: a window of periodicity cannot outlast the left edge (Jen with a clock). *Status:* proved.

**Theorem A (a window cannot outlast the edge).** Take a nonzero configuration whose leftmost black cell at time 0
is $L \ge 0$ cells to the left of column $i$. If columns $i$ and $i + 1$ are $P$-periodic on $[a, b]$, then

```math
b \le 2a + L + 2P - 1 .
```

At time $a$ the left edge is $L + a$ cells away. So the window's length $b - a$ is less than that distance plus $2P$.

*Proof.* Three facts, each one line of Rule 30.
1. **Periodicity moves left and loses one step.** $x_t(k-1) = x_{t+1}(k) \oplus (x_t(k) \vee x_t(k+1))$. So if columns
   $k$ and $k+1$ are $P$-periodic on $[a, b]$, column $k - 1$ is $P$-periodic on $[a, b - 1]$. After $j$ steps to the
   left, column $i - j$ is $P$-periodic on $[a, b - j]$.
2. **The edge moves left one cell a step.** The leftmost black cell has two white cells to its left, and $001 \to 1$.
   So column $i - j$ is white before time $j - L$ and black at time $j - L$ (for $j \ge L$).
3. **The two meet.** Take $j = a + P + L$. Column $i - j$ turns black for the first time at $e = a + P$. If
   $b \ge 2a + L + 2P$, then $e \le b - j$. So both $e - P = a$ and $e$ lie in the window where column $i - j$ is
   $P$-periodic. It is white at one and black at the other, a contradiction. $\square$
