# Proposition 5 (Rule 90 has no finite configuration with a period-two column)

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "16. Proposition 5 (Rule 90 has no
finite configuration with a period-two column)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

In Rule 30's simpler cousin, Rule 90, the blinking middle is impossible, proved with Pascal's triangle.

**What it says.** Rule 90 just adds neighbours (exclusive-or). Its patterns are Sierpinski triangles, and at times
that are powers of 2 the middle must be white twice in a row, so it cannot blink for ever.

**Why it matters.** It shows the kind of proof that works for the linear cousin, and why Rule 30, with its "or", is
harder: the clean arithmetic is missing.

**An everyday picture.** Sierpinski's triangle of triangles: every power of 2 is a fresh, empty triangle at the
centre.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.3 What was already known, Rule 30's siblings, and the owner's harmonics (2026-10-04)". *Bears on:* the siblings: Rule 90 has no finite configuration with a period-two column. *Status:* proved.

**Proposition 5 (Rule 90 has no finite configuration with a period-two column).** Under Rule 90, $x' = l \oplus r$,
let a finite row have its support in $[-w, w]$. Then column 0 is 0 at time $2^n$ and at time $2^n + 1$ whenever
$2^n > w + 1$.

*Proof.* Rule 90 is linear, and a single 1 at position $j$ reaches $(0, t)$ with the value
$\binom{t}{(t-j)/2} \bmod 2$. By Lucas' theorem, $\binom{2^n}{k}$ is odd only for $k \in \{0, 2^n\}$, and
$\binom{2^n+1}{k}$ only for $k \in \{0, 1, 2^n, 2^n+1\}$. These need $|j| \in \{2^n - 1, 2^n, 2^n + 1\}$, outside the
support. $\square$
