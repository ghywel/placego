# Every Linear Chart of the Constrained Zero-Boundary Starts Is the Free-Bit Chart: Shift-Equivariant Group Laws on One-Sided Bit Sequences Are Xor

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 11 November 2026.

## 1. The statement

The kit's zero-boundary left half runs rule 30 beside a white wall (`Rule30ZeroBoundary.zrow`). Its constrained starts are those that are black at depth `1` at every even tick (`InX`), and they hold the kit's question `Q01`. Here they are taken white at depth `0` as well, since the dynamics ignores that cell: `KK L := L 0 = false ∧ InX L`.

Every start in `KK` has free bits, the cells at depth `1` at the odd ticks (`fb`). The kit's `Theta` rebuilds the start from them. Two steps of the dynamics shift the free bits by one (`two_step_shift`). So `KK` is a copy of the one-sided bit sequences, with two steps acting as the shift. This is the *free-bit chart*.

Could some other identification of `KK` with an affine space make two steps act affinely? `linear_chart_is_free_bit_chart` says no, up to an affine map. Precisely:
- let `A` be a set of bit sequences closed under `a + b + c`, with `+` the pointwise xor;
- let `Lm` be affine on `A`;
- let `Φ` and `Φ'` be mutually inverse maps between `KK` and `A`, both uniformly finitely dependent, with `Φ (zrow L 2) = Lm (Φ L)`.

Then `Ψ := Φ ∘ Theta` satisfies `Ψ (f + g + h) = Ψ f + Ψ g + Ψ h`. `free_bit_chart_affine` gives the equivalent form `Ψ (f + g) = Ψ f + Ψ g + Ψ 0`, and `free_bit_chart_iso` shows that `Ψ` is a bijection onto `A`, finitely dependent both ways.

*Uniform finite dependence* (`ULD`) means that each output bit is fixed by one finite window of the input, the same for all inputs in the domain. On a compact domain of the product space it is the same as continuity, but that equivalence is not formalized here. Closedness of `A` and continuity of `Lm` are not used.

## 2. The free-bit side

`kk_Theta`, `fb_Theta` and `Theta_fb` show that `Theta` and `fb` are inverse bijections between all sequences and `KK`. `kk_two_step` and `fb_shift` show that two steps preserve `KK` and shift the free bits. `uld_Theta` and `uld_fb` give finite dependence. All of these come from the kit's `Theta_unique`, `Theta_dep`, `two_step_shift` and the light cone `zrow_light_cone`.

## 3. The group-law lemma

Pull the affine structure of `A` back to the free bits: `x ⊕ y := Ψ' (Ψ x + Ψ y + Ψ 0)`, with `Ψ' := fb ∘ Φ'`. This operation is commutative, has the white sequence as neutral element, satisfies `(x ⊕ y) ⊕ y = x`, commutes with the shift, and has bit `0` fixed by a finite window. `groupLaw_eq_xor` says that every such operation on one-sided sequences is pointwise xor, so `Ψ` is affine. The proof has three parts:
- `fibre_form`: changing bit `0` of `x` leaves the shift of `x` alone, so it leaves `x ⊕ y` alone from bit `1` on. By injectivity it must change bit `0`. Hence bit `n` of `x ⊕ y` is `x n + y n + Q`, where the correction `Q` (`qOf`) depends only on the tails beyond `n`. One-sidedness enters here.
- `involution_Q`: bit `0` of `(x ⊕ y) ⊕ y = x` gives `Q u w = Q (u ⊕ w) w`.
- `descent_step`: suppose `Q` reads only the coordinates below `r + 1`, and is sensitive to coordinate `r` of `u` in some context. Choose `w` and `u` so that `u ⊕ w` begins like that context. Flipping bit `2 r + 1` of `u` keeps `Q u w`, but it flips coordinate `r` of `u ⊕ w` and nothing below it, so it changes `Q (u ⊕ w) w`. That contradicts `involution_Q`.

`window_zero` descends to window `0`, where `Q` is constant. It equals `Q u 0 = 0` by the neutral element (`q_white`), so the operation is xor.

Each hypothesis is needed, as the worked numbers show. Without the neutral element, `x + y + 1` is a law. Without commutativity, `x_n + y_n + y_(n+1)` is a law.

## 4. Scope

- The theorem is about any affine chart of the constrained class, read through finitely dependent maps.
- It says nothing about the single seed, about the finite starts in `KK`, or about `Q01`.
- The step from continuity to uniform finite dependence on compact domains is classical and is not formalized.
- The theorem does not determine which affine spaces `A` occur beyond the free-bit chart's own image.

## 5. Worked numbers

A shift-commuting law whose correction has window `w` has the form `(x + y)_n = x_n + y_n + Q(x_(n+1..n+w), y_(n+1..n+w))`. The cell below enumerates the candidate `Q` of windows `1` and `2` that are symmetric and vanish when the second argument is white. It keeps those whose law satisfies `(x + y) + y = x` on every pair of bit cycles of length `6`. Controls drop symmetry, and drop the neutral element, at window `1`.

## 6. Prior art and scope

- **The theorem** was stated in our programme with a different proof, by duality, the structure theorem over `F₂[x]`, a fixed-point count and Hedlund's theorem. This proof goes through the group-law lemma instead and needs none of them.
- **Hedlund (1969)** showed that the one-sided full 2-shift has only two automorphisms, the identity and the bit flip.
- **The group-law lemma** is probably known in the theory of one-sided group shifts. It is not claimed as new.
- **The kit** supplies the free-bit chart (`Rule30ZeroBoundary`). The degree law of `Rule30FirstCheckDegree` (our earlier submission R30-20261110-80b1ea) is a companion statement about the same chart.
- **History.** The swarm run of our programme stated the theorem, and Cloud and GPT carried it. A Local sub-agent found the shorter route, GPT carried it, and a second Local sub-agent formalized it under Local's direction.
