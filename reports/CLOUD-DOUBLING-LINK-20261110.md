# The doubling link: what the record already held, what I got wrong, and what the block adds

Cloud, CL771 and CL772, 10 November 2026, at the owner's word ("take the doubling link from the period-12 work").
Nothing here is a prize statement. The object is the whole-line light-speed family Fix(tau^P), written as two-sided
paths in the graph of profile pairs: a pair (c, d) of P-tick columns at sites i+1, i+2 has children (u, c) with
u(t+1) = u(t) xor (c(t) or d(t)). Leftward is forward.

**Outcome.** The pull I wrote at CL768 is closed by the record. Its test was run by Local a week ago, and two of
its sentences were false. Inside the same object the block carries GPT's two hand arguments, puts a second code
on three of the record's computations, and adds one new computed fact: the period-15 core has no walls at all.

## 1. Reconciliation with the record

| What I wrote at CL768 | What the record says |
|---|---|
| "Grow the period-32 graph leftward from the period-16 core and look for branching. Not run." | Run: `rule30-genealogy.md` §29.11 (T23, Local) for G16, T19 for G8, the defect trees behind white and the rain to period 128. Nothing but the rain is reached. GPT found this at GC2833. |
| "Going left the period never falls." | False. GPT's wall (23,40), (42,23), (21,42) has pair periods 6, 6, 2 (GC2835). True: a child's period divides twice the period of its drive; odd factors can be erased, never created. |
| "Branching is born at a doubling step and nowhere else." | False. In a world of odd period the pair period cannot rise, and the period-15 core branches (LN-12; confirmed in §4 below). |
| The induction frame (a new layer entered at antiperiodic columns; the half-difference) | §28 and §29.6 of the genealogy. I read that line at CL676 (§38) and had lost it. |

My prediction for the test (no branching, 0.7) agrees with T23. The result is Local's.

## 2. The link lemma (known mechanism, restated; hand)

Let c and d have period p, and let the drive c or d have odd weight over p.

1. At period p the pair has no child. At period 2p it has exactly two, u and its complement, and u(t+p) is the
   complement of u(t), because u(t+p) + u(t) is the weight of the drive over one period. So **the two children
   are the two time-phases of one antiperiodic column.**
2. Hence both continue for ever or neither does, and the two continuations are p-tick time shifts of each other:
   shifting the whole configuration by p ticks fixes everything to the right of the link.
3. The pair (u, c) has a child exactly when c has an even number of white cells over p, because
   (u or c)(t) + (u or c)(t+p) is the complement of c(t).

In GPT's language (GC2835) the link is the place where a half-phase bit is born: the parents have zero
half-difference, the child's is constant, so the child's spin is free. This is why, at period 12, each period-6
wave feeds exactly two components three rotation steps apart (CL768): they are the two phases of step 2.

COMPUTED on every link met below (1,523 links): steps 1 and 3 hold without exception. My prediction D2 said
"even weight" in step 3. That is right only for even p; the first run showed it failing at p = 1, 3, 5, 7 and the
statement above is the corrected one (run 1 is kept).

## 3. Second code on the record's computations

[Census](../tests/probes/swarm/sw02/carry/cloud_core_census.c) ([log](../tests/probes/swarm/sw02/carry/cloud_core_census.log)),
[analysis](../tests/probes/swarm/sw02/carry/cloud_doubling_links.py)
([output](../tests/probes/swarm/sw02/carry/cloud_doubling_links.out),
[run 1](../tests/probes/swarm/sw02/carry/cloud_doubling_links_run1.out)). Predictions D1 to D6 were pushed first (CL771).

**The core table (LN-12 §5).** A full census of all 4^P pairs for P = 1..15 gives the swarm's states and edges at
every period: 1/1, 6/8, 1/1, 6/8, 6/6, 42/50, 15/15, 46/56, 46/46, 11/13, 1/1, 270/326, 144/144, 62/64, 606/636.
Branching occurs at 12 and 15 only. The census took 52 seconds at P = 15.

**T23 (D1 PASS).** From G16's ring: 1,310 tree states at period 16 and 18,238 at period 32, 16 edges into the rain
at each, no other cycle reached. The longest path is 14 pairs at period 16 if the wall into the rain is counted
and 11 if only dying paths are; 41 at period 32 either way. T23's "14" and "41" are the first measure.

**Every doubling link out of a complete lower core (D3 PASS).**

| Step | Links | Survive for ever | The rest die within | Where the survivors go |
|---|---|---|---|---|
| 1 to 2 | 1 | 1 | | the rain (the black edge) |
| 2 to 4 | 2 | 0 | 1 pair | |
| 3 to 6 | 1 | 1 | | the rain |
| 4 to 8 | 4 | 0 | 2 pairs | |
| 5 to 10 | 21 | 1 | 6 pairs | the rain |
| 6 to 12 | 32 | 6 | 2 pairs | the six branching components, one each |
| 7 to 14 | 78 | 1 | 10 pairs | the rain |
| 8 to 16 | 56 | 0 | 13 pairs | |
| 16 to 32 | 1,328 | 0 | 31 pairs | |

For 16 to 32 the start is the cycles of the period-16 core (white, the rain, G8, G16; that core is T20's, which I
did not recompute); the closure has 43,092 pairs. So, COMPUTED: **at 2, 4, 8 and 16 no doubling link survives,
and the only doubling links that survive at all up to 16 are the black edge and six links from period 6 into the
period-12 family.** The period-12 cycle of 12 pairs is not reached from period 6: it is native to 12.

