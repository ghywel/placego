# Rule 30, Prize Problem 1, period 2: where it stands

*A handover, written 2026-10-05 so that the work survives a move of compute, a new machine, or an outage. For a
person, or for an assistant given this file: read it, then the documents it names in the order given, run the
checks at the end, and stop. Do not start an experiment you were not asked for. Run `git log --since=2026-10-05` to
see what moved after this was written.*

## 1. The question

Wolfram's Rule 30 Prize Problem 1 asks whether the centre column of Rule 30, started from one black cell, ever
becomes periodic. The work here attacks it **period by period, for every finite starting configuration**, which is
stronger than the prize needs.
- **Period 1 is closed.** Condrey proved that no nonzero finite configuration has an eventually constant centre
  column (arXiv:2609.09431, 2026-09-08).
- **Period 2 is open.** That is the case worked on here: can a finite configuration's centre column be 0101...
  from some time on? Condrey's own conclusion names it as the next unresolved case.

Rule 30 is $x_{t+1}(i) = x_t(i-1) \oplus (x_t(i) \lor x_t(i+1))$. It is permutive in its left neighbour, so it can be
run sideways: given columns 0 and 1 for all times, every column to the left is determined (the *forced left half*,
PRIZE-PROBLEMS.md §5).

## 2. The chain of statements

Each line implies the one above it. Section numbers are in PRIZE-PROBLEMS.md.

| Statement | Where |
|---|---|
| **Prize Problem 1, period 2**: no finite configuration has its centre column eventually 0101... | §1, §8 |
| **B**: no finite right half makes the forced left half for 0101... eventually zero | §8, §8.11 |
| **LR_m** for some layer width $m$: no input to a width-$m$ layer next to column 0 makes it eventually zero | §8.11 |
| **LR (= LR_0)**: no column 1 at all makes the forced left half eventually zero | §7 |
| **R(d) is finite for every d** (equivalent to LR, by König's lemma) | §8.36, PRIOR-ART |
| **The doubling conjecture**: R(d) <= d + 4 | §8.36 |

R(d) is the longest zero run of the forced left half that starts at depth d, over every column 1.

The same question has several exact forms, each checked against the others by a probe:
- **The forced walk** (§8.37). A zero run from depth d is one deterministic walk per prefix of column 1: at every
  other cell, column 1's newest bit is forced.
- **The wall form** (§8.39). Run Rule 30 on the half-line $x \le -1$ against a wall at $x = 0$ that alternates
  white and black. The forced left halves are exactly the evolutions in which the cell beside the wall is black at
  every odd time.
- **Black, white and both** (§8.40). At the wall's black times the condition involves the left half alone. At its
  white times it couples the left and right halves. A finite configuration must keep both.

Known theorems used:
- **Jen (1990), via Kopra**: two adjacent columns of a configuration with an eventually zero left half are never
  both eventually periodic. So no eventually periodic column 1 can work (Proposition 7, §8.13).
- **The channel bound**. Next to 0101..., column 1 carries at most about 0.13 bits per visible bit (0.064 per step),
  whatever the right half. The figure is 0.128 by power iteration (§8.20), certified as 0.1292 in integer
  arithmetic (§8.33).

## 3. What has been measured

All numbers come from probes whose predictions were committed before they ran. Each probe's header records its
OUTCOME.

- **R(d), exact** at depths 1 to 61, 65, 69, 73, 77 and 81 (§8.36, §8.37). R(81) = 65, R(d) <= d + 4 at every
  depth, and R(d) - d is about -0.18 d.
- **Distinct forced walks** at depth d (§8.38): about $2^{0.41 d}$. Each free bit multiplies them by 1.764, not 2,
  because about 6% merge at every step.
- **The record is the best of those walks** under coin flips (§8.38): $R(d) \approx 0.826\,d + 0.8$. This
  predicts depths 49 to 81 within 4.1 cells.
- **Column 1 next to 0101..., from a real right half** (§8.4 to §8.11): the wheel $U$, an exact coding of the
  rotation by 17/56, kicked by domain walls in notches of 1/28 turn.
- **The best finite seed for 0101** (§8.24): its total width plus at most 9 steps, for right halves up to 32 cells.
- **The same for every word up to period 4**, and for a random word (§8.42): total width plus +6 to +10, growing
  like a logarithm of the depth.

## 4. Routes closed (do not reopen without new evidence)

- **Bounded runs from a thin layer**: at every layer width up to 16 the zero runs still grow with depth (§8.14).
  So no local rule of column 1 bounds them (§8.41).
- **Periodic column 1**: settled by Jen's theorem (§8.13). The 550,201 periodic words searched were a check of the
  instrument, not evidence.
- **"Structured families" beating chance**: luck (§8.16).
- **The entropy squeeze as a reduction** (§8.33). It restates the problem. It needs a lower bound on a column's
  entropy that nobody has.
- **The SAT crib** (§8.37): correct, but slower than enumeration.
- **A merging lemma as the easy half** (§8.38, corrected). A merge needs black cells, so it is the original
  problem's flavour again.
- **A Chebyshev-type exact identity in the survivor counts** (§8.41): none is visible.
- **"Periodic words hold deep zero runs down"** (§8.42): refuted.
- **Self-similarity between depths d and 2d** (§8.36, RC5): none beyond chance.

## 5. The one missing statement

Every form of the problem ends at the same sentence: **keeping the wall's conditions costs real information.** The
delivery side is a theorem (the channel bound). The cost side holds exactly only next to a constant wall. There
column 1 can only turn black once, and that is Condrey's proof. Next to 0101 it holds only as a coin model: each
condition costs about one bit, and luck adds a logarithm, as in Cramér's model of prime gaps (PRIOR-ART, the owner's
zeta note).

