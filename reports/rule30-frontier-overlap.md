# The OR's overlap term at the read-out frontier (L1062)

28 October 2026, Local, at the owner's request ("Yes, run the test", after L1061). Hand work first, then one cheap
check of every hand claim. Single-party; the carrying steps are short and listed for GPT's read.

**Record searched:** `record_find.py 'right edge.*white run|white run.*right edge|first black.*right|2\^m.*right edge|white triangle'`,
then RULE30-PRIZE §8.27, PROOFS.md item 36 (Proposition 23), GC1998, L1054 and GC2000. Proposition 23 turned out
to carry the frontier itself; nothing in the record treats the overlap term.

**The test, as written first in L1061.** Can the overlap parity at the frontier B(P) be written in terms of earlier
centre bits plus quantities already controlled? *Prediction:* no; it needs a whole off-centre period.
*Counterfactual:* a closed form in polynomially many controlled terms would make the line a lever on Prize 1.

**Result in one line.** This reduction found no centre relation; it does not prove that none exists (GC2002). On the way, the frontier turns out to be an old friend: the place
where the past's copy of the centre first fails is fixed by the white triangle that touches the right edge at time P.

## Set-up

Right diagonal d is D_d(t) = U(t, t − d), so D_0 is the black right edge and the centre is c(n) = D_n(n). Then
D_d(t+1) = D_d(t) XOR g_d(t) with g_d = D_(d−1) OR D_(d−2), and every D_d is purely periodic with a dyadic least
period p_d: 1, 2, 2, 4, 8, 8, 16, 32, 32, 64, … (§8.27; Rowland; OEIS A094605). For P = 2^v, B(P) is the first d
whose period does not divide P, and the past read-out U(n − P, −P) equals c(n) exactly for n < B(P) (GC1998).

Write π(f) for the parity of the 1s of f over any P consecutive times. That is well defined whenever f has a
period dividing P.

## 1. The frontier is Proposition 23 seen from the past (known; the link is new to the record)

Since D_d(0) = 0 for d ≥ 1, π(g_d) = D_d(P) − D_d(0) = D_d(P) whenever g_d has a period dividing P. So for
d ≤ B(P), "p_d divides P" is the same as "cell (P, P − d) is white". Hence

    B(P) = L(P) + 1,

where L(P) is the white run just inside the black right edge at time P. That is exactly Proposition 23 (PROOFS.md
item 36, Cloud, second-read by GPT in GC730, 2026-10-09), which gives L(2^v) = w(v) = 2, 3, 5, 6, 8, 14, 15, 23,
24, 26, 28 … for v = 1, 2, 3 …

*What this changes.*
- GC1998's exact frontier and Proposition 23 are one theorem. GC1998, L1054 and GC2000 did not cite it, and the
  reconstruction reports should credit it.
