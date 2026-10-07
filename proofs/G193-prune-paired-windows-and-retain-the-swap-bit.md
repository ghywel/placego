# prune paired windows and retain the swap bit in the quotient

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT193. prune paired windows
and retain the swap bit in the quotient (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The paired graph can be reduced while keeping a bit that records exchange.

**What it says.** A lower-order backward function must take opposite values on the two windows at every edge's target. Discarding the other vertices preserves all positive-length closed walks and all positive paths to an exchanged start. In the unordered-pair quotient, an edge bit records an orientation change; its sum distinguishes exchange from ordinary return. Local independently verified the pruning and exchange labels (S89/L160).

**Why it matters.** This makes the swap phase explicit and reduces the state count without discarding the backgrounds. Parallel edge choices must retain their bits. It classifies no larger actual graph and supplies no growth bound.

**An everyday picture.** Two labeled cards can be stored as an unordered pair, provided each move also records whether their order changed. Getting back to the same pair does not by itself say which card is first.

## The formal statement and proof

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
