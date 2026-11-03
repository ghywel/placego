# The seven cells immediately before a return to 1951 — GC2463

GPT, 3 November 2026. **PROVED hand, two-party L1381**, conditional on the
carried strip transfer and (for the clocked applications) the critical-reset budget. A
specialization of the known local Rule 30 preimage relation. No new trajectory,
solver query, width or horizon. A tiny one-update self-check is below. The complete actual row
continues to carry the history.

## Pull, prediction and prior art

GC2462's actual-row map F is now carried by Local L1380. Can its return
condition be written as a small physical pattern immediately before the
event? The cheap objection is that a fall alone does not prescribe its
returned core. We invert that particular core explicitly, retaining the
phase and clean-half-line guards.

Prediction for a read of the existing GC2460 trace: the first two passages
pass the pattern below; the third fails it even though its anchor falls.
Counterfactual: if the exact seven bits disagree with the claimed endpoint,
the algebra/indexing is wrong and this sketch must be corrected. The read
will not simulate further or start a solver.

Record searched: GC2453/L1375 reset formula, GC2460's immutable witness,
GC2462/L1380 return map; current kitc42f6e51 lean/equivalents/catalogues and
the current portal/open-PR index (last complete refresh04:35:16Z, Local04:40).
Actual kit `Rule30Equivalents.Preimages.evol_one` states the cell equation;
`eq_of_evol_one_eq_on` and `eq_of_evol_one_eq` implement the known leftward
preimage recursion. Its source introduction and proofs through the
right-asymptotic injectivity theorem were read, SHA256
`d29af2ca2b994f2b38c2c29de58c92da9faae64bd9bea7e9dc23bd8c3929d378`.
The general preimage method is known and reused. No novelty or submission
assessment is made for this seven-bit calculation.

## A guarded one-step equivalence

At a B3 anchor a in phase2, assume the actual row agrees with the reference
on x≤a. Write g_i for the cell at a+i for i≥1. The reference supplies
g_−1=1 and g_0=0. Here the two symbols with negative/zero subscripts denote
the actual cells at a−1,a, rather than additional freely chosen values.

**Claim:** the next update is an anchor fall whose new thirteen-cell word
is1951 if and only if

`g_1..g_7 = 10011pq`, with `p OR q = 1`.

In this displayed word p,q are bits. Equivalently use the three little-endian words
`{57,89,121}`, or the spatial words

```text
1001110
1001101
1001111
```

Proof. The next anchor cell is
`1 XOR (0 OR g_1) = 1 XOR g_1`, whereas its reference value is1.
Thus a fall happens exactly when g_1=1. After shifting the anchor left7,
the next core's first six cells are the known reference word111110.
The next two cells are the failed old anchor and its right neighbor,01.
The low byte is therefore159, as in carried GC2453/L1375.

The five remaining core cells are the next values at old positions2..6:

`y_i = g_i XOR (g_(i+1) OR g_(i+2))`, for i=1..5.

Since1951=159+256·7, these five desired bits are11100. With g_1=1:

1. y_1=1 gives g_2=g_3=0.
2. y_2=1 then gives g_4=1.
3. y_3=1 is automatic, since g_3=0 and g_4=1.
4. y_4=0 gives g_5 OR g_6=1.
5. y_5=0 gives g_5=(g_6 OR g_7).

If g_5=0, the fifth equality forces g_6=g_7=0, contradicting the fourth.
Hence g_5=1 and g_6 OR g_7=1. Conversely these conditions give all five
desired y bits and the fall, for every choice of cells further right.
The clean half-line follows from the carried anchor transfer. This proves
both directions without enumerating histories.

The pattern is phase-specific and is applied to the actual seven adjacent
cells before a fall. A raw input word or a freely labelled strip path does
not itself establish that these cells have an actual common past. Three
possible seven-bit words do not mean three possible initial rows.

## Exact packets for the rooted return map

Retain GC2462's definitions: Q is the whole-line Rule 30 update,
F(r)(x)=Q^44(r)(x−7), and C is ether-left/core1951 at phase3. From r∈C the
budget excludes every fall before44. Therefore

`F(r) belongs to C` if and only if `Q^43(r)(1..7)=10011pq`, `p OR q=1`.

For repeated returns, suppose the original row is in K_j, so the previous
j returns really occurred. At t_j=44j+43, the relevant physical columns are
`1−7j,...,7−7j`. The next return condition is exactly five unit constraints
with values10011 on the first five of those columns, and the clause

`H(t_j,6−7j) OR H(t_j,7−7j) = 1`.

Call this six-clause physical condition A_j. Induction on the number of
returns gives `K_(j+1)=K_j intersect A_j`, with K_0=C. The K_j guard supplies
the actual phase, anchor and clean half-line used in the one-step proof.
Dropping it is not licensed.

The packet's largest initial right dependency is
`44j+43+(7−7j)=50+37j`, exactly13+37(j+1). This recovers the earlier
sufficient prefix cutoffs50,87,124. It does not make the extra37 initial
cells independent or prove this cutoff minimal. The nonlinear evolution
from the initial row to the packet remains to be understood.

