# Carrying read of GC2706 and GC2709: the return automaton, the clock, the seam and the tail completion — Cloud, CL753, 6 November 2026

*GPT asked Local to carry five hand steps: in [GC2706](GPT-BRIDGE-RETURN-AUTOMATON-20261106.md) the generic
induced-return/quotient construction and the conditional sharp clock; in [GC2709](GPT-PHYSICAL-47-RETURN-20261106.md)
the Post-image inclusion with its limited consequence, the phase/width/head guards at the 193/167 split, and the
tail-completion identity with its endpoints q = 0 and q < 2^360. The owner asked Cloud to take the read instead.
Every step was read from the two reports, checked by hand, and, wherever the data allow, replayed with code written
here from GPT's evidence packets: `cited/gpt/gc2706-bridge-return-20261106.tar.gz` (SHA256 `1d7e054c…`, 29,313 bytes)
and `cited/gpt/gc2709-physical-return-20261106.tar.gz` (SHA256 `f55c0d38…`, 3,909,947 bytes), both downloaded and
digest-checked. The probes are `tests/probes/swarm/sw02/block3/cloud_hand_checks.py` and `cloud_return_replay.py`
with their outputs. Kit names GPT credits were checked at kit main `9d837cd5`. Cloud is a different worker from GPT,
so a verdict below is a two-party read; it is not a read of Local's original DFA construction, whose 128-bit subset
hash caveat (L1569) every statement about the tables inherits.*

## Verdicts

| Step | Verdict | Where carried |
|---|---|---|
| GC2706 (1): the induced return machine on complete-E boundaries recognises exactly E(A*E)* in the DFA, its unary-orbit labels cover every exponent, and the quotient by equality of all future exponent sequences is exact | **PROVED hand/two-party** as a finite-automata statement; **COMPUTED** instance reproduced | §1 |
| GC2706 (2): the conditional clock, mean ≥ 145/2 sampled steps per excursion, sharp, with the exact minima 145m + 62 and 145m − 7 | **PROVED hand/two-party**, conditional on the two-state grammar (which is COMPUTED relative to the tables) | §2 |
| GC2709 (3): Post_C(S_E) ⊆ S_E for C = A⁴EA⁷E, a decreasing chain, and its limited consequence | **PROVED hand/two-party**, under the subset-construction semantics stated | §3 |
| GC2709 (4): the phase, width and head guards at the 193/167 split, and the witness "iff" | **PROVED hand/two-party** | §4 |
| GC2709 (5): B_b(X) ≫ 1 = D(X), E_m(X) ≫ m = D^m(X), D a width-preserving permutation, unique tail completion, the endpoints q = 0 and q < 2^360 | **PROVED hand/two-party**; known specialisation, as GPT says, of the kit's `diagonal`/`Phi` facts | §5 |

The seam equivalence and completion identity are statements about physical right halves. They provide no bridge realisation, finite-support survival or capture theorem; those limits are carried with the results.

## 1. The induced return automaton

**Statement (GPT).** Let the X gap DFA be complete with a sink. With A = 25 and E = 33535555, let q₀ = δ(0, E) and
f_n(q) = δ(q, AⁿE). The machine on the closure of {q₀} under the f_n recognises exactly the words E(A*E)* accepted
by the DFA; the unary orbit of A from q is a prefix followed by a cycle, so f_n is an ultimately periodic function of
n and is known for every n; and the quotient by "equal future exponent sequences" is a right congruence that
preserves the boundary language.

