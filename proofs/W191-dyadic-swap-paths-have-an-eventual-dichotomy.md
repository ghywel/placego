# Dyadic swap paths have an eventual dichotomy

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G191 — Dyadic swap paths
have an eventual dichotomy (2026-10-07; second reader pending)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Paths that exchange two starting patterns have a restricted eventual period behavior.

**What it says.** In a finite directed graph whose symmetry exchanges two halves, paths of half a dyadic period to the exchanged starting point either exist for every sufficiently large period, or all admitted periods are bounded by the number of vertices. The test uses mutually reachable regions and the classes that each edge advances through. Second review is pending.

**Why it matters.** Applied to G190, this characterizes the weaker question of whether absolute return delays grow. The actual return graphs remain unclassified; it establishes neither normalized growth nor a path from the root.

**An everyday picture.** Two markers move around a circular track. Exchanging their starting positions can preserve their position in the repeating schedule, or shift it halfway around. Those two arrangements permit different journey lengths.

## The formal statement and proof

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
