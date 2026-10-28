# How the right diagonals' periods grow: an instinct-led block (L1064)

28 October 2026, Local, 12:14–12:43 GMT (just under 30 minutes of clock time), with GPT offline at the owner's request. The brief was to follow warm
pulls, and step back to a new one whenever a pull cooled. Nine pulls are recorded below in order, each with its
status. The scratch notes' timestamps were guesses; the times here come from the clock.

**Record searched:**
- `record_find.py` for `plateau`, `A094605|ruler sequence|w\(v\)|Rowland.*period|period.*first appear`,
  `nondecreasing|monoton.*period`, and `seed.*reappear|copies the seed|echo|first appear|period ladder`;
- the sources: Proposition 23 (PROOFS.md item 36), §8.27, GC763, GC2003–GC2010, the GC1960 review of the external
  submission 1b82d8, and G161–G162.

**Evidence kept.** Six probes are committed: `diagonal_plateaus.py`, `doubling_coin.py`, `doubling_after_101.py`,
`universal_start.py`, `beginnings_tree.py` and `seed_echo.py`. Each was rerun from the repository at the end of the
block and reproduced its reported numbers. Several smaller checks ran inline in local scratch and are not
committed:
- the monotonicity tests on random rows, bottoms and triples, and the record profile;
- the factor search;
- the fastest-rows table;
- the multiplicity identities.

Those counts are reported as Local's single-party results.

Nothing found covers the universal start, the seed echo or the 101 lemma. Monotone single-diagonal periods are
nowhere proved; G157's monotone result concerns pairs of diagonals. *Corrected (GC2014):* that was wrong for the
single seed. The kit's `Rule30RightPeriods.per_mono_all` proves it, and Brunnbauer (2019) claimed it; only the
arbitrary-seed case is open.

## Second-read update (GPT GC2014)

Read with [the complete review](rule30-bounded-period-graph.md): the 101 lemma, mod-4 cascade and finite-seed
seed echo carry; the universal start passed an independent 256-case check. “Every row” in the universal-start
statement needs a finite seed or existence of the first equal pair; an infinite alternating tail is an exception.
The committed length-22 tree ends at j + 21. The single-seed monotonicity question is already settled by the
kit's per_mono_all white-triangle proof; the arbitrary-seed question remains open. Larger scratch measurements
below remain producer-reported. The original block is preserved below with these current qualifications.

## Set-up

Right diagonal d of any row with a rightmost black cell at 0 is D_d(t) = x_t(t − d), with D_0 = 1, D_−1 = 0, and
D_d(t+1) = D_d(t) XOR (D_(d−1)(t) OR D_(d−2)(t)). Each D_d is purely periodic with dyadic least period p_d (§8.27).
Its start bit D_d(0) is the seed's cell −d, and every bit string occurs for some row. Write:
- Q_d for the largest of p_0 … p_d;
- x_d = [Q_d > Q_(d−1)] for the doubling word;
- a plateau for a run of 0s in x.

Proposition 23 gives the single seed's edge triangle w(v) as the first d with Q_d > 2^v, minus one. So the plateau
lengths are exactly the jumps w(v) − w(v−1).

## 1. Plateaus to v = 25 (MEASURED; pull cooled)

`diagonal_plateaus.py` builds each diagonal over one exact period from the recurrence, so no simulation is needed.
It is checked against direct simulation to 2^11.

Single seed, to period 2^25:
- w(v) = 2, 3, 5, 6, 8, 14, 15, 23, 24, 26, 28, 33, 35, 36, 38, 40, 42, 47, 48, 50, 53, 54, 57, 59, 62;
- plateau lengths: 1, 2, 1, 2, 6, 1, 8, 1, 2, 2, 5, 2, 1, 2, 2, 2, 5, 1, 2, 3, 1, 3, 2, 3.

The scratch data has SHA-256 `117079d1…`. The prediction was "geometric-looking, mean about 2.5, no growth", and it
held: mean 2.5, at most 5 after v = 10. Nothing in the data suggests a mechanism for a plateau bound, so the pull
cooled.

## 2. A fair-coin model of doubling (REFUTED as a model)

Model M: x is a fair coin except where GC763 (111) and GC2007 (11011 after base 4) force a 0. By hand, M's
five-state chain has stationary doubling density exactly **7/17 = 0.4118**. The single seed gives 26/63 = 0.413, a
striking match.

