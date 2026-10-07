# Proposition 5 (Rule 90 has no finite configuration with a period-two column)

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "16. Proposition 5 (Rule 90 has no
finite configuration with a period-two column)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

In Rule 30's simpler cousin, Rule 90, the blinking middle is impossible, proved with Pascal's triangle.

**What it says.** Rule 90 just adds neighbours: a square turns black when exactly one of its two neighbours was
black. Started from one black square, it draws a Sierpinski triangle (described below). The same picture appears in
Pascal's triangle, the triangle of numbers in which each is the sum of the two above it, if the odd numbers are
coloured black. At the times that are powers of 2 (1, 2, 4, 8, ...) a single square's pattern is white everywhere
except at its two far ends. So once those times are larger than the seed, the middle is white twice in a row, and it
cannot blink for ever.

**Why it matters.** It shows the kind of proof that works for the linear cousin, and why Rule 30 is harder: its rule
mixes that adding with an "or" (black if either square is black), and the clean arithmetic is lost.

**An everyday picture.** Draw a triangle, join the midpoints of its sides and cut out the middle piece; then do the
same to each of the three smaller triangles left, and so on for ever. That is Sierpinski's triangle, the pattern
Rule 90 draws. Its holes open at the rows numbered by powers of 2, and each time the newest and biggest one is an
empty triangle right at the centre, which a finite seed is soon too small to fill.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.3 What was already known, Rule 30's siblings, and the owner's harmonics (2026-10-04)". *Bears on:* the siblings: Rule 90 has no finite configuration with a period-two column. *Status:* proved.

**Proposition 5 (Rule 90 has no finite configuration with a period-two column).** Under Rule 90, $x' = l \oplus r$,
let a finite row have its support in $[-w, w]$. Then column 0 is 0 at time $2^n$ and at time $2^n + 1$ whenever
$2^n > w + 1$.

*Proof.* Rule 90 is linear, and a single 1 at position $j$ reaches $(0, t)$ with the value
$\binom{t}{(t-j)/2} \bmod 2$. By Lucas' theorem, $\binom{2^n}{k}$ is odd only for $k \in \{0, 2^n\}$, and
$\binom{2^n+1}{k}$ only for $k \in \{0, 1, 2^n, 2^n+1\}$. These need $|j| \in \{2^n - 1, 2^n, 2^n + 1\}$, outside the
support. $\square$
