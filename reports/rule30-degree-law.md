# The degree law: Rule 30's t-step rule has algebraic degree 2t − 1 (L1072)

Local, 28 October 2026, at the owner's request ("Prove the degree law"), following L1071 §2. **PROOF-SKETCH,
single-party; GPT's carrying read is requested.** Every lemma was checked against brute force before writing
(`tests/probes/wolfram/degree_law_check.py`, all exact identities). The theorem itself is computed for t ≤ 12
(`tests/probes/wolfram/centre_anf_degree.py`; L1071).

**Record searched:** L1071's search (`record_find.py` on cryptanalysis, ANF and degree terms). The agent found
nothing on the algebraic degree of Rule 30 iterates, and Mariot's 2024 survey (arXiv:2405.02875) lists the degree of
CA generators as open. No novelty is claimed beyond "not found".

## Statement

Let f_t : {0,1}^(2t+1) → {0,1} be Rule 30's t-step local rule: the cell x_t(0) as a function of the initial cells
y_(−t), …, y_t, under new(i) = x(i−1) XOR (x(i) OR x(i+1)). Write f_t as a polynomial over GF(2), its algebraic
normal form (ANF).

> **Theorem (degree law).** For t ≥ 2, deg f_t = 2t − 1. For t ≥ 3 the ANF has exactly one monomial of degree 2t − 1,
> namely y_(−t+2) y_(−t+3) ⋯ y_t, the product of all cells except the two leftmost. For t = 2 there are exactly two,
> y_(−1) y_1 y_2 and y_0 y_1 y_2. (For t = 1, f_1 = y_(−1) ⊕ y_0 ⊕ y_1 ⊕ y_0 y_1 has degree 2.)

By translation the same holds for every cell x_t(i). This is a property of the rule's t-step map, not of the single
seed; the single seed's centre column is one evaluation of it. **In words:** each step adds exactly two to the
degree, and the nonlinearity is spread over every input except the two leftmost.

## Tools

- **Möbius formula.** The coefficient of the monomial ∏_(j∈S) y_j is τ_S(f), the parity of the number of inputs
  supported inside S with f = 1. Equivalently it is the parity of the weight of f restricted to S, with every
  cell outside S set to 0.
- **Weight parity is additive.** wt(a ⊕ b) ≡ wt(a) + wt(b) (mod 2). A function that ignores a variable has even
  weight. A function linear in some variable is balanced.
- **Left-permutivity.** Cell x_k(p) = y_(p−k) ⊕ (a function of y_(p−k+1), …, y_(p+k)). Its leftmost input enters by
  exact XOR. So f_t = y_(−t) ⊕ g, and y_(−t) occurs only in the monomial y_(−t) itself.

Every monomial of degree ≥ 2t − 1 therefore omits y_(−t). The candidates are:
- the full product over [−t+1, t] (degree 2t);
- [−t+1, t] with one cell j removed (degree 2t − 1).

## Step 1. The derivative in the rightmost cell is a white anti-diagonal (Lemma 1)

> **Lemma 1.** ∂f_t/∂y_t = ∏_(k=0)^(t−1) (1 ⊕ e_k), where e_k = x_k(t − 1 − k).

*Proof.* Flip y_t. At time k the damage lies in [t − k, t + k], and its left edge advances at most one cell per
step. For cell 0 to be damaged at time t, the left edge must be exactly at t − k at every time k. Suppose the
leftmost damaged cell is at p = t − k. The new cell p − 1 is x_k(p−2) ⊕ (x_k(p−1) OR x_k(p)), where only x_k(p) is
damaged. So it is damaged exactly when x_k(p−1) = 0. If that ever fails, the edge falls behind and never recovers.
The cells e_k lie left of the damage, so they are the same in both worlds and do not involve y_t. ∎

So for any S ∋ t, the coefficient of S in f_t equals the coefficient of S \ {t} in ∏(1 ⊕ e_k). By the Möbius
formula that is the **parity of the number of words supported in S \ {t} whose evolution keeps the anti-diagonal
e_0, …, e_(t−1) white**. Since e_0 = y_(t−1), such words also have y_(t−1) = 0, so the parity depends only on
T = S \ {t, t−1} ⊆ [−t+1, t−2]. Write N(T) for the number of words supported in T with e_1 = ⋯ = e_(t−1) = 0
(and y_(t−1) = 0).

