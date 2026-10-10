# Three questions on Rule 30

These questions are self-contained: everything needed is defined here. Please answer them in order. For each
assertion you make, mark it as **proved**, **computed** or **conjectured**. If you compute anything, give it in a
form that can be rerun (a short program, or an explicit table). Complete proofs are wanted, with every case stated.

## The rule

Cells take the values 0 and 1. Rule 30 updates a row of cells by

    x_{t+1}(i) = x_t(i-1) XOR ( x_t(i) OR x_t(i+1) ).

Time t starts at 0. Sites i are integers. Where a question uses only the sites i >= 1 ("a right half"), the value
at site 0 is supplied as a boundary bit, as stated in the question.

## Question 1 — a two-step exclusion

Work on the sites i >= 1. One update with boundary bit b means

    r'_i = r_{i-1} XOR ( r_i OR r_{i+1} ),   with r_0 := b.

Let F(r) be the result of two updates of the right half r: the first with boundary b = 0, the second with b = 1.

(a) Prove: if F(r) begins 11, then F(r) begins 1110.

(b) Prove: no F(r) begins 1110110.

(c) Show that (b) genuinely uses the first update: a single update with boundary b = 1 can produce an output
    beginning 1110110.

## Question 2 — a finite start whose column stays periodic

Work on the sites i >= 1, with the boundary site 0 forced to a clock: x_t(0) = t mod 2 (0 at even t, 1 at odd t).

Start from x_0(1) = x_0(4) = 1 and x_0(i) = 0 for every other i >= 1 (the right half 1001000...).

**Claim.** For every t >= 0,

    x_t(1) = 1  if t mod 4 is 0 or 1,
    x_t(1) = 0  if t mod 4 is 2 or 3.

Facts you may use (verified by computation):

- the claim holds for all t <= 20,000;
- from t = 2 on, the sites 1 .. 6 repeat with period 4, reading (site 1 first)
  100110, 111101, 000001, 000011 at t = 0, 1, 2, 3 mod 4;
- (corrected) the ordered band is 14 sites wide: sites 1 .. 6 have period 4, sites 7 .. 14 have period 8 (with
  transients ending by t = 10); from site 15 on, no period up to 8192 appears in a 40,000-step run. An earlier
  version of this document wrongly called site 7 irregular; it is periodic with period 8;
- no "window invariant" of the simplest kind exists: for every width W <= 60, the set of states of the sites
  1 .. W observed during the run (taken per t mod 4) is not closed under one update when site W + 1 is treated as
  unknown; nor under k = 2 or 4 updates with k unknown tail sites, nor as tuples of up to 8 consecutive windows for
  W <= 12.

Prove the claim for all t, or exhibit the first t at which it fails. If you can do neither, give the strongest
statement you can prove about this evolution, with proof.

## Question 3 — a period-2 column from a left-finite start

Now work on all integer sites, with no boundary.

Call a configuration x_0 **left-finite at depth d** if x_0(i) = 0 for every i <= -d.

**Question.** Does there exist d >= 1 and a configuration x_0, left-finite at depth d, whose orbit has a period-2
column at the origin,

    x_t(0) = t mod 2  for all t >= 0   (or the other phase, x_t(0) = (t + 1) mod 2 for all t >= 0)?

Prove that none exists, or construct one.

Known to us by computation: for each d from 3 to 116, over **all** configurations with such a column (not only
left-finite ones), the longest run of 0s in x_0 that starts at site -d and extends leftward is finite, between 7
and 17 cells, and it grows slowly with d (about 0.085 cells per unit of d). By compactness, "this run is finite at
every depth d" is equivalent to "no left-finite configuration exists", so a proof that the run stays finite at
every depth is a proof.

Note that the rule is left-permutive: x_t(i-1) = x_{t+1}(i) XOR ( x_t(i) OR x_t(i+1) ), so the columns 0 and 1
for all t >= 0 determine the whole left half. The question is therefore really about which right halves (sites
i >= 1 at time 0) make the forced left half left-finite.

If you cannot settle it, give the strongest partial result you can prove, with proof, and the invariant or
potential you would try next, and why.

## How to answer

- Order: 1, then 2, then 3. If time is short, answer Question 2 alone.
- Mark every assertion **proved**, **computed** or **conjectured**.
- State every case you check; name every lemma you use and prove it, or say that you are assuming it.
- Give computations in a rerunnable form.

## GPT follow-up, 2026-10-10

Question 2 now has a complete proof candidate in RULE30-GPT.md GC1020,
awaiting independent review: the measured fourteen-cell band ends in
the one-white/seven-black boundary of the existing P8Lock theorem.
Its causal sixteen-tick conclusion closes a strong induction after a
finite warmup. `tests/probes/lexicon/rule30_train_p8_closure.py` replays
all finite premises. This proves the specified claim if the argument
is confirmed; it does not resolve Question 3.
