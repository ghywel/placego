# Proposition 20 (proved by hand, second-read): a checkerboard fringe on the right edge is invisible, so infinitely many finite seeds share the single cell's pattern

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "33. Proposition 20 (proved by hand,
second-read): a checkerboard fringe on the right edge is invisible, so infinitely many finite seeds share the single
cell's pattern"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** second-read by GPT (GC641, 2026-10-09); promoted from the waiting room by Local (L351).

## In plain words

Infinitely many finite starting rows (11, 101, 1011, 10101, ...) grow into exactly the single cell's Rule 30 pattern, except for a striped fringe on the right edge, so they all share its centre column.

**What it says.** Put a black cell, then an alternating white-black stretch, then a black cell. That fringe rides the pattern's right edge and flips every cell it touches at every step. Its two innermost stripes are always opposite, so the OR in Rule 30, the only way the fringe could reach inward, is already 1. The inside of the pattern never learns the fringe is there.

**Why it matters.** It answers the owner's cipher question in miniature: the centre column is an autokey encryption of the starting row, and it cannot tell which of infinitely many finite keys made it. A scan of every right half up to 16 cells found no other such seed. It does not touch the prize problems' difficulty, since every one of these seeds has the same column as the single cell. Cloud proved it by hand after an exploratory scan; it waits for a second reader.

## The formal statement and proof

*Status:* second-read by GPT (GC641, 2026-10-09); promoted from the waiting room by Local (L351). Waiting-room heading: "33. Proposition 20 (proved by hand; waiting room, second reader wanted): a checkerboard fringe on the right edge is invisible, so infinitely many finite seeds share the single cell's pattern". Not a prize claim.
*Provenance:* Cloud, 2026-10-09 (00:43 BST), from the owner's question "if the centre column was an encrypted message,
not just random but encoding information, how might we decrypt it" (CHAT-LEDGER.md CL069). Found by
`tests/probes/lexicon/rule30_cloud_equivalent_seeds.c`, an exploratory scan with no prediction written first; the proof
was written afterwards.

**Proposition 20.** For $r \ge 1$ let $S_r$ be the seed with black cells $0$ and $r$ and cells $1, \dots, r-1$
alternating white, black, white, … ($S_1 = 11$, $S_2 = 101$, $S_3 = 1011$, $S_4 = 10101$; $S_r = 1(01)^{r/2}$ for even
$r$, $1(01)^{(r-1)/2}1$ for odd $r$). At every time $t \ge 0$ and every cell $x \le t - 1$, Rule 30 from $S_r$ has
the same colour as Rule 30 from the single black cell. In particular the two have the same centre column.

**Proof.** Write $D_k(t) = x_t(t - k)$, the diagonal $k$ cells in from the line $x = t$. Rule 30 at cell $t + 1 - k$
reads $D_k(t+1) = D_k(t) \oplus (D_{k-1}(t) \lor D_{k-2}(t))$, with $D_k(0) = x_0(-k)$. For the single cell,
$D_k \equiv 0$ for $k < 0$ and $D_0 \equiv 1$, so $D_1(t) = t \bmod 2$. For $S_r$, $D_k \equiv 0$ for $k < -r$ and
$D_{-r} \equiv 1$. Every $D_k$ with $-r < k \le 0$ flips at each step. $D_{-r+1}$ sees $1 \lor 0$ and $D_{-r+2}$ sees
$D_{-r+1} \lor 1$. For $k \ge -r + 3$, $D_{k-1}$ and $D_{k-2}$ both flip and start at the adjacent cells
$x_0(1-k) \ne x_0(2-k)$ of the alternating stretch $1, \dots, r-1$. So they stay in opposite phase and their OR is $1$.
Hence $D_0(t) = (t + 1) \bmod 2$. For $k = 1$, $D_0 \lor D_{-1} \equiv 1$ in $S_r$: if $r = 1$, $D_{-1} \equiv 1$; if
$r \ge 2$, $D_{-1}$ flips from $x_0(1) = 0$, opposite to $D_0$. The single cell's OR is $1 \lor 0$, and both
$D_1(0) = 0$, so $D_1$ agrees. For $k = 2$, $D_1 \lor D_0 = (t \bmod 2) \lor ((t+1) \bmod 2) \equiv 1$ in $S_r$, and
$D_1 \lor 1$ in the single cell. $D_2(0) = 0$ in both, so $D_2$ agrees. For $k \ge 3$ both inputs agree and
$D_k(0) = 0$ in both, so $D_k$ agrees by induction. Every cell $x \le t - 1$ lies on a diagonal $k = t - x \ge 1$. ∎

**What the computation adds (exploratory).** The scan decrypts the single cell's centre column under every right half
$x_0(1..W)$. The column is an autokey cipher of the left half keyed by the right half, so the left half is the unique
plaintext. At $T = 400$ the right halves whose plaintext has no black deeper than $200$ are, for $W = 12$ and
$W = 16$, exactly the $S_r$ with $r \le W$ and the single cell itself (13 and 17 of 4,096 and 65,536). Joint cycle
detection on the closed right-edge diagonals confirmed $S_1$ to $S_7$ for ever, in a scratch check. Open: whether a
wider right half, or a finite left half deeper than $200$, also gives the single cell's column.

**Reading.** The centre column does not determine its finite seed, and the OR is the mechanism. The fringe flips
every cell it touches, and its two innermost diagonals are in opposite phase, so the OR that would carry it inward is
already $1$. Compare §8.19: a second seed $d$ cells to the right leaks inward at about $0.28$ cells per step and
reaches the centre after $2.3$ to $2.9\,d$ steps. This fringe leaks at speed zero. It is the smallest case of
Meier and Staffelbach's observation that many right halves are equivalent (PRIOR-ART.md). The prize problems ask
about the single cell's centre column, which every $S_r$ shares. Prior art: none found in a bounded search; likely
folklore of the right-edge diagonals (Jen).

*Independent reading (GPT GC641, 2026-10-09).* Verified by hand: the diagonal update reads left, centre and right inputs D_k, D_(k-1), D_(k-2) in the correct orientation; the fringe's diagonals through D_0 toggle with adjacent ones in opposite phase, the first two after the outermost covered by its fixed black input (r = 1 and 2 included); D_1 and D_2 agree, and the induction gives agreement for every k >= 1 and t; the centre at t = 0 is black in both. *Scoped extension (GC641; read by Local L351).* The same proof covers any common initial left half, finite or infinite, with x_0(0) = 1 and x_0(-1) = 0: the diagonals k <= 0 read only cells x >= 0, D_1 starts at the common 0 and toggles in both histories, and D_2 and deeper start equal and stay equal. The nearest-left guard is essential: with a common black cell at -1, the base {-1, 0} and the fringed {-1, 0, 1} have first rows {-2, -1, 1} and {-2, -1, 2} and centres 0 and 1 at time 2. Local replayed the extension on 600 random common left halves with x_0(-1) = 0 and r up to 9, for 80 steps (7.29 million cells at x <= t - 1, no disagreement), and found the centre columns differing in all 600 cases once x_0(-1) = 1.
