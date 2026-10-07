# a fixed right tail gives a unique left seed for every wall

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT130. a fixed right tail
gives a unique left seed for every wall (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Fix the seed's right part, and any wall forces exactly one left part, though usually an infinite one.

**What it says.** Reading Rule 30 backwards (the crossword quirk) fills in the left part uniquely from the requested
middle column and any chosen right part. Even an all-white right part works, if the left part may be infinite.

**Why it matters.** So a finite seed exists exactly when some finite right part makes the forced left part turn
white for good. That is the precise target.

**An everyday picture.** The primer's crossword again: write in the middle column and any right half, and the left
half is forced, letter by letter, but it may run off the edge of the page.

## The formal statement and proof

### G130. Fixing the initial right tail gives a unique left seed for every wall trace (2026-10-06)

**Status and purpose.** Exact coordinate reduction of G4.4's triangular inversion; independently verified by Local L084. This is not a new left-permutivity theorem or a solution of the wall problem. G129 leaves finite right support as an additional constraint. Here the target is to identify exactly what that constraint can and cannot exclude. No experiment. Counterfactual: finite initial right support alone restricts possible temporal walls, or exact finite-prefix realizations guarantee a finite left seed. The delayed single-cell example below independently rejects the latter implication at a fixed right tail.

Fix the initial values r_i at all sites i>=0. For any desired one-sided wall tau with tau(0)=r_0, there is exactly one initial left word u=(x_-1,x_-2,...) whose full forward Rule 30 evolution has x_0(t)=tau(t) for every t>=0. The map from u to the future trace (tau(1),tau(2),...) is a homeomorphism of binary sequence spaces. No periodicity premise is used.

**Proof.** G4.4 gives, for each n>=1,

    x_0(n) = x_-n(0) XOR P_n(x_(-n+1)(0),...,x_n(0)).

The unique path carrying the leftmost input to the observed output contributes by XOR; all other terms use higher initial indices. Fix r and solve x_-1, then x_-2, and so on, using the prescribed tau(n). Each step has exactly one solution and does not alter earlier samples. These compatible finite assignments define one infinite initial row, and its ordinary forward evolution realizes every sample. Uniqueness follows from the same successive solving. Both directions are continuous: a trace prefix of length N uses only the first N left bits and r_0,...,r_N; conversely those N left bits are determined by that trace prefix and the same finite right data. This is an initial-row/trace coordinate map, not a conjugacy between Rule 30 evolution and a shift on a fixed-tail space, since the initial right tail need not remain fixed after an update.

**Finite-right support is compatible with every wall in isolation.** Set r_0=tau(0) and r_i=0 for all i>0. The construction realizes every tau, including an alternating wall, with this finite initial right tail. Its forced left word may be infinite. Thus no obstruction based only on requiring finite initial right support can exclude a temporal word when arbitrary infinite left support is allowed. This does not assert that a chosen companion from G129 has a finite-right extension.

**Exact finite-global criterion.** For a prescribed tau, let r range over all eventually-zero initial right tails with r_0=tau(0), and write u_r for the uniquely solved left word. A finite global seed realizes tau if and only if at least one u_r is eventually zero. Necessity applies uniqueness to that seed's right tail; sufficiency joins the two finite tails and invokes the construction. Hence the joint boundary problem is a zero-tail question for this canonical family, rather than existence of an unrestricted right extension. This supplies no uniform zero-tail test, search bound, or exclusion theorem. The finite-left condition of G129 still has to hold for the same row.

**Unexpected fixed-tail finite-prefix guard, exact.** Take the initial row x_i=1 for i<0 and x_i=0 for i>=0. Rule 30 sends it in one tick to the single black cell at site 0: triples 111 and 110 give zero on the left, triple 100 gives one at the wall, and triples 000 give zero on the right. Let tau be this row's wall trace: its first sample is zero and its later samples are the single-cell wall trace shifted by one tick. With the fixed initial right tail all zero, this tau has the unique left seed 111..., so no finite left seed with that same right tail realizes it forever.

For every N>=1, truncating that left seed to ones at -N,...,-1 yields a finite seed with the same right tail and exactly the same wall through time N. Its first wrong wall sample is at time N+1: the higher initial indices agree, while the fresh XOR pivot x_(-N-1)(0) differs. Thus arbitrary finite horizons are realized with growing left support even though no fixed finite left seed works for that fixed right tail. No claim is made about alternative right tails for this tau, or about periodicity of the single-cell trace. The check uses both the explicit one-tick truth table and the independent triangular uniqueness mechanism.

**Next obligation.** For an alternating or eventually alternating prescribed wall, prove a property of u_r uniform over finite r that prevents an eventual zero tail, or identify a counterexample. Periodic companion assumptions, unrestricted trace existence and growing finite-prefix realizations do not supply that property. This is a reformulation of the missing proof, not a claim that the canonical words have been classified.

*Second reader's note on G130 (Local, 2026-10-06; chat L084).* Correct. With the right half fixed, each wall sample
brings exactly one fresh left bit by XOR, so the left word is solved uniquely and continuously; a finite seed exists
exactly when some finite right tail gives an eventually-zero left word. Checked (`rule30_audit_g99_g100.py`, S28): 200
random finite right tails with random wall prefixes to length 12 each have exactly one solution at every step, and
its evolution realizes the prefix; $\ldots111|000\ldots$ becomes the single black cell in one tick; truncating its
left seed at radius $N$ keeps the wall through time $N$ and breaks it at $N + 1$, for $N = 1$ to 14. For the
alternating wall, the record's LR records add one fact to this criterion: for every finite right tail, the left word
cannot be zero from any depth up to 85 onward, so an eventually-zero $u_r$, if one exists, starts its zero tail
beyond depth 85.
