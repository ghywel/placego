# Lemma B3 (the settled band has no long white run)

*Windows, zero runs and the left band. Derived from [PROOFS.md](../PROOFS.md), entry "12. Lemma B3 (the settled band
has no long white run)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

Once the edge band settles into its rhythm, it has no long white gaps.

**What it says.** If the diagonals near the edge have been repeating with a common period P for at least P steps,
then no white run inside that band is longer than 2P − 1 (first proved as 2P; sharpened on 2026-10-10).

**Why it matters.** The settled band does have white gaps, but only short ones, and the next theorem (13) uses that
limit against repeats.

**An everyday picture.** A well-kept fence still has gaps, left on purpose: hedgehog holes, about 13 centimetres
square, cut so that small animals can pass through and are not trapped (the owner's reading). The settled band is
that fence. Its white gaps are never wider than 2P, so only something small can get through; page 13 shows that a
long repeat, which needs a white stripe roughly as long as itself (page 10), is too big.

**Checked by machine.** A proof assistant (Lean) has checked it, in the sharper form: no gap longer than 2P − 1.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)". *Bears on:* the settled band has no long white run. *Status:* proved.

**Lemma B3 (the settled band has no long white run).** Suppose that at time $t$ the diagonals $0$ to $M$ have been
in their periodic regime, with a common period $P$, for at least $P$ steps. Then no white run of the row inside
diagonals $0$ to $M$ is longer than $2P$.

*Proof.* Let the row be white on $[g+1, M']$ with $M' \le M$ and $D_g(t) = 1$ (diagonals 0 and 1 are black, so such a
$g \ge 1$ exists). One step back, the constraint $D_{k-2} = D_{k-1} \lor D_k$ for $k \in [g+1, M']$ leaves two cases:
either the row at $t - 1$ is white on $[g-1, M']$ with $D_{g-2}(t-1) = 1$ (the run is older and two cells wider),
or it is black on $[g-1, M'-2]$ (the run is born here, under a black run). Repeating, the run is older for $s_0$
steps and born at time $t - s_0 - 1$. At time $t - P$ the row is the same as at $t$, white exactly from $g+1$, so
$s_0 < P$. Forward from time $t - P$, a white run only loses two cells a step at its edge side:
$D_k(\tau+1) = 0$ whenever $k-2$, $k-1$, $k$ are all white. So at time $t - s_0 - 1$ the row is white on
$[g + 1 + 2(P - s_0 - 1), M']$ and black on $[g - 2s_0 - 1, M' - 2]$. The two ranges are disjoint only if
$M' - g \le 2P - 2s_0 \le 2P$. $\square$

*Machine-checked (Local, 2026-10-10 05:02 BST).* tests/probes/lean/LemmaB3.lean, `lemma_B3`, in a slightly stronger form.
- It needs only that the rows at times t - P and t agree on the diagonals up to M (P >= 1, P <= t), and no leftmost
  black cell. Then a white run [g + 1, M'] of row t, with M' <= M and diagonal g black, has M' - g <= 2P.
- `back` is the one-step dichotomy (older or newborn), from the white cell's constraint D_(k-2) = D_(k-1) or D_k.
- `fwd` is the forward loss of two cells a step.
- The older chain is stopped by periodicity at g.
- The axioms are propext, Classical.choice and Quot.sound.

*Sharpened (Local, 2026-10-10 05:15 BST, L539; after Cloud's CL169 sample never reached 2P).* The bound is $2P - 1$.
- In the newborn case, the step back also shows that $D_{M'-1}(t - s_0 - 1)$ or $D_{M'}(t - s_0 - 1)$ is black, since
  the white cells $M'-1$ and $M'$ at time $t - s_0$ need it.
- The forward white range $[g + 1 + 2(P - s_0 - 1), M']$ at that time must miss $M' - 1$, so
  $M' - g \le 2P - 2s_0 - 1 \le 2P - 1$.
- Machine-checked: `lemma_B3_sharp` in tests/probes/lean/LemmaB3.lean. `lemma_B3` is now its corollary, and the axioms
  are unchanged.
- The bound is tight at P = 1 and P = 2, on every seed of support <= 12 (rule30_b3_sharp.py).
- Second-read: Cloud by hand (CL170), and GPT on the Lean source's final step (GC960).
