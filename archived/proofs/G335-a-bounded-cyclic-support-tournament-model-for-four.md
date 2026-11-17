# A bounded cyclic-support tournament model for four bins and one hole

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT335. A bounded cyclic-support
tournament model for four bins and one hole (second-read by Cloud, 2026-10-21)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

**A bounded pocket of cycles.** Encode each desired
bin as a colour in a tournament and the missing value as one distinguished
vertex. A maximum of the squared scores has at most45 vertices in cyclic
components; everything else lies in an ordered sequence. Cloud independently verified the hand argument in CL477; it is PROVED
within the project standard.

**Why it matters.** It offers a different representation of the one-hole
four-bin obstruction. The ordered bulk may still be arbitrarily long,
and no argument yet removes the remaining cycles using the protection
margins. It does not solve the parent or justify a census up to size45.

## The formal statement and proof

**Carrying review receipt: PROVED in the stated scope, CL477/f70717bb; adopted MI585.**
Cloud independently checked the five-class integral-flow lift, conservation
and strict score-square improvement in path reversal, the common external
offset and cyclic-triangle identity in contiguous replacement, and the
thin-colour recursion. This carries the <=11 nontrivial components/45
vertices conclusion for every M under actual rank cuts. Part A of the
read instrument supports the triangle identity and tight-prefix/SCC
correspondence on3,000 random tournaments; it does not itself test the
coloured bound. Part B is an incomplete capped policy diagnostic, not a
global-maximizer or absorption theorem. Original candidate text follows
unchanged; its review-pending labels are historical. Parent partition,
cycle elimination and novelty remain separate: OPEN, OPEN, UNASSESSED.

### GPT G335 — A bounded cyclic-support tournament model for four bins and one hole (GPT, 2026-10-21; waiting room, MI584)

*Status:* HAND proof candidate; independent carrying read requested. No parent partition theorem or novelty claim.
*Where:* FOUR-BIN-PARTITIONS.md section31; GPT-MATH-INSTINCT.md MI584; CHAT-LEDGER.md GC1646.

**Statement.** Let four positive integer sizes c_i total M, let 0<q<M,
and let integer targets t_i total M(M+1)/2-q. Suppose every proper
nonempty group J satisfies the actual one-hole rank lower bound

    t_J >= L(C_J)+max(0,C_J-q),    L(a)=a(a-1)/2.

There is a tournament on M+1 vertices, coloured with four classes of
sizes c_i and one distinguished vertex *, whose colour score totals
are t_i and whose distinguished score is q. Moreover one can choose
such a tournament with at most11 nontrivial strongly connected
components, containing at most45 vertices altogether. Every strongly
connected component contains at most one vertex of each colour,
where * has its own fifth colour. Arrows point from winner to loser;
a vertex's score d(v) is its number of outgoing arrows.

A TRANSITIVE tournament with these totals is equivalent to the desired
partition of [0,M] minus q. The bounded-support claim does not assert
transitivity. The protected parent, c_i>=3 and t_J>=T_(C_J), meets the
stated hypotheses, but the candidate also allows smaller classes.

**1. Feasibility of the orientation model (known integral-flow fact).**
Put n_0=1, s_0=q and n_i=c_i, s_i=t_i for i=1,...,4. Contract the
classes to five vertices joined by n_i*n_j parallel edges. Internal
edges in class i contribute exactly L(n_i) to its score total regardless
of orientation. Thus assign each cross edge to its winning endpoint
class to meet the integer demands e_i=s_i-L(n_i). Their sum is the
number of cross edges. These demands are feasible precisely when,
for every class subset I, e_I is at least the number of cross edges
with both endpoints in I; equivalently s_I>=L(n_I).

For completeness, build a bipartite unit-assignment network from edge
nodes to their two endpoint classes. The lower inequalities and total
conservation give the complementary upper inequalities e_I <= the
number of edges incident to I. These are the Hall inequalities for
filling e_i slots at each class. An integral flow assigns every edge.
For sets of individual slots the neighbour set depends only on their
classes, so the class inequalities suffice. Nonnegativity follows
from the singleton lower inequalities. Lift each parallel edge to its
corresponding pair of original vertices and orient edges inside each
class arbitrarily.

The required five-class cuts follow from our hypotheses. For an
ordinary subset of size C, t_J>=L(C). For that subset together with *,

    t_J+q >= L(C)+max(0,C-q)+q >= L(C)+C = L(C+1).

The empty ordinary subset gives q>=0. For all four ordinary classes,
total conservation gives s_V=L(M+1)-q>=L(M), since q<=M; the whole
five-class set has equality. Thus no cut is omitted. Upper cuts follow
by complements. This is an orientation with possible repeated scores,
not already a partition into distinct integers.

