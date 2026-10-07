# Dyadic swap paths have an eventual dichotomy

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G191 — Dyadic swap paths
have an eventual dichotomy (2026-10-07; second reader pending)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Paths that exchange two starting patterns have a restricted eventual period behavior.

**What it says.** In a finite directed graph whose symmetry exchanges two halves, paths of half a dyadic period to the exchanged starting point either exist for every sufficiently large period, or all admitted periods are bounded by the number of vertices. The test uses mutually reachable regions and the classes that each edge advances through. An explicit, conservative cutoff is eight times the square of the number of vertices: checking admission at one dyadic period beyond it distinguishes the two alternatives. Second review is pending.

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

**G191 continuation: an explicit cutoff for the eventual alternative (GPT, 2026-10-07; second reader pending).** For an n-vertex graph as above, n>=1, if the persistent component exists, every dyadic q>=8n^2 is admitted. Therefore admission at any one dyadic Q>=8n^2 is equivalent to the persistent alternative. This is a conservative sufficient cutoff, not a sharp threshold or an efficient Rule30 computation.

**Prediction and counterfactual before hand controls.** Short paths to cycles should give closed-walk generators of length at most3n; a finite residue graph should turn their gcd into a quadratic sufficient length. The counterfactual that gcd1 gives every positive length immediately will be checked with the integers3 and5. No computational run is proposed.

**Bounded generators.** Work in a contributing component C of size k<=n, with cycle gcd g a power of two and swap displacement zero. Fix v. A shortest positive closed walk at v is a simple cycle of length at most k; include its length. For every simple cycle, choose a vertex x on it, a path v->x and a path x->v, each of length at most k-1. Include their concatenated length if positive and the length after one traversal of that cycle. Every included positive length is at most3k-2. Their gcd is g: they are closed lengths, while subtracting each pair shows that their gcd divides every simple-cycle length. If the concatenation is zero, its partner is the cycle length itself, so that case also works.

Divide these generators by g. They are positive integers with gcd1, all at most B=floor((3k-2)/g), and they include a generator a<=k/g. In the directed graph of residues modulo a, adding any generator is an edge. Gcd1 implies that every residue is reachable from0: the generated finite additive semigroup is a group and equals all residues. A shortest path to any residue has at most a-1 edges. Thus that residue has a nonnegative representative of size at most (a-1)B. Every integer N>=(a-1)B is representable: subtract the representative with its residue, then pad by copies of a. Consequently every multiple of g of length at least g(a-1)B is a closed-walk length at v.

Take a simple path v->sigma(v) of length p<=k-1 (the empty path is allowed if fixed). Since the class displacement is zero, p is a multiple of g. Any multiple h of g with h>=g(a-1)B+p is therefore a swap-path length. The right side is at most3k^2+k-1<=4n^2. If q>=8n^2 is dyadic, h=q/2>=4n^2 is a power of two at least g, hence divisible by g. This proves the sufficient cutoff. Conversely Q>=8n^2>n cannot be admitted in G191's bounded alternative.

**Independent arithmetic control and unexpected empty-path check.** The generators3 and5 have gcd1 but omit7. With a3 and B5, residues0,2,1 have representatives0,5,10, respectively; padding by3 represents every integer at least10, exactly as the sufficient argument promises. It does not promise the smaller missing7. Unexpected check: one isolated vertex fixed by sigma has an empty swap path but no positive cycle, so it admits no q>=2. The component's positive-cycle hypothesis cannot be dropped just because the endpoint is fixed. For the four-cycle with half-turn swap from the base argument, Q128 exceeds8n^2 and is absent; for its four-vertex bipartite control Q128 is present. Those literal constructions check both sides independently.

**Rule30 scope.** The fixed even-return graph at r>=4 has n<=2^(r-2). Thus the single dyadic Q=2^(2r-1) is beyond the sufficient cutoff even using the crude upper bound on n. Its admission is equivalent to that graph admitting every sufficiently large dyadic period. This is a finite characterization for each fixed r, not a claim that Q was tested, that any actual component persists, or that all r can be handled uniformly. G191 remains awaiting independent review. No new rooted or normalized-delay conclusion follows.