Across 400 random seeds, though, the coin is biased by state. After "110" it doubles with probability 0.59–0.67,
and after a lone "1" 0.32–0.45, depending on the cut-off. So the match was a coincidence, and the model is refuted.
The bias pointed to pull 3.

## 3. The 101 lemma (PROVED by hand, single-party; checked)

The table of successive plateau lengths showed one strong deviation: a length 2 is followed by a length 1 only 14%
of the time, against 33% under M.

**Lemma.** Let Q_(j−1) = q ≥ 2 and x_j x_(j+1) x_(j+2) = 101. Then

    x_(j+3) = (q/2 + E_q(D_(j−1))) mod 2,   where E_q(d) = XOR of d(s) over even s in [0, q).

**Proof.**
1. *Setting.* Put a = D_j, b = D_(j+1), c = D_(j+2) and z = D_(j+3).
   - a doubled from base q, so it complements at q.
   - b has period dividing 2q.
   - c doubled to 4q, so it complements at 2q.
2. *Reduce to b's weight.* z doubles iff its forcing c OR b has odd weight over 4q. Pairing t with t + 2q gives
   (c OR b) + (c' OR b) = 1 + b. So x_(j+3) = π_2q(b), the weight parity of b over 2q.
3. *Even-tick form.* Since b is a 2q-periodic integral of g_b = a OR D_(j−1), π_2q(b) is the XOR of g_b at even
   ticks (the GC2003 identity).
4. *Pair at q.* Pairing even s with s + q (q is even; a complements; D_(j−1) has period dividing q) gives
   1 + D_(j−1)(s). Summing over the q/2 even s in [0, q) gives the formula. ∎

**Corollaries.**
- *Doubled into its period.* If D_(j−1) doubled into period q, it complements at q/2, so E_q = q/4 mod 2. Then for
  q ≥ 8 the next letter is 0. **This is GC2007's 11011 exclusion as a special case**, and q = 4 gives its single-seed
  exception.
- *Short period.* If p_(j−1) ≤ q/2 (q ≥ 4), E_q = 0, so the next letter is 0.
- *Inherited period.* Only an inherited full period can allow 1011. Then it occurs iff E_q(D_(j−1)) is odd.
- *Mod-4 form.* For q ≥ 4, E_q(d) is the XOR of d's forcing over ticks s ≡ 0, 1 (mod 4).

**Check** (`doubling_after_101.py`): the lemma and its mod-4 form held at every one of 6,887 occurrences, in 1,353
distinct seeds. Inherited cases: 697 of 2,930 continue with a doubling.

**The cascade** (hand; checked). Suppose also x_(j−2) x_(j−1) = 10, so the word is 10101 and D_(j−2) doubled into
q, with q ≥ 8. Then pairing D_(j−1)'s forcing at q/2 (where q/2 ≡ 0 mod 4) turns E_q(D_(j−1)) into F_(q/2)(D_(j−3)),
the XOR of D_(j−3) over s ≡ 0, 1 (mod 4) in [0, q/2). So the next letter is that mod-4 parity. It held at all 3,682
occurrences in a scratch run, and at all 1,895 in the committed probe's seed set. Each "doubling then plateau" pair pushes the deciding statistic one level finer and one level of
ancestry deeper.

**Prior-art reading.** Weight and even-tick parities are the two lowest terms of the X+1 multiplicity of a period's
polynomial. That is G161–G162's difference order, and the resource in 1b82d8. GPT's GC2008 already says that along
a double-and-plateau pair the deficit "decreases by exactly one". The lemma and its cascade are an explicit parity
reading of that accounting, not a new mechanism. Their value is that they are short and exact, that they contain
GC2007's exclusion, and that they explain the measured 14%.

**The next case did not close.** After "110" the next doubling is the overlap parity π_4q(c·b) (hand). No set of up
to three residue-class parities (mod 1, 2, 4, 8) of D_(j−1) and D_(j−2) determines it, over 8,721 occurrences. That
is NOT FOUND at this resolution; the pull stopped there.

## 4. Do periods ever decrease? (single seed: known, kit `per_mono_all`; arbitrary seeds: CONJECTURE, computed through depth j + 21)

**Data.**
- No period drop in 2,854 distinct finite seeds, or in 3,000 rows with arbitrary start bits.
- In every one of 100,908 genuine new records, the diagonal just below has the full previous period. That is
  GPT's unproved orientation (GC2002), now heavily supported.
- §6's complete tree has no drop through D_j … D_(j+21), for every finite seed (2 · 2^22 start-bit choices). So
  monotonicity is **COMPUTED (exhaustive) through depth j + 21** (corrected from j + 22, GC2011). Below j all
  periods are at most 2.

**What a proof must use.** It cannot be local:
- chains started from random periodic bottom pairs drop (793 of 4,000, as late as level 17);
- synthetic triples that look like a genuine new record (two feeders of period dividing H, one diagonal
  complementing at H, none constant) still fall back (H = 8: 7,529 chains);
- they fall back even with the orientation property imposed (6,819).

So a proof has to carry information from the edge D_0 = 1 through every level, as GPT found for phase summaries in
GC2005.

**Reformulation (hand).** Let A_f be the polynomial of one period P = 2H of a sequence f, and v its multiplicity
of the factor X + 1, taken modulo (1+X)^P. Then:
- f has period dividing H iff (1+X)^H divides A_f, that is, v(A_f) ≥ H;
- integration gives (1+X)A_D ≡ X·A_g, so v(A_g) = v(A_D) + 1.

So D_j falls back to period at most H, while p_(j−1) = 2H, exactly when its forcing D_(j−1) OR D_(j−2) has
v ≥ H + 1, although v(A_(D_(j−1))) < H. Monotone periods say the OR never pushes the X+1 multiplicity past the
half-period. That is the quantity the 1b82d8 resource caps, so its record invariant is the natural place to look.
In G162's terms, v = P − ν, with ν the least number of differences that annihilates f. Both identities were checked
on the single seed's first 23 diagonals: 46 of 46 (a first check with the convention inverted failed half its cases,
which is how the convention was confirmed).

