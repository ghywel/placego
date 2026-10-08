# two binary potentials test the quotient persistent phase

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT194. two binary potentials test the
quotient persistent phase (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Two yes-or-no equations decide whether a loop region can keep swapping.

**What it says.** For a region of the shrunken map that a walk can circle, two simple equations on the order bits
decide everything: either swaps never happen, or they are locked to one period, or every large enough power-of-two
period allows one.

**Why it matters.** It turns the swap question for any one region into a quick finite test. No larger real region
has been classified.

**An everyday picture.** Two strands of rope coiled together: they may never cross, cross once every turn of the
coil, or cross in a way that fits coils of almost any length; a quick count on one turn shows which.

## The formal statement and proof

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
