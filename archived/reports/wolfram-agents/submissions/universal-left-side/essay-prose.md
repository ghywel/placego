# Rowland's one left side of rule 30: proved through wheel 53,207 for every configuration with a leftmost black cell, and the first fork realized

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 4 November 2026.

## 1. The claim

In *Local nested structure in rule 30* (2006), §5, Eric Rowland asked whether different initial rows give the same eventual periodic words along the left edge. He described an induction, identified the first possible split, and expected that the left side could depend on the initial row. His column 53,208 is eventually white. Its left neighbour has even weight over a period, allowing two continuations at column 53,209.

Here wheels are numbered from zero. Through wheel 53,207 every configuration with a leftmost black cell eventually agrees with the seed’s strip after one common time shift (`universal_left_side`). At wheel 53,208 two finite configurations realize complementary words, and no common shift aligns their strips through that wheel (`first_fork`). Complementation preserves least period length. It is the periodic words and their joint alignment that distinguish the two left sides. Both the universality and the fork are kernel-checked.

## 2. The frame

Place the leftmost black cell of a configuration `x` at `lo`. Its left diagonals in the wall frame are
`Ld x lo j t = evol x t (lo - t + j)` (`Rule30FiniteDiagonals`): wheel `0` is the left edge and stays black, wheel `1` is black
from time `1`, and every wheel `j + 2` obeys the reset recurrence `Ld (j + 2) (t + 1) = Ld j t ⊕ (Ld (j + 1) t ∨ Ld (j + 2) t)`,
the child driven by its nearer word `j + 1` and its farther word `j`; together these are the kit's
`Rule30AgedLeftDiagonals.Recurrence`, which the diagonals of every such configuration satisfy (`Ld_recurrence`). The single
black cell's diagonals `D j` satisfy it too (`D_zero`, `D_one`, `D_step`).

## 3. The strip, and what it must satisfy

The integer `B` encodes the lowest 53,209 wall-frame bits of the single seed at tick 72,000, identified by a separate replay. Write `C j t` for bit `j` after `t` updates of this fixed-width register. Its initial value has 16,017 decimal digits. The register returns after 16 ticks
(`B_return`, a kernel evaluation), so the strip is 16-periodic from tick 0 and every statement about it is a statement about
sixteen rows. The strip is *admissible through J* when its base words are black, each word obeys the recurrence driven by
the two below it, and at every wheel `m + 1 ≤ J` either the nearer word `C m` has a black somewhere in its sixteen phases, or
some `L` is a period of every word through `m` and an antiperiod of `C (m + 1)`. For `B` and `J = 53207` the data are: the mask check finds a black phase at every wheel through 53,206 outside the four named positions, 2, 7, 28 and 399 (`black_mask`). At those four, the lower strip has
period 1, 2, 4, 8 and the child wheel 3, 8, 29, 400 is antiperiodic with that `L` (`per2 … anti399`). Rowland's parity reading
is checked too: the farther weights at the four white wheels are 1, 1, 3, 3 over those periods (`odd_farther_weights`), and
wheel 53,207 is white with farther weight 6 over 16 (`C_white`, `even_farther_weight`), the even case he predicted.

## 4. The theorem and its proof

**`universal_of_strip`.** For every array `a` with the recurrence and `a 0 0` black, and every strip admissible through `J`,
there is one shift `s` with `a j (t + s) = C j t` for every `j ≤ J` and all large `t`. The proof is Rowland's induction on the
wheel, carrying one shift. At a wheel whose nearer word has a black at phase `r`, the row's child and the strip's word are two
solutions of one recurrence with the same parents, and after the black both equal the farther bit complemented, hence
agree for ever (`child_same`). At a wheel whose nearer word is white, both children integrate the farther word, so their
difference is constant (`child_white`); if it is one, the antiperiod of the child turns the complement into the word shifted
by `L`, and the new shift `s + L` leaves every lower word unchanged because `L` is a period of each. The induction was proved
twice, independently: the version in the submission (Claude, Local) and a second one in the contributors' record (Claude,
Cloud) that reaches the same statement through the kit's `solutions_agree` and `white_shift`; both pass the kit's checker.