- The read-out cost is the ruler sequence. Reading n centre bits from the past needs a depth P = 2^v with
  w(v) ≥ n − 1 for the prefix c(0) … c(n−1), and P ≥ n so the copies lie in the past (GC2002's indexing). That is
  the measured "about 2^(n/3)" of L1053, now with an exact source. *Proved since (GC2007, read in L1063):*
  w(v) ≥ 5v/3 − 1, so a depth 2^⌈3n/5⌉ always suffices. A matching lower bound on the cost is not proved.
- In the Rule 60 twin (D_d(t+1) = D_d(t) XOR D_(d−1)(t)), row 2^v is 1 0…0 1 (Lucas), so B(2^v) = 2^v. The
  Sierpiński frontier is linear in P (exact). Rule 30's ruler sequence is logarithmic in the measured range
  only (MEASURED). In that range the OR shrinks the white triangle at 2^v from size 2^v to size w(v).

## 2. The overlap term reduces to two diagonal weights (proved by hand)

At d = B, a OR b = a XOR b XOR ab gives

    π(D_(B−1) · D_(B−2)) = π(g_B) + π(D_(B−1)) + π(D_(B−2)) = 1 + π(D_(B−1)) + π(D_(B−2)).

Each weight π(D_k), for k = B−1 or B−2 (whose period divides P), has three cases:
- If p_k < P, P covers an even number of periods, so π(D_k) = 0.
- If p_k = P and D_k doubled at k (p_k = 2q_k), then D_k(s + P/2) = NOT D_k(s). Exactly P/2 of any P consecutive
  values are 1, so π(D_k) = 0 for P ≥ 4.
- If p_k = P and D_k did not double at k, π(D_k) is the weight of one period. No closed form is known.

So the overlap parity is 1, except when one of the two feeders has period P that it inherited rather than doubled
into. Then it may carry that feeder's period weight: an inherited period allows an odd weight but does not force
one, and two odd weights cancel (GC2002). Here "doubled" means p_k = 2q_k, with q_k the least period of the
forcing g_k. The probe's `doubled` test compares with 2p_(k−1) instead, a proxy, so it does not test this premise
directly. GC2003–GC2004 settle the case: the weight is odd exactly when the forcing is odd on both alternate-tick
classes.

## 3. Where the centre enters (red team on my own reduction)

The P-window of D_(B−1) and D_(B−2) does contain centre cells: exactly c(B−1) and c(B−2), at t = B−1 and t = B−2.
In the overlap sum they appear as the products c(B−1)·U(B−1, 1) and U(B−2, −1)·c(B−2). The other P − 2 products
are off-centre cells:
- about B/2 left-half cells, between the left edge and the centre on those diagonals;
- the rest in the right half.

At P = 64, 256 and 512 there are 17, 60 and 125 nonzero products, of which the two centre products contribute
1, 0 and 1.

So the identity ties two centre bits to the parity of about P other cells. That is the forward rule D_B(P) =
D_B(0) XOR Σ g_B, collapsed by periodicity. It is not a relation among centre bits. No other centre bit c(n) with
n ≥ B appears, because c(n) lies on diagonal n.

A more general reading (hand, short; a reading, not a theorem). Periodicity alone relates c(n) = D_n(n) only to
D_n(n + k·p_n), which are its own copies (in the past for k < 0). Different centre bits lie on different diagonals.
Any constraint between them must therefore come from combining periodicity with the update across diagonals, as
Proposition 23 does for the right edge. Such combinations can reach the centre. For example, if p_n ≤ n, then
c(n) = D_n(n − p_n). With the known p_n > ⌈n/2⌉ (§8.27), that time lies in D_n's initial white run, above the
pyramid, so c(n) = 0 (GC2002 supplied the missing bound). That happens only at n = 2 in the computed range, since
p_n outgrows n quickly. The frontier identity is the natural combination at the read-out's edge, and it reaches the
centre only through a parity of about P cells.

## 4. Check (computed, `tests/probes/wolfram/frontier_overlap.py`)

Forward cells only, P = 4 … 2048. Periods match A094605 up to diagonal 29, and B = 4, 6, 7, 9, 15, 16, 24, 25, 27,
29 matches L + 1 and w(v) + 1.
- H1 (B = L + 1) held for every P.
- H2 (p_(B−1) = P, and p_(B−2) = P or P/2) held for every P. This is *measured*: monotonicity of the periods is not
  proved here.
- H3 (the overlap formula and the zero cases) held for every P.
- The two inherited-period cases with weight 1 occur at P = 8, 64 and 256.

## Verdict

- **The test** (corrected per GC2002): this reduction leaves inherited-period weights unresolved, and no centre
  recurrence was obtained. The two centre bits sit inside a parity over a whole period. That does not prove no
  reduction exists, or that a full period must be read; the conserved-difficulty suspicion stays a CONJECTURE.
- **What it does show about Rule 30:**
  - The reconstruction's frontier and the right-edge white triangles (Proposition 23) are the same object.
  - The read-out cost is the ruler sequence w(v).
  - In the measured range, the OR shrinks Sierpiński's linear frontier to a logarithmic one.
  - The overlap term is exactly 1 except at inherited periods.

**For GPT's read:** §1's identification (one line, given Proposition 23), §2's three weight cases, and §3's reading that
periodicity alone gives only copies, so any centre constraint must combine it with the cross-diagonal update.
