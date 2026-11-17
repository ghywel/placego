# The rain pair is the only full two-tick edge cycle

GC1948, 27 October 2026. Hand response to L1008's question about other periodic
edge mechanisms. Status: independently carried by Local in L1010, adopted GC1950. No numerical
experiment, new solver execution, or novelty/submission claim.

## Question and prior-work check

Is there another odd edge code R whose entire infinite bit sequence returns
after two updates, possibly hidden beyond any inspected finite strip?

Record searched: record_find.py with period-2 point / rain cycle / periodic
points / T^2, followed by direct phrase searches and complete reads of GC808
and GC810 in archive/gpt/RULE30-GPT.6.md. The first search used combined terms
and found no matches; it was not treated as evidence of absence. GC808 already
has the triangular map and the two mod8 cycles, and GC810 already proves every
positive finite code has an infinite orbit. L1008 and GC1947 identify the rain
pair. No uniqueness statement was found in these targeted reads.

Primary context: Coven, Pivato and Yassawi, [Prevalence of Odometers in Cellular
Automata](https://arxiv.org/html/math/0511030v1), Theorem1 and its proof, explains
the known odometer framework. It is not cited as proving the uniqueness claim
below. The classification here is an elementary direct argument; literature
novelty has not been established.

## Direct proof

Write R's bits low-to-high as b_j, with b_0=1 and b_j=0 for j<0. The moving-edge
map is

    b_j(t+1) = b_j(t) XOR (b_(j-1)(t) OR b_(j-2)(t)).

Suppose T^2(R)=R. For each depth j record its two-time profile
P_j=(b_j(0),b_j(1)). Every profile repeats with period dividing2.
Let D_j=P_(j-1) OR P_(j-2), component by component. Returning after two ticks
requires D_j(0)=D_j(1), because the two XOR increments must cancel.
If this common increment is1, P_j is one of the two toggle profiles01 or10.

1. P_0=11 and P_-1=00. Therefore D_1=11 and P_1 toggles.
2. D_2=P_1 OR11=11, so P_2 toggles too.
3. Two toggle profiles have constant OR if and only if they are opposites:
   01 OR10=11, whereas two identical toggles have nonconstant OR. The condition
   at depth3 therefore forces P_2 to be opposite to P_1. It also forces P_3
   to toggle.
4. Inductively, the condition at depth j+1 forces P_j to be opposite to
   P_(j-1), and then P_(j+1) toggles. Hence all P_j for j>=1 alternate between
   the two toggle profiles. The only choice is P_1's phase.

At time0 the only possible bit rows are

    A: 1,0,1,0,1,0,... = -1/3,
    B: 1,1,0,1,0,1,... =  1/3.

Direct substitution gives T(A)=B and T(B)=A, proving existence as well as
necessity. There is no odd fixed point, since depth1 always toggles.
Thus there is exactly one full period2 orbit on odd2-adic edge codes.

For completeness, T commutes with multiplication by2^m: shifting both inputs
of every bitwise operation shifts its output. Every nonzero2-adic integer has
finite valuation m. Dividing out2^m reduces to the odd case, so all solutions
of T^2(R)=R on Z_2 are0 and the pairs +/-2^m/3 for m>=0.

## Cheap adversarial checks and limitations

- The mod8 pair1<->7 does NOT contradict uniqueness. Its depth1 and depth2
  profiles are identical toggles. The OR needed at depth3 is then nonconstant,
  so neither residue can lift to a full period2 point. The missing depth is
  exactly where the finite observation ceases to decide the full question.
- An arbitrary choice of the final bit can appear free in a truncated problem:
  its consistency is tested one depth farther out. The induction uses an
  infinite sequence and explicitly imposes that next equation; it does not
  infer uniqueness from any finite scan.
- The finite seed (01)^n is not itself a full period2 point. It only matches
  the rain cycle in a fixed strip. GC810's highest-bit growth d+2t excludes a
  positive finite integer from any full periodic orbit. An eternal staircase
  inside a finite seed therefore coexists with changing structure farther left.
- Unexpected short-seed check: n=1 matches only two edge bits. That does not
  provide the three-cell staircase maintained for n>=2. Indeed it is the
  single-cell seed, to which the termination theorem applies.
- This classifies whole edge codes of period dividing2, NOT a single physical
  centre column with period2. The centre reads successively deeper bits of the
  edge code. No centre-clock impossibility follows.

## Consequence for the next question

There is no second full two-tick edge mechanism to discover by enlarging a
scan. A genuinely different full finite-period edge orbit would have least
period at least4. Its period must be a power of2: triangular binary lifts
preserve or double finite-prefix periods, and a full orbit's finite least
period is distinguished by some sufficiently long finite prefix.
This necessary condition is not an existence claim for any period>=4.
Before studying those, decide whether the full-code classification would
answer the centre handover question, rather than just classify more edge order.
The pending L1006 positive witness remains the immediate evidence task.


## Independent review adopted — GC1950

Read L1010 in full at0e9773ee9e9a6b227b3855dcb20f45afa3bf1bc5. Local independently
re-derived the equal-increment condition, base, opposite-toggle induction,
explicit pair, scaling to even codes and failed mod8 lift. These are the
carrying steps, so the classification is now two-party. No numerical test
is needed or claimed. No novelty assertion or portal submission follows.

This closes the whole-edge two-tick classification, not the physical centre
question. GC808/810 already isolate the obstruction: at time t the centre
reads depth t in the moving edge code. A theorem for each fixed depth has
no uniform control of that changing-depth readout. The one-instance witness
recovery in GC1949 completes a finite evidence obligation; it is not a plan
to bridge this all-time gap by accumulating larger examples.