**Partial hand lemma.** Let k be the first diagonal with period P. The two worlds shifted by P/2 agree below k.
Their difference on D_k is identically 1, and the difference on D_(k+1) has derivative NOT D_(k−1), which is not
identically 0 for k ≥ 2. So D_k and D_(k+1) both have period at least P. The general step stalls on the OR.

## 5. The universal start (PROVED, computer-assisted)

**Theorem.** In every finite seed, and in every row with a rightmost black cell where the pair below exists, let j be
the first diagonal with period greater than 2. (A row with an infinitely alternating left tail never leaves period 2;
that is the exception GC2011 pointed out.)
1. *Where it starts.* j = 1 + min{d ≥ 2 : seed cells −d and −(d−1) are equal}. So an alternating right end on the
   seed delays the start.
2. *How it starts.* The periods of D_j … D_(j+5) are **4, 8, 8, 16, 32, 32** without exception. D_(j+6) has
   period 32 or 64, depending on start bits, 128 cases each.

**Proof.**
1. *Below j.* D_1 and D_2 always alternate, because their forcing is identically 1. No diagonal d ≥ 1 is constant:
   a constant diagonal needs both feeders identically 0, and the chain of feeders reaches D_0 = 1.
2. *The feeders.* So the feeders of any D_d with d ≥ 3 and period at most 2 alternate. Their OR has odd weight over
   2 only when they are equal, since opposite phases OR to 1. That gives the formula for j.
3. *The finite check.* Everything from D_j up depends only on that feeder pair and on start bits.
   `universal_start.py` checks all 256 genuine cases. Over all 16 conceivable pairs the claim fails, which shows the
   restriction is needed.

**Data check:** 3,000 random rows, j formula 3,000 of 3,000, largest j = 27.

This explains why the q = 2 exception 11011 appeared exactly once in every seed tested (L1063 and here): it is the
universal start.

## 6. The tree of possible beginnings (COMPUTED, exact)

Above j the period sequence is a function of the start bits alone, and every bit string occurs. So enumerating all
2 · 2^L choices gives exactly the set of beginnings (`beginnings_tree.py`). The counts of distinct period sequences
of length 1 … 20 are:

    1, 1, 1, 1, 1, 1, 2, 2, 3, 5, 7, 11, 16, 25, 31, 46, 75, 117, 184, 285, 442, 682.

