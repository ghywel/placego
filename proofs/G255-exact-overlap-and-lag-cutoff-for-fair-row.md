# Exact overlap and lag cutoff for fair-row window density

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT255. Exact overlap and lag cutoff
for fair-row window density (second-read by Local, 2026-10-09)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Over a random row, how much a fixed window's black count now predicts the same window's count k steps later is exact, and drops to zero once k reaches the window's width.

**What it says.** Each cell is correlated with exactly one cell k steps later, the one k places to its right along the light-speed diagonal, and with no other. So two windows' black counts are correlated only through the pairs of cells that line up that way. For one window of width w watched over time this gives the diagonal's correlation times (w - k)/w, which is exactly zero from k = w on, while a window that moves right with the diagonal keeps the full correlation. Second-read by Local, with exact checks for a width-3 window.

**Why it matters.** A fixed window's correlation vanishing at large lags is geometry, not evidence that Rule 30 forgets: the memory has moved out of the window along the diagonal.

**An everyday picture.** Watching a fixed stretch of a conveyor belt, you lose sight of each parcel once it has moved past the end, even though the parcel itself is unchanged.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-09 (Local L407).** Second reader: Local, chat L407. Waiting-room heading: "GPT G255 — Exact overlap and lag cutoff for fair-row window density (GPT, 2026-10-09; waiting room)". The text below is unchanged, so its *Status:* line is historical.

*Status:* independent hand reading pending. *Where:* RULE30-GPT.md GC776. *Provenance:* Cloud’s §8.70 cell-covariance collapse and G97 fair-row invariance; elementary summation corollary, no novelty claim. Duplicate gate passes; nearest W254,G163,G147 read in full. W254 addresses diagonal Markov memory; G163 winding-rate timing and G147 phase-countability do not restate this elementary window corollary. Proof copied verbatim below.

**Bounded continuation of CL078 and GC773.** The existing collapse of cell covariances gives an exact window-overlap law, not merely a small-lag edge approximation. Expected a fixed width to impose a covariance cutoff even while the moving diagonal retains memory. Counterfactual: a nonzero rho_k forces nonzero density covariance for every fixed window at that lag. Independent control counts the surviving spatial pairs; unexpected check compares a stationary window with one translated right by k. No enumeration, Monte Carlo or single-seed run. This is a corollary of Cloud's §8.70 third addendum and G97's fair-row invariance, not a new all-lag sign or decay theorem.

Take Rule 30 on the line with an iid fair row, and let S_t(i)=(-1)^x_t(i). Each row remains iid fair. For k >= 1, left permutivity gives x_(t+k)(j)=x_t(j-k) xor g_k of the other cone inputs. Therefore

    E[S_t(i) S_(t+k)(j)] = rho_k if i=j-k, and 0 otherwise.

When i is outside the future cone its bit is independent of that cone. Inside the cone but different from j-k, averaging the independent fair bit at j-k cancels the product. This explains both zero cases and prevents extending the leading-bit argument to a bit outside its stated cone without justification.

For finite nonempty site sets I and J, put Z_t(I)=sum_(i in I) S_t(i). Their variances are |I| and |J|. Summing the exact cell identity gives

    Cov(Z_t(I),Z_(t+k)(J)) = rho_k * |I intersect (J-k)|,
    Corr(Z_t(I),Z_(t+k)(J)) = rho_k * |I intersect (J-k)| / sqrt(|I|*|J|).

Here J-k means every site of J translated left by k. Black counts or mean densities have the same normalized correlation, since each is an affine transform of its spin sum. For the same contiguous width-w window at both times this becomes exactly

    Corr = rho_k * max(w-k,0)/w.

In particular every lag k >= w has zero covariance, for any value of rho_k. With w = 1 and k = 1, the fixed cell has zero correlation while the rightward diagonal has rho_1=-1/2. These are different observables; GC773's diagonal memory does not contradict the fixed-window cutoff. No independence, finite Markov order or higher-order mixing follows from the covariance identity alone.

**Unexpected transport check.** If the later window is J=I+k, all earlier sites retain their matching light-speed partner and Corr=rho_k exactly, for every finite I and every k. Translation left instead yields overlap |I intersect (I-2k)|. Thus the edge loss is geometric transport of this linear observable, not a demonstrated decay of the diagonal process. At fixed k, letting w grow recovers rho_k; at fixed w, increasing k reaches a strict zero cutoff. The large-window approximation must not be used uniformly in lag without the overlap factor.

**Disposition.** Keep the positive-part overlap factor in any fixed-window baseline or interpretation of CL078. This retains the unproved all-lag sign/decay questions for the moving diagonal and imports nothing to the deterministic single seed, a periodic ring, nonlinear black-pair counts or thresholded density flips. No new literature leap: the existing permutivity argument and elementary covariance summation suffice; no novelty claim. File this explicit finite-window corollary for independent hand reading. Scratch deferred without retry; room closed.

*Independent reading (Local L407, 2026-10-09).* Verified by hand: for i outside the cone of x_(t+k)(j) independence and zero means kill the covariance; for i inside it but not j - k, averaging the independent fair bit x_t(j - k), which enters with coefficient one, kills it; at i = j - k it is the diagonal correlation rho_k by shift and stationarity; summing gives rho_k |I intersect (J - k)| and the stated window factors. Checked exactly by enumerating every fair row on the cone for a width-3 window: correlations -1/3, 1/12, 0 at k = 1, 2, 3, equal to rho_k (w - k)/w with rho = -1/2, 1/4, -1/4.
