# The transmutation proposal: keep the drivers and the coordinates — GC2602

GPT, 3 November 2026. Complete CL708 read; reply to the owner's curiosity
as recorded there. The three-frame Boolean identity is **CARRIED by hand**.
The proposed interpretation is useful once its periodicity and measurement
guards are explicit. No T-a/T-c run, new census, finite-state model or prize
claim. The path/composition presentation and moving-frame application below
were **PROOF-SKETCH**; CL710's scoped hand carry, adopted GC2610 below,
makes the conditional composition and moving-frame application two-party.

## The object that can change form

Write the whole-line rule as

    X(t+1,p) = X(t,p-1) XOR [X(t,p) OR X(t,p+1)].

Choose a path p_t with step delta=p_(t+1)-p_t in {-1,0,1}, and let
x_t=X(t,p_t). Each step has exactly the form

    x_(t+1) = m_t*x_t XOR s_t.

Here multiplication is Boolean AND. All cells in this table are at time t;
p means p_t. The table follows by separating the two values of the OR's
other input; it needs no simulation.

| Path step | Retention m_t | Forcing s_t |
|---|---|---|
| +1, right diagonal | 1 | X(t,p+1) OR X(t,p+2) |
| 0, laboratory column | NOT X(t,p+1) | X(t,p-1) XOR X(t,p+1) |
| -1, left wheel | NOT X(t,p-1) | X(t,p-2) XOR X(t,p-1) |

This carries CL708's three identities. The four possible maps of the old
bit are copy, complement, constant0 and constant1. The **pair (m,s)** names
the map; m alone says only whether this conditional one-bit map retains
the old bit. Changing frame also changes the chosen path and its drivers.
It is not a claim that three different observed cells are one physical
worldline, or that every moving front has a nearest-neighbour path.

For fixed driver values over u<=t<v, composition gives

    x_v = M*x_u XOR S,
    M = product_(u<=t<v) m_t,
    S = XOR_(u<=t<v) [s_t * product_(t<q<v) m_q].

The empty map is (M,S)=(1,0). Appending the next step sends (M,S) to
(m_v*M, s_v XOR m_v*S), proving the formula by induction. Two blocks
compose as

    (M2,S2) after (M1,S1) = (M2*M1, S2 XOR M2*S1).

If r is the last reset (m_r=0) in the block, all earlier contributions
vanish, and x_v is the XOR of s_r,...,s_(v-1). Without a reset it retains
x_u plus the forcing parity. This is the familiar reset/running-parity
algebra, packaged as a composable object. Four possible conditional maps
do **not** make the full Rule30 history a four-state system.

## Which periodicity claims the known theorems actually support

1. **Unmasked is insufficient on its own.** For any prescribed binary
   sequence v, take m_t=1, s_t=v_(t+1) XOR v_t and x_0=v_0. Then x=v.
   For example v_t=1 exactly at positive powers of2 is not eventually
   periodic (its black gaps are unbounded). Thus m=1 does not imply a
   clock. These are forced-recurrence examples, not asserted physical
   Rule30 orbits with arbitrary independently realizable drivers.
2. **Periodic masking is insufficient on its own.** Set m_t=0 at every
   tick and s_t=v_(t+1). The same arbitrary v is copied after each reset.
   A reset forgets the conditional old bit; it need not forget news in s.
3. **The correct periodic-driver statement.** Suppose P>0 and BOTH m,s
   are P-periodic from T onward. If one period contains a reset, compare
   times r and r+P at such a reset: x_(r+1)=s_r=s_(r+P)=x_(r+P+1).
   Identical subsequent drivers preserve equality, so x is P-periodic
   from r+1 onward. If m is always1 after T, then
   x_(t+P)=x_t XOR parity(s_t,...,s_(t+P-1)). This parity is independent
   of t>=T. Even parity gives period P; odd gives anti-period P and
   period2P. Least-period claims require the corresponding least-driver-
   period hypothesis, not an arbitrary common multiple.
4. **Why the right edge is a dyadic clock.** In Rule30GateClocks, the
   forcing is a fixed, depth-dependent gate of two *lower* bits, with a
   fixed white boundary. Every finite prefix is autonomous and triangular.
   This extra structure gives pure power-of-two prefix periods, even for
   an infinite initial code. The theorem does not treat arbitrary forcing
   sequences merely because their retention bit is1.

These repairs are already explicit in the sources: Rule30LeftReset's
`reset_periodic` assumes both `ha` and `hb`; `white_double` assumes the
farther parent's periodicity as well as a white nearer parent.
`white_period_iff` states the parity test. CL697/F1--F3 likewise conditions
on the actual parent words. At a white left wheel, the next wheel becomes
an integrator of its farther parent; it inherits the P/2P conclusion after
that parent has settled. This is a precise instance of the owner's idea.

There is a second necessary guard: two histories may be compared by the
same (M,S) only if their drivers and path are held fixed. In a physical
trajectory, changing an older bit can change a future driver. GC2592--94's
carried retained-bit examples already demonstrate that failure. A one-bit
reset is not by itself future equivalence of initial-history classes.

## T-a: compare defined observables in one coordinate system

The kit definitions are R_j(t)=X(t,t-j) and D_k(t)=X(t,k-t).
Thus the same cell has **k+j=2t**. For the single seed the row has indices
0<=k<=2t, a total of2t+1 cells.

If the certified left prefix is k<B and the right observed prefix is
0<=j<=J, the uncovered integer indices are

    B <= k <= 2t-J-1,
    uncovered count = max(0, 2t-J-B).

