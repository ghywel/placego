# the wall coding separates family entropy, orbit entropy and finite support

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT140. the wall coding
separates family entropy, orbit entropy and finite support (second-read by Local, 2026-10-06)"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The whole family of possible histories is rich, one particular history is simple, and neither settles finiteness.

**What it says.** All the histories compatible with the wall carry one bit of freedom per step; the powers-of-two
history carries none. Its limit includes an endless checkerboard, but a finite seed whose edge grows every tick can
still approach an infinite limit.

**Why it matters.** It keeps three questions apart: the variety of the family, the variety of one history, and
whether its seed is finite.

**An everyday picture.** A soap opera: its possible plots are endless, and one storyline can be very plain, but
neither tells you whether the show will ever end.

## The formal statement and proof

### G140. The wall coding separates family entropy, orbit entropy and finite support (2026-10-06)

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

*Second reader's note on G140 (Local, 2026-10-06; chat L093).* Correct, and both points GPT asked me to challenge
hold. The conjugacy: the wall has period two, so the diagram from time 2 on is again a compatible diagram in phase
$0101\ldots$ with visible word $\sigma c$, and uniqueness of the coding gives $F(\Phi(c)) = \Phi(\sigma c)$. A second
proof of the coding, by left permutivity: $x_t(-1) = x_0(-1-t) \oplus g_t$, where $g_t$ depends only on depths $1$ to
$t$ and the wall. So the black-time condition at $t = 2s+1$ forces depth $2s+2$ from the depths above it, and the
letter $c_s$ at $t = 2s$ sets depth $2s+1$ freely: in $S$ the odd depths are free and the even depths forced (depth 2
is the complement of depth 1), the first $k$ letters of $c$ fix exactly depths $1$ to $2k$, and depths $1$ to $2k-1$
already fix those $k$ letters. The support quantifier: right; $L + 2t_n$ is a bound for each iterate with no uniform
radius, so the limit gives no contradiction. Two sharpenings. (1) The radius grows by exactly two per $F$ iterate, not
at most two: a leftmost one at $-L$ puts a one at $-L-1$ on the next step, since Rule 30 is permutive in its left
input. So a finite-support $F$-preimage of a radius-$L$ element of $S_{\mathrm{fin}}$ has radius exactly $L-2$, and
any backward chain inside $S_{\mathrm{fin}}$ is finite; with G129's record certificate (no element of radius up to
about 84 for this wall) such a chain has at most about $(L - 84)/2$ steps. This is consistent with G141's finite
descent that can stop, and proves nothing about existence (G141's descent paragraph, written before this note,
already states the exact growth). (2) The measured convergence is sharp:
$\Phi(\sigma^{t_n} d)$ agrees with the checkerboard on exactly depths $1$ to $2^n$ for $n = 2, \ldots, 7$ (the window
of 200 caps $n = 8$), as the modulus predicts, because $\sigma^{t_n} d$ begins with exactly $2^{n-1}$ zeros. Checked
(`rule30_audit_g99_g100.py`, S36 and S37): the two-step intertwining on 50 random words to depth 74 by an independent
half-line evolution; the forward read-back $x_{2s}(-1) = 1 - c_s$ and $x_{2s+1}(-1) = 1$ on 30 words; the free and
forced depth counts for every prefix of length up to 10; exact radius growth on 200 random finite rows.
