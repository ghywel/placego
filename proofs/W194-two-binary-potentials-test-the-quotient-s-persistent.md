# Two binary potentials test the quotient's persistent phase

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G194 — Two binary
potentials test the quotient's persistent phase (2026-10-07; second reader pending)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Two binary equations expose the obstruction to persistent exchange.

**What it says.** On a recurrent labeled quotient component, test whether its exchange labels come from vertex potentials, and whether they do so after adding the cyclic-class wrap bit. The first excludes exchange; the second locks it to one possible dyadic period. If both fail and the component period is a power of two, sufficiently large dyadic periods occur. Independent review and G193's review are pending.

**Why it matters.** This expresses the known component phase test as finite binary equations, while retaining parallel edges. No larger actual component is classified and no growth bound follows.

**An everyday picture.** Marking a complete lap is different from marking every step. A two-track route can keep the tracks apart, exchange them only after one lap, or permit exchange after many lap counts.

## The formal statement and proof

**Conditional continuation of pending G193, using reviewed G191.** Let C be a strongly connected component of G193's labeled quotient, with a positive directed cycle, k vertices, cycle gcd g, and edge labels epsilon in {0,1}. Preserve parallel edge orbits. Assign cyclic classes i(v) in {0,...,g-1}, so each edge increases i by1 modulo g. Define its wrap bit w(e)=1 exactly when i(source)=g-1 and i(target)=0 (for g=1, every edge wraps).

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

**Scope and next question.** This derives an explicit potential form of G191's standard cyclic-class test using G193's standard two-sheet lifting (the graph-cover and finite-state prior methods credited there). No novelty is claimed for those methods. G193 remains independently unreviewed at this writing, so the Rule30 application is conditional on that construction. No actual larger component has been tested, no first-return or rootedness conclusion is added, and normalized growth remains open. Local: second-read the connectivity, wrap equation and the necessary-only q=2g clause; no run requested. The next structural question is whether Rule30's backward recurrence forces either potential on each recurrent quotient component; no such claim is made here.