**Read.** (i) The unary orbit q, δ(q, A), δ(q, A²), … lives in a finite set, so it is a prefix of μ states and a cycle
of length π, and f_n(q) = δ(orbit[n], E) is determined for all n by the first μ + π values. (ii) Induction on the number
of E's: a word E Aⁿ¹ E … Aⁿᵏ E is accepted by the DFA from state 0 iff the induced path q₀ → f_{n₁}(q₀) → … is nondead,
since each step reads the same letters in the same DFA. (iii) Language equivalence of states is always a right
congruence; here every nondead boundary state is accepting (a complete E is a boundary), so the initial partition is
nondead against dead and the refinement compares, for each state, the sequence of successor classes over n ∈ ℕ. Two
ultimately periodic sequences with preperiods at most N and periods dividing L are equal iff they agree on n < N + L,
so a comparison on any horizon ≥ N + L decides it; GPT's canonical (shortest preperiod, primitive period) encoding is
the same test. The refinement terminates on a finite state set and its stable partition is the coarsest congruence
that preserves acceptance, hence the language. All three steps hold. The one thing the construction does not deliver
by itself is the factor language (words starting or ending inside a block, or with no E at all); GPT's separate product
comparison covers that, and my replay repeats it with a different encoding.

**Replay (own code, same tables).** Horizons used: 22, 22, 25, 27.

| W | DFA states | q₀ (windows) | raw boundary states | classes | R: next n → class | S: next n → class |
|---|---:|---:|---:|---:|---|---|
| 38 | 240 | 20 (11,870) | 6 | 2 | 4 → S; n ≥ 6 → R | n ≥ 6 → R |
| 39 | 209 | 20 (16,437) | 5 | 2 | 4 → S; n ≥ 6 → R | n ≥ 7 → R |
| 40 | 236 | 20 (22,882) | 5 | 2 | 4 → S; n ≥ 6 → R | n ≥ 7 → R |
| 41 | 291 | 20 (31,339) | 6 | 2 | 4 → S; n ≥ 6 → R | n ≥ 7 → R |

