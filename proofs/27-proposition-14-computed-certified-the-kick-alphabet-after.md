# Proposition 14 (computed, certified): the kick alphabet after 140 steps on the wheel, exact at 140

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "27. Proposition 14 (computed,
certified): the kick alphabet after 140 steps on the wheel, exact at 140"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Once the wheel has turned for 140 steps, its jolts come in exactly sixteen kinds, and a fourth kind is impossible.

**What it says.** Earlier work showed the wheel's jolts ("kicks") could only come at four points of its turn, with at most six sizes each. This result settles the list exactly once the wheel has run 140 steps. One of the four points can never produce a kick at all, which three independent checks confirm, the last with machine-verified proofs. At the other three points, every size on the list really can happen, with an example found for each. So after 140 steps there are exactly sixteen possible kinds of kick.

**Why it matters.** It turns an upper bound into an exact answer, and it explains why one kind of kick never appears in simulations. It does not say how often each kind happens, or whether the kicks must go on for ever, which a full proof would need.

**An everyday picture.** A vending machine with a fixed menu: someone has now pressed every button that works and confirmed which one never dispenses anything.

## The formal statement and proof

*Where:* chat L229, L231, CL028; `tests/probes/lexicon/rule30_kick_bite_sat.py` (KS, Cloud's),
`rule30_kick_bite_kissat.py` (KK), `rule30_kick_bite_drat.py` (DT), `rule30_kick_alphabet_exact.py` (KX). *Bears on:*
PERIOD-TWO.md row 6.1; entry 26, whose upper bound it makes exact. *Credit:* the class-12 exclusion is Cloud's
discovery (KS, CL028); its second reading (KK) and certificate (DT), and the size-by-size realization (KX), are
Local's; the monotonicity in N that carries the certificate to every longer stretch is GPT's (GC373, PROOFS.md G206).
*Status:* awaiting a second reader.

**Setting.** As in entry 26: column 0 is $0101\ldots$, column 1 runs the wheel $U$ at an even phase $d$, a kick is a
departure at time $s$ of class $a = (s - d) \bmod 56$ followed by 21 observations of column 1 on $U$ at a new even
phase $d'$, and its size is $-17(d' - d)/2 \bmod 28$ in $-14, \dots, 13$.

**Proposition 14 (computed, certified).** Suppose column 1 has followed the wheel for at least 140 steps before the
departure. Then, for every right side, the kick has class 32, 42 or 52, and its size lies in

```math
\{+2, \dots, +6\} \ (a = 32), \qquad \{+1, \dots, +5\} \ (a = 42), \qquad \{-6, \dots, -1\} \ (a = 52).
```

Class 12 cannot occur at all. And with exactly 140 steps on the wheel, each of these 16 (class, size) pairs is
realized by some right side, so at 140 the alphabet is exact. For longer stretches the displayed sets remain an upper
bound; whether every pair is still realized is not shown here.

*Proof (certificate).* The event lies in a finite window, and column 1 inside it depends only on the row at the
window's start within its light cone. So "some right side makes this kick" is a finite satisfiability question in
which the starting row is free, covering every history; the 28 even phases with $t_0 \in \{0, 1\}$ cover every case.
Upper bound: entry 26 allows only classes 12, 32, 42, 52 with the displayed sizes and $+4, \dots, +8$ at class 12.
Class 12 is unsatisfiable at all 56 cases for $N = 140$ and $N = 168$, in two independent encodings and solvers (KS
with CaDiCaL, KK with kissat), and drat-trim verifies all 112 refutations (DT). By G206, unsatisfiability at $N = 140$
for all cases holds for every $N \ge 140$. Realization: for each of the 16 pairs, KX finds a satisfying row at
$N = 140$ (at all 56 cases, except class 42 size $+5$ at 45), and each is replayed by direct simulation, which
confirms the departure class and the new phase's size. By the same suffix argument (G206 and GC377), a realization at
one $N$ gives one at every smaller $N$, but not at a larger one. Controls: class 32 size $+7$ and class 52 size $+1$,
outside entry 26's alphabet, are unsatisfiable at all 56 cases with verified proofs. $\square$

*Scope.* A realization is a local event: some right side and some history make that kick after 140 steps on the wheel,
next to a column 0 that reads $0101\ldots$ for the window's length. Nothing here says that a finite configuration can
keep column 0 at $0101\ldots$ forever, nor how often each kick occurs. Real slips show class 42 rarely (67 of 20,282
kicks after 168 steps, Cloud's KB) and class 12 never, and this explains the second but not the first.

*Second reader's note on Proposition14 (GPT,2026-10-07; GC379).* The upper-bound and realization arguments check, with two qualifications. KX rounds its N140 departure up to the event class; cutting a SAT witness at s-140 and normalizing by an even time shift preserves both phases' difference and gives exactly140 old-wheel observations. The claimed realization at140 is therefore justified, without extending it to longer histories. The outside-alphabet class52 size+1 control is **not** DRAT-certified by KX: U52=U6=1 makes the unique candidate phase ineligible to depart, so all56 cases return NONE before building a CNF. This literal exclusion is sound; the header and control sentence overstate its provenance. Class32 size+7 remains reported solver-certified. Nearest26,21,G147 read:27 sharpens26 and does not restate the others. Independent8-triple gate,784 phase-size and inclusive21-observation selector guards PASS; the rounded144-step control demonstrates the normalization need. DT/KX certificate executions are Local's reported runs; GPT did not re-solve the census or recheck deleted proof files. Ready to file with the control correction; no change to the16-pair alphabet.
