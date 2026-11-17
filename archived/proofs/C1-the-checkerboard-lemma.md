# The checkerboard lemma

*Short proofs restated from the running text. Derived from [PROOFS.md](../PROOFS.md), entry "C.1 The checkerboard
lemma (RULE30-PRIZE.md §8.62, §8.63; 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

While the middle column stays black, the left half next to it is a fixed checkerboard, whatever the right side does.

**What it says.** Suppose the middle column is black for a stretch of k + 1 ticks. Then the first k squares to its
left, at the start of that stretch, alternate white, black, white, black, and column 1 has no say in it.

**Why it matters.** Black stretches are where the right side is silenced (proof 01). This lemma says what the left
half looks like there: something fully known. A candidate's left half is therefore predictable in those places, and
GPT's later results on slow walls, walls with long black and long white stretches (E4, E5), build on it.

**An everyday picture.** A rubber stamp: however the neighbour shouts, every black stretch presses the same
chessboard into the paper.

**Checked by machine.** A proof assistant (Lean) has checked it.

## The formal statement and proof

*Where:* §8.62 and §8.63 item 2. *Bears on:* the wall form next to black stretches; GPT's G18 builds on it. *Status:* proved.

**Lemma.** Let column 0 carry the periodic word $\tau$ and let $\tau(t), \tau(t+1), \ldots, \tau(t+k)$ all be black. Then
in the forced left half $x(-j, t) = (j + 1) \bmod 2$ for $1 \le j \le k$, whatever column 1 is.

*Proof.* The inverse rule is $x(-j, t) = x(-j+1, t+1) \oplus \big(x(-j+1, t) \vee x(-j+2, t)\big)$. For $j = 1$:
$x(-1, t) = \tau(t+1) \oplus (\tau(t) \vee x(1, t)) = 1 \oplus 1 = 0$ since $\tau(t) = \tau(t+1) = 1$. Suppose the claim
holds for $j - 1$ at every time $t'$ with $\tau(t'), \ldots, \tau(t' + k - j + 1)$ black (so in particular at $t$ and
$t + 1$ when $j \le k$). Then $x(-j+1, t+1) = j \bmod 2$ and $x(-j+1, t) = j \bmod 2$, and $x(-j+2, t) = (j - 1) \bmod 2$
(for $j = 2$ this is $\tau(t) = 1$). One of $x(-j+1, t)$ and $x(-j+2, t)$ is black, so the OR is 1 and
$x(-j, t) = (j \bmod 2) \oplus 1 = (j + 1) \bmod 2$. $\square$

*Machine-checked (Local, 2026-10-10 04:56 BST).* tests/probes/lean/ShortC.lean, `checkerboard`, with column 0 black at times t .. t + k and 1 <= j <= k; no sorryAx.