## 4. The period-15 core (D6; the unexpected test)

COMPUTED by full census (2^30 pairs): 606 pairs, 636 edges, five cyclic components and **no transient pair**.

| Component | Pairs | Edges | Pair period |
|---|---|---|---|
| branching | 525 | 555 | 15 |
| cycle | 60 | 60 | 15 |
| cycle | 15 | 15 | 15 |
| cycle | 5 | 5 | 5 |
| white | 1 | 1 | 1 |

- The branching component has 30 branch vertices and is carried to itself by every rotation of time.
- Nothing leaves it (predicted, 0.65: held) and nothing enters it (I predicted it would be entered, 0.6: refuted).
  No edge joins any two components.
- The same holds at every odd period up to 15: the core is a disjoint union of cycles and, at 15, this one
  branching component. At 5, 7, 9 and 13 there is only white and one other component, so 15 is the only period
  where the statement has content.

What is proved and what is not. White is isolated at every odd period, by hand: its only non-white child is the
all-black column beside white, whose drive has odd weight P. For the other components "no walls at odd period"
is an observation at one period. I do not have an argument and I do not conjecture it.

What it does to the working picture. At 12 the branching family is the sink of the core and is fed by plain
waves. At dyadic periods the sink is the rain and nothing branches. At 15 there is no sink: the branching
component stands alone. So "a core has one sink and it branches or not" describes even periods only.

## 5. Carrying read of GPT's two hand arguments (GC2835)

**(1) The equality-graph reduction. Carried, with one guard.** For P = 2L, H z = z xor (z shifted by L),
A = Hc and not d, B = Hd and not c, C = Hc and Hd.
- I rederived the legality condition from a or b = a + b + ab: shifting c alone changes the drive by A, shifting d
  alone by B, shifting both by A + B + C = H(c or d), and shifting u changes its difference by the same
  A + B + C. So spins (e_u, e_c, e_d) are legal exactly when
  (e_u + e_c) A + (e_u + e_d) B + (e_u + e_c e_d) C = 0. This is GPT's formula.
- Applying H kills C and sends A and B to C, which gives (e_c + e_d) C = 0. So C ≠ 0 forces e_c = e_d, and then
  the condition is (e_u + e_c)(A + B + C) = 0. If C = 0, A and B have disjoint supports and the condition is the
  two equalities where A or B is nonzero. Necessary and sufficient, as claimed.
- The lift: a finite lifted component has at most N sites because a repeated residue would give a translation; at
  most two infinite components can cross a cut with edges of length at most 2. Read and agreed.
- **Guard.** A column with zero half-difference is its own half-shift. It never gets an edge (I checked both
  cases), so it is always a finite component, and flipping it changes nothing. The entropy count K/N must count
  only components that contain a column with nonzero half-difference. With that guard the count stands.
- COMPUTED: on the five period-12 backgrounds (14, 20 and three of 34 cells) the classification equals the literal
  rule at every site and spin choice; each has one infinite component and exactly two valid fields, confirmed by
  brute force over all 2^14 assignments on the first. D5, the control GPT's fixtures could not exercise: in every
  simple cycle of the cores at even periods up to 14 there is no finite field-changing component, as the entropy
  count requires of cores with growth 1.

Status after this read: **PROVED, hand, two-party** (GPT's derivation, Cloud's read), with the guard.

**(2) Half-phase rigidity of the period-12 family. Carried.** If x is any two-sided path inside one of the six
components and y is a valid field whose every column is x's column or its six-tick shift, then y is x or its
six-tick shift.
- At U and V the half-differences are 4095 and 1560, which overlap, so the two columns of the pair carry the same
  spin (COMPUTED here as well). The continuing children have weights 5 and 7. A time shift keeps weight and the
  two integrals are complements, so the child carries the pair's spin too.
- Leftward the spin is carried along: y is two-sided, so its pairs are core pairs, and in the full core no edge
  leaves the six components (CL768's replay, which is stronger than the 92-state closure GPT cites). At a
  non-branch vertex the continuing child is unique.
- Every position lies to the left of a branch vertex of x, and two spins on overlapping tails would give a pair
  fixed by the six-tick shift, which does not exist. So one spin holds everywhere.

Status after this read: **PROVED, hand, two-party**, on finite inputs computed by both workers.

Together with §2 this says where the half-phase bit lives: it is created once, at the link, and the family then
carries it rigidly. The free binary choice of the family is not a phase choice. It is the choice between the
weight-5 and weight-7 integral at U or V, as GPT says.

## 6. What is left, and my view

- Open, unchanged, and not made easier by anything here: whether a dyadic period beyond 16 has a branching
  component. The full period-32 core is out of reach of a census (4^32 pairs).
- GPT's next step (the temporal-word quotient, keeping the 5 and 7 labels) is its own and I have not touched it.
- One concrete test this block suggests, small and not run: at period 15 the branch vertices' two continuing
  children are complements, so their weights are w and 15 − w with opposite parity. At 12 they are 5 and 7, same
  parity. If the weights at the 30 branch vertices of period 15 fall in one pattern, that is a second data point
  for GPT's observable; if they do not, the 5 and 7 are an accident of 12.
