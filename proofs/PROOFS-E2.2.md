# PROOFS, section E2, volume 2: G.GPT127 to G.GPT198

*Part of [PROOFS.md](../PROOFS.md), section E2 (GPT's proofs, second-read). Moved here unchanged on 2026-10-28 by Local at the owner's request: PROOFS.md had reached 1.9 MB, and E2 was 85% of it. PROOFS.md section E2 indexes every proof in the four volumes. 132 proofs.*

### G.GPT127. no shift-commuting section stays in the image; strict loss at one more layer (second-read by Local, 2026-10-06)

### G127. No shift-commuting predecessor section stays in the ternary image (2026-10-06)

**Status:** symbolic section obstruction and strict deeper-image loss; NS0/NS2 pass and NS1 prediction held. Uses G126's image theorem; independent review pending. The preregistered distinction between a section failure and strict loss is resolved by the separate certificate below. Further image layers remain open.

For the ternary sideways map T, let Y be the sequences avoiding100,101,112,0210,0211,0202. The period-two points of Y are exactly the repeating words00,11,12,21,22. Literal evaluation of G22's rule gives

    00 -> 00,
    11 -> 22,
    22 -> 11,
    12 -> 22,
    21 -> 22.

Thus the target(12)^infinity belongs to Y but has no period-two predecessor in Y. Any shift-commuting section Q:Y->Y of T would preserve being fixed by the two-step shift. Its value at this target would be such a predecessor, a contradiction. There is no shift-commuting section into Y, regardless of continuity; in particular there is no local one. G126's section into the full ternary shift is unaffected.

**Unexpected guard: a deeper predecessor nevertheless exists.** The repeating word0102 lies in Y and T(0102)=1212. It is a period-four predecessor of the period-two target. G126's canonical section instead returns(01)^infinity, outside Y. Hence failure of the canonical choice, and even failure of every period-preserving section, cannot establish absence of all image-constrained predecessors. These statements separate a constructive local inverse from mere onto-ness.

**NS0-NS2 preregistration.** A bounded search will address a different implication:does some target in Y have a finite prefix with no possible predecessor from Y? NS0 compares all27 radius-two ternary cases with an independent binary-pair decoding. NS2 checks the five period-two targets, the period-four lift0102, and the canonical-section failure;this is the identified unexpected check.

NS1 considers prefix lengths n=1..7, in increasing order. Enumerate all3^(n+2) full-shift precursor blocks, compute their length-n outputs, and retain as possible Y precursors every block avoiding the six forbidden words internally. This is a superset of globally admissible precursor blocks, so a missing output certifies impossibility for nonperiodic predecessors too. Restrict target witnesses to words w whose cyclic repetition lies in Y, to certify target extendability. Stop at the first length and lexicographically first missing target prefix. Blind prediction:a witness occurs by length7. If none occurs, record that prediction as refuted;do not infer stabilization.

For a witness, retain the complete set of its full-shift precursor blocks in memory and the spectrum of forbidden factors excluding them. Independently count every full-shift precursor via a de Bruijn-pair dynamic program using the binary-decoded rule, and require exact agreement with the enumerated count. No sampling or floating arithmetic. A full blocked-prefix certificate would prove T(Y) is a proper subset of Y;the absence of a short certificate would be finite evidence only. Counterfactual:the period-two failure alone proves strict deeper-image loss;NS2 must refute it. Publish the predictions and instrument before execution. This small structural certificate search duplicates no ring census or Local computational job.

**NS0-NS2 outcome (2026-10-06 22:20 BST).** Executed after81fb4fd published the proof,predictions and instrument. NS0 PASS on all27 triple cases;NS2 PASS on the period-two section obstruction and period-four lift. NS1 HELD at n=6,so the blind witness-by7 prediction held. The search checked9,828 full-shift precursor blocks across n=1..6. The first missing periodic target prefix is022000. All six full-shift precursor blocks are

    22100000, 22100001, 22100002,
    22100022, 22100220, 22100221.

Each contains100. The independently decoded de Bruijn path count is also6. No floating arithmetic or sampling. Minimality is asserted only within the preregistered search of cyclically admissible target words through length6,not all possible global target classes.

**All-sequence obstruction,independently derived from binary constraints.** In any target starting02200d with d in{0,1}, C begins011000 and D begins00100 (the sixth D need not be used). The predecessor constraints force A(0)=1 because D(0)=0,C(1)=1. Compatibility at site0 forces A(1)=1,and compatibility at site1 then forces A(2)=0. The target equations at sites3 and4 force A(3)=A(4)=0. Encoding(C,A) forces precursor prefix22100,which contains100. This eliminates every global ternary predecessor lying in Y,periodic or not,without relying on enumerated boundary choices. Thus T(Y) forbids022000 and022001 in addition to Y's old exclusions.

The cyclic target(022000)^infinity belongs to Y: it consists of zero runs of length4 and two runs of length2,with no ones and no0202. Hence it has a full-shift predecessor by G126,but no predecessor from Y. Therefore T(Y) is a proper subset of Y,or equivalently T^2(full ternary shift) is strictly smaller than T(full ternary shift). G126's explicit predecessor section cannot establish stabilization,and now stabilization at this layer is refuted by a complete finite obstruction. This proves strict loss at one further layer,not strict loss at every depth or zero entropy of the limit set. Further iterated images and any wall-specific consequence remain open. Independent review pending.

### G.GPT128. the sideways limit set has every binary trace as a factor (second-read by Local, 2026-10-06)

### G128. The sideways limit set has every binary temporal trace as a factor (2026-10-06)

**Status:** all-depth compactness proof using G4.4/G22; independently verified by Local L081. No experiment or probability extrapolation. The entropy here is word-count entropy under time-axis shift, not dynamical entropy under sideways iteration and not the entropy of a fixed-wall fibre.

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

### G.GPT129. the finite-left wall fibre is compact at each radius (second-read by Local, 2026-10-06)

### G129. The finite-left wall fibre is a compact constraint class at each fixed radius (2026-10-06)

**Status and target.** Symbolic bridge from G128 to the finite-left boundary problem; independently verified by Local L083. No experiment or novelty claim for compactness. Existing record: G27.2 excludes periodic companions, G53 identifies the wall-visible bits, and G128 characterizes unrestricted spacetime pairs. The target is an exact finite-left constraint that does not assume companion periodicity. The counterfactual is that a compact limit of witnesses with growing support must retain finite support. One unexpected check below separates counting full itineraries from counting their time factors.

Use one-sided time t>=0. Let X+ be all pairs of binary future tracks and H(a,b)=(S a XOR (a OR b),a), with S advancing time. Let Lambda+ be the intersection of H^n(X+) over n>=0. The same strip-compactness proof as G128 identifies Lambda+ exactly with adjacent-column pairs in full-space, forward-time Rule 30 diagrams: right extensions of every finite width have a coherent compact limit, and all left columns are uniquely given by H iterates. This does not require any periodicity or a past before time zero.

Fix any prescribed wall tau and integer L>=0. Define

    B(L,tau) = { (a,b) in Lambda+ : a=tau,
                 first_track(H^d(a,b))(0)=0 for every d>L }.

**Exact boundary interpretation.** B(L,tau) consists precisely of the wall/right-neighbor pairs of full forward diagrams whose initial left row is zero at all sites i<-L. There is no bound on the initial right row. In one direction, H^d recovers column -d, so the displayed conditions are its initial zero tail. In the other direction, Lambda+ supplies a full forward diagram with this pair; every possible extension has the same forced left columns and therefore the specified initial zero tail. This is a left-support condition, not a finite global seed condition.

For fixed L, B(L,tau) is compact: Lambda+ is an intersection of nested compact images; fixing a track is closed; and each displayed initial-cell equation is a closed cylinder condition depending on only finitely many input cells. Their countable intersection is closed. All finite-left pairs form the union of these classes over L. That union cannot be treated as one fixed-radius compact class merely because each member is compact.

**Finite-box alternative.** B(L,tau) is empty if and only if some finite rectangle already forbids a forward diagram with that wall and that left radius. Specifically, take sites -N through N and times 0 through N, fix the wall samples, fix initial cells -N through -L-1 to zero when N>L, and enforce every Rule 30 equation whose three input sites and output lie in the rectangle. Leave the right initial row unrestricted. If every N has an assignment, extend each assignment arbitrarily outside its rectangle and use compactness. Every fixed wall sample, local equation and initial left-zero condition is eventually enforced, so the limit is a full forward diagram in the class. The converse follows by restriction. Thus a failure at fixed L has a finite Boolean certificate in principle; no uniform certificate size or effective search bound is supplied. Certificates for a few radii do not prove emptiness for every radius.

**Visible itineraries have a finite cardinality bound at fixed L.** Observe b only at white wall times. There are at most 2^L such complete visible itineraries in B(L,tau). Choose the L initial left bits. With tau imposed as a boundary, forward evolution of sites i<0 is deterministic. Write its nearest-left trace as ell(t). At a white time, the wall equation forces b(t)=tau(t+1) XOR ell(t). At a black time, it instead requires ell(t)=1-tau(t+1), independently of b(t); failure rejects that left seed. Thus each left seed permits at most one whole visible itinerary, even when hidden black-phase bits or full right extensions are not unique. This is a boundary-determinism count, not an entropy or finite-state closure theorem.

**Counterfactual and unexpected check.** Initial rows with ones at -L,...,-1 and zeros elsewhere converge, as L increases, to an infinite left black tail. Their ordinary forward Rule 30 diagrams consequently have a compact limit with infinite initial left support. This general support guard does not claim those rows share one prescribed alternating wall; it shows why varying-radius compactness alone does not retain the required boundary condition. Separately, a single sequence formed by concatenating every finite binary word has one prefix of each length but all 2^n time factors of length n. Therefore the 2^L whole-itinerary bound gives no zero factor-entropy conclusion. This is the identified unexpected check, reused from G64's distinction; it is not a Rule 30 realization claim.

**Remaining bridge.** To exclude a finite seed realizing an alternating wall, it would suffice to prove B(L,tau) empty for every L; that stronger finite-left assertion is not proved here. If a class is nonempty, full finite-right support remains an additional obligation. The next invariant must address an aperiodic companion inside these explicit classes, rather than unrestricted Lambda+ or a periodic closure. No new channel census is requested.

*Second reader's note on G129 (Local, 2026-10-06; chat L083).* Correct. With the wall fixed, the left half evolves
deterministically from its initial left row, the white-time wall equation forces each visible bit and the black-time
one constrains only the left trace, so a seed determines at most one visible itinerary. Two connections. First, the
record's exact zero-run records next to $0101\ldots$ (RULE30-PRIZE.md §8.36, §8.37; PERIOD-TWO.md Q6: no left half is
zero from any depth up to 85, for every column 1) are finite certificates of exactly G129's kind: they show
$B(L, 0101\ldots)$ empty for every $L$ up to about 84, and Conjecture LR (or the doubling conjecture) for every column
1 would make it empty for every $L$. Second, an independent direct check (`rule30_audit_g99_g100.py`, S27): every
left seed of radius $L \le 10$ evolved against the alternating wall, in either phase, violates the black-time equation
within 18 ticks, so those classes are empty with very small boxes (death times 1, 7, 7, 7, 7, 9, 9, 9, 17, 17, 17 for
the phase starting white).

### G.GPT130. a fixed right tail gives a unique left seed for every wall (second-read by Local, 2026-10-06)

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

### G.GPT131. the Sturmian exclusion survives every finite block factor (second-read by Local, 2026-10-06)

### G131. The Sturmian exclusion survives every finite block factor (2026-10-06)

**Status and purpose.** Symbolic extension of RULE30-PRIZE.md section 8.57's Theorem E; independently verified by Local L085. No experiment. The target is the open rotation-code lead in PERIOD-TWO.md question 7, without assuming a periodic companion. The counterfactual is that a finite recoding can remove the early repetitions responsible for Theorem E. The proof retains the exact fixed margin. Prior art: finite block coding and orbit-endpoint rotation partitions are standard; the abstract of Kupsa and Starosta, [On the partitions with Sturmian-like refinements (2015)](https://www.aimsciences.org/article/doi/10.3934/dcds.2015.35.3483), discusses this class and stronger refinement results. Only the abstract was read; no refinement or injectivity theorem is imported. The result below is a corollary of the project's existing repeat obstruction, not a novelty claim about Sturmian coding.

**Theorem.** Let g be any irrational Sturmian sequence, with any phase. Let F be any binary function of a fixed block of width w+1, and set c_s=F(g_s,...,g_(s+w)) for s>=0. If c is column 1's visible sequence beside the alternating Rule 30 wall 0101..., the forced initial left row cannot be eventually zero. No injectivity, nonconstancy or aperiodicity premise is imposed on F.

**Proof.** Section 8.57 Step 0 says finite left support would supply a fixed constant C>=0 such that every repetition c_s=c_(s+q) on a<=s<=b, q>=1, obeys

    b <= 2a+q+C.                         (repeat bound)

Enlarging a possibly negative original C only weakens this necessary bound. Suppose g_s=g_(s+q) on a<=s<=e. If e>=a+w, then c repeats on a<=s<=e-w, so e<=2a+q+C+w. If e<a+w, the same inequality holds automatically. Thus finite left support for c would make every repetition of g obey the repeat bound with constant C+w. The continued-fraction argument in section 8.57 Steps 1 to 4 proves that no irrational Sturmian sequence, at any phase, can obey that bound with any fixed constant. Its proof uses only the repeat bound after Step 0, so it applies here unchanged. This contradiction proves the theorem. The margin is w, not a scale-dependent loss.

A finite block function using shifts m,...,M of a bi-infinite mechanical word is also covered: rephase the Sturmian input by m and take w=M-m. Likewise an eventual finite-block coding is excluded once the clock and coding have both begun: restart at an even physical time beyond that prefix. Finite initial left support remains finite at that time by the light cone.

**Corollary: every finite union of arcs with endpoints on one rotation orbit.** Let 0<alpha<1 be irrational, let f be a binary, right-continuous step function on the circle, and suppose its actual jump endpoints all have the form beta+k_j*alpha modulo one, with finitely many integer k_j. Then c_s=f(theta+s*alpha) is excluded beside 0101... for every theta and every alpha, including bounded-partial-quotient angles. This covers multiple arcs, not just the original interval of length alpha.

Here is a direct finite-block construction, with exact endpoint conventions. Put y=x-beta and g(y)=1 on [1-alpha,1), zero elsewhere. A binary circular step function has an even number of jump endpoints. Over GF(2), form the Laurent polynomial

    Q(z)=sum_j z^(k_j)=(1+z)*P(z).

The divisibility follows from Q(1)=0 after multiplication by a power of z to clear negative exponents. For each nonzero coefficient P_k define

    h(y)= XOR_k g(y-(k+1)*alpha).

The k-th term jumps at k*alpha and (k+1)*alpha, so the jump set of h is precisely Q: interior endpoints cancel modulo two. Thus f(beta+y) and h(y) have the same jumps and differ by one constant bit. Right-continuity makes the equality hold at the endpoints as well. Along the orbit this is a finite XOR block code of one rephased Sturmian word, plus that constant. The theorem therefore applies. A constant f is the empty-code case and is covered too.

**Unexpected degeneracy check.** With irrational 0<alpha<1/2, the standard Sturmian word has no adjacent ones: rotating its one interval [1-alpha,1) by alpha lands in [0,alpha), where the next bit is zero. Hence the finite block factor F(u,v)=u AND v is constantly zero, not Sturmian. The proof still excludes it, directly through the repeat bound. Therefore the argument must use inherited repetitions rather than assert that a finite factor stays Sturmian or invertible. This is the identified independent check.

**Scope and lead status.** The one-orbit-endpoint subclass of question 7 is now covered for all phases and all irrational angles, conditional only on the already proved Theorem E repeat argument. Endpoints on unrelated rotation orbits with bounded partial quotients remain open; a finite recoding of several differently phased Sturmian words does not guarantee a common long repeat. Torus rotations, kicked codes and general aperiodic companions remain outside this result. It is a class exclusion for the finite-left problem, not the prize's exclusion of every companion.

*Second reader's note on G131 (Local, 2026-10-06; chat L085).* Correct. A repetition of $g$ on $[a, e]$ gives one of
the block code on $[a, e - w]$, so Step 0's bound passes to $g$ with constant $C + w$; and Theorem E's Steps 1 to 4
(RULE30-PRIZE.md §8.57) apply that bound only to stretches where the Sturmian word itself repeats with period $q_n$,
so they run unchanged on $g$. The corollary's construction is right: an even number of endpoints gives $Q(1) = 0$, and
each $g(y - (k+1)\alpha)$ codes $[k\alpha, (k+1)\alpha)$, so the XOR has exactly $Q$'s jumps. Checked
(`rule30_audit_g99_g100.py`, S29): for 40 random one-orbit arc unions at two irrational angles, $f(\beta + y) \oplus h(y)$ is constant along 20,000 orbit points; for $\alpha < 1/2$ the Sturmian word has no adjacent ones; block codes
inherit repetitions as stated. This closes the one-orbit part of PERIOD-TWO question 7 for every angle; arcs with
unrelated endpoints and small partial quotients remain open, as G131 says.

### G.GPT132. circle-covering codes and one-character torus codes are excluded (second-read by Local, 2026-10-06)

### G132. Circle-covering codes and one-character torus observables are excluded (2026-10-06)

**Status and target.** Corollary of G131 and G27.2; independently verified with G131 by Local L086. No experiment or novelty claim for integer characters. Target: clarify which multi-orbit and torus codes the finite-block argument already excludes. Counterfactual: a circle covering or additional unobserved torus coordinates automatically evade the Sturmian obstruction. A genuine two-coordinate box below is the unexpected scope check.

**Statement.** Let the torus orbit be x_s=theta+s*omega modulo one in each of d coordinates. Fix an integer vector v and the circle projection

    h_v(x)=sum_j v_j*x_j modulo one,
    beta=h_v(omega).

Observe c_s=psi(h_v(x_s)). If beta is rational, every such deterministic observable psi gives a periodic c and is excluded beside the alternating Rule 30 wall with finite initial left support. If beta is irrational, the same exclusion holds whenever psi is a binary finite-union-of-arcs code whose jump endpoints lie on one beta-rotation orbit. Arbitrary fixed choices at the endpoints are allowed. In both cases no assumption is made about periodicity of the actual right-neighbor trace at its hidden phases.

**Proof.** Integer coefficients make h_v well-defined on the torus. Direct addition gives

    h_v(x_s)=h_v(theta)+s*beta modulo one.

For rational beta with denominator q these projected points repeat every q samples, hence c is periodic. The corresponding nearest-left trace is periodic: at even physical times it is 1-c_s, and at odd times it is one. G27.2 excludes this pair for finite initial left support, independently of the right half.

For irrational beta, the projected observable is exactly a circle rotation code of the class in G131, so its finite-block exclusion applies for every starting phase. If endpoint values differ from the half-open convention used there, each endpoint is visited at most once: two visits would make a nonzero multiple of beta integral. There are finitely many endpoints, so the code eventually agrees with the half-open code. G131's eventual-factor clause therefore preserves the exclusion. This also explains why endpoint exceptions do not create a new companion class.

**Circle coverings give a concrete multi-orbit case.** In dimension one take v=2, irrational alpha as omega, and beta=2*alpha modulo one. Let psi be the standard Sturmian interval [1-beta,1). Then f(x)=psi(2*x modulo one) is a two-arc observable for the original alpha rotation. Its endpoint set is

    {0, 1/2, -alpha, 1/2-alpha} modulo one.

The two original alpha-orbit classes represented by 0 and 1/2 are distinct: an equality 1/2=k*alpha modulo one would make alpha rational for nonzero integer k. Thus f does not have all endpoints on one original orbit, yet its sampled code is Sturmian for the projected angle beta and is excluded. More generally any integer circle covering can be used. This narrows part of the unrelated-endpoint lead; it does not exclude arbitrary unrelated endpoints without such a quotient structure.

**Unexpected genuinely multidimensional guard.** On the two-torus, let f(x,y)=1 when both x and y lie in [0,1/2), zero otherwise. This observable cannot be a function of any single integer character h_(a,b). A function of that character would be invariant under every translation (b*t,-a*t), since the character changes by zero. If b is nonzero, choose x just below 1/2 and y=1/4; a sufficiently small such translation crosses the x boundary while keeping y interior, so f changes. If b=0 and a is nonzero, a vertical translation changes f while leaving the character fixed. The zero character would require f constant. All cases contradict factorization. Therefore this corollary makes no claim about genuinely two-coordinate box codes, nor about the general torus lead. This is a geometric scope check, not a Rule 30 counterexample or a claim that a box code supplies a finite witness.

**Resulting boundary.** The class exclusion includes finite recodings after a one-circle projection, even when the original partition has multiple orbit classes or the underlying motion has several torus coordinates. General partitions using independent coordinates, arbitrary unrelated circle endpoints and kicked observables remain open. No uniform finite-left exclusion or prize solution follows.

*Second reader's note on G132 (Local, 2026-10-06; chat L086).* Correct, with its G131 dependency reviewed above. The
character projection is linear along the orbit; rational $\beta$ gives a periodic code (G27.2), irrational $\beta$ a
rotation code whose endpoints are each visited at most once, so G131's eventual clause applies. Checked
(`rule30_audit_g99_g100.py`, S30): the covering example's jumps sit exactly at $\{0, 1/2, -\alpha, 1/2 - \alpha\}$ for
two irrational angles (with $2\alpha$ on either side of 1), on two distinct $\alpha$-orbits, and its orbit code
equals the $2\alpha$-Sturmian code for 20,000 steps; the box $[0, 1/2)^2$ is not a function of any nonzero character
with coefficients up to 4. PERIOD-TWO question 7's row now records the one-orbit and one-character exclusions.

### G.GPT133. golden-angle codes cannot be rescued by super-geometric kicks (second-read by Local, 2026-10-06)

### G133. Golden-angle codes cannot be rescued by super-geometrically separated kicks (2026-10-06)

**Status and target.** Quantitative extraction from Theorem E's existing continued-fraction proof; independent review pending. No experiment. G131/G132 are verified by Local L085/L086. Target: advance the kicked-code part of PERIOD-TWO question 7 with an aperiodic base, rather than another exact-code reformulation. Counterfactual: zero kick density alone permits arbitrarily long unbroken Sturmian stretches beside a finite left seed. The conservative constants below are not optimized. The dyadic-kick guard prevents an entropy or all-kicks exclusion claim.

Let alpha=(sqrt(5)-1)/2 and g_s=1 when theta+s*alpha modulo one belongs to [1-alpha,1), with any theta. Assume the Rule 30 wall is 0101... from time zero and the initial left row is zero beyond radius L.

**Finite repetition lemma.** For every integer C>=0, a golden-angle Sturmian prefix through index

    N=84*(C+4)

cannot obey the finite repeat bound b<=2a+q+C for every repetition g_s=g_(s+q) on a<=s<=b with b+q<=N. In particular a visible companion cannot agree with such a Sturmian word through index 84*(L+4). The L=0 left seed already fails the first black-time equation; for L>=1 Theorem E Step 0 supplies a repeat constant no larger than L.

**Finite-horizon proof.** Use section 8.57's convergent notation q_n, delta_n, K_n and the first two visit times h,h' to K_n. For a fixed q=q_n, if N>=4q+3C+8, the finite repeat bound alone forces

    h <= q+C+2,
    h' <= 2h+q+C+4.

Indeed, if h>q+C+2, the repetition from 0 through q+C+1 violates the bound; all compared samples lie within N. After the first visit, if h'>2h+q+C+4, the repetition from h+1 through 2h+q+C+3 violates the bound. Its last compared index is at most 4q+3C+7, using the first inequality. These are exactly Theorem E's two visit inequalities, obtained without assuming the second visit was already observed. As in that proof, returns to K_n are at least q_(n+1) apart. Thus

    q_(n+1)-q_n-C-4 <= h(n) <= q_n+C+2.       (visit bounds)

Choose n minimally so q_(n-1)>2C+8. For the golden angle all partial quotients are one. The separation argument of Theorem E Step 4, applied at n and n+1, gives

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

Here its prerequisites are just the visit bounds at n,n+1,n+2 and q_(n-1)>2C+8: the two arcs at successive scales are disjoint and closer than delta_(n-1), and the only possible signed return in the bounded visit-time difference is -q_n. No extra hypothesis about the Rule 30 orbit enters this separation step.

The visit bounds and first identity give h(n)>=q_(n-1)-C-4. The second identity and the upper visit bound at n+2 give h(n+1)<=q_n+C+2. Combining these with the first identity yields q_(n-1)<=2C+6, a contradiction.

All three scales are present in the stated horizon. Minimality and the Fibonacci recurrence imply q_(n-1)<=4C+16 and q_(n+2)<=5q_(n-1)<=20C+80. Therefore

    4q_(n+2)+3C+8 <= 83C+328 < 84*(C+4).

This proves the finite repetition lemma.

**Unbroken stretches at later times.** If the visible companion agrees with a golden-angle Sturmian word from visible index a through b, restart at physical time 2a. The left-zero radius is then at most L+2a by the light cone, and the wall has the same phase. The finite lemma, with this larger radius and arbitrary rephased theta, requires

    b-a < 84*(L+2a+4).

This statement does not require the companion to be periodic or the rest of it to be Sturmian.

**Necessary kick-gap bound.** Suppose c equals a fixed golden-angle Sturmian word except at its actual disagreement indices k_0<k_1<.... Finite support requires infinitely many disagreements, since an eventual exact code is already excluded by G131. Before the first kick, the finite lemma gives k_0<=84*(L+4). Between consecutive kicks use a=k_j+1 and b=k_(j+1)-1. The preceding inequality yields the conservative integer bound

    k_(j+1) <= 169*k_j + 84*L + 505.

Thus schedules with unbounded ratios k_(j+1)/k_j are excluded. In particular, flipping the Sturmian bit at every index 2^(2^j) cannot give a finite-left companion, for any phase and any L. This is an infinite class exclusion from a uniform finite-horizon argument, not evidence extrapolated from measured kicks.

**Unexpected checks and limits.** The Fibonacci sizes 13,21,34,55 at C=0 give a hand check of the three-scale horizon: 4*55+8=228<336. More importantly the zero-density schedule k_j=2^j satisfies the derived kick-gap and first-kick bounds for every L>=1. The theorem therefore does not exclude every sparse schedule or establish positive entropy, positive kick density or realizability of dyadic kicks. It supplies only a necessary upper bound on consecutive disagreement times. The actual measured rational wheel, arbitrary irrational angles, phase-reset kicks and genuinely multidimensional codes are outside this golden-base result. These are the identified independent scope checks.

*Second reader's note on G133 (Local, 2026-10-06; chat L087).* Correct. Both visit inequalities are obtained from
repetitions whose compared samples end by index $4q + 3C + 7$; for the golden angle $q_{n+1} - q_n = q_{n-1}$, and the
two Step 4 identities give $q_{n-1} \le 2C + 6$, against the choice $q_{n-1} > 2C + 8$; $q_{n+2} \le 5 q_{n-1} \le 20C + 80$ puts all three scales inside $84(C + 4)$; restarting at physical time $2a$ gives the kick-gap recursion
$k_{j+1} \le 169 k_j + 84L + 505$. Checked (`rule30_audit_g99_g100.py`, S31): for 30 random phases and $C = 0, 2, 5$
every golden prefix of length $84(C + 4)$ contains a violating repetition; descriptively the latest first violation
over those phases came at prefix lengths 27, 45 and 74, about a tenth of the proved horizons, so the constants could
be tightened; the Fibonacci hand check and the two kick schedules (excluded $2^{2^j}$, admitted $2^j$) check.

### G.GPT134. bounded-type rotation codes need geometrically spaced corrections (second-read by Local, 2026-10-06)

### G134. Bounded-type rotation codes require geometrically spaced corrections (2026-10-06)

**Status and target.** Symbolic extension of G133, independent review pending. No experiment or new numerical prediction. Theorem E and G2.2 supply the continued-fraction facts; G133 supplies the finite comparison deadlines. Target: remove the golden-angle restriction from the sparse-kick exclusion. Counterfactual: bounded partial quotients might still allow corrections with unbounded successive spacing ratios beside a finite left seed. The proof below excludes that possibility. This is a consequence of the existing repetition obstruction, with no general novelty claim.

Let alpha in (0,1) be irrational with every partial quotient a_j<=A, where A>=1 is an integer. For any phase theta let g be its standard half-open Sturmian code. Define

    K_A=8*(A+1)^4+3.

**Finite-prefix theorem.** For every integer C>=0, the prefix of g through index N=K_A*(C+4) cannot satisfy b<=2a+q+C for every repetition g_s=g_(s+q) on a<=s<=b with b+q<=N.

Use Theorem E's convergents q_n, errors delta_n, mismatch arcs K_n and first visit h(n). G133's finite comparison argument, valid for every irrational angle once these mismatch arcs have the stated form, gives

    q_(j+1)-q_j-C-4 <= h(j) <= q_j+C+2

whenever N>=4q_j+3C+8. Choose n minimally with q_(n-1)>T=2C+8. The initial denominator q_0=1 is below T. Minimality and q_j=a_j*q_(j-1)+q_(j-2) give q_(n-1)<=(A+1)*T. Thus

    q_(n+2) <= (A+1)^3*q_(n-1) <= (A+1)^4*T,
    4q_(n+2)+3C+8 <= K_A*(C+4).

The visit bounds therefore hold at all three indices n,n+1,n+2. If any of a_(n+1),a_(n+2),a_(n+3) is at least two, the corresponding visit bounds imply q_(j-1)<=2C+6, impossible. All three coefficients must consequently be one.

**Quantitative separation, including the finite-offset check.** Put D=2C+6. At j=n and j=n+1, the opposite mismatch arcs are disjoint, their combined length is |delta_(j-1)|, and the visit bounds place

    m=h(j)-h(j+1) in [-q_j-D,D].

Also m is nonzero and ||m*alpha||<|delta_(j-1)|. Best approximation forces |m|>=q_j. Since D<q_(j-1)<=q_j, this means m=-q_j-r with 0<=r<=D. If r>0, then r<q_(j-1), so the preceding best-approximation bound and the error recurrence give

    ||r*alpha|| >= |delta_(j-2)|
                 = a_j*|delta_(j-1)|+|delta_j|
                 >= |delta_(j-1)|+|delta_j|.

The triangle inequality on the circle now gives ||(q_j+r)*alpha||>=|delta_(j-1)|, a contradiction. Hence r=0 exactly, and

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

This finite-offset argument uses no unspecified sufficiently-large threshold or phase-dependent distance. It also supplies the explicit justification for G133's quantitative use of Theorem E Step 4. At the selected indices the standard mismatch description applies: n>=2; if n=2 then q_1>T forces alpha<1/8, and later convergent errors are smaller than both coding-interval lengths. The same assertion at n>=3 follows from the first convergent errors and their monotone decrease.

Finally the lower visit bound at n is h(n)>=q_(n-1)-C-4. The second identity and upper bound at n+2 give h(n+1)<=q_n+C+2. Substituting the first identity forces q_(n-1)<=2C+6, again a contradiction. This proves the finite-prefix theorem.

**Finite-left companion consequence.** Let the Rule 30 wall be 0101... and its initial left row be zero beyond radius L>=1. Theorem E Step 0 permits repeat constant C=L. Restarting at physical time 2a enlarges the left-zero radius to at most L+2a. Any matching stretch with this fixed-angle Sturmian code, rephased as necessary, obeys

    b-a < K_A*(L+2a+4).

For the actual disagreement indices k_0<k_1<... against a fixed base code, G131 already excludes finitely many disagreements. The finite-prefix theorem and the intervals between disagreements give

    k_0 <= K_A*(L+4),
    k_(j+1) <= (2K_A+1)*k_j + K_A*L + 6K_A + 1.

Thus unbounded ratios k_(j+1)/k_j are impossible for every bounded-type irrational angle, every phase and every finite left radius. In particular super-geometric flip schedules are excluded throughout this class. The sharper golden constant in G133 remains useful; this uniform class constant is deliberately conservative.

**Independent and unexpected scope checks.** The finite-offset check above is independent of G2.2's asymptotic eta argument and is the identified unexpected check. At A=1 this theorem gives K_A=131 rather than G133's 84, a consistency check without an optimality claim. The schedule k_j=2^j still satisfies the resulting necessary bounds for L>=1, so this argument establishes neither positive kick density nor positive entropy nor realizability. For unbounded partial quotients, the controlled denominator growth used to choose a linear horizon fails; this proof supplies no uniform linear bound there. Arbitrary phase-reset kicks, the measured rational wheel and genuinely multidimensional observables remain outside the claim.

### G.GPT135. a uniform Sturmian horizon bounds phase and angle resets (second-read by Local, 2026-10-06)

### G135. A uniform Sturmian horizon also bounds phase and angle resets (2026-10-06)

**Status and target.** Symbolic proof, independent review pending; no experiment. G133 is independently verified by Local L087; G134 is awaiting review. This strengthens their angle scope rather than optimizing the golden constant. Counterfactual: a huge continued-fraction coefficient could postpone the next usable scale beyond every horizon proportional to the left radius. The finite repetition bound itself prevents that escape. All inputs are the existing Theorem E continued-fraction facts and the explicit G134 finite-offset argument; no general novelty claim.

**Uniform finite-prefix theorem.** For every irrational alpha in (0,1), every phase theta and every integer C>=0, its standard half-open Sturmian prefix through

    N=251*(C+4)

contains a repetition g_s=g_(s+q) on a<=s<=b with b+q<=N and b>2a+q+C. There is no bound on partial quotients in this statement.

Suppose otherwise. Put T=2C+8. Choose n minimally with q_(n-1)>T and put r=n-2. Then q_r<=T. At every usable scale j the finite comparison deadlines of G133 give

    q_(j+1)-q_j-C-4 <= h(j) <= q_j+C+2,
    q_(j+1) <= 2q_j+2C+6 < 2q_j+T,

provided N>=4q_j+3C+8. The second line is the crucial replacement for an externally assumed bound on partial quotients.

The starting scale r is usable, including its small-index cases. If r=0, q_1>T implies alpha<1/8; delta_0=alpha and the two mismatch arcs for period q_0=1 are disjoint, so Theorem E's break description and return gap at least q_1 hold. If r>=1, |delta_r| is at most min(alpha,1-alpha), making the same break description valid. Indeed, when a_1=1, |delta_1|=1-alpha; when a_1>=2, the recurrence alpha=a_2*|delta_1|+|delta_2| gives |delta_1|<alpha. Later errors decrease. Equality of an error with the shorter interval length merely makes the mismatch arcs touch at a half-open endpoint; it does not create an overlap.

Starting with q_r<=T, apply the growth inequality successively at r,r+1,r+2,r+3. Every application is justified within the fixed horizon, because the resulting bounds are

    q_(n-1) < 3T,
    q_n < 7T,
    q_(n+1) < 15T,
    q_(n+2) < 31T,

and

    4*(31T)+3C+8 = 251C+1000 < 251*(C+4).

Thus the visit bounds hold at n,n+1,n+2 as well. This is an induction on already bounded denominators, not a circular assumption that the later scales fit.

At those three scales, any coefficient a_(j+1)>=2 would give q_(j-1)<=2C+6, contradicting q_(n-1)>T. Hence a_(n+1),a_(n+2),a_(n+3) must all be one. The explicit separation in G134 applies at n and n+1: for m=h(j)-h(j+1), best approximation gives m=-q_j-u with 0<=u<=2C+6; a positive u<q_(j-1) would give

    ||(q_j+u)*alpha|| >= |delta_(j-2)|-|delta_j|
                         >= |delta_(j-1)|,

contrary to the distance across the opposite mismatch arcs. Therefore

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

Combining the lower visit bound at n with the upper bound at n+2 yields q_(n-1)<=2C+6, the final contradiction. The uniform finite-prefix theorem follows.

**Companion and reset consequences.** Beside a Rule 30 wall 0101... with initial left-zero radius L>=1, any interval [a,b] matching a standard irrational Sturmian code obeys

    b-a < 251*(L+2a+4).

The phase and angle may be chosen separately for each interval: restart at physical time 2a, use the light-cone radius L+2a and apply the uniform theorem with repeat constant C=L+2a. No relation between the different intervals' angles is required.

Consequently, if a companion is made of consecutive Sturmian-coded pieces with reset times 0=t_0<t_1<..., even allowing both phase and angle to change at each reset, it necessarily satisfies

    t_(j+1) <= 503*t_j + 251*L + 1004.

A final infinite piece is impossible. Super-geometrically separated resets cannot support a finite left seed. For actual disagreements k_j against one fixed irrational Sturmian base, the corresponding statement is

    k_0 <= 251*(L+4),
    k_(j+1) <= 503*k_j + 251*L + 1507.

This excludes super-geometric flips for every irrational base angle, including unbounded-type angles. The improved golden constant of G133 is still stronger within its narrower class.

**Unexpected independent checks and limits.** A tiny alpha whose first denominator is enormous is the identified unexpected check: the initial q_0=1 scale already forces q_1<=2C+8, so the proof never waits for that enormous denominator. The complementary near-one case uses q_1=1 and its short error, rather than incorrectly using the long q_0 mismatch arc. These endpoint-angle controls justify the uniform claim. Dyadic times still pass the necessary bounds, so no positive density, positive entropy or realizability conclusion follows. The pieces must use the standard Sturmian interval (or its complement, which has identical repetitions); arbitrary arc observables and the measured rational wheel are not asserted to have this form. This is a class exclusion for companions, not a prize solution.

*Second reader's note on G134 and G135 (Local, 2026-10-06; chat L088).* Both correct. G134: minimality gives
$q_{n-1} \le (A+1)T$ and $q_{n+2} \le (A+1)^4 T$, hence $K_A = 8(A+1)^4 + 3$ (131 at $A = 1$); the finite-offset step
is sound, since $0 < r \le D < q_{j-1}$ would give $\|r\alpha\| \ge |\delta_{j-2}| \ge |\delta_{j-1}| + |\delta_j|$
and so $\|(q_j + r)\alpha\| \ge |\delta_{j-1}|$, and that step also supplies the explicit form of Theorem E Step 4
that G133 used. G135: the visit bounds themselves give $q_{j+1} \le 2q_j + 2C + 6$, and starting from $q_r \le T$
each step uses a horizon already justified ($3T, 7T, 15T, 31T$), so $4 \cdot 31T + 3C + 8 = 251C + 1000$ fits inside
$251(C + 4)$ with no bound on partial quotients; the tiny-angle and near-one starts are handled correctly. Checked
(`rule30_audit_g99_g100.py`, S32): for the golden angle, $\sqrt 2 - 1$, $e - 2$, $\pi - 3$, a tiny angle
$1/(50 + \varphi)$ and one minus it, at 10 random phases each and $C = 0, 2$, every prefix of length $251(C + 4)$
contains a violating repetition; the latest first violation over all of them came at prefix length 45, so the
uniform constant is very conservative.

### G.GPT136. uniform recoding horizons include rational mechanical bases (second-read by Local, 2026-10-06)

### G136. Uniform recoding horizons include rational mechanical bases (2026-10-06)

**Status and purpose.** Symbolic corollary of G131 and G135; independent review pending. Dependencies G134/G135 are independently verified by Local L088. No experiment. Counterfactual: either a finite recoding margin or a rational limiting angle might evade the uniform horizon. The exact margin and a finite-prefix approximation settle both. This advances recoded/reset companions, not the missing entropy theorem. The inherited rotation-partition prior art is recorded in G131; no general novelty claim.

Let g_s be the standard mechanical code of theta+s*alpha modulo one in [1-alpha,1), now allowing every alpha in [0,1]. The endpoint angles give the constant zero and constant one codes. Let F be any binary function of a block of width w+1, w>=0, and put c_s=F(g_s,...,g_(s+w)). Define

    H(C,w)=251*(C+4)+250*w.

**Finite-prefix theorem.** For every integer C>=0, the prefix of c through index M=H(C,w) contains a repetition c_s=c_(s+q) on a<=s<=b with b+q<=M and b>2a+q+C. Neither injectivity nor nonconstancy of F is needed.

First extend G135 to rational and endpoint angles. Every finite prefix g_0,...,g_N of the specified mechanical code is also a prefix of an irrational mechanical code with slightly perturbed angle and phase. To see the boundary issue explicitly, change the angle by epsilon and increase the phase by eta, choosing eta>(N+1)*abs(epsilon), with both arbitrarily small. At a sample exactly on the upper endpoint 0 modulo one, its displacement is eta+s*epsilon>0, giving the correct right-hand value zero for an interior angle. At a sample on the lower endpoint 1-alpha, its displacement relative to that moving endpoint is eta+(s+1)*epsilon>0, giving the correct right-hand value one. All other finitely many samples have a positive margin and keep their value for sufficiently small changes. Choose the perturbed angle irrational. For alpha=0, choose a small positive angle and a phase perturbation larger than the total drift; every sample stays outside its tiny one-interval. For alpha=1, choose an angle just below one and the same dominating positive perturbation; every sample stays inside the one-interval. Thus the finite-prefix contradiction of G135 holds for every mechanical angle.

Now suppose c satisfies the finite repeat bound through M. The underlying mechanical prefix is available through N=M+w=251*(C+w+4). If g repeats on [a,e] with e+q<=N and e>=a+w, then c repeats on [a,e-w], and its compared samples end by N-w=M. Hence e<=2a+q+C+w. If e<a+w, the same inequality is automatic. Every repetition of g through N would therefore satisfy the forbidden bound with constant C+w, contradicting the extended G135 theorem. This proves the claim and explains why the margin is 250*w rather than an unspecified additive loss.

**Matching pieces and corrections.** Beside the alternating Rule 30 wall with initial left-zero radius L>=1, a companion cannot match such a recoded mechanical word on [a,b] unless

    b-a < H(L+2a,w).

For pieces with reset times t_j and widths bounded by one fixed w, the functions, angles and phases may change from piece to piece, but necessarily

    t_(j+1) <= 503*t_j + 251*L + 1004 + 250*w.

For actual disagreement indices against one fixed recoded mechanical base, the bounds are

    k_0 <= 251*(L+4)+250*w,
    k_(j+1) <= 503*k_j + 251*L + 1507 + 250*w.

Finitely many disagreements or a final infinite piece are impossible by the same finite-prefix theorem at a later restart. Consequently super-geometrically spaced resets or corrections are excluded for bounded-width recodings at every mechanical angle. These are necessary bounds, not a construction of a realizable companion.

**Orbit-endpoint interpretation.** G131 constructs a finite block code for any half-open binary arc partition whose actual jump points have the form beta+k_j*alpha. If the integer exponents span D=max(k_j)-min(k_j)>=1, its Laurent polynomial Q(z)=sum(z^k_j) has an even number of jumps and Q=(1+z)P. P has exponent span D-1, so after rephasing its block width parameter is w=D-1. The same construction works for rational angles: distinct actual jump points are listed once, and equality of the jumps leaves only a constant difference, absorbed in F. Constant partitions use w=0. Thus pieces whose endpoint representations have uniformly bounded exponent span inherit the reset bound, even if their angles and partitions vary. The controlling parameter here is exponent span, not merely the number of endpoints. No arbitrary unrelated-endpoint partition is claimed to have this representation.

**Unexpected width guard, proved without a run.** An unrestricted finite block code can fit any prescribed finite binary prefix. Fix an irrational Sturmian g and finitely many starting indices 0,...,m. Their infinite future tails are pairwise distinct: equality of two would give an eventually periodic mechanical code, impossible because its symbol frequency is irrational. For each pair there is a finite first differing coordinate; take w at least the largest such coordinate. All the blocks g_s,...,g_(s+w) at these indices are distinct. Define F on them to output the desired prefix, and define it arbitrarily elsewhere. This does not give an infinite prescribed word, a uniform w or a finite-left Rule 30 realization. In particular the record's overlap-free Thue-Morse prefixes can pass the repeat inequality for arbitrary finite horizons while being fitted by increasingly wide recodings. A horizon independent of all recoding widths is therefore false. This is the identified independent scope check. At w=0 the theorem recovers G135 and its rational extension; constant F also retains the immediate period-one obstruction. Geometric correction schedules still pass the displayed necessary bounds, and no positive density, entropy or prize solution follows.

*Second reader's note on G136 (Local, 2026-10-06; chat L089).* Correct. The perturbation is sound: with
$\eta > (N + 1)|\epsilon|$ a sample on either endpoint moves to the correct side of the moved interval, and every other
sample keeps a positive margin; the prefix through $N = M + w = 251(C + w + 4)$ carries repetitions of $g$ to
repetitions of $c$ with constant $C + w$, which is where $H(C, w) = 251(C + 4) + 250w$ comes from; the reset and
disagreement recursions follow. Checked (`rule30_audit_g99_g100.py`, S33): exact rational mechanical codes
($\alpha = 0, 1, 1/2, 2/5, 3/7$) and random block codes of width up to 4 over irrational and rational mechanical words
all violate within $H(C, w)$; for the width guard, fitting the first 121 Thue–Morse bits by a recoding of a golden
Sturmian word needs width 204 here, and that Thue–Morse prefix (overlap-free) passes the repeat bound with $C = 0$,
so no width-independent horizon exists, as G136 says.

### G.GPT137. a dyadic sparse word passes every repeat test; faster powers fail (second-read by Local, 2026-10-06)

### G137. A dyadic sparse word passes every repeat test; faster powers fail (2026-10-06)

**Status and target.** Symbolic obstruction audit, independent review pending; no experiment. G134/G135 are verified by Local L088 and G136 awaits review. Counterfactual: using every period and every starting position in Theorem E Step 0, rather than only the derived kick recursion, might rule out all geometrically sparse corrections or force positive word-count entropy. The explicit dyadic word refutes that inference. This strengthens the scope guard rather than claiming a Rule 30 realization. The existing Thue-Morse guard in section 8.57 already shows that the repeat inequality alone is not an entropy theorem; the new point is its exact compatibility with sparse geometric defects. G26/G64 concern a different Rule210 dyadic-run construction and do not supply a Rule30 realization here.

Let d_s=1 precisely when s=2^j for some integer j>=0, and d_s=0 otherwise, including d_0=0.

**Every repetition obeys the strongest nonnegative-margin test.** If d_s=d_(s+q) for every a<=s<=b, where a>=0 and q>=1, then

    b <= 2a+q-1.

For a>=1, choose the smallest power of two p>=a, so p<=2a. If p+q is not a power of two, there is a mismatch at s=p. If p+q=P is a power of two, then P>=2p and p+2q=2P-p lies strictly between P and 2P. Thus there is a mismatch at s=P=p+q. In both cases a mismatch lies in [a,2a+q], proving the bound.

For a=0, if q is a power of two, s=0 is already a mismatch. Otherwise q>=3. If q+1 is not a power of two, s=1 is a mismatch; if q+1 is a power of two, s=2 is a mismatch since q+2 lies strictly between q+1 and its double. In either case the first mismatch is at most q, giving b<=q-1 as required. The reasoning covers every q, not only a selected sequence of convergent periods.

Consequently d satisfies the necessary finite-left repeat bound b<=2a+q+C for every C>=0, all periods and all starting positions. Passing this necessary condition does not establish a compatible forced left row, a full right evolution or a finite global seed.

**Sparse, aperiodic and zero word-count entropy.** The ones have zero density because their count up to N is at most 1+floor(log_2 N). They are infinite but have unbounded gaps, so d is not eventually periodic. For a factor length m>=1, starts a<m contribute at most m different words. For a>=m, two powers of two cannot both lie in [a,a+m-1]: their separation is at least a>=m. Such factors have at most one one, giving at most m+1 possibilities. Therefore the number P(m) of distinct length-m factors obeys

    P(m) <= 2m+1,
    limsup log_2(P(m))/m = 0.

This is word-count entropy of this one word, not the dynamical entropy of Rule 30. Complementing d preserves all repetition tests and its factor complexity.

**Unexpected rate control.** For an integer B>=3 let d^(B) have ones at B^j and zero elsewhere. For sufficiently large p=B^j, between p and Bp the period-one equality stretch has a=p+1 and b=Bp-2. The repeat bound would require

    (B-2)*p <= C+5.

It fails for arbitrarily large p, for every fixed C. Thus these faster geometric isolated-one schedules are excluded for a finite-left alternating-wall companion by Theorem E Step 0 alone. Powers of two are the exact surviving integer-base case for this necessary test. This is the identified independent check: geometric spacing is not a single undifferentiated regime. No experiment or claim about irrational-base flips is used in this control.

**Closed bridge and next obligation.** Do not try to deduce positive entropy, positive defect density or exclusion of every geometric schedule solely from the repeat inequality, even when all q and a are imposed. The explicit sparse word passes the full family. Adding it to a Sturmian base need not preserve that property, so this does not prove that a dyadically flipped Sturmian word passes the tests or is realizable. A useful next proof must use a further Rule30 wall constraint, a relation across the corrections, or the coupled-tail condition of G130. The finite-left sufficiency question for d itself is not answered here.

*Second reader's note on G137 (Local, 2026-10-06; chat L090).* Correct. For $a \ge 1$ the first power of two
$p \ge a$ satisfies $p \le 2a$; either $p + q$ is not a power of two, or $P = p + q$ is and $2P - p$ lies strictly
between $P$ and $2P$, so a mismatch falls in $[a, 2a + q]$; the $a = 0$ cases check; at most $2m + 1$ factors of length
$m$; for base $B \ge 3$ the zero stretch between $p$ and $Bp$ forces $(B - 2)p \le C + 5$. Checked
(`rule30_audit_g99_g100.py`, S34): no repetition of the dyadic word to index 3,000 reaches $b \ge 2a + q$; factor
counts are at most $2m + 1$ for $m \le 40$; the base-3 and base-4 words violate the bound with $C = 5$. The open
question G137 names, whether $d$ itself has a finite left half, is measured directly in
`rule30_dyadic_companion.py` (predictions pushed with this note).

### G.GPT138. the first nonlinear kick gate does not close the initial tail (second-read by Local, 2026-10-06)

### G138. The first nonlinear kick gate does not close the initial-tail problem (2026-10-06)

**Status and purpose.** Symbolic wall audit, independent review pending; no experiment. This follows G137's failed entropy bridge by using the actual Rule30 inverse, rather than another repetition inequality. Prediction: the first few forced columns expose an explicit nonlinear product of neighboring visible bits. Counterfactual: sparsity of that product alone makes the entire forced initial row finite or infinite. Neither implication is obtained. This is an exact low-depth reduction and a retained failed bridge, not a new general inversion theorem or prize result.

Write v_j(t)=x_(-j)(t), with v_0(2s)=0 and v_0(2s+1)=1. Let c_s be column 1's visible bit at physical time 2s. The wall forces v_1(2s)=1-c_s and v_1(2s+1)=1. The inverse Rule30 identity is

    v_(j+1)(t)=v_j(t+1) XOR (v_j(t) OR v_(j-1)(t)).

Put A=c_s, B=c_(s+1), D=c_(s+2). Repeated Boolean substitution yields the exact even/odd pairs

    (v_1(2s),v_1(2s+1)) = (1-A,1),
    (v_2(2s),v_2(2s+1)) = (A,B),
    (v_3(2s),v_3(2s+1)) = (1-B,1-B),
    (v_4(2s),v_4(2s+1)) = (A*B,D),
    (v_5(2s),v_5(2s+1)) = (D XOR (A OR (1-B)),1-B).

For example the depth-four even entry is (1-B) XOR ((1-B) OR A)=A*B. Its odd entry is (1-D) XOR ((1-B) OR B)=D. The depth-five odd entry is B*D XOR (D OR (1-B))=1-B: for B=0 both sides are one, and for B=1 both sides are zero. These independent Boolean simplifications check the product and the cancellation without a dynamical run. They apply to the forced left construction; a full right evolution is an additional constraint.

**Dyadic specialization.** For c=d of G137, c_s*c_(s+1)=1 only at s=1, because 1 and 2 are the only consecutive positive powers of two. Depth four's even trace therefore has exactly one one, at physical time 2; its odd trace still contains infinitely many shifted dyadic pulses. The initial row's first five cells are

    (v_1(0),...,v_5(0))=(1,0,0,0,1).

This supplies neither a tail classification nor a finite-left realization. Vanishing on one temporal parity at one depth is not eventual vanishing across all initial depths.

**Unexpected constant-code control.** If c is constantly zero, the same formulas give an all-one depth-one column and then stationary alternating columns 0,1,0,1 through the depths displayed. The inverse recurrence continues that checkerboard to arbitrary depth: whenever two neighboring columns are stationary and opposite, the next outward column is the inner column's complement. Thus the forced initial left row has infinitely many ones even though the depth-four product is identically zero. This is the identified independent check against treating a sparse product as a finite tail. The constant-one case gives a time-alternating depth-one column, stationary one at depth two, then stationary alternating columns 0,1,0,... outward, likewise an infinite initial tail.

**Failed bridge retained.** A long zero segment of c creates a local checkerboard strip, but the strip's temporal margins grow with the number of inverse columns. Dyadic segments move outward in time as their lengths increase. The low-depth identities do not put that strip onto arbitrarily large depths of the single initial row. Nor does the single nonzero product guarantee that all deeper nonlinear products stay sparse. To settle the dyadic candidate, one needs a uniform all-depth invariant for this inverse recurrence, or a certified initial one at unbounded depths. To settle the general prize, the invariant must cover every admissible companion. No additional census or claimed closed finite-state recursion follows from these formulas.

### G.GPT139. fixed-depth temporal entropy does not measure the initial row (second-read by Local, 2026-10-06)

### G139. Fixed-depth temporal entropy does not measure the forced initial row (2026-10-06)

**Status and target.** Symbolic inverse-locality proof, independent review pending; no experiment. G138's low-depth audit is extended to every fixed depth. Prediction: a temporally sparse visible input creates temporally localized defects at each fixed depth, without controlling the entire spatial initial tail. Counterfactual: irregularity measured along the forced initial row would therefore imply positive temporal word-count entropy in a fixed column. The proof separates those axes. G64's earlier zero-entropy result concerned fixed right columns in a different Rule210 family; it is not imported as a Rule30 theorem.

Use G138's v_j(t) and inverse recurrence. For the constant-zero visible code, the background is b_j=1 at odd j and 0 at even j, for every j>=1. For any visible c define e_j(t)=v_j(t) XOR b_j. Then e_1(2s)=c_s and e_1(2s+1)=0. At depth two,

    e_2(t)=e_1(t+1) XOR e_1(t).

For j>=2, direct subtraction of the stationary background gives

    e_(j+1)(t)=e_j(t+1) XOR e_j(t)*(1-e_(j-1)(t))    when j is odd,
    e_(j+1)(t)=e_j(t+1) XOR (1-e_j(t))*e_(j-1)(t)    when j is even.

Indeed adjacent background bits are opposite. Their perturbed OR differs from one by e_j*(1-e_(j-1)) in the odd case and (1-e_j)*e_(j-1) in the even case. The temporal advance e_j(t+1) remains present; this is not an autonomous elementary rule for the defect field.

**All-depth locality.** By induction, e_j(t) is determined by the samples of e_1 on [t,t+j-1]. If all those samples vanish, e_j(t)=0. The base cases j=1,2 are explicit; at the next depth the two e_j terms use [t,t+j] and the shallower term uses a subinterval, and zero maps to zero in both displayed formulas. For the dyadic c=d of G137, the possible defect times at depth j therefore lie in

    union over k>=0 of [2^(k+1)-j+1, 2^(k+1)], intersected with t>=0.

This is an upper support bound, not equality. Outside these backward neighborhoods the forced column is exactly its checkerboard background value. It does not require linearizing away a nonlinear interaction.

**Temporal word bound.** Let P_c(n) count distinct length-n factors of c. A length-m time factor of v_j starting at u is determined by u modulo two and at most m+j consecutive visible symbols: the inverse locality spans physical times [u,u+m+j-2], and e_1 inserts a zero between visible symbols. Padding the visible window if needed gives

    P_(v_j)(m) <= 2*P_c(m+j).

The same reasoning jointly bounds a temporal vector of the first J columns by 2*P_c(m+J). Thus zero word-count entropy of c implies zero temporal word-count entropy at every fixed depth, and in every fixed finite left window. For d or its complement, G137 gives the explicit bound P_(v_j)(m)<=4(m+j)+2. This is not a uniform statement when the observed depth grows with m.

**Unexpected spatial-tail guard.** To evaluate v_j(0), the determining window length grows with j. Once j>=3, the first dyadic pulse at physical time 2 lies inside that window for every further j. The support lemma therefore does not force e_j(0) to vanish at large j. Nor may the fixed-j entropy limit be taken with j growing. G136's arbitrary-prefix fitting guard is another exact illustration of why unbounded recoding windows evade fixed-width control. These are the identified independent quantifier checks. Finite initial-row measurements described as coin-like are compatible with the proved zero temporal entropy; they concern different axes and do not supply an entropy theorem in either direction.

**Remaining obligation.** This characterizes fixed-depth temporal behavior, but neither proves nor disproves eventual zero support of the forced initial row. An all-depth spatial statement is still required: an explicit infinite family of v_j(0)=1, or another invariant preventing a zero tail. Full right-half realizability and a finite global Rule30 seed remain additional questions. No computational job duplicates Local's dyadic initial-row probe.

*Second reader's note on G138 and G139 (Local, 2026-10-06; chat L092).* Both correct. G138's five even/odd pairs
follow from the wall's two conditions and the inverse recurrence; G139's background is stationary and alternating in
depth, the defect field obeys the two displayed recurrences, and a defect at depth $j$ needs a visible pulse in
$[t, t + j - 1]$. Checked (`rule30_audit_g99_g100.py`, S35) by direct column computation: the five pairs on 100
random visible words; the dyadic initial cells $1, 0, 0, 0, 1$; both defect recurrences and the locality for depths
to 12; the dyadic defects at depths to 30 inside the stated backward neighbourhoods; temporal factor counts at most
$4(m + j) + 2$ for $j \le 10$, $m \le 30$. G139's quantifier point also qualifies my L091: the dyadic word's spatial
row looks coin-like while every fixed-depth column has zero word entropy, and a zero tail beyond the measured depth
is not excluded by that measurement.

### G.GPT140. the wall coding separates family entropy, orbit entropy and finite support (second-read by Local, 2026-10-06)

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

### G.GPT141. wall predecessors have a finite-tail test but need not be unique or finite (second-read by Local, 2026-10-06)

### G141. Wall predecessors have a finite-tail test but need not be unique or finite (2026-10-06)

**Status and target.** Symbolic spatial-support audit, independent review pending; no experiment. Counterfactual: G121's finite-row injectivity and unique-root descent carry over unchanged to an imposed alternating wall. The boundary guard below refutes the injectivity import, and the inverse transducer gives the exact replacement. G122 already records the zero/black and period-three inverse-tail graphs; this block applies them with the wall's phase and black-time condition specified. It does not revive the closed root route as a prize proof.

Let u be a finite left row at white wall phase zero. Assume, for the conditional clock statement, that u belongs to G140's compatible set S. Rows are listed by increasing depth from the wall. A backward step solves

    q_(j+1)=y_j XOR (q_j OR q_(j-1)),

where y is the output row and q_0 is the input wall bit.

**First backward step, black phase.** The input wall bit is q_0=1 and the black-time condition forces q_1=1. Thus there is exactly one black-phase predecessor z. If u is zero beyond radius L, its outward recursion eventually follows

    M0(a,b)=(a OR b,a).

The graph is 00->00, 01->10, 10->11, 11->11. Consequently z has either an eventual zero tail or an eventual black tail, determined after finitely many inverse steps through u's nonzero region. If u is clock-compatible, z extends its future clock by one black-time sample, so it is compatible in the black starting phase too.

**Second backward step, white phase.** The input boundary is zero, and the nearest-left input bit a is free, giving exactly two white-phase predecessors w^(0),w^(1). They are distinct because their depth-one bits differ. Each evolves to z, then u. If u belongs to S, both predecessors belong to S: their first black-time condition is z_1=1 and all later conditions are inherited from u. Their newly prepended visible bit is 1-a.

If z has an eventual black tail, the far-left recursion of either w follows

    M1(a,b)=(1 XOR (a OR b),a).

Its recurrent graph is 00->10->01->00, with 11 entering at 01. Both predecessors therefore have an eventual period-three tail containing ones, and neither is finite. If z has an eventual zero tail, process its finite nonzero region for each a, then inspect the inverse pair. A 00 pair gives a zero tail; every other pair enters 11 under M0. This is a finite test for which of the two predecessors are finite, conditional on the given finite u. It does not decide whether u satisfies the infinitely many future clock conditions.

**Unexpected finite boundary guard.** With the white boundary fixed at zero, the distinct finite input rows

    (0,1,1,0,0,...) and (1,0,1,0,0,...)

both produce the same left output row (1,0,1,1,0,0,...). Direct XOR-OR substitution at depths 1 through 4 verifies every nonzero output; farther triples are zero. Its depth-one bit is one, so both inputs satisfy the first black-time condition. Their next left output under the black boundary is (1,0,0,1,1,0,0,...). Thus even two-step finite wall evolution is not injective on finite rows passing that first condition. No claim is made that either row passes every later condition or lies in S_fin. Ordinary whole-line finite injectivity remains true: the discarded boundary output and the full right evolution are precisely what this guard omits. This is the identified independent check.

**Descent and its remaining gap.** Any nonempty finite left row has its leftmost one advance exactly one site left per forward step, since the exterior triple is 001. A compatible white-phase row is nonempty, because an empty row fails its first black-time condition. Hence a finite two-step predecessor, when one exists, has radius L-2. Backward descent through finite compatible predecessors must terminate, but it may branch and it can stop when the inverse tails are infinite. Neither a unique finite root nor a finite ancestor for every compatible finite row has been proved. The actual missing bridge would have to exclude these clock-compatible roots or supply a further spatial invariant; the existence of two unrestricted predecessors does not supply such a bridge. No new census, full right extension, finite-left witness or prize conclusion is asserted.

*Second reader's note on G141 (Local, 2026-10-06; chat L094).* Correct; the phase convention, the tail tests and the
finite-prefix scope all hold. With rows by depth and $q_0$ the wall bit, the black-phase predecessor is unique
($q_0 = q_1 = 1$), its tail follows $M_0$ from the last pair, and the two white-phase predecessors ($q_0 = 0$,
$q_1 = a$) follow $M_1$ after a black tail (recurrent cycle $00 \to 10 \to 01 \to 00$, so a period-three tail with
ones) or the $M_0$ test after a zero tail. The guard is right: $011$ and $101$ both give $1011$ and then $10011$, so
$10011$ has two finite white-phase predecessors and the descent really can branch. One connection: by G140's
conjugacy the white-phase predecessors of $\Phi(c)$ are exactly $\Phi(0c)$ and $\Phi(1c)$, the new letter
being $1 - a$, so G141's backward tree is the tree of one-letter extensions of the visible word, and the finite-tail test is
a computable pruning of it. Credit: the exact radius growth that L093 offered as a sharpening of G140 is already in
G141's descent paragraph, written before that note. Checked (`rule30_audit_g99_g100.py`, S38) on 400 random finite
rows of radius 1 to 15: the black-phase predecessor evolves forward to the row, has radius $L - 1$ when finite, and
has the tail $M_0$ predicts; both white-phase predecessors evolve to it, are finite exactly when the test says so,
then with radius $L - 2$, and have a period-three tail after a black tail; the guard; and $\Phi(ac)$ as the
predecessors on 30 random words.

### G.GPT142. a finite compatible candidate must accumulate on infinite support (second-read by Local, 2026-10-06)

### G142. A finite compatible candidate must accumulate on infinite support (2026-10-06)

**Status and target.** Symbolic consequence of the reviewed G140 compact wall coding and G141 exact radius growth; independent review pending. No experiment or novelty claim about compactness. The targeted record search found G129's varying-radius guard and G140's dyadic checkerboard limit, but no statement excluding every compact forward-invariant finite-support subfamily. Counterfactual: an infinite-support accumulation point would contradict a finite compatible starting row. The conclusion below reverses that inference conditionally; it does not prove a finite candidate exists.

Use G140's compact compatible space S and continuous two-step map F. Its finite-support subset S_fin is forward invariant. Every member has positive integer radius R, since the empty row fails the first black-time condition, and G141 proves R(Fu)=R(u)+2.

**Lemma.** There is no nonempty compact A contained in S_fin with F(A) contained in A.

**Proof.** Suppose such an A exists. The sets F^n(A) are nested, nonempty and compact, so their intersection K is nonempty and compact. Moreover F(K)=K. The forward inclusion follows from nesting. For the reverse inclusion, fix y in K. For each n the set

    C_n = F^n(A) intersect F^(-1)({y})

is nonempty, since y belongs to F^(n+1)(A). These sets are nested and compact. Any x in their intersection lies in K and satisfies F(x)=y.

Every point of K has positive integer radius. Choose y in K with the smallest radius occurring in K; this uses the well-ordering of the integers, not continuity or boundedness of the radius function. Surjectivity on K supplies x in K with F(x)=y. Exact growth gives R(x)=R(y)-2, contradicting minimality. Thus A cannot exist.

**Consequences, conditional on existence.** For any u in S_fin, its forward orbit closure in S is nonempty, compact and forward invariant. The lemma forces that closure to contain a row z of infinite support. Since every orbit point F^n(u) is finite, z is an accumulation point along indices tending to infinity. Therefore every hypothetical finite compatible candidate necessarily has an infinite-support orbit accumulation point, not merely the dyadic candidate of G140. Also S_fin is either empty or not closed in S: if nonempty and closed it would itself be a forbidden compact forward-invariant A. In particular it cannot be assumed compact to manufacture finite ancestors. This sharpens G140's closure qualification without deciding whether S_fin is empty.

**Unexpected compactness check.** Compactness alone does not bound finite radii. In the ordinary binary half-line product space, the set consisting of the empty row and the rows e_n with exactly one one at depth n is compact, every row is finite, and its radii are unbounded: e_n converges to the empty row. This is not a compatible wall family; the empty row is excluded from S. It rejects a false shortcut to the lemma. The proof instead uses forward invariance, a compact surjective core and strict radius growth. No assertion that an individual finite row has a finite predecessor is used, and G141's branching or infinite-tail predecessors remain allowed.

**Remaining prize obligation.** An infinite-support limit cannot exclude finite initial support; conditional on such a candidate it is unavoidable. The open Q7 question is still emptiness of S_fin, or a wall-specific constraint on each individual initial tail. This closes the general compact-orbit-limit shortcut, not the finite-tail problem. No measurement, full right extension, finite witness or prize solution is claimed.

*Second reader's note on G142 (Local, 2026-10-06; chat L095).* Correct, checked by hand; no run was needed. The
surjective core holds: $F(K) \subseteq K$ by nesting, each $C_n$ is nonempty because $y \in F(F^n(A))$, and it is
compact because $F^{-1}(\{y\})$ is closed, so the nested intersection supplies a preimage inside $K$. The quantifier
is right: the conclusion is about each member of $S_{\mathrm{fin}}$ and is vacuous if that set is empty. The core is
correct but more than the lemma needs. Every point of $F^n(A)$ is $F^n(a)$ with $a$ nonempty, so its radius is
$R(a) + 2n \ge 2n + 1$; the sets $F^n(A)$ are nested, compact and nonempty, so their intersection has a point, and that
point would have radius at least $2n + 1$ for every $n$, which no finite row has. So the lemma is a nested compact
intersection plus the radius clock. The exclusion of the empty row enters only through exact growth, since the empty
row gains radius one, not two, over a white-black pair. The guard is well chosen: the rows $e_n$ show precisely that
compactness without forward invariance bounds nothing. The consequence that $S_{\mathrm{fin}}$ is empty or not
closed generalises G140's dyadic case to every candidate.

### G.GPT143. an aperiodic half-circle code passes every repeat test (second-read by Local, 2026-10-07)

### G143. An aperiodic half-circle code passes every repeat test (2026-10-07)

**Status and target.** Symbolic Q7 repeat-filter counterexample, independent review pending. No experiment run by GPT. HR0-HR3 were published for Local at d8bb640 before the requested finite test; Local L097 reports HR0, HR2 and HR3 PASS and HR1 HELD on that requested scope; the proof below is all-period and does not infer its conclusion from that test. Existing record: G137's sparse dyadic counterexample, GC158's failed XOR-derivative transfer, and Local L096's all-odd convergent guard. PRIOR-ART.md records the known Rote/Sturmian relation. This is an application to the wall's necessary repeat inequality, not a novelty claim about Rote sequences or a Rule30 realization.

Put beta=2-sqrt(2), alpha=beta/2 and r=sqrt(2)-1. Define

    c_s = floor(s*beta) modulo 2,    s>=0.

**Claim.** For every q>=1 and every interval of equality c_s=c_(s+q) on a<=s<=b, with a>=0,

    b < 2a+q.

Thus this aperiodic half-circle rotation code passes the wall's entire necessary repeat family even with constant C=0. It is not thereby a compatible finite-left companion. Its XOR derivative is the Sturmian mechanical word of slope beta, every constant run of c has length at most two, and its word-count entropy is zero. In particular this filter alone cannot exclude every nonsparse, low-complexity unrelated-endpoint rotation code.

**Mismatch intervals and reduction to records.** Choose the even integer P nearest q*beta and set epsilon=q*beta-P, so -1<epsilon<1 and epsilon is nonzero. With x_s={s*beta}, direct floor subtraction says a mismatch occurs exactly when

    epsilon>0: x_s in [1-epsilon,1),
    epsilon<0: x_s in [0,-epsilon).

For errors of the same sign, a smaller absolute error gives a smaller mismatch interval. Therefore it suffices to prove the claim at the successive same-sign error records: for any q choose a record q0<=q whose error has the same sign and no greater magnitude. A q-repeat interval avoids the larger mismatch interval, hence is a q0-repeat interval, giving b<2a+q0<=2a+q.

Here these records are among q=1, q=2, and the denominators listed below. To justify completeness, alpha=[0;3,2,2,...]. After its first denominator 3, consecutive convergents P/Q and P'/Q' form an integer basis, with opposite signed errors D,D' satisfying |D'|=(2+r)|D|, where Q'<Q. The next denominator is 2Q+Q'. Any pair (p,q) has the form m(P,Q)+k(P',Q'). If its error improves the current record of its sign, m and k must both be positive: opposite signs of coefficients add the error magnitudes, while a zero coefficient gives a multiple no better than a current record. With q<2Q+Q', m must then be one. For k>=2 the magnitude of D+kD' exceeds |D'|, so the only possible improving intermediate is m=k=1, the mediant. At the next convergent the induction repeats. Before denominator 3, the relevant nearest-integer periods are just 1 and 2. Scaling these errors by two gives exactly the even-integer records needed for beta; records with even larger error need not be retained.

Let p_n/q_n be beta's convergents, starting p_1/q_1=1/1 and p_2/q_2=1/2. For n>=2 all p_n are odd,

    q_(n+1)=2q_n+q_(n-1),
    delta_n=q_n*beta-p_n=(-1)^n*r^n.

The alpha convergents after denominator 1 are the even-numerator beta mediants

    Q_n=q_n+q_(n-1),    P_n=p_n+p_(n-1),    n>=2.

Their errors have sign opposite delta_n and magnitude E=(1+r)*|delta_n|. The intervening alpha mediants have beta denominators 2q_n and even numerator 2p_n. This follows by the displayed denominator recurrence (the first such denominator is 4). Hence the required candidate periods are 1, 2, Q_n and 2q_n for n>=2; proving more candidates than strictly set records is harmless.

**A return bound with its mesh proof.** Fix n>=2, put d=|delta_n| and Qnext=q_(n+1). Every block of Qnext successive orbit samples {s*beta} meets every half-open interval of length E=(1+r)*d. Indeed the Qnext orbit points have successive gaps d and d+|delta_(n+1)|=E. To see this directly, in the orientation given by the sign of delta_n, advance the index by q_n modulo Qnext. Without index wrap the circular distance is d; with wrap it is d+|delta_(n+1)|. Coprimality makes one cycle through all indices, and its total distance is

    Qnext*d + q_n*|delta_(n+1)| = 1

by the consecutive-convergent determinant identity. Thus this is the circular neighbor order and its largest gap is E. A half-open arc of length E contains a point even at a gap endpoint. Translating this mesh proves the block statement. It also holds for intervals of length 2d>E. Consecutive mismatch visits for either length therefore have time gap at most Qnext.

We also use the ordinary continued-fraction best-approximation fact already used in G134: for 0<k<q_n, the distance of k*beta to any integer is at least |delta_(n-1)|=(2+r)*d. Both E and 2d are smaller. So neither mismatch interval has a positive visit before q_n.

**Mediant periods Q_n.** The mismatch interval has length E and sign opposite delta_n. If it is the upper interval, its first visit is exactly q_n; if it is the lower interval, it contains time zero and its first positive visit is exactly q_n. In either case the samples at q_n land in it because their signed error has magnitude d<E. A repeat interval before that visit has b<=q_n-1<Q_n, and so satisfies the claim. For any later maximal repeat interval, write its preceding mismatch time as h>=q_n and the next mismatch time as h+g, with g<=Qnext. Then a=h+1, b=h+g-1 and

    b-2a-Q_n = g-h-Q_n-3
              <= Qnext-q_n-(q_n+q_(n-1))-3 = -3.

Subintervals only lower this debt. In the lower-interval case the first run starts at 1, making its bound still stronger.

**Doubled convergent periods 2q_n.** The mismatch interval now has length 2d and the same sign as delta_n. Its first positive visit lies between q_n and Q_n: there is no visit before q_n, and the mediant Q_n has the opposite signed error of magnitude E<2d, so it lands in the interval. In the lower-interval case time zero is also a mismatch. Any repeat before the first positive visit ends by Q_n-1<2q_n. Every later maximal repeat has preceding mismatch h>=q_n and gap g<=Qnext, giving

    b-2a-2q_n <= Qnext-q_n-2q_n-3
               = q_(n-1)-q_n-3 < 0.

This proves the claim for these periods too. For q=1 a match requires x_s<1-beta; its next sample is outside that interval because beta>1/2, so a match run has length at most one. For q=2 the nearest even displacement has epsilon=2beta-2<0, so a match requires x_s>=2-2beta. Its next sample wraps into [1-beta,beta), outside the match interval, and again every match run has length at most one. Both small periods satisfy the claim. The record reduction now proves it for every q.

**Complexity and the unexpected phase check.** The derivative g_s=c_s XOR c_(s+1) equals floor((s+1)*beta)-floor(s*beta), a Sturmian word. Thus c is aperiodic. Since beta>1/2, g contains no consecutive zeros, so c has no constant run longer than two. A length-m c block is determined by its first bit and the length-(m-1) g block. Hence P_c(m)<=2m and c has zero word-count entropy; no randomness statement follows.

The phase is essential. For c'_s=floor(s*beta+1/2) modulo2, the exact first 19 bits are 0110010011001001101. Period 7 repeats on [0,10] and fails at 11, giving debt 10-7=3. These finite values follow from adjacent-integer square-root bounds, the HR3 control preregistered in GC159; this is a direct algebraic check, not a new run or an all-phase conclusion. The period-q derivative lift counterfactual remains refuted by 0101... and its constant-one derivative.

**Scope.** The known half-circle code and the sparse dyadic word of G137 both pass the full necessary repeat family, by different mechanisms. Here numerator parity and mediant returns explain the gap. No initial-tail support theorem, full right extension, finite-left witness, positive-entropy theorem or prize conclusion is established. Q7 now needs a further wall or coupled-tail constraint to exclude this particular phase-zero code; stronger repetition arguments must specify a condition beyond the inequality just passed.

*Second reader's note on G143 (Local, 2026-10-07; chat L099).* Correct; I checked each step by hand, and the lemmas
exactly (S39). The mismatch rule follows from $\lfloor x_s + \varepsilon \rfloor$ with an even shift. The record
reduction is right because a larger mismatch interval of the same sign contains the smaller one. Since
$\alpha = [0; 3, 2, 2, \ldots]$, the same-sign records are the convergents and the single intermediate fraction between
each pair. With $\delta_n = (-1)^n r^n$, the mediant error is $(1+r)d$ with the opposite sign and the doubled error is
$2d$ with the same sign. The mesh is the two-gap case of the three-distance theorem at $q_{n+1}$ points: gap $d$ taken
$q_{n+1} - q_n$ times and gap $E$ taken $q_n$ times, by $q_{n+1} d + q_n |\delta_{n+1}| = 1$. The first-hit times and
both debt bounds follow, and so do the two small periods. The bounds are sharp. At every mediant scale the interval from
$q_n + 1$ to $q_n + q_{n+1} - 1$ (for example $[13, 40]$ at period 17) attains debt $-3$, exactly as L097 measured. At
period 4 the initial interval $[0, 2]$ attains the doubled-period bound $q_{n-1} - q_n - 1 = -2$, and period 1 attains
the overall maximum $-1$. The survival is L096's parity guard made quantitative: every even-sign shift is a mediant or a
doubled convergent, whose error is $\sqrt 2$ or 2 times the convergent's. At a mediant the longest return gap $q_{n+1}$
equals the shift $Q_n$ plus the first-hit time $q_n$, so the debt cannot pass $-3$. Checked (`rule30_audit_g99_g100.py`,
S39, within GC159's 4,096 symbols and with 60-digit decimals): the mismatch rule for every period up to 200; the record
list to 2,048; the gap counts for $n = 2$ to 9; the first hits; the debt bounds at every record period, with $-3$
attained at 7 to 577. The first S39 run failed through my own sign error in the mismatch test ($1 + \varepsilon$ for
$1 - \varepsilon$); after the fix every part passes.

**Reviewed extension,29 October2026 (GC2193/L1193).** For the silver code above and odd convergent indices
n>=3, set Q=q_n+q_(n-1). Its first3Q letters are A B B, with A and B differing in exactly the zero-based bit q_n,
where A has0 and B has1. One substitution makes a cube at arbitrarily large scales; the original exact bound
still holds. Proof: the first two lag-Q mismatches are q_n and q_n+q_(n+1), and the latter exceeds2Q. This uses
G143's first hit and L1192's independently carried signed-arc exclusion. L1193 directly carried the block split,
values and debt Q-1. **PROVED hand/two-party**, no fixed-edit/Rule30/novelty claim.
[Full proof and qualifications](../reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2193-exact-repetition-is-classified-at-phase-zero-but-one-error-admits-arbitrarily-long-near-cubes).
The exact longest one-substitution prefix2q_(n+1) is a separate PROOF-SKETCH in GC2194, not silently included in
this second read. Ordinary cube-freeness is known from the2020 primary result compared there.
Update GC2197/L1195: that exact fixed-lag endpoint extension is now independently carried, PROVED hand/two-party.
Its global-period and physical-Rule30 qualifications remain unchanged.

### G.GPT144. the phase-zero half-circle repeat filter has an exact exceptional class (second-read by Local, 2026-10-07)

### G144. The phase-zero half-circle repeat filter has an exact exceptional class (2026-10-07)

**Status and target.** Symbolic Q7 classification, independent review pending; G143 independently verified by Local L099. No experiment. Fix the phase zero used in GC159; this is not an all-phase classification. The inputs are G143's signed mismatch intervals and tail-two mesh argument, ordinary continued-fraction best approximation and Legendre's criterion. The Rote critical-exponent literature is recorded in PRIOR-ART.md; its ordinary factor exponent does not include the starting index in our debt and no theorem from it is imported.

Let beta be any irrational in (0,1), let c_s=floor(s*beta) modulo2, and write p_n/q_n for its convergents, a_(n+1) for the next coefficient and delta_n=q_n*beta-p_n. Then the following are equivalent:

1. There is a finite constant C such that every equality interval c_s=c_(s+q), a<=s<=b, a>=0, q>=1, satisfies b<=2a+q+C.
2. Eventually every a_n is 2 and every convergent numerator p_n is odd.

The angles in (2) form a countable quadratic class. G143's beta=2-sqrt(2) belongs to it and even satisfies the strict C=0 bound. Passing this filter is not a finite-left Rule30 realization. Every other phase-zero half-circle code is excluded by the wall's necessary repeat inequality for every finite left radius.

**Obstruction from even numerators.** Suppose p_n is even, with n large enough that |delta_n|<1. The period q_n has signed even-integer error delta_n, so its mismatch interval is the upper or lower arc of length |delta_n| given in G143. Its first positive visit is exactly h=q_(n+1). Indeed best approximation gives distance at least |delta_n| to every integer at every 0<k<q_(n+1); q_n itself has the wrong error sign to enter this arc, and no other such k attains the opposite endpoint. At q_(n+1) the error has opposite sign and smaller magnitude, so the arc is hit.

If delta_n>0, the prefix equality interval is [0,h-1]. If delta_n<0, time zero is a mismatch and the equality interval is [1,h-1]. Their debts b-2a-q_n are respectively

    q_(n+1)-q_n-1,    q_(n+1)-q_n-3.

Both are at least q_(n-1)-3. Infinitely many even p_n therefore produce unbounded debt. Condition (1) forces all sufficiently late p_n to be odd. The numerator recurrence then forces every sufficiently late a_(n+1) to be even.

**Obstruction from large coefficients.** Put d=|delta_n| and a=a_(n+1)>=3. Write |delta_(n-1)|=(a+gamma)*d with 0<gamma<1. For large n, the period 2q_n has signed even-integer error 2delta_n and mismatch arc of length 2d. Its first positive visit is

    h=(a-1)*q_n+q_(n-1).

Here is an explicit first-hit justification. Expand any integer pair (p,k) in the unimodular basis (p_n,q_n),(p_(n-1),q_(n-1)), with coefficients m,l. An error of the sign opposite delta_n and magnitude less than 2d, which is less than |delta_(n-1)|, requires m,l>0: opposite coefficient signs add error magnitudes, and a zero coefficient is either of the wrong sign or too large. If k<h, then m<=a-2. Its opposite-sign error has magnitude

    l*|delta_(n-1)|-m*d >= (2+gamma)*d > 2d.

Thus no earlier positive visit is possible. At h, m=a-1 and l=1 give the required opposite error (1+gamma)*d<2d. As before the initial equality interval starts at zero or one, according to the sign of delta_n. Its debt for period 2q_n is

    (a-3)*q_n+q_(n-1)-1, or
    (a-3)*q_n+q_(n-1)-3.

These tend to infinity along any infinite set of coefficients at least three. Condition (1) therefore forces eventually a_n<=2. Combined with eventual evenness from the numerator obstruction, it forces eventually a_n=2. This proves (1) implies (2), with explicit violating intervals whenever either obstruction occurs infinitely often.

**Converse: finite exceptions cost only a finite constant.** Assume (2), put r=sqrt(2)-1, and take n sufficiently late. Then the exact error ratios and recurrence are

    |delta_(n-1)|=(2+r)*|delta_n|,
    |delta_(n+1)|=r*|delta_n|,
    q_(n+1)=2q_n+q_(n-1).

The even-numerator mediants have denominator B_n=q_n+q_(n-1) and numerator A_n=(p_n+p_(n-1))/2. They approximate alpha=beta/2 with alternating errors D_n=(delta_n+delta_(n-1))/2, whose successive magnitude ratio is r. Consecutive pairs (A_n,B_n) are unimodular, as direct substitution gives determinant of absolute value one; their denominators satisfy the same tail-two recurrence. Moreover

    B_n*|D_n| = 1/(B_(n+1)/B_n+r)
                -> 1/(2*sqrt(2)) < 1/2.

Legendre's criterion makes them genuine alpha convergents for all sufficiently late n. They are consecutive: their errors have opposite signs, whereas a skipped even number of convergent steps has the same sign, and a skipped odd number of at least three has determinant of magnitude at least two. Thus alpha also has an eventual continued-fraction tail of twos. Its late same-sign error records are its convergents and intervening mediants, by G143's unimodular record argument. Their beta periods are B_n and B_n+B_(n-1)=2q_n. There are only finitely many earlier record periods.

For every sufficiently late B_n or 2q_n, G143's entire mesh and first-hit argument applies verbatim with the displayed error ratios: a q_(n+1)-point orbit mesh has largest gap (1+r)*|delta_n|; no positive arc visit precedes q_n; the mediant visits provide the required first-hit upper bound. Consequently every repeat at these candidate periods satisfies b<2a+q, without any assumption on the finite continued-fraction prefix. Same-sign mismatch-interval inclusion reduces all other late periods to these records.

Each of the finitely many earlier record periods has a nonempty mismatch arc. Irrational rotation has a finite orbit mesh finer than that arc, so every translate of a sufficiently long fixed block hits it. Its equality runs therefore have bounded length, and its repeat debt has a finite upper bound independent of a. Taking the maximum of these finitely many bounds and zero supplies C. This proves (2) implies (1).

**Unexpected parity controls and limits.** The tail-two angle beta=sqrt(2)-1 fails the criterion: it has infinitely many even convergent numerators. Already the convergent 2/5, followed by 5/12, gives a period-5 equality on [0,11] of debt 6. Thus being in the silver quadratic field or having a tail of twos alone is insufficient. Conversely beta=[0;1,1,4,4,...] has eventually all odd numerators but fails by the doubled-period obstruction. These are direct arithmetic controls, not new runs. They distinguish both required conditions from weaker shortcuts.

Every angle satisfying (2) has a finite integer continued-fraction prefix followed by the same infinite tail, so there are countably many and they are quadratic. Their complements and arbitrary phases were not classified here. The wall has a necessary repeat constant determined by its finite left radius, so the theorem excludes all other phase-zero codes as companions. The exceptional class remains unresolved for actual initial-tail support. No finite witness, full right extension, positive-entropy or prize claim follows.

*Second reader's note on G144 (Local, 2026-10-07; chat L100).* Correct, read jointly with G143 as asked. Even
numerators: for $0 < k < q_{n+1}$ with $k \ne q_n$ best approximation is strict, $\|k\beta\| > |\delta_n|$, and $q_n$
itself has the wrong sign, so the first hit is $q_{n+1}$ and the initial debts are $q_{n+1} - q_n - 1$ or $- 3$. Large
coefficients: with $|\delta_{n-1}| = a d + |\delta_{n+1}|$, an opposite-sign error below $2d$ needs both basis
coefficients positive, $k < h$ forces $m \le a - 2$ and an error of at least $(2 + \gamma) d$, and $m = a - 1$, $l = 1$
gives $(1 + \gamma) d$; so $h = (a-1) q_n + q_{n-1}$ and the debts follow. The Legendre step holds: with $a_{n+1} = 2$
the determinant of consecutive even mediants is $\pm 1$ by direct expansion; unimodularity and opposite signs give the
exact identity $B_n |D_n| = 1/(B_{n+1}/B_n + |D_{n+1}|/|D_n|)$, whose limit is $1/(2\sqrt 2)$. The consecutiveness
argument needs both of its parts: two convergents two steps apart can have determinant one when the coefficient between
them is one, and only the sign excludes that case. For late $n$ the complete quotients equal $1 + \sqrt 2$ exactly, so
G143's ratios, mesh and first hits apply verbatim, and the finitely many early records each have bounded equality runs.
Checked (`rule30_audit_g99_g100.py`, S40, G144's own controls, prefixes under 2,100, 60-digit decimals): at
$\sqrt 2 - 1$ the even numerators 2, 12 and 70 give first hits $q_{n+1}$ and the stated debts (6 at period 5 on
$[0, 11]$); at $[0; 1, 1, 4, 4, \ldots]$ the numerators are odd and the doubled periods have first hit
$(a-1) q_n + q_{n-1}$ and the stated debts; and at $2 - \sqrt 2$ the even mediants are unimodular, alternate in sign,
satisfy the identity and the Legendre bound, and are exactly the convergents of $\alpha$.

**Reviewed quantitative extension,29 October2026 (GC2187/L1192).** With R(n) the shortest prefix length
containing two n-factors and rep=liminf R(n)/n, the phase-zero code has rep=2 exactly on G144's eventual-twos/
odd-numerator class. Unbounded digits give rep=1; late digits bounded by A off that class give
rep<=2-1/(A+2). **PROVED hand/two-party**, with original G144/L100 first-hit dependencies retained.
[Carrying proof](../reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2187-hand-candidate--the-phase-zero-repetition-exponent-has-an-exact-exceptional-maximum).
GC2193 positively credits the unbounded case to Nguyen7.4/Bugeaud–Kim10.3 at every phase; precise bounded-type
prior-art disposition is unresolved. No formal validation, CA realization or submission claimed.

### G.GPT145. the silver half-phase code fails every finite repeat allowance (second-read by Local, 2026-10-07)

### G145. The silver half-phase code fails every finite repeat allowance (2026-10-07)

**Status and target.** Symbolic Q7 proof, independent review pending. No experiment. G143 is independently verified by Local L099; G144 remains under review. This block follows the finite half-phase control HR3 already preregistered in GC159 and reported by Local L097. The prediction is that its debt-3 witness is the first member of an unbounded family. The counterfactual is a uniform finite debt bound at this phase. The proof uses G143's explicit convergents and mismatch interval, not a new computational scan or a theorem imported from the Rote literature in PRIOR-ART.md.

Put beta=2-sqrt(2), r=sqrt(2)-1 and c_s=floor(s*beta+1/2) modulo2. Let p_n/q_n be beta's convergents, with n=1 giving 1/1 and n=2 giving 1/2. For every odd n>=3, put Q_n=q_n+q_(n-1). Then the period-Q_n prefix equality interval is exactly

    [0, h_n-1],    h_n=2q_n+q_(n-1)/2,

and its debt is

    (h_n-1)-Q_n = q_n-q_(n-1)/2-1 -> infinity.

Consequently no finite C makes b<=2a+q+C hold for every repeat of this half-phase code. In particular it cannot be the wall's companion from any finite left radius. This concerns the chosen half-phase silver code, not every phase or angle.

**Proof of the first hit.** For these odd n, q_n is odd, q_(n-1) is even, and both numerators are odd. Set d=|delta_n|, where delta_n=q_n*beta-p_n. The exact signed errors are delta_n=-d and delta_(n-1)=(2+r)d. Period Q_n has an even numerator and positive error E=(1+r)d. Since E<1/2 for n>=3, its mismatch interval in the shifted coordinate is [1-E,1). Thus a positive time k is a mismatch exactly when

    {k*beta} is in [1/2-E,1/2).

Equivalently, there is an odd integer p with 2k*beta-p negative and magnitude at most 2E. Equality at the endpoint is impossible: it would imply an integer multiple of beta is an integer, since E=Q_n*beta-(p_n+p_(n-1)). Expand the integer pair (p,2k) in the unimodular basis (p_n,q_n),(p_(n-1),q_(n-1)), with integer coefficients m,l. Denominator parity forces m even; odd numerator parity then forces l odd. Its error is

    [-m+(2+r)l]*d.

A negative error of magnitude less than 2E requires m,l>0. Indeed m<=0,l>0 has the wrong sign; both negative give a negative denominator. If m>0,l<0, parity gives m>=2 and |l|>=1, and the magnitude is at least (4+r)d>2E. A zero coefficient is ruled out by parity, has the wrong error sign, or has a nonpositive denominator. Therefore m is a positive even integer and l a positive odd integer.

For l=1, the first possible m is 4: m=2 has positive error; m=4 has negative error of magnitude (2-r)d<2E. It gives denominator 4q_n+q_(n-1), hence time h_n. If l>=3, negative error requires m>(2+r)l, so m>=8; its denominator exceeds the one just found. This proves h_n is the first positive mismatch. Time zero is not a mismatch, since its shifted coordinate is 1/2. The prefix equality and its exact endpoint follow.

The denominator recurrence gives unbounded q_n and q_(n-1)<q_n, so the displayed debt is greater than q_n/2-1 and diverges. This proves the exclusion for every finite allowance.

**Unexpected check and scope.** At n=3 the convergents are 3/5 and 1/2: Q_n=7, h_n=11, and debt=3, exactly HR3's retained finite witness. The same angle at phase zero passes every period with C=0 by G143. Thus changing the phase can change boundedness of the repeat debt, not just its finite constant. This is not a finite Rule30 witness at either phase. The boundary-phase exceptional angles in G144 and their actual forced initial tails remain unresolved; no prize claim follows.

*Second reader's note on G145 (Local, 2026-10-07; chat L101).* Correct. At phase one half the mismatch rule for period
$Q_n$ moves the arc to $\{k\beta\} \in [1/2 - E, 1/2)$, which is exactly an odd $p$ with $2k\beta - p \in [-2E, 0)$. For
odd $n$ the denominators $q_n$ are odd and $q_{n-1}$ even, so in the basis expansion of $(p, 2k)$ the coefficient $m$ is
even and $l$ odd, and the error is $(-m + (2+r) l) d$. Mixed signs give at least $(4 + r) d > 2E$, zero coefficients
fail by parity, sign or denominator, and for $l = 1$ only $m = 4$ lands in the window $(2 + r, 4 + 3r)$; every $l \ge 3$
needs $m \ge 8$ and a larger denominator. So the first hit is $h_n = 2q_n + q_{n-1}/2$, time zero is not a mismatch, and
the prefix debt is $q_n - q_{n-1}/2 - 1$. The phase contrast with G143 is the striking part: the same angle passes every
period at phase zero with $C = 0$ and fails every finite allowance at phase one half. Checked
(`rule30_audit_g99_g100.py`, S41, within GC159's 4,096 symbols, the integer floors cross-checked against 60-digit
decimals): for $n = 3, 5, 7, 9$ the first mismatch of period $Q_n$ is $h_n$, every mismatch time lies in G145's arc and
every arc time is a mismatch, and the prefix debts are 3, 22, 133 and 780, the first being HR3's witness.

### G.GPT146. shifted passing codes approach an explicitly excluded infinite tail (second-read by Local, 2026-10-07)

### G146. Shifted passing codes approach an explicitly excluded infinite tail (2026-10-07)

**Status and target.** Symbolic Q7 closure audit, independent review pending. Depends on verified G140/G143 and the pending G145 half-phase exclusion. No experiment. Prediction: every time shift of the passing silver code still has some finite repeat allowance, but these allowances cannot be uniform when the phases approach one half. Counterfactual: closure of the passing family might transfer its repeat bound, or finite support, to every limiting rotation phase. G142 already closes the general finite-support compact-limit shortcut; this block names a specific excluded limit and identifies exactly which allowance loses uniformity. Existing rotation and wall-coding records are used, with no new prior-art theorem or computational job.

For a binary one-sided word x define B_C by the requirement that every equality interval x_s=x_(s+q), a<=s<=b, satisfies b<=2a+q+C, for all a>=0 and q>=1. Take C>=0, and put B=union over all nonnegative integer C of B_C. Let sigma be the left shift.

**Shift and finite-prefix control.** If x belongs to B_C, sigma^t x belongs to B_(C+t). A repeat of the shifted word translates to [a+t,b+t] in x, whose bound gives b<=2a+q+C+t. Conversely, if sigma^t x belongs to B_C, then x belongs to B_(C+t). For a repeat of x with a>=t, translate back and use the shifted bound. If a<t<=b, its suffix [t,b] translates to a repeat starting at zero, giving b<=t+q+C<=2a+q+C+t. If b<t, the bound is automatic. Thus x is in B if and only if sigma^t x is in B. Words that agree after a finite prefix also agree on membership in B. Global complementation preserves every B_C exactly.

**Closed at fixed allowance, not at some allowance.** Each B_C is closed in the product topology: any violation is certified by a finite repeat witness, involving finitely many coordinates through b+q, and persists in the corresponding cylinder. An intersection of these closed finite-witness constraints is closed. This does not make their increasing union B closed.

Let beta=2-sqrt(2) and c^(rho)_s=floor(s*beta+rho) modulo2, with rho considered modulo2. G143 places c^(0) in B_0, hence every sigma^t c^(0)=c^(t*beta modulo2) is in B. Irrational rotation has a dense forward orbit, so choose t_j with t_j*beta modulo2 tending to 1/2. No coordinate s*beta+1/2 is an integer, so every fixed finite prefix eventually agrees exactly with c^(1/2). Therefore

    sigma^(t_j)c^(0) -> c^(1/2),

while G145 gives c^(1/2) not in B. This proves B is not closed. More precisely, for any fixed C, choose a G145 witness with debt greater than C. Every sufficiently large j shares all coordinates of that witness and fails B_C. Thus the smallest nonnegative repeat allowances for these passing shifted words tend to infinity, not just along some unspecified subsequence. The simple upper allowance t_j remains valid.

The passing phases t*beta modulo2 and the excluded phases 1/2+t*beta modulo2 are both dense. The latter exclusion follows from the reverse-shift implication above. These are two countable dense phase orbits, not a classification or measure statement about the other phases. They are disjoint by irrationality.

**An explicit infinite forced-tail limit.** In G140's notation Phi maps a visible word to its unique compatible initial left row and satisfies F Phi=Phi sigma for the two-step wall evolution F. Its exact finite-prefix modulus makes Phi continuous. Put u_0=Phi(c^(0)) and u_half=Phi(c^(1/2)). Then

    F^(t_j)(u_0) = Phi(sigma^(t_j)c^(0)) -> u_half.

G145 and the wall's necessary finite-radius repeat bound force u_half to have infinite support. This identifies an infinite-support accumulation point of the actual forced-tail orbit of u_0, without assuming whether u_0 itself has finite support. If u_0 were finite, the exact radius clock in G141/G142 would grow by two per F, and such an infinite-support limit is entirely consistent. No contradiction to a finite u_0 follows. Nor does the existence of infinite support at the limiting phase provide a fixed depth beyond which every approximating phase is nonzero.

**Unexpected prefix guard and remaining obligation.** Altering finitely many symbols of a passing word cannot create the unbounded-debt failure, by the shift control just proved. Hence the half-phase failure is not explained by changing the first boundary symbol or a finite startup transient; the two codes differ at infinitely many times. The phase comparison still yields no lower bound on the actual support of u_0. Q7's remaining obligation is a constraint on that individual forced tail, beyond repetition or nonuniform compact limits. No finite witness or prize claim follows.

*Second reader's note on G146 (Local, 2026-10-07; chat L102).* Correct. The shift control holds in both directions,
including the straddling case $a < t \le b$, where the suffix $[t, b]$ gives $b \le t + q + C$. Each $B_C$ is closed
because a violation is a finite witness. $\sigma^t c^{(0)} = c^{(t\beta \bmod 2)}$ holds since adding 2 to the phase
leaves every parity unchanged. Convergence to $c^{(1/2)}$ is coordinatewise, because no $s\beta + 1/2$ is an integer, so
each G145 witness is eventually inherited and the least allowance escapes along the whole approach, not along a
subsequence. The two dense phase orbits are disjoint by irrationality, and continuity of $\Phi$ with
$F \Phi = \Phi \sigma$ carries the limit to the forced rows. As the block says, this gives no contradiction for a finite
$u_0$ (G142). Checked (`rule30_audit_g99_g100.py`, S42, only GC159's 4,096 symbols of $c^{(0)}$): the shift identity,
the shift allowance (maximal debt at most $t$) on the seven shifts below 2,048 that set a new closest phase to 1/2, and
the G145 witnesses for $n = 3, 5, 7$ inside every shifted prefix whose agreement with $c^{(1/2)}$ covers them.
Descriptive: at $t = 11, 18, 35, 373$ the maximal debt is exactly $t - 3$, so the shift allowance is nearly attained.
The reason: a G143 interval lying wholly beyond $t$ gains exactly $t$ in debt under the shift, and the maximum comes
from a sharp one, for example $[13, 40]$ at period 17 when $t = 11$. My first draft of S42 also expected the agreement
and the debt to rise monotonically along those shifts. G146 claims neither; the approach alternates sides of 1/2 and the
prefix truncates the debt, so that draft failed and was narrowed.

### G.GPT147. at a fixed irrational angle, finite-tail phases are empty or countable and dense (second-read by Local, 2026-10-07)

### G147. At a fixed irrational angle, finite-tail phases are empty or countable and dense (2026-10-07)

**Status and target.** Symbolic Q7 corollary, independent review pending. No experiment or general symbolic-dynamics novelty claim. Uses the verified wall coding G140, radius clock G141/G142 and fixed-radius count G129. G145 is independently verified by Local L101. Prediction: varying the phase can give an almost-every-phase exclusion without deciding one exceptional phase. Counterfactual: density of the phase orbit would promote a finite-tail realization to an interval of finite-tail phases. The countability argument refutes that promotion. The phase-dependent repeat record is G143-G146; no external theorem beyond the elementary density of an irrational rotation is imported.

Fix any irrational beta in (0,1). For phases rho modulo2 let c^(rho)_s=floor(s*beta+rho) modulo2, and let

    E_beta = {rho : Phi(c^(rho)) has finite support}.

Then E_beta is countable and forward invariant under rho -> rho+beta modulo2. It is either empty or dense. In particular almost every phase has an infinite forced initial left tail, at every fixed irrational angle, including the exceptional phase-zero angles of G144. This statement does not exclude any specified phase in E_beta, or establish that E_beta is nonempty.

**Proof.** Distinct phases modulo2 give distinct visible words. Indeed the two shifted half-circle partitions disagree on a nonempty open interval of the length-two circle whenever their shifts differ modulo2. The forward orbit s*beta modulo2 is dense and enters that interval, giving a differing symbol. The uniqueness of Phi therefore makes the phase-to-initial-row map injective.

There are only countably many finite binary initial rows: at radius at most L there are at most 2^L. Injectivity gives at most 2^L phases in E_beta with radius at most L. Taking the union over positive integer L makes E_beta countable, hence of Lebesgue measure zero. The empty row is not compatible with the clock, as in G141.

The conjugacy gives F(Phi(c^(rho)))=Phi(c^(rho+beta modulo2)). Forward evolution preserves finite support, so E_beta is forward invariant. If it contains rho, it contains its whole dense irrational forward orbit. Its radii on that orbit are exactly R(rho)+2t by the radius clock. This proves the empty-or-dense dichotomy, and explains why countability and density do not conflict.

**Uniform-radius qualification.** Every fixed-radius phase set is finite. Consequently, along any convergent sequence of pairwise distinct phases in E_beta, the radii tend to infinity: a bounded-radius subsequence would lie in a finite set, contradicting distinctness. An interval of finite-tail phases is impossible, but a dense exceptional set of finite tails is allowed. No uniform-radius conclusion follows from density of one orbit.

**Unexpected check and remaining obligation.** The same countability argument applies at the silver angle even though G143 passes every repeat test and G145 fails every allowance at another phase. Conversely, assuming just one finite phase would supply a dense countable orbit with steadily growing radii, fully consistent with the infinite-support limits in G142/G146. Thus an almost-every-phase theorem, residual-set argument or dense collection of infinite tails cannot settle the individual boundary-phase candidate. E_beta has not been shown nonempty, and its countability is not a prize solution or an all-phase exclusion. The next obligation remains a spatial constraint on Phi(c^(0)), rather than another phase-counting estimate.

*Second reader's note on G147 (Local, 2026-10-07; chat L103).* Correct, checked by hand with G146 as asked; no run was
needed. Two phases that differ modulo 2 code by two half-circles of the length-2 circle whose symmetric difference is a
nonempty open set (the whole circle when the phases differ by 1, giving the complement), and the dense forward orbit
enters it, so phase to word is injective, and $\Phi$ makes phase to row injective. Countability follows from the
countable finite rows. $\sigma c^{(\rho)} = c^{(\rho + \beta)}$ with $F \Phi = \Phi \sigma$ gives forward invariance,
the dense forward orbit gives the dichotomy, and the radius clock gives $R(\rho) + 2t$ along it. One sharpening from
GC156: by the free odd depths, at most $2^{\lceil L/2 \rceil}$ phases in $E_\beta$ have radius at most $L$, not $2^L$.
The record certificate behind G129 also makes every member of $E_\beta$, at every angle, have radius above about 84.
This bounds nothing uniformly, as the block's divergence statement already says. GC164's warning is well placed: a
measure or census statement would be overwhelmingly negative and still blind to the countable set a candidate must lie
in.

### G.GPT148. fixed-order temporal differences preserve entropy but not the repeat sign (second-read by Local, 2026-10-07)

### G148. Fixed-order temporal differences preserve entropy but not the repeat sign (2026-10-07)

**Status and target.** Symbolic diagnostic audit, independent review pending. No experiment, shader change or new general finite-difference novelty claim. The owner linked the project to temporal motion fields; WHAT-WE-BUILT.md's overview and motion-field description were read, alongside the existing G96 transport guard, G138/G139 stationary-tail controls and G143's Sturmian derivative. Prediction: every fixed-order XOR temporal difference has the same word-count entropy as the original binary trace. Counterfactual: going to acceleration, jerk or another fixed order automatically reveals positive entropy missed by the visible trace. The elementary block argument refutes that implication, without refuting uses of these fields for specific structural diagnostics.

Let S shift a one-sided binary word forward, and let D=1+S over GF(2). For any fixed k>=1, D^k is the order-k XOR temporal difference. If P_x(n) counts the distinct length-n factors of x, then

    P_(D^k x)(n) <= P_x(n+k) <= 2^k P_(D^k x)(n).

The first inequality holds because the difference block is a fixed function of its n+k input symbols. For the second, each output block and the first k input bits determine all the remaining input bits: the coefficient of x_(s+k) in (D^k x)_s is one, so solve sequentially for x_k,x_(k+1),...,x_(n+k-1). There are at most 2^k possible first k bits. Thus the word-count entropies agree (using limsup log2(P(n))/n, and invariance under the fixed length shift k). This is valid for one word and its factors, not only for the full shift.

In particular every fixed-order difference of G143's silver code still has zero word-count entropy. The combined jet (x,Dx,...,D^k x) has exactly P_x(n+k) distinct length-n vector factors: its first component gives the n observed input bits; at the last observed time, levels 1 through k form a triangular system recovering the next k input bits in order, because each level has coefficient one on its newest input. Keeping all levels cannot add an entropy rate either. No assertion is made for k growing with the observation length, or for unbounded spatial windows.

**Period and sign controls.** G96 already proves the dyadic identity D^(2^m)=1+S^(2^m); it is reused, not rediscovered as a new result. Thus at these orders a zero difference interval is exactly an equality interval with lag 2^m. A nonzero difference distinguishes a complement-repeat from a repeat, which is the sign lost in the Sturmian integration in GC158. If D^k x is eventually zero, choose 2^m>=k and multiply by D^(2^m-k): x is eventually periodic with period dividing 2^m. More generally eventual periodicity of D^k x implies eventual periodicity of x, by integrating each order: when Dy is p-periodic, y_(s+p) XOR y_s is the constant parity of one derivative period, hence y is 2p-periodic. Iterating gives a sufficient period 2^k p. This period bound is not claimed optimal.

These XOR observables are different from ordinary signed finite differences on integer-valued samples. If an ordinary order-k difference of a bounded integer sequence is eventually zero, successive summation makes its tail a polynomial of degree at most k-1; boundedness forces that polynomial to be constant. For the alternating binary trace 0101..., D^2 x is zero, but its ordinary second difference is the alternating sequence -2,2,-2,2,... . XOR acceleration zero therefore does not mean a constant binary state, or zero ordinary acceleration.

**Unexpected support guard and next obligation.** G138's constant-zero visible code has the stationary checkerboard forced left row, with infinitely many ones. Every fixed-depth temporal column is constant, so all positive-order temporal differences vanish there, under either arithmetic. The derivatives discard the stationary spatial background. This directly refutes inferring finite spatial support from quiet temporal jets, even when every fixed order at every fixed depth is checked. G96 separately explains why fixed-cell differences are not physical acceleration of tracked structures. A productive next use must name a coupled spatial constraint or a specific phase/sign relation; it cannot rely on a generic entropy increase, derivative quietness or the mere word 'acceleration'. No finite initial-tail exclusion or prize claim follows.

*Second reader's note on G148 (Local, 2026-10-07; chat L104).* Correct, with both points GPT asked me to audit
confirmed. The block inversion: the coefficient of $x_{s+k}$ in $(D^k x)_s$ is $\binom{k}{k} = 1$, so the first $k$
input bits and an output block of length $n$ fix the input block of length $n + k$, giving
$P_x(n+k) \le 2^k P_{D^k x}(n)$. The joint jet: the first component gives the $n$ observed bits, and at the last
observed time level $j$ has coefficient one on $x_{t+j}$ with all its other inputs already known, so the jet block and
the input block of length $n + k$ determine each other and the count is exactly $P_x(n+k)$. The integration period $2p$,
the dyadic identity owned by G96, the ordinary-difference contrast and the stationary checkerboard all hold. The
checkerboard is fixed by every single wall step, since every cell has a black cell among its centre and right inputs
(the wall included) and so becomes the complement of its left neighbour, which is its own value. Checked
(`rule30_audit_g99_g100.py`, S43): both inequalities and the exact jet count for $k \le 5$ and $n \le 12$ on GC159's
silver prefix and 20 random words; the dyadic identity for $m \le 4$; the period $2p$ for every derivative pattern with
$p \le 6$; the $0101\ldots$ contrast; and the checkerboard fixed for 40 single steps.

### G.GPT149. eventually finite compatible rows have exactly zero-reaching periodic tails (second-read by Local, 2026-10-07)

### G149. Eventually finite compatible rows have exactly zero-reaching periodic tails (2026-10-07)

**Status and target.** Symbolic Q7 tail reduction, independent review pending. No experiment. Uses the reviewed inverse-pair maps and periodic-tail classification G124, the wall coding G140 and predecessor/radius facts G141/G142. Existing-record search found these ingredients but not the all-depth equivalence below. No novelty claim for finite-state inversion or backward shift density. Prediction: finite future support is a stricter spatial-tail property than mere eventual periodicity, but is invariant under finite visible-prefix changes. Counterfactual: a periodic initial tail or a quiet temporal field automatically supplies a finite future row. The stationary checkerboard refutes that shortcut.

Write S for the compatible initial left rows with imposed wall 0101..., F for two physical steps, and S_fin for its finite-support rows. Define

    S_event = union_(k>=0) F^(-k)(S_fin), inside S.

Then u belongs to S_event if and only if its initial far-left tail is eventually spatially periodic, with that periodic pattern reaching the all-zero pattern after a finite number of ordinary Rule30 steps. This is an exact characterization of becoming finite later, not of being finite at time zero.

**Necessity, using both neighboring cells.** Suppose F^k(u) is finite, so the row at physical time 2k is eventually zero. A single backward step solves the known inverse recurrence

    q_(j+1)=y_j XOR (q_j OR q_(j-1)).

If the output y has an eventually periodic tail of period p, the outward recursion is a deterministic finite-state system: its state is the adjacent input pair together with position modulo p. There are 4p states. Along the actual predecessor row the state eventually repeats, so the predecessor also has an eventually periodic spatial tail. No injectivity, finite predecessor or particular choice of near-wall bits is assumed. Repeating this argument for all 2k backward steps proves that u has an eventually periodic tail.

For any fixed number of forward steps, sufficiently far-left cells have cones disjoint from the finite head and the wall. Their evolution is therefore exactly the ordinary Rule30 evolution of this periodic tail pattern. Since the output after 2k steps is eventually zero, the whole periodic pattern reaches zero by then. G124 now restricts its least spatial period to 1 or 3*2^a, a>=0. For k>=1 a nonconstant such pattern has a<=2k-2, since the two final steps are period3 -> all ones -> all zeros, and each earlier backward period can at most double. Thus its least period is at most 3*4^(k-1). These bounds describe tails only; they do not decide the wall compatibility of a finite head.

**Sufficiency.** Conversely, suppose u is in S and its eventual periodic tail pattern reaches zero after T steps. Beyond the finite head enlarged by the T-step light cone, the evolved row is zero. It has finite support. Advance to the next even physical time if T is odd; finite support is preserved. Thus F^ceil(T/2)(u) is finite and u belongs to S_event. The imposed wall and its compatibility must be retained; a tail pattern alone is not a construction of such a u.

**Visible-prefix interpretation and density qualification.** Let C_fin=Phi^(-1)(S_fin). G140's conjugacy gives

    Phi^(-1)(S_event)=union_(k>=0) sigma^(-k)(C_fin).

Each length-k binary prefix can be prepended freely to any c in C_fin, producing a compatible row that becomes Phi(c) after k two-step iterates. All these ancestors have zero-reaching periodic spatial tails by the equivalence just proved. Initial finiteness itself is not asserted for them; G141 explains that ancestors may instead have black or period-three tails.

S_event is countable: S_fin is countable, and each finite row has exactly 2^k compatible preimages under F^k by the full one-sided shift coding. It is empty exactly when S_fin is empty. If nonempty, it is dense in S: to match any finite visible prefix w, prepend w to one chosen c in C_fin. Continuity of Phi transfers this cylinder density. This countable dense conditional family is not a finite-support compact family or an existence proof.

**Unexpected periodic-tail control and consequence.** A spatial 001 tail evolves to all ones and then zero. A spatial 01 checkerboard is stationary, so periodicity alone does not suffice. G138/G140's compatible checkerboard example has quiet temporal columns and lies outside S_event. Conversely a zero-reaching tail class, if wall-compatible, gives a finite future row even though its initial support can be infinite. These are far-tail identities, not new experiments or candidate constructions.

An unbounded-debt visible word cannot lie in S_event: if any shift had a finite compatible row, its repeat allowance would be finite; G146's reverse-shift control would give one for the original word. Hence G145's half-phase code has neither a finite initial tail nor any zero-reaching eventual periodic tail. The phase-zero silver code remains unresolved. For it, proving an aperiodic tail or a periodic tail outside the zero basin would exclude even future finiteness; proving membership in the zero-reaching tail class would instead supply a finite compatible future row. Full right extension and a finite global seed remain separate obligations. No prize conclusion follows.

*Second reader's note on G149 (Local, 2026-10-07; chat L105).* Correct. Necessity: the inverse recursion run outward on
an output with eventual period $p$ is a finite-state system on (pair, position modulo $p$), so every predecessor,
whatever its near-wall bits, has an eventually periodic tail, and $2k$ steps carry this back to $u$. Far cells see
neither the head nor the wall for a fixed number of steps, so the tail pattern itself must reach zero by time $2k$. The
period bound rests on G124's reviewed rule that a nonconstant output's periodic predecessors at most double the least
period, with the only other step $001 \to 111$; so a nonconstant tail has period $3 \cdot 2^a$ with $a \le T - 2$ and
$T \le 2k$. Sufficiency, the prefix interpretation, countability through exactly $2^k$ preimages, and conditional
density all hold, and the unbounded-debt exclusion is right by G146's reverse-shift control. Checked
(`rule30_audit_g99_g100.py`, S44): on every cyclic ring up to size 24, each row reaching zero has least period 1 or
$3 \cdot 2^a$ with $a \le T - 2$; from 200 random finite rows, one to four backward wall pairs give eventually periodic
tails of an allowed period that reach zero within $2k$ ordinary steps, and each evolves forward to its finite row; and
the 001 and 01 controls. The first run of the second part failed through my own orientation slip: the depth-indexed
tails, which run leftward, were fed to a ring that reads left to right. Reversed, every case passes.
*Correction (Local, 2026-10-07, chat L109).* The ring part of S44 was not exhaustive as first run: it followed each
row forward for only $3n + 3$ steps, and on the 24-ring 2,592 rows first reach zero later, up to step 147. S44 now
takes the exact basin from a backward search from zero, cross-checked on the 24-ring against 1,500 forward steps,
and the period statement holds on every zero-reaching row of every ring up to size 24.

### G.GPT150. a zero-gap parity criterion determines every periodic predecessor period (second-read by Local, 2026-10-07)

### G150. A zero-gap parity criterion determines every periodic predecessor period (2026-10-07)

**Status and target.** Symbolic periodic-tail refinement, independent review pending. No experiment. Uses reviewed G13's exact reset language and G124's inverse-pair period bound; relevant prior-art scope is in PRIOR-ART.md. Prediction: for a nonconstant periodic output, the stay-or-double choice is determined by a parity of its cyclic zero gaps. Counterfactual: G124's bound alone leaves that choice unspecified. The two-state return calculation below supplies the exact choice and counts the aligned whole-line predecessors. This concerns ordinary spatial rows, not temporal diagonals or a forced-wall finite head.

Fix a nonconstant whole-line output y of least spatial period p. Around one primitive period, list the lengths L of runs of ones between consecutive zeros, including L=0 for adjacent zeros. Then:

- If any L is 1 modulo3, y has exactly one whole-line predecessor, of least period p.
- Otherwise, let N count the gaps with L=2 modulo3. If N is even, y has exactly two whole-line predecessors, both of least period p. If N is odd, it has exactly two whole-line predecessors, both of least period 2p; translation by p exchanges them.

Every whole-line predecessor is periodic. Counts are for a fixed labeled output y, without quotienting the predecessors by spatial phase. Constant outputs are separate: zero has its two constant predecessors, and one has the three period-three phases from G124.

**Return-map proof.** Use G13's adjacent input state (a,b) and descending driver transitions

    T_y(a,b)=(b, y XOR (a OR b)).

Reading one spatial output period gives a deterministic map H on four states. A whole-line predecessor supplies a bi-infinite orbit of H at successive period cuts. Every such orbit lies on a cycle: in a finite functional graph, a noncycle point has only a bounded backward transient; a deterministic cycle cannot be exited. Conversely every cycle point determines a unique predecessor by following the within-period transitions in both directions. This also proves that no nonperiodic whole-line predecessor was omitted.

If a cyclic gap has L=1 modulo3, repetitions of the driver contain the G13 reset factor 0 1^(3h+1) 0 z. Some power of H therefore has singleton image. H has exactly one cycle point and that point is fixed, giving one p-periodic predecessor. Least period is p because an output's least period divides every predecessor period. The reset factor may straddle periods; it is not necessary that H itself already have rank one.

Suppose no gap is 1 modulo3. After sufficiently many zeros, the surviving pair-state set just after a zero is either

    C={00,11},    A={00,01}.

This follows from G13's image table: the second zero reduces the full image to at most two states, and in the absence of the forbidden gap the after-zero sets are C or A. Label 00 as zero and the other state as one. Direct use of the four-state transition table gives, for a run of L ones followed by a zero:

| L modulo3 | Starting C or A | Ending set | Label map |
|---|---|---|---|
| 0 | either | C | identity |
| 2 | either | A | interchange |

This includes L=0. For positive multiples of three, T_1 cycles 00->01->10->00, and the following zero yields C with the same labels; for residue two the following zero yields A with exchanged labels. In particular both labels survive every permitted gap. At a fixed cyclic cut the set type returns to itself, so H on its recurrent two-state set is identity when N is even and interchange when N is odd. The corresponding one- or two-period cycles give exactly the stated two predecessors. Output least period p rules out any smaller period; the interchange case is not p-periodic, so its least period is 2p.

**Independent arithmetic controls, without a run.** Output (001)^infinity has a cyclic one-run of length1 and the unique predecessor (101)^infinity. Output (011)^infinity has one gap of length2, hence two period-six predecessors: (001010)^infinity and its translate by three, as in G124's literal trajectory. Output (000111)^infinity has gaps 0,0,3 and no interchange; its two period-six predecessors are (000010)^infinity and (111001)^infinity. Their six literal triples give the same labeled output 000111. This last example is the unexpected guard: absence of a reset does not itself imply period doubling; the parity is essential. Constants cannot be put into the zero-gap rule unchanged.

**Tail implication and limit.** G149's backward periodic tail can now be classified at each step by reset presence and this parity, rather than only bounded by p or 2p. A reset fixes the tail independently of the finite head; without one, the head selects a surviving label, possibly only the phase of a doubled tail. This does not bound reset gaps across successive backward rows, determine the boundary-phase silver initial tail, or prove a forced wall has a finite head. The one-step criterion must not be iterated as though its gap counts stayed unchanged. No new run, finite witness or prize conclusion follows.

*Second reader's note on G150 (Local, 2026-10-07; chat L106).* Correct. I checked the gap-label table by hand from the
descending transitions: after a zero the surviving pair sets are $\{00, 11\}$ or $\{00, 01\}$. A run of ones of length
$0 \bmod 3$ returns to the first set with labels kept, one of length $2 \bmod 3$ ends in the second set with labels
exchanged, and a run of length $1 \bmod 3$ is G13's reset. The aligned counts follow from the cycle structure of the
period return map. Every whole-line predecessor is periodic because its cut states form a bi-infinite orbit of a finite
deterministic map. The counts were also checked by a method that does not use the reset machinery
(`rule30_audit_g99_g100.py`, S45). For every nonconstant cyclic output of least period at most 14 (32,474 outputs:
28,637 with a reset, 1,872 even, 1,965 odd), the left-to-right transfer matrix counts the predecessors on rings of size
$mp$ for $m = 1$ to 6. They are 1 for every $m$ with a reset, 2 for every $m$ with even parity, and 2 or 0 by the parity
of $m$ with odd parity, so no predecessor of period $3p$, $4p$, $5p$ or $6p$ exists anywhere in that range. The three
literal controls were checked as ring steps. GC167's caution stands: the criterion is exact for one step, and the gaps
change from row to row.

### G.GPT151. backward period doublings cannot be consecutive (second-read by Local, 2026-10-07)

### G151. Backward period doublings cannot be consecutive (2026-10-07)

**Status and target.** Symbolic tail-period refinement, independent review pending; G150 independently verified by Local L106. No experiment. Uses G150's two-label criterion and reviewed G13/G124. Prediction: a doubled predecessor necessarily acquires a reset, forcing the next backward step to preserve its period. Counterfactual: the bound p or 2p permits doubling at every backward nonconstant row. The reset argument excludes that possibility; it gives no upper bound on the delays between doublings or a wall-support conclusion.

Let y be a nonconstant periodic ordinary Rule30 row of least period p, and suppose its predecessor x has least period 2p. Then x contains a cyclic factor 010. Consequently x has exactly one whole-line predecessor z, with least period 2p. In particular no periodic backward chain has consecutive doublings between nonconstant rows.

**Proof.** By G150, y has no resetting zero gap, and an odd number of its cyclic runs of ones have length 2 modulo3. Choose one such run, whose length is at least two. At the cut just after the preceding zero the inverse recurrent pair set is C={00,11} or A={00,01}. Label 00 as zero and the other state as one. One p-period interchanges the labels. Thus in the doubled predecessor x, the selected cut takes both labels one p apart. At the occurrence with label zero, the actual adjacent input pair is 00. The first two driver ones give

    00 --1--> 01 --1--> 10.

The consecutive reconstructed input symbols are therefore 0,1,0. Reversing the spatial reading direction leaves 010 unchanged. Since x is a whole-line periodic row there is also a following symbol, so G13's reset factor 010z occurs. G150's reset case now gives exactly one predecessor of x, of the same least period 2p. This proves the claim without assuming any particular finite head or boundary bit.

**Improved zero-basin time bound.** If a nonconstant periodic pattern first reaches zero at physical time T>=2, the last two backward states are the all-one row and a period-three phase of 001. That period-three pattern has a cyclic 010 reset, so the next earlier pattern, if present, must also have period three. Beyond it, no two consecutive steps can double. Thus if the original least period is 3*2^a,

    a <= floor((T-2)/2),
    period <= 3*2^floor((T-2)/2).

This is stronger than G124/G149's a<=T-2 cap. In G149's setting, a compatible row becoming finite after k two-step iterates has a nonconstant zero-reaching eventual tail with

    a <= k-1,    period <= 3*2^(k-1),    k>=1.

If its periodic tail reaches zero earlier, apply the first-hit statement with that earlier T<=2k. Constant tails retain least period one. The former 3*4^(k-1) bound remains true but is superseded by this stronger bound; no reviewed text is invalidated.

**Independent control and unexpected sharpness guard.** The literal six-site trajectory extends G124 as

    101011 -> 001010 -> 011011 -> 010010 -> 111111 -> 000000.

The first arrow is checked by its six ordinary left-to-right triples, which give 0,0,1,0,1,0. The first two words have least period six; 011011 and 010010 have least period three. Read backward, the 3-to-6 doubling is followed by a 6-to-6 preservation, exactly as proved. Moreover 101011 itself has cyclic factor 010 (at positions 1,2,3), so its predecessor again preserves period six. The control prevents claiming that the upper bound is automatically attained by doubling every other step. No such matching all-depth construction is supplied.

**Scope.** This sharpens the periodic spatial zero basin and the conditional ancestors of finite compatible rows in G149. G123's canonical periods still have unbounded growth, and this theorem does not bound the gaps between their increases. It does not prove that the phase-zero silver tail is periodic, zero-reaching, finite or infinite. A new multi-row invariant or an actual all-depth tail classification is still required. No new computation, full right extension or prize conclusion follows.

*Second reader's note on G151 (Local, 2026-10-07; chat L107).* Correct, read jointly with G150. In the doubled case the
selected residue-two run sees both labels one period apart, and at the label-zero occurrence the pair is $00$; two
driver ones give $00 \to 01 \to 10$, so the reconstructed inputs read $0, 1, 0$, a run of one 1 between zeros, which is
G150's reset case for $x$. The time indexing is right: below the all-one row and the period-three phase of $001$ (which
itself contains $010$, forcing the next row back to period three) there remain $T - 3$ backward steps, so at most
$\lceil (T-3)/2 \rceil = \lfloor (T-2)/2 \rfloor$ non-consecutive doublings, and $a \le k - 1$ in G149's setting.
Checked (`rule30_audit_g99_g100.py`, S46): for all 672 doubling outputs of least period at most 12, both period-$2p$
predecessors (found by the descending recursion and confirmed forward) contain $010$ and have exactly one predecessor on
rings of size $2p$ and $4p$; on every ring up to size 24 (all 3,168 rows first reaching zero at time 2 or later; the
per-size cap was never hit) the period obeys $a \le \lfloor (T-2)/2 \rfloor$; and the six-site trajectory, with
$101011$'s own $010$.
*Correction (Local, 2026-10-07, chat L109).* "All 3,168 rows" was wrong: I checked that a sampling cap was never
hit and missed that the forward run stopped after $3n + 3$ steps. On the 24-ring 2,592 rows first reach zero later,
up to step 147. With the exact basin from a backward search the complete count of rows first reaching zero at time
2 or later, on rings up to 24, is 5,760, and every one obeys $a \le \lfloor (T-2)/2 \rfloor$.

### G.GPT152. rotation classes sharpen the periodic zero-basin first-hit bound (second-read by Local, 2026-10-07)

### G152. Rotation classes sharpen the periodic zero-basin first-hit bound (2026-10-07)

**Status and target.** Symbolic refinement, independent review pending. No experiment. Uses reviewed G123/G124. Prediction: quotienting translations sharpens the labeled-ring first-hit bound because a zero-reaching orbit cannot revisit a rotation class. Counterfactual: distinct labeled rows might require counting all their phases separately. An absorbing quotient argument removes those phases. Existing-record search found no necklace bound; necklace counting and cellular-automaton rotation quotients are established prior art, recorded in PRIOR-ART.md. No novelty claim for the method.

Let x be a nonconstant spatially periodic Rule30 row of least period p that first reaches zero at physical time T. By G124, p=3*2^a for some a>=0. Define L(q) to be the number of binary rotation classes of least period q. Then

    T+1 <= C_a := 2 + sum_(b=0)^a L(3*2^b),
    L(3)=2,
    L(q)=(2^q - 2^(q/2) - 2^(q/3) + 2^(q/6))/q  for q=3*2^b, b>=1.

In particular p=3 forces T<=3; p=6 forces T<=12. These are upper bounds, not assertions that each is attained.

**No repeated rotation class.** Write x_i=F^i(x), 0<=i<=T. Suppose x_j is a spatial translate of x_i for i<j<=T. On the p-cell ring the update commutes with rotations, so it induces a deterministic map on rotation classes. The class of x_i then lies on a cycle of length dividing j-i. It cannot subsequently enter the distinct absorbing class of zero. If the class already is zero, the first-hit property instead gives i>=T, impossible. Thus all T+1 classes are distinct. This uses no assumption that the cellular automaton is injective.

Every intermediate row reaches zero and has spatial period dividing p. G124 therefore permits only least period one or 3*2^b, 0<=b<=a. Period one contributes precisely the constant zero and constant one classes. Counting all binary classes of the remaining permitted periods gives C_a; some counted classes may lie outside the zero basin, so the inequality can be strict. A primitive word of length q has q distinct rotations even when repeated on a larger p-cell ring. There is no additional factor p/q in the class count.

**Counting derivation.** If A(q) counts labeled binary words of least period q, then 2^q=sum_(d|q) A(d). Divisor inversion gives A(q)=sum_(d|q) mu(d)*2^(q/d), where mu is the ordinary Moebius function. Dividing by q gives L(q). For q=3 the only squarefree divisors are 1,3. For q=3*2^b, b>=1, they are 1,2,3,6; their signs give the displayed formula. This is the standard primitive-necklace formula, not a new counting identity.

**Asymptotic consequence.** Along p=3*2^a tending to infinity, C_a=(1+o(1))*2^p/p. The largest term L(p) has that asymptotic by its explicit formula; all smaller terms together are at most a*2^(p/2), whose ratio to 2^p/p tends to zero. Hence along zero-reaching rows with T tending to infinity,

    p >= log2(T+1) + log2(log2(T+1)) - o(1).

Indeed log2(T+1)<=p-log2(p)+o(1), while the original labeled-ring count gives p>=log2(T+1); substituting that lower bound inside log2(p) yields the claim. G123's canonical ancestor tail C_n first reaches zero at time n, so the same bound applies to its p_n. This improves a generic counting floor; it gives no upper bound on doubling gaps or a temporal-wall exclusion.

**Independent arithmetic control and unexpected guard, by hand.** The two primitive period-three classes are represented by 001 and 011. The literal trajectory 011 -> 010 -> 111 -> 000 visits both classes (010 is a rotation of 001) and then the two constants; T=3 attains C_0-1. At period six the four-term formula gives (64-8-4+2)/6=9, so C_1=2+2+9=13. Counting labeled primitive words would instead give 54 and miss the rotation reduction. As the identified unexpected scope check, the stationary checkerboard has least period two and revisits its rotation class forever: the no-repeat argument requires eventual absorption at zero, not mere periodicity or finite ring size. None of these controls is a numerical run.

**Scope.** This is a necessary first-hit bound for periodic spatial tails and the reviewed canonical ancestry. It neither constructs a finite compatible wall head nor identifies the silver phase-zero forced tail. The all-depth wall-tail obligation remains open.

*Second reader's note on G152 (Local, 2026-10-07; chat L109).* Correct. The rotation quotient is deterministic because
the update commutes with rotations; a revisited class would lie on a cycle of the quotient, and the zero class is a
fixed absorbing class, so a revisit forces the class to be zero before the first hit. Every row on the trajectory
reaches zero and has period dividing $p$, so G124 leaves only the constants and the primitive periods $3 \cdot 2^b$,
$b \le a$. The Moebius count is the standard primitive-necklace formula, with $L(3) = 2$, $L(6) = 9$ and $L(12) = 335$.
The asymptotic substitution is right: the smaller terms total at most $a \, 2^{p/2}$, which is negligible against
$2^p/p$, and $\log_2 p \ge \log_2 \log_2 (T+1)$ follows from the labeled count. Checked (`rule30_audit_g99_g100.py`,
S47): the three necklace counts by brute force; on rings of size 3, 6, 12 and 24 every zero-reaching row's trajectory
visits distinct rotation classes, all of allowed periods, with $T + 1 \le C_a$; and the period-three trajectory
attaining $C_0 - 1 = 3$. The largest first-hit times are 3, 10, 17 and 147, far inside the bounds 4, 13, 348 and
699,218. Writing S47 exposed a fault in my S44 and S46 ring censuses, which stopped each row after $3n + 3$ steps; all
three checks now use the exact basin from a backward search (corrections in the G149 and G151 notes).

### G.GPT153. Rudin–Shapiro passes the necessary repeat-debt filter (second-read by Local, 2026-10-07)

### G153. Rudin–Shapiro passes the necessary repeat-debt filter (2026-10-07; computer-assisted theorem)

**Status.** Computer-assisted theorem, independently verified by Local L111 at 8f7841c. The direct RSP-S semantic reconstruction and debt-product argument have been audited and independently replayed; the Walnut compilation dependency is discharged. RSP preregistration was pushed at dd61eb5 before runs. No finite-left realization or prize claim. The raw universal decision is TRUE and an independently implemented graph-product check agrees, conditional on the compiled repeat predicate's semantics. The standard automatic-sequence logical decision theorem is the prior-art method, not a new technique.

Let r(n) be the parity of overlapping occurrences of11 in the binary representation of n, r(0)=0. Proposed statement: for every a,b>=0 and q>=1, if r(s)=r(s+q) for all a<=s<=b with b>=a, then

    b <= 2*a+q.

Thus Safe(0) and Bounded in the RSP plan hold. This is a necessary-filter pass, not a candidate construction. RSP2 was not run because a verified Safe(0) would already settle Bounded positively.

**Certificate chain.** The four-state output automaton remembers the last binary digit h and the parity e. Reading d updates (h,e) to (d,e XOR h*d); induction on digits proves the definition of r, including leading-zero padding. Pinned Walnut7.1.0 source commit67e69c248d07324b25de1d4a498e877ac504999a compiled the exact RSP predicate

    q>=1 AND b>=a AND FOR ALL s:
        (a<=s AND s<=b) IMPLIES r(s)=r(s+q)

into a deterministic78-state automaton over synchronized most-significant binary digits of (a,b,q). Its exported file SHA256 is1a0f3ac7b9222da522c2077b1dbeccb8098bc9df15a1200af6920a2243f309b6. Review artifacts rsp-repeat-dd61eb5.txt and rsp-product-dd61eb5.json are in the shared scratch; bulk outputs stay outside Git. The formula, driver and replay verifier are in tests/probes/prizes/rudin_shapiro_repeat.py.

The independent checker intersects that exported relation with a separately derived debt comparator. After a digit triple, the signed prefix debt d=b-2a-q updates to 2*d+b_bit-2*a_bit-q_bit. Values at most-1 stay negative under all later digits; values at least3 stay positive. Saturation to the five states -1,0,1,2,3 is therefore exact, with final d>0 accepting. Breadth-first traversal of the product has84 reachable states and no accepting state. Closed reachability proves emptiness for all finite digit strings, not a finite integer horizon. This product check alone does not establish the compiled relation's semantics. The separate RSP-S reconstruction, audited and replayed by Local L111, discharges that dependency for this exported relation. Walnut's separately compiled universal formula also returned TRUE.

**Controls and failures.** RSP0 passes: the supplied generator versus the integer bit-count formula at0..4095 and189 selected64-bit carry-boundary inputs;2040 admissible literal repeats through a,b<=15 and q<=15; constant-zero and alternating Bounded=FALSE controls; and G137's powers-of-two Safe(0)=TRUE control. An expanded4096-tuple replay includes q=0 and reversed ranges and checks three additional leading zeros. The debt comparator matches32768 independent integer comparisons through31. These finite controls check instruments, not the universal theorem. The identified unexpected padding check is supplemented by the initial all-zero-digit self-loop and unbounded finite-graph traversal; no fixed bit width is used.

The first RSP0 run failed because Walnut resolves command filenames inside its command directory; the absolute positional filename was invalid. That failed run is retained, lookup corrected, and RSP0 completed before RSP1. Python's toolchain metadata request also failed its certificate-store check; system curl succeeded without disabling TLS. A checksum-verified portable Java archive and isolated tool/dependency caches were used, with no system-runtime installation. Formula processes had120 CPU-second limits,768MiB Java heap bounds,1GiB sampled-RSS termination checks and an additional180-second wall limit. No limit was approached: successful formulas took about0.42 seconds wall each, with sampled peak RSS below50MiB. Resource samples are not exact peak-memory measurements. No Local computational job was duplicated.

**Scope and next obligation.** After independent review, the ordinary repeat-filter exclusion route is closed for this specific automatic word. Its forced initial tail and full right extension remain unresolved. Passing this necessary inequality is neither finite evidence for support nor a theorem that a compatible finite row exists.

*Second reader's note on G153 (Local, 2026-10-07; chat L111).* Correct as a computer-assisted theorem, with the semantic
dependency on Walnut discharged. The definition, the inclusive endpoints and the quantifiers match the RSP plan and
G135's convention, and the first interval $[0, 1]$ at period 1 has debt exactly 0, so $C = 0$ is tight. I audited
RSP-S's three steps. The carry completion holds, since $s \le b$ fits the input width and $s + q$ needs at most one more
digit, so one implicit zero digit closes the carry and the last adjacent pair. The reversal holds: reversing the
exported automaton makes its accepting states the starts and its initial state the target, and a simultaneous subset
search that closes decides language equality for every nonempty input. The adjacent-11 parity is the same in either
reading direction. The saturated debt comparator is exact, since $2(-1) + 1 < 0$ and $2 \cdot 3 - 3 \ge 3$. Checked in
code sharing nothing with GPT's (`rudin_shapiro_review.py`). RV1: the exported relation agrees with brute force on all
$32^3$ triples at two paddings. RV2: my own debt product on it reaches 84 states and no violation. Reproduced on this
machine: RSP-S's equivalence closing at 17,033 states with the mutation caught at $(0, 0, 0)$, and G153's replay with 84
product states. Both GPT scripts need Python 3.10 or later for `int.bit_count`, and this machine's default is 3.9. My
first attempt, an independent most-significant-digit construction, was stopped at 3 GB while still determinising once
GC177 showed GPT had closed that lane; it is kept in the script's docstring. The scope stands as written: this closes
the repeat-filter route for this word at this start, and says nothing about its forced tail.

### G.GPT154. finite-tail exceptions in a minimal trace family are empty or countable dense (second-read by Local, 2026-10-07)

### G154. Finite-tail exceptions in a minimal trace family are empty or countable dense (2026-10-07)

**Status and target.** Symbolic scope audit, independently verified by Local L112; no computation. Uses reviewed G140's wall coding and radius clock, and generalizes G147's phase-counting argument to a minimal trace family. This is an elementary dynamical argument, not a novelty claim about substitution systems. Prediction: generic infinite support cannot exclude the original Rudin–Shapiro trace. Counterfactual: minimal recurrence plus a generic exclusion forces every individual trace to have an infinite tail. The conditional dense-exception argument below shows why that inference fails. G153 and its RSP-S certificate are not assumed in this proof.

Let X be a nonempty compact, forward-shift-invariant family of one-sided visible binary words in which every forward orbit is dense. Assume X is infinite. Under G140's bijection Phi from visible words to compatible white-phase initial rows, set

    E_X = {c in X : Phi(c) has finite left support}.

Then E_X is empty or countable dense in X. Its complement is residual and has full measure for every shift-invariant probability measure on X. For each fixed radius L, at most 2^L words of E_X have radius at most L. None of these statements excludes a specified word of X.

**Proof.** There are at most 2^L binary rows supported in the first L cells. Injectivity of Phi gives the same bound for words, so E_X is countable. The conjugacy F Phi = Phi shift and finite-support preservation show that E_X is forward invariant. If nonempty, it contains a dense forward orbit and hence is dense. On that orbit radii increase by exactly two at each shift.

An infinite minimal compact trace family has no eventually periodic points: such a point would yield a finite periodic orbit in X, whose dense orbit would force X to be finite. It also has no isolated points. If a cylinder isolates c, minimality supplies a positive return of c to that cylinder, forcing shift^n(c)=c. More explicitly, compactness gives a finite cover by inverse images of that cylinder; applying the cover to shift(c) supplies the positive return. The resulting periodic point contradicts infinitude. Thus each singleton is nowhere dense, and countability makes E_X meagre. For an invariant probability measure, an atom at c would give every distinct forward image mass at least that atom's mass, since the preimage of the image contains c. Infinitely many such images contradict total mass one. Hence every such measure is nonatomic and E_X is null. This argument does not require Phi to preserve a preferred measure.

**Rudin–Shapiro supplies such an X.** Write r(n) for adjacent-11 parity. Appending a binary digit gives r(2n)=r(n) and r(2n+1)=r(n) XOR (n modulo 2). The pair (r(n),n modulo 2) is the fixed word starting at a of the substitution

    a -> ab, b -> ad, c -> cd, d -> cb,
    a=(0,0), b=(0,1), c=(1,0), d=(1,1).

Its directed graph reaches a from every letter in at most three steps and reaches every letter from a in at most three; the a self-loop pads each composed path to exactly six. Thus every sixfold substituted letter contains every letter. Any factor of the fixed word occurs inside some substituted prefix of a; consequently every sufficiently large substituted letter contains it. The fixed word is tiled by equal-length such substituted letters, so every sufficiently long factor contains that chosen factor. Projecting to the first coordinate preserves this bounded-gap property. The binary shift closure X_r is therefore minimal: every factor of r occurs in every member with bounded gaps, so every forward orbit meets every cylinder of X_r.

For completeness r is not eventually periodic. For m<2^(k-1), the separated binary blocks give r(2^k+m)=r(m) and r(3*2^k+m)=1 XOR r(m). If r were eventually q-periodic, taking k arbitrarily large in the first identity transfers that periodicity to every initial m, making it purely q-periodic. Now choose k with 2^(k-1)>q. The first identity at m=0 through q-1 says translation by 2^k fixes the entire q-periodic word; translation by 3*2^k must then fix it too. The second identity at m=0 contradicts that, since r(0)=0 and r(3*2^k)=1. Thus X_r is infinite and the stated dichotomy applies.

**Unexpected periodic-family check.** If X is instead a finite periodic orbit, E_X is empty: a finite row corresponding to a p-periodic visible word would return after p applications of F, contradicting radius growth by 2p. The all-zero visible control gives the infinite checkerboard initial tail, not a finite row. This verifies why temporal simplicity is not a spatial-support certificate.

**Scope.** For Rudin–Shapiro, generic members of its binary shift closure have infinite forced initial tails, independently of the pending repeat-filter decision. If even one member has finite support, its dense shift orbit has growing finite radii and remains fully consistent with generic infinite support and infinite-support accumulation points. The original r is a specified member; this argument neither excludes it nor constructs an exception. The missing obligation remains a direct spatial-tail constraint on Phi(r), and full right extension is separate. No prize claim.

*Second reader's note on G154 (Local, 2026-10-07; chat L112).* Correct; every hypothesis is stated and used. The
substitution follows from appending a digit: $r(2n) = r(n)$ and $r(2n+1) = r(n) \oplus (n \bmod 2)$, so a letter
$(r, p)$ becomes $(r, 0)(r \oplus p, 1)$, which is $a \to ab$, $b \to ad$, $c \to cd$, $d \to cb$. Its graph reaches $a$
from every letter and every letter from $a$ within three steps, and the loop at $a$ pads to exactly six, so the sixth
power is positive. Uniform recurrence of the fixed word passes to its first coordinate because a factor of $r$ is the
projection of the factor of the pair word at the same positions. Minimality then gives the two generic statements. An
isolated point would return to its own cylinder and be periodic, so singletons are nowhere dense. An atom would put at
least its mass on every distinct forward image, since each image's preimage contains the point. The block identities
need $m < 2^{k-1}$ so that the digit after the leading 1 or 11 is 0, and both proofs use exactly that. One sharpening,
as in G147: by GC156's free odd depths, at most $2^{\lceil L/2 \rceil}$ words of $E_X$ have radius at most $L$. Checked
(`rule30_audit_g99_g100.py`, S48): both digit recurrences for $n < 2^{14}$; the pair word equals the substitution's
fixed word on $2^{14}$ letters; the sixth power of the letter matrix is positive; and the separated-block identities for
$k \le 12$.

### G.GPT155. trace factor complexity bounds the number of finite-tail exceptions (second-read by Local, 2026-10-07)

### G155. Trace factor complexity bounds the number of finite-tail exceptions (2026-10-07)

**Status and target.** Symbolic deduction, independently verified by Local L113; no computation. Uses reviewed G139 inverse locality, G140 coding/radius growth and G154 (Local L112). The record search found G147/G154's exponential fixed-radius count and G139's fixed-depth temporal factor bound, but not this growing-radius exception count. This is an elementary application of substitution factor counting, not a new general complexity theorem. Prediction: Rudin–Shapiro's exception count is at most linear in radius. Counterfactual: temporal zero entropy alone resolves whether there is even one finite-tail exception; the matching conditional lower bound shows the remaining gap.

For a forward-shift-invariant trace family X, let P_X(k) count its length-k factors and N_X(L) count c in X whose compatible initial row Phi(c) has radius at most L. For integers L>=1, put k=ceil(L/2). Then

    N_X(L) <= P_X(k).

**Proof.** G139's inverse recurrence determines the first L initial cells from the visible prefix c_0 through c_(k-1): the physical-time determining window at depth j is [0,j-1], containing exactly ceil(j/2) even samples. Thus two visible words sharing their first k bits have identical initial rows through depth L. If both rows are zero beyond L, the entire rows agree; injectivity of Phi makes the words identical. Hence the exceptional words inject into their length-k prefixes, a subset of X's factors. This also proves Local L112's sharper universal bound 2^k, without assuming that different arbitrary length-k prefixes necessarily produce different length-L rows.

**Rudin–Shapiro bound.** Use G154's four-letter length-two fixed substitution word. For k>=1 choose m minimal with h=2^m>=k; then h<2k. Any length-k factor fits inside two consecutive level-m substituted letters, with its start at one of h offsets in the first. There are at most sixteen ordered letter pairs. Projection to the binary word cannot increase this count, so

    P_(X_r)(k) <= 16*h < 32*k,
    N_(X_r)(L) < 32*ceil(L/2).

This is a deliberately coarse all-length bound, not a claim about the exact known factor complexity. If a finite-tail exception c of radius R exists, its time shifts have distinct radii R+2t. For L>=R this gives

    N_(X_r)(L) >= floor((L-R)/2)+1.

Consequently N_(X_r) is either identically zero or grows linearly in L, with matching upper and conditional lower orders. No existence has been supplied.

**Unexpected endpoint check.** Replacing ceil(L/2) by floor(L/2) is wrong. At depth three G138 gives v_3(0)=1-c_1: words with the same c_0 but different c_1 have different depth-three cells. At even depth four the determining prefix has two symbols, as v_4(0)=c_0*c_1. Thus the count uses the actual growing window, not a fixed-depth entropy limit or an omitted endpoint. The bound is compatible with a dense countable exceptional set and unbounded radii from G154.

**Scope.** This counts hypothetical finite-tail rows within the Rudin–Shapiro family. It excludes neither the original word nor any specified shift and gives no full right extension. The necessary count is linear, not positive entropy. A spatial invariant forcing N_(X_r) to be zero is still missing; another prefix census cannot establish that invariant. No prize conclusion.

*Second reader's note on G155 (Local, 2026-10-07; chat L113).* Correct. The determining window is the one from my G140
note: depth $j$ at time 0 needs the wall-neighbour column at times 0 to $j - 1$, whose even times carry
$\lceil j/2 \rceil$ visible letters, so two words sharing $\lceil L/2 \rceil$ letters share the row through depth $L$.
Two finite rows that agree through $L$ and vanish beyond it are equal, and injectivity of $\Phi$ finishes. The two-block
coverage holds because the fixed word is tiled by level-$m$ blocks of length $h \ge k$, so a factor of length $k$ lies
in two consecutive blocks and is fixed by the pair and an offset. The lower bound uses the radius clock, and the
depth-three endpoint check is right. Checked (`rule30_audit_g99_g100.py`, S49): on 60 random words, for $L$ up to 40,
changing any letter from position $\lceil L/2 \rceil$ on leaves depths 1 to $L$ unchanged, while changing letter
$\lceil L/2 \rceil - 1$ changes depth $L$ when $L$ is odd. Depth 3 is $1 - c_1$ and depth 4 is $c_0 c_1$, and on
$2^{18}$ letters of $r$ the factor counts obey $P(k) \le 16h < 32k$ for $k \le 64$. Descriptive: those counts equal
$8k - 8$ at every tested $k$ from 8 to 64, the value I recall from the automatic-sequences literature for Rudin–Shapiro
(not re-read here). If that value holds, the exception count is at most $8 \lceil L/2 \rceil - 8$ once
$\lceil L/2 \rceil \ge 8$.

**Source-checked refinement (GPT GC184; Local L114 checks the transfer).** Allouche and Shallit1993, Theorem1, gives P_r(k)=8k-8 for k>=8 for the exact substitution and binary coding used here. Consequently N_(X_r)(L)<=8*ceil(L/2)-8 for L>=15. For k=ceil(L/2)=1..7 use2,4,8,16,24,36,46 instead; the affine formula is not asserted below8. The published base enumeration is accepted, not independently rerun. See PRIOR-ART.md for the primary source and scope. This changes only the upper constant, not existence or the zero-or-linear dichotomy.

### G.GPT156. temporal rotation classes sharpen the fixed-period edge-history bound (second-read by Local, 2026-10-07)

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

### G.GPT157. odd factors do not enlarge the rooted edge-history tree (second-read by Local, 2026-10-07)

### G157. Odd factors do not enlarge the rooted edge-history tree (2026-10-07)

**Statement.** Let P>=1 and Q=2^v, where v is the exponent of two dividing P. The common-period-P rooted tree of G7 is isomorphic to the common-period-Q tree: repeat each Q-bit temporal word P/Q times. This preserves depth, the predecessor B, zero hits and temporal rotation classes. In particular its maximum prefix length K is identical, and G156 sharpens to

```math
K+1\le N_4(Q)=\frac1Q\sum_{d\mid Q}\varphi(d)4^{Q/d}.
```

Every odd P has exact maximum K=3; every P with v=1 has exact maximum K=8. These are finite-tree statements, not a bound on physical transient lengths.

**Proof.** A child c of the adjacent pair (a,b) obeys

```math
c(t+1)=a(t)\oplus\bigl(b(t)\vee c(t)\bigr).
```

Suppose a and b have a common dyadic period d. If b has a one, a reset at t0 fixes c(t0+1)=a(t0) XOR1 independently of c(t0). The same reset occurs at t0+d, so c agrees with its d-shift immediately after the reset and thereafter by the recurrence. For any integer t choose an earlier reset; hence the entire periodic word c has period d. If b is zero, summing d steps gives c(t+d)=c(t) XOR sigma, where sigma is the parity of one d-block of a; in particular c has period 2d. Starting from the constant root, induction makes every profile's least period a power of two. Each profile is also P-periodic, so its least period divides P and therefore divides Q.

Restrict every profile to its first Q letters. Since all have period Q, restriction commutes with shift, OR, XOR and B. Conversely repetition embeds any Q-periodic rooted history in the P-periodic tree. The two maps are inverse on every node and edge, and a rotation by t on either side depends only on t modulo Q. Thus the entire rooted trees and their rotation quotients agree. Apply G156 at Q. Its literal Q=1 and Q=2 controls supply the asserted exact maxima. Square.

**Controls and identified unexpected check (symbolic, no run).** Local L114's P=3,5,7 maxima3 and P=6 maximum8 follow exactly, rather than merely fitting a pattern. At P=6 the necklace upper bound drops from700 to10; excluding the known nonabsorbing class gives exact K=8. The rooted hypothesis is essential: the ambient period-three pair (0,100), with the cyclic word written in temporal order, has least pair period3 and cannot be reduced to Q=1. It is excluded by the rooted induction, not by an assertion that all periodic B-states are dyadic. This is the unexpected scope guard.

**Prior art and limits.** This is an explicit finite-tree corollary of the reset/integration mechanism in Nersissian, section4, Theorems10-12 (read directly); that source attributes dyadic diagonal periods to Jen. No novelty is claimed for period doubling or the reset proof. The source's initialized physical tails do not alone establish equality of our arbitrary-phase rooted trees, so the two-sided periodic argument above supplies that transfer. This does not identify maximum K at Q>=4, control actual settling times, establish an upper period-growth law, or solve a prize problem. No computational experiment was launched.

*Second reader's note on G157 (Local, 2026-10-07; chat L115).* Correct. The two-sided reset argument holds on the cyclic
group: when $b$ has a one, the same reset recurs every $d$ steps, so $c$ agrees with its $d$-shift after every reset,
and every time is preceded by one. When $b = 0$, integration over a block gives $c(t+d) = c(t) \oplus \sigma$. From the
constant root, induction keeps every least period a power of two, which divides $P$ and so divides $Q$. Restriction to
$Q$ letters commutes with the shift, OR, XOR and $B$, and repetition inverts it, so the trees and their rotation
quotients coincide. Checked (`rule30_audit_g99_g100.py`, S51) for every $P \le 15$, building each rooted tree from its
children: every profile has a dyadic least period dividing $Q$, restriction maps the $P$-tree's nodes bijectively onto
the $Q$-tree's with depths kept, and the longest $K$ is that of $Q$. By-product, not claimed by G157:
$K = 3, 8, 29, 400$ for $Q = 1, 2, 4, 8$, the last from a tree of 3,065 nodes. A first draft also built $P = 16$; it ran
past ten minutes and was stopped, nothing concluded.
*Correction (Local, 2026-10-07, chat L119).* The heights $3, 8, 29, 400$ given above as a by-product were already
in the record as G2.3's common-period doubling points, and G2.3 also certifies the first genuine branch at diagonal
53,208; the by-product reproduces it and is not new.

### G.GPT158. only even-parity integration branches the temporal-rotation quotient (second-read by Local, 2026-10-07)

### G158. Only even-parity integration branches the temporal-rotation quotient (2026-10-07)

**Statement.** Quotient G7's common-period-P rooted tree by simultaneous temporal rotation of each adjacent pair. It remains a finite rooted tree. At a node represented by (a,b), its number of child classes is classified as follows:

- If b is nonzero, there is exactly one child class.
- If b=0, write q for the least period of a and sigma for the parity of one q-block. The two words cannot both be zero. For sigma=0 there are exactly two child classes, both of least word period q.
- For sigma=1 and 2q dividing P, there is exactly one child class: the two literal children, of least period2q, differ by a rotation through q.
- For sigma=1 and 2q not dividing P, there are no children.

By G157, q is dyadic and divides Q=2^v2(P), so the final case means q=Q. Thus genuine branching in the quotient occurs precisely at even-parity zero-driver nodes; leaves occur precisely when odd-parity integration would exceed the allowed dyadic period. In particular, if E counts the even-parity zero-driver node classes and L counts leaf classes, then L=E+1. Period doubling itself supplies no new branch choice after phase quotienting.

**Proof.** Rotation commutes with B. Every node orbit has a unique predecessor orbit. Distinct depths cannot coincide by G156's first-zero-hit argument; no reconvergence is possible because predecessors are unique. The root is rotation invariant. Hence the quotient is a finite rooted tree. To find its children, rotate any child so that its parent is a chosen representative. Two representative children give the same orbit exactly when a rotation preserving that parent exchanges them.

An active driver b resets the scalar recurrence, as in G157: one complete driver period determines the unique periodic solution c. It has period dividing a common period of a and b, hence divides P. There is one child, before as well as after quotienting.

For b=0 the equation is c(t+1) XOR c(t)=a(t). Choosing c(0) gives exactly two complementary solutions. Summing q steps gives c(t+q)=c(t) XOR sigma. If sigma=0, both solutions are q-periodic. Their least periods are exactly q: any period of c is a period of its difference a, so it must be divisible by q. If sigma=1, their least periods are exactly2q for the same reason, and their q-shifts are their complements. Such solutions close at period P if and only if2q divides P.

Finally the stabilizer of (a,0) consists precisely of shifts divisible by q. For sigma=0 those shifts fix each child and cannot exchange the complementary solutions; for sigma=1 a shift by q exchanges them. This proves the child-class counts. A finite rooted tree with outdegrees0,1,2 has L=E+1 by counting edges in two ways. Square.

**Symbolic controls and identified unexpected check.** At P=1, the three G156 nodes form one chain and the last node (1,0) is the excluded-doubling leaf. At P=2, a nonzero word of least period1 has odd block parity, and a binary word of least period2 is01 or10, also odd. There are therefore no even-parity branch nodes; the quotient is one chain, with its eight nodes given by G156. The apparent first doubling is two phase copies of one continuation.

The unexpected even-parity guard is a=0110, of least period4: with b=0 its solutions are c=0010 and1101. Their child pairs are not rotation equivalent, because any rotation fixing the parent a is a multiple of4. This is a local transition check, not a claim that this parent lies in the rooted tree. By contrast a=01 integrates to0011 and1100, exchanged by rotation through2. Confusing these two parity cases would erase actual possible quotient branching.

**Prior art and scope.** The scalar reset/integration classification is the existing mechanism of Nersissian section4, Theorems10-12, and G7. The additional statement here classifies child orbits using the parent stabilizer; the record's G152 spatial quotient is different and need not be a tree. G157 is a pending proof dependency for the dyadic leaf identification, while the child-orbit calculation above holds without that dependency whenever a is periodic. No novelty is claimed for reset, integration or elementary tree counting. No new computation, larger graph census, uniform bound on E, period-growth upper bound, physical settling bound or prize solution is asserted.

*Second reader's note on G158 (Local, 2026-10-07; chat L115).* Correct. A rotation taking one child $(0, c_1)$ to
another $(0, c_2)$ must fix the parent, since $B$ commutes with rotation and both children map to $(a, 0)$. So the
relevant rotations are the shifts by multiples of $q$. They fix each $q$-periodic solution when $\sigma = 0$, and
exchange the two complementary solutions when $\sigma = 1$. The leaf count $L = E + 1$ is edge counting in a tree with
outdegrees at most 2. Checked (`rule30_audit_g99_g100.py`, S52): on the rooted trees for $P \le 15$, every node's
child-class count follows the rule, leaves exceed branch classes by one, and $P = 1, 2$ are chains. Because those trees
turned out to contain no even-parity branch at all, the rule was also checked ambiently at every pair of $P$-periodic
words for $P \le 8$, including 236 pairs with two child classes. The two local guards check in time order.

### G.GPT159. genuine quotient branches are separated by at least seven depths (second-read by Local, 2026-10-07)

### G159. Genuine quotient branches are separated by at least seven depths (2026-10-07)

**Statement.** On any rooted periodic edge history, two consecutive even-parity zero-driver branch nodes of G158 have depth difference at least7. Consequently the number of temporal-rotation classes at depth n in the common-period-P tree is at most2^ceil(n/7). This is a branch-choice rate bound, not an upper bound on the height of the tree or on physical waiting times.

**Proof.** At an even-parity branch write the profiles starting at its zero driver as0,c,d,e,f,g,h. The previous profile a is nonzero and satisfies Delta c=a, so c is nonconstant. The equation for d is S d=c OR d. A one in the periodic c resets d to1; thereafter1 persists. Periodicity therefore forces d=1. Next S e=1 XOR c, so e is nonconstant. If f=0, its equation S f=1 XOR(e OR f) would force e=1, impossible. Thus profiles c,d,e,f are all nonzero.

If g=0 then its equation forces e=f. Substituting in the equation for f gives S e=1 XOR e, so e and c are alternating and a=Delta c=1. But the constant-one profile has least period1 and odd block parity; it cannot be the even-parity branch under consideration. Hence g is nonzero.

If h=0 then f=g, and the equation for g gives e=f XOR S f. The equation for f is S f=1 XOR(e OR f). At any time with f=0 these two identities imply S f=1 XOR S f, a contradiction. Thus f must be constant1; then its equation would give S f=0, another contradiction. Hence h is nonzero. No zero-driver node occurs in the next six depths, proving the spacing claim.

A path from the root to depth n crosses at mostceil(n/7) binary branch nodes. By G158 all other nodes have at most one child in the rotation quotient. The binary decision words for distinct depth-n nodes are prefix-free (a proper prefix would give the same path until one node already ended at depth n). A prefix-free collection with maximum word length m has at most2^m members, by extending its words to disjoint sets of m-bit strings. Take m=ceil(n/7). The case n=0 has the single root. Square.

**Controls and identified unexpected check (symbolic, no run).** The constant-one predecessor is essential: odd-parity integration gives an alternating c, and the resulting segment0,c,1,c,c,0 has zero drivers only5 depths apart. This is exactly the period-two control and rejects extending the seven-depth claim to all zero drivers. The even-parity local guard a=0110 from G158 is nonconstant and does not trigger that exception. No claim of attainment at distance7 is made. A tree consisting entirely of unary nodes can have arbitrary height while obeying the depth-n count1; this is the unexpected inference guard against converting a branch-rate bound into a settling bound.

**Prior art and dependencies.** The calculation uses G7's recurrence and the pending G158 quotient classification; the six-step exclusion is proved directly here. Existing reset/integration prior art and G156-G158 are the relevant records. No computation or literature novelty claim is made. The number and location of later branch nodes, dyadic-period record spacing and adaptive physical waiting budgets remain open.

*Second reader's note on G159 (Local, 2026-10-07; chat L115).* Correct. After an even-parity zero driver, $c$ is
nonconstant; $d$ is forced to the constant one by the persistent reset; and $e$ is nonconstant. $f = 0$ would make $e$
constant. $g = 0$ forces $e = f$ and then an alternating $c$, so $a = 1$ with odd parity, which is excluded. $h = 0$
gives $e = f \oplus Sf$, which at any zero of $f$ contradicts $f$'s own equation. The width bound is the prefix-free
count. A finding that changes how much any check here can say: on the rooted trees for every $P \le 15$ there is no
even-parity branch node, each rotation quotient is a single chain, and the spacing claim is vacuous there. So S53
(`rule30_audit_g99_g100.py`) also tests the lemma ambiently: below every nonzero even-parity $a$ with zero driver, for
$P \le 8$, all 2,736 continuations keep nonzero drivers for six depths. On the rooted trees it confirms at most
$2^{\lceil n/7 \rceil}$ classes per depth, which is trivially 1.

### G.GPT160. a closed arrival-phase gate removes only transient front states (second-read by Local, 2026-10-07)

### G160. A closed arrival-phase gate removes only transient front states (2026-10-07)

**Statement.** Use G8's common-period-P full-line reset-front graph, excluding the zero word-pair. For a state (a,b,r), define the gate by

- if a is nonzero: a(r-1)=1;
- if a=0: (S b XOR b)(r-1)=1.

Indices are modulo P. The gate is forward invariant. Every nonzero compatible front path is in it after at most two edges. The rooted front starts at the exceptional pair (0,1) and enters the gate after one edge. Every compatible phase-augmented cycle lies entirely inside the gate.

**Proof.** An edge goes to (b,c,r'), with S c=a XOR(b OR c). If b is nonzero, r'=r+delta(b,r) is exactly one time past the first black b cell at or after arrival. Thus b(r'-1)=1 and the child is in the first part of the gate regardless of the parent's phase.

If b=0, delta=0 and r'=r. The child obeys S c XOR c=a. Since (a,b) is not the zero pair, a is nonzero and c is nonconstant. A gated parent has a(r-1)=1, so the child's second gate condition holds. This proves invariance. From any ungated state an active b enters immediately. If b=0, its child has nonconstant driver c, so the following edge enters immediately. No nonzero pair has the zero pair as a child, by the same recurrence. Hence two edges suffice. The root has constant-one driver and cost1, giving the gated child (1,1). On a cycle every state has at least two preceding edges on the same cycle; the two-edge entry assertion puts every state inside the gate. Square.

**Phase counts and certificate transfer.** For a fixed pair of common period P, the gate allows exactly the number of black bits in a when a is nonzero, or the number of transitions in b when a=0. On its relative-phase fiber of size q, use the corresponding counts in q letters. This is an exact local restriction, not a census of reachable states. If a phase-sensitive potential on the gated graph bounds interval debt at slope gamma>=0 by H, the whole nonzero graph has the bound H+2P: discard at most two initial edges, each of cost at most P, and apply the gated certificate to the rest. For the rooted front, the initial cost is1, giving H+1 instead. Intervals wholly inside the discarded part obey the same conservative bound. These are full-line front statements; birth clamps and sublinear period growth remain separate obligations.

**Controls and identified unexpected check (symbolic, no run).** The root (0,1) itself fails the second gate condition because a constant word has no transitions; its first child satisfies the first condition. The derivative condition at a=0 is essential, as the period-two integrated children have zero first coordinate yet valid arrival phases.

The two-step threshold is needed on the unrestricted graph. In temporal order take a=0101, b=0000, r=1 at period4. Integration gives c=0011. The parent fails a(0)=1, and the child (0,c,1) still fails Delta c(0)=1. Its active c then enters on the next edge. This checks a local compatible path, not root reachability. The identified unexpected cycle guard is that every cycle already lies in the gate: G8's compatible slope-2 obstruction survives unchanged. Gate pruning cannot improve cycle means or cure that obstruction; it removes transient arrival phases only.

**Record and scope.** This is a direct finite-graph consequence of G8's reviewed next-black arrival rule and G7's diagonal recurrence. It does not depend on the pending G157-G159 proofs. No computation or literature novelty claim is made. A uniform gated potential size bound remains unproved; the gate by itself gives neither a settling bound nor a prize result.

*Second reader's note on G160 (Local, 2026-10-07; chat L116).* Correct. With an active driver the arrival lands one past
a black driver cell, so the child is gated whatever the parent's phase. With a zero driver the phase is kept, and the
child's word difference equals the parent's first word, so a gated parent gives a gated child. A nonzero pair never has
the zero pair as a child, so two edges always reach an active driver. Every state on a cycle has two cycle edges before
it and is therefore gated. The transfer charge is at most $P$ per discarded edge, and 1 for the root's edge. Checked
exhaustively (`rule30_audit_g99_g100.py`, S54) on the full-line front graph for every $P \le 7$: the gate is invariant,
every state is gated within two edges, and every state of every cyclic strongly connected component is gated (5,894
cyclic states at $P = 7$). The gated phases of each pair number the black cells of $a$, or the transitions of $b$ when
$a = 0$. GPT's period-four control fails the gate at the parent and at both integrated children, and enters at the next
edge. A muddled first draft of the control's boolean expression was rewritten before the recorded run.

### G.GPT161. one representative path decides the first genuine rooted branch (second-read by Local, 2026-10-07)

### G161. One representative path decides the first genuine rooted branch (2026-10-07)

**Statement.** For a dyadic common-period cap Q, the existence of an even-parity zero-driver node anywhere in the rooted tree can be decided by one representative path, without enumerating its phase copies. Start at (a,b)=(0,1) with least common period q=1. Repeat:

1. If b is nonzero, construct the unique q-periodic child c by resetting at any black b cell and following the scalar recurrence. Replace (a,b) by (b,c); keep q.
2. If b=0 and one q-block of a has even parity, stop: this path is a rooted genuine-branch witness.
3. If b=0 and that parity is odd, then if q=Q stop: no rooted genuine branch exists at this cap. Otherwise integrate a with c(0)=0 over2q letters, repeat a and b to that length, replace the pair by (b,c), and double q.

The procedure terminates. It uses O(Q) working bits apart from a retained witness, and O(sum q_j) bit updates along its visited path; in particular O(QK) for K visited nodes. These are symbolic complexity bounds, not runtime measurements or a claim that K is small.

**Proof.** All rooted pair periods are dyadic by verified G157. If a child pair has a period d, its predecessor B has period d too; therefore the least common period of the parent divides that of the child. Active-driver construction gives a child with period dividing q, so its pair period is exactly q. At a zero driver the pair period is the least period of a. Odd integration gives child period exactly2q, as in G158. The period variable therefore remains exact throughout.

By verified G158 an active-driver node has one child class and an odd-parity integration node has one child class after rotation. Choosing c(0)=0 in the odd case selects one of two representatives of that same class. Every property being tested, including zero driver, least period and block parity, is invariant under temporal rotation. Until an even-parity node is met the entire quotient is a single chain, so the representative path cannot bypass an earlier genuine branch. An even-parity node has two q-periodic child classes and is a witness regardless of the remaining cap. Conversely an odd-parity node at q=Q is a leaf; if the representative chain reaches it with no genuine branch, no other quotient branch exists. Termination follows from G7's finite, nonrepeating rooted tree at cap Q. A reset scan, parity scan or integration costs O(q) with only the current words retained, proving the resource bounds. Square.

**Controls and identified unexpected check (no run).** Local L115's complete trees at Q=1,2,4,8 have no genuine branch and respective heights3,8,29,400. Under that independently checked condition, their total labeled-node counts must be3, 3+2*(8-3)=13, 13+4*(29-8)=97 and97+8*(400-29)=3065: each quotient node at pair period q has q distinct rotations. These identities agree with G8 and L115 and check that phase copies, rather than missing branches, account for those counts. This does not extend the observation to Q=16.

The unexpected choice guard is that selecting c(0)=0 is safe only before the first genuine branch. At an even-parity node the two children are not rotation equivalent, so silently selecting one and continuing would cease to certify the whole tree. The procedure stops and reports that node instead. No Q=16 run was launched; Local's stopped full build remains a recorded limitation, not a negative result.

**Scope.** This is a direct algorithmic corollary of the verified rooted-tree and child-orbit proofs, not a new automaton or phase-independent cost certificate. It supplies a bounded-memory exact alternative to a full phase-copy enumeration for this specific first-branch question. Large height, actual waiting costs, and the uniform potential bound remain unresolved. No literature novelty claim or prize result is asserted.

*Second reader's note on G161 (Local, 2026-10-07; chat L117).* Correct. The period variable stays exact: a parent's
least common period divides its child's, an active driver's child has period dividing $q$, and odd integration doubles
it exactly. Before the first even-parity node the quotient is a single chain (G158), so choosing $c(0) = 0$ only picks a
phase copy. Stopping at an even-parity node is what keeps the certificate complete. The labeled-count identity holds
because the chain at cap $Q$ extends the chain at cap $Q/2$ through its leaf, and every later node has pair period $Q$
and so $Q$ rotations. Checked (`rule30_audit_g99_g100.py`, S55) against S51's complete trees, for $Q = 1, 2, 4, 8$ only.
The single path reports no genuine branch and visits exactly $K = 3, 8, 29, 400$ nodes with non-decreasing periods, and
$N(Q) = 3, 13, 97, 3065$ satisfies the identity. The procedure makes $Q = 16$ inexpensive; it was not run, because GC190
asked for no new job.

### G.GPT162. three post-split reset steps cost two adjacent run lengths (second-read by Local, 2026-10-07)

### G162. Three post-split reset steps cost two adjacent run lengths (2026-10-07)

**Statement.** At a genuine even-parity zero-driver node (a,0) of least period q, the complementary integrated children are c and1 XOR c. Let r be the arrival phase and suppose the gate a(r-1)=1 holds. Then r starts a constant run of c. Let ell and m be the lengths of this run and the next one, respectively. For G8's full-line reset front, the unordered pair of elapsed costs over the next three nonzero drivers is

    {ell+2, ell+m+2}.

In particular the worst sibling cost is at most q+2. This bound is attained on the gated compatible domain at every dyadic q>=4, so these three steps do not have a uniform period-independent cost bound. Root reachability of the attaining family is not asserted.

**Proof.** Since Delta c=a is nonzero, c is nonconstant. The next driver d satisfies S d=c OR d; periodicity and a black reset force d=1. The following driver e satisfies S e=1 XOR c, hence e(t)=1 XOR c(t-1). For the complementary child the same reasoning gives drivers1 and1 XOR e. These are exactly the next three drivers on each continuation.

If c(r)=1, the first reset costs1 and reaches r+1; the constant-one driver costs1 more. The first one of e at or after r+2 is at r+ell+1, including the ell=1 endpoint. Its reset therefore finishes at r+ell+2. The complementary child initially has zeros of length ell, so its first reset finishes at r+ell+1, and its constant-one reset at r+ell+2. Its third driver is c(t-1); the next c-one starts after the following zero run of length m. That reset finishes at r+ell+m+2. When c(r)=0 interchange the two children. Subtract the initial r to obtain the formula. Adjacent runs occupy at most one period, so ell+m<=q.

For sharpness take c to have one black cell at q-1 and zeros elsewhere, with r=0. Then ell=q-1 and m=1. Its difference a has black cells only at q-2 and q-1, least period q for q>=4 and even parity. The parent gate holds because a(q-1)=1. Both integrated children close at period q, and the larger three-step cost is q+2. This is an ambient compatible witness, not a rooted one. Square.

**Known rooted control, not a new search.** Local L118 and GPT's backward audit give a=0000110001010011. Choosing c(0)=0 integrates to c=0000010000110001. G160's gate allows phases0,5,6,10,12,15. The respective (ell,m) pairs are(5,1),(1,4),(4,2),(2,3),(3,1),(1,5); therefore the two unordered costs are{7,8},{3,7},{6,8},{4,7},{5,6},{3,8}. The maximum is8. An independent literal reset scan checks all six table entries and the same-order cost18 counterexample, without a continuation search. This certifies only the first three full-line reset steps after the known split; it gives no later cost or actual transient maximum.

**Difference-order guard.** At dyadic q>=8, put a single pulse g at q-1 and take c=Delta g, a=Delta^2 g, r=0. Then c has its two adjacent ones at q-2,q-1, a has two ones at q-3,q-1, the gate holds, and the least periods remain q. Since nu(g)=q, their orders are nu(a)=q-2 and nu(c)=q-1. The cost maximum is again q+2. At q=16 this has exactly the known rooted witness’s orders14 ->15 but cost18 rather than8. It is not asserted rooted. Thus these scalar difference orders do not alone control local reset cost on the gated compatible domain.

**Identified unexpected check and scope.** At ell=1 the third driver is already black at its arrival, so its cost is1, not0: the fast sibling cost is3. The sharp gated single-black-cell family rejects a uniform local three-step slope below3 once q>=8, despite the structural seven-depth branch spacing. A period-dependent potential could still absorb such a finite cost; no uniform potential-size bound is disproved. Existing G2.3, G8, G159 and G160 are the relevant prior records; this is direct run-length accounting, with no novelty claim or new search. Birth clamps, rooted all-branch control and sublinear period growth remain separate obligations.

*Second reader's note on G162 (Local, 2026-10-07; chat L120).* Correct, including the timing GPT asked me to check.
Below the split the three drivers are $c$, the all-ones word forced by the persistent reset, and
$e(t) = 1 \oplus c(t-1)$. The gate makes $r$ a run start of $c$. With $c(r) = 1$ the first two resets end at $r + 2$,
and $e$'s first black cell at or after $r + 2$ is at $r + \ell + 1$; for $\ell = 1$ this is the arrival itself, so the
cost is 1 and the fast total is 3. The sibling waits $\ell$ for its first black cell and then for the whole next run,
giving $\ell + m + 2$. I traced the rooted control's six gated phases by hand from the runs of $c$ (5, 1, 4, 2, 3, 1)
and they give G162's pairs, maximum 8. The two $q + 2$ families check as stated, with orders $q - 2 \to q - 1$ for the
pulse differences. Checked by literal reset arithmetic, independent of the run-length formula
(`rule30_audit_g99_g100.py`, S56). That covers all 4,458 gated even-parity cases for every period $P \le 10$, the rooted
control at period 16, and both families at $q = 4$ to 16 where they apply. GC196's averages also check: over the six
phases the slower sibling averages $22/3$ and both siblings 6.

### G.GPT163. one winding rate controls repeated-strip block debt (second-read by Local, 2026-10-07)

### G163. One winding rate controls repeated-strip block debt (2026-10-07)

**Statement and domain.** Fix a spatially repeated list of m temporal drivers, each periodic with common period P. It may be a compatible Rule30 pair cycle, but the timing statement only uses G8's full-line next-black reset rule. Let F(t) be the integer arrival time after one whole spatial block, starting at integer time t. There is one phase-independent rational rate rho per block such that, for every integer t and n>=0,

    abs(F^n(t)-t-n*rho) <= P-1.

A single orbit of the phase map F modulo P determines rho: if its eventual phase cycle has length d<=P and lift displacement k*P, then rho=k*P/d. All phase cycles have this same rate, even if they do not merge. The per-driver asymptotic slope is rho/m.

At block boundaries, a nonnegative P-periodic integer potential H with

    H(t) >= 2*(F(t)-t)-5*m+H(F(t))

exists if and only if rho<=5*m/2. Whenever it exists, one can choose max H<=2*(P-1), independent of m. This is a whole-block certificate for this fixed repeated strip, not G8's one-edge potential on the entire compatible graph.

**Proof.** A nonzero driver's reset map sends t to one plus its first black time at or after t; a zero driver's map is the identity. Both are nondecreasing and commute with translation by P. Their composition F has both properties. Its phase map is a function on P residues, so every phase orbit eventually cycles. A recurrent lift cycle of length d has displacement k*P; repeating it gives limiting displacement rate k*P/d. If t<=u<=t+P, monotonicity and translation give F^n(t)<=F^n(u)<=F^n(t)+P. Hence any two initial times have the same limiting rate rho, by translating one into that interval and dividing by n. This proves existence, independence and the orbit formula without requiring an invertible phase map.

Fix n>=1 and let D_n(t)=F^n(t)-t. This is P-periodic. For residues t,u with 1<=u-t<=P-1, the previous inequality gives -(u-t)<=D_n(u)-D_n(t)<=P-(u-t). Thus its largest and smallest residue values differ by at most P-1. Write these values M_n and a_n. Iterating F^n in blocks shows j*a_n<=F^(j*n)(t)-t<=j*M_n. Divide by j and let j grow to obtain a_n<=n*rho<=M_n. Every D_n(t) lies in that same interval, giving the claimed P-1 error. The n=0 case is exact.

When rho<=5*m/2, define H(t) as the supremum, over n>=0, of 2*D_n(t)-5*m*n. The n=0 term is0; the error bound makes every term at most2*(P-1). Since these are integers in a bounded interval, the supremum is a finite nonnegative integer, periodic in t. Splitting off the first block gives the potential inequality. Conversely, sum such an inequality over n blocks. A finite periodic H bounds the total reward; dividing by n yields 2*rho-5*m<=0. Equality is allowed: zero-weight recurrent loops do not make the potential infinite. Square.

**Independent existing control.** G8's compatible period4, spatial-length12 witness has F(0)=27 and F(3)=31. Therefore F^n(0)=28*n-1 for n>=1, while F^n(3)=3+28*n; both rates are28 per block, hence slope7/3. The phase-zero first-block slope27/12 is not its asymptotic rate. Its whole-block error from phase0 is1, within P-1=3. No new cycle search was run.

**Identified unexpected check: coalescence is not required.** The all-zero compatible strip gives F(t)=t. Its P phase residues remain separate fixed points, but all have rate0 and H=0. The proof needs weak monotonicity, not invertibility or convergence to one phase. A single pulse at time0 gives a sharp clock-only error control: F(0)=1, F(t)=P+1 for 1<=t<P, and its recurrent rate is P. The error at t=0 is P-1. That single-driver repeated strip is not claimed Rule30-compatible for P>1; it tests the timing lemma's general domain, not a compatible slope obstruction.

**Prior record and limits.** This is the standard monotone degree-one translation-number mechanism, here proved directly on integer times with the discrete P-1 bound. The primary Mathlib translation-number module states phase-independent limits and bounded iterate displacement; no novelty is claimed for rotation theory, and no Lean validation of this application is claimed. G6 already gives phase comparison for a fixed history; G8/G10 already compute exact recurrent phase means. This entry supplies the explicit whole-block potential consequence. It does not prove rho<=5*m/2 for all compatible cycles, charge partial blocks independently of m, bound outward trees or rooted branched paths, include birth clamps, or establish sublinear period growth. Those remain separate obligations before any prize conclusion.

*Second reader's note on G163 (Local, 2026-10-07; chat L121).* Correct; the two points GPT asked about hold. The
displacement sandwich: for residues $1 \le u - t \le P - 1$, monotonicity gives $D_n(u) \ge D_n(t) - (u - t)$, and
translation gives $D_n(u) \le D_n(t) + P - (u - t)$, so the spread of $D_n$ over residues is at most $P - 1$. Splitting
$F^{jn}$ into $j$ blocks of $n$ puts $n\rho$ between the extremes, hence $|F^n(t) - t - n\rho| \le P - 1$. The
potential: with $\rho \le 5m/2$ every term $2D_n(t) - 5mn$ is at most $2(P - 1)$, the supremum is a bounded nonnegative
integer, and shifting the index by one block gives the inequality; summing it gives the converse. The G8 witness
arithmetic ($F^n(0) = 28n - 1$) and the sharp pulse strip both check. Checked (`rule30_audit_g99_g100.py`, S57) on 400
random strips with zero drivers allowed: monotone degree-one maps, one rate per strip over every phase cycle, the
$P - 1$ band for $n \le 60$, and a truncated potential within $2(P - 1)$ that satisfies the block inequality. The pulse
strip's error is exactly $P - 1$ at $P = 2, 5, 8$.

### G.GPT164. one full-line path certifies every interval phase and birth restart (second-read by Local, 2026-10-07)

### G164. One full-line path certifies every interval phase and birth restart (2026-10-07)

**Statement.** Fix a finite list of M temporal drivers with one common period P. Let F_j be G8's full-line reset map, including the identity for a zero driver, and let T_0=0, T_(j+1)=F_j(T_j). For gamma>=1 define the reference path's all-interval debt

    D = max over 0<=a<=b<=M of [T_b-T_a-gamma*(b-a)].

Then for every such interval and every integer starting time u,

    G_(a,b)(u)-u <= gamma*(b-a)+D+P-1,

where G_(a,b)=F_(b-1) composed through F_a. Consequently G9's normalized birth-clamped front, with barriers beta_j<=j, obeys T_birth(k)<=gamma*k+D+P-1 for every k<=M. The statement also holds for every global temporal phase shift of the same driver list. No compatibility or spatial repetition is needed for this transfer; those conditions remain necessary to establish a useful D for the actual Rule30 history.

**Proof.** G_(a,b) is nondecreasing on integer times and commutes with translation by P. Its displacement Q(u)=G_(a,b)(u)-u is P-periodic. For residues u<v with 1<=v-u<=P-1, monotonicity and periodicity give

    -(v-u) <= Q(v)-Q(u) <= P-(v-u).

Hence the spread of Q over every starting residue is at most P-1. At the actual reference arrival T_a its value is T_b-T_a, so any Q(u) is at most T_b-T_a+P-1. The definition of D proves the interval inequality. Apply G9's exact maximum-over-restarts identity to that uniform interval budget and beta_j<=j to obtain the birth bound. A phase shift phi conjugates each reset to F_j(s+phi)-phi, so the shifted interval displacement is the original Q(u+phi); it obeys the same bound. Square.

This uses the displacement-spread argument of G163 for a finite interval composition, not its repeated-block rate. The reference debt must cover all intervals, not just the whole prefix. Comparing two reference prefix bounds separately would introduce 2(P-1); composing the interval directly keeps the overhead to P-1. The common P must cover the whole driver list being certified; it cannot be replaced by a smaller current-driver period without a separate justification.

**Existing finite evidence, not a new run.** G7's recorded phase-zero period16 history through M=53207 has maximum interval debt26.5 at slope5/2. Conditional on that recorded finite calculation, this lemma supplies all-starting-time interval debt at most41.5 on the same history. For every phase and L>=1, its normalized birth-clamped absolute bound is T_birth(k)<=(5/2)*k+41.5 for k<=53207. G9 also gives birth-clamped interval debt at most42.5 for L=1, or41.5+L in general. These are loose universal budget consequences, not new maxima or a sharper final settling time; G2's final-time bounds remain unchanged. The computation is not rerun or newly independently verified here. The history ends at the known genuine split: another continuation requires its own reference-path debt. No all-branch or asymptotic conclusion follows.

**Identified unexpected sharpness/domain control.** A single pulse driver at residue0 has reset displacement1 from reference time0, but displacement P from starting time1. Thus its displacement spread is exactly P-1; the transfer cannot remove that overhead in the generic clock domain. At gamma=1 the one-step reference debt is0 while the starting-time1 debt is P-1. This is not claimed a repeated compatible Rule30 strip. At P=1 the overhead vanishes, including the zero-driver identity. G9's endpoint-only birth counterexample remains consistent: this lemma explicitly adds the period overhead and requires every reference interval. G163's interior-debt counterexample still prevents replacing D by a whole-block rate certificate.

**Scope and remaining obligation.** Direct corollary of reviewed G6/G9/G163 monotone clock maps; no new prior-art or computation claim. The missing research bound is now an all-interval budget on one full-line reference path per admissible branched history, together with the independent period-growth requirement. An arbitrary-period D=O(P) bound is not supplied. Births and phase restarts need no separate search once that reference budget is established. No prize result is claimed.

*Second reader's note on G164 (Local, 2026-10-07; chat L122).* Correct; the two points GPT asked about hold. The
all-interval quantifier is needed and is used correctly. The bound at an interval $[a, b]$ comes from that interval's
own displacement, pinned at the reference arrival $T_a$, so $D$ must cover every reference interval, and composing the
interval map directly keeps the overhead at $P - 1$ rather than $2(P - 1)$. The phase conjugacy holds: a global shift
$\varphi$ turns each reset into $F(s + \varphi) - \varphi$, so the interval displacement is $Q(u + \varphi)$, with the
same spread. The birth bound uses $\beta_j \le j \le \gamma j$, which is where $\gamma \ge 1$ enters. Checked
(`rule30_audit_g99_g100.py`, S58) on 300 random driver lists, $M \le 40$ and $P \le 8$, at $\gamma = 1$ and $5/2$. Every
interval, every start and every phase shift obeys the bound. The birth-clamped front, computed by its own recursion
$f_j = \max(\beta_j, F(f_{j-1}))$ rather than G9's identity, stays below $\gamma k + D + P - 1$ for random barriers. The
single pulse attains the overhead $P - 1$. The period-16 numbers (26.5 and 41.5) rest on G7's recorded computation,
which this review did not rerun.

### G.GPT165. dyadic stage budgets stitch without a logarithmic loss (second-read by Local, 2026-10-07)

### G165. Dyadic stage budgets stitch without a logarithmic loss (2026-10-07)

**Conditional reduction.** Follow one infinite admissible rooted diagonal history. At node k let p_k be the least common temporal period of its adjacent pair, with the root (0,1) at k=0. Use gamma with 1<=gamma<3. Suppose there is one finite constant C>=0 for this history such that, on every maximal constant-period stage q, one full-line reference path has debt at most C*q on every finite subinterval of that stage. Different stages may use different reference arrival phases, but C and gamma must stay uniform along this history.

Then, for a prefix of M edges, every full-line interval and every starting time has debt at most2*(C+1)*p_M. The same bound transfers to normalized birth-clamped absolute timing:

    T_birth(M) <= gamma*M+2*(C+1)*p_M.

It also covers every global temporal phase of this same history. Thus p_M=o(M), together with the assumed stage budget, would supply G2's below-3 sufficient settling bound on this history. To cover every admissible left side, both assumptions must hold separately on every history; history-dependent constants are allowed as in G2. No stage budget or period-growth estimate is proved here.

**Exact stage structure.** The predecessor B commutes with temporal shifts. If a child pair has period q', its predecessor has a period dividing q'. G157's reset/integration rule supplies child common period at most q, or2q at an odd zero-driver integration, when the parent's least period is q. Since rooted periods are dyadic, the child's least period is therefore q or2q, never smaller. A doubling can occur only on a zero-driver edge; that edge has full-line reset cost0. Every edge whose source pair has period q uses a driver with period dividing q, including that final zero edge. Consequently all clock maps within a stage share common period q. Genuine even-parity branches preserve q; they do not start a new period stage.

**Proof of the budget.** Fix any finite interval within the M-edge prefix and split it at period changes. For its part in a q-stage, G164 upgrades the assumed reference all-interval debt C*q to an arbitrary-start debt at most(C+1)*q-1. Each stage is contiguous, so the interval visits each q at most once. The distinct q are powers of2 bounded by p_M. Their sum is at most2*p_M-1. Sum the interval inequalities at their actual arrival times to obtain elapsed <=gamma*(interval length)+2*(C+1)*p_M. This holds for every starting time, so G9's restart identity applies on the finite prefix, giving the stated birth bound. Phase conjugacy preserves the same inequalities. No separate phase sum, per-birth penalty or per-branch allowance occurs. Square.

**Equivalent period-growth checkpoint.** Every infinite rooted history has unbounded p_k: otherwise its path would be infinite in G7's finite rooted tree. Let N_j be the first node of least period2^j, for j>=1. The exact stage structure gives p_k=2^j for N_j<=k<N_(j+1). Hence p_k=o(k) if and only if2^j/N_j tends to0. Necessity evaluates at k=N_j; sufficiency bounds p_k/k by2^j/N_j throughout that stage. This is a reformulation, not an estimate for N_j. A large finite doubling delay does not prove the limiting condition.

**Identified unexpected check: branching is not doubling.** The known split at diagonal53208 has period16 children, as G2.3, G158 and the independent FBR16 replay establish. It is not the first period32 node N_5 and earns no new stage allowance. The known initial stage entries3,8,29,400 do not locate N_5. Nor may one add C*q after every genuine branch at fixed q: the assumed all-interval budget must already cover the selected continuation within that entire stage. The elementary sum1+2+4+8+16=31 checks the strict bound below2*16, but certifies no actual stage debt.

**Scope.** Direct use of G2, G7, G157/G158, G164's interval transfer and G9's birth theorem; elementary geometric summation, with no novelty or new computation claim. G164 was independently verified by Local L122 during this publication; its review and controls are preserved. The hard obligations remain uniform one-reference-path stage debt and superlinear doubling-entry positions on every admissible history. Word-only branch counting, finite doubling records and repeated-strip rates supply neither obligation. No prize conclusion is asserted.

*Second reader's note on G165 (Local, 2026-10-07; chat L123).* Correct as a conditional reduction. The stage structure
holds: since $B$ commutes with shifts, the parent's least period divides the child's, so with G157's reset and
integration rule a child has period $q$ or $2q$ and never less. Doubling happens only on an odd-parity zero-driver edge,
which costs 0, and an even-parity branch keeps $q$. The budget sum holds: within a stage G164 turns the assumed $Cq$
into an arbitrary-start $(C + 1)q - 1$. An interval meets each dyadic stage at most once, and the powers of two up to
$p_M$ sum to less than $2p_M$. The period-growth reformulation is right in both directions. Checked
(`rule30_audit_g99_g100.py`, S59) along the known $Q = 16$ representative path to its first genuine branch (53,208
nodes). The period never decreases and changes only at odd-parity zero drivers, by doubling. Every node's driver has
least period dividing its stage period. The stage entries are $N_1, \ldots, N_4 = 3, 8, 29, 400$ with no period-32 node,
and the branch keeps period 16. Both hypotheses, the uniform stage budget and $2^j/N_j \to 0$, remain unproved, as G165
says.


### G.GPT166. finite-horizon and state-projection guards (second-read by Local, 2026-10-07)

**Exact horizon diagnostic: tight-edge distance, not potential size (2026-10-07; symbolic, review requested).** Consider any finite directed graph with real edge rewards w, no positive-reward cycle, and stopping permitted at every vertex. Let h(v) be its least nonnegative feasible potential, equivalently the maximum reward of any finite walk from v, including the empty walk. G8 already proves finiteness by deleting nonpositive cycles. For an edge v->u set its slack s(v,u)=h(v)-w(v,u)-h(u)>=0. For any at-most-n-edge walk p ending at z, telescoping gives

    h(v)-reward(p)=h(z)+sum of the edge slacks on p.

Therefore h(v)-H_n(v) is exactly the minimum of this terminal potential plus accumulated slack over all such walks. In particular H_n(v)=h(v) if and only if some at-most-n-edge walk consists entirely of tight edges (slack0) and ends at h=0. All summands are nonnegative, so neither implication loses a condition. This also covers h(v)=0 by the empty walk and vertices with no successors.

Such a tight walk always exists: choose a minimum-length walk attaining h(v). An optimum exists among simple paths by cycle deletion. Its endpoint must have h=0, since otherwise a positive optimal continuation increases the reward; then the telescoping identity forces every traversed edge to be tight. Let d(v) be the shortest tight-edge distance to the zero-potential set. The first globally stable Bellman horizon is exactly max_v d(v): equality H_n=h is equivalent to n>=max d; and any equality H_(n+1)=H_n makes H_n a feasible potential, hence the least potential because H_n<=h. The shortest tight path is simple, so d(v)<=|V|-1. This is a finite graph bound, exponential rather than linear in q for the aligned pair domain; it supplies no all-period Rule30 budget.

**Identified unexpected check: allowed numerical weights do not control horizon.** On a directed chain take2L+1 edges with rewards(-1,+1) repeated L times, followed by+1, for L>=1. These weights have the exact numerical reset form2*delta-5 with delta2 or3. Every even-index vertex before the final leaf has h=1, every odd-index vertex has h=2, and the leaf has h=0. Every edge is tight. Thus max h=2 while the initial vertex has d=2L+1: all earlier even prefixes have reward0 and odd prefixes reward-1. No positive cycle exists. This refutes a generic inference from bounded potential size to bounded horizon, even with bounded positive reset delays and odd integer rewards. It is an abstract chain, not a claimed compatible or rooted Rule30 history. The zero leaf and empty-stop conventions are essential controls, and no computation was run.

**Application and next question.** HG4 failure concerns the tight-route length in the full gated graph. It does not by itself refute a potential magnitude O(q). Local's descriptive85, if its fixed-point computation is correct, means max d=85 in that finite q8 domain; this is an interpretation, not an independent global audit. A future horizon proof needs a compatibility theorem on tight paths, while the actual stage goal can instead bound h directly without a short-horizon theorem. This isolates two obligations that should not be conflated. No new universal bound, rooted counterexample or prize result follows. The reweighting/telescoping mechanism is standard shortest-path potential theory; see PRIOR-ART.md, not a novelty claim.


**Direct-potential restriction: the current driver and phase are insufficient (2026-10-07; symbolic, review requested).** At any dyadic q>=4, let b have its sole black bit at time q-1, let a=S b XOR b, and take arrival phase0. Then c=b is a valid child of(a,b), because S b=a XOR(b OR b). Both source(a,b,0) and target(b,b,0) satisfy G160's gate: a(q-1)=1 and b(q-1)=1. The source reset costs q, so the clock returns to phase0 and the edge reward at slope gamma is q-gamma.

Suppose a proposed finite potential has the form f(b,r), depending on the whole current driver b and relative phase r but forgetting the preceding word a. Its edge inequality here becomes

    f(b,0) >= q-gamma+f(b,0).

This is impossible when gamma<q. In particular no such potential can certify slope5/2 on the full gated q-domain for any dyadic q>=4. More generally a fixed finite gamma cannot be certified on all dyadic periods by this restricted family. The argument permits arbitrary dependence on q and arbitrary finite potential magnitude: changing constants, density, run lengths, difference orders or even retaining the whole b cannot rescue the family if a is discarded. This is a restriction on the potential's information, not a refutation of G8's two-word-and-phase potentials or G165's desired bound. Root reachability of these sources is not asserted.

**Identified unexpected check: the projected loop is not an actual repeatable cycle.** The target(b,b) has unique period-q child0: a black b resets c to0 and all intervening white times preserve c. Thus the actual next target is(b,0), not another copy of(b,b). The second reset also costs q, and the next zero-driver reset costs0. Forgetting a creates a positive self-loop in the projected driver graph from a valid edge, while the actual pair graph has no such self-loop here. Repeating that projected loop is invalid. The actual two-edge cost2q is a finite period-scale charge, consistent with an O(q) pair potential. At q4 the source is(12,8), its target(8,8), and then(8,0): both delays4 and rewards3, agreeing with HG4's known H0 rejection and G10's maximum6. At q2 the edge reward at slope5/2 is negative, so this specific obstruction does not apply; the dyadic q>=4 condition matters. No numerical run or new cycle census was used.

**Prior record and next intention.** G7's scalar compatibility/reset rule and G160's gate supply the calculation; G8 already keeps both words. This sharpens the earlier phase-loss guard by showing that preserving phase while discarding the preceding word also fails on the ambient gated domain. It is elementary state-projection reasoning, with no novelty claim. Next candidate charges must retain preceding-word information or explicitly exploit a proved rooted restriction. No claim is made that the rooted domain contains this family, and no additional Local computation is requested.


**G8 phase-free obstruction survives the arrival gate (2026-10-07; symbolic scope audit, review requested).** G8.2 already rejects a phase-free two-word potential on the full compatible domain at every slope gamma<3. It is not a new cycle discovery. The remaining scope question is whether G160's gate removes the individually maximizing phases used in that proof. It does not. For G8's cyclic list of period4 words the following exact table supplies a gated maximum-delay phase on each edge; a is the preceding cyclic word and b the listed driver. Time bits are least-significant first.

| b | a | arrival r | a(r-1) | delta(b,r) |
|---|---|---|---|---|
|9|13|1|1|3|
|8|9|0|1|4|
|14|8|0|1|2|
|12|14|0|1|3|
|4|12|3|1|4|
|7|4|3|1|2|
|6|7|3|1|3|
|2|6|2|1|4|
|11|2|2|1|2|
|3|11|2|1|3|
|1|3|1|1|4|
|13|1|1|1|2|

Each source is gated, each triple is the existing compatible G8 triple, and each target is gated by G160 closure. A finite phase-free g(a,b) that satisfies the edge inequalities for all gated states must satisfy each independently chosen row. Summing cancels the cyclic pair potentials and gives36<=12*gamma. Hence gamma>=3 remains necessary even on the gated domain, at dyadic q4. The existing phase-sensitive q4 certificate at gamma5/2 is consistent with this distinction.

**Identified unexpected check and counterfactual.** The selected phases need not concatenate into one physical front. Their use is valid precisely because g forgets phase and must satisfy all gated instances separately. Claiming a real36-step compatible clock cycle would be false: G8's coherent recurrent circuit has elapsed28. If even one of the displayed maximizing phases were excluded by the gate, the old unrestricted proof could not simply be imported; all twelve gate bits have instead been checked explicitly. No new computation was run. This is an exact scope extension of G8, using G160, not a new general potential theorem.

**Working restriction after the two projection guards.** On the full gated domain, neither discarding a while retaining(b,r), nor discarding r while retaining(a,b), can support the desired below3 certificate. These facts do not prove that every successful statistic must store the full pair and phase; other compressions or a rooted-only restriction remain possible. The next direct-charge argument must preserve the distinction each proposed compression erases, rather than transfer an unrestricted graph result without checking its gate. No rooted debt lower bound or prize conclusion is claimed.



*Second reader's note on G166 (Local L127, 2026-10-07).* The tight-edge distance identity and both projection obstructions are correct. S60 checks equality of tight distance and stabilization at horizons4,21,85 for q4,6,8 and the abstract chain controls. S61 checks all twelve gated phases and the compatible q4 cycle. The audit initially imported HG4's module-level CPU limit and lost later output; Local moved the limit to main() and repeated the audit. The corrected complete audit passes; the earlier incomplete run is not a pass.

### G.GPT167. complete branch blocks and partial interval costs (second-read by Local, 2026-10-07)

### GPT G167 — complete branch blocks and partial interval costs (RULE30-GPT.md G167; awaiting second reader, 2026-10-07)

**Bounded symbolic result, independent review requested.** Include G162's zero-driver branch edge(a,0)->(0,c), then the three nonzero-driver edges whose elapsed cost is either ell+2 or ell+m+2. Here r is gated, ell and m are the first two constant-run lengths of c, and ell+m<=q. The zero-driver edge costs0. At slope5/2 the total doubled reward of this four-edge block is therefore one of

    2*ell-16, 2*(ell+m)-16.

The worst endpoint reward is at most2q-16. Thus every such block at dyadic q<=8 has nonpositive endpoint reward. This is an ambient gated statement, not a rootedness assertion. At larger periods the upper bound can be positive. G162's pulse attaining family makes the larger reward2q-16 sharp. G159's seven-depth separation ensures these four-edge blocks around distinct genuine branches do not overlap, but supplies no bound on the remaining edges.

**Exact partial-prefix audit.** On the fast sibling c(r)=1, the four reset delays are0,1,1,ell. Its prefix doubled rewards, after0 through4 edges, are

    0, -5, -8, -11, 2*ell-16.

On the slow sibling c(r)=0, the delays are0,ell+1,1,m. The rewards are

    0, -5, 2*ell-8, 2*ell-11, 2*(ell+m)-16.

These follow directly from G162's literal reset arithmetic, including the m=1/ell=1 endpoint cases. Consequently the largest reward of a prefix anchored before the free zero edge is the maximum of0,2*ell-8,2*(ell+m)-16 across the two siblings. It is at most max(0,2q-10), since a nonconstant c has ell<=q-1. This says nothing about an interval that begins after the free edge.

**Known rooted control, not a new run.** G162's six allowed phases at the recorded q16 split have(ell,m)=(5,1),(1,4),(4,2),(2,3),(3,1),(1,5). Hence every whole four-edge branch block there has doubled reward at most-4, while the largest branch-anchored prefix reward across phases and siblings is2 (debt1). This is arithmetic on the existing table, not a continuation search or a uniform q16 theorem. No actual birth-clamped settling estimate is imported.

**Identified unexpected check/counterfactual: endpoint payment does not pay arbitrary intervals.** At q8 choose the valid G162 gated pulse family with ell=7,m=1. The slow sibling's whole four-edge reward is0, but its two-edge prefix reward is6 (debt3). If an interval starts immediately after the free edge, its very next reset costs8 and has reward11 (debt5.5). These are actual compatible local blocks from G162, unlike the generic clock schedules of G163's addendum; rooted membership is not claimed. They refute treating nonpositive block endpoints as a certificate for every prefix or subinterval.

**What moves and what remains.** The free zero edge is an exact part of the local branch charge and should not be discarded when charging complete branch blocks. Negative complete blocks can be recognized without charging a fresh period budget per branch. However interior endpoint effects and the intervening nonbranch edges still need control, especially at larger q. Removing blocks does not create a new compatible history, so no bound may be applied to the compressed word sequence without a separate argument. G165's uniform all-interval stage obligation remains unproved. This is a symbolic corollary of G162 and G159, not a new general amortized theorem or prize claim; no computation was run.

*Second reader's note on G167 (Local, 2026-10-07; chat L128).* Correct. With the free zero edge included, the four-edge
block costs $\ell + 2$ or $\ell + m + 2$. Its doubled slope-5/2 reward is therefore $2\ell - 16$ or $2(\ell + m) - 16$,
at most $2q - 16$ and sharp in the pulse family. The per-sibling delays are $0, 1, 1, \ell$ (fast) and
$0, \ell + 1, 1, m$ (slow), which give the stated prefix rewards. So the anchored prefix maximum is at most
$\max(0, 2q - 10)$. The rooted $q = 16$ arithmetic gives block maximum $-4$ and prefix maximum 2, and the $q = 8$
counterexample gives 0, 6 and 11 as stated. Checked by literal reset arithmetic (`rule30_audit_g99_g100.py`, S62) on all
8,916 gated even-parity sibling cases for $P \le 10$, plus the rooted arithmetic and the $q = 8$ case.

### G.GPT168. lift contracted branch charges with one reserve (second-read by Local, 2026-10-07)

### GPT G168 — lift contracted branch charges with one reserve (RULE30-GPT.md G168; awaiting second reader, 2026-10-07)

**Conditional finite-history statement; review requested.** Fix one finite gated periodic history and disjoint four-edge branch blocks from G167, all at common period q. Keep every other edge unchanged and replace each complete branch block by one edge between its actual endpoints, with reward equal to the sum of its four original rewards. These contracted edges represent actual blocks; the compressed sequence is not asserted to be a new Rule30 history. Suppose a nonnegative potential K on the retained vertices satisfies every contracted edge inequality, with original doubled slope5/2 rewards.

Let A bound the positive reward of every prefix starting at a branch block's first vertex, allowing an empty prefix. Let B bound the positive reward of every contiguous subinterval inside any one block. Both are nonnegative and uniform across the blocks. Then K lifts to a nonnegative potential h on every original vertex, satisfying every original edge inequality, with

    max h <= max K+A+B.

Thus the interior cost is one reserve for the whole fixed-period history, not A or B multiplied by the number of branches. This is conditional on a certificate K for all retained ordinary edges and complete blocks; no such uniform certificate is supplied here.

**Proof.** Give every retained vertex h=K+A. Inside a block, define h backwards from that fixed endpoint by h(v)=max(0,w(v,u)+h(u)). This is possible on a finite block and verifies all its interior edge inequalities. Expanded at an internal vertex, h is the maximum of rewards from stopping at an interior vertex and the remaining-block reward plus the endpoint's K+A. The first terms are at most B and the last is at most B+max K+A. At the block's first vertex the backwards-required value is the maximum of prefix stopping rewards, at most A, and whole-block reward plus K(endpoint)+A, at most K(start)+A by the contracted inequality. Hence the assigned h at the first vertex also covers its first original edge. Ordinary edges retain their inequalities because the same A is added at both ends. Nonnegativity and the stated uniform upper bound follow. Adjacent blocks would also work if they share only a retained endpoint; G159's spacing guarantees disjoint blocks on the rooted histories under discussion. No new compatibility after contraction is assumed. Square.

**Exact G167 reserves.** Its fast block rewards are(-5,-3,-3,2ell-5); its slow block rewards are(-5,2ell-3,-3,2m-5). With ell+m<=q and ell,m>=1, G167 supplies A=max(0,2q-10). Every single positive edge is at most2q-5; every two-edge interval is smaller than this, and every three-edge interval is at most2q-11, while the four-edge reward is at most2q-16. Thus B=max(0,2q-5) suffices. The lifted overhead is at most4q-15 for q>=8 (and3 for q4), independent of the number of genuine branches. On the known q16 split's table, the sharper reserves A=2 and B=7 give overhead9 for those local blocks only. This is not a bound on later q16 branch blocks.

**Identified unexpected control and counterfactual.** The q8 slow pulse block has rewards(-5,11,-3,-3), total0. With K=0 at its two contracted endpoints, naive lifting with no reserve fails at the first endpoint because its two-edge prefix earns6. With A=6 the backwards construction gives original vertex values(6,11,0,3,6); every edge inequality holds and the zero stopping option is active at the middle vertex. The general bound max K+A+B=17 safely covers these values. Using a whole-block endpoint inequality alone would miss that middle stop; repeating the block does not require adding6 per repetition. This is exact arithmetic on the existing compatible block, with no new computation or root-membership claim.

**Scope and next obligation.** This is standard finite-path dynamic programming, already present in G8/G166, now applied to G167's actual branch blocks. It resolves how a contracted certificate would transfer to arbitrary subintervals without a per-branch reserve. It does not construct K, bound intervening nonbranch charges, solve the all-period cycle problem, or establish period growth. For multiple dyadic stages, any eventual O(q) certificate must still be stitched as in G165/G166. No prize conclusion or new run is claimed. Next reasoning target is K on the retained ordinary edges and genuine branch transitions, rather than accumulating a fresh allowance for each branch.

*Second reader's note on G168 (Local, 2026-10-07; chat L130).* Correct. With $h = K + A$ at retained vertices and the
backward fill inside each block, the value required at a block's first vertex is the larger of a prefix reward, at most
$A$, and the block reward plus the endpoint's value. The contracted inequality covers the second. Interior values are a
subinterval reward, at most $B$, or the remaining block plus the endpoint, at most $B + \max K + A$. Since the same $A$
is added at both ends of every retained edge, one reserve serves the whole history. The G167 reserves follow from the
edge rewards $(-5, -3, -3, 2\ell - 5)$ and $(-5, 2\ell - 3, -3, 2m - 5)$: $A = \max(0, 2q - 10)$ and
$B = \max(0, 2q - 5)$. At the known $q = 16$ split these are 2 and 7. Checked (`rule30_audit_g99_g100.py`, S63). The
lifting holds on 500 random paths with disjoint blocks, the least contracted potential lifting with
$\max h \le \max K + A + B$. Both reserves hold over every gated block for $P \le 10$, and the $q = 8$ slow pulse block
lifts to $(6, 11, 0, 3, 6)$.

### G.GPT169. reject a uniform three-distance linear potential (second-read by Local, 2026-10-07)

### GPT G169 — reject a uniform three-distance linear potential (RULE30-GPT.md G169; awaiting second reader, 2026-10-07)

**Exact family restriction; independent review requested.** Use G8's reset distance D(w,r)=delta(w,r), including D(0,r)=0. Consider a potential on the full gated compatible domain of the form

    h_q(a,b,r)=C_q+alpha*D(a,r)+beta*D(b,r)+chi*D(a XOR b,r),

where alpha,beta,chi are fixed real coefficients, shared by every dyadic q>=4. C_q is any finite constant depending only on q. This family retains both words and the clock, but only through three scalar reset distances. No member satisfies every doubled slope5/2 edge inequality for every such q. The proof does not require nonnegative coefficients or nonnegative h; it rejects even this larger algebraic family. C_q cancels on every within-q edge.

**Period4 constraints.** First use the gated edge(12,8,0)->(8,8,0) from G166. It costs4 and has reward3. The three source distances are(3,4,3), and the target distances are(4,4,0). Its inequality requires

    -alpha+3*chi >=3.

Next use the zero-driver edge(9,0,0)->(0,14,0). In time-bit notation14 is(0,1,1,1), its cyclic difference is9=(1,0,0,1), and S14=9 XOR14. Both states are gated:9 at time-1 is1, and14(0) XOR14(-1)=1. The edge costs0 and has reward-5. Its source distances are(1,0,1), and target distances are(0,2,2), so

    alpha-2*beta-chi >=-5.

Adding the two inequalities gives2*(chi-beta)>=-2, hence beta-chi<=1. Every triple and distance here is explicit scalar arithmetic; no enumeration or experiment is used.

**Unbounded-period constraint.** For each dyadic q>=4 let b have its sole black bit at q-1. The gated compatible edge(b,b,0)->(b,0,0) costs q and has reward2q-5. Its source distances are(q,q,0), and target distances are(q,0,q). Thus

    q*(beta-chi) >=2q-5.

As dyadic q tends to infinity this requires beta-chi>=2, contradicting the period4 bound. Square. The same contradiction already follows at any dyadic q>=8, where2-5/q>1. Thus this single uniform formula cannot simultaneously certify q4 and q8; no larger computation is needed.

**Identified unexpected guard: the free edge is decisive.** The zero-driver constraint is not vacuous just because its physical waiting cost is0: its doubled reward is-5, and its child can have reset distance2. Omitting it would remove the upper bound on beta-chi and lose this contradiction. All three witnesses are valid gated edges, but root membership is not asserted. The pulse target's zero child is the unique compatible reset continuation, as already proved in G166. These are not projected cycles or sampled independent clocks.

**Scope and counterfactual.** Coefficients depending on q, a special formula at q4, nonlinear combinations, additional features, and a proved rooted-only domain are outside this rejection. In particular this is not a refutation of an asymptotic O(q) bound with finitely many exceptional periods. The constant C_q cannot help because it cancels; but replacing coefficients at small q genuinely changes the family. G8's phase-sensitive pair potential remains valid at the tested periods. The prior record is G8's certificate inequality, G160's gate and G166's pulse edge; no novelty claim is made for the linear-inequality contradiction. Next charge proposals need a richer compatibility feature than this single shared three-distance formula. No computation or prize conclusion is claimed.

*Second reader's note on G169 (Local, 2026-10-07; chat L131).* Correct. All three witness edges are valid gated
compatible edges. $(12, 8, 0) \to (8, 8, 0)$ costs 4 with distances $(3, 4, 3) \to (4, 4, 0)$.
$(9, 0, 0) \to (0, 14, 0)$ is free, since $S\,14 = 9 \oplus 14$, with distances $(1, 0, 1) \to (0, 2, 2)$. The pulse
edge $(b, b, 0) \to (b, 0, 0)$ costs $q$ with distances $(q, q, 0) \to (q, 0, q)$. The first two give
$-\alpha + 3\chi \ge 3$ and $\alpha - 2\beta - \chi \ge -5$, whose sum is $\beta - \chi \le 1$, while the third gives
$\beta - \chi \ge 2 - 5/q$, which already exceeds 1 at $q = 8$. As G169 stresses, the free edge's reward $-5$ is what
supplies the upper bound. Checked (`rule30_audit_g99_g100.py`, S64): the children, gates, costs and distance triples of
all three edges (the pulse at $q = 4, 8, 16$), and the coefficient arithmetic of the two inequalities.

### G.GPT170. embedded period constraints reject three-distance coefficients (second-read by Local, 2026-10-07)

### GPT G170 — embedded period constraints reject three-distance coefficients (RULE30-GPT.md G170; awaiting second reader, 2026-10-07)

**Stronger family restriction; review requested.** Fix a dyadic common period q>=8. Its compatible graph includes words whose least period divides q, as G7/G157 specify; it is not restricted to least period exactly q. Consider

    h_q(a,b,r)=C_q+alpha_q*D(a,r)+beta_q*D(b,r)+chi_q*D(a XOR b,r).

Here all four coefficients may depend on the common graph period q, but are shared by all its vertices. If this potential satisfies every gated edge inequality at slope gamma, then necessarily

    gamma >=3q/(q+1).

Thus no such formula certifies gamma5/2 at any dyadic common period q>=8. Even allowing coefficients to vary with the common period cannot rescue this family. For any fixed gamma<3 it fails at all sufficiently large dyadic q. This is a necessary bound, not a construction at equality, and nonnegativity of the coefficients is not assumed.

**Proof by three explicit edges.** Repeat G169's period4 words(12,8),(8,8),(9,0),(0,14) q/4 times in time. Shift, OR and XOR commute with this repetition, so their two edges remain compatible. Their phase0 delays and feature differences remain exactly the same: the gate reads time q-1, which has residue3 modulo4. Consequently their edge inequalities at slope gamma are

    -alpha_q+3*chi_q >=8-2*gamma,
    alpha_q-2*beta_q-chi_q >=-2*gamma.

Adding yields beta_q-chi_q<=2*gamma-4. The separate least-period-q single-pulse edge(b,b,0)->(b,0,0) remains gated and requires

    q*(beta_q-chi_q) >=2q-2*gamma.

Together these force2-2*gamma/q<=2*gamma-4, hence gamma>=3q/(q+1). Equivalently multiply each embedded inequality by q/2 and the pulse inequality by1. Every coefficient cancels, leaving0>=6q-2*gamma*(q+1). This explicit nonnegative combination is the contradiction certificate whenever the displayed necessary slope fails. C_q cancels separately on each edge. No numerical optimization is involved. Square.

**Known-value control and identified unexpected check.** At q8 the required slope is at least8/3, strictly larger than5/2. At gamma5/2 the cancelling combination gives0>=q-5, hence0>=3 at q8. The pulse itself has reward11 while the two embedded constraints give beta_q-chi_q<=1. At q4 the same combination gives no contradiction at5/2; no feasibility conclusion is made there. The unexpected ingredient is the embedded period4 states: their distances remain small after repetition, rather than scaling with q. Treating every q-bit word as having least period q would incorrectly erase these valid constraints.

**Scope and revised next intention.** G169's period-dependent-coefficient escape is now closed for coefficients chosen only by the common graph period. Coefficients chosen by the state's least pair period are different: the embedded states would use period4 coefficients and the pulse states period-q coefficients, so cancellation no longer follows. Nor does this reject nonlinear features, additional state information, a different domain proved closed, or rooted-only certificates. A full gated pair/phase potential is known feasible at gamma5/2 for q8; only this linear feature compression fails. Dependencies are G7's common-period convention, G169's literal edges and G160's gate. The repetition argument and linear dual certificate are elementary, with no novelty claim or new computation. Next useful family must distinguish embedded period strata or retain richer joint information; the all-period debt theorem remains open.

*Second reader's note on G170 (Local, 2026-10-07; chat L132).* Correct. Repeating G169's period-4 words $q/4$ times
commutes with the shift, OR and XOR, so both edges stay compatible. Their phase-0 delays and distance triples are
unchanged, and the gate reads time $q - 1$, which is 3 modulo 4. In doubled units at slope $\gamma$ the two embedded
inequalities give $\beta_q - \chi_q \le 2\gamma - 4$, and the least-period-$q$ pulse needs
$\beta_q - \chi_q \ge 2 - 2\gamma/q$. The weights $q/2, q/2, 1$ cancel every coefficient and leave
$0 \ge 6q - 2\gamma(q + 1)$, so $\gamma \ge 3q/(q + 1)$. That is $8/3 > 5/2$ at $q = 8$ and only $12/5$ at $q = 4$.
Checked (`rule30_audit_g99_g100.py`, S65) at $q = 8$ and 16: the repeated edges' children, gates, delays and triples,
and the dual combination's value for slopes on both sides of the bound. The scope point stands: coefficients chosen by
each state's least period are not covered.

### G.GPT171. exact-period witnesses reject three-distance coefficients (second-read by Local, 2026-10-07)

### GPT G171 — exact-period witnesses reject three-distance coefficients (RULE30-GPT.md G171; awaiting second reader, 2026-10-07)

**Stronger restriction; independent review requested.** For every dyadic q>=16, restrict to gated edges whose source and target pairs both have least temporal period exactly q. A potential of the three-distance form in G170, with coefficients selected by this least pair period, still requires gamma>=3q/(q+1). Thus no fixed gamma<3 can be certified at all sufficiently large dyadic periods by this family, even after removing all lower-period states and allowing arbitrary period-dependent coefficients. G170's embedded-state proof alone did not imply this stronger scope.

**Exact-period first edge.** Let b have black bits only at3,7,q-1, let a=S b XOR b, and take arrival r=0. The compatible child is c=b. Since b(0)=0 and b(q-1)=1, a(q-1)=1 and the source is gated. It costs4 and reaches(b,b,4); that target is gated because b(3)=1. The source distance triple is(3,4,3): D(a,0)=3, D(b,0)=4 and a XOR b=S b has first black bit2. From phase4 the target has distances(4,4,0), because its next black bit is7. Hence the first constraint remains

    -alpha_q+3*chi_q >=8-2*gamma.

The word b has odd weight3. A proper-period word at a dyadic common period repeats an even number of times and has even weight. Therefore b, and both endpoint pairs containing b, have least period q. The far black bit at q-1 creates exact-period membership without changing the local distance triples.

**Exact-period zero edge.** Let c have black bits only at1,q-1, and put a=S c XOR c. Use(a,0,0)->(0,c,0). The scalar integration equation holds, the cost is0, and the source/target gates follow from c(0)=0,c(q-1)=1. The feature triples are(1,0,1) and(0,2,2), so

    alpha_q-2*beta_q-chi_q >=-2*gamma.

The two black positions are not opposite at q>=16, so c cannot be a repetition of a proper dyadic divisor: a two-black word with a proper period would have to repeat twice with opposite black positions. Thus c has least period q. Also a has least period q. If a had period dividing q/2, then the difference c(t+q/2) XOR c(t) would be constant, since its temporal difference is0. Constant0 contradicts c's least period; constant1 would force c to have q/2 black bits, contrary to its weight2. This checks exact-period membership of the source as well as the child, which a common-period closure check would not suffice to establish.

**Third edge and contradiction.** The single pulse b at q-1 supplies the gated edge(b,b,0)->(b,0,0), both pairs of least period q, with constraint q*(beta_q-chi_q)>=2q-2*gamma. All three edges now use the same least-period coefficients and constant, which cancels on each edge. Multiply the first two inequalities by q/2 and the third by1. Their left sides cancel and give0>=6q-2*gamma*(q+1), hence gamma>=3q/(q+1). This is an explicit three-edge dual certificate, not a numerical feasibility result. Square.

**Known arithmetic controls and identified unexpected guard.** At q16 the first word is b=32904 and its preceding word is a=49356; the first arrival becomes phase4, not phase0. The second edge uses c=32770 and a=49155. Its preceding word must also have exact period16; checking only c would leave the coefficient cancellation unjustified. The pulse is32768. At gamma5/2 the certificate reads0>=q-5, hence0>=11 at q16. The original G170 embedding changed common period without changing least period; these sparse constructions genuinely change least period while retaining the same three observed distances. No run was used to obtain these controls.

**Counterfactual and remaining scope.** If coefficients were chosen by additional state features, the three inequalities could use different coefficients and cancellation would fail. Nonlinear features, explicit pair interactions, history-dependent or rooted-only certificates remain open. Root reachability of these witnesses is not asserted, and no positive compatible cycle or finite-seed obstruction is claimed. The bound3q/(q+1) is necessary only, not sufficient. This closes the least-period-coefficient escape for the specific three-reset-distance linear family, including finitely many exceptional small periods, but not the all-period O(q) debt conjecture. It uses G169-G170's algebra with explicit compatible exact-period witnesses; no novelty claim is made for linear duality or period counting. Next direct-charge proposals need additional joint state information rather than a period lookup for these same three features.

*Second reader's note on G171 (Local, 2026-10-07; chat L133).* Correct. The first edge is compatible because
$S b = a \oplus b$, and both ends are gated: the arrival moves to phase 4, where $b(3) = 1$. It keeps the triples
$(3, 4, 3) \to (4, 4, 0)$, since $b$'s next black bit after phase 4 is 7. The zero edge keeps $(1, 0, 1) \to (0, 2, 2)$,
and the pulse edge is as in G166. The exact-period arguments hold. An odd-weight word cannot repeat at a dyadic period.
The two black positions 1 and $q - 1$ are opposite only when $q = 4$. A period of $q/2$ in $a$ would make
$c(t + q/2) \oplus c(t)$ constant, which neither value allows. So the same least-period coefficients appear in all three
inequalities, and the dual weights cancel them as in G170. Checked (`rule30_audit_g99_g100.py`, S66) at
$q = 16, 32, 64$: compatibility, gates, costs, triples and least period exactly $q$ for every endpoint word. At $q = 16$
the words are 32904, 49356, 32770, 49155 and 32768, as stated.

### G.GPT173. exact-period feature collision rules out nonlinear three-distance charges (second-read by Local, 2026-10-07)

### GPT G173 — exact-period feature collision rules out nonlinear three-distance charges (RULE30-GPT.md G173; awaiting second reader, 2026-10-07)

**Symbolic theorem; independent review requested.** For every dyadic q>=4 there is a gated compatible edge whose source and target have the same three reset distances(1,3,1), the same least pair period q, and elapsed time3. Consequently no finite potential depending only on these three distances and the least pair period can satisfy every full gated-domain edge inequality at any slope gamma<3. The function can be arbitrary and nonlinear, chosen separately for each period; no potential-size or coefficient restriction is assumed. This is an ambient-domain compression obstruction, not a rooted theorem.

**Construction at q>=8.** Let b have black bits only at2,3,q-1, and c black bits only at1,5,q-1. Define a=S c XOR(b OR c), so the triple is compatible by construction. Begin at phase0. Since b's first black bit is2, its reset costs3. At the source a(0)=c(1) XOR(b(0) OR c(0))=1, while b(0)=0; therefore D(a,0)=1, D(b,0)=3 and D(a XOR b,0)=1. At the target(b,c,3), b(3)=1, c(3)=c(4)=0 and c(5)=1. Its three distances are also(1,3,1). Both gates hold: a(q-1)=c(0) XOR(b(q-1) OR c(q-1))=1 at the source, and b(2)=1 at the target.

Both b and c have exactly three black bits, so have least period q: any repetition of a proper dyadic divisor would have even weight. Each pair contains b, hence both pair periods are q even if a has a smaller period. This last distinction matters at q8, where a is the constant-one word. In the proposed feature potential the edge's two values are identical, while its reward is3-gamma (or twice that in doubled arithmetic). The inequality would require0>=3-gamma. Square.

**Period4 base and known controls.** Local's DQ3 edge is source(a,b)=(15,12), child c=2, arrival0->3. Its aligned target is(9,4). Both pair periods are4, both gates hold, and both feature triples are(1,3,1). The reward at5/2 is1 in doubled arithmetic. At q8 the sparse family gives source(255,140), unaligned child162 and aligned target(145,84); the independent scalar audit above verifies it. The q4 and sparse q8 checks use different actual triples, not an assumed extension of one pair cycle. No further numerical run is needed for the general construction.

**Identified unexpected guard: pair period survives even when one word collapses.** At q8 the source a=255 has period1, not8; source pair(a,b) still has least period8 because b has odd weight3. Requiring every individual word to have period exactly q would incorrectly discard the witness, although G8/G172's graph and G171's coefficient classification use the pair's period. Conversely the source and target actual pairs differ, so the feature self-loop cannot be repeated as a real self-loop. The known original finite certificates remain consistent with this positive projected edge.

**What closes and what remains.** G169-G171's linear restrictions are strengthened: even arbitrary nonlinear functions of the same three distances, augmented by least pair period, fail below3 on every tested or constructed dyadic period q>=4. A rooted-only domain may exclude these witnesses; no root membership is asserted. Additional temporal profile information, other joint features and history-sensitive charges remain possible. The actual all-period O(q) budget, contracted certificate K of G168, and period-growth estimate remain unproved. This theorem is a direct symbolic extension of DQ3's audited feature collision using G7 compatibility and G160's gate; no novelty or prize solution is claimed. Next reasoning should use a feature that distinguishes these explicitly colliding states, rather than another function of the same three distances.

*Second reader's note on G173 (Local, 2026-10-07; chat L135).* Correct. The triple is compatible by construction. At
phase 0, $a(0) = c(1) = 1$ and $b(0) = 0$ give the source triple $(1, 3, 1)$, and $b$'s reset costs 3. At phase 3,
$b(3) = 1$, $c(3) = c(4) = 0$ and $c(5) = 1$ give the target triple $(1, 3, 1)$. Both gates hold. Both pairs have least
period $q$ because $b$ has weight 3, even at $q = 8$, where $a$ is the all-ones word. A function of the features and the
pair period alone would therefore need $0 \ge 3 - \gamma$. Checked (`rule30_audit_g99_g100.py`, S67) at $q = 4$ (DQ3's
$(15, 12)$ with child 2, aligned target $(9, 4)$) and at $q = 8, 16, 32, 64$: compatibility, gates, cost and arrival
phase, both triples, and pair least period $q$ at both ends. At $q = 8$ the words are 255, 140 and 162, with aligned
target $(145, 84)$, as stated.

### G.GPT174. rooted word membership does not imply root-clock membership (second-read by Local, 2026-10-07)

### GPT G174 — rooted word membership does not imply root-clock membership (RULE30-GPT.md G174; awaiting second reader, 2026-10-07)

**Root-word versus root-clock scope audit (2026-10-07; review requested).** DQ3's period4 source pair(15,12) is word-rooted, reached after10 spatial edges on the unique predecessor chain. In root-to-source order the exact pairs are

    (0,15),(15,15),(15,0),(0,5),(5,15),(15,5),(5,5),(5,0),(0,9),(9,15),(15,12).

Every consecutive triple satisfies the scalar equation; the constant-one root is integer15, not integer1. Carry G8's full-line clock from each initial root time0,1,2,3 along this chain. The source arrival times are9,13,13,13, hence all four arrival phases are1. These values were predicted from literal arithmetic before the independent targeted script `tests/probes/lexicon/rule30_dq3_root_clock_review.py` was executed; its scalar backward, forward and reset checks pass. No tree or quotient census was repeated.

At the actual reached phase1, source features are(1,2,1), its next reset costs2, and the target phase3 features are(1,3,1). The feature self-loop at source phase0 therefore disappears on this particular root-clock edge. Phase0 still satisfies the gate a(-1)=1. This is the identified unexpected guard: a pair can be word-rooted and gated at a clock that no root-start phase reaches. G7's unique predecessor guarantees there is no alternate word path to this same pair; enumerating all four initial clock residues is sufficient for the fixed period4 full-line front.

Consequently the q4 witness rejects a three-distance certificate on rooted word pairs required to cover every gated clock, but does not reject the same family restricted to clock states actually reached from the root. This is a sharper quantifier distinction than saying the witness is simply unrooted. Restart clocks at interior vertices and birth-clamped fronts are different domains; neither was tested or excluded here. G164's separate phase-transfer theorem remains relevant if a reference-clock budget can be proved. The all-period exact-family construction of G173 remains ambient, with no newly claimed rooted-clock membership at larger periods. Next scope to investigate is the explicitly root-reached clock graph, preserving actual clocks through every child rather than treating the gate as sufficient reachability.

*Second reader's note on G174 (Local, 2026-10-07; chat L136).* Correct. The ten-edge chain is compatible at every
triple. It is the unique predecessor chain from $(15, 12)$ back to the root $(0, 15)$, so with G7's unique predecessor,
the four root residues exhaust every root-reached clock. Carrying the full-line clock by literal reset scans from times
0, 1, 2, 3 reaches the source at times 9, 13, 13, 13, so always at phase 1. There its triple is $(1, 2, 1)$, the reset
of 12 costs 2, and the target at phase 3 has $(1, 3, 1)$, so DQ3's feature self-loop does not occur on a root-reached
clock. Phase 0 is gated but no root start reaches it. Checked (`rule30_audit_g99_g100.py`, S68) by my own scans, and
GPT's `rule30_dq3_root_clock_review.py` reproduces here with the same path and arrivals. The scope is as stated:
interior restarts, birth clamps and larger periods are not covered.

### G.GPT176. reached q8 feature collision: targeted independent audit (second-read by Local, 2026-10-07)

### GPT G176 — Reached q8 feature collision: targeted independent audit (2026-10-07)

**Finite exact certificate, pending second reader.** Local's RQ3 outcome L137 refutes G175's blind RQ-P1 at q8; q4 passes descriptively. Independently reconstructing the q8 witness confirms a root-reached compatible edge with identical features(Phi,p)=(1,5,1,8) and delay5. Thus no finite function of these features can satisfy every edge inequality at any slope gamma<5 even on actual root-reached clocks at q8. This is a compression obstruction, not a cycle of actual states or a lower bound on long-run speed.

**Reproducible certificate.** Bits are indexed by time modulo8. Let the absolute source pair be(183,176) and child26. The target at phase5 is aligned(133,208). Reconstruct the predecessor of(a,b) as(B,a), with B(t)=b(t+1) XOR(a(t) OR b(t)). Iterating this deterministic rule exactly190 times reaches(0,255). Reversing gives a compatible root path; append(176,26) as edge191. Literal reset scans from root time0 arrive at the source at360 and target at365. Both gates hold. At source phase0 and target phase5, the three distances are(1,5,1); both pairs have least period8. Therefore their feature potential values agree and their edge inequality would require0>=5-gamma. No all-period extension is asserted.

**Independent controls before execution.** The source, target, delay, depths and arrival365 were reported by Local, not blind predictions. GPT's independent `tests/probes/lexicon/rule30_rq3_review.py` imports no Local code, builds no graph, derives the child by undoing the target rotation, reconstructs the unique ancestry, then checks every forward triple and carried clock. All pass. Toggling source bit0 breaks compatibility, as the counterfactual requires. The identified unexpected check carries all eight initial root residues: all reach this same absolute source/target time pair(360,365). Thus the displayed edge is not an artifact of choosing only one root residue. GPT Intel CPU0.0024 s/RSS9.4 MiB; these are targeted audit resources, distinct from Local's M5 full RQ3 run CPU0.05 s/RSS9.8 MiB.

**Finite evidence retained.** Local reports reached vertices/edges3/2,9/9,31/32,409/411 at common caps1,2,4,8, with one cap exit each and maximum depths2,7,28,399. RQ-C1/C2/CF and boundary controls pass; q4 feature potential maximum1 passes every lifted edge. GPT does not independently certify that census or q4 feasibility here. The independent path certificate suffices for the q8 obstruction. RQ-P1 is REFUTED, not rescued by the q4 pass. No period-growth, all-period debt, restart or birth theorem follows. Existing unrestricted pair/phase potentials remain consistent: their two endpoint values may differ. Next reasoning must distinguish these two reached states or use a nonlocal/path certificate; another function of these same features cannot repair the failure.

*Second reader's note on G176 (Local, 2026-10-07; chat L138).* Correct; this is GPT's independent reconstruction of my
RQ3 witness, and it agrees with mine at every point. The pair $(183, 176)$ has a unique predecessor chain of exactly 190
steps to the root $(0, 255)$. Its child 26 gives $(176, 26)$, aligned $(133, 208)$ at phase 5. Every forward triple is
compatible. From all eight root residues the clock reaches the source at 360 and the target at 365, so the edge does not
depend on the root phase. Both ends are gated, with distances $(1, 5, 1)$ and pair least period 8, so any function of
those features would need $0 \ge 5 - \gamma$. Checked (`rule30_audit_g99_g100.py`, S69) by my own code, including the
bit-0 toggle counterfactual, and GPT's `rule30_rq3_review.py` reproduces here unchanged. G176 does not certify my RQ3
census or the $q = 4$ feasibility; those rest on the RQ3 run's controls.

### G.GPT178. temporal-order refinement still aliases distinct reached segments (second-read by Local, 2026-10-07)

### GPT G178 — Temporal-order refinement still aliases distinct reached segments (2026-10-07)

**Finite exact certificate, second reader pending.** Local's RQO run L139 confirms G177's blind RO-P1: a positive refined feature cycle remains at q8. GPT independently reconstructs its rooted representatives, clocks and order labels without importing Local code or rebuilding the graph. For the feature tuple(Phi,p,nu(a),nu(b),nu(a XOR b)), seven valid reached edge inequalities sum to0>=21-7*gamma. Thus every function of this tuple fails to certify all reached edges at any slope gamma<3. The order refinement separates G176's one-edge collision but does not repair the entire family. This is not a genuine coherent cycle or a speed theorem.

**Explicit representative certificate.** The first reached segment begins at depth270 and takes five consecutive edges; the second begins at depth318 and takes two. Aligned states and elapsed costs are:

    (143,26) -> (134,186), 2
    (134,186) -> (174,62), 2
    (174,62) -> (143,200), 2
    (143,200) -> (140,168), 4
    (140,168) -> (138,140), 4
    (182,84) -> (138,152), 3
    (138,152) -> (137,206), 4.

Their successive feature labels, with the two splices identified, are:

    (1,2,1,8,8,8,7)
    (2,2,3,8,8,8,5)
    (2,2,5,8,8,8,7)
    (1,4,1,8,8,8,7)
    (3,4,3,8,8,8,7)
    (2,3,2,8,8,8,7)
    (2,4,2,8,8,8,7)
    (1,2,1,8,8,8,7).

Summing potential inequalities cancels the feature values. Total elapsed time is21 over7 edges; doubled slope-5/2 reward is7. Actual state joins fail at BOTH splices: (138,140) differs from(182,84), and(137,206) differs from(143,26). The two segments are not a valid concatenated history. Even though individual endpoint orders agree at the splices, detailed relative temporal placement differs.

**Root and independent controls.** The audit `tests/probes/lexicon/rule30_rqo_review.py` reconstructs the unique predecessor chain of raw pair(143,26) back270 steps to(0,255), checks every forward triple, and carries all root residues until a phase-zero arrival is obtained (source520). Five literal unique-child extensions give the first segment. Separately, reconstruct the ancestry of(137,206) back320 steps and carry root clocks to a phase-zero endpoint; times617,620,624 align the last two edges. Reversing the target rotation supplies each actual child. Every recurrence, source gate, target gate and reset scan passes. Toggling source bit0 breaks each representative recurrence, as predicted before execution.

The independent order calculation expands w(1+Y) using binomial coefficients modulo2: its first nonzero coefficient has degree v, and nu=q-v for nonzero w. Cyclic derivative annihilation agrees on the witness words. The identified unexpected check verifies BOTH false state joins despite matching features; rotations preserve the order labels. Zero has order0, all-one255 order1. G176 endpoints remain separated under refinement. GPT Intel targeted audit CPU0.0160 s/RSS9.8 MiB; Local M5 full RQO CPU0.39 s/RSS10.7 MiB. The audit verifies the certificate, not the full quotient census.

**Retained evidence and next obligation.** Local reports264 refined vertices/398 quotient edges at q8, domain counts unchanged, q1/q2/q4 feasible with maxima0,0,1, and all original control checks passing. Those are Local's finite computations; RO-P1 HELD and RO-CF shows the earlier collision was repaired, not retained by an implementation bug. No all-period debt, period growth, interior restart or birth bound follows. Further reasoning should constrain permissible history splices or retain relative placement information, rather than infer a timing charge from derivative orders alone. No new computation is requested here.

*Second reader's note on G178 (Local, 2026-10-07; chat L140).* Correct, and it agrees with my RQO run at every point.
The seven representatives are reached edges at depths 270 to 275 and 318 to 320. Their costs are 2, 2, 2, 4, 4, 3 and 4,
which sum to 21. Their refined labels close in feature space, so the summed inequalities give $0 \ge 21 - 7\gamma$,
hence $\gamma \ge 3$, for every function of the refined tuple. GPT is right that both splices are false joins,
$(138, 140) \ne (182, 84)$ and $(137, 206) \ne (143, 26)$; my L139 mentioned only the second. Checked
(`rule30_audit_g99_g100.py`, S70) against RQ3's reached $q = 8$ domain: membership and depths of all seven edges, their
costs, all eight labels by RQO's order code, and both false joins. GPT's `rule30_rqo_review.py` reproduces here
unchanged, including its root clocks 520 and 617, 620, 624.

### G.GPT179. form actual edge context before compression; conditional lift pays the first edge (second-read by Local, 2026-10-07)

### GPT G179 — Form actual edge context before compression; conditional lift pays the first edge (2026-10-07)

**Symbolic conditional theorem, second reader pending; no run.** Let a directed graph have real edge rewards w(e), with W=max(0,sup_e w(e)) finite. Its actual line graph has an edge-state e=(s,t) for each original edge, and an arc e->f precisely when f=(t,u) is an actual consecutive edge. Charge that arc by w(f). Suppose a nonnegative bounded K on edge-states satisfies

    K(e) >= w(f)+K(f) for every actual consecutive pair e,f.

Define the original vertex potential

    h(s)=max(0,sup over outgoing e=(s,t) of [w(e)+K(e)]),

with an empty outgoing supremum omitted. Then h(s)>=w(e)+h(t) on every original edge e=(s,t), and 0<=h(s)<=W+sup K. Conversely any nonnegative original vertex potential h satisfying the one-edge inequalities gives an edge potential K(s,t)=h(t) satisfying all consecutive-edge inequalities. Thus the actual line graph changes representation, not the existence of an unrestricted certificate.

**Proof.** Fix e=(s,t). Nonnegativity gives K(e)>=0. Its consecutive-edge inequalities give K(e)>=w(f)+K(f) for every outgoing f at t. Therefore K(e)>=h(t), including t with no outgoing edge. By definition h(s)>=w(e)+K(e)>=w(e)+h(t). The size estimate uses w(e)<=W and bounded K. For the converse, K(s,t)=h(t) turns its required inequality into h(t)>=w(t,u)+h(u), an original edge inequality. Square. Telescoping bounds every original finite subinterval by W+sup K, including the first edge and early stopping. There is one reserve, not one reserve per context change.

**Compression order matters.** For a feature map phi, form the actual line graph FIRST, then label an edge-state by(phi(s),phi(t)) and retain only arcs witnessed by an actual pair s->t->u. A potential of these labels lifts by the theorem, if all actual arcs and nonnegative stopping inequalities hold. It can distinguish permissible triples that the one-feature quotient lost. It need not distinguish all actual histories, and no such potential is constructed here.

In contrast, taking the line graph AFTER compressing vertices creates an arc whenever two feature edges meet at a feature, even if their representatives have different actual middle states. Every directed feature cycle gives a directed cycle of its edge-states with the same total reward, since charging each line arc by its second edge merely cyclically shifts the sum. G178's seven-edge/elapsed21 false cycle therefore survives this post-compression line graph unchanged. This counterfactual is refuted symbolically; adding edge labels after losing actual adjacency cannot remove the obstruction.

**Identified unexpected terminal check.** A graph consisting of one edge s->t of positive reward r has a line graph with one vertex and no arcs. K=0 satisfies every line inequality, yet zero original potential fails. The formula correctly gives h(s)=r and h(t)=0. Omitting the first-edge reserve or replacing h(s) by an incoming-context value misses this terminal path. This is a generic weighted-graph control, not a claim of a new Rule30 compatible witness.

**Rule30 scope and record.** For doubled slope5/2 within common cap q, every original delay is at most q, so W=max(0,2q-5). Consequently a proved O(q) context certificate would yield an O(q) original interval certificate with this single extra reserve; G165/G164's separate stage, clock and birth transfers remain conditional on their own hypotheses. Neither K nor a uniform size bound or period-growth theorem is supplied. G8/G166 already use weighted Bellman inequalities; G168 gives a different conditional lift for contracted branch blocks. This is standard line-graph representation and elementary Bellman algebra, not a novelty claim. The primary Wolfram LineGraph documentation defines directed adjacency by actual target/source equality: https://reference.wolfram.com/language/ref/LineGraph.html. Existing-record search found no prior actual-before-feature edge-context lift in this lane. Next useful question is whether a small pre-compression context family has a uniform certificate, rather than assuming the line graph of an already failed quotient provides new information.

*Second reader's note on G179 (Local, 2026-10-07; chat L141).* Correct. Nonnegativity and the consecutive-edge
inequalities give $K(e) \ge h(t)$, so $h(s) \ge w(e) + K(e) \ge w(e) + h(t)$, with $h \le W + \sup K$; and
$K(s, t) = h(t)$ gives the converse. Compressing before forming the line graph keeps every feature cycle as an
edge-state cycle with the same total, because charging each arc by its second edge only shifts the sum cyclically. So
G178's false cycle survives that order. The single-edge terminal case shows why the first-edge reserve is needed.
Checked (`rule30_audit_g99_g100.py`, S71) on 300 random weighted DAGs, comparing the least line-graph potential, its
lift and the converse. It also checks the terminal control ($h = (5, 0)$ with $K = 0$), and that G178's seven feature
edges, line-graphed after compression, still close with total doubled reward 7. For Rule 30 at cap $q$ the reserve is
$W = \max(0, 2q - 5)$, as stated.

### G.GPT182. the finite RC2 certificate verified statically (second-read by Local, 2026-10-07)

### GPT G182 — RC2 finite reached-domain certificate independently verified (2026-10-07)

**Finite certificate theorem, second reader pending.** On the clock-aligned root-reached graphs at common caps q1,2,4,8, the exported RC2 certificate supplies nonnegative original vertex potentials h satisfying h(s)>=2*delay(s,t)-5+h(t) on every retained edge, with maxima0,0,1,14 respectively. Therefore every finite path segment remaining in the corresponding reached domain has doubled slope-5/2 reward at most that maximum, by telescoping. The q8 upper budget is14, or7 in undoubled arithmetic. This proves neither minimality nor any uniform all-period bound. A cap exit has reward-5 but the ensuing larger-period stage is outside this certificate.

**Artifact and provenance.** The static artifact `rc2-certificate.json` has56,232 bytes and SHA-256 f8d57126f5601ec41295db803ba13271ac54523e4b39a6c5a749b3f30e76a2a7. Local produced it with exporter commit c5d24a0, after regenerating the arrays because the original RC2 run retained none; L143 records that limitation and matching counts/maxima. The numerical data remains outside Git in the shared scratch. Git holds the producing source, checksum, independent checker and this conclusion. No claimed provenance relies on a flag's note.

**Independent verification of coverage and values.** GPT's `tests/probes/lexicon/rule30_rc2_certificate_check.py` imports no Local code and performs no Bellman iteration, potential search or graph-generation traversal. For each supplied vertex it validates the supplied parent chain to the constant root, and every supplied edge by literal compatibility, rotation and reset scans. It enumerates scalar candidate child words at each supplied state to verify successor closedness against the edge list; reachability plus closedness certifies the exact finite reached graph. A no-child state must be a zero driver with odd source parity, whose cap exit costs0/reward-5. Features use scalar resets, least pair period and independent binomial substitution at X=1 for temporal difference order.

Every K row is nonnegative, every actual consecutive-edge inequality holds, and every edge label is represented, terminal labels included. The G179 lift is computed explicitly and every original edge inequality checked. Confirmed counts (vertices/edges/context labels/actual arcs) are3/2/2/1,9/9/9/9,31/32/32/33,409/411/398/413. Confirmed K and h maxima are0,0,1,14 at the four caps. The checker verifies the artifact's summary against these computed values, not merely its printed assertions.

**Controls retained from G181.** Zero K fails a known positive actual context arc; deleting the known(143,26)->(134,186) edge fails successor closedness. Terminal labels are present. The identified unexpected strict-bound guard passes: q8 hmax14 is strictly below Kmax+11, so the checker does not mistake the reserve bound for an equality. Parent coverage, successor closedness and numerical inequalities all pass separately. GPT Intel static audit CPU0.1287 s/RSS14.4 MiB; Local's regeneration CPU0.01 s/RSS12.2 MiB is a separate run. CV-C1/C2 expectations hold; no failed check or partial stop is counted as a pass.

**Scope and closure of this block.** RC-P1's finite success is now independently verified, while its398/411-label caveat remains unchanged. This does not establish a small context family, bounded degree-independent memory, linear certificate magnitude at unbounded periods, period growth, arbitrary interior clocks or birth-clamped bounds. The gap-1 candidate-refinement loop stops here following CL011's coordination steer. Next GPT work is a reasoning synthesis of the compression failures, then the open period-growth obligation of G165; no new candidate family or larger-period job is launched.

*Second reader's note on G182 (Local, 2026-10-07; chat L144).* Correct. The theorem rests on the lifted $h$ alone:
$h \ge 0$ and $h(s) \ge 2\delta - 5 + h(t)$ on every edge telescope to a path bound of $h(\text{start}) \le \max h$, and
the labels, $K$ and context arcs only produce $h$. The domain is exact because the parent chains give reachability and
successor closedness shows that no reached state is missing. Checked (`rule30_audit_g99_g100.py`, S72) on the
certificate rebuilt in memory, which is byte-identical to the shared artifact (56,232 bytes, the recorded SHA-256), so
the audit needs no outside file. GPT's checker on this machine's Python 3.9 stops with an `AttributeError` on
`int.bit_count` (a crash, not a pass). With that one call replaced it accepts all four caps and a reordered copy. It
rejects eight real corruptions, each at the intended assertion: zero $K$, a lowered tight $K$, the known edge removed, a
non-tree edge removed, a changed delay, a dropped terminal label, a false summary and an unreached vertex. GPT's two
negative controls are proxies (a positive context arc exists; a set difference is nonempty), not runs on a corrupted
file; S72 runs them. One detail to correct: removing $(143, 26) \to (134, 186)$ is caught first by the parent check,
because it is $(134, 186)$'s parent edge. Successor closedness catches a removed non-tree edge (three exist at $q = 8$,
one of them $(0, 85) \to (170, 255)$). Beyond G182, the finite maximum is minimal. The least nonnegative potential on
the certified edges has maxima 0, 0, 1, 14. At $q = 8$ the maximum is attained once, by the reached path from
$(143, 200)$ at depth 273 to $(132, 215)$ at depth 281, with doubled rewards 3, 3, 1, −3, 5, −3, 3, 5. So no certificate
on this domain has a maximum below 14. Pointwise the $K$ lift is not least: it exceeds the least potential at 14 of 409
vertices, by at most 5. As GPT states, this says nothing about larger periods.

### G.GPT183. compression fails exactly at positive label-balanced edge collections (second-read by Local, 2026-10-07)

### GPT G183 — Compression fails exactly at positive feature-balanced edge collections (2026-10-07)

**Symbolic synthesis, second reader pending; no run or new candidate family.** Let G be a finite directed graph of actual states and edges, with elapsed costs delta(e), and let phi map states to any finite set of retained labels. Fix slope gamma and reward w(e)=delta(e)-gamma. A finite potential F on labels satisfying

    F(phi(s))-F(phi(t)) >= w(s,t) for every actual edge s->t

exists if and only if there is NO finite multiset of actual edges with positive total reward and equal incoming/outgoing edge multiplicity at each LABEL. Balance is required at phi(s), not at the actual state s. Consequently a collection can obstruct this feature family even when its edges cannot concatenate into an actual history. This is the exact information-loss mechanism common to the recorded failures; it names a criterion on a chosen compression, not a universal theorem against every compression.

**Proof of obstruction and converse.** For a label-balanced multiset, sum its edge inequalities with their nonnegative integer multiplicities. Each label's potential cancels, giving0>=sum w, which contradicts positive reward. Conversely form the label multigraph with one arc phi(s)->phi(t) for each actual edge, retaining its reward. Any label-balanced edge multiset decomposes into directed label cycles by repeatedly following an unused outgoing edge until a vertex repeats and removing that cycle. Thus if its total reward is positive, at least one cycle has positive reward. A positive label cycle itself supplies a balanced multiset of actual representative edges. These equivalences do not assume actual-state joins.

If there is no positive label cycle, set H(x) to the maximum total reward of any finite label walk starting at x, allowing the empty walk. Every cycle has nonpositive reward; deleting cycles never decreases a walk's reward, so a maximum occurs on a simple path and is finite. Prepending an arc x->y gives H(x)>=w(x,y)+H(y), so H is a nonnegative feasible potential. Any other nonnegative feasible F bounds every starting walk by telescoping and F(end)>=0, hence F(x)>=H(x). H is the least nonnegative feature potential. Square. Arbitrary real finite potentials add no feasibility advantage: on this finite label set a constant shift makes them nonnegative without changing inequalities.

**What the records actually close.** G166 supplies a driver-only label loop and a phase-free balanced collection; G173 supplies exact-period same-label edges on every dyadic ambient cap q>=4, requiring slope>=3. G176's actually reached q8 edge requires slope>=5 for the three-distance-plus-period labels. G178 supplies a seven-edge collection balanced in distance-plus-order labels, elapsed21 over7 edges, requiring slope>=3. Its two false joins explain why the balance is not an actual cycle. G179 shows that a line graph formed after compression preserves the same balanced collection. RC2 avoids those known collections at q<=8 by retaining actual adjacency before compression, but G182's398/411 labels give no small uniform representation theorem. These are distinct domain and feature restrictions; none may be promoted to a claim that every lost observable is indispensable.

**Budget magnitude is a separate obligation.** Even if every q-level quotient has no positive cycles, an O(q) feature budget requires the maximum reward of ALL quotient walks to be O(q), by the least-potential characterization above. Existence alone gives no such estimate; walks may use joins impossible in the actual graph. On the uncompressed graph, uniform bounded debt B over every finite path is equivalent to a nonnegative vertex potential bounded by B: define h(s)=sup of rewards of finite paths starting at s, including the empty path, and prepend edges as above. Conversely telescope a bounded potential. This statement also holds on an infinite graph if B is genuinely uniform. The definition is a restatement of the debt bound, not a method to prove it. A single C shared across all histories is stronger than G165's permitted history-dependent constants; this synthesis does not silently strengthen that quantifier.

**Identified unexpected check against overgeneralization.** A generic three-state path s->t->u with rewards+1,-1 admits the noninjective label map phi(s)=phi(u)=A, phi(t)=B. Its label cycle has total0, and F(A)=1,F(B)=0 pays both edges. States were forgotten and a false join introduced, yet a bounded feature certificate exists. This is a weighted-graph logical control, not a new Rule30 witness. It refutes inferring 'every noninjective compression fails' from the selected positive examples. Likewise taking an already proved h as a scalar feature trivially yields a sound budget, but merely encodes the answer; one scalar is not automatically one small piece of information.

**Prior record and next direction.** G8/G166 already use the standard difference-constraints/positive-cycle criterion; this statement consolidates its representative-edge and uniform-size quantifiers for CL011. Primary prior art: MIT's difference-constraints lecture explains the corresponding negative-cycle criterion after reversing reward signs (https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/a9e76885a78c729f2375e14830caebf2_MIT6_046JS12_lec07.pdf, section7.2.2). No novelty claim. The gap-1 refinement loop remains closed. The next reasoning block is G165's independent period-growth obligation2^j/N_j->0; no new family, larger graph or run is queued.

*Second reader's note on G183 (Local, 2026-10-07; chat L145).* Correct. It is the standard difference-constraint
criterion (the positive-cycle test, the textbook negative-cycle test with signs reversed) on the graph whose vertices
are labels and whose arcs are the actual edges. Summing the inequalities over a label-balanced multiset cancels every
potential. A balanced multiset splits into closed label walks, one of them positive. The least potential is the best
walk from each label, and telescoping puts it below every other nonnegative one. Checked (`rule30_audit_g99_g100.py`,
S73) on 400 random small graphs with random label maps. Feasibility by longest-path relaxation agrees with a brute-force
search over subsets of actual edges for one that balances at every label with positive reward (111 feasible, 260 not).
Subsets suffice, because a simple label cycle uses each arc once. On the feasible graphs the least potential equals the
best simple label walk, and potentials relaxed from random nonnegative starts lie above it. The merged-endpoint control
is feasible with $F = (1, 0)$, as stated. The cited collections were re-checked on actual edges. G176's reached $q = 8$
edge (cost 5) balances alone in the three distances plus period, but not in RQO's labels. DQ3's literal $q = 4$ edge
$(15, 12) \to (9, 4)$ (cost 3) balances alone in the three distances. G178's seven reached edges, elapsed 21, balance at
every RQO label but not at four actual states. The size remark agrees with S72: the same least-potential argument on the
actual $q = 8$ graph gives the exact budget 14. The quantifier remark is right, since G165 asks for one $C$ per history,
not one for all. I did not open the cited lecture notes; the proof as given is complete without them.

### G.GPT184. the period-growth gap is an exponentially weighted stage-length condition (second-read by Local, 2026-10-07)

### GPT G184 — Period-growth gap is an exponentially weighted stage-length condition (2026-10-07)

**Symbolic checkpoint, second reader pending; no run.** Fix one infinite admissible rooted history, with N_j the first node of least pair period2^j as in G165. Let ell_j=N_(j+1)-N_j be its spatial stage length, lambda_j=ell_j/2^j and R_j=N_j/2^j. G165's required sublinear period growth is exactly R_j->infinity. The entry recurrence becomes

    R_(j+1)=(R_j+lambda_j)/2,
    R_j=2^(-(j-J))*R_J + sum from i=J to j-1 of 2^(-(j-i))*lambda_i.

Thus the missing growth estimate is divergence of this exponentially weighted moving sum of normalized stage lengths. It is not merely divergence of absolute stage lengths, a large observed entry depth, or a geometric delay lower bound.

**Proof and useful sufficient condition.** N_(j+1)=N_j+ell_j gives the first identity after division by2^(j+1); induction gives the second. G165 already proves p_k=o(k) iff2^j/N_j->0, which is R_j->infinity. If lambda_j->infinity, then R_(j+1)>=lambda_j/2->infinity. More generally, for any fixed positive m and j>=J+m,

    R_j >= 2^(-m) * sum from i=j-m to j-1 of lambda_i.

Hence divergence of an unweighted sum over any fixed recent window of normalized stage lengths is sufficient. These are conditions to prove from compatibility, not estimates supplied here. Their constants and eventual thresholds may depend on the history, as G165 allows.

**Counterfactual: geometric delay alone is insufficient.** For a synthetic stage schedule with lambda_j=C>0 after J (choose integer C so ell_j=C*2^j are positive integers), the recurrence gives R_j=C+2^(-(j-J))*(R_J-C). Thus R_j tends to C rather than infinity, despite exponentially increasing absolute stage lengths and arbitrarily large initial R_J. Its period/depth ratio tends to1/C rather than0. This is a logical stage-schedule control, not a compatible Rule30 counterexample. It shows that a proof of ell_j>=c*2^j with fixed c would not by itself settle the growth target.

**Identified unexpected check: individual normalized stage lengths need not diverge.** In a synthetic integer schedule let lambda_j=1 at even j and lambda_j=j at odd j (after any finite prefix). Then R_j->infinity: if j-1 is odd, R_j>=(j-1)/2; if j-1 is even, the preceding odd term gives R_j>=(j-2)/4. Yet lambda_j remains1 at every even index. Therefore lambda_j->infinity is sufficient, not necessary; refuting that stronger condition would not refute period growth. The two-step recent-window sufficient condition covers this example. Conversely any finite prefix's contribution decays as2^(-(j-J)), so no finite delay record alone can force the limit.

**What the recorded depths say.** The certified unbranched small-cap prefixes give N_1=3,N_2=8,N_3=29,N_4=400, hence R_1=1.5,R_2=2,R_3=29/8,R_4=25. Their normalized completed stage lengths are lambda_1=5/2,lambda_2=21/4,lambda_3=371/8. These are existing G161/G165 and Local L115 records, not new measurements. The known period16 genuine branch at depth53208 preserves period16; it is NOT N_5. Later period16 branch examples likewise supply no certified period32 entry. No N_5 value or asymptotic stage-length estimate is inferred.

**Scope and next proof obligation.** The recurrence is elementary weighted summation applied to G165's reviewed dyadic stage structure; no novelty claim or new experiment. All controls here are algebraic synthetic schedules and explicitly lack Rule30 compatibility. A sufficient next lemma would bound actual normalized stage lengths from below by a quantity tending to infinity, or establish divergence of their recent-window sum on each admissible history. Genuine branch spacing from G159 does not imply this bound: same-period branches do not end the stage. GPT next examines constraints at consecutive odd zero-driver doubling events, reasoning first; no new gap-1 family or larger-period run is queued.

*Second reader's note on G184 (Local, 2026-10-07; chat L146).* Correct. Dividing $N_{j+1} = N_j + \ell_j$ by $2^{j+1}$
gives the recurrence, and unrolling it gives the closed form. Each weight $2^{-(j-i)}$ with $i \ge j - m$ is at least
$2^{-m}$ and the other terms are nonnegative, which gives the window bound. G165's criterion is $R_j \to \infty$ because
on stage $j$ the ratio $p_k/k$ peaks at entry, where it equals $1/R_j$. Checked (`rule30_audit_g99_g100.py`, S74). The
entries 3, 8, 29, 400 were recomputed from RQ3's reached graphs rather than copied: they are the first node of least
period $q$ at $q = 2, 4, 8$, and the node after the single $q = 8$ cap exit at depth 399. At every depth the reached
states are temporal rotations of one another, so these prefixes are unbranched, as stated. The reached graphs at
$q \le 8$ are acyclic, each with one sink (its cap exit), so no history stays at a period of 8 or less. $R_j$,
$\lambda_j$, the recurrence and the closed form hold exactly on these entries. The closed form and the window bound also
hold on 200 random nonnegative schedules. The constant schedule $\lambda = 3$ from $R = 100$ gives exactly $3 + 97/2^j$,
and the alternating schedule meets both of G184's bounds. Depth 53208 follows G2.3's convention (zero driver at 53207,
split at 53208). One point of scope: if a history's period stopped doubling, $N_j$ would be undefined from some $j$ on
and $p_k = o(k)$ would hold trivially. G184's "exactly $R_j \to \infty$" therefore presumes unbounded period; at
$q \le 8$ that presumption is now checked. One consequence the record already gives: the shared prefix keeps period 16
through the split, so $N_5 \ge 53{,}208$ on every history. Hence $\lambda_4 \ge 3{,}300$ and $R_5 \ge 1{,}662$, lower
bounds rather than a value of $N_5$.

**GPT scope clarification after L146 (2026-10-07; existing theorem, no run).** The unbounded-period premise on an infinite ROOTED history is already proved in G165's equivalent period-growth checkpoint, using G7/G156. For completeness, a pair at depth k has first backward zero-hit time k+1 under B; therefore two distinct depths cannot have the same pair. If all periods were bounded by a fixed dyadic Q, all pairs would lie in the finite set of4^Q Q-periodic binary pairs, contradicting this injectivity along an infinite history. Rotation classes strengthen the same argument but are not needed. Ambient B-cycles such as G156's period-two example do exist; they are excluded by rooted first-hit times, not by a global acyclicity assertion. Thus every infinite admissible rooted history has all dyadic entries N_j, and no additional bounded-period cyclic rooted case remains to classify. This settles the scope question, not the growth rate. From the shared period16 prefix, the conservative reviewed bound N_5>=53208 implies lambda_4>=(53208-400)/16=6601/2 and R_5>=53208/32=6651/4; neither is the unknown exact entry. These are finite lower bounds, not asymptotic estimates.

*Local's correction (2026-10-07, L149).* Accepted. The scope point in my note above was already settled in the record: G165 proves unbounded period on every infinite rooted history, because by G156 the pair at depth $k$ first hits zero backwards at time $k + 1$, so no pair repeats. S74's acyclicity at $q \le 8$ is a special case. I should have searched the record before calling it open.

### G.GPT185. maximal difference order can return three edges after a doubling (second-read by Local, 2026-10-07)

### GPT G185 — Maximal difference order can return three edges after a doubling (2026-10-07)

**Symbolic counterlemma, second reader pending; no computation.** G161's temporal-difference addendum gives a useful stage-entry fact: odd zero-driver integration at least period q creates a profile of order q+1 and least period2q. That fact does not supply a slowly recovering order deficit. For every dyadic q>=4 there is an ambient gated compatible prefix whose new period2q stage reaches maximal difference order2q in three further spatial edges. One of those edges raises the maximum order of the pair by q-1. Rooted ancestry of this family is NOT established.

**Construction and entry.** Write temporal words in increasing time order, with S w(t)=w(t+1), Delta=I+S, and nu(w)=min{k>=0:Delta^k w=0}. Thus nu(0)=0 and nu(1)=1. On a2q-cycle take

    c = 0^(q-2) 1 0  1^(q-2) 0 1,
    a = Delta c,   e = 1 XOR S^(-1)c.

The second q-block of c complements the first, so a repeats every q letters. Its q-block has exactly three black cells, at q-3,q-2,q-1. Odd parity on a dyadic cap gives nu(a)=q and least period q: Delta^(q-1)a is constant1, whereas Delta^q a=0. Also Delta c=a gives nu(c)=q+1 and least period2q. These are the previously recorded integration identities, not a new stage-entry theorem. The compatible word prefix is

    a, 0, c, 1, e, f,

where f is the unique2q-periodic child of (1,e). Compatibility means S z=x XOR(y OR z) for three successive words x,y,z. The first triple is Delta c=a. For (0,c,1), constant1 satisfies the equation and c is a nonzero reset driver. For (c,1,e), S e=c XOR1. Finally f satisfies S f=1 XOR(e OR f), with a unique periodic solution because e has black reset cells. Choose arrival phase r=q-2 at the source (a,0); then a(r-1)=1. G160's gate is preserved along this prefix with the ordinary reset-clock updates. This certifies gated compatibility, without any root-start clock claim.

**Counting the last profile.** The cyclic white-run lengths of e are q-2,1,1, and its black-run lengths are the same. At a black e cell the recurrence forces the next f cell to0. Across a white e run of length ell, f alternates, starting at0, up to and including the next black e position. That disjoint interval contributes ceil(ell/2) black f cells. Hence one2q-block of f has weight

    (q-2)/2 + 1 + 1 = q/2 + 1.

For dyadic q>=4, q/2 is even, so this weight is odd. Consequently nu(f)=2q and f has least period2q. Shifts preserve nu, and adding the order-one constant to the order-(q+1) word cannot cancel its highest nonzero difference, so nu(e)=q+1. The successive pair maxima after the entry (0,c) are therefore

    q+1, q+1, q+1, 2q

at (0,c),(c,1),(1,e),(e,f). In particular the final edge raises that maximum by q-1, an unbounded jump as q grows. Rotating each pair to its actual arrival phase leaves these orders unchanged.

**Independent literal control, by substitution.** At q=4 the time-ordered words a,c,1,e,f on the cap8 are respectively01110111,00101101,11111111,01101001,01001010, or integer masks238,180,255,150,82 with time0 in the low bit. The q-block of a is0111. For the last triple e OR f=01101011 and S f=10010100, its complement, so the scalar equation holds. The orders are4,5,1,5,8, and f has three black cells. This is a hand substitution control independent of the general run-count argument; no census or measured run is reported. The q=2 case is excluded: its proposed q-2 run is empty and the evenness argument does not apply.

**Counterfactual and identified unexpected guard.** The assertion that every compatible edge raises the pair's difference order by at most one is false on the gated ambient domain. Only the zero-driver integration step has the recorded exact +1 relation. However, restoring maximal order does NOT end the stage: all three further pairs still have least period2q, their drivers are nonzero, and no next odd zero-driver event has been supplied. Thus this family neither realizes a short doubling-to-doubling stage nor refutes rooted period growth. It closes a blanket order-recovery shortcut, while leaving a root-specific restriction or a genuine bound on the distance to the next zero driver open.

**Existing record and next intention.** G161's difference addendum and G162 already separate order, period and reset cost; G178 retains order labels yet still loses actual adjacency. G184 identifies divergence of normalized stage delays as the missing growth statement. The present algebraic control adds no timing certificate, new experiment or prize claim. Next reasoning should use the actual zero-driver hitting condition along an admissible rooted history; an order deficit alone is insufficient on the larger compatible domain. Gap-1 refinement stays closed and Local's status-board contraction remains theirs.

*Second reader's note on G185 (Local, 2026-10-07; chat L147).* Correct, and at $q = 4$ more than claimed. The
construction checks out: $c$'s second $q$-block complements its first, so $a = \Delta c$ has period $q$ with block
$0^{q-3}111$. At a black $e$ cell the equation forces $S f = 1 \oplus 1 = 0$, and across a white run it reads
$S f = 1 \oplus f$, so $f$ alternates; the run count follows. Checked (`rule30_audit_g99_g100.py`, S75) at
$q = 4, 8, 16, 32, 64$ with $f$ taken as the single periodic child of $(1, e)$. The four triples are compatible. The
orders are $q, 0, q + 1, 1, q + 1, 2q$, with least periods $q$ for $a$ and $2q$ for $c, e, f$. $f$ has weight $q/2 + 1$,
and the pair maxima are $q + 1, q + 1, q + 1, 2q$. The three later pairs keep least period $2q$ with nonzero drivers,
and G160's gate holds at all five pairs from arrival phase $q - 2$ under the reset-clock updates. The $q = 4$ masks
match, with $f$ confirmed by brute force. On the excluded $q = 2$: $f$ still has order 4 (its weight is 1), so the order
conclusion survives there. What fails is the run-count formula and the gate at $(a, 0)$ from phase 0. Rooted ancestry at
$q = 4$ is established, not open. RQ3's reached $q = 8$ graph passes through this exact prefix at depths 28 to 32 by
consecutive edges, with arrival phases equal to G185's plus 5 on the 8-cycle. So the actual history enters period 8 at
$N_3 = 29$ and recovers order 8 three edges later, a jump of 3 on the edge from 31 to 32. Seven reached edges at $q = 8$
make that jump, the largest on the graph. The $q = 8$ member is not rooted in this way: the rooted cap exit at depth 399
has $a$-block $10000101$, not $00000111$. Beyond $q = 4$, rooted ancestry stays open, as G185 says.


**GPT incorporation of L147 (2026-10-07).** Local S75 independently verifies the family for q4 through64 and locates the q4 member on the rooted history at depths28 through32, with arrival phases shifted by5 on the cap8 cycle. Thus the rooted period8 stage starts at depth29 with order5 and reaches order8 at depth32; the stage continues through its zero-driver exit at depth399. Rootedness for the larger members remains unproved here; the q8 member is not the rooted cap16 exit word, as Local observes. At q2, direct substitution gives c=1001, a=1010, e=0011, f=0100, with f of weight1/order4. So the order conclusion survives, although the three-run proof degenerates. The stated arrival choice r=q-2=0 fails its gate since a(3)=0. The theorem retains q>=4; the q2 exclusion is not an assertion that maximal order fails to return. Local's verified filing is preserved.

### G.GPT186. arbitrarily good prefix depths suffice for the Thue–Morse and recorded paperfolding reductions (second-read by Local, 2026-10-07)

### GPT G186 — Arbitrarily good prefix depths suffice for the Thue–Morse reduction (2026-10-07)

**Conditional lemma, second-read by Local L151; reasoning only.** Fix one admissible rooted history and a fixed left-edge distance L. Let p(M) be its nondecreasing least common prefix period. Suppose its entire-prefix settling bound satisfies

    tau(M) <= gamma*M + A*p(M) + B,
    1 <= gamma < 3,  A >= 0,

with finite constants A,B along this history. Then liminf as M tends to infinity of p(M)/M equal to0 suffices for the unbounded Thue–Morse repeat contradiction of G2.4. A full limit p(M)/M ->0 is not required for this application. This supplies no actual growth or settling estimate for Rule30.

**Proof, including endpoint rounding.** Choose a fixed theta with 2<theta<6/gamma; then theta<6. Take integer depths n_s tending to infinity with p(n_s)/n_s ->0. Choose the largest nonnegative integer k_s for which M_s=ceil(theta*2^k_s)<=n_s, and put P_s=p(M_s). Such a k_s exists eventually and tends to infinity. Maximality gives

    n_s < ceil(2*theta*2^k_s) <= 2*theta*2^k_s + 1.

Monotonicity gives P_s<=p(n_s), hence P_s/2^k_s ->0. Also M_s=theta*2^k_s+O(1). The three G2.4 requirements now hold eventually: M_s<6*2^k_s because theta<6; tau(M_s)+P_s<=6*2^k_s because gamma*theta<6 and (A+1)*P_s+B+O(1)=o(2^k_s); and M_s>=L+2*2^k_s+2*P_s because theta-2>0. Substitution in G2.4's A⁗ inequality gives its one-cell contradiction at arbitrarily large scales. Every endpoint uses the settling bound and period from this SAME history. To exclude the code for every admissible left side, the assumptions must hold separately on every such history; constants may depend on the history.

**Stage-entry reformulation.** For the infinite rooted dyadic histories of G165, all entries N_j exist and p(M)=2^j for N_j<=M<N_(j+1). Write R_j=N_j/2^j as in G184. Then

    liminf_M p(M)/M = 0  if and only if  limsup_j R_j = infinity.

For the reverse implication, evaluate p(M)/M at entries N_j along an unbounded R_j subsequence. For the forward implication, a good depth n in stage j obeys N_(j+1)>n, so R_(j+1)>n/(2*p(n)); this is unbounded along the good-depth subsequence. Its stage indices tend to infinity because every fixed stage is finite. Thus, conditional on G165's uniform stage debt bound at slope gamma<3, unbounded R_j suffices for this Thue–Morse application: G165 supplies A=2*(C+1), with any fixed normalization offset absorbed in B. G165's stronger all-depth sublinear-period conclusion and G184's equivalence for a FULL limit remain unchanged.

**Independent margin control and counterfactual.** At gamma=5/2, theta=11/5 gives gamma*theta=11/2<6 and theta-2=1/5. Thus the time margin is half the dyadic scale and the endpoint margin is one fifth; both absorb any fixed B,L and vanishing relative period. If periods were not monotone, moving a good endpoint backwards could destroy its small period. The proof uses the reviewed predecessor-divisibility property, rather than assuming sparse depths align with repeat scales.

**Identified unexpected check: the weakened growth condition is strictly weaker.** This is an algebraic synthetic schedule, NOT a Rule30 history. Start N_1=2 and use the G184 recurrence R_(j+1)=(R_j+lambda_j)/2 with lambda_j=1 except at j_k=2^k, k>=1, where lambda_(j_k)=2^(2^(k-1)). Set each integer stage length to lambda_j*2^j. Immediately after a spike, R_(j_k+1)>=lambda_(j_k)/2, so limsup R_j=infinity. Before the next spike, at j=j_(k+1), the baseline contributes1 and the k earlier spikes contribute in total at most k*2^(-2^(k-1)): each contribution is bounded by 2^(3*j_h/2-j_(k+1))<=2^(-j_k/2). Hence R_(j_(k+1))->1. Consequently p(M)/M has liminf0 but does not tend to0, as evaluating at these latter entries shows. Unlike G184's previous oversized-deposit control, these deposits decay before the next spike.

**Prior record, scope and next intention.** G2.4 supplies the repeat criterion; G165 supplies conditional birth timing and monotone dyadic periods; G184 supplies the exact stage recurrence. This is an elementary subsequence application, with no literature novelty or computation claim. Neither the stage debt hypothesis nor even the weaker growth condition is proved on actual histories. No paperfolding claim or prize conclusion is added. Local: please second-read the endpoint selection, the equivalence and the strictness control; no run requested. GPT next seeks actual odd-zero hitting constraints strong enough to force unbounded R_j on each history.


**G186 continuation: the recorded paperfolding repeats also suffice (GPT, 2026-10-07; second reader pending, no run).** The initial G186 statement concerned only Thue–Morse. RULE30-PRIZE.md section8.59 also records paperfolding repeats with i=s, i'=3*s and ell=2*s-1 at dyadic scales s. Apply A⁗ to the same adjacent pair (-1,0) at distance L-1, with a=2*s, a'=6*s and n=2*ell=4*s-2. Its endpoint and one-cell contradiction requirements become

    M < 4*s,
    tau(M)+P <= 6*s,
    M >= L+2*s+2*P+2.

Indeed these give 4*s-2 <= L-1+6*s-M+2*P <= 4*s-3, impossible. The lost repeat symbol contributes the additional2 in the lower endpoint requirement; the later start contributes the stricter upper endpoint4*s, not6*s.

Under G186's SAME history-specific settling bound and liminf p(M)/M=0, choose theta with 2<theta<min(4,6/gamma). This interval is nonempty for 1<=gamma<3. The already proved endpoint selection gives M=ceil(theta*s), P/s->0 and arbitrarily large dyadic s. The strict positive margins 4-theta, 6-gamma*theta and theta-2 absorb all fixed offsets and the extra2. Thus the conditional sparse-depth criterion excludes the recorded paperfolding code as well as Thue–Morse. No new repeat theorem is proved here: the application uses exactly the recorded section8.59 repeats and A⁗, with the original timing/settled-band assumptions.

**Independent offset control and identified unexpected check.** Put L=1, s=8, P=1 and M=21, and assume tau(21)+1<=48. The upper endpoint is21<32, the lower threshold is1+16+2+2=21, and the A⁗ right side is1-1+48-21+2=29 whereas n=30, the desired one-cell contradiction. Reusing the Thue–Morse lower threshold would allow M=19, giving right side31 and NO contradiction. This literal arithmetic control retains the two-cell correction instead of treating the two repeat families as identical. No actual settling-time measurement is claimed by this assumed-timing control. The unresolved stage budget and actual unbounded stage-entry ratios remain necessary proof obligations for this route; no prize claim. Local: review the additional start-time and length offsets, no new job.

*Second reader's note on G186 (Local, 2026-10-07; chat L151).* Correct. The three requirements are exactly G2.4's
($M_k < 6 \cdot 2^k$, $\tau(M_k) + P_k \le 6 \cdot 2^k$, $M_k \ge L + 2^{k+1} + 2P_k$), and the third is also the upper
half of the A⁗ sandwich. Choosing $k$ maximal with $\lceil \theta 2^k \rceil \le n$ keeps the good depth below $2M + 1$,
since $n < 2\theta 2^k + 1$ and $M \ge \theta 2^k$. Monotone periods, from predecessor divisibility, then carry the
small period down to the endpoint, so $P/2^k \to 0$. The two margins are $6 - \gamma\theta$ for time and $\theta - 2$
for space, and both are fixed fractions of $2^k$ that absorb $A P + B$, $L$ and the ceiling. The equivalence follows
from $p/M = 1/R_j$ at entries and from $R_{j+1} > n/(2p(n))$ inside stage $j$. Checked (`rule30_audit_g99_g100.py`, S76)
at $\gamma = 5/2$, $\theta = 11/5$ on 300 random good depths. In the 134 cases where $P/2^k$ is small against $A$, $B$
and $L$, all three requirements and the sandwich hold with the settling bound taken at its worst. A slope with
$\gamma\theta = 6$ fails the time requirement, as it should. On the spike schedule the recurrence holds exactly, and
$R_{2^k + 1} \ge 2^{2^{k-1}}/2$ and $R_{2^{k+1}} \le 1 + k 2^{-2^{k-1}}$ for $k = 1$ to 4 ($R_{17} > 128$,
$R_{32} - 1 < 1/100$). So the weakened condition is strictly weaker, as stated. Beyond G186, the weakened condition has
an exact restatement: $\limsup R_j = \infty$ if and only if the normalized stage lengths $\lambda_j$ are unbounded,
since $\lambda_j/2 \le R_{j+1} \le \max(R_j, \lambda_j)$ (also checked in S76). The paperfolding continuation is also
correct. With §8.59's recorded repeat ($i = s$, $i' = 3s$, $\ell = 2s - 1$), A⁗ at $(-1, 0)$ has $a = 2s$, $a' = 6s$ and
$n = 4s - 2$. So $M < a' - a = 4s$, and the contradiction needs $M \ge L + 2s + 2P + 2$, the same offsets as BF4's
general form $L + 2i' - 2\ell$. S77 checks both thresholds exactly for $s = 2^3$ to $2^{20}$: one below the threshold
there is no contradiction, and $M = 4s$ breaks the first requirement. It also reproduces GPT's offset control (29
against 30 at $M = 21$, and 31 at the Thue–Morse threshold) and checks that $\theta = 11/5$ serves both families at
$\gamma = 5/2$. The quantifier stays per history, as in GC233. Rule 30's finite record cannot bear on a limsup.

### G.GPT187. a positive period/depth threshold suffices for both repeat reductions (second-read by Local, 2026-10-07)

### GPT G187 — A positive period/depth threshold suffices for both repeat reductions (2026-10-07)

**Conditional quantitative lemma, second-read by Local L152; no GPT run.** Fix a left-edge distance L and one admissible rooted history with nondecreasing common prefix period p(M). Suppose its entire-prefix settling bound is

    tau(M) <= gamma*M+A*p(M)+B,
    1 <= gamma < 3, A >= 0,

with finite constants A,B on that history. Define

    delta = (3-gamma)/(2*gamma+2*A+8).

Then liminf p(M)/M < delta suffices for G2.4's unbounded Thue–Morse repeat contradiction. For the recorded paperfolding repeats, the sufficient condition is liminf p(M)/M < min(delta,1/6). In G165's application A=2*(C+1)>=2, so delta<=1/7<1/6 and the SAME delta suffices for both codes. This complements G186: for a specified budget it weakens the sufficient growth condition. G186 remains useful when only existence of a finite budget constant is known. Neither lemma proves an actual budget or period estimate.

**Endpoint construction and proof.** Choose a number r strictly between the liminf and the relevant threshold. Along arbitrarily large integer depths n, let q=p(n)<=r*n. Put D=L for Thue–Morse and D=L+2 for paperfolding, and choose the largest dyadic s for which 2*s<=n-2*q-D. Such a scale exists eventually. Then

    s > (n-2*q-D)/4,
    M = 2*s+2*q+D <= n,
    P = p(M) <= q.

Thus s tends to infinity, and limsup along these chosen depths of q/s is at most 4*r/(1-2*r). Direct rearrangement shows

    r < delta  iff  4*r/(1-2*r) < (6-2*gamma)/(2*gamma+A+1).

Consequently

    tau(M)+P <= 2*gamma*s+(2*gamma+A+1)*q+gamma*D+B < 6*s

eventually, by a strict linear margin in s. For Thue–Morse, r<delta<=1/5<1/4 implies q/s<2 eventually, hence M<6*s. For paperfolding, r<1/6 implies q/s<1 eventually, hence M<4*s. All fixed D and B are absorbed by those strict margins.

For Thue–Morse, the G2.4 A⁗ right side is at most L-1+6*s-M+2*q=4*s-1, below its repeat-run length4*s. For paperfolding the same expression is4*s-3, below repeat-run length4*s-2. Both contradictions use exactly the repeats and timing hypotheses already recorded in G2.4 and G186's section8.59 continuation. To exclude either code for every admissible left side, this quantitative condition and the settling budget must hold separately on every such history, with history-dependent constants allowed.

**Exact dyadic stage interpretation.** In G165's rooted stage structure the last depth m_j=N_(j+1)-1 minimizes p(M)/M within stage j. Its value is

    p(m_j)/m_j = 1/(2*R_(j+1)-2^(-j)).

Every stage is finite and its index tends to infinity with depth. Thus taking the liminf of these stage minima gives the exact extended-real identity

    liminf_M p(M)/M = 1/(2*limsup_j R_j),

with 1/infinity=0 and 1/0=infinity. The vanishing subtraction2^(-j) does not affect the denominator's limsup; inversion exchanges positive limsup and liminf, including these limiting cases. Hence the displayed quantitative condition is equivalent to limsup R_j>1/(2*delta). The factor2 comes from using the END of a stage, just before the next doubling, rather than its entry. For G165 at gamma=5/2 and C=1, A=4 and delta=1/42. Entry ratios above21 by a fixed margin at arbitrarily large indices therefore suffice for BOTH repeat applications, conditional on that stage budget. No such actual asymptotic statement is established.

**Independent integer control.** Hypothetically take L=1, B=0, gamma=5/2, A=4, n=1000 and q=16. For paperfolding D=3; the selected s is256 and M=547. The assumed bound gives tau(M)+P<=1447.5<1536=6*s, and M<1024=4*s. The A⁗ right side is at most1021 against repeat-run length1022. The same endpoint also works for Thue–Morse, whose run length is1024. This verifies the arithmetic under the stated assumptions; it is NOT a settling measurement or a certified C=1 budget on a Rule30 history.

**Identified unexpected strictness/control check.** If q/s equals (6-2*gamma)/(2*gamma+A+1), the scale-dependent time margin vanishes. A positive gamma*D+B then prevents the required timing inequality: this argument cannot replace its strict threshold by a non-strict one. Moreover the synthetic schedule N_j=25*2^j has constant R_j=25 and integer stage lengths25*2^j; it satisfies the gamma=5/2,C=1 entry threshold while p(N_j)/N_j=1/25 never tends to0. Its stage-end ratios tend to1/50. At period16, the entry depth400 has ratio1/25 above1/42, but the last stage depth799 has ratio16/799 below1/42. Thus G186's unbounded-ratio condition is sufficient but not necessary for the conditional application. This schedule has no asserted Rule30 compatibility.

**Prior record and next intention.** This is a quantitative endpoint selection using reviewed G165 timing, G184 stage notation and the pending G186 repeat applications; no novelty or computation claim. A finite large entry such as the conservative N_5 lower bound does not establish arbitrarily many useful scales. The actual target can now be a history-specific positive period/depth threshold tied to its stage-debt constant, rather than unbounded R alone. Both linked obligations remain open. Local: please second-read the threshold algebra and scope, together with G186; no run requested. GPT next examines what actual odd-zero hitting constraints could maintain or recurrently recover such a threshold.


**G187 continuation: align the repeat scale with the dyadic period (GPT, 2026-10-07; second reader pending, no run).** The general sparse-depth threshold is sufficient but can lose room by treating periods as arbitrary integers. In G165's actual stage structure, let q=2^j and choose a FIXED power of two K with

    K > (2*gamma+A+1)/(6-2*gamma).

For the paperfolding application also require K>1. With G165's A=2*(C+1)>=2 and gamma>=1, the displayed fraction is at least5/4, so its smallest admissible dyadic K automatically meets this additional requirement. Then

    limsup_j R_j > K+1

suffices for both repeat contradictions, conditional on that same history's settling budget. At infinitely many stages the next entry obeys N_(j+1)>2*(K+1)*q+D, where D=L for Thue–Morse or L+2 for paperfolding, because the limsup inequality has a fixed positive margin and q tends to infinity. Set s=K*q (a valid dyadic repeat scale) and M=2*(K+1)*q+D. Since M<N_(j+1), its common prefix period P is at most q, whether M falls in the q-stage or an earlier stage. The settling bound gives

    tau(M)+P <= [2*gamma*(K+1)+A+1]*q+gamma*D+B < 6*K*q = 6*s

eventually. The strict coefficient gap is (6-2*gamma)*K-(2*gamma+A+1)>0. Also M<4*s eventually when K>1, hence the paperfolding upper endpoint holds; this also implies the Thue–Morse upper endpoint M<6*s. Both lower endpoints and the one-cell contradictions follow from the same M=2*s+2*q+D construction in G187. This proves the claim without assuming liminf period/depth zero, or measuring any new stage length.

**Independent coefficient control and identified unexpected comparison.** For the hypothetical gamma=5/2,C=1 budget, A=4 and the coefficient fraction is10. Choose K=16; the sufficient entry threshold is now17 rather than G187's general21. At q=16,L=1,B=0 the paperfolding endpoint is again M=547,s=256, and the timing margin is6*q-7.5=88.5, agreeing with the earlier literal control. A synthetic constant schedule N_j=18*2^j has R_j=18 and stage-end period/depth ratios tending to1/36. It passes this new threshold but fails the earlier sufficient condition liminf period/depth<1/42. Thus the improvement is strict as a reduction; no Rule30 compatibility or actual C=1 budget is asserted. Choosing K=8 instead would give a negative coefficient gap8-10=-2, so the next smaller dyadic scale is not licensed by this bound. If the fraction itself is a power of two, equality still leaves no positive margin for offsets: choose the next power. No optimality claim is made for other endpoint strategies or stronger timing information.

**Handoff.** This is a refinement of the same pending G187 proof, not a new growth estimate or a reopened gap-1 family. Local: include the dyadic scale choice and the earlier-stage prefix-period guard in the second read; no job requested. The remaining actual obligation is a recurrent entry-ratio margin linked to the history's uniform stage-debt constant. Finite large entries alone still supply no such recurrence.

*Second reader's note on G187 (Local, 2026-10-07; chat L152).* Correct. With $M = 2s + 2q + D$ the third G2.4
requirement holds with $q$ in place of $P$, and $P \le q$ by monotone periods. The time requirement then reduces to
$(2\gamma + A + 1) q < (6 - 2\gamma) s$, up to the fixed $\gamma D + B$. Taking $s$ maximal and dyadic gives $q/s$ at
most $4r/(1 - 2r)$ in the limit. Cross-multiplying, $4r/(1 - 2r) < (6 - 2\gamma)/(2\gamma + A + 1)$ is
$r(4\gamma + 4A + 16) < 6 - 2\gamma$, which is $r < \delta$. The two codes differ only in $D$, and in paperfolding's cap
$M < 4s$, which $r < 1/6$ secures; $\delta \le 1/7$ once $A \ge 2$. Within a stage $p/M$ falls until the last depth,
where it equals $1/(2R_{j+1} - 2^{-j})$, so the liminf is $1/(2 \limsup R_j)$. Checked (`rule30_audit_g99_g100.py`,
S78). The equivalence holds on a rational grid. On 400 random depths the construction reaches both contradictions
whenever $r < \delta$ (800 of 800), and at $r = 3\delta$ its time margin fails (200 of 200). S78 also covers GPT's
integer control, the strictness case, the stage-end identity on random schedules and the $25 \cdot 2^j$ schedule.
Against the record, at $\gamma = 5/2$ and $C = 1$ ($\delta = 1/42$, so entries above 21): RC2's exact finite budget, a
debt of 7 at $q = 8$ (S72), lies within $Cq$ with $C = 1$ through period 8. The recorded entry $R_4 = 25$ and the bound
$R_5 \ge 1{,}662$ both exceed 21, and the stage ends $8/399$ and at most $16/53{,}207$ lie below $1/42$. That is finite
evidence about two scales and proves nothing about arbitrarily large ones, as G187 says. The dyadic refinement is also
correct. With $K$ the least power of two above $(2\gamma + A + 1)/(6 - 2\gamma)$, the endpoint $s = Kq$,
$M = 2s + 2q + D$ lies before the next entry, so $P \le q$, and the coefficient gap $(6 - 2\gamma)K - (2\gamma + A + 1)$
is positive while at $K/2$ it is not. Since the fraction is at least 5/4 once $A \ge 2$, $K \ge 2$ gives paperfolding's
$M < 4s$ (S79, with GPT's control: fraction 10, $K = 16$, threshold 17, margin 88.5). At $C = 1$ the record's $R_4 = 25$
clears this threshold too.

### G.GPT188. a doubled stage of period at least four cannot return to zero within eleven steps (second-read by Local, 2026-10-07)

### GPT G188 — A doubled stage of period at least four cannot return to zero within eight steps (2026-10-07)

**Local zero-return lemma, second reader pending; symbolic, no run.** Consider an odd zero-driver integration that doubles period from q/2 to q>=4. Write its following compatible temporal profiles as

    0, c, 1, e, f, g, h, i, ...,

with S w(t)=w(t+1), Delta=I+S over binary XOR, and T=S^(q/2). Integration gives T c=1+c. Then none of profiles at positions1 through8 after the displayed initial zero can be identically zero. Thus the first subsequent zero is at position at least9. On a rooted history, every stage entered by doubling to q>=4 has length at least9. This is a CONSTANT bound; it gives no positive lower bound on normalized stage length as q grows.

**The first six positions.** The reset equations force the next profile to1 and S e=1+c, equivalently e=1+S^(-1)c. G159's direct six-position calculation applies because the pre-integration source Delta c has least period q/2>=2 and is nonconstant. Its only earlier-zero exception would require that source to be constant1. Therefore c,1,e,f,g,h are nonzero. This uses the already reviewed local proof, not its even-branch hypothesis: nonconstancy excludes the same exception here.

**Position7 cannot be zero.** If i=0, compatibility forces g=h. The equations for g and h then give S g=f+g and e=f*g (pointwise product). Since e is contained in f, the f equation reduces to S f=1+f. Thus f alternates, g integrates that alternating word, and g is a rotation of0011 repeated. The word e=f*g has exactly one black cell per four positions. Therefore c=1+S e has least period4 and three black cells per four positions. But an entry word c of least period q with complementary q/2 halves has exactly q/2 black cells. Here q must be4 and the required weight is2, contradicting3.

**Position8 cannot be zero.** Suppose the profile after i is0; then h=i. The equations for h and i give g=Delta h, and comparison with the h equation gives f=g*h. Since f is contained in g, the g equation gives e=Delta g=Delta^2 h. Put x=h(t), y=h(t+1), z=h(t+2). The f equation reads

    y*(1+z) = 1 + [(x+z) OR x*(1+y)].

Its allowed triples are001,010,011,100,101. No periodic or bi-infinite word satisfying these constraints can contain11: both110 and111 are forbidden. Hence011 is also absent, and h has no adjacent ones and no three consecutive zeros. The shifted word T h has the same two properties.

Now beta=h+T h obeys Delta^2 beta=1, because e+T e=1 follows from c+T c=1. Thus beta(t+2)=1+beta(t): beta is a rotation of0011 repeated. Choose a phase with five successive beta bits11001. At the second position, h and T h differ; absence of adjacent ones forces their common bit at the third position to0. At the fifth position they also differ, forcing their common fourth-position bit to0. Absence of000 now forces BOTH second-position bits to1, a contradiction. This excludes position8.

**Independent literal control and identified unexpected exception.** The seven-step compatible zero return

    a=0110, 0, c=1101, 1=1111, e=0001,
    f=0101, g=0011, h=0011, 0

uses increasing temporal order on cap4. Direct substitution gives Delta c=0110, S e=0010=1+c, S f=1010=1+(e OR f), S g=S h=0110, and the last equal pair produces0. It has an EVEN pre-integration source and no complementary halves in c, so it does not refute the lemma. Rootedness of this control is not asserted. The q=2 exception is essential: the compatible prefix0,01,11,01,01,0 returns to zero in five steps after constant-one integration, as already recorded in G159. The new assertion keeps q>=4. These literal checks independently guard against extending the result to all zero-driver events or to the smallest doubling.

**Prior record and scope.** G157-G159 supply reset, integration and the six-position guard; G185 shows difference order can recover rapidly without ending a stage. The present short-return exclusion uses actual compatibility and complementary temporal halves, rather than an autonomous order or half-difference model. Neither rooted reachability of the control nor attainment at position9 is claimed. The bound9/q tends to0: this result does NOT establish the unbounded normalized lengths of G186/L151, or the budget-linked recurrent thresholds of G187. No literature novelty, computation or prize claim. Local: please second-read the two return equations, especially the five-position beta contradiction; no job requested. Next useful task is whether longer return constraints yield a period-dependent obstruction, rather than extrapolating this constant bound.


**G188 continuation: positions9 and10 are also impossible (GPT, 2026-10-07; second reader pending, hand algebra only).** These two exclusions require only a nonzero initial c, which forces the following profile to1; they do not require complementary halves. Together with the initial G188 argument, a period-doubling entry of least period q>=4 has no subsequent zero in positions1..10, so its first return and its stage length are at least11. This remains a constant bound, not a normalized-stage estimate.

Define, for three consecutive bits x,y,z of a temporal word w,

    E(x,y,z) = x+y+z*(1+x)*(1+y),

where additions are XOR and products are AND. In the order000,001,010,011,100,101,110,111, its values are0,1,1,1,1,1,0,0. This function arises directly by eliminating the four profiles before a repeated pair (w,w): they are E(w), Delta^2 w, w*Delta w, Delta w, followed by w,w. Here E(w)(t)=E(w(t),w(t+1),w(t+2)). Indeed the closest equations first give Delta w, then w*Delta w, then Delta^2 w, and the next gives S(w*Delta w)+(Delta^2 w OR w*Delta w)=E(w).

**Return at position9.** In 0,c,1,e,f,g,h,i,j,0, the repeated pair i=j=w forces h=Delta w, g=w*Delta w, f=Delta^2 w and e=E(w). The remaining equation for f is

    S(Delta^2 w) = 1 + (E(w) OR Delta^2 w).

For x=w(t), y=w(t+1), z=w(t+2), v=w(t+3), this fixes v uniquely. The resulting triple-state transitions are

    000 -> 001 -> 010 -> 101 -> 010,
    011 -> 111 -> 110 -> 101,
    100 -> 000.

These lines include all eight states. The only cycle is010 <->101, so every periodic w satisfying the equation alternates. Then e=1 and c=1+S e=0, contradicting the nonzero entry. Merely finding a cycle of the necessary temporal map is insufficient: the entry condition must still be checked.

**Return at position10.** In 0,c,1,e,f,g,h,i,j,k,0, the repeated pair j=k=w instead forces i=Delta w, h=w*Delta w, g=Delta^2 w and f=E(w). With e=S g+(f OR g), the remaining f equation reduces to

    if E(x,y,z)=1: E(y,z,v)=0;
    if E(x,y,z)=0: E(y,z,v)=1+x+y+z+v.

Its ONLY allowed triple-state edges are

    011 -> 110 or111,  111 -> 110,  110 -> 100,  100 -> 000.

State000 has no outgoing edge; states001,010,101 likewise have none. This graph has no cycle, so no periodic temporal word can satisfy the return equation. In fact it has no infinite path, even without periodicity. This excludes position10.

**Independent substitution controls and identified unexpected fragment check.** At state000 the position9 equation forces v=1 because E=0 and Delta^2 w=0; at state111 it forces v=0 for the same reason, reproducing the two easily confused endpoints of the first table. At state011 the position10 equation admits both v values because E=1 while E(1,1,v)=0; at state000 it admits neither because it would require v=1+v. The finite fragment0111000 obeys four successive position10 constraints (edges011->111->110->100->000), yet cannot continue even one more bit. A short temporal window can therefore mimic the return condition without defining a compatible periodic profile. No finite fragment is counted as a return certificate. These are direct Boolean substitutions independent of the cycle inspection, not a computational job or a new measured census.

**Scope and handoff.** The argument uses the same backward pair equations as G7/G159, with all word products and shifts retained. It supplies two additional local exclusions; no attainment at11, period-dependent return bound, rooted control example or prize claim follows. Local: include these two tables and the nonzero-entry guard in G188's second read, no run requested. The normalized lower bound11/q still tends to0; whether longer constraints force a growing obstruction remains open.


**G188 continuation: return11 has an odd-period cycle, so cannot follow doubling (GPT, 2026-10-07; second reader pending, hand algebra only).** Retain E(x,y,z)=x+y+z*(1+x)*(1+y), and define H(x,y,z)=(x+y) OR (y+z), equal to0 exactly at000 and111. Four profiles before a repeated pair were eliminated in the previous continuation. One further backward step gives

    F(x,y,z,v)=y+v+H(x,y,z).

For a putative return0,c,1,e,f,g,h,i,j,k,l,0, the last equal pair k=l=w therefore forces j=Delta w, i=w*Delta w, h=Delta^2 w, g=E(w), f=F(w), and e=S E(w)+(F(w) OR E(w)). Its remaining f equation simplifies to

    S F(w) = 1 + (F(w) OR Delta E(w)).

For consecutive w bits x,y,z,v,u, it determines the next bit uniquely:

    u = z + H(y,z,v) + 1
        + [F(x,y,z,v) OR (E(x,y,z)+E(y,z,v))].

The resulting four-bit-state successors, in increasing binary order0000 through1111, are

    0001,0011,0100,0111,1000,1011,1100,1111,
    0000,0010,0100,0111,1001,1011,1100,1110.

Every state feeds the SINGLE cycle

    0000 -> 0001 -> 0011 -> 0111 -> 1111 -> 1110
         -> 1100 -> 1001 -> 0010 -> 0100 -> 1000 -> 0000.

Hence a periodic w satisfying the equation has least period11. The reconstructed preceding profiles are all11-periodic. In particular c cannot have the even least period created by odd integration: its period divides11. For a rooted dyadic stage, there is also the direct check that w cannot be both11-periodic with least period11 and q-periodic for a power of two q. No earlier zero occurs through position10 by the preceding exclusions, so reset uniqueness indeed keeps all these profiles within the entry period until this putative return. Thus position11 is excluded. Combined with G188's earlier parts, the first subsequent zero and the stage length after doubling to q>=4 are at least12. This is still a constant bound.

**Independent cycle-word control and identified unexpected ambient return.** Reading the cycle gives the cyclic temporal word w=00001111001. Its four-bit windows reproduce exactly the eleven cycle states above. It has five black cells and, since11 is prime and the word is nonconstant, least period11. At window0000 the formula has E=F=S E=0, so e=0; at window0111 it has E=F=1 and S E=0, so e=1. Therefore c=1+S e is nonconstant and of least period11. Backward reconstruction consequently DOES produce a compatible ambient return at position11 with a nonzero entry; its pre-integration source Delta c has even block parity. This guards against claiming that the return equation has no compatible solutions. What fails is period-doubling ancestry, not compatibility. Neither this odd-period ambient return nor its gate/root reachability is asserted to belong to the rooted tree. The table and these controls are Boolean proof calculations, not a computed census or a requested Local run.

**Next obligation.** This continuation identifies an actual domain countercontrol while extending only a fixed local exclusion. The lower bound12/q still vanishes. No rule for arbitrary return lengths, period-dependent obstruction, recurrence of large normalized stages, or prize conclusion is established. Local: include the successor list, single cycle and odd-period scope check in G188's second read; no new job.

*Second reader's note on G188 (Local, 2026-10-07; chat L153).* Correct, with its continuation. Checked
(`rule30_audit_g99_g100.py`, S80) exhaustively at $q = 4, 8, 16$. After every odd doubling (every odd $q/2$-source, both
integration children, each with $Tc = 1 + c$), no profile at positions 1 to 11 is zero. Positions 9 and 10 need only a
nonzero $c$, as the continuation says. At every cap from 2 to 12, for every nonzero $c$ and every branch, position 2 is
$1$ and positions 9 and 10 are nonzero. GPT's $E$ table, the position-9 transitions (whose only cycle is
$010 \leftrightarrow 101$), the five position-10 edges (no cycle) and position 8's allowed triples were rebuilt by brute
force over bits. Both literal controls substitute correctly. The return-11 continuation is also correct (S81). The
successor rule reproduces GPT's sixteen entries, and every state feeds the one 11-cycle, whose word is $00001111001$.
Backward reconstruction from it gives a compatible return at position 11 at cap 11, nonzero throughout and with an
even-parity source, and the forward walk reproduces it. Among caps 2 to 13, a first zero at position 11 occurs only at
cap 11. The rooted $q = 16$ stage, followed forwards from the $q = 8$ cap exit $(161, 0)$, first returns to zero 52,808
steps later, at depth 53,207, with an even driver. That is G2.3's genuine split, replayed a third way. The constant is
far from sharp. An exploratory enumeration that was not preregistered (`rule30_g188_returns.py`) gives the earliest
first return after any odd doubling as 21 at $q = 4$, 88 at $q = 8$ and 6,343 at $q = 16$. In units of $q$ that is 5.25,
11 and about 396. Sixteen walks at $q = 16$ show no zero within 200,000 steps. These are descriptive numbers for three
periods, not a bound, and they cover the ambient domain, which contains every rooted history.

### G.GPT189. odd zero returns require logarithmic delay in the entry period (second-read by Local, 2026-10-07)

### GPT G189 — Odd zero returns require logarithmic delay in the entry period (2026-10-07)

**Odd-return period bound, second reader pending; symbolic, no run.** Let compatible periodic profiles start with0,c,1, where c is nonzero of least period q. Suppose the first subsequent identically zero profile occurs at an ODD position r=2k+3, counting the initial zero as position0. Then

    q <= 2^k; equivalently r >= 2*log2(q)+3.

This applies to a doubled dyadic stage when its first zero return is odd. It does not assert that first returns are always odd, or that logarithmic delay supplies the normalized growth required by G186/G187.

**Prediction and counterfactual before the hand checks.** The backward profile functions at even indices should be affine with coefficient1 in their newest temporal bit, so a constant-one condition determines that bit. At odd indices this coefficient can vanish. The counterfactual that every return constraint is deterministic should fail at G188's return10 branch. The controls below check these three claims without a census or computational job.

**Backward functions and their temporal support.** At the final zero the preceding two profiles must be equal; call them w,w. Define U0(w)=U1(w)=w and, for n>=0,

    U_(n+2)(w) = S U_n(w) + (U_(n+1)(w) OR U_n(w)).

Here S w(t)=w(t+1), addition is XOR, and OR is pointwise. This is exactly the compatibility equation solved for the preceding profile, not a model that drops its background. By induction, U_(2j) and U_(2j+1) depend only on bits w(t)..w(t+j). Moreover

    U_(2j)(w)(t) = w(t+j) + A_j(w(t),...,w(t+j-1))

for a Boolean function A_j (A0=0). For the induction step, S U_(2j) has the new bit w(t+j+1) with coefficient1; the OR term in U_(2j+2) depends only on bits through t+j and cannot cancel it. The odd function U_(2j+3) has support through t+j+1, because it is S U_(2j+1) plus an OR term on that same support. This proves both support and affine claims.

In a return of length r, the profile at position2 is U_(r-3)(w), and the entry at position1 is U_(r-2)(w). Thus odd r=2k+3 forces U_(2k)(w)=1. For k>=1 this fixes

    w(t+k) = 1 + A_k(w(t),...,w(t+k-1)).

The k consecutive bits are therefore a state of a deterministic shift map with2^k states. Because w is periodic, its state sequence is a directed cycle, of length P<=2^k. Its temporal word repeats with period P. Every reconstructed profile, including c=U_(r-2)(w), also repeats with P, since these functions commute with time shift. Hence the least period q of c divides P and q<=2^k. For k=0, U0(w)=1 gives w=1 and q=1, yielding the same bound directly. No root reachability assumption is needed for this necessary bound.

**Independent literal and formula controls.** The first functions are U2=Delta w, U3=w*Delta w and U4=Delta^2 w, where Delta=I+S. Thus the r=5 equation fixes w(t+1)=1+w(t), and the r=7 equation fixes w(t+2)=1+w(t), matching G188's alternating and0011 cycles. The literal first return0,01,11,01,01,0 has q2,r5 and meets the bound exactly. Direct forward substitution checks its four interior triples: the right-hand sides are11,10,10,00, respectively, equal to the shifted children. Its preceding source is constant1, so this also guards the essential q2 exception in G188. The ambient r7 control there has entry1101 of least period4 and also meets the bound exactly, but is not an odd-source doubling. G188's ambient r11 entry has period11<=16, consistent with the bound and inconsistent with a blanket dyadic claim for ambient histories.

**Identified unexpected check: even returns retain branching.** U3(x,y)=x*(1+y) is independent of y when x=0, so the even-index induction does not extend to all U_n. More directly, G188's actual r10 condition admits BOTH next bits from state011, even though its full graph has no periodic cycle. This prevents replacing the even return condition with a deterministic map on the same states. For a nondeterministic graph, a periodic word can revisit states before its least temporal period: even the full binary shift admits words0^(m-1)1 of arbitrary least period m on a fixed finite state graph. That abstract control is not a compatible Rule30 return. It only shows why counting states alone is insufficient for the even case.

**Existing record, scope and next obligation.** This generalizes the deterministic odd-return maps of G188 using the backward identity already present in G7/G159. Finite deterministic maps and their cycle bounds are standard; no literature novelty is claimed. The result is a parity-restricted necessary logarithmic delay, not a growing normalized delay: log2(q)/q tends to0. Even first returns, ancestry restrictions and recurrence of large normalized stage lengths remain open. Local: please second-read the support induction, r-3 indexing and least-period divisibility; no new job or larger cap requested. The saved return12 calculation remains unpublished rather than supplying another fixed-bound increment.

*Second reader's note on G189 (Local, 2026-10-07; chat L154).* Correct. Solving each compatibility triple for its first
profile gives $U_{n+2} = SU_n + (U_{n+1} \lor U_n)$ from the final pair $(w, w)$, so $U_n$ is the profile at position
$r - 1 - n$. Hence position 2 is $U_{r-3}$ and the entry is $U_{r-2}$, as stated. In the induction, $SU_{2j}$ carries
$w(t + j + 1)$ with coefficient 1 and the OR term stops at $t + j$, so $U_{2j+2}$ is affine in its newest bit. A
periodic word driven by a deterministic $k$-bit map lies on one cycle of length $P \le 2^k$, so $w$, and with it every
shift-commuting profile, has period $P$, and the entry's least period divides $P$. Checked (`rule30_audit_g99_g100.py`,
S82). The backward functions were computed directly on all words of length 9: for $n \le 12$ the support and affine
claims hold, and $U_2 = \Delta w$, $U_3 = w\,\Delta w$, $U_4 = \Delta^2 w$. On actual walks, every nonzero $c$ at caps 2
to 11 whose first zero falls at an odd position $r = 2k + 3$ has least period at most $2^k$. The bound is exact at
$r = 5$ and $r = 7$ and loose from $r = 11$ on. The even case is not merely unproved: at cap 12 an even first return at
$r = 8$ has an entry of least period 12, far above what the odd bound would allow at that length, so an even-return
obstruction must use the doubling structure, as G188's position-8 argument does.

### G.GPT190. even returns as paths between swapped temporal halves (second-read by Local, 2026-10-07)

### GPT G190 — Even returns as paths between swapped temporal halves (2026-10-07)

**Exact ambient reformulation, second reader pending; hand proof, no run.** Fix an even return position r=2m+2>=4 and a dyadic target period q=2^j>=2; put h=q/2. There is a compatible q-periodic prefix0,c,1,...,w,w,0 returning to zero at position r, entered by odd integration from least period h, if and only if the finite paired-window graph below has a path of length h from some vertex v to its swapped vertex sigma(v). The return need not be FIRST, and no root reachability or growth bound follows.

**Prediction and counterfactual.** The affine newest-bit identity of reviewed G189 should fix the XOR of the two appended bits, leaving up to two candidates before filtering. The counterfactual that complementarity alone fixes BOTH bits is false. The exact path construction must also force least period q, not merely a representation on cap q; the nondyadic guard below checks this obligation.

**Graph definition retaining the full background.** Use G189's exact backward functions U0=U1=w and

    U_(n+2)=S U_n+(U_(n+1) OR U_n).

For m-bit windows X, let F_m(X) be U_(2m-1), which uses only those m bits. Write

    U_(2m)(w)(t)=w(t+m)+A_m(w(t),...,w(t+m-1)).

Vertices are pairs v=(X,Y) with F_m(X)=F_m(Y)=1. An edge appends bits b,b', drops the oldest bit of each window, and requires both the new vertex condition and

    b+b'=1+A_m(X)+A_m(Y).

All additions are XOR. There are at most4^m vertices and at most two outgoing candidates before the new vertex test. Swapping X,Y and b,b' preserves every condition, so sigma is a graph symmetry. This stores the actual backward functions, including their OR backgrounds; it is not an autonomous difference-order approximation.

**Necessity.** In the stated prefix the final zero forces its preceding profiles equal to w. Backward reconstruction places U_(2m-1)=1 at position2 and U_(2m)=c at position1. Since w is q-periodic and c(t+h)=1+c(t), its paired windows X(t) and Y(t)=X(t+h) obey the edge equation. After h shifts their order is swapped. Thus they supply the required length-h path. In particular an actual FIRST even return after doubling to q satisfies this condition: reset uniqueness keeps its profiles q-periodic until that return.

**Sufficiency and overlap audit.** Given v0->...->v_h=sigma(v0), follow it by its swapped copy. This is a closed walk of length2h=q. Extend it periodically in both time directions. The shift-and-append edges make the first windows consistent with a temporal word w, even if h<m; closed-window consistency handles overlapping indices. The second window at time t is the first window at time t+h, because the second half of the walk is the swapped first half. Define c=U_(2m)(w). The edge equation gives c(t+h)=1+c(t), and the vertex equation gives U_(2m-1)(w)=1.

All reconstructed profiles have period dividing q. Since q is a power of two, every proper divisor of q divides h. Hence c's complementary halves force its least period to be EXACTLY q. Its source a=Delta c is h-periodic, and its h-block parity is

    XOR_(t=0)^(h-1) a(t)=c(0)+c(h)=1.

A smaller period dividing h would repeat an even number of times in the h-block, contradicting that odd parity. Thus a has least period h. This is genuinely odd period-doubling integration, rather than the balanced same-period control of GC244.

Backward reconstruction supplies every interior compatibility triple and the final triple(w,w,0). At the other end, U_(2m+1)=S1+(c OR1)=0, so the initial zero is also correct. If an earlier zero appears, it is part of this compatible q-periodic prefix; the construction makes no first-return claim. Its first return is at most r. Arrival-clock gates and rooted ancestry are not supplied by this ambient statement.

**Independent boundary control and identified unexpected nondyadic check.** At r4, m1, F1=w forces both windows to1. Then A1(X)=X=1, so the complementary edge needs b+b'=1, whereas new vertices force b=b'=1. The graph has no edge, consistently excluding this return. GC244's literal balanced cap8 return8 satisfies the constant-one reconstruction but fails c(1)+c(5)=1; the paired condition rejects precisely what scalar balance admitted. Its eight forward triples were independently verified by Local S83, L155.

The dyadic assumption in the least-period conclusion is essential: c=010101 on cap6 has c(t+3)=1+c(t), yet least period2 and source Delta c=111111 of least period1. This is a word-level countercontrol, not an asserted even-return graph path. An ordinary closed walk alone does not certify primitive period; dyadic complementarity supplies that extra conclusion here.

**Record, prior method and limitations.** G7/G159 supply backward compatibility; G188 supplies short-return languages and the complementary-half guard; G189 supplies exact support and affine functions. The record already uses standard finite-window path graphs for precursor blocks (G127); no novelty is claimed for that representation or for closing a path with its swapped copy. The new application retains the exact doubling domain for even returns. Neither candidate branching nor a state count establishes recurrent branching, a period-dependent delay, uniform normalized growth or a prize result. Local: please audit the overlap closure, initial-zero indexing and dyadic least-period/source-parity steps; no census or larger run requested. Next reasoning concerns the recurrent part of this paired relation, not fixed-position table extensions.

*Second reader's note on G190 (Local, 2026-10-07; chat L156).* Correct. The vertex test is G189's $U_{2m-1} = 1$ read on
each window. The edge equation is $c(t) + c(t + h) = 1$ written through G189's affine form of $U_{2m}$. A path of length
$h$ from $v$ to $\sigma(v)$, followed by its swap, is a closed walk of length $q$, so it is the same thing as a
$q$-periodic word with both properties. The three steps GPT asked about hold. Overlap closure needs only that
consecutive first windows shift by one bit, which the edges enforce whatever the size of $h$ against $m$. The initial
zero is $U_{2m+1} = S1 + (c \lor 1) = 0$. At dyadic $q$ every proper divisor divides $h$, so complementary halves force
least period $q$, and the source's odd $h$-parity forces its least period $h$. Checked (`rule30_audit_g99_g100.py`,
S84). With the graph built from its definition (1, 1, 25, 25, 225 and 1,089 vertices for $m = 1$ to 6), there is no swap
path and no doubling-entered return for $q = 2$ to 16. The positive direction was checked on the two actual even first
returns after odd doublings: $q = 8$ at $r = 88$, and the rooted $q = 16$ at $r = 52{,}808$. Both equal the backward
reconstruction at every position, with $U_{r-3} = 1$, complementary halves, the initial zero, least period $q$ and an
odd source of least period $q/2$. The $q = 8$ return also traces a length-4 swap path in the graph built from the
definition at $m = 43$, the overlap case $h < m$. In both actual cases $m$ is much larger than $h$ (43 against 4, and
26,403 against 8), so the paths are short and the windows long.

### G.GPT191. dyadic swap paths have an eventual dichotomy (second-read by Local, 2026-10-07)

### GPT G191 — Dyadic swap paths have an eventual dichotomy (2026-10-07; second reader pending)

**G190 continuation: dyadic swap paths are eventually all present or all absent (GPT, 2026-10-07; second reader pending).** This is a finite-graph lemma applied to the independently verified G190 construction. No component of an actual return graph was enumerated or classified, and no new computation ran.

Let a finite directed graph have n vertices and an involutive automorphism sigma. Call q=2^j, j>=1, admitted when a path of length q/2 joins some v to sigma(v). Then exactly one of these alternatives holds:

    every sufficiently large dyadic q is admitted;
    every admitted dyadic q satisfies q<=n.

The first alternative holds exactly when a sigma-invariant strongly connected component with a positive cycle has power-of-two cycle gcd g and sigma preserves its cyclic classes. A strongly connected component is a set of vertices mutually reachable by directed paths. Its cycle gcd is the greatest common divisor of its positive closed-walk lengths; its g cyclic classes advance by one class on every edge.

**Prediction and counterfactual before the hand controls.** The involution should restrict its cyclic-class shift to zero or half a cycle. Thus dyadic admissions should become constant, rather than alternate forever with j. The counterfactual that arbitrary closed walks suffice should fail when the swap exchanges disconnected components. The literal graphs below check these distinctions independently of the general argument.

**Component and phase proof.** An admitted path followed by its swapped copy is a closed walk of length q, lying in a sigma-invariant strongly connected component C. Thus g divides q, so g=2^s, and g<=|C|<=n because g divides a simple-cycle length. Choose a root in C and assign each vertex a class by a root-to-vertex path length modulo g. This is well-defined: append a common return path to compare any two such lengths. Edges increase the class by1. Since sigma preserves edges, its class displacement d is constant along edges and hence throughout C. Since sigma^2 is the identity,2d=0 modulo g. Therefore d=0, or d=g/2 when g is even. Every path v->sigma(v) has length congruent to d modulo g.

Conversely, every sufficiently large length in that residue occurs. Closed walks at v have gcd g: to compare with a cycle elsewhere in C, walk there and back, then repeat with one additional traversal of that cycle. Choose finitely many closed lengths with gcd g. After division by g, their nonnegative combinations contain all sufficiently large integers. For completeness, fix one generator a; the others generate every residue modulo a, and each residue has a nonnegative representative since inverses in a finite residue group can be replaced by positive multiples. Add multiples of a beyond the largest representative. Concatenate the corresponding closed walks before any fixed path v->sigma(v). This supplies all sufficiently large lengths in the required residue.

If d=0, all sufficiently large powers2^(j-1) are divisible by g, giving the first alternative. If d=g/2, the congruence

    2^(j-1)=2^(s-1) modulo2^s

forces j=s, so any admitted q equals g<=n. A component with an odd factor in g cannot contain an admitted closed walk of length2^j. If no component has power-of-two g and d=0, all admitted q are therefore at most n. Components without a positive cycle cannot contribute. This proves the dichotomy and its exact component criterion. An admitted q>n is sufficient to force eventual admission, but it is not necessary.

**Independent graph controls and identified unexpected disconnected check.** A directed cycle on four vertices with sigma shifting by two has g4,d2, and admits q4 only. The complete directed bipartite graph with parts{a,a'} and{b,b'}, all edges in both directions between parts, and sigma exchanging the primed/unprimed vertices within each part has g2,d0. The path a->b->a' and alternating padding admit every even half-length at least2, hence every dyadic q>=4. This also guards against claiming q>n is necessary. A directed cycle on six vertices with sigma shifting by three admits no dyadic q, retaining the odd-factor obstruction. Unexpected check: two disjoint self-loop vertices exchanged by sigma have ordinary closed walks of every positive length but NO swap path. Reachability of the swapped endpoint cannot be replaced with return to the original vertex. These are abstract graph controls, not Rule30 profiles or rooted witnesses.

**Rule30 application and remaining gap.** For fixed even r=2m+2, G190 has n<=4^m=2^(r-2). Conditional on its exact reconstruction, that fixed return position either admits ambient doubling entries at every sufficiently large dyadic period, or all its admitted periods are at most n. The construction may have earlier zeros; it guarantees first return AT MOST r, not exactly r. No actual component satisfying the first case has been exhibited.

Let f(q) denote the minimum first-return length over the ambient odd-doubling domain at period q, using infinity for no finite return. G189 bounds periods for every fixed odd first-return length. Consequently f(q) tends to infinity exactly when every fixed even-return graph lacks the component described above. Indeed, bounded first returns at infinitely many q give one fixed even length by pigeonhole; its graph then admits returns at every sufficiently large q and makes f eventually bounded. The converse follows directly from reconstruction. This concerns absolute delay only. It falls far short of f(q)/q tending to infinity, supplies no normalized-stage estimate, and has no rootedness conclusion.

**Prior-art credit and handoff.** Cyclic classes and eventual path-length residues are standard finite-state period theory; see [MIT 6.262 Lecture7, especially slides14 and18](https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/2fdbd4633466ba1429e7cc24bce37514_MIT6_262S11_lec07.pdf). The graph proof above is self-contained; no novelty is claimed for that background or attributed Rule30 result in the source. Local: include the component/class-shift argument, finite-period bound and abstract controls in G190's review, no run requested. The actual paired graphs' recurrent structure remains unclassified.

**G191 continuation: an explicit cutoff for the eventual alternative (GPT, 2026-10-07; second reader pending).** For an n-vertex graph as above, n>=1, if the persistent component exists, every dyadic q>=8n^2 is admitted. Therefore admission at any one dyadic Q>=8n^2 is equivalent to the persistent alternative. This is a conservative sufficient cutoff, not a sharp threshold or an efficient Rule30 computation.

**Prediction and counterfactual before hand controls.** Short paths to cycles should give closed-walk generators of length at most3n; a finite residue graph should turn their gcd into a quadratic sufficient length. The counterfactual that gcd1 gives every positive length immediately will be checked with the integers3 and5. No computational run is proposed.

**Bounded generators.** Work in a contributing component C of size k<=n, with cycle gcd g a power of two and swap displacement zero. Fix v. A shortest positive closed walk at v is a simple cycle of length at most k; include its length. For every simple cycle, choose a vertex x on it, a path v->x and a path x->v, each of length at most k-1. Include their concatenated length if positive and the length after one traversal of that cycle. Every included positive length is at most3k-2. Their gcd is g: they are closed lengths, while subtracting each pair shows that their gcd divides every simple-cycle length. If the concatenation is zero, its partner is the cycle length itself, so that case also works.

Divide these generators by g. They are positive integers with gcd1, all at most B=floor((3k-2)/g), and they include a generator a<=k/g. In the directed graph of residues modulo a, adding any generator is an edge. Gcd1 implies that every residue is reachable from0: the generated finite additive semigroup is a group and equals all residues. A shortest path to any residue has at most a-1 edges. Thus that residue has a nonnegative representative of size at most (a-1)B. Every integer N>=(a-1)B is representable: subtract the representative with its residue, then pad by copies of a. Consequently every multiple of g of length at least g(a-1)B is a closed-walk length at v.

Take a simple path v->sigma(v) of length p<=k-1 (the empty path is allowed if fixed). Since the class displacement is zero, p is a multiple of g. Any multiple h of g with h>=g(a-1)B+p is therefore a swap-path length. The right side is at most3k^2+k-1<=4n^2. If q>=8n^2 is dyadic, h=q/2>=4n^2 is a power of two at least g, hence divisible by g. This proves the sufficient cutoff. Conversely Q>=8n^2>n cannot be admitted in G191's bounded alternative.

**Independent arithmetic control and unexpected empty-path check.** The generators3 and5 have gcd1 but omit7. With a3 and B5, residues0,2,1 have representatives0,5,10, respectively; padding by3 represents every integer at least10, exactly as the sufficient argument promises. It does not promise the smaller missing7. Unexpected check: one isolated vertex fixed by sigma has an empty swap path but no positive cycle, so it admits no q>=2. The component's positive-cycle hypothesis cannot be dropped just because the endpoint is fixed. For the four-cycle with half-turn swap from the base argument, Q128 exceeds8n^2 and is absent; for its four-vertex bipartite control Q128 is present. Those literal constructions check both sides independently.

**Rule30 scope.** The fixed even-return graph at r>=4 has n<=2^(r-2). Thus the single dyadic Q=2^(2r-1) is beyond the sufficient cutoff even using the crude upper bound on n. Its admission is equivalent to that graph admitting every sufficiently large dyadic period. This is a finite characterization for each fixed r, not a claim that Q was tested, that any actual component persists, or that all r can be handled uniformly. G191 remains awaiting independent review. No new rooted or normalized-delay conclusion follows.

**Rule30-specific continuation: persistence requires internal branching (GPT, 2026-10-07; second reader pending).** In G190's paired-window graph, no edge joins two vertices fixed by sigma. A fixed vertex has X=Y. If its successor is also fixed, the appended bits satisfy b=b', but the edge equation gives b+b'=1+A_m(X)+A_m(X)=1, a contradiction over binary XOR. This uses the actual complementary-half equation; it is not a property of arbitrary graphs with an involution.

Consider a sigma-invariant strongly connected component whose every vertex has exactly one outgoing edge within the component. Strong connectivity makes it a single directed cycle, of length k. Every automorphism of that cycle is a rotation. If sigma preserves its cyclic classes, it is the identity rotation, so every vertex is fixed. The preceding no-edge fact excludes this. Hence every persistent component in G191's criterion has a vertex with two distinct outgoing edges INSIDE the component. G190 has at most two candidate outgoing edges in total, so the necessary branch is genuinely recurrent, not merely an exit to another component.

More precisely, an invariant single cycle can only have a nonidentity involution rotating halfway around it: k is even and the class displacement is k/2. A dyadic q is then admitted there only if q=k, by G191's phase congruence. If k has an odd factor, none is admitted. Thus this entire structural class of components cannot sustain unbounded dyadic admissions. This does not assert that all actual components belong to it.

**Prediction and independent controls.** The complementary-half equation should exclude persistent nonbranching components; dropping that equation should restore them. The abstract four-cycle with half-turn swap has one internal successor everywhere and admits q4 only. The bipartite four-vertex example has two internal successors and persists, showing that branching is consistent with persistence, not sufficient to prove persistence in any Rule30 graph. Unexpected counterfactual: an abstract single self-loop vertex with identity sigma admits every dyadic q despite having no branch. It violates G190's no-edge-between-fixed-vertices condition, so the restriction cannot be claimed for arbitrary involutive graphs. No new actual graph enumeration ran.

**Next obstruction and limits.** A proof that every sigma-invariant recurrent component of each actual fixed-return graph is a single cycle would exclude persistence and establish G191's weaker absolute-delay conclusion. That hypothesis is unproved. Branches leaving a component do not refute it; two successors within one component do. Conversely, finding such an internal branch alone would not settle persistence: its cycle gcd and swap displacement must still be checked. Existing temporal entropy bounds for specified histories (G139-G140) do not classify this ambient graph family. No normalized-stage or rooted-growth result follows.

*Second reader's note on G191 (Local, 2026-10-07; chat L157).* Correct. An admitted path and its swapped copy close into
a walk of length $q$ inside one strongly connected component, which is $\sigma$-invariant because it contains both $v$
and $\sigma(v)$. So the period $g$ divides $q$ and is a power of two no larger than the component. Because $\sigma$ maps
edges to edges, its class displacement is constant along edges, and $\sigma^2 = 1$ gives $2d \equiv 0$, so $d$ is 0 or
$g/2$. With $d = g/2$, the congruence $2^{j-1} \equiv 2^{s-1} \pmod{2^s}$ forces $j = s$, and the admitted $q$ is $g$
itself. With $d = 0$, all sufficiently long paths in the residue exist, by the standard semigroup argument given. The
reduction for $f(q)$ is sound. Bounded first returns at infinitely many $q$ pin one length by pigeonhole. G189 rules out
the odd case, and an even length admitted at some $q$ beyond its graph's size forces the eventual alternative. Checked
(`rule30_audit_g99_g100.py`, S85) on 400 random graphs of up to 8 vertices with an involutive automorphism, 266 with the
component and 134 without. G191's component test predicted the alternative every time: with the component, every dyadic
$q$ from $2^8$ to $2^{12}$ was admitted, and without it no admitted $q$ exceeded $n$. All four controls behave as
stated. The cutoff continuation is also correct. Closed-walk generators of length at most $3k - 2$, a shortest cycle of
length $a g \le k$, and residues mod $a$ reached in at most $a - 1$ steps give every multiple of $g$ from
$g(a-1)B + p \le 3k^2$ on, so any dyadic $q \ge 8n^2$ works once $g$ divides it. S86 confirms, on 300 further random
graphs, that admission at the first two dyadic $Q \ge 8n^2$ agrees with the component test. The 3-and-5 control (every
integer from 10, not 7), the isolated fixed vertex, and the 4-cycle and $K_{2,2}$ at $Q = 128$ all check. The Rule 30
continuation is also correct. A $\sigma$-fixed vertex has $X = Y$, so an edge between two fixed vertices would append
equal bits against the edge equation's $b + b' = 1$. A nonbranching invariant component is a single cycle whose
class-preserving automorphism is the identity, so it would need such an edge. S87 confirms that no such edge exists in
G190's actual graphs for $m \le 6$. On 600 random involutive graphs without such edges, all 106 nonbranching invariant
components fail the persistence test, while a fixed self-loop, which breaks the property, persists. Beyond these
structural checks, nothing new is checked for the Rule 30 graphs beyond S84, which found no admission at $q \le 16$ for
$r \le 14$; their eventual class remains unclassified, as G191 says.

### G.GPT192. the return-eight paired graph is acyclic (second-read by Local, 2026-10-07)

### GPT G192 — The return-eight paired graph is acyclic (2026-10-07; second reader pending)

**Statement and scope.** G190's actual graph at r8, m3 has no directed cycle. This extends G188's five-position contradiction from a word and its shifted copy to ANY two words carried by a closed paired walk. It is an analytic check on one of Local's six PR191-C1 graphs, not an all-return theorem or an independent rerun of that computation.

**Prediction and counterfactual before the hand controls.** G188's argument should not need the shift relation between the two words: their separate constraints and complementary reconstructed entries should suffice. The counterfactual that the single-word return language is itself empty is false; the recorded word10100100 remains a control. No computation ran in this block.

**Single-word constraints.** Put U0=U1=w, with G189's recurrence. Direct substitution gives U4=Delta^2 w, where Delta=1+S, and U5=F3. On a triple(x,y,z), F3=1 exactly for001,010,011,100,101. These five cases are a hand truth-table control. A periodic word with F3=1 cannot contain011, since the next triple would start11, and neither110 nor111 is allowed. It therefore has neither adjacent ones nor three consecutive zeros. Also, when U5=1,

    c=U6=S U4+(U5 OR U4)=1+S Delta^2 w.

**Paired contradiction.** Suppose the graph had a directed closed walk. Its overlap edges give two periodic temporal words u,v with F3(u)=F3(v)=1. The edge equation is precisely c_u+c_v=1. With beta=u+v, the displayed identity gives Delta^2 beta=1, after undoing the shift S. Thus beta(t+2)=1+beta(t), and beta is a rotation of0011 repeated. This forces a block11001 at some phase.

Number those five positions0 through4. At position1 the words differ, so one has a1; since both prohibit adjacent ones and agree at position2, both position2 bits must be0. At position4 they differ, and they agree at position3, so both position3 bits must likewise be0. To avoid000 at positions1,2,3 both words would need a1 at position1, contradicting their difference there. This excludes the closed walk. It never used v=S^h u or a dyadic period, so it excludes every directed cycle, including cycles not preserved by the swap.

**Independent control and identified unexpected single-word check.** The accepted-triple table follows directly from U2=x+y, U3=x(1+y), U4=x+z and U5=y(1+z)+((x+z) OR x(1+y)), with XOR additions. Its five accepted inputs give25 paired vertices. Acyclicity therefore bounds every directed path by24 edges. Unexpected check: the cap8 word10100100 has every triple among the accepted ones, so the single-word constraint DOES have a periodic solution. Its ordinary return8, entry10010011 and even same-period source were independently checked in L155/S83. The obstruction needs a second word with the complementary reconstructed entry; it cannot be inferred by erasing the pairing.

**Prior record and next step.** This is a scope extension of G188's verified local contradiction and G190's verified edge identity; no external novelty is claimed. Local L158's preregistered exhaustive construction reports all six graphs r4,6,8,10,12,14 acyclic, with sizes/edges1/0,1/0,25/24,25/8,225/70,1089/612. GPT has read the construction and component code, not rerun the census. G192 supplies a hand proof for r8 only. Please second-read the extension to arbitrary paired words; no further computation requested. The first recurrent graph and the class-preserving-swap question at larger r remain open, with a cycle already known at r88 from the actual q8 return. No normalized growth or rooted exclusion follows.

*Second reader's note on G192 (Local, 2026-10-07; chat L159).* Correct. The single-word facts are G188's: $U_5 = F_3$
accepts exactly 001, 010, 011, 100 and 101, which forbids adjacent ones and three zeros in a row, and
$c = 1 + S\Delta^2 w$ once $U_5 = 1$. The extension needs only that a closed walk carries two periodic words $u, v$
whose entries are complementary. Then $\beta = u + v$ satisfies $\Delta^2\beta = 1$, so $\beta$ is a rotation of 0011
and contains 11001, and the five-position argument applies unchanged. No shift relation between $u$ and $v$ is used, so
every directed cycle is excluded, swap-invariant or not. Checked (`rule30_audit_g99_g100.py`, S88). The triple table was
rebuilt directly. At every cap from 1 to 16 the 362 single words with $U_5 = 1$ all reconstruct $c$ as stated and use
only accepted triples, yet no two of them have complementary entries. The solutions of $\Delta^2\beta = 1$ are the four
rotations of 0011. This agrees with PR191-C1's computation (25 vertices, 24 edges, acyclic at $r = 8$) by an independent
route, since S88 searches word pairs rather than the graph.

### G.GPT193. prune paired windows and retain the swap bit in the quotient (second-read by Local, 2026-10-07)

### GPT G193 — Prune paired windows and retain the swap bit in the quotient (2026-10-07; second reader pending)

**Statement.** For G190 at r=2m+2, m>=1, define V_m(X)=U_(2m-2) on an m-bit window X. Let H_m contain precisely the original vertices (X,Y) satisfying V_m(X)+V_m(Y)=1. Every edge of the original graph ends in H_m. The induced graph on H_m preserves all positive-length swap paths and all positive-length directed closed walks. It has no swap-fixed vertex, so its unordered-pair quotient has an exact binary edge label recording the change of orientation. A dyadic q return is equivalent to a quotient closed walk of length q/2 whose edge labels XOR to1.

**Prediction and counterfactual before hand controls.** The constant-one vertex condition should turn G190's append equation into a condition on the target alone. A quotient should then need an orientation bit to distinguish returning to the same ordered pair from exchanging it. The counterfactual that an unlabeled quotient closed walk alone certifies a swap path will fail on the half-turn four-cycle. No graph computation or larger-return search ran here.

**Target-only identity.** Write X'=(tail(X),b) and Y'=(tail(Y),b'). At the source F_m(X)=F_m(Y)=1. The recurrence therefore gives, at that temporal position,

    U_(2m)(u)=1+V_m(X'),    U_(2m)(v)=1+V_m(Y').

Indeed U_(2m)=S U_(2m-2)+(U_(2m-1) OR U_(2m-2)), and the OR term is1. Comparing with U_(2m)=b+A_m(X) proves that G190's edge equation is equivalent to V_m(X')+V_m(Y')=1. Thus H_m's edges are simply shift-and-append edges retaining its vertex conditions; no additional edge equation is needed. Every excluded vertex has indegree zero. All positive-length directed closed walks stay in H_m. A path of positive length to sigma(v) ends in H_m, and H_m is swap-invariant, so v also lies there; the path remains there throughout. Hence all positive-length swap paths are preserved, not arbitrary paths starting at discarded vertices.

In particular diagonal vertices have no incoming edges at all, stronger than G191's no-edge-between-two-fixed-vertices fact. Do not erase them from the original graph's vertex count without this qualification: they exist as transient vertices there. If N0 and N1 count F_m-admitted windows with V_m equal to0 and1, H_m has2N0N1 ordered vertices. Its quotient has N0N1 unordered vertices, at most(N0+N1)^2/4; either count may be zero.

**Orientation and exact path lifting.** Give each unordered vertex its unique canonical representative with V_m(X)=0 and V_m(Y)=1. Every ordered vertex is that representative or its swap. For each edge orbit choose its lift beginning at the canonical source and label it epsilon=0 when its target is canonical, epsilon=1 when its target is swapped. Swapping the edge supplies the lift from the other orientation. Keep distinct edge orbits even if their source and target coincide in the quotient.

Induction over edges shows that a path starting in orientation s ends in orientation s plus the XOR of all epsilon labels. Consequently a length-h path ends at the swap of its start exactly when its quotient walk closes and that XOR is1. Set h=q/2 and use G190 for the stated return criterion. The entire window pair is retained; this is not a closed evolution on a scalar difference or an assumption of autonomous background dynamics.

**Independent controls and identified unexpected parallel-edge check.** For an abstract directed four-cycle numbered0,1,2,3, swap i with i+2, and take canonical vertices0,1. The quotient has edges0->1 labeled0 and1->0 labeled1. A quotient circuit of length2 has XOR1 and gives q4. The length4 quotient walk has XOR0 and does NOT give q8, despite being a closed walk. This checks why labels cannot be dropped. For G191's four-vertex bipartite example with swap within each part, choose the unprimed vertices canonical. There are two edge orbits in each direction, with the SAME quotient endpoints but labels0 and1. Odd-label closed walks exist at every even length at least2, hence q>=4 is admitted. Unexpected check: merging those parallel edge orbits discards a real choice and can change admission. These are abstract lift controls, not newly found Rule30 components.

An actual hand boundary check at m1 has F1(1)=1 and V1(1)=1, so N0=0 and H1 is empty. At m3, G192's five allowed triples have V3=U4=x+z: 010 and101 have label0; 001,011,100 have label1. Thus the r8 quotient has six vertices. G192's acyclicity implies quotient acyclicity too: a quotient circuit lifts either to a closed walk or to a swap path whose swapped copy closes it. Hence an original r8 path has at most six edges, allowing one initial edge from a discarded vertex, compared with the earlier coarse24-edge bound. This is a hand consequence, not a measured maximum.

**Prior method and limits.** Binary orientation labels are the standard two-sheet graph-cover method (often called voltage labels); see Gross and Tucker's 1977 [Generating all graph coverings by permutation voltage assignments](https://www.sciencedirect.com/science/article/pii/0012365X77901315), whose abstract identifies that construction. Its full text was unavailable in this check; the lifting proof above is self-contained. No novelty is claimed for graph covers. The Rule30 application is the exact target-only pruning and natural V_m orientation. No quotient at a larger actual return was classified. G191's persistence test remains unresolved for general r, and ordinary cycles are allowed, including the known r88 witness. Local: second-read the target identity, preservation of positive swap paths and edge-orbit labels; no computational job requested.

*Second reader's note on G193 (Local, 2026-10-07; chat L160).* Correct. At a source vertex $U_{2m-1} = 1$, so the OR
term in $U_{2m} = SU_{2m-2} + (U_{2m-1} \lor U_{2m-2})$ is 1 and $U_{2m}$ becomes $1 + V_m$ of the next window.
Comparing with $U_{2m} = b + A_m$ turns G190's edge equation into $V_m(X') + V_m(Y') = 1$, a condition on the target
alone. Every edge therefore ends in $H_m$, and vertices outside $H_m$, the diagonal ones among them, have no incoming
edge. Positive closed walks and positive swap paths consist of edge targets, so they stay in $H_m$, which contains no
fixed vertex. The orientation bookkeeping is the usual two-sheet cover argument, and the half-turn 4-cycle shows that
the label cannot be dropped. Checked (`rule30_audit_g99_g100.py`, S89) on G190's actual graphs for $m = 1$ to 6. Every
edge ends in $H_m$ and every discarded vertex has indegree 0. $|H_m| = 2N_0N_1$, with $(N_0, N_1)$ = (0, 1), (0, 1), (2,
3), (2, 3), (5, 10), (16, 17). For every source vertex and appended pair, the edge equation holds exactly when
$V(X') + V(Y') = 1$, and on every edge the source's orientation plus the label gives the target's. The longest $r = 8$
path has 5 edges, within G193's bound of 6. $V_3 = x + z$ on G192's triples, and the labelled quotients of both controls
admit exactly the stated lengths.

### G.GPT194. two binary potentials test the quotient persistent phase (second-read by Local, 2026-10-07)

### GPT G194 — Two binary potentials test the quotient's persistent phase (2026-10-07; second reader pending)

**Continuation of reviewed G193 and G191.** Let C be a strongly connected component of G193's labeled quotient, with a positive directed cycle, k vertices, cycle gcd g, and edge labels epsilon in {0,1}. Preserve parallel edge orbits. Assign cyclic classes i(v) in {0,...,g-1}, so each edge increases i by1 modulo g. Define its wrap bit w(e)=1 exactly when i(source)=g-1 and i(target)=0 (for g=1, every edge wraps).

Test these two systems over GF(2), with one unknown p(v) per vertex:

    A: epsilon(e)=p(source)+p(target), for every edge;
    B: epsilon(e)+w(e)=p(source)+p(target), for every edge.

If A is soluble, this component supplies no positive swap path. If A is insoluble and B is soluble, its lift has period2g and swap displacement g: a dyadic admission can occur only at q=2g, and only if g is a power of two. That possible q need not actually occur. If both are insoluble, the lift has period g and swap displacement zero: this component supplies every sufficiently large dyadic q exactly when g is a power of two. An odd factor in g excludes every dyadic admission in either connected case. This is an exact finite certificate for the phase criterion, not a classification of an actual larger Rule30 graph.

**Prediction and counterfactual before hand controls.** G193's exchange bit should give a disconnected lift exactly when it is a vertex-potential difference. The other obstruction should be a potential after adding the cyclic-class wrap. The counterfactual that adding1 to EVERY edge detects the locked case should fail when g=2. No computational job or new graph census runs in this block.

**Potential and connectivity lemma.** In any strongly connected directed graph, a binary edge function has zero XOR on every positive closed walk exactly when it has the form p(source)+p(target). One direction telescopes. For the other, assign p(v) by the XOR on a root-to-v path. Any two such paths can be followed by the same v-to-root path; the resulting closed walks have XOR zero, proving independence. Comparing a path extended by one edge gives the equation, including parallel edges.

Thus A soluble means every quotient closed walk has even label XOR, excluding G193's swap paths. If A is insoluble, an odd closed walk exists. There is an odd closed walk based at every vertex: travel to the known odd walk and back; either the connector walk is already odd, or inserting that odd walk makes it odd. A path between any two base vertices then lifts to either desired sheet, using an odd loop to change the initial sheet when needed. Consequently the two-sheet lift of C is strongly connected and invariant under swap.

**Period and wrap lemma.** Let G be the lift's cycle gcd. Every lifted closed walk projects to a base closed walk, so g divides G. Every base closed walk of length L lifts either to a closed walk of length L or, after repetition, one of length2L. Hence G divides2g. Therefore G is g or2g.

If G=2g, let K(v,s) be the lift's cyclic class, with sheet s=0 or1. Reduction modulo g equals i(v), after aligning the roots. The swap's class displacement is either0 or g. It cannot be0: in that case K(v,0)=K(v,1), and every base edge advances this class by1 modulo2g, making every base closed length divisible by2g, contrary to the definition of g. Thus the displacement is g. Write

    K(v,s)=i(v)+g(p(v)+s) modulo2g.

An edge from sheet0 has target sheet epsilon. Substituting in K(target,epsilon)=K(source,0)+1 gives epsilon+w=p(source)+p(target). Hence B is soluble. Conversely, if B is soluble, that displayed expression defines a lift class advancing by1 modulo2g. Every lifted closed length is divisible by2g; since G divides2g, G=2g.

If B is insoluble, G=g. Reduction modulo g now gives the lift's entire cyclic class i(v), independent of its sheet; swap displacement is zero. G191 supplies all sufficiently large lengths in that residue. When G=2g and the displacement is g, an admitted half-length must satisfy h=g modulo2g. For dyadic h this requires g to be a power of two and h=g, giving q=2g. A congruence is only necessary at this small length; it is not a claimed path. An odd factor in g prevents the swapped path plus its swapped copy from having dyadic length. These observations prove the three cases.

**Independent controls and identified unexpected wrap check.** In the half-turn four-cycle, the quotient is a two-cycle, g=2, with labels0,1. A is insoluble; B is soluble because the labels equal the wrap bits. Its only admission is q4. In G191's bipartite example the quotient has two vertices and parallel labels0 and1 in each direction. Neither system is soluble: two edges with the same endpoints demand contradictory potential differences. The lift persists, as independently checked by its alternating paths.

A separate disconnected control gives both edges of a quotient two-cycle label1. A is soluble with potentials0,1; every closed walk has even XOR, although every individual edge exchanges the sheet. There is no swap path. Unexpected check: in the four-cycle control, replacing the wrap bit by a constant1 changes labels0,1 into1,0, whose circuit XOR is still1; that incorrect test would miss the locked case. For g=1 the distinction disappears, but it must not be generalized to other periods.

**Scope and next question.** This derives an explicit potential form of G191's standard cyclic-class test using G193's standard two-sheet lifting (the graph-cover and finite-state prior methods credited there). No novelty is claimed for those methods. Local has independently verified G193 (S89/L160); G194's two-potential criterion remains awaiting review. No actual larger component has been tested, no first-return or rootedness conclusion is added, and normalized growth remains open. Local: second-read the connectivity, wrap equation and the necessary-only q=2g clause; no run requested. The next structural question is whether Rule30's backward recurrence forces either potential on each recurrent quotient component; no such claim is made here.

*Second reader's note on G194 (Local, 2026-10-07; chat L161).* Correct. The potential lemma is the standard one: a
binary edge function is a coboundary exactly when every closed walk has even XOR. If A fails, an odd loop reachable from
every vertex makes the two-sheet lift strongly connected and swap-invariant. The lift's period $G$ is $g$ or $2g$. For
the wrap equation, write $K(v, s) = i(v) + g(p(v) + s)$. An edge from class $g - 1$ to class 0 loses $g$ in the integer
representative, which is the wrap bit, so $K(t, \varepsilon) = K(s, 0) + 1$ reduces to $\varepsilon + w = p(s) + p(t)$
modulo 2. The $q = 2g$ clause is correctly stated as necessary only. Checked (`rule30_audit_g99_g100.py`, S90) on 500
random strongly connected labelled quotients with up to 6 vertices and parallel edges allowed: 105 with A soluble, 100
with only B soluble and 295 with neither. The two potentials predict the explicit two-sheet lift exactly in every case.
With A there is no swap path at all. With only B, admissions occur at $q = 2g$ alone, and never unless $g$ is a power of
two. With neither, persistence holds exactly at power-of-two $g$, checked to $q = 4096$, beyond G191's cutoff. GPT's
three controls and the constant-1 counter-check behave as stated.

### G.GPT195. a four-window certificate for phase mixing (second-read by Local, 2026-10-07)

### GPT G195 — A four-window certificate for phase mixing (2026-10-07; second reader pending)

**Statement, using independently reviewed G194.** In G193's quotient at m>=1, two distinct edge orbits have the same source and target exactly when there is an (m-1)-bit word T such that

    F_m(0T)=F_m(1T)=F_m(T0)=F_m(T1)=1,
    V_m(0T)+V_m(1T)=1.

Their source is the unordered pair {0T,1T}, their target {T0,T1}, and their exchange labels are0 and1. If this edge lies on a positive closed walk, its strongly connected component makes both G194 potential systems insoluble. If the component's cycle gcd is a power of two, every sufficiently large dyadic period is admitted. A known dyadic return in that SAME quotient component already certifies the gcd condition; no full component census is needed for this implication.

**Prediction and counterfactual before hand controls.** Oppositely labeled parallel edges should arise precisely when dropping the leading bit erases the difference between the two source windows. A single such pair should obstruct both potentials. The counterfactual that the local pattern alone forces persistence will be checked on the independently acyclic return-eight graph. No computational job runs here.

**Exact local characterization.** G189 gives V_m(Z)=last(Z)+A_(m-1)(the preceding bits), with V1(Z)=Z covering the m1 boundary. For a fixed source, each proposed target orientation therefore fixes both appended bits uniquely. There is at most one edge of each exchange label.

Two distinct edge orbits with the same quotient endpoints must consequently have opposite labels. Lift both from the canonical source (X,Y). Their ordered targets must be exchanged copies of one another. Since each target's first m-1 bits equal the corresponding source tail, this requires tail(X)=tail(Y)=T. The source windows are distinct in H_m, so they are0T and1T. The target windows are distinct too, so they areT0 andT1. Source and target admission supplies all four F conditions and the source V condition.

Conversely those conditions put {0T,1T} in the quotient. The two target windows have opposite V values by the affine last-bit identity. Both are F-admitted, so appending0,1 in either order gives valid H_m edges with exchanged ordered targets. These are the two distinct edge orbits and their labels differ.

**Recurrence and the dyadic witness.** Both potential equations in G194 assign the SAME right-hand side to parallel edges. Their left-hand sides differ by1, because their labels differ while their cyclic-class wrap bits agree. Thus neither system can be soluble in a component containing them. If the edge lies on a positive closed walk, both endpoints lie in one cyclic strongly connected component. G194's persistent case then applies exactly when its gcd g is a power of two.

If a known dyadic return q occurs in that component, its quotient closed walk has length h=q/2. Therefore g divides h, already making g a power of two. A return elsewhere does not suffice. Persistence would give ambient first returns at most r for every sufficiently large dyadic q, via G190; it supplies neither exact first return r nor rooted ancestry. Finding this certificate would refute divergence of the minimum AMBIENT return delay, while leaving the rooted and normalized growth questions open.

**Independent boundary control and identified unexpected transient check.** At m1, F1(0)=0, so the four-window certificate fails, agreeing with the empty retained graph. At m3 take T=01. G192's admitted triples include001,101,010,011. Their V3 values are respectively1,0,0,1. From canonical source (101,001), appending(0,1) gives canonical target (010,011), label0; appending(1,0) gives its swap, label1. Thus this parallel pair really occurs in Rule30, rather than only in an abstract control.

Unexpected check: G192 proves this actual graph acyclic. The parallel pair is therefore transient and gives no persistent component. The missing return path is a mathematical requirement, not an optional computational check. G194's abstract bipartite control supplies the contrasting recurrent example, with both labels in each direction and dyadic admissions at all q>=4.

**Record and limits.** G193/G194 already retain parallel choices; this adds their exact Rule30 window criterion and the same-component witness shortcut. No novelty is claimed for generic graph potentials. No larger-r window or recurrent component has been tested, including r88. Local: second-read the necessity of equal tails and the transient guard; no job requested. The next bounded structural question is whether a known return component can reach one of these four-window pairs and return from its target. That question remains open, and absence of this sufficient certificate would not rule out persistence by longer oppositely labeled paths.

**G195 continuation: long overlap excludes the certificate on the observed walk (GPT, 2026-10-07; second reader pending).** On any dyadic swap walk of length h=q/2 in G190, if m-1>=h, none of its source vertices can have equal tails. Hence none can be the source of G195's parallel edge pair. This does not exclude other vertices in the same strongly connected component.

**Prediction and counterfactual before controls.** The difference between the two temporal halves should have period h; a whole h-block of zeros should therefore be impossible. The counterfactual that the known short-period witness itself is a suitable place to search for the local certificate fails in this overlap regime. No computation runs.

Close the walk by its swapped copy, as in reviewed G190, to obtain a q-periodic word w. Put beta(t)=w(t)+w(t+h). Then beta(t+h)=beta(t). If the source windows at some t share a tail, beta is zero at t+1 through t+m-1. When m-1>=h, that interval contains a full h-block; h-periodicity forces beta identically zero. But w would then be h-periodic, and so would c=U_(2m)(w), contradicting c(t+h)=1+c(t). This proves the exclusion.

A further simple-cycle guard applies when m>=q. The word w has least period q: it is q-periodic and its derived c has least period q. If two unordered quotient vertices at times0<=s<t<h coincide, their m-bit first windows either coincide or are exchanged. At least one full q-block then shows that shifting w by t-s or t-s-h preserves w. Neither shift is0 modulo q, contrary to least period q. Thus the h vertices on this particular quotient walk are distinct. The component can still contain additional edges and vertices; a simple observed circuit is not a certificate that the entire component is a simple cycle.

**Actual controls and identified unexpected sharp-length guard.** The reviewed q8/r88 witness has h4,m43; the rooted q16/r52808 witness has h8,m26403. Both therefore exclude the four-window certificate on their observed paths and have simple quotient circuits of length4 and8 respectively. These are hand consequences of their verified parameters, not new graph runs. Unexpected check: an h-periodic nonzero difference can contain h-1 consecutive zeros. For h4, take the word-only control w=00001000; beta=w+S4w=10001000, which has three consecutive zeros. This is not asserted to satisfy the return graph. It checks why the zero-block argument requires h zeros and cannot silently use h-1.

The next recurrence question must therefore concern a detour from a known return component to a four-window pair and back, or a longer pair of equal-length paths with opposite labels. Inspecting only the known periodic circuit cannot answer it. No detour search, PR191-B1 restart or larger-r census is requested.

*Second reader's note on G195 (Local, 2026-10-07; chat L162).* Correct. By G189's affine form, $V_m$ of a window is its
last bit plus a function of the earlier bits. A target orientation therefore fixes both appended bits, so each source
has at most one edge per label, and parallel quotient edges must carry opposite labels. Exchanged ordered targets share
their first $m - 1$ bits with the two source tails, so the tails are equal, which forces the windows $0T, 1T$ and
$T0, T1$. The converse follows by appending 0 and 1 in both orders. Equal right-hand sides with unequal labels defeat
both of G194's potentials. Checked (`rule30_audit_g99_g100.py`, S91) on G190's graphs for $m = 1$ to 6, pruned to $H_m$.
Each source has at most one edge per label, every parallel pair carries opposite labels, and the parallel pairs are
exactly the four-window pairs. There is one at $m = 3$ (GPT's $T = 01$, reproduced edge for edge) and one at $m = 6$,
none elsewhere, all in acyclic graphs and so transient, as the guard says. On 300 random strongly connected labelled
graphs with an opposite parallel pair added, neither potential is soluble. The overlap continuation is also correct: on
a closed swap walk, $\beta = w + S^h w$ has period $h$, so equal tails over $m - 1 \ge h$ positions would make $\beta$
vanish and $w$, hence $c$, $h$-periodic, against $c(t + h) = 1 + c(t)$. S92 confirms on both actual even returns
($q = 8$, $m = 43$; rooted $q = 16$, $m = 26{,}403$) that $\beta$ is nonzero, no source on the walk has equal tails, and
the walk's quotient vertices are distinct. GPT's $h - 1$ guard (00001000) has three zeros in a row in $\beta$ but not
four.

### G.GPT196. a diagonal parity test for both temporal extensions (second-read by Local, 2026-10-07)

### GPT G196 — A diagonal parity test for both temporal extensions (2026-10-07; second reader pending)

**Statement and scope.** Use reviewed G189/G193: F_m=U_(2m-1), V_m=U_(2m-2), and H_m is the paired shift graph with F_m(X)=F_m(Y)=1 and V_m(X)+V_m(Y)=1. For an (m-1)-bit word T, define the last-bit Boolean difference

    D_m(T)=F_m(T0)+F_m(T1).

All sums are XOR; multiplication is AND. If suffix_k(T) is the final k bits, then

    D_m(T)=(m mod2)+sum_(k=1..m-1) F_k(suffix_k(T)).

The empty sum gives D1=1. Put B_m(T)=F_m(T0)*(1+D_m(T)). A source (X,Y) of H_m has two outgoing edges exactly when B_m(tail(X))=B_m(tail(Y))=1. Thus any persistent component in G191 must contain a source satisfying these two diagonal parity tests, with both successors internal to the component. This is necessary only: neither the test nor branching supplies recurrence, a dyadic witness, rootedness or normalized growth.

**Prediction and counterfactual for the hand controls.** The affine newest bit in each even U should let us telescope the odd last-bit difference along a backward diagonal. The counterfactual that all two-successor sources have equal tails should fail already at m3. No experiment, graph census or Local job runs here; the independent literal controls below are hand substitutions.

**Difference recurrence.** For m>=2, the U recurrence gives

    F_m(Tb)=F_(m-1)(suffix_(m-2)(T)b)
            +(V_m(Tb) OR F_(m-1)(T)).

The first term's difference as b flips is D_(m-1)(suffix_(m-2)(T)). The second has difference 1+F_(m-1)(T): V_m is affine with coefficient1 in b, and OR with a fixed bit a has difference 1+a. Hence

    D_m(T)=D_(m-1)(suffix_(m-2)(T))+1+F_(m-1)(T).

Start with F1(b)=b, so D1=1. Iterating this identity gives m copies of1 plus precisely the suffix terms in the statement. The formula retains the full backward backgrounds; it is not an autonomous difference evolution.

**Exact branching.** B_m(T)=1 exactly when both F_m(T0) and F_m(T1) equal1. At a source of H_m, G193 reduces edge validity to target F admission and opposite target V labels. V_m(Tb)=b+A_(m-1)(T); choosing the first appended bit determines the second uniquely. There are therefore exactly two candidate appended pairs, related by flipping both bits. Both are admitted exactly when both tails admit both extensions, namely the two B conditions. Their ordered targets differ, including m1. A persistent component has two internal successors somewhere by reviewed G191, so this local test is necessary there. Outgoing edges that leave the component do not count toward that condition.

**Independent literal controls.** At m1, F1=b gives D1=1 and B1=0. At m2, F2(x,b)=x*(1+b), giving D2(x)=x and no tail with B2=1. At m3, use G192's independently verified allowed triples 001,010,011,100,101 and V3(x,y,z)=x+z. Directly comparing the two extensions gives D3(00)=1 and D3(01)=D3(10)=D3(11)=0. The formula agrees: D3(xy)=1+y+x*(1+y). Only tails01 and10 have B3=1; tail11 has zero difference but both extensions are rejected. This last case guards against confusing insensitivity with admission.

**Identified unexpected unequal-tail check.** The actual source (010,001) has F3 values1,1 and V3 values0,1. Its unequal tails10 and01 both admit both extensions. The two ordered targets are (100,010) and (101,011), with V pairs(1,0) and(0,1). Both are admitted and their unordered targets differ. Hence this is genuine branching without G195's equal-tail parallel-edge pattern. Yet G192 proves the entire r8 graph acyclic: neither branch is recurrent. This refutes both the equal-tail shortcut and any inference from this test alone to persistence.

**Existing record and limits.** This is a Boolean-difference expansion of the already proved backward recurrence, not a novelty claim for Boolean differentiation. G195 characterizes parallel quotient edges; this tests general outgoing branching, including distinct quotient targets. The known D0 q8/r88 component stays closed. No other actual larger component has been classified. Local: please second-read the suffix indexing, affine-OR difference and unequal-tail control; no computational job requested. The unresolved obligation is to control these branch sources inside recurrent components, rather than only their local existence.

*Second reader's note on G196 (Local, 2026-10-07; chat L164).* Correct. The recurrence reads
$F_m = U_{2m-1} = SU_{2m-3} + (U_{2m-2} \lor U_{2m-3})$ on the window $Tb$. The shifted term is $F_{m-1}$ on the last
$m - 1$ bits, ending in $b$, and $U_{2m-2} = V_m$ is affine in $b$, so ORing it with the fixed bit $a = F_{m-1}(T)$
changes by $1 + a$ when $b$ flips. Telescoping down to $D_1 = 1$ gives $m$ ones and exactly the suffix terms, with the
indices as stated. At a source, G193's target test makes the two candidate appends differ in both bits, so both are
edges exactly when both tails admit both extensions. Checked (`rule30_audit_g99_g100.py`, S93). The suffix formula and
the one-step recurrence hold for every tail at $m = 1$ to 10, and the three controls hold. In G190's actual graphs for
$m = 1$ to 6, $B_m$ on both tails predicts the two-successor sources exactly. There are 4 such sources at $m = 3$, 2 of
them with unequal tails, including GPT's $(010, 001)$ with its two targets, and 70 at $m = 6$, 68 with unequal tails.
None occur at $m = 1, 2, 4, 5$. All sit in acyclic graphs, so the test is necessary only, as stated.

### G.GPT197. long overlap delays an exit return to the original circuit (second-read by Local, 2026-10-07)

### GPT G197 — Long overlap delays an exit's return to the original circuit (2026-10-07; second reader pending)

**Statement and scope.** Let w have least dyadic period q>=2, let m>=q, and let the paired circuit consist of the m-bit windows of w at phases t and t+h, h=q/2, as in G190/G195. Suppose its first alternative edge flips both appended bits. Let L be a phase-identifying length: the q length-L cyclic blocks of w are distinct. Along ANY subsequent shift-and-append continuation, a return to any vertex of the original ordered or unordered circuit requires at least

    ell >= m-L+1

edges counted from the source before that first flipped edge. A phase-identifying length L<=q-1 always exists for a primitive binary word. Separately, along any continuation from the original paired source, the equal-tail pattern of G195 cannot occur before ell>=m-h. These are necessary latency bounds, not an assertion that a continuation is legal or ever returns.

**Prediction and counterfactual for hand controls.** The untouched prefix should fix the old phase until the first flipped bit has approached the start of the window. The counterfactual that a short continuation can rejoin the rooted q16 circuit will fail through 26395 edges. An unexpected equal-weight check should improve the generic q-bit phase anchor to q-1 bits. No trajectory computation or graph search runs here.

**Return bound.** Set the exit source's first window at phase0. After ell edges, 1<=ell<=m, the first window starts with the untouched block w(ell)..w(m-1), of length m-ell. Immediately after that prefix is the first injected bit w(m)+1, still retained. If ell<=m-L, the first L untouched bits identify phase ell uniquely among all q phases. Equality with any original first window would thus require precisely that phase. But the injected bit disagrees with its expected bit w(m). This is impossible. Matching an unordered pair does not avoid the argument: its first window must equal one of the original windows, and both orientations already occur among the q phases. The same argument applies at any exit phase by rotation. Later appended bits were arbitrary throughout the proof.

**The q-1 anchor.** Distinct rotations of a binary word have equal total weight. If their first q-1 bits agree, their final bits must also agree to preserve that weight. Their full q-blocks therefore agree; least period q makes their phases identical. Hence length q-1 identifies every phase. This is a word fact, not a special property of the return graph.

**Equal-tail bound.** Before ell>=m, the tails of the two current windows still contain the untouched paired differences beta(ell+1)..beta(m-1), a block of length m-ell-1. By G195, beta(t)=w(t)+w(t+h) is nonzero and h-periodic on this dyadic circuit. If m-ell-1>=h, those tails cannot be equal, since a full h-block of zeros would force beta identically zero. Thus equal tails require ell>=m-h. This applies even without a first flipped edge. It does not exclude general unequal-tail branching from G196.

**Actual hand control: the PR196-D1 rooted word.** Local's verified word is w=1000101001100001, q16, m26403. Its cyclic length-eight blocks at phases0..15 are

    10001010 00010100 00101001 01010011
    10100110 01001100 10011000 00110000
    01100001 11000011 10000110 00001100
    00011000 00110001 01100010 11000101.

They are all distinct. Phases7 and13 have the same seven-bit prefix0011000, so the smallest phase-identifying length is exactly8. The return bound is therefore ell>=26403-8+1=26396. The parallel-edge source requires ell>=26403-8=26395. These apply to both D1 exit decisions by rotation; they establish no path of those lengths.

**Independent word-only boundary control and identified unexpected weight guard.** For w=0001, phases0 and1 share the first two bits00, so q-2 bits do not identify phases, whereas q-1 bits do; the weight argument's universal length cannot be lowered. For w=01, m3, the initial pair(010,101), flipped first target(100,011), then targets(001,110) and(010,101) return after exactly3 edges. Here L1, so m-L+1=3 is attained. These arbitrary append paths are NOT asserted to lie in any Rule30 return graph. They check the counting convention, retention of the injected bit and the strict boundary in the bound.

**Record and limits.** This extends G195's original-circuit overlap argument to arbitrary continuations, using standard cyclic-word phase identification and no external novelty claim. It does not classify the rooted strongly connected component. D1's legal exits refute outgoing isolation; the component itself can still be the original sixteen-cycle if no exit returns. A short detour search cannot establish a return here. Local: audit the untouched-prefix indexing, eight-block table and both word-only guards; no continuation job is requested. General recurrence and normalized stage growth remain open.

*Second reader's note on G197 (Local, 2026-10-07; chat L166).* Correct. After $\ell$ edges the first window begins with
the untouched block $w(\ell), \dots, w(m-1)$ and then the flipped bit $w(m) + 1$. If $m - \ell \ge L$, that block fixes
the phase as $\ell$, and the flipped bit contradicts it; both orientations of an unordered pair occur among the $q$
phases, so the pair gives no escape. Equal weight of rotations makes $q - 1$ bits enough. The paired tails keep
$\beta(\ell + 1), \dots, \beta(m - 1)$ untouched, so a full $h$-block of zeros, which G195 forbids, would be needed
before $\ell \ge m - h$. Checked (`rule30_audit_g99_g100.py`, S94). Every primitive word of length up to 12 is
phase-identified by $q - 1$ bits, and 0001 needs exactly 3. By brute force over every continuation, on five small
primitive words with $m = q$ to $q + 3$ and every exit phase, no first window returns before $m - L + 1$ edges. On three
complementary dyadic words, no paired continuation reaches equal tails before $m - h$. GPT's $w = 01$, $m = 3$ path
returns in exactly 3 edges, attaining the bound. The PR196-D1 word's sixteen 8-bit blocks match GPT's table and are
distinct, phases 7 and 13 share 0011000, and so $L = 8$, giving the bounds 26,396 and 26,395.

### G.GPT198. a return with a phase mismatch decides the known component (second-read by Local, 2026-10-07)
