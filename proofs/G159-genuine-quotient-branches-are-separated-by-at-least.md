# genuine quotient branches are separated by at least seven depths

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT159. genuine quotient
branches are separated by at least seven depths (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Real forks in the tree of edge histories are at least seven steps apart.

**What it says.** After a real fork of G158, the next six steps inward are forced, so along any path real forks come
at least seven steps apart. At depth n there are at most 2 to the power n/7 different histories. The rooted trees up
to period 15 have no real forks at all, each being a single chain; at period 16 the first one comes 53,207 steps in,
as an earlier result (G2.3) had already recorded.

**Why it matters.** It limits how fast the histories can multiply. It does not limit how long a single history can
run, which is what the settling question needs.

**An everyday picture.** On a road whose junctions are at least seven miles apart, the map cannot branch quickly.

## The formal statement and proof

### G159. Genuine quotient branches are separated by at least seven depths (2026-10-07)

**Statement.** On any rooted periodic edge history, two consecutive even-parity zero-driver branch nodes of G158 have depth difference at least7. Consequently the number of temporal-rotation classes at depth n in the common-period-P tree is at most2^ceil(n/7). This is a branch-choice rate bound, not an upper bound on the height of the tree or on physical waiting times.

**Proof.** At an even-parity branch write the profiles starting at its zero driver as0,c,d,e,f,g,h. The previous profile a is nonzero and satisfies Delta c=a, so c is nonconstant. The equation for d is S d=c OR d. A one in the periodic c resets d to1; thereafter1 persists. Periodicity therefore forces d=1. Next S e=1 XOR c, so e is nonconstant. If f=0, its equation S f=1 XOR(e OR f) would force e=1, impossible. Thus profiles c,d,e,f are all nonzero.

If g=0 then its equation forces e=f. Substituting in the equation for f gives S e=1 XOR e, so e and c are alternating and a=Delta c=1. But the constant-one profile has least period1 and odd block parity; it cannot be the even-parity branch under consideration. Hence g is nonzero.

If h=0 then f=g, and the equation for g gives e=f XOR S f. The equation for f is S f=1 XOR(e OR f). At any time with f=0 these two identities imply S f=1 XOR S f, a contradiction. Thus f must be constant1; then its equation would give S f=0, another contradiction. Hence h is nonzero. No zero-driver node occurs in the next six depths, proving the spacing claim.

A path from the root to depth n crosses at mostceil(n/7) binary branch nodes. By G158 all other nodes have at most one child in the rotation quotient. The binary decision words for distinct depth-n nodes are prefix-free (a proper prefix would give the same path until one node already ended at depth n). A prefix-free collection with maximum word length m has at most2^m members, by extending its words to disjoint sets of m-bit strings. Take m=ceil(n/7). The case n=0 has the single root. Square.

**Controls and identified unexpected check (symbolic, no run).** The constant-one predecessor is essential: odd-parity integration gives an alternating c, and the resulting segment0,c,1,c,c,0 has zero drivers only5 depths apart. This is exactly the period-two control and rejects extending the seven-depth claim to all zero drivers. The even-parity local guard a=0110 from G158 is nonconstant and does not trigger that exception. No claim of attainment at distance7 is made. A tree consisting entirely of unary nodes can have arbitrary height while obeying the depth-n count1; this is the unexpected inference guard against converting a branch-rate bound into a settling bound.

**Prior art and dependencies.** The calculation uses G7's recurrence and the pending G158 quotient classification; the six-step exclusion is proved directly here. Existing reset/integration prior art and G156-G158 are the relevant records. No computation or literature novelty claim is made. The number and location of later branch nodes, dyadic-period record spacing and adaptive physical waiting budgets remain open.

*Second reader's note on G159 (Local, 2026-10-07; chat L115).* Correct. After an even-parity zero driver, $c$ is
nonconstant; $d$ is forced to the constant one by the persistent reset; and $e$ is nonconstant. $f = 0$ would make $e$
constant. $g = 0$ forces $e = f$ and then an alternating $c$, so $a = 1$ with odd parity, which is excluded. $h = 0$
gives $e = f \oplus Sf$, which at any zero of $f$ contradicts $f$'s own equation. The width bound is the prefix-free
count. A finding that changes how much any check here can say: on the rooted trees for every $P \le 15$ there is no
even-parity branch node, each rotation quotient is a single chain, and the spacing claim is vacuous there. So S53
(`rule30_audit_g99_g100.py`) also tests the lemma ambiently: below every nonzero even-parity $a$ with zero driver, for
$P \le 8$, all 2,736 continuations keep nonzero drivers for six depths. On the rooted trees it confirms at most
$2^{\lceil n/7 \rceil}$ classes per depth, which is trivially 1.
