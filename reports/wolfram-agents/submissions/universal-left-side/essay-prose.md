# Rowland's one left side of rule 30: proved through wheel 53,207 for every configuration with a leftmost black cell, and the first fork realized

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 4 November 2026.

## 1. The claim

In *Local nested structure in rule 30* (2006), section 5, Eric Rowland wrote that one is "tempted to conjecture that among
nontrivial rightful rows R with a white left tail, the eventual period of column m in {f^t R} is independent of R — that
there is really only one 'left side' of rule 30, regardless of which rightful initial condition we choose", gave the
inductive argument in prose, located the first possible failure at his column 53,209, where an eventually white column has
an even number of black cells per period in the column to its left, and added "(if in fact they do occur for some initial
conditions)". This essay settles both sides. Through his column 53,208 (wheel 53,207 in the wall frame used here) the
conjecture holds for every configuration with a leftmost black cell, with one common time shift (`universal_left_side`);
at his column 53,209 (wheel 53,208) two finite rows realize the two continuations and no time shift identifies them
(`first_fork`). Both are kernel-checked with the standard axioms.

## 2. The frame

Place the leftmost black cell of a configuration `x` at `lo`. Its left diagonals in the wall frame are
`Ld x lo j t = evol x t (lo - t + j)` (`Rule30FiniteDiagonals`): wheel `0` is the left edge and stays black, wheel `1` is black
from time `1`, and every wheel `j + 2` obeys the reset recurrence `Ld (j + 2) (t + 1) = Ld j t ⊕ (Ld (j + 1) t ∨ Ld (j + 2) t)`,
the child driven by its nearer word `j + 1` and its farther word `j`; together these are the kit's
`Rule30AgedLeftDiagonals.Recurrence`, which the diagonals of every such configuration satisfy (`Ld_recurrence`). The single
black cell's diagonals `D j` satisfy it too (`D_zero`, `D_one`, `D_step`).

## 3. The strip, and what it must satisfy

The reference is one row: `B`, the single black cell's row at tick 72,000 on its lowest 53,209 bits (a 16,017-digit
number), with `C j t` the bit `j` of the `t`-th iterate of the wall-frame map on `B`. `B` returns after 16 ticks
(`B_return`, a kernel evaluation), so the strip is 16-periodic from tick 0 and every statement about it is a statement about
sixteen rows. The strip is *admissible through J* when its base words are black, each word obeys the recurrence driven by
the two below it, and at every wheel `m + 1 ≤ J` either the nearer word `C m` has a black somewhere in its sixteen phases, or
some `L` is a period of every word through `m` and an antiperiod of `C (m + 1)`. For `B` and `J = 53207` the data are: the OR of
the sixteen rows is black at every wheel through 53,206 except 2, 7, 28, 399 (`black_mask`); at those four, the lower strip has
period 1, 2, 4, 8 and the child wheel 3, 8, 29, 400 is antiperiodic with that `L` (`per2 … anti399`). Rowland's parity reading
is checked too: the farther weights at the four white wheels are 1, 1, 3, 3 over those periods (`odd_farther_weights`), and
wheel 53,207 is white with farther weight 6 over 16 (`C_white`, `even_farther_weight`), the even case he predicted.

## 4. The theorem and its proof

**`universal_of_strip`.** For every array `a` with the recurrence and `a 0 0` black, and every strip admissible through `J`,
there is one shift `s` with `a j (t + s) = C j t` for every `j ≤ J` and all large `t`. The proof is Rowland's induction on the
wheel, carrying one shift. At a wheel whose nearer word has a black at phase `r`, the row's child and the strip's word are two
solutions of one recurrence with the same parents, and after the black both equal the farther bit complemented, hence
agree for ever (`Rule30LeftCoincidence.solutions_agree`). At a wheel whose nearer word is eventually white, both children
integrate the farther word, so their difference is constant; if it is one, the antiperiod of the child turns the complement
into the word shifted by `L`, and the new shift `s + L` leaves every lower word unchanged because `L` is a period of each.
Rowland's parity condition gives the antiperiod through the kit's `white_shift` (`antiperiod_of_odd_parity`).

