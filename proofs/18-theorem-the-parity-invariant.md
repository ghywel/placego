# Theorem (the parity invariant)

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "18. Theorem (the parity invariant)";
rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

Next to a blinking wall, Rule 30's sibling Rule 210 behaves exactly like the simple cousin Rule 90.

**What it says.** With the wall blinking, every black square of Rule 210's forced left half sits on one colour of a
checkerboard, and on that checkerboard the rule reduces to Rule 90's simple addition.

**Why it matters.** It explains why the left-side conjecture fails for Rule 210 but may hold for Rule 30: Rule 210's
nonlinearity switches itself off there, and Rule 30's does not.

**An everyday picture.** A dancer who only ever lands on the black squares of a chessboard never meets the white
ones, yet must step over a white one with every move, even without touching it (the owner's reading). That is the
proof. Each step of Rule 210's rule looks at the square in between, and its one non-adding part, an "and not", asks
whether that square is black. Whenever the answer matters, the square is on the white colour and so empty, so the
step never trips, and what is left is Rule 90's plain addition.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.65 Rule 210, the one sibling: conjecture LR is false there (2026-10-06)". *Bears on:* Rule 210 next to 0101: the forced left half is Rule 90's (so LR fails there by linearity plus GPT's witness). *Status:* proved.

**Theorem (the parity invariant).** With column 0 equal to 0101... ($x(0, t) = t \bmod 2$) and any column 1, every
black cell $(-m, t)$ of Rule 210's forced left half has $t + m$ odd, and the forced left half is exactly Rule 90's:
$x(-m, t) = x(-m+1, t+1) \oplus x(-m+2, t)$.

*Proof.* Column 0 is black at odd $t$, parity $t + 0$ odd. Column $-1$: $x(-1, t) = \tau(t+1) \oplus (\lnot \tau(t) \land \sigma(t))$
is $1 \oplus \sigma(t)$ at even $t$ (parity $t + 1$ odd) and $0$ at odd $t$. Induction on $m$: the inverse rule is
$x(-m, t) = x(-m+1, t+1) \oplus (\lnot x(-m+1, t) \land x(-m+2, t))$, and the cells $(-m+1, t)$ and $(-m+2, t)$ have
parities $t + m - 1$ and $t + m$, so by the invariant they are never both black: when $x(-m+2, t) = 1$ its neighbour is
white and the AND-NOT equals $x(-m+2, t)$; when it is 0 the term is 0. So the term is $x(-m+2, t)$ in every case,
the rule is Rule 90's inverse, and $x(-m, t) = 1$ needs one of $(-m+1, t+1)$, $(-m+2, t)$ black, both of parity $t + m$,
so $t + m$ is odd. $\square$
