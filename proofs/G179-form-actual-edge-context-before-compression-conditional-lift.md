# form actual edge context before compression; conditional lift pays the first edge

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT179. form actual edge
context before compression; conditional lift pays the first edge (second-read by Local, 2026-10-07)"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Check the real connections first, then simplify the labels.

**What it says.** A budget can be put on pairs of consecutive real steps that share the same middle state, rather
than on single states. If it is bounded and never negative, it turns back into a budget on states, at the cost of
one extra allowance for the first step. Building the pairs after simplifying the labels keeps G178's false loops.

**Why it matters.** It gives the rule for using context. RC2 then tested it at period 8 and passed, but with labels
barely simpler than the full state (398 labels for 411 steps): a finite success, not the small budget the settling
question needs.

**An everyday picture.** Check that two train journeys really share a station before replacing the stations by
summaries; join the summaries first and the lost connection cannot be recovered.

## The formal statement and proof

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
