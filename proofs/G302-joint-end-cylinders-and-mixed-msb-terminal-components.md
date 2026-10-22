# Joint end cylinders and mixed MSB terminal components (second-read by Local, L737)

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT302. Joint end cylinders and mixed
MSB terminal components (second-read by Local, L737)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Numbers that reach the ternary01 set after multiplication by a power of4 can have any prescribed fixed
leading block, low unit1-residue and numeral-length residue, all at once. The relevant forward orbit
meets the same cylinders. PROVED after Local L737; small exact controls pass.

**Why it matters.** A regular invariant would need mixed terminal components in MSB as well as LSD order.
Bounded information at both ends cannot decide it; finite middle memory and multiplication remain open.

## The formal statement and proof

### GPT G302 — Backward Cantor hits meet every joint end cylinder (2026-10-15; GC1274-1275)

*Status:* PROVED, carrying second read Local L737 atc06fbb3f; finite arithmetic controls COMPUTED separately.
*Bears on:* K2-prime in8.113, via G298's backward-hitting set. No general automaton barrier or Erdős conclusion.
*Dependencies:* G298's separated-digit congruence construction and the known primitive-root identity for4 mod3^k;
Lagarias math/0512006 section2's leading-digit irrational rotation, now used on an arithmetic exponent class.
No novelty claim for those tools or an exhaustive literature claim for the formulation.

**Notation.** C-star is the positive integers whose ternary digits are only0 and1;
B-star={n>=1:4^j*n belongs to C-star for some j>=0}. Fix h,k,M>=1, an h-digit canonical ternary prefix of
integer value p (3^(h-1)<=p<3^h), r modulo3^k with r=1 mod3, and a modulo M. Let D(p,r,a) be the integers
whose leading h digits are p, whose residue modulo3^k is r, and whose ternary length lambda satisfies
lambda=a mod M. Only integers long enough to have these digits are considered.

**Claim.**
1. D(p,r,a) contains infinitely many B-star integers.
2. For every positive x=1 mod3, it contains infinitely many integers4^t*x, t>=0.
3. Hence any set L holding such an x, satisfying4L subset L and avoiding C-star, has infinitely many members
   and infinitely many nonmembers in every D(p,r,a). In particular membership on the unit1 stratum cannot
   eventually be a function of bounded leading digits, bounded trailing digits and length modulo a fixed M.
4. For a finite MSB-first DFA recognising such an L, every state reachable by a canonical positive prefix has
   both an accepting and a rejecting continuation. Every terminal SCC reachable by a canonical prefix is mixed.
These are necessary conditions, not the assertion that no such regular L exists. G297 provides the separate
state-preserving unit normalization when the initial witness has positive3-adic valuation.

**1. Choose the multiplier without losing the low residue.** Powers of4 generate the units1 mod3 modulo3^k,
as used in G298: v3(4^(3^s)-1)=s+1 gives order3^(k-1). Thus choose j0 with4^j0*r=1 mod3^k. Every
j=j0+3^(k-1)*t has4^(-j)=r mod3^k. On this progression, fractional parts of -j*log_3(4) are dense, because
log_3(4) is irrational and a nonzero integer multiple remains irrational. Choose j>=1 and an integer d with

    p*4^j < 3^d < (p+1)*4^j.                         (J)

The open leading-prefix interval guarantees such a choice: its logarithmic fractional interval is
(log_3(p)-(h-1),log_3(p+1)-(h-1)), with the appropriate integer translate. This is ordinary irrational rotation
after restricting j to one residue class, not a new independent multiplier or an inference from two separate
marginal densities. Put m=4^j; the strict bounds in(J) will give an exact prefix margin.

**2. Restore divisibility while leaving room for one high digit.** Let P=lcm(ord_m(3),M), so3^P=1 mod m.
Choose N0 with N0=a+d-h mod M, for instance0<=N0<M. Define

    c = -(3^N0+1)*3^(-k) mod m, chosen in{0,...,m-1},
    B = 1 + sum_(t=0)^(c-1) 3^(k+tP).

The sum is empty when c=0. Its exponents are distinct and at least1; B is ternary01 and B=1 mod3^k.
If c>0 put E=k+(c-1)P; if c=0 put E=0. Then B<3^(E+1). For every sufficiently large N=N0 mod P with
N>=max(k,E+d+1), set

    y=3^N+B, n=y/m.

The high exponent N exceeds all exponents of B, so y is a positive ternary01 integer. Modulo m,
y=3^N0+1+c*3^k=0, hence n is an integer in B-star. Modulo3^k it is m^(-1)=r.
By(J) and B<3^(E+1)<=3^(N-d),

    p*m*3^(N-d) < 3^N+B < (p+1)*m*3^(N-d).

For the upper bound, the integer margin(p+1)m-3^d is at least1, strictly larger after multiplication than B.
After division by m, n has leading h-digit block p and length lambda=N-d+h. Since P is a multiple of M and
N0=a+d-h mod M, lambda=a mod M. Increasing N by P strictly increases n without changing the requirements.
This proves infinitely many B-star points in the joint cylinder, with all finite leading/trailing constraints
realized by THE SAME integers. There is no assertion that every fixed-scale cylinder controls the middle digits.

**3. Forward orbit in the SAME joint cylinder.** Given x=1 mod3, choose t0 so4^t0*x=r mod3^k. All
t=t0+u*s, u=3^(k-1), have that same low residue. Their logarithms base3 are

    beta+s*u*log_3(4), beta=log_3(x)+t0*log_3(4).

Modulo M this is an irrational rotation. Its orbit visits the open interval a-1+I_p modulo M infinitely often,
where I_p=(log_3(p)-(h-1),log_3(p+1)-(h-1)) subset[0,1]. Such a visit gives floor(log_3(4^t*x))+1=a mod M
and leading prefix p simultaneously. Taking arbitrarily late visits makes the words arbitrarily long.
This uses a single rotation modulo M, rather than assuming independence of a length residue and a mantissa.

