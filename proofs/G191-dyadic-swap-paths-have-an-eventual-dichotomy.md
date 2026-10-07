# dyadic swap paths have an eventual dichotomy

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT191. dyadic swap paths have
an eventual dichotomy (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Paths that exchange two starting patterns have a restricted eventual period behavior.

**What it says.** In a finite directed graph whose symmetry exchanges two halves, paths of half a dyadic period to the exchanged starting point either exist for every sufficiently large period, or all admitted periods are bounded by the number of vertices. The test uses mutually reachable regions and the classes that each edge advances through. An explicit, conservative cutoff is eight times the square of the number of vertices: checking admission at one dyadic period beyond it distinguishes the two alternatives. Independently reviewed by Local (L157, S85-S87).

**Why it matters.** Applied to G190, this characterizes the weaker question of whether absolute return delays grow. In the Rule30 graphs, a persistent component must contain branching within that component; a single cycle cannot suffice. The actual return graphs remain unclassified; it establishes neither normalized growth nor a path from the root.

**An everyday picture.** Two markers move around a circular track. Exchanging their starting positions can preserve their position in the repeating schedule, or shift it halfway around. Those two arrangements permit different journey lengths.

## The formal statement and proof

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