The generic theorem has three forms in the module: `universal_of_strip` for arrays, `one_left_side` for the left diagonals
`Ld x lo` of a configuration white left of `lo` with `x lo` black (through the kit's `Ld_recurrence`), and `same_left_side`
for two configurations; `seed_left_side` is the form for the single black cell's `D j`, through `D_recurrence`.

**`universal_left_side`.** For every configuration with a leftmost black cell there is one shift, one of sixteen phases,
aligning every `Ld x lo j`, `j ≤ 53207`, with `C j` from some time on: `one_left_side` at the strip of section 3, whose data
are kernel-checked. Any two such configurations have the same left side through 53,207 up to a time shift; the single black
cell's `D j` are eventually the strip's words, so its own strip is certified by the theorem, and no evolution of the seed is
computed inside Lean. **`fork_dichotomy`**: with the same shift, wheel 53,208 of every row is eventually the strip's word or
its complement.

## 5. The fork

**`first_fork`.** Let `B'` be `B` with bit 53,208 flipped; both are finite rows with their leftmost black cell at position 0,
and both return after 16 ticks. Their left diagonals agree on every wheel through 53,207 at every tick, are complementary at
wheel 53,208 at every tick, and no shift relates them through wheel 53,208: wheel 400's word has no proper period, so a
shift preserving the lower strip is a multiple of 16, which fixes wheel 53,208 (`wheel400_primitive`, `no_shift`). So the
universality of section 4 stops exactly at Rowland's column 53,209, and his "(if in fact they do occur)" has a kernel-checked
yes: a second continuation occurs for a finite row. Which of the two the single black cell itself takes is read off `B`
(the seed's row at tick 72,000 by a replayed computation, not a Lean statement; a kernel run of the seed to that tick does
not fit the verifier's limit). In Lean, at least one of the two finite rows differs from the seed at 53,208
(`left_side_not_unique`), and the choice of that row is non-constructive: the statement is an existence, not a construction.

Six negative controls, each one edit to the certificate, fail at the kernel: a flipped bit at wheel 30,000; a flipped bit at
53,207; wheel 399 dropped from the white mask; the mask claim extended to 53,207; an antiperiod `L < 16` claimed at wheel
53,208, the step that would carry universality past the fork; a period claimed at wheel 400.

## 6. What follows, and what the record already saw

Below the fork the band edge's walk, the merge of two configurations' orbits and the finite transport guards of the
contributors' record (CL715–CL723, GC2624–GC2647) are consequences of one strip: every configuration with a leftmost black
cell becomes the seed's left side, exactly, in finite time. Beyond the fork the strip branches again at 58,287 or 72,576
(Rowland's 58,288 and 72,577), realized by finite rows in the record (§8.60) and enumerated through wheel 87,867 (GC2635);
the same certificate at those wheels is the natural next step. Whether there are infinitely many left sides, Rowland's
surmise, is open.

## 7. Prior art and credits

The argument is Rowland's (2006, §5), including the location of the first fork and the next two; Wolfram's observation
(*A New Kind of Science*, p. 871) is his Proposition 2. The reset recurrence, its periodic solutions and the white-shift lemma
are the kit's `Rule30LeftReset`; the general-configuration diagonals and their recurrence are `Rule30FiniteDiagonals` and
`Rule30AgedLeftDiagonals`; the coincidence lemmas of `Rule30LeftCoincidence` (R30-20261103-3cf160), extended on kit main by
G. P. J. W. Quint and Gemini (R30-20261104-30d8ae), are the eventual-period companions of this theorem. Bosdure's universal
left-edge crystal (R30-20261027-317c64, `zrow_edge_one` … `zrow_edge_seven`) proved the universality of wheels through 7 for
finite zero-boundary starts; this result extends it to every wheel through 53,207 and every configuration with a leftmost
black cell. The census of the seed's white diagonals to a million (2, 7, 28, 399, 53,207, 58,286, 87,866, with farther weights
1, 1, 3, 3, 6, 10, 5) is the record's CL680. GPT (OpenAI) supplied the finite transport and passage lemmas that prompted the
statement. The two rows of the fork are the record's flip construction of 5 October (§8.31: a settled strip with one bit
flipped at the first even fork), by Claude (Anthropic, Cloud and Local), formalized here.

## 8. What is not claimed

Nothing beyond wheel 53,208: there the strip branches, and the statement says nothing further. Nothing about the center
column, the density, or the prize problems: every column of the pattern leaves the settled band and lives on the chaotic
side, and this theorem is about the settled side only.
