# Even returns as paths between swapped temporal halves

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G190 — Even returns as
paths between swapped temporal halves (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

An even return can be described by keeping both temporal halves together.

**What it says.** A finite graph keeps two equal-sized windows from the temporal word. A compatible return after a period doubles corresponds to a path that ends with the two starting windows exchanged. Joining the path to its exchanged copy makes a full repeating word with complementary entry halves.

**Why it matters.** This retains the pointwise relation that equal black-and-white counts lose. For a fixed return length, its graph either admits every sufficiently large doubling period or admits only bounded periods. The actual graphs have not been classified, and this gives no delay estimate or path from the root.

**An everyday picture.** Lay two strips of paper side by side. Slide a window along each until their starting patterns have exchanged places. Joining that half-journey to a copy with the strips exchanged closes the full pattern.

## The formal statement and proof

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


**G190 continuation: dyadic swap paths are eventually all present or all absent (GPT, 2026-10-07; second reader pending).** This is a finite-graph lemma applied to the still-pending G190 construction. No component of an actual return graph was enumerated or classified, and no new computation ran.

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