## Step 2. The anti-diagonal conditions are triangular (Lemma 2)

e_k = x_k(t−1−k) has leftmost input y_(p_k), with p_k = t − 1 − 2k. Condition k involves only cells ≥ p_k, and is
linear in y_(p_k). Call p_1, …, p_(t−1), that is t − 3, t − 5, …, −t + 1, the **pivots**. The other cells of
[−t+1, t−2], namely t − 2, t − 4, …, −t + 2, are the **free** cells: there are t − 1 of each.

> **Lemma 2.** If T contains every pivot, then N(T) = 2^(|T| − (t−1)). Solve condition k for y_(p_k), in the order
> k = 1, 2, …; each has a unique solution given the cells to its right.

Lemma 2 settles every coefficient but one:
- **Degree 2t.** S = [−t+1, t] gives T = [−t+1, t−2], so N = 2^(t−1), which is even for t ≥ 2. Hence deg f_t ≤ 2t − 1.
- **j = t − 1.** Same T, same even count: coefficient 0.
- **j a free cell.** T = [−t+1, t−2] \ {j} contains every pivot, and N = 2^(t−2), which is even for t ≥ 3: coefficient
  0. At t = 2, T is the single pivot −1 and N = 1, which gives the extra monomial y_0 y_1 y_2.
- **j a pivot p_m with m ≤ t − 2.** Conditions k < m use pivots right of p_m and are solved uniquely. Condition m,
  with y_(p_m) = 0, constrains only cells right of p_m. Conditions k > m are solved by their own pivots, given
  everything to their right. The free cells left of p_m are therefore unconstrained. There are t − 1 − m ≥ 1 of
  them, so N carries a factor 2^(t−1−m): even, coefficient 0.
- **j = t.** This monomial, [−t+1, t−1], does not contain y_t, so it needs a separate argument. Write
  f_t = y_(−t) ⊕ h ⊕ u ⊕ v ⊕ uv, where:
  - h = x_(t−1)(−1) ⊕ y_(−t) ignores y_(t−1);
  - u = x_(t−1)(0) is linear in y_(−t+1);
  - v = x_(t−1)(1), with y_t = 0, ignores y_(−t+1).

  Over the 2t − 1 cells of S, h, u and v have even weight. uv has weight wt(v) over [−t+2, t−1], because exactly one
  value of y_(−t+1) makes u = 1. That is 2^(2t−3), since v is linear in y_(−t+2). So the coefficient is 0 for t ≥ 2.

**What remains:** the coefficient for j = −t + 1 = p_(t−1), the claimed top monomial. It equals N(T) mod 2 for
T = [−t+2, t−2], the window without the last pivot. Pivots p_1, …, p_(t−2) still solve conditions 1, …, t−2. The last
condition, e_(t−1) = 0, then becomes a function Φ of the t − 1 free cells. There are 2^(t−1) assignments, so the
number of zeros of Φ is odd exactly when **Φ has odd weight**, that is, when its top coefficient τ(Φ) is 1.

## Step 3. The z-frame and the induction (Lemmas 3 and 4)

Measure distance j to the left of the anti-diagonal: z_k(j) = x_k(t − 1 − k − j).
- **The rule in this frame.** For j ≥ 1 the real rule becomes z_(k+1)(j) = z_k(j+2) ⊕ (z_k(j+1) OR z_k(j)). It never
  reads j = 0.
- **The anti-diagonal.** It is z_k(0) = 0, and z_(k+1)(0) = z_k(2) ⊕ z_k(1) given z_k(0) = 0. So the conditions read
  **z_k(1) = z_k(2)** for k = 0, …, t−3, with **Φ = z_(t−2)(1) ⊕ z_(t−2)(2)**.
- **The initial row.** z_0(j) = y_(t−1−j). Free cells are odd j = 1, 3, …, 2t−3, pivots are even j = 2, …, 2t−4, and
  z_0(j) = 0 for j ≥ 2t − 2.
- **Permutivity in this frame.** z_k(j) = z_0(j + 2k) ⊕ (a function of z_0(j), …, z_0(j+2k−1)).

