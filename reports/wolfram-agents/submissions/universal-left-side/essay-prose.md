# Rowland's one left side of rule 30, proved below the first fork for every configuration with a leftmost black cell

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 4 November 2026.

## 1. The claim

In *Local nested structure in rule 30* (2006), section 5, Eric Rowland wrote that one is "tempted to conjecture that among
nontrivial rightful rows R with a white left tail, the eventual period of column m in {f^t R} is independent of R — that
there is really only one 'left side' of rule 30, regardless of which rightful initial condition we choose", gave the
inductive argument in prose, and located the first possible failure at his column 53,209, where an eventually white column
has an even number of black cells per period in the column to its left, "providing a counterexample to the conjecture (if in
fact they do occur for some initial conditions)". This essay proves the conjecture below that column, in the kit's reset
framework, for every configuration with a leftmost black cell, with one common time shift; the result is a kit module,
`Rule30UniversalLeftSide`, whose headline `one_left_side` passes the kit's checker with the standard axioms.

## 2. The frame

Place the leftmost black cell of a configuration `x` at `lo`. Its left diagonals in the wall frame are
`Ld x lo j t = evol x t (lo - t + j)` (`Rule30FiniteDiagonals`): wheel `0` is the left edge, which stays black; wheel `1` is
black from time `1`; and every wheel `j + 2` obeys the reset recurrence `Ld (j + 2) (t + 1) = Ld j t ⊕ (Ld (j + 1) t ∨ Ld (j + 2) t)`,
the child driven by its nearer word `j + 1` and its farther word `j` (`Ld_step`). The single black cell's diagonals `D j` obey
the same recurrence (`Rule30Diagonals.D_step`), and the kit's `Rule30LeftReset` holds the two facts the proof turns on: after a
black of the nearer word the child is reset, so two children of the same parents agree from the next tick on
(`Rule30LeftCoincidence.solutions_agree`); under a white nearer word the child integrates the farther word, so a time shift
by `L` changes it by the parity of the farther word over `L` (`white_shift`).

## 3. Admissible strips and the theorem

A strip `C : Nat → Nat → Bool` (wheel, time) is *admissible below the cut `J`* when: its base words are black, `C 0 = C 1 = 1`;
every word obeys the recurrence driven by the two below it; and at every wheel `j + 2 < J` either the nearer word `C (j + 1)`
has blacks arbitrarily late, or it is white and the farther word `C j` has odd parity over some `L` that is a period of every
lower word. The last clause is exactly Rowland's dichotomy: the even case is the fork he found at column 53,209.

**Theorem (`one_left_side`).** For every strip admissible below `J` and every configuration `x` white left of `lo` with
`x lo` black, there are a shift `s` and a time `T` such that `Ld x lo j t = C j (t + s)` for every `j < J` and every `t ≥ T`.

**Corollaries.** Any two configurations with a leftmost black cell have the same left side below `J` up to a time shift
(`same_left_side`). The single black cell's diagonals `D j` are eventually the strip's words (`seed_left_side`): the seed is one
such configuration, so the theorem certifies the seed's own strip from the strip's local consistency alone, without
evolving the seed.

## 4. The proof

Induction on the wheel, carrying one shift `s` and one time `T` for all wheels so far. The base wheels are black for every
configuration, so any shift serves. For wheel `n + 2`, the row's child and the strip's shifted word `C (n + 2) (· + s)` obey the
same recurrence with the same parents from `T` on. If the nearer word has a black at or after `T`, both children are reset
there and agree from the next tick on: the shift stays. If the nearer word is white, both children integrate the farther
word, so their difference is constant from `T`; if it is zero the shift stays, and if it is one the odd parity of the farther
word over `L` turns the complement into the word shifted by `L` (`white_shift`), and the new shift `s + L` leaves every lower
word unchanged because `L` is a period of each of them. That is the whole argument; it is Rowland's, carried with the shift.

## 5. The data

The universal strip is generated from `C 0 = C 1 = 1` by the recurrence alone: at a nearer word with a black, the forced
periodic child; at a white nearer word, the integrator with the single seed's phase. The generator and its checks are the
probe `universal_table.py` in the contributors' record. Below 53,208 the recurrence holds at every wheel and phase, the
white words are exactly wheels 2, 7, 28, 399, each with odd farther weight (1, 1, 3, 3) over the common period of the strip
below it (1, 2, 4, 8), which is a period of every lower word; the strip's period doubles at wheels 3, 8, 29, 400 to 2, 4, 8, 16;
wheel 53,207 is white with farther weight 6 over period 16, so wheel 53,208 is the first fork, Rowland's column 53,209. As a
control, the seed's actual row at time 65,536 agrees with the strip on every one of its 49,021 settled wheels. These are
finite checks of the data; a kernel-checked certificate module is the natural follow-up, and the theorem does not depend on
it: its data enters only as the hypotheses `Admissible`.

## 6. What follows, and what the record already saw

Below the fork the band edge's walk, the merge of two configurations' orbits and the finite transport guards of the
contributors' record (CL715–CL723) are consequences of one strip: every configuration with a leftmost black cell becomes the
seed's left side, exactly, in finite time. Rowland's "(if in fact they do occur)" is answered on the other side of the cut:
the forks at 53,208 and then at 58,287 or 72,576 are realized by finite rows, with four distinct left sides followed to a
million diagonals in the record (§8.60) and the four paths through wheel 87,867 enumerated and checked (GC2635). Whether
there are infinitely many left sides, Rowland's surmise, is open.

## 7. Prior art and credits

The argument is Rowland's (2006, §5), including the location of the first fork and the next two. The reset recurrence, its
periodic solutions and the white-shift lemma are the kit's `Rule30LeftReset`; the general-configuration diagonals and their
recurrence are `Rule30FiniteDiagonals`; `solutions_agree` is in `Rule30LeftCoincidence` (R30-20261103-3cf160), extended on
kit main by G. P. J. W. Quint and Gemini (R30-20261104-30d8ae), whose dichotomy results are the eventual-period companions of
this theorem. The census of the seed's white diagonals to a million (2, 7, 28, 399, 53,207, 58,286, 87,866, with farther
weights 1, 1, 3, 3, 6, 10, 5) is the record's CL680. GPT (OpenAI) supplied the finite transport and passage lemmas that
prompted the statement.

## 8. What is not claimed

Nothing beyond the cut: beyond wheel 53,207 the strip branches, and the statement says nothing there. Nothing about the
center column, the density, or the prize problems: every column of the pattern leaves the settled band and lives on the
chaotic side, and this theorem is about the settled side only.
