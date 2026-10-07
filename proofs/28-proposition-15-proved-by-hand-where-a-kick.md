# Proposition 15 (proved by hand): where a kick can land

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "28. Proposition 15 (proved by hand):
where a kick can land"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** second-read (GC389).

## In plain words

When the wheel is jolted to a new position, it lands on a spot of the same parity and the opposite colour, which is why its forward jolts all land in one short stretch.

**What it says.** Next to a column that alternates black and white, the neighbouring column behaves like a wheel turning a fixed step each tick. When it jumps to a new position (a kick), the new position must have the same parity as the old one and the opposite colour, and a jump can only start right after a white. The wheel's only black spots at even positions form one short run, so every forward jump from the usual starting points lands there.

**Why it matters.** A two-line argument explains the landing window Cloud saw in the tables, and why each forward kind of jolt has at most six sizes. It does not say which jolts actually happen; that needs the computed results (entries 26 and 27).

**An everyday picture.** A chess bishop on a white square can only ever reach white squares, whatever the position on the board. Here the rule is a little different (same parity, opposite colour), but it fixes the possible landings before any details of the game come into play.

## The formal statement and proof

*Where:* chat L238, L239, CL031, GC389; `tests/probes/lexicon/rule30_kick_landing.py` (LW, and its `lemma` check).
*Bears on:* PERIOD-TWO.md row 6.1; entries 26 and 27, whose forward alphabets it explains; CL031's landing window.
*Credit:* the landing frame (kicks read as angles, and the window seen in the tables) is Cloud's (KA, CL031); the
lemma and its proof are Local's; the second reading and the even-phase scope note are GPT's (GC389). *Status:*
second-read (GC389).

**Setting.** As in entry 26: column 0 is $0101\ldots$ (column 0 at time $t$ is $t \bmod 2$), and column 1 runs the
wheel $U$, $x_t(1) = U((t - d) \bmod 56)$ at a phase $d$. Read $U$ by angle: $W(17p \bmod 56) = U(p)$. Then

```
W = 0101010101010101 (angles 0..15)   0 x 23 (16..38)   10101 (39..43)   1 x 12 (44..55)
```

**Proposition 15.** Let column 1 follow the wheel at an even phase $d$ before time $s$, depart at $s$, and follow
the wheel at an even phase $d'$ from $s$ on. Write $\alpha = 17(s - d) \bmod 56$ for the take-off angle and
$\ell = 17(s - d') \bmod 56$ for the landing angle. Then:

- (i) $W(\alpha - 17) = 0$: column 1 is white just before a take-off;
- (ii) $\ell \equiv \alpha \pmod 2$;
- (iii) $W(\ell) = 1 - W(\alpha)$.

*Proof.* (ii) At an even phase the angle at time $t$ is $17(t - d)$, which has the parity of $t$, since 17 is odd and
56 and $d$ are even. So $\alpha$ and $\ell$ both have the parity of $s$. (iii) At a departure, column 1 at $s$ differs
from the old wheel's value $W(\alpha)$, and the new phase shows that value at $s$. (i) Rule 30 gives
$x_s(1) = x_{s-1}(0) \oplus (x_{s-1}(1) \lor x_{s-1}(2))$. If $x_{s-1}(1) = 1$, then $x_s(1) = 1 \oplus x_{s-1}(0)$,
whatever column 2 holds. The wheel obeys the same rule, so this value is $W(\alpha)$ and no departure occurs. Hence
$x_{s-1}(1) = W(\alpha - 17) = 0$. $\square$

**Corollary.** The wheel's even black angles are exactly 44, 46, ..., 54, because the combs are black only at odd
angles. So a kick that takes off from an even white angle lands in that window. A class $a$ whose take-off angle
$\alpha = 17a \bmod 56$ is even and white therefore has at most six kick sizes, the residues
$k \equiv (\ell - \alpha)/2 \pmod{28}$ for those six $\ell$, with $k$ written in $-14, \dots, 13$ as in entry 26.
For entry 26's forward classes (take-off angles 34 to 42) these are the integers $(44 - \alpha)/2$ to
$(54 - \alpha)/2$, with no wrap. A take-off from an even black angle (class 52, $\alpha = 44$) lands at an even
white angle, 0 to 42. From an odd angle the landing is at an odd angle of the other colour; the odd white angles are
17 to 37.

*Scope.* These are necessary conditions. They bound where a kick can land, not which take-offs occur or which
landings are reached. In KL's relaxed model the even classes 2 to 42 reach all six landings at widths 2 to 15, and
width 16 drops 54 (LW). Entry 27 gives the exact alphabet after 140 steps. The phases must be even: an odd new phase
breaks the parity arithmetic (GC389), which is why evenness is part of the statement. Checked against all 1,118
(class, size) pairs of KL's settled tables (m = 2 to 16) and its one-turn table, with no exception
(`rule30_kick_landing.py lemma`).

*Second reader's note (GPT, 2026-10-07; GC389).* Correct in its even-phase scope. An independent scalar check of
the 112 choices of time residue and column-2 bit agrees: the old word admits its forced transition at every
residue, every departing transition has a white predecessor, and the even black angles are exactly 44 to 54. Keep
KL's convention explicit: $k$ is a residue modulo 28 written in $[-14, 13]$, and the six-size bound counts phase
choices. That the necessary conditions realize all six landings is not claimed; it rests on the relaxed-model result.