Call this system **S_m**, with m = t − 1 free cells. It is intrinsic: S_(m−1) is S_m with z_0(2m−2) and z_0(2m−1) set
to 0. Its pivot z_0(2k+2) solves the condition at time k, using only cells nearer the boundary. Define:
- Φ_m = z_(m−1)(1) ⊕ z_(m−1)(2);
- W_k^(m) = z_k(2m − 2k) for 1 ≤ k ≤ m − 1, the cells on the speed-2 line from the first white cell z_0(2m);
- P = z_0(2m − 2), the last pivot of S_m. It equals Φ_(m−1)(free cells), because S_(m−1)'s final condition is linear
  in that cell.

**Damage along the speed-2 line.** Flip the farthest free cell q = 2m − 1; no pivot depends on it.
- *On the line:* cells with j + 2k = q always flip.
- *Behind the line:* the cell with j + 2k = q + 1 reads itself, the line cell (which flips) and the cell ahead (which
  never changes). So its damage β satisfies β_(k+1) = β_k ⊕ NOT z_k(q − 1 − 2k), with β_0 = 0.
- *Ahead of the line:* undamaged.
- *Rewriting in S_(m−1):* each cell z_i(2m − 2 − 2i) equals P ⊕ W_i^(m−1). This is linear in z_0(2m − 2), and its
  other inputs are the same in S_m and S_(m−1).

> **Lemma 3.** Δ Φ_m = m ⊕ (m−1)·P ⊕ W_1^(m−1) ⊕ ⋯ ⊕ W_(m−2)^(m−1), where Δ is the derivative in z_0(2m−1).
>
> **Lemma 4.** Δ W_k^(m) = k ⊕ k·P ⊕ W_1^(m−1) ⊕ ⋯ ⊕ W_(k−1)^(m−1).

*Proof.*
- **Lemma 3:** z_(m−1)(1) is on the line, so Δ = 1. z_(m−1)(2) is behind it, so Δ = β_(m−1).
- **Lemma 4:** W_k^(m) is behind the line, so Δ = β_k.

In both cases β_k = k ⊕ (the XOR of z_i(2m−2−2i) over i < k), and each of those cells is P ⊕ W_i^(m−1), with
W_0^(m−1) = 0. ∎

Take the top coefficient over all m free cells. That equals the top coefficient of Δ over the other m − 1 free cells,
which are exactly S_(m−1)'s. τ is linear, constants vanish when m ≥ 2, and P = Φ_(m−1). So:

  τ(Φ_m) = (m−1) τ(Φ_(m−1)) ⊕ Σ_(i=1)^(m−2) τ(W_i^(m−1)),   τ(W_k^(m)) = k τ(Φ_(m−1)) ⊕ Σ_(i=1)^(k−1) τ(W_i^(m−1)).

**Induction.** At m = 1, Φ_1 = z_0(1) ⊕ z_0(2) = z_0(1), so τ(Φ_1) = 1, and there are no W terms. Suppose τ(Φ_(m−1)) = 1
and τ(W_i^(m−1)) = 1 for all i. Then:
- τ(W_k^(m)) = k ⊕ (k − 1) = 1;
- τ(Φ_m) = (m − 1) ⊕ (m − 2) = 1.

So Φ has odd weight, the coefficient of y_(−t+2) ⋯ y_t is 1 for every t ≥ 2, and the theorem follows. ∎

## Checks

`tests/probes/wolfram/degree_law_check.py` verifies each lemma as an exact identity over all inputs, not just its
parity, and exits 0 only if all pass:

| Lemma | Range checked |
|---|---|
| L1, the anti-diagonal product formula | t ≤ 7 |
| L2, the triangular count 2^(t−1) | t ≤ 10 |
| L3 and L4, the two recursions as functions | m ≤ 7 |
| L5, τ = 1 | m ≤ 8 |

The theorem itself is computed for t ≤ 12 by two implementations: an agent's to t = 9, and mine to t = 12.

## What it shows, and what it does not

- *Exact nonlinearity:* the t-step rule gains exactly two degrees per step, so its nonlinearity is exactly
  accounted. By Schnorr's bound (multiplicative complexity ≥ degree − 1, cited and not checked), any circuit for f_t
  needs at least 2t − 2 AND gates. The naive circuit uses t².
- *The proof uses both of the asymmetric halves seen in L1069:*
  - the left side's exact XOR, through permutivity and the pivots;
  - the right side's OR masking, through the white anti-diagonal.
- *Not a prize result:* it says nothing directly about the single seed's centre column, which is one point of f_t.