If4L subset L and x in L, these orbit points lie in L. Also L is disjoint from B-star: otherwise iterating
closure sends a member into C-star. Thus the preceding B-star points are nonmembers. Any proposed bounded-end/
length-residue membership function is constant on each sufficiently long cylinder; both populations contradict it.
No regularity is needed up to this point.

**4. MSB finite-state consequence.** Every canonical prefix p has both an accepted and a rejected canonical
extension, by the preceding statement (use any k>=1 and choose r=1 mod3,M=1). For any state reached by that
prefix, these extensions supply accepting and rejecting continuations. If it lies in a terminal SCC, all
continuation paths stay there, so it contains both accepting and rejecting states. In an n-state DFA each
kind has a shortest continuation of length at most n-1 (an empty continuation is permitted). This extends
G298's necessary LSD terminal-component condition to MSB reading by a DIFFERENT leading-digit argument.
It does not assert a common state count in the two directions or justify changing Local's already registered
solver encoding/runs. Finite-state middle information can still distinguish arbitrarily long words.

**Registered controls.** GC1274/62219a4a preceded execution of erdos_gpt_two_ends.py. With j,k,h=1..3,
M=1..3 and every length class, all162 base constructions and162 larger N+P lifts pass independent integer
division, ternary-digit, prefix, residue and length checks. Largest tested numeral length2542. The wrong
correction c=-3^(-k) mod m omits the high digit and fails divisibility in all162 cases; failures retained as
controls. Fifteen wrong-low-sign controls remain2 mod3 and outside C-star. Unexpected: the first construction
is n=190=(21001)_3,4n=760=(1001011)_3, so B-star can begin with2 although its multiple is ternary01.
These finite cases do not prove rotation density or the quantified automaton condition; those are hand steps.

**Limits and countercontrol.** L={unit1 mod3 with leading digit2} avoids C-star and meets every allowed LOW
cylinder, as in G298, but not every leading cylinder. It is not x4-closed:64 is in it and256 is not. Thus the
new leading/mixed-MSB constraint removes this former necessary-condition countercontrol; it still does not
prove K2-prime. The wrong-sign invariant{n:lowest nonzero ternary digit2} remains a valid x4-closed avoider
without the required witness, so that witness cannot be dropped. No new Mahler coupling or prize claim.

**Joint-cylinder countercontrol.** A stronger regular control is J={n=1 mod3: the ternary numeral has an
odd number of2s}. It avoids C-star and has members AND nonmembers in every joint cylinder above: for any
sufficiently large allowed length, keep both fixed ends and change one unconstrained middle digit0 to2.
This toggles membership without changing the ends or length. But7=(21)_3 is in J and4*7=28=(1001)_3 is not.
Thus even regularity plus the full joint-cylinder conclusion is insufficient; multiplication closure still
carries the unresolved obligation. Fixed end widths may NOT grow with the integer's total length in the proof.
The construction gives no uniform bound allowing them to exhaust the numeral.

Filing check: proof_dupes --near W302 passes. Nearest G298, G297 and G41 read in full. G298 is the lower-end
construction extended here; G297 supplies unit normalization; G41 is a Collatz free-pair estimate and does
not combine leading and trailing numeral constraints. This is an explicit extension of G298, not its restatement.

**Independent carrying second read (Local, L737, 2026-10-15; appended 13:56 BST, after the first append failed on a
line-broken anchor). VERIFIED.** The four points GC1275 asked for:
- *The exponent class.* On j = j0 + 3^(k-1) t the low residue 4^(-j) = r mod 3^k is fixed, since 4 has order 3^(k-1).
  As 3^(k-1) log_3 4 is irrational, the fractional parts of -j log_3 4 are dense, and (J) holds for infinitely many j.
  The target interval (log_3 p, log_3 (p+1)) shifted by h - 1 has positive length inside [0, 1].
- *The top-term correction.* With 3^P = 1 mod m and N = N0 mod P:
  - y = 3^N0 + 1 + c 3^k = 0 mod m, which is exactly why c carries 3^N0 (the wrong control without it fails);
  - y = 1 mod 3^k for N >= k, so n = m^(-1) = r mod 3^k;
  - the exponents of y are distinct, since N > E.
- *The prefix margin.* (J) times 3^(N-d) puts 3^N strictly between p m 3^(N-d) and (p+1) m 3^(N-d). The integer gap
  (p+1)m - 3^d >= 1 times 3^(N-d) exceeds B, because B < 3^(E+1) <= 3^(N-d). After division by m, n lies strictly
  between p 3^(N-d) and (p+1) 3^(N-d): leading block p, length N - d + h = a mod M (M divides P).
- *The forward orbit.* Rotation by 3^(k-1) log_3 4 on R/MZ is dense. A value v = log_3(4^t x) in a - h +
  (log_3 p, log_3 (p+1)) mod M has floor(v) = a - 1 mod M and leading block p, fixing the prefix and the length
  class together.
- *Mixed MSB terminal components.* With M = 1, any canonical prefix has members (the orbit, by closure) and
  nonmembers (B-star, disjoint from L) among its long extensions. So each reachable state has accepting and
  rejecting continuations, and a reachable terminal SCC holds both.
- *The examples.* 190 = (21001)_3 with 760 = (1001011)_3, and the countercontrol J (an odd number of 2s, 1 mod 3:
  toggle a middle 0 and 2; 7 = (21)_3 in J, 28 = (1001)_3 not) are correct.

Status: PROVED (a proof with a second reader), as necessary conditions only, as stated.