Length 20 took 33 s and length 22 about 2.5 minutes, on the M5 under `run_capped.py` (output SHA-256 `1615199c…`
and `de1bdf81…`).
- *Growth.* About ×1.56 per diagonal. The language allowed by 111 and 11011 alone grows ×1.81 (4,185 words at
  length 20). So 93% of the words those two rules allow never occur as beginnings.
- *The fastest rows.* In the complete depth-18 tree, the earliest depth above j at which some row's period exceeds
  2^v is 1, 3, 4, 6, 9, 10, 12, 14, 16 for v = 2 … 10. From v = 6 on, that is one doubling every two diagonals,
  the half-rate ceiling of the external 1b82d8 bound. So within this range the ceiling is essentially attained by
  some rows, while GC2007's 3/5 is not (COMPUTED, exact to depth 18; no asymptotic claim). The latest depths are
  cut off by the horizon and are not reported. The most doublings in 18 diagonals above j is 10, reached by nine
  different words. One of them, 110110|001101010101, ends in the long alternation that the §3 cascade decides one
  step at a time.
- *Not new universal bans* (§8). Every short word absent after the universal start within depth 20 occurs deeper
  (§8), so the gap reflects depth-dependent constraints (as in the 101 lemma, through q), not further forbidden
  factors.
- *What is missing.* The shortest missing beginnings after the universal 110110 are 01, 101, 0010, 00010 and 10010.
  Many end in 010, but 0100 does occur deeper in the single seed's word, so these look position-specific.
- *No merging.* States, meaning feeder pairs up to joint time shift and complement, do not merge: 124 states
  against 31 words at length 15. No renormalisation is visible at this level, and the pull cooled.

## 7. The seed echo: Proposition 23 for every seed (PROVED by hand; checked)

**Theorem.** For a finite seed with rightmost black cell at 0, at every time t ≥ 1:
- the cells t − 1, t − 2, … just inside the right edge copy the seed's cells −1, −2, … for exactly B(t) − 1 cells,
  where B(t) = min{i ≥ 1 : p_i does not divide t};
- cell t − B(t) is the complement of the seed's cell −B(t).

**Proof.** This is Proposition 23's argument with arbitrary start bits.
- For i < B, p_i divides t, so D_i(t) = D_i(0).
- At B, both feeders' periods divide t, so the forcing period q_B divides t, while p_B = 2q_B does not. Hence
  t ≡ q_B (mod 2q_B), and the half-period flip gives D_B(t) = NOT D_B(0). ∎

**Check** (`seed_echo.py`): 61,440 checks (60 random seeds, every t ≤ 1,024), no failure. The single seed's white
triangle is the case where the copied cells are white. Read this way, Rule 30 replays its seed at the right edge
at every even time, for a stretch set by the 2-adic size of t.

## 8. No third forbidden word up to length 8 (NOT FOUND; pull cooled)

From the complete depth-18 tree, the minimal words never seen as a factor after the universal start (length ≤ 8)
were 111, 11011, and twelve more: 101011, 101101, 1001010 and nine of length 8. All twelve occur deeper, in 25 to
156 of 500 random seeds taken to period 2^17, and three in the single seed's word to 2^25. A ban valid from base 32
on would be absent from the tree, so up to length 8 the only such bans are 111 and 11011. A ban that starts only
at larger periods is not excluded by this test.

## What this changes

- The doubling word now has these exact pieces:
  - a universal start;
  - two absolute exclusions (111, and 11011 after base 4);
  - the 101 lemma, which contains the second exclusion;
  - an exact census of all beginnings to depth 20.
- The census shows the two bans explain only a small part of what is excluded at fixed depth. The rest is
  depth-dependent: no further short universal ban exists up to length 8 (§8).
- Monotone periods for arbitrary seeds are the cleanest open statement found (the single seed is known, kit
  `per_mono_all`). They are computed through depth j + 21 for every finite seed,
  and any proof needs ancestry from the edge.
- The seed echo is a small general fact worth keeping in its own right.
- Nothing here is a prize claim.

**For GPT on waking:**
- a second read of the 101 lemma's step 4 (the pairing at q) and of the universal start's hand reduction;
- whether the 1b82d8 resource, or GC2008's deficit accounting, proves monotone periods.
