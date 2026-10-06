# The wall coding separates family entropy, orbit entropy and finite support

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G140. The wall coding separates
family entropy, orbit entropy and finite support (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

The wall's whole compatible family and a single dyadic orbit have different entropy, and neither settles finite support.

**What it says.** The existing wall coding turns two evolution steps into one shift of the visible word. The full compatible family has entropy one, while the dyadic orbit closure has entropy zero. That orbit closure contains an infinite checkerboard state as a limit.

**Why it matters.** An infinite-support limit does not rule out a finite starting row when its support bound grows with time. The missing statement still concerns the starting row's spatial tail.

**An everyday picture.** The variety of an entire library differs from the variety along one story; a limit of growing finite objects need not stay finite.

## The formal statement and proof

**Status and target.** Symbolic quantifier audit of section 8.39's existing wall itinerary/seed bijection, independent review pending. No experiment or new novelty claim about that bijection. G139 controls fixed-depth temporal words; this block makes its dynamical meaning explicit and checks whether a checkerboard limit supplies a finite-tail contradiction. Counterfactual: zero temporal entropy or an infinite-support limit state would settle the finiteness of the initial seed. Neither does.

Let S be the set of left initial rows whose evolution with imposed wall 0101... has a black nearest-left cell at every odd time. Let Phi(c) be the forced initial left row for any one-sided binary visible word c, and let F be two steps of this wall-driven half-line evolution.

**The known coding intertwines the dynamics.** Phi is a homeomorphism from the full one-sided binary sequence space onto S. Existence follows by the inverse columns: v_1(2s)=1-c_s, v_1(2s+1)=1, and the inverse recurrence constructs all farther columns. Every constructed left cell satisfies the forward Rule30 equation; uniqueness of forward evolution with the imposed wall recovers this diagram from row zero. Conversely any row in S determines c_s=1-v_1(2s), and the same inverse reconstructs that row. Finite output coordinates depend on finite c prefixes, and finite c prefixes depend on finite initial cones, proving continuity both ways. This is the section 8.39/WA1 coding, not a new existence theorem.

The periodic boundary returns to its original phase after two steps. Shifting the whole constructed diagram by two physical times therefore gives

    F(Phi(c))=Phi(shift(c)).

Unlike G130's fixed-right-tail coordinate map, this boundary condition is invariant under the chosen time step, so the displayed relation really is a dynamical conjugacy. S is compact and F-invariant. Its full-family topological entropy is one bit per two-step iterate, because its conjugate is the full binary shift. This does not give a positive entropy theorem for each individual row or any finite-support subclass.

**Dyadic orbit closure.** Let X_d be the closure of the one-sided shifts of the powers-of-two word d. Phi(X_d) is exactly the F-orbit closure of its forced left row. The length-m language of X_d is the language of d; G137 bounds its size by 2m+1. Hence X_d, and by conjugacy Phi(X_d), have zero topological entropy. Equivalently, in the product topology every fixed finite spatial observation has zero temporal entropy as in G139. The full compatible family has entropy one while this particular orbit closure has entropy zero: the quantifiers differ.

**Unexpected support-limit check.** Take t_n=3*2^(n-1), n>=1, halfway between successive dyadic ones. Its distance to the next one tends to infinity, so shift^(t_n)(d) converges to the all-zero visible word. Continuity gives

    F^(t_n)(Phi(d)) -> Phi(0,0,...).

G138 identifies the limit row as the stationary left checkerboard, with one at every odd depth. Thus the dyadic orbit closure contains an infinite-support row regardless of whether its starting row has finite support. If that starting row had radius L, its radius at this iterate would be at most L+2t_n; this bound grows without limit. Finite-support rows with no common radius bound can converge to an infinite-support row. The limit therefore supplies no contradiction. This is the identified independent check, now within one fixed wall and one orbit closure rather than a collection of unrelated initial rows.

**Finite-left target retained.** Write S_fin for S intersected with the eventually-zero initial rows. It is forward invariant, since the left light cone expands by at most two cells per F iterate. It is not known to be nonempty, closed or compact. Neither entropy of S, zero entropy of a particular orbit closure, nor the checkerboard limit decides membership in S_fin. For d itself the needed statement remains an all-depth spatial certificate that Phi(d) has infinitely many ones. For the prize the required exclusion must cover every admissible visible word. This closes only the proposed temporal-entropy/limit-state shortcut; no finite-left witness, full right extension or prize solution is asserted.
