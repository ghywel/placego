# only even-parity integration branches the temporal-rotation quotient

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT158. only even-parity
integration branches the temporal-rotation quotient (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

When a rhythm doubles, its two choices are the same choice seen at two moments.

**What it says.** Going inward from the edge, a stripe can split into two possible next stripes. When the period
doubles, the two are the same stripe shifted in time, so counting time-shifted copies once removes the choice. Only
one kind of step, which keeps the period and has an even count of black beats, gives a real fork. Dead ends
outnumber real forks by exactly one.

**Why it matters.** Period doubling is not a free choice, which simplifies the tree of edge histories. How many real
forks there are, and how long the histories take to settle, stays open.

**An everyday picture.** A fork whose two roads are one road seen an hour apart is not a fork.

## The formal statement and proof

### G158. Only even-parity integration branches the temporal-rotation quotient (2026-10-07)

**Statement.** Quotient G7's common-period-P rooted tree by simultaneous temporal rotation of each adjacent pair. It remains a finite rooted tree. At a node represented by (a,b), its number of child classes is classified as follows:

- If b is nonzero, there is exactly one child class.
- If b=0, write q for the least period of a and sigma for the parity of one q-block. The two words cannot both be zero. For sigma=0 there are exactly two child classes, both of least word period q.
- For sigma=1 and 2q dividing P, there is exactly one child class: the two literal children, of least period2q, differ by a rotation through q.
- For sigma=1 and 2q not dividing P, there are no children.

By G157, q is dyadic and divides Q=2^v2(P), so the final case means q=Q. Thus genuine branching in the quotient occurs precisely at even-parity zero-driver nodes; leaves occur precisely when odd-parity integration would exceed the allowed dyadic period. In particular, if E counts the even-parity zero-driver node classes and L counts leaf classes, then L=E+1. Period doubling itself supplies no new branch choice after phase quotienting.

**Proof.** Rotation commutes with B. Every node orbit has a unique predecessor orbit. Distinct depths cannot coincide by G156's first-zero-hit argument; no reconvergence is possible because predecessors are unique. The root is rotation invariant. Hence the quotient is a finite rooted tree. To find its children, rotate any child so that its parent is a chosen representative. Two representative children give the same orbit exactly when a rotation preserving that parent exchanges them.

An active driver b resets the scalar recurrence, as in G157: one complete driver period determines the unique periodic solution c. It has period dividing a common period of a and b, hence divides P. There is one child, before as well as after quotienting.

For b=0 the equation is c(t+1) XOR c(t)=a(t). Choosing c(0) gives exactly two complementary solutions. Summing q steps gives c(t+q)=c(t) XOR sigma. If sigma=0, both solutions are q-periodic. Their least periods are exactly q: any period of c is a period of its difference a, so it must be divisible by q. If sigma=1, their least periods are exactly2q for the same reason, and their q-shifts are their complements. Such solutions close at period P if and only if2q divides P.

Finally the stabilizer of (a,0) consists precisely of shifts divisible by q. For sigma=0 those shifts fix each child and cannot exchange the complementary solutions; for sigma=1 a shift by q exchanges them. This proves the child-class counts. A finite rooted tree with outdegrees0,1,2 has L=E+1 by counting edges in two ways. Square.

**Symbolic controls and identified unexpected check.** At P=1, the three G156 nodes form one chain and the last node (1,0) is the excluded-doubling leaf. At P=2, a nonzero word of least period1 has odd block parity, and a binary word of least period2 is01 or10, also odd. There are therefore no even-parity branch nodes; the quotient is one chain, with its eight nodes given by G156. The apparent first doubling is two phase copies of one continuation.

The unexpected even-parity guard is a=0110, of least period4: with b=0 its solutions are c=0010 and1101. Their child pairs are not rotation equivalent, because any rotation fixing the parent a is a multiple of4. This is a local transition check, not a claim that this parent lies in the rooted tree. By contrast a=01 integrates to0011 and1100, exchanged by rotation through2. Confusing these two parity cases would erase actual possible quotient branching.

**Prior art and scope.** The scalar reset/integration classification is the existing mechanism of Nersissian section4, Theorems10-12, and G7. The additional statement here classifies child orbits using the parent stabilizer; the record's G152 spatial quotient is different and need not be a tree. G157 is a pending proof dependency for the dyadic leaf identification, while the child-orbit calculation above holds without that dependency whenever a is periodic. No novelty is claimed for reset, integration or elementary tree counting. No new computation, larger graph census, uniform bound on E, period-growth upper bound, physical settling bound or prize solution is asserted.

*Second reader's note on G158 (Local, 2026-10-07; chat L115).* Correct. A rotation taking one child $(0, c_1)$ to
another $(0, c_2)$ must fix the parent, since $B$ commutes with rotation and both children map to $(a, 0)$. So the
relevant rotations are the shifts by multiples of $q$. They fix each $q$-periodic solution when $\sigma = 0$, and
exchange the two complementary solutions when $\sigma = 1$. The leaf count $L = E + 1$ is edge counting in a tree with
outdegrees at most 2. Checked (`rule30_audit_g99_g100.py`, S52): on the rooted trees for $P \le 15$, every node's
child-class count follows the rule, leaves exceed branch classes by one, and $P = 1, 2$ are chains. Because those trees
turned out to contain no even-parity branch at all, the rule was also checked ambiently at every pair of $P$-periodic
words for $P \le 8$, including 236 pairs with two child classes. The two local guards check in time order.
