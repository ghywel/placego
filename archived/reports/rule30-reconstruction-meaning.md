# GC2000 — what selecting the white-right past changes

28 October 2026. Owner asks whether reconstruction is a trick, an altered problem, or useful mathematics. Hand analysis only; no numerical run, schedule change, submission or new Local assignment. G122 is an established independently reviewed result, recovered from the older record. The finite-patch formulation and nonlocality check below are elementary hand consequences, not a novelty claim or independently reviewed new theorem.

Record searched: `record_find.py 'right.bound.*biject|white.right.*unique|inverse.*continu|entire.*past.*wedge|finite.*patch.*past'`, then direct reading of archive/gpt/RULE30-GPT.2.md G122–G124, RULE30-PRIZE.md 8.27, GC1998 and the actual inverse/readout source. G122 already proves the required bijection; G123–G124 already classify the canonical ancestor backgrounds more sharply than the recent period-3 observation. These are recovered knowledge, not new discoveries.

## 1. A boundary convention selects a history; it does not alter the future

Let R be the set of binary rows eventually zero to the right, allowing infinitely many black cells to the left. G122/L077 establishes that Rule 30 is a bijection R -> R. For output y, choose B beyond its last possible black cell, set predecessor bits x_B=x_(B+1)=0, and descend using

    x_(i-1) = y_i XOR (x_i OR x_(i+1)).

A larger B adds only zero steps and gives the same answer. For uniqueness, if two R predecessors differ, let j be their rightmost difference. Their outputs differ at j+1 because the other two inputs there agree. Hence two such predecessors cannot have the same output. This is the known proof, included to expose what information is used.

All full-line ancestors obeying Rule 30 remain valid ancestors. R singles out one of them at every backward step. Thus 'the only valid past' must read 'the unique past in this specified class'. We have added a selection convention for an extended problem at negative times. We have changed neither Rule 30 nor the seed nor any nonnegative-time cell in the prize problem. The convention does not consult the centre's answers, and works for every row in R, not just this seed.

It would change the prize problem to forbid other legal futures, force centre bits, or assume finite support at negative times. None is part of this construction. In fact the first selected predecessor of the isolated seed is black throughout the left half-line, so finiteness cannot be imported backwards.

## 2. What reconstructs is every finite patch, not just the centre

Use GC1998's U(t,x), defined for all integer times. Let D_d(t)=U(t,t-d), with D_d=0 for d<0. Each d>=0 has a finite dyadic least period p_d. For a finite set of future locations A, choose a power of two P greater than every time in A and divisible by p_0,...,p_N, where N=max(0,max_(t,x in A)(t-x)). Then at each point of A,

    U(t-P,x-P) = D_(t-x)(t-P) = D_(t-x)(t) = U(t,x).

Points with t-x<0 are zero on both sides. The translated patch lies entirely before time zero. Translation preserves adjacency and every included local update. Consequently a whole finite pyramid through height H has an exact copy in the chosen past, by covering diagonals through depth 2H. A centre prefix is one narrow example of this general phenomenon.

This answers a cheap objection: matching the centre is not evidence that the selection secretly fitted the centre. The established diagonal recurrence explains the larger copying property without reading its answers.

There is also an exact limit. For P=2^m, let B(P) be the first d with p_d not dividing P. GC1998/L1054 proves that translation by (-P,-P) agrees at all times on every d<B(P), and complements at all times on d=B(P). The earlier proof already holds for every t; the band formulation adds no new carrying inference. Thus the first failed diagonal is not a statistical accident. Unbounded diagonal periods ensure such a B exists for every fixed dyadic P.

Every finite patch therefore has a past copy, but no fixed dyadic translation copies the entire history. These quantifiers cannot be interchanged. Nor does this failure prove that the centre is nonperiodic: simultaneous space-time translation and vertical time translation are different statements.

## 3. Unexpected check: a unique inverse need not be local

Here is a hand counterexample to a tempting computational inference. Let Z be the all-white row, and S_N a row with its sole black cell at position N>0. They agree on every prescribed window about zero when N is far enough away. The selected inverse of Z is Z. The selected inverse of S_N is

    x_i=1 for i<=N-1;   x_i=0 for i>=N.

Check the update: triples entirely on either constant side output zero; at N-1 the triple 110 outputs zero; at N the triple 100 outputs one. Hence its output is exactly S_N, and G122 supplies uniqueness.

The two selected inverse rows disagree at the origin for every N>0. Therefore no fixed-radius local rule computes this inverse on R. In the usual topology of agreement on larger finite windows, S_N tends to Z but their selected inverses do not tend to the selected inverse of Z. The inverse is discontinuous there. Set-theoretic bijectivity on R must not be described as a reversible cellular automaton with a local inverse.

This is not a lower bound on the effort needed to compute the single-seed centre, nor an objection to algorithms supplied with a known right edge. It identifies exactly what uniqueness does not buy: uniformly local backward access on this whole class.

## 4. Utility and the remaining question

No extra independent information about the future enters: the exact rule and seed already determine it. A new representation can nevertheless reveal relations that were hard to see, just as factoring a known expression reveals its roots. Here we have a canonical history without backward branching, exact finite-patch copies, and a precise parity obstruction at their first unsupported diagonal. Those are concrete mathematical uses. Neither a faster algorithm nor a prize proof has been obtained.

The Rule 60 control in GC1998 remains decisive: its centre is constant, yet it has the same dyadic copying and growing first-failure mechanism. This defeats the inference 'reconstructible from increasingly elaborate pasts implies nonperiodic centre'. The feature doing additional work would have to involve Rule 30's particular coupling between diagonals.

The better question is whether this representation produces a usable relation between previously uncontrolled centre bits, or a cheaper way to evaluate them, with a proof that does not presuppose those bits. A translation of the original prize statement is insufficient. A useful relation need not solve the prize immediately, but must constrain something beyond the copies already explained by diagonal periods.

Verdict: the selection is legitimate for studying the original future, provided its extra boundary convention is explicit. Reconstruction is an exact structural representation, not independent evidence for the prize. The finite-patch result broadens our understanding; the nonlocality example prevents an unjustified shortcut claim. The question stays open here for the owner's discussion, with no new experiment or review job dispatched.