Consequently CL708's `t-0.8t-2.4 log2(t)` is not a width in these wheel/
diagonal units. With its proposed finite approximations the arithmetic
would be `1.2t-2.4 log2(t)`, subject to endpoint conventions. If lengths
are instead normalized by the whole row width, divide *every* term by
the same scale. This is a coordinate repair, not evidence for either fit.

Two more definitions must be kept separate before T-a is frozen:

- The actual `band_edge_coin.py` computes B_P(t), the first disagreement
  between D(t) and D(t+P), for a **fixed lag P**. It certifies that the
  lower prefix is P-periodic forever, but is not the unrestricted least-
  period settling frontier. GC736/GC2520 already prove that it eventually
  saturates at the first diagonal whose eventual period does not divide P.
  Its observed linear segment is not an asymptotic linear-growth law.
- CL708 defines J by j+2^e_j<=t. That is a permissible observation budget
  if the j cost is explicitly intended, but not the geometric birth time
  of R_j in the full light cone: t-j>=-t means t>=ceil(j/2). The center
  intersects R_j at t=j, whereas the diagonal is defined from t=0 on the
  whole line. Specify whether the budget starts at time0, cone entry or
  center crossing. One-period observation is not a settling event: the
  right diagonal is already periodic in the edge frame.

The measured doubling fraction near0.42 through depth92 cannot establish
J(t)~2.4 log2(t). The kit gives an upper bound on prefix exponents, not
this density or a matching lower bound. Atlas §16's phrase attributing
`periods 2^(0.41 j)` to a proved kit theorem needs the same correction.
CL708 also revives a `2^(-P)` coincidence-rate statement; the atlas's own
§14/GC2404--05 already limits it to a heuristic, not a conditional hazard.
Nothing here disputes the measured finite examples.

Concrete route: use the already saved left onset/lag records and right
exponents, name P and the finite time window, and tabulate the three J
conventions separately. A growing-lag left prefix is an alternative, but
then lag changes are separate events, not one fixed-pair damage process.
No enlargement or new run is required to repair the comparison.

## T-c: an exact moving-frame equation before a finite-state search

Fix P and, where the first mismatch B_t=B_P(t) is finite, set

    Z_t(h)=D_(B_t+h)(t),
    Zbar_t(h)=D_(B_t+h)(t+P),
    Delta_t=B_(t+1)-B_t.

Extend left-wheel coordinates to integers using the original whole-line
trajectory. Substituting the left-wheel rule gives, for either copy,

    Z_(t+1)(h) = Z_t(h+Delta_t-2)
                 XOR [Z_t(h+Delta_t-1) OR Z_t(h+Delta_t)].

The same shift Delta_t aligns both copies. The already carried front law
supplies Delta_t=0 iff the common Z_t(-1)=0. Larger healing displacements
are found by the next mismatch of the two updated rows; a measured maximum
does not bound every future displacement.

This supplies the coordinate equation for the proposed news frame. A
window h in [-w,w] still needs cells as far right as w+Delta_t, and may
need cells beyond its left end. Even with a bounded jump it generally has
external input. A front jump in the lab is Delta_t-1, which may exceed1;
do not silently apply the nearest-neighbour one-bit path table across it.

A discriminating next test, using saved data first, is to specify a paired
window and any certified periodic phase, then search for two occurrences
with the same proposed state but different next displacement/window. A
collision refutes that state description. No collision is a finite
observation, not closure. A proof of closure must quantify over all
admissible exterior completions sharing one actual input history (or
explicitly carry the needed external drivers). This is the concrete route
around the familiar reset-only compression failure, not a new state census.

## Sources and review boundary

Record searched: `masked integrator`, `affine`, `co-moving`, `B_P` through
record_find and its current cached kit/portal/open-PR index. Read CL708,
atlas §§14--16 and the controlling GC2520 review, full band_edge_coin.py,
the actual kit definitions and carrying statements in Rule30Diagonals,
Rule30LeftReset and Rule30GateClocks; CL697/F1--F3 and GC2594 were already
fully carried. Kit pin c42f6e5133f61a47e99289fd4b6e0536fd8a0453;
last COMPLETE refresh19:14:56Z, preserved. Portal7b0d12/9861e5 and public
3cf160 are existing packages, not proposals to recreate. Relevant PR117
head7204c94/source3aa1dbf7 was read in GC2597/99, not freshly re-reviewed
here. This scoped hypothesis review makes no priority claim or assertion
of complete closed-PR coverage.

Primary literature: [Rowland, Local Nested Structure in Rule30, §5](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf),
Proposition2 and Lemma3, read directly. It already relates loss of a bit's
influence to a black nearer column and period doubling to a white nearer
column with odd farther-column parity. The present discussion reuses that
mechanism; the proposed composition notation is elementary bookkeeping.

**Next ownership.** Cloud retains its T-a/T-c proposal and owner exchange;
no GPT run or authorization of a substitute tool. Specific carrying
request: check the path table/composition, the two-driver guard and the
moving-frame substitution. Source/definition corrections require no new
computation. GPT's independent next step remains the saved19-witness/
15-state observer audit; Local retains the three-phase Lean build.


## CL710 carry and endpoint convention — GC2610

Cloud's complete CL710 carries the conditional four-map composition,
two-driver periodicity guard and moving-frame substitution. Adopt these
PROVED hand/two-party, with the fixed-path/fixed-driver restrictions above.
The owner's Cloud-only substitute-tool decision is recorded in CL710;
macOS requirements are unchanged.

One endpoint must remain explicit in T-a: this report uses left indices
k<B and right indices j<=J, giving max(0,2t-J-B) uncovered cells. CL710's
max(0,2t-B-J-1) instead fits a left prefix k<=B. Both are valid conventions,
but a count of settled cells and the last settled index differ by one.
Return this distinction before any measurement specification; no new run.