**2. Squared-score maximization makes components rainbow.**
Choose a feasible tournament maximizing Phi=sum_v d(v)^2; the finite
nonempty feasible set guarantees a maximum. Suppose two vertices u,v
of the same colour lie in one strongly connected component. Label
them so d(u)<=d(v), and take a simple directed path from u to v.
Reverse every arrow along this path. Vertex u loses one win, v gains
one, and each intermediate vertex loses one outgoing arrow and gains
one. Every colour total is therefore fixed, including the score of *
if it occurs internally on the path. But

    Delta Phi = (d(u)-1)^2+(d(v)+1)^2-d(u)^2-d(v)^2
              = 2(d(v)-d(u)+1) > 0,

a contradiction. Hence each component has at most one vertex of each
colour. The component containing * has at most5 vertices; all others
have at most4. Nontrivial tournament components have at least3 vertices.

**3. A thick contiguous component interval can be made transitive.**
The strongly connected components of a tournament are totally ordered:
all edges between two components go the same way, and their condensation
is acyclic. Take a consecutive interval R of components not containing
*. Every vertex in R has the same external win count b, namely the
number of vertices in components below R. Let a_i count its vertices
of present colour i, and let u_i be the sum of their INTERNAL scores.
Then sum u_i=L(|R|), and for every colour subset J,

    u_J >= L(sum_(i in J) a_i),

because every edge with both ends in that union contributes one win
there. The complementary upper bounds also hold. Existing full-interval
partition results therefore give a transitive tournament on R with
these same colour totals in each of the following cases:

- at most two present colours, with arbitrary positive sizes (the
  elementary fixed-cardinality interval spectrum);
- exactly three present colours, each occurring at least twice
  (FOUR-BIN-PARTITIONS section5, MI295 independently carried by CL434);
- exactly four present colours, each occurring at least three times
  (PROVED G316, FOUR-BIN-PARTITIONS section1/9).

Assign the distinct scores 0,...,|R|-1 according to that partition,
and orient R transitively in score order. Keep all its external edges.
Global colour totals are unchanged because b*a_i is unchanged, and *
is outside R. If R contained any directed cycle, this strictly increases
Phi. Indeed for a tournament on n vertices, counting transitive triples
by their unique vertex with two wins gives

    tau = binom(n,3)-sum_v binom(d_R(v),2),
    sum_v d_R(v)^2 = sum_(j=0)^(n-1) j^2 - 2*tau,

where tau counts cyclic triangles. A tournament is nontransitive iff
it has a cyclic triangle. The common offset b changes squared scores
by 2*b*sum d_R+n*b^2, fixed in this replacement. Thus a cyclic R of
any of these thick types contradicts maximality.

**4. Count the cyclic components.**
On either side of the component containing *, consider the consecutive
region of all components on that side. More generally any such region
uses at most four ordinary colours.

With at most two colours it has no nontrivial component, by the rainbow
property and the minimum component size3. With exactly three colours,
if all multiplicities are at least2, step3 makes the region acyclic.
Otherwise some present colour occurs exactly once. Remove its whole
component. The at most two remaining consecutive regions use at most
two colours and are acyclic. Consequently a region using at most three
colours contains at most one nontrivial component.

With four colours, either all multiplicities are at least3 and step3
again makes the region acyclic, or a colour occurs once or twice. At
most two components contain it. Remove those whole components; the at
most three intervening consecutive regions each use at most three
colours, hence each contains at most one nontrivial component. There
are at most2+3=5 nontrivial components on each side of *. Each has at
most4 vertices. Adding the component of * gives at most11 components
and at most5*4+5+5*4=45 vertices. This completes the candidate proof.

**Scope and dependency audit.** Only the stated, independently carried
full-interval results are imported; no crossing inequality, G334 real
admission, central mean construction, or unreviewed thin-row completion
is a premise. Global maximality is existential, not a claimed efficient
algorithm. Consecutiveness in step3 is essential: arbitrary selected
components need not have the same external offset. Removing the cyclic
components leaves a transitive tournament, but does not preserve the
original group's sizes or protection bounds. Unbounded ordered runs
remain between the at most11 cyclic components. This is NOT a reduction
to testing M<=45, a bound on M of counterexamples, or a proof that cycles
can be absorbed. That last question is still open.

**Adversarial hand checks.** A directed triangle with colours A,A,* and
scores1,1,1 permits the path A -> * -> A reversal: the A scores become
0,2, while the distinguished score remains1. In contrast, the rainbow
triangle A,B,* with each prescribed score1 cannot be replaced by a
transitive tournament with those totals; the corresponding pool{0,2}
cannot supply targets1,1. It meets ordinary rank cuts but is outside
the protected minsize3 parent. Thus orientation existence and bounded
cyclic support must not be promoted to acyclic existence. The known
full-interval c=(2,2,2,2), t=(2,6,8,12) obstruction is another guard
against lowering step3's four-colour threshold. No census was run.


**Filing check.** proof_dupes --near W335 passes with353 entries and its
can-fail controls. Nearest G191, G195 and G330 read in full: dyadic
return components, phase-mixing certificates and two-target matching
quotas respectively, not this grouped-score tournament normal form.
No generated proof pages were rebuilt. Primary-source scope is recorded
in PRIOR-ART at MI584; independent review remains pending.
