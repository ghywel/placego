# The first three columns are affine in column 1

*Short proofs restated from the running text. Derived from [PROOFS.md](../PROOFS.md), entry "C.7 The first three
columns are affine in column 1 (RULE30-PRIZE.md §8.58; used in COLLATZ-PRIZE.md §5)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved (a table computed from the inverse.

## In plain words

The first three columns left of the middle copy or flip visible bits; the fourth introduces a formal product.

**What it says.** The inverse rule next to the blinking wall gives copy, flip and delay formulas through column −3. Its arbitrary-input formula for column −4 combines consecutive visible bits with an "and" gate.

**A domain matters.** Actual right-side histories cannot have consecutive visible ones, so that fourth-column product is always zero. GPT's second-reading audit derives affine formulas through column −6 on this restricted domain. Column −7 then combines visible bits separated by one intervening bit; four admissible prefixes show that interaction survives. Independent review is pending.

**Why it matters.** A product in a formal formula can disappear when the inputs are constrained. The audit locates a surviving interaction without claiming the entire evolution is linear or supplying the finite left tail needed for a prize counterexample.

**An everyday picture.** An "and" gate wired to two signals that can never both be on produces only zero. A later gate connected to different signals can still combine them.

## The formal statement and proof

*Where:* §8.58. *Bears on:* the counting form; the Collatz twin. *Status:* proved (a table computed from the inverse
rule next to the alternating wall; the product first appears in column $-4$).

**Fact.** Next to the wall $0101\ldots$, write $c_s$ for column 1 at time $2s$ (the visible bits). At times $2s$ and
$2s+1$ the forced columns are:

| Column | $-1$ | $-2$ | $-3$ | $-4$ |
|---|---|---|---|---|
| time $2s$ | $\bar c_s$ | $c_s$ | $\bar c_{s+1}$ | $c_s\,c_{s+1}$ |
| time $2s + 1$ | 1 | $c_{s+1}$ | $\bar c_{s+1}$ | $c_{s+2}$ |

Column $-2$ is column 1 with every visible bit held for two steps, column $-3$ is its complement one step on, and
the first product appears in column $-4$.

*Proof.* Lemma 1's explicit form gives column $-1$ ($1$ at odd times, $\bar c_s$ at time $2s$); each further
column is the inverse rule $x(-j, t) = x(-j+1, t+1) \oplus (x(-j+1, t) \vee x(-j+2, t))$ applied to the two columns
to its right, which the table carries out for $j = 2, 3, 4$. $\square$


*Admissibility audit (GPT, 2026-10-07, R4/GC299; independent review pending).* The table above is formal in arbitrary visible words. An actual right half beside0101 obeys Lemma3's no11 condition, so its depth4 product is zero. R4 derives affine even/odd formulas through depth6 and the depth7 odd value1 XOR c_(s+3) XOR (c_(s+1) AND c_(s+3)). A single preregistered256-seed check matches literal inverse columns; four witnesses with c_s=c_(s+2)=0 realize all product-input pairs and mixed XOR1. Thus depth7 is nonaffine in these four visible inputs on the driven-right prefix domain. This does not provide an eventually white initial left tail or a global linearization; C7's formal table is preserved.
