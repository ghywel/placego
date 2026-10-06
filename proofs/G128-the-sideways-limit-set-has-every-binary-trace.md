# the sideways limit set has every binary trace as a factor

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT128. the sideways limit set
has every binary trace as a factor (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The unrestricted sideways limit still contains every binary temporal trace.

**What it says.** Adjacent columns in a full spacetime diagram give exactly the sideways limit set. Projecting onto either column can produce any binary time sequence, so the limit contains nonperiodic sequences and retains at least one bit of word-count entropy per site.

**Why it matters.** Strict image losses do not imply a small or finite limit. The result allows unrestricted infinite spatial rows; fixing an alternating wall or insisting on a finite seed adds constraints that this argument does not remove.

**An everyday picture.** A shrinking set of paired records can still contain every possible individual record.

## The formal statement and proof

### G128. The sideways limit set has every binary temporal trace as a factor (2026-10-06)

**Status:** all-depth compactness proof using G4.4/G22; independent review pending. No experiment or probability extrapolation. The entropy here is word-count entropy under time-axis shift, not dynamical entropy under sideways iteration and not the entropy of a fixed-wall fibre.

Let X be all pairs of bi-infinite binary time tracks, H(a,b)=(S a XOR(a OR b),a), and

    Lambda_H = intersection_(n>=0) H^n(X).

Let Lambda_T be the corresponding limit set of G22's ternary map. Then Lambda_H is exactly the set of adjacent-column pairs occurring in full Rule 30 spacetime diagrams on integer space and integer time. Projection onto either track is onto the full binary shift. Under G22's ternary recoding, the one-block map pi(z)(t)=[z(t)=2] maps Lambda_T onto the full binary shift. Consequently every ternary iterated image and the limit set itself have word-count entropy at least1 bit per time-axis site. Lambda_T contains nonperiodic time-axis sequences. No fixed finite initial seed is asserted to realize them.

**Spacetime equivalence.** A full spacetime diagram supplies predecessors of an adjacent pair at every sideways depth: shifting to two columns farther right and applying H recovers the chosen pair. Hence that pair lies in every H^n(X).

Conversely, membership in H^n(X) supplies a right extension of n columns satisfying the inverse-column equations at every time. All left columns are determined by forward H iterates. For each n there is therefore a spacetime strip extending arbitrarily far left and n columns right. Fill its remaining sites arbitrarily. The full diagram space {0,1}^{Z x Z} is compact. A convergent subsequence, or the equivalent finite-intersection argument, preserves the given two columns and every local rule equation:each finite spatial region is covered once n is large enough. The resulting diagram obeys Rule 30 at every integer space-time site. No coherent choice of predecessors at successive finite depths was assumed.

**Every binary trace is realizable in this unrestricted class.** Fix any desired bi-infinite binary column b(t). For each N, prescribe b on times-N through N. Start a row at time-N. Iterated left-permutivity gives the sample after k ticks as its initial bit at site-k XOR a function of higher initial bits. Fix the initial positive-index bits and solve successively for sites0,-1,...,-2N, as in G4.4. This realizes the desired finite window;all other initial bits may be zero. Evolve forward on the whole spatial line, and fill times earlier than-N arbitrarily.

Compactness now gives a full spacetime diagram whose source column is b(t) at every integer time:each prescribed value and each local rule equation is eventually enforced in these diagrams. The finite-window seeds may differ with N and grow in width. Their compact limit need not have finite spatial support at any chosen time. Spatial translation makes the same argument apply to either track of an adjacent pair. Thus both projections of Lambda_H are onto the full binary shift.

**Ternary factor and entropy bound.** H's one-step image I is invariant under H, and G22 conjugates H restricted to I with T. The nested images starting from I have the same intersection as those starting from X, because H^n(I)=H^(n+1)(X). Therefore the conjugacy maps Lambda_H onto Lambda_T. In the recoding, the second binary track is exactly[z(t)=2], so its surjectivity is a one-block factor statement. Every length-N binary word is the pi-image of a length-N ternary word in Lambda_T;distinct binary words require distinct ternary words. There are at least2^N such words, proving the entropy lower bound. Every finite iterate contains Lambda_T and inherits it. If b is nonperiodic, any preimage under pi is nonperiodic, proving nonperiodic sequences exist in the limit set. This says nothing about recurrence or periodicity under T itself.

**Unexpected fixed-wall guard, checked algebraically.** The binary trace b=1^infinity is realized in Lambda_H by the pair(a,b)=(0^infinity,1^infinity), from the fixed spatial checkerboard:Rule 30 preserves cyclic01. But the pair(a,b)=((01)^infinity,1^infinity) is not even in H(X). G22 compatibility would force a(t)=1-b(t+1)=0 at every t, which the proposed a violates. Therefore the unrestricted factor is not onto after fixing an alternating wall. It cannot refute the thin fixed-wall channel bounds or supply a finite-seed counterexample. This is the identified unexpected check.

**Implication for the active route.** G127's strict image loss is genuine, yet unrestricted image pruning cannot collapse this limit set to finitely many traces or below1 bit of shift entropy. A prize-relevant invariant must use the wall, finite support, or another restriction absent from the full spacetime class. The all-depth factor is a structural obstruction to a proposed global-collapse route,not a theorem that a particular seed is random. The construction is the standard triangular trace argument plus compactness;no novelty claim for those ingredients.

*Second reader's note on G127 and G128 (Local, 2026-10-06; chat L081).* Both correct, including the steps GPT asked
me to challenge. G127: the forced bits at sites 0 to 4 follow from G126's target and compatibility equations, and
$(022000)^\infty$ is admissible in $Y$ (no ones, runs of length at least two, no 0202). G128: the finite-window step is
the usual left-permutive solving, the compactness steps are standard, and the transfer through G22's conjugacy uses
$H^n(I) = H^{n+1}(X)$. Checked (`rule30_audit_g99_g100.py`, S26): $T$ on the period-two points
$00, 11, 22, 12, 21$ gives $00, 22, 11, 22, 22$; 0102 lies in $Y$ and maps to 1212; the precursor blocks of 022000 are
exactly the six listed, all beginning 22100, and every precursor of 022001 also begins 22100; $(022000)^\infty$ lies in
$Y$; every binary word of length up to 11 is the site-0 trace of a finite initial row; the checkerboard is fixed;
and a brute force over period-2 and period-4 inputs finds no $H$-preimage of (alternating, all ones). (A first
version of that last check was vacuous and was replaced before recording.)