A future clause exporter could replace an explicitly required next-core1951
condition by this packet under the exact root and previous-return guard.
**The packet is a next-return condition, not a consequence of the previous
returns alone.** In particular A_2 must not be added as an implied clause
to the original three-fast-fall query: that query leaves its last endpoint
free, and its checked SAT witness violates A_2. Adding it would change the
question. Any augmented-CNF solver receipt still needs the declared
equivalence or certification against the original CNF. No exporter,
augmented solve or additional theorem compilation is run here.

## Existing-witness read

Only the immutable GC2460 trace was read, SHA256
`972e18f6ede946704ea863d00312ec1288e600d3250205edfb23450991a0998e`.
No evolution was rerun. The prediction holds:

| Time | Current anchor | Pre-fall core | First seven cells | Next core |
|---:|---:|---:|---|---:|
| 43 | 0 | 5369 | 1001111 (121) | 1951 |
| 87 | −7 | 1369 | 1001101 (89) | 1951 |
| 131 | −14 | 2093 | 1011010 (45) | 4767 |

The first two packets pass all six clauses. The third has black at its
third required position (physical column−11) and white at its fifth
required position (physical column−9). It fails those two unit clauses;
its first bit and terminal OR still permit a fall. This locates the exact
same-core-return failure without claiming an obstruction to other initial
histories. All rows/cores come from the already checked132-tick model.

The inexpensive independent-coordinate self-check
`tests/probes/gpt_reset_packet_check.py` (SHA256
`645a5ec24c391671bb0f7c80cbdcaa5eedad6114a8c766abdaacca558f8f4037`)
also passes all128 seven-bit parents. It applies one literal update on old
coordinates−8..7, then reads old−6..6 as the re-anchored core. Exactly57,89,121
give a fall and core1951. This is a same-worker check of the hand indexing,
not an independent carrying read or a search for an actual long history.

## A guarded reduction of the sufficient cutoff — GC2464

**PROVED hand, two-party L1381.** A return packet with p=g_6=1 does not require g_7. The
first six pre-fall values are then100111 and already force the last OR.
This is an explicit use of the Rule 30 masking gate at a rooted return.

More precisely, suppose an actual row r is in K_n, n≥1, and the last
packet has p=1. Every row with the same ether left half and the same initial
prefix through **12+37n** is also in K_n. This is a sufficient cutoff;
no minimality assertion follows.

Proof. The previous packets have largest right dependencies at most
13+37(n−1), which is below12+37n for n≥1 (there are no previous packets
when n=1). Thus they still hold. The first six cells of the last packet
have right dependencies at most

`(44n−1) + (6−7(n−1)) = 12+37n`.

They retain100111. The seventh cell may change but cannot invalidate its
OR with a sixth cell fixed at1. The exact packet equivalence then preserves
the last return, and the earlier packet guards preserve its phase/anchor.
The proof is for membership in the returned-prefix set C; it does not
claim that the entire returned row or its future is unchanged.

Two concrete applications use existing evidence:

- GC2460's first packet is121, so its initial prefix through49 forces a
  first fall at44 returning to1951 for **every** continuation from50 onward.
  The generic cutoff from F locality was50. The two later returns are not
  being claimed for this shorter prefix.
- For the older retained trajectory B, normalize its time431 row by
  r_B(x)=B(431,x−68), as in GC2453/55. Its two44-tick returns end at original
  times475,519. Reading the existing GC2452 frame trace gives pre-fall
  cores1369 at474 (word89) and4857 at518 (word121). Its second packet has
  p=1. Thus fixing this normalized initial prefix through86 forces **both**
  same-core returns for every continuation from87 onward. The generic
  cutoff was87. This family starts from r_B as an initial row; no claim
  is made that all its members arise at time431 from B's original time-zero
  input family.

The latter read used the unchanged frame trace SHA256
`c777a9b782d5af8466e7717755852db1c81204d54e1f3f0c45a17932b1c3df21`;
the full normalized template is already retained in GC2455's encoder
artifact. No new sample, run, seed, horizon or numeric fit was needed.

This shows that a particular initial bit can cease to matter to a specified
future return under an explicit root/history guard. It is not wholesale
forgetting of the right tail, a finite-state closure, or an improvement of
the asymptotic speed bound. When p=0, the packet still needs q=1; its
dependence cannot be dropped by this argument.

## Next step

**Carrying read adopted:** complete L1381 proof, packet_check.py and retained
output read. Local carries the packet, coordinates, masked cutoff and both
applications. Its exhaustive16384 strip/input cases have zero mismatches,
with packets57,89,121, and both actual templates are replayed. These are
Local computations; GPT's separate128-parent self-check is the Intel check.
The general common-past relation between packets remains open.

Next either derive an actual
relation between different packets from one shared initial row, or identify
the exact missing relation. An isolated packet is not that cross-passage
compatibility theorem. Avoid an automatic fourth-fall query or a ladder
that merely repeats one more ancestor gate at a time. The independent
alternative remains retained original gap43 proof support.

The packet-coupling route is parked against a third local ancestor layer;
reopen on a genuinely cross-passage relation or exact inverse. The independent
original-gap43 proof-support audit is the next separately frozen step.
My own pull: a small spatial return pattern is a more concrete target than
an unlabelled zero-cost cycle; its common past remains the hard part.
