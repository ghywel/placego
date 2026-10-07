# Genuine quotient branches are separated by at least seven depths

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G159. Genuine quotient branches
are separated by at least seven depths (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Genuine choices of branch cannot occur within seven depths of one another. This limits how quickly distinct histories multiply after time rotations are identified. It does not limit how long a single history can continue or how long it takes to settle.

## The formal statement and proof

**Statement.** On any rooted periodic edge history, two consecutive even-parity zero-driver branch nodes of G158 have depth difference at least7. Consequently the number of temporal-rotation classes at depth n in the common-period-P tree is at most2^ceil(n/7). This is a branch-choice rate bound, not an upper bound on the height of the tree or on physical waiting times.

**Proof.** At an even-parity branch write the profiles starting at its zero driver as0,c,d,e,f,g,h. The previous profile a is nonzero and satisfies Delta c=a, so c is nonconstant. The equation for d is S d=c OR d. A one in the periodic c resets d to1; thereafter1 persists. Periodicity therefore forces d=1. Next S e=1 XOR c, so e is nonconstant. If f=0, its equation S f=1 XOR(e OR f) would force e=1, impossible. Thus profiles c,d,e,f are all nonzero.

If g=0 then its equation forces e=f. Substituting in the equation for f gives S e=1 XOR e, so e and c are alternating and a=Delta c=1. But the constant-one profile has least period1 and odd block parity; it cannot be the even-parity branch under consideration. Hence g is nonzero.

If h=0 then f=g, and the equation for g gives e=f XOR S f. The equation for f is S f=1 XOR(e OR f). At any time with f=0 these two identities imply S f=1 XOR S f, a contradiction. Thus f must be constant1; then its equation would give S f=0, another contradiction. Hence h is nonzero. No zero-driver node occurs in the next six depths, proving the spacing claim.

A path from the root to depth n crosses at mostceil(n/7) binary branch nodes. By G158 all other nodes have at most one child in the rotation quotient. The binary decision words for distinct depth-n nodes are prefix-free (a proper prefix would give the same path until one node already ended at depth n). A prefix-free collection with maximum word length m has at most2^m members, by extending its words to disjoint sets of m-bit strings. Take m=ceil(n/7). The case n=0 has the single root. Square.

**Controls and identified unexpected check (symbolic, no run).** The constant-one predecessor is essential: odd-parity integration gives an alternating c, and the resulting segment0,c,1,c,c,0 has zero drivers only5 depths apart. This is exactly the period-two control and rejects extending the seven-depth claim to all zero drivers. The even-parity local guard a=0110 from G158 is nonconstant and does not trigger that exception. No claim of attainment at distance7 is made. A tree consisting entirely of unary nodes can have arbitrary height while obeying the depth-n count1; this is the unexpected inference guard against converting a branch-rate bound into a settling bound.

**Prior art and dependencies.** The calculation uses G7's recurrence and the pending G158 quotient classification; the six-step exclusion is proved directly here. Existing reset/integration prior art and G156-G158 are the relevant records. No computation or literature novelty claim is made. The number and location of later branch nodes, dyadic-period record spacing and adaptive physical waiting budgets remain open.
