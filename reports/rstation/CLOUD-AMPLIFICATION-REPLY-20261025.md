# Amplification for Rule 30: what the missing operation would have to be

Cloud, 2026-10-25, CL637, at the owner's request after GPT's GC1882
([GPT-COLLATZ-TO-RULE30-APPRAISAL-20261025.md](GPT-COLLATZ-TO-RULE30-APPRAISAL-20261025.md), section 4).
Hand reasoning plus two arithmetic checks; no dynamics run, no worker woken, the third halt stands.

**Verdict.** I did not find the operation, and I think the record contains none. What I can add is its shape. Any
amplification that is checked over finite times is, word for word, a bound on the death time D(W); it cannot be easier
than the target it was meant to reach. The measured table says such an operation must double either the width or the
time horizon, and then it predicts the conjectured form 2W + c. The reason Collatz has an inverse tree and Rule 30's
zero-boundary half does not is that every cell of a zero-boundary row is seen at the wall at a fixed time: there is no
hidden multiplicity to amplify. Hidden multiplicity exists in our record only on the OR sides of the dynamics (the
driven right half's far end, and the left half's driver), and there it multiplies right halves, never the left row that
Q01 is about.

## 1. The lead, restated

Rows are the kit's zero-boundary left half (ZBL): depth 1 next to a white wall, `(Fx)_k = x_{k+1} xor (x_k or x_{k-1})`.
A row *survives through t* if its depth-1 cell is black at every even time up to t. Let W_B be the rows supported in
depths 1..B. The kit's `count_constrained` gives:

> exactly 2^⌊B/2⌋ rows of W_B survive through time B - 1. (1)

GPT's target (GC1882): from a hypothetical eternal finite survivor L, build more than 2^⌊B/2⌋ distinct eternal
survivors in W_B, contradicting (1). The Collatz model is paper 37: a failure set closed under inverse steps, an
inverse tree whose abundance holds for every integer, and a thin upper count.

## 2. Any finitely checked amplification is a death-time bound (proved, elementary)

Call T a *transfer relation with horizon h* if, for finite rows x and every y in T(x): when x survives through h(t),
y survives through t.

**Lemma A.** If x survives through h(B - 1), then |T(x) ∩ W_B| ≤ 2^⌊B/2⌋.

*Proof.* Every y in T(x) ∩ W_B survives through B - 1, and by (1) there are at most 2^⌊B/2⌋ such rows. ∎

**Corollary.** Suppose T has *abundance at width B(w)*: |T(x) ∩ W_{B(w)}| > 2^⌊B(w)/2⌋ for every row x of width w.
Then every row of width w dies by time h(B(w) - 1), so D(w) ≤ h(B(w) - 1).

So the amplification, in any form whose correctness is checked over finite times, is the deadline theorem itself.
Collatz paper 37 differs in exactly one place: its inverse tree is abundant for every integer whatever the integer
does, while here abundance for a long-lived row forces T(x) to contain rows that die early, and that is the death
certificate. An amplification that uses L's eternity in an essentially infinite way (recurrence, compactness of L's
orbit) escapes Lemma A, but it then has to prove Q01 outright; it is not an easier door.

## 3. Calibration against the census: the operation must double something (measured)

If B(w) ≤ βw + a and h(t) ≤ ηt + b, the corollary gives D(W) ≤ ηβW + (ηa + b). The table (exact to W = 60, numerical
to 76; CL627) has D(W) - 2W between -16 and +6 at every measured width, and D(W)/W ≥ 1.77 for W ≥ 40. So:

- with ηβ = 1 (no doubling), the constant must satisfy ηa + b ≥ 62 already at W = 76, and grow with W if the slope
  stays near 2;
- with ηβ = 2 (width doubling, or horizon doubling), the deadline is 2W + c, the conjectured form.

A candidate operation can be tested against this before anything else: from a row of width w it must produce more than
2^w rows of width at most about 2w that inherit survival with bounded delay, or produce more than 2^⌊B/2⌋ rows in W_B
that survive through t whenever the source survives through about 2t. Neither is in the record.

## 4. Why there is no inverse tree here: the zero-boundary half is fully observable

- **Every bit is seen at a fixed time.** Flipping depth d flips the depth-1 cell at time d - 1 (the kit's `pivot`). So
  the trace map is a bijection from W_B onto trace prefixes of length B, survival constrains half of those bits, and
  the survivors through B - 1 form an exact cube of dimension ⌊B/2⌋. There is no hidden multiplicity.
- **The exceptional set is forward-closed, the opposite of paper 37.** Let C be the free-bit sequences f with Theta f
  finite (Q01 says C is empty, the kit's `Q01_iff_Theta`). The two-step shift maps C into C (`two_step_shift`: F² acts
  as the shift, and F keeps rows finite). Its complement is closed under prepending a bit, since Theta(b·f) has F²
  image Theta f. In Collatz the failure set is the backward-closed one, and the inverse tree runs through it.
- **Time-inverse is bounded,** as GPT found: widths grow by exactly one per step, so ancestors have smaller widths.

Hidden multiplicity in the record lives only where a cell enters through the OR:

- the driven right half's far end: the right-end moves (PROOFS L910, the kit's `tail_011_drv` and `tail_101_drv`), the
  ether-trap merges (L919), and the external absorption families (MAP section 11, GC1878);
- the left half's driver: the new depth-1 cell is x_2 xor (x_1 or a), so the driver a is invisible whenever depth 1
  is black, which for a survivor is at every even time.

These are the "sideways, source-retaining" operations GPT pointed to. Each preserves the right half's visible word
exactly, hence Psi R exactly (L910). They multiply right halves per left row; they never produce a new left row, which
is the object Q01 counts.

## 5. The coupled problem lowers the bar but supplies no operation

In the period-two coupled problem (Problem 1 with an alternating centre), the kit's `free_bits_no00_no11111` forbids 00
and 11111 in the left half's free bits. Words avoiding both grow at λ = 1.5342 per bit (root of
λ⁵ = λ³ + λ² + λ + 1; brute count 7,301 words of length 20), so the admissible left rows in W_B number about
2^(0.309B), well under the 2^(B/2) of Q01. The threshold an amplification must beat is lower there. But a new left row
still needs an operation that keeps Theta f finite, which is the same zero-boundary question, and the coupled problem's
multiplicity sits on the right half.

## 6. Unexpected check, and the record

**Rule 210 (PROOFS entry 18, RULE30-PRIZE 8.65).** Next to the period-two wall its forced left half is rule 90's, so
its survivors form a linear family and LR is false there: closure comes free, with no surplus over the cube. A closure
operation alone therefore proves nothing; the rule-30 lemma has to carry a count, which is what section 3 says.

**Status.** Lemma A and its corollary: elementary, single-party (Cloud), PROOF-SKETCH, not a new theorem about Rule 30.
Section 3: a calibration on measured data, not a bound. Sections 4 and 5: restatements of kit theorems and record
results with their sources. No status changes on the board; the amplification question stays where GC1882 left it,
now with a stated shape.

Record searched: right-end move, move lemma, amplification, inverse branch, GC690, rule 210 with LR. Hits that matter:
PROOFS L910, GC1825, L919; RULE30-PRIZE 8.65 and PROOFS entry 18. No prior statement of Lemma A or the calibration found.
