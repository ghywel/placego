# temporal rotation classes sharpen the fixed-period edge-history bound

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT156. temporal rotation
classes sharpen the fixed-period edge-history bound (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Identifying temporal rotations sharpens the edge-history period bound.

**What it says.** An edge history cannot revisit a rotation class of profile pairs before reaching its zero boundary. Counting four-letter necklaces improves the number of possible depths from about 4^P to about 4^P/P. The exact maximum prefix lengths are three at period one and eight at period two.

**Why it matters.** It sharpens a necessary lower period bound. It does not provide the upper period bound or waiting-time estimate needed for settling; independent review is pending.

**An everyday picture.** A clockface seen after a rotation is still the same clockface.

## The formal statement and proof

### G156. Temporal rotation classes sharpen the fixed-period edge-history bound (2026-10-07)

**Status and target.** Symbolic edge-diagonal proof, independent review pending; no computation. Returns to Q7's open period-growth/settling lead, distinct from Local's G155 review. G7 already proves the absolute-profile tree bound K<=4^P-1. Prediction: counting temporal rotations gives a stronger bound of order 4^P/P. Counterfactual: rotation-equivalent pairs can occur at different edge depths despite the absorbing zero boundary. The first-hit argument excludes that. The small-period controls below are literal finite graph proofs, not a sampled census.

Let K count a compatible prefix w_0 through w_(K-1) of P-periodic diagonal profiles rooted at (w_(-1),w_0)=(0,1^P). On pairs define

    B(a,b)=(S b XOR (a OR b),a),

with cyclic time shift S. G7's diagonal equation gives B(w_(j-1),w_j)=(w_(j-2),w_(j-1)). The zero pair is fixed, and the root maps to it. Thus the pair at depth j has first zero-hit time j+1: an earlier zero would force the root to be zero after further applications. B commutes with temporal rotation, so rotation-equivalent pairs have the same first-hit time. Pairs at different depths are therefore inequivalent even after rotation. Including the zero class gives

    K+1 <= N_4(P),
    N_4(P) = (1/P) * sum over d dividing P of phi(d)*4^(P/d).

Here N_4(P) counts cyclic words of length P over the four-letter pair alphabet. For a rotation by h, a fixed pair word has gcd(P,h) freely chosen letters, hence 4^gcd(P,h) possibilities. Averaging fixed counts over the cyclic group and grouping equal gcd values gives the displayed standard necklace formula. All periods dividing P are included; using only primitive necklaces would undercount.

For P>=2 the nonidentity contribution is at most (P-1)*4^(P/2)/P. Consequently N_4(P)=(4^P/P)*(1+o(1)). Along prefixes with K tending to infinity this strengthens G7's lower period floor to

    P >= log_4(K)+log_4(log_4(K))-o(1).

It is a lower bound on period, not an upper bound or a waiting-time budget.

**Period-one control.** N_4(1)=4. The root path (0,1),(1,1),(1,0) contains three pairs; each maps backward to its predecessor and then zero. The last pair has no constant-profile child. Thus K=3 attains the bound.

**Unexpected nonabsorbing-class check, period two.** Encode two-bit temporal words with the least significant bit at time zero. S swaps1 and2, fixes0 and3. The pairs (1,2) and (2,1) form a B-cycle and are rotations of one another, so their single rotation class cannot lie on a rooted edge history. N_4(2)=(16+4)/2=10; excluding zero and this additional class gives K<=8. The eight-pair path

    (0,3),(3,3),(3,0),(0,1),(1,3),(3,1),(1,1),(1,0)

attains it. Substitution in B sends each pair to the preceding one and the first to zero. Hence the maximum common-period-two rooted prefix has K=8. This check both tests the quotient convention and prevents mistaking every necklace class for an absorbing class.

**Prior-art map distinction.** Re-read Nersissian's section4 through Theorem13: its backward map B is exactly G7's edge-diagonal map, and its absolute-profile first-hit argument is the same mechanism. The earlier vertical-wall audit remains correct: that inverse shifts the first coordinate rather than the second and is a different map. The paper's profile bound is not a new wall theorem; the rotation quotient here applies directly to the diagonal tree. Standard necklace counting was already recorded for G152. No novelty is claimed for that counting method.

**Scope.** This improves the necessary period lower bound for every compatible edge branch and certifies the two smallest controls. It supplies no sublinear upper period growth, no adaptive waiting bound below slope3, no finite-left exclusion and no prize result. Q7's all-branch settling obligation remains open. No period16 graph, new ring census or Local computational job is requested.

*Second reader's note on G156 (Local, 2026-10-07; chat L114).* Correct. The indexing is right: $K$ words give $K$ pairs
including the root $(0, 1^P)$, the pair at depth $j$ first hits zero at $j + 1$ because an earlier zero would make the
root zero, and $B$ commutes with rotation, so distinct depths lie in distinct rotation classes. The count must be of all
necklaces, since a pair can have a smaller period, and the Burnside formula is the right one. I traced both controls by
hand: the period-one path stops after $(1, 0)$, and every arrow of the period-two path maps to its predecessor, with
$(1, 2)$ and $(2, 1)$ forming a rotation class on a 2-cycle. Checked exhaustively (`rule30_audit_g99_g100.py`, S50) for
every $P \le 7$ over all $4^P$ pairs: rotation commutes with $B$; the rooted tree's depths lie in distinct classes;
$K + 1 \le N_4(P)$; $K = 3$ and 8 at $P = 1$ and 2; and the same results with the time shift taken in either direction.
Descriptive, not part of G156: the longest $K$ is 3, 8, 3, 29, 3, 8, 3 for $P = 1$ to 7, against bounds 4, 10, 24, 70,
208, 700, 2344. So the deepest branch depends only on the power of two in $P$, odd periods add nothing beyond the
constant path, and $P = 6$ repeats $P = 2$. This is consistent with the powers-of-two periods of Jen's theorem on these
diagonals (§8.13).
