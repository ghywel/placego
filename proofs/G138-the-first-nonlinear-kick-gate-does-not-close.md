# the first nonlinear kick gate does not close the initial tail

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT138. the first nonlinear
kick gate does not close the initial tail (second-read by Local, 2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The first place where Rule 30's "and" matters stays quiet for the powers-of-two pattern, but quiet is not enough.

**What it says.** Reading backwards from the wall, the first five forced columns have exact formulas in column 1's
visible bits, and the fourth contains Rule 30's first product (C7). For the powers-of-two candidate that product
fires only once. But even a constant column 1, where it never fires, forces an endless checkerboard to the left.

**Why it matters.** It starts testing candidates against the wall's own equations rather than repeat tests, and
records why one shallow check cannot certify a finite seed.

**An everyday picture.** One quiet gate does not certify that the rest of the circuit is quiet.

## The formal statement and proof

### G138. The first nonlinear kick gate does not close the initial-tail problem (2026-10-06)

**Status and purpose.** Symbolic wall audit, independent review pending; no experiment. This follows G137's failed entropy bridge by using the actual Rule30 inverse, rather than another repetition inequality. Prediction: the first few forced columns expose an explicit nonlinear product of neighboring visible bits. Counterfactual: sparsity of that product alone makes the entire forced initial row finite or infinite. Neither implication is obtained. This is an exact low-depth reduction and a retained failed bridge, not a new general inversion theorem or prize result.

Write v_j(t)=x_(-j)(t), with v_0(2s)=0 and v_0(2s+1)=1. Let c_s be column 1's visible bit at physical time 2s. The wall forces v_1(2s)=1-c_s and v_1(2s+1)=1. The inverse Rule30 identity is

    v_(j+1)(t)=v_j(t+1) XOR (v_j(t) OR v_(j-1)(t)).

Put A=c_s, B=c_(s+1), D=c_(s+2). Repeated Boolean substitution yields the exact even/odd pairs

    (v_1(2s),v_1(2s+1)) = (1-A,1),
    (v_2(2s),v_2(2s+1)) = (A,B),
    (v_3(2s),v_3(2s+1)) = (1-B,1-B),
    (v_4(2s),v_4(2s+1)) = (A*B,D),
    (v_5(2s),v_5(2s+1)) = (D XOR (A OR (1-B)),1-B).

For example the depth-four even entry is (1-B) XOR ((1-B) OR A)=A*B. Its odd entry is (1-D) XOR ((1-B) OR B)=D. The depth-five odd entry is B*D XOR (D OR (1-B))=1-B: for B=0 both sides are one, and for B=1 both sides are zero. These independent Boolean simplifications check the product and the cancellation without a dynamical run. They apply to the forced left construction; a full right evolution is an additional constraint.

**Dyadic specialization.** For c=d of G137, c_s*c_(s+1)=1 only at s=1, because 1 and 2 are the only consecutive positive powers of two. Depth four's even trace therefore has exactly one one, at physical time 2; its odd trace still contains infinitely many shifted dyadic pulses. The initial row's first five cells are

    (v_1(0),...,v_5(0))=(1,0,0,0,1).

This supplies neither a tail classification nor a finite-left realization. Vanishing on one temporal parity at one depth is not eventual vanishing across all initial depths.

**Unexpected constant-code control.** If c is constantly zero, the same formulas give an all-one depth-one column and then stationary alternating columns 0,1,0,1 through the depths displayed. The inverse recurrence continues that checkerboard to arbitrary depth: whenever two neighboring columns are stationary and opposite, the next outward column is the inner column's complement. Thus the forced initial left row has infinitely many ones even though the depth-four product is identically zero. This is the identified independent check against treating a sparse product as a finite tail. The constant-one case gives a time-alternating depth-one column, stationary one at depth two, then stationary alternating columns 0,1,0,... outward, likewise an infinite initial tail.

**Failed bridge retained.** A long zero segment of c creates a local checkerboard strip, but the strip's temporal margins grow with the number of inverse columns. Dyadic segments move outward in time as their lengths increase. The low-depth identities do not put that strip onto arbitrarily large depths of the single initial row. Nor does the single nonzero product guarantee that all deeper nonlinear products stay sparse. To settle the dyadic candidate, one needs a uniform all-depth invariant for this inverse recurrence, or a certified initial one at unbounded depths. To settle the general prize, the invariant must cover every admissible companion. No additional census or claimed closed finite-state recursion follows from these formulas.