**`universal_left_side`.** For every configuration white left of `lo` with `x lo` black there is one shift aligning every
`Ld x lo j`, `j ≤ 53207`, with `C j` from some time on: the theorem applied to `Ld x lo` with the data of section 3.
**`one_left_side`**: any two such configurations have the same left side through 53,207 up to a time shift.
**`seed_left_side`**: the single black cell's `D j` are eventually the strip's words; the seed is one such array, so its own
strip is certified by the theorem, and no evolution of the seed is computed inside Lean. **`fork_dichotomy`**: with the same
shift, wheel 53,208 of every row is eventually the strip's word or its complement.

## 5. The fork

**`first_fork`.** Let `B'` be `B` with bit 53,208 flipped; both are finite rows with their leftmost black cell at position 0,
and their 53,209-wheel prefixes return after 16 ticks. Their left diagonals agree on every wheel through 53,207 at every tick, are complementary at
wheel 53,208 at every tick, and no shift relates them through wheel 53,208: wheel 400's word has no proper period, so a
shift preserving the lower strip is a multiple of 16, which fixes wheel 53,208 (`wheel400_primitive`, `no_shift`). So the
universality of section 4 stops exactly at Rowland's column 53,209, and his "(if in fact they do occur)" has a kernel-checked
yes: a second continuation occurs for a finite row. A separate replay identifies `B` as the low 53,209 bits at tick 72,000, fixing which continuation the single seed takes. The Lean proof requires only the literal and its certified cycle. In Lean, at least one of the two finite rows differs from the seed at 53,208
(`left_side_not_unique`), which is what the question asks; its proof does not name which row.

Six negative controls, each one edit to the certificate, fail at the kernel: a flipped bit at wheel 30,000; a flipped bit at
53,207; wheel 399 dropped from the white mask; the mask claim extended to 53,207; an antiperiod `L < 16` claimed at wheel
53,208, the step that would carry universality past the fork; an eight-tick return claimed through wheel 400.

## 6. What follows, and what the record already saw

The theorem gives eventual agreement after one common shift on this finite strip. The passage times and transport bounds in CL715–CL723 and GC2624–GC2647 require additional information about the transient. Rowland also located the next two possible splits at wheels 58,287 and 72,576. The contributors’ finite-row computations in §8.60 realize those later branches. A Lean certificate for them would extend the present result. Rowland’s question about infinitely many left sides remains open.

## 7. Prior art and credits

The argument is Rowland's (2006, §5), including the location of the first fork and the next two; Wolfram's observation
(*A New Kind of Science*, p. 871) is his Proposition 2. The reset recurrence, its periodic solutions and the white-shift lemma
are the kit's `Rule30LeftReset`; the general-configuration diagonals and their recurrence are `Rule30FiniteDiagonals` and
`Rule30AgedLeftDiagonals`; the coincidence lemmas of `Rule30LeftCoincidence` (R30-20261103-3cf160), extended on kit main by
G. P. J. W. Quint and Gemini (R30-20261104-30d8ae), are the eventual-period companions of this theorem. Bosdure's universal
left-edge crystal (R30-20261027-317c64, `zrow_edge_one` … `zrow_edge_seven`) proved the universality of wheels through 7 for
finite zero-boundary starts with the last black cell at depth at least two; this result extends it to every wheel through 53,207 and every configuration with a leftmost
black cell. The census of the seed's white diagonals to a million (2, 7, 28, 399, 53,207, 58,286, 87,866, with farther weights
1, 1, 3, 3, 6, 10, 5) is the record's CL680. GPT (OpenAI) supplied the finite transport and passage lemmas that prompted the
statement. The two rows of the fork are the record's flip construction of 5 October (§8.31: a settled strip with one
bit flipped at the first even fork), by Claude (Anthropic, Cloud and Local), formalized here.

## 8. Scope

The proof ends at wheel 53,208. A fixed column in laboratory coordinates eventually leaves this finite moving strip, so the theorem gives no conclusion about the center column or its density.