**Why it is hard.** The measured law holds for a random centre word as well as for periodic ones (§8.42), so a proof
cannot come from properties every word shares. It must use what is special about periodic words, as Jen's theorem
and Condrey's proof do. The one structure found that exists only next to the 0101 wall is **the wheel**: no other
trace tried turns a wheel of its own (§8.8). The likely shape of a proof is a size argument, like Chebyshev's
proof of Bertrand's postulate, and not a proof that Rule 30 is random.

## 6. Live leads (2026-10-05)

1. **The wheel's kicks.** What sets a kick's size is unknown (§8.8, §8.9). The owner's lead, from the interpolation
   shaders: rotation shows an oscillating hole at the centre, and rotation with translation makes it drift. Being
   dug next: is a kick's size set by how far its wall travelled through the rotating domain?
2. **Local's depths 85 and 89** (CLOUD-LOCAL.md, lead M4). They were running on Local when this was written. A blind
   prediction waits for them: R(85) between 65 and 75, R(89) between 69 and 79 (MG8 in `rule30_merge.py`).
3. **Job M3** (CLOUD-LOCAL.md): the channel bound at layer widths 27 and 28, and the counterexample search to 34
   cells.

## 7. Reading order

1. This file.
2. `WORKFLOW-SAVED-MEMORY.md`: the working rules. Predictions are written before runs, failures are recorded,
   prior art is surveyed before leaps, and every script that produced a recorded number is kept.
3. `CLOUD-LOCAL.md`: how Cloud and Local split work, and the ledger (start from main and the ledger, never from
   memory).
4. `PRIZE-PROBLEMS.md`: the honest summary at the top, then §5, §7, §8.4 to §8.14, §8.20, §8.36 to §8.42.
5. `PRIOR-ART.md`: the dated surveys, especially Condrey, Jen and Kopra, Rowland, and the prime-gap parallel.
6. `tests/probes/PROBES.md`: the index of every probe (row `lexicon/`).

## 8. How to reproduce the core numbers

Everything is in `tests/probes/lexicon/`. Each script's header gives its command, cost and predictions. Pure
Python 3 scripts need nothing else, and the C engines need a C compiler with OpenMP.

| Script | What it computes | Cost |
|---|---|---|
| `records.c`, `rule30_records.py` | exact R(d), the forced walk over every prefix | seconds to depth 61 |
| `records_bits.c`, `records_fast.c` | the same, 64 prefixes per machine word (Local's engines) | 12 times faster |
| `rule30_merge.py` (and mode `recur`) | the distinct walks D(d) and the merge rate | a minute |
| `rule30_wall.py` | the wall form, checked against `records.c` | seconds |
| `rule30_words.py` | black, white and both, for every word up to period 4 | 25 minutes |
| `rule30_race.py` | the information race in the combined game | seconds |
| `rule30_uniform.py` (modes `deep`, `horizon`, `windows`) | total width plus a constant or a logarithm | 15 minutes |
| `rule30_complement.py` | the best finite seed for 0101 (§8.24) | 5 minutes |
| `ladder.c`, `rule30_ladder_deep.py` | the ladder R(m, s) | minutes |
| `entropy.c`, `entropy2.c` | the channel bound | minutes to hours by width |
| `wheel_orbit.c` | Proposition 6's certificate for the pure wheel | minutes per phase |
| `rule30_walls.py`, `rule30_slips.py` | the wheel's domain walls and kicks | minutes |

**The math check.** After any edit of a document with TeX in it, run `python3 tests/probes/mathcheck/check.py
PRIZE-PROBLEMS.md` once `npm install` has been run in that folder. It must report 0 TeX errors and no stray dollar
signs.

## 9. Checks before you start

- `git log --oneline -5` on main and on the working branch. Read the ledger's last rows.
- `python3 tests/probes/lexicon/rule30_wall.py` must print ALL CHECKS PASS (4 seconds). It ties the wall form to
  `records.c`.
- `python3 tests/probes/lexicon/rule30_merge.py` must print ALL CHECKS PASS (14 seconds).
- Then stop, and ask what to do.