This is GC2706's table to the member lists (R's members at 41 are raw 20, 81, 94, 109, 200; S is raw 60, the state
A⁴E reaches with 14,865 windows). The counterwords of GC2698 reproduce as factors read from every DFA state:
55 A⁴ E A⁴ 3 absent at all four widths, 55 A⁴ E A⁶ 3 present at 38 and absent at 39 to 41. The whole factor language
equals the two-state grammar (every state initial and accepting on both sides; my NFA has 60 states, 67 at 38, against
GPT's 46, a different encoding of the same rule): equal at 481, 422, 484 and 612 reachable subset pairs. So, relative
to the tables, the finite languages carry exactly one bit of history: n ∈ {4} ∪ [6, ∞), and 4 forbids the next 4 and,
from 39, the next 6.

## 2. The clock

One return E Aⁿ costs c(n) = 34 + 7n sampled steps (E's gaps sum to 34, A's to 7), twice that in physical ticks. With
h(R) = 0, h(S) = −21/2, every edge of the 39–41 grammar satisfies c(n) − 145/2 ≥ h(q′) − h(q): equality at R→S (n = 4,
cost 62) and S→R (n = 7, cost 83), slack 7/2 at R→R (n = 6, cost 76), and larger n only add cost; checked for all edges
to n = 39. Summing over k returns gives cost ≥ 145k/2 + h(end) − h(start) ≥ 145k/2 − 21/2, and the 4,7 cycle attains the
mean 145/2. The recurrence r_{k+1} = min(r_k + 76, s_k + 83), s_{k+1} = r_k + 62 with r₀ = 0, s₀ = ∞ gives r_{2m} = 145m,
r_{2m+1} = 145m + 76, s_{2m} = 145m − 7 (m ≥ 1), s_{2m+1} = 145m + 62, so the minimum over k intervals from R is
145m + 62 at k = 2m + 1 and 145m − 7 at k = 2m ≥ 2; a brute-force dynamic program over the grammar agrees for k ≤ 11.
At 38, where S also admits 6, the minimum mean is 69, attained by 4,6. All as GPT states. GC2698's earlier bound
(145k − 21)/2 is tight at odd k and off by 7/2 at even k; the exact minima are the sharper statement.

Carried with its scope: the bound is about the finite language; (A⁴EA⁷E)^∞ is a periodic word of the abstraction,
and the replay shows E A⁴ E A⁷ E present as a factor at every width, so the sharpness claim stands inside the
tables; nothing follows about a physical row.

## 3. The Post-image inclusion and what it buys

In the subset construction, the state reached from state 0 by a word w is Post_w(B), with B the component's black
windows (state 0's 5,887,908 windows at 41 are a black subset of X's 20,710,807). Every complete gap letter ends at the
next black sample, so Post_w(S) ⊆ B for every nonempty w and every S. Hence Post_C(S_E) = Post_E(Post_{A⁴EA⁷}(S_E)) ⊆
Post_E(B) = S_E, and the iterates of Post_C on S_E form a decreasing chain of finite sets, which stabilises. Carried.

Replay: from q₀ the chain is 31,339 → 30,163 and then fixed (raw 200) at 41; 11,870 → 11,105 (raw 165) at 38;
16,437 → 15,537 (raw 165) at 39; 22,882 → 21,914 (raw 173) at 40, the GC2709 table exactly. The reset thresholds too:
for n ≥ 8 every boundary state reaches one raw state (raw 20 at 38 to 40; raw 109, 31,333 windows, at 41), while n = 7
and n = 6 do not; so the raw fibres forget one block later than the predictive quotient, as GPT says.

**The limited consequence, made precise.** If F = Post_C(F) is nonempty, every window of F has a C-predecessor in F,
so the finite graph on F has a cycle: the 4,7 itinerary is realised by a bi-infinite path of windows with exterior
inputs chosen freely at each move. That is the whole content, and it is the same kind of object as the component
itself: an abstract path, with no exterior consistency and no row. GPT's reading ("stable nonempty Post-images do not
make every member immortal, or supply a consistent exterior") is right.

## 4. The seam guards and the witness "iff"

The physical word E A⁴ E A⁷ E has 34 + 28 + 34 + 49 + 34 = 179 sampled steps, 358 ticks, 359 with the initial
black-centre update (the kit's u(R, s) = column 1 at tick 1 + 2s). The seams fall at ticks 1, 1 + 68 = 69 and
69 + 56 + 68 = 193, which is GC2708's phase correction. A 360-cell root reaches column 1 at tick 359 from cells
1 … 360 − t at tick t: 291 cells at 69, 167 at 193, 1 at 359. The row M at tick 193 has width at most 360 + 193 = 553,
so q = M ≫ 193 < 2^360. The head at ticks 193 + s depends on M's cells 1 … 1 + s with the prescribed centre, so
s ≤ 166 uses cells 1 … 167: A⁷E, 83 sampled steps, is 166 ticks. All carried.

Predecessor uniqueness under a prescribed drive bit: a nonzero finite row grows by exactly one cell per tick, so the
predecessor X of an output Y of width N has x_N = x_{N+1} = 0, the descent x_{i−1} = Y_i ⊕ (x_i ∨ x_{i+1}) for
i = N, …, 2 is forced, and the start is accepted iff Y₁ = b ⊕ (x₁ ∨ x₂); Y = 0 and Y = 1 have the predecessor 0 for
b = 0 and b = 1 respectively. Checked exhaustively for X < 2¹³ and both b: no output has two finite predecessors.
Hence the equivalence GPT states: the trace query has a witness iff some M of width ≤ 553 has 193 successful inversions
whose odd-time heads read E A⁴ E, and a first 167 cells whose forward heads read A⁷E. Forward: the witness's own row at
193. Backward: the inversions reconstruct the unique root of width ≤ 360, its heads are checked, and M's future is
checked; join the two at M. The head checks in (i) are part of the condition, not implied by ancestry. Carried.

## 5. The tail-completion identity

With B_b(X) = ((X ≪ 1) | b) ⊕ (X | (X ≫ 1)) and D(X) = X ⊕ ((X ≫ 1) | (X ≫ 2)): bit i ≥ 1 of B_b(X) is
x_{i−1} ⊕ (x_i ∨ x_{i+1}), so B_b(X) ≫ 1 = D(X) for both b; D commutes with ≫; and by induction the m-step driven
evolution satisfies E_m(X) ≫ m = D^m(X) whatever the drive. On w-bit words D is a bijection, inverted from the top
bit down by x_i = y_i ⊕ (x_{i+1} ∨ x_{i+2}), and it preserves the position of the highest bit. So a high tail q = M ≫ m
determines the root X₀ = D^{−m}(q), and with the drive fixed it determines all of M = E_m(X₀); q < 2^360 iff X₀ < 2^360;
q = 0 gives X₀ = 0 and M = E_m(0), which is nonzero as soon as a drive bit is 1. Exhaustive to 2¹² and random to 2²⁰
(drives of length ≤ 9); tail completion checked for w = 10, m = 5. The corridor law F(R)₁ = ¬(x₁ ∨ x₂ ∨ x₃) for
F = B₁ ∘ B₀ checked for R < 2¹⁰. Carried.

Kit credit, names checked at `9d837cd5`: `Rule30ControlledResponse.diagonal x k = xor (x k) (x (k+1) || x (k+2))` is
D itself, with `step` and `run_sound`; `Rule30Equivalents.TFunction.testBit_Phi`, `Phi_mod`, `mod_of_Phi_mod`;
`Rule30Predecessors.T`, `back`, `lin_back`, `eq_back`; `Preimages.eq_of_evol_one_eq_of_right`;
`Rule30CoupledGerms.double_corridor_of_u_succ_true` (u R s = false and columns 2, 3 white at 2s + 1 when
u R (s + 1) = true: the corridor read backwards). GPT's "known specialisation, reproved here" is the right status.

## 6. Not carried, and a route around

- The tables themselves. Both GPT's checks and mine run on Local's DFAs from `lift.c`; their determinisation names
  states by a 128-bit hash of the window set and no second host has rebuilt them. Every COMPUTED line above is
  conditional on that, as both reports say.
- The physical SAT query's UNKNOWN at 60,000 conflicts is not evidence in either direction. I agree with GPT that no
  larger blind budget is the next step.
- **A route around, cheap and without SAT.** The 4,7 cycle is a periodic word of the abstraction with 145 sampled
  steps per period, and §3 gives its window cycle inside the fixed fibre. Whether it is physically realisable is
  whether that one periodic word's windows lift width by width, which is Block 3's lift restricted to one cycle
  instead of the whole X component: L1569's question 1 ("a column-word tree can test one cycle at a time without
  growing the window") in its sharpest form. If the lift of (A⁴EA⁷E)^∞ dies at some width, the sharp clock's cycle
  is not real and the next cheapest cycle (6, 4 at 138, or 6, 6 at 152) is tested next; if it persists to the
  program's limit, it gives the exterior words a realisation must supply, which is the "short tail restriction forced
  jointly by the two excursions" GPT is after, read off rather than guessed. This replaces neither GPT's fixture
  diagnostic nor a theorem; it is a finite test with a prediction to write first, for whoever runs it.

## GPT GC2711 response to the proposed next test

The five carrying verdicts are received and adopted. Two guards on §6's proposal matter before any run. First,6,4 (cost138 sampled steps) is a finite R→R→S path, not a repeatable cycle: the next6 rejects from S at widths39–41. The basic6 self-loop costs76 sampled/152 physical ticks;4,8 is another closed two-return path of total152 sampled ticks. Repeating6,6 adds no new primitive itinerary.

Second, a width lift must state its temporal and tail scope. A fixed-P periodic spacetime search can miss a P-periodic head supported by longer-period or aperiodic farther columns. A phase-augmented finite graph allowing all temporal cycles is a safe finite-width obstruction test, provided its transitions encode actual physical steps. Nonempty compatible lifts at every width can give an infinite right-half history by compactness; they do not impose an eventually white tail or finite seed. Finite persistence alone proves neither. Runtime has not been established as cheaper than SAT. The proposal is retained as an alternative with these guards, not automatically launched or certified.
