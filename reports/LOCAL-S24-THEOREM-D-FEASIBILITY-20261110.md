# S-24 (Cloud's K-10, Theorem D): feasibility map and a shorter route

Local, 10 November 2026 (L1661). This is a read-only map made by a Local sub-agent and checked by Local, so it is a self-check. Nothing has been built yet. The (★) argument below is PROOF-SKETCH pending GPT's carrying read.

## The statement

Let K be `{L | L 0 = false ∧ InX L}` in the kit's `Rule30ZeroBoundary`. `InX` ignores depth 0, so `Theta` is onto this set and no larger one. Let A be a closed F₂-affine subspace of F₂^ℕ, and L : A → A continuous and affine. Let Φ : K → A be a homeomorphism with Φ ∘ G = L ∘ Φ, where G is two ticks. Then Ψ = Φ ∘ Θ : F₂^ℕ → A is an affine homeomorphism. In words: every linear chart of K is the free-bit chart, up to an affine isomorphism (swarm XP-2 report, Theorem D; carried two-party; part (a) is S-06).

## A shorter route (PROOF-SKETCH, Local self-check)

**Reduction.** Write X = F₂^ℕ, S for the shift, and a₀ = Ψ(0). Since `two_step_shift` gives ΨS = LΨ, we have L a₀ = a₀. Define `x ⊕ y := Ψ⁻¹(Ψx + Ψy + a₀)`; the argument lies in A because A is affine.

Properties of ⊕:
- ⊕ is commutative, `x ⊕ 0 = x`, and `(x ⊕ y) ⊕ y = x`.
- `S(x ⊕ y) = Sx ⊕ Sy`, because L is affine and fixes a₀.
- Ψ, Ψ⁻¹ and + are continuous on compact spaces, so bit 0 of `x ⊕ y` depends only on `x_{<R}` and `y_{<R}` for some R.

Theorem D is then equivalent to **(★): `x ⊕ y = x xor y`**. That says `Ψ(x xor y) = Ψx + Ψy + Ψ0`, which is affinity.

**Proof of (★).**
1. **Shape of the bits.** Let x and x′ differ only at bit 0. They have the same shift, so `x ⊕ y` and `x′ ⊕ y` agree from bit 1 on. The map `x ↦ x ⊕ y` is an involution, so they differ, and hence they differ exactly at bit 0. The same holds in y, so
   `(x ⊕ y)_n = x_n + y_n + Q(S^{n+1}x, S^{n+1}y)`, where `Q(u, w) := (0u ⊕ 0w)_0`.
   Q has a finite window, is symmetric, and `Q(u, 0) = 0`.
2. **Involution identity.** Bit 0 of `(x ⊕ y) ⊕ y = x` reads `Q(u, w) = Q(u ⊕ w, w)`.
3. **Descent.** Suppose Q depends only on the coordinates below r + 1, and suppose `Q(p, q) ≠ Q(flip_r p, q)`.
   - Take `w = q_0 … q_r` followed by q.
   - Back-solve u with `S^{r+1} u = p` and `(u ⊕ w)_{<r} = p_{<r}`, coordinate by coordinate from r − 1 down to 0.
   - Let u′ be u with bit 2r + 1 flipped. Then `Q(u′, w) = Q(u, w)`, because 2r + 1 is outside the window.
   - But `u′ ⊕ w` and `u ⊕ w` differ, among their first r + 1 bits, exactly at bit r, in the sensitive context `(p_{<r}, q)`. So `Q(u′ ⊕ w, w) ≠ Q(u ⊕ w, w)`, against step 2.
   - By symmetry Q also drops w's coordinate r. Descending from R gives Q ≡ Q(0, 0) = 0.

One-sidedness is used in step 1. The two-sided analogue fails: marker automorphisms conjugate xor to other group laws.

**Bounded check (COMPUTED; prediction written first).** Encode "Q has window r + 1, is symmetric, has `Q(u,0) = 0`, satisfies the involution identity, and is not identically 0" as SAT ([`s24_star_descent_check.py`](../tests/probes/swarm/sw02/carry/s24_star_descent_check.py)).
- It is UNSAT for r = 1, 2, 3, which is the prediction.
- Dropping identity or dropping symmetry gives SAT, so both hypotheses are used.

This checks step 3's finite combinatorics only, not the theorem.

**Prior art.**
- Hedlund 1969 (Math. Systems Theory 3): Curtis–Hedlund–Lyndon, and the automorphism group of the one-sided full 2-shift is Z/2.
- (★) is likely known in the literature on one-sided group shifts (Kitchens 1987; Wibmer, arXiv:2008.00755) but has not been located.
- No formalization of Curtis–Hedlund–Lyndon or Hedlund's theorem was found, in Lean or elsewhere.
- `known_find` returns no hits for these terms in the kit, the portal or the open PRs.

## What exists

- **Kit, core Lean:** step 1 completely. `Theta`, `Theta_free`, `Theta_unique`, `inX_iff`, `Theta_inj`, `Theta_dep`, `Theta_inverse_dep`, `two_step_shift`, `zrow_light_cone`, `zrow_zero_self`.
- **Mathlib at the kit's pin `56a00585`**, read at that commit:
  - Tychonoff and the product topology;
  - cylinders (`PiNat.cylinder`, `isTopologicalBasis_cylinders`);
  - `Continuous.homeoOfEquivCompactToT2`;
  - the PID structure theorem (`Module.equiv_free_prod_directSum`);
  - `Polynomial` over a field as a Euclidean domain;
  - algebraic dual annihilators;
  - `PontryaginDual`, but no duality theorem;
  - `SymbolicDynamics.FullShift`, but no sliding block codes, no Curtis–Hedlund–Lyndon and no shift automorphisms.
- **Absent from Mathlib:** continuous duality for compact F₂-spaces, expansivity, Curtis–Hedlund–Lyndon and Hedlund's theorem.

## The plan

- **Route Q, core Lean, about 600 to 1,000 lines, in `lean/` beside `Rule30ZeroBoundary`:**
  - Q1a: (★), for any operation with the five properties above, with continuity stated as uniform finite dependence;
  - Q1b: the transport from Ψ to ⊕;
  - Q1c: the K side (Θ and the free-bit read-off are inverse bijections between words and K, with uniform finite dependence);
  - Q1d: the assembled theorem.
- **Q2, optional, Mathlib, about 150 to 300 lines:** the literal topological statement. Continuity on a compact subset of ℕ → Bool gives uniform finite dependence.
- **Route H**, the six-step hand proof, would need the absent duality theory and Curtis–Hedlund–Lyndon: about 2,500 to 4,800 lines with real library risk. Not chosen.

**Build cost.**
- Route Q builds in seconds against the kit's existing core build.
- A complete prebuilt Mathlib at the pin already exists on Local's host, in the L1156 pipeline kit (6.6 GB, 8,643 oleans). This corrects L1659.
- Narrow Mathlib imports for Q2 measured 1.4 to 4.8 GB in earlier runs, within the 8 GiB caps.
