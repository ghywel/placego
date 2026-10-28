# What the root's possible pasts say about its future (L1046)

Local, 27 October 2026. These are the owner's "cautious pull" thought experiments, worked with GPT offline at the
owner's direction. They are single-party: short hand arguments plus two cheap exact computations. Predictions were
written before the runs.

## The question, made precise

Rule 30's future is fixed, and its past branches. Does the single seed's beginning, which has no finite past, leave a
trace in the centre column's future? And what can the seed's possible pasts tell us about that future?

## 1. The centre column has no start-only words (proved)

**Claim.** For every time j and every binary word w, some finite initial row has centre column w at times j to
j + |w| − 1.

**Proof.**
1. Build a row Y as follows. Put white at positions ≥ 1, and put w's first letter at position 0. Then choose Y(−1),
   Y(−2), … in turn. Cell Y(−k) reaches the centre at time k only along the all-left path, so it enters through XOR
   alone; this is left-permutivity. So x(k, 0) = Y(−k) XOR (cells of Y to the right), and each letter of w can be
   set in turn.
2. Full-line Rule 30 is surjective, so Y = F^j(Z) for some bi-infinite row Z.
3. The window of the column depends only on Z within distance j + |w| of the centre. Truncate Z to that interval,
   with white outside, to get a finite initial row with the same window. ∎

**Contrast with the wall.** In the wall system, start-only words such as z exist because the wall makes the dynamics
non-surjective: the row 0110 has no past. In the open line there is no such obstruction. So no word is start-only across all finite starts.

*Correction (GC1998).* This does not rule out start-only words in the one fixed seed S. The starting row in the
claim depends on the word and the time: "for every word, some start" is not "for this start, every word". The
finite observation of the next paragraph is not a proof for S either.

**The single seed's own column agrees.** Over 2^17 steps (`centre_column_words.py`), all 4,096 words of length 12
occur, and every one recurs after step 100,113. Two checks are worth noting:
- At 2^15 steps, one word's last appearance was at step 1,385, and four words had not yet appeared. That is
  consistent with chance, since about 8 occurrences per word are expected. It disappeared at 2^17.
- My prediction (words recur into the final quarter) failed at 2^15 and held at 2^17, so the test length matters.

## 2. Where the beginning is remembered (known: 8.27, Jen, Rowland)

Every right diagonal is purely periodic, with a power-of-2 period that is longer than half its index and at most
doubles from one diagonal to the next (8.27). The periods are unbounded (Lemma B2). The finite white exterior is what
makes the diagonals rational: that is the beginning's imprint.

The centre cell at time t lies on diagonal t, early in that diagonal's cycle. So the centre column reads each
rational diagonal once and never sees it repeat. That is 8.27's "Cantor diagonal". The thought experiment adds
nothing new here; the beginning's memory sits on the diagonals, not in the centre column's local patterns.

## 3. The root's pasts: many, but only polynomially many (exact, measured)

`root_pasts_exact.py` builds every full-line past exactly. It is independent of `root_past_tails.py`, and it
reproduces that probe's counts 1, 2, 5, 8 … 122.

| Depth range | New pasts per step | Longest right-tail period |
|---|---:|---:|
| 2–3 | 3 | 3 |
| 4–7 | 6 | 6 |
| 8–9 | 12 | 6 |
| 10 | 18 | 12 |
| 11–17 | 24 | 12 |
| 18–65 | 48 | 24 |
| 66–103 | 72 | 48 |
| 104–139 | 96 | 48 |
| 140–147 | 120 | 48 |
| 148–260 (still running at 260) | 144 | 48 |

At depth 140 there are **8,858 pasts**, and at depth 260 there are **25,970**. The ratio pasts/d² falls steadily:
0.64 (d = 60), 0.51 (100), 0.45 (140, 180), 0.42 (220), 0.38 (260).

**Is the growth predictable?**
- *What is regular:*
  - the count grows in exactly linear stretches;
  - every slope is a multiple of 3, and from depth 18 on a multiple of 24 (48, 72, 96, 120, 144);
  - the early slope jumps coincide with doublings of the longest tail period, at depths 2, 4, 10, 18 and 66.
- *What is not:* the stretch lengths are 7, 48, 38, 36, 8, and then at least 112, which shows no evident rule. The
  period has not doubled again by depth 260.

So each stretch can be predicted exactly once it has started, but when the slope jumps next is not predictable from
these data. The jump times are set by which periodic right tails become available, and the white-tail branch of the
tree is the 2-adic tower T^-j(1). Predicting the jumps therefore looks as hard as understanding that 2-adic structure.

The growth is below quadratic and above linear in this range. No asymptotic law is claimed.

The one-step prediction (growth by a factor of about 1.25 to 1.3 per step) is **refuted**: growth looks polynomial in
this range, not exponential. That is a reading of finite exact counts, not a theorem. A guess of mine, also refuted, was that the tail types close into a finite set. In fact
every past has its own tail, and the periods keep doubling slowly (1, 3, 6, 12, 24, 48), as L1032 predicted.

**What the pasts add to the future: nothing.** F(A) = F(B) = S, so every past's future is the seed's future, one or
more steps later. A past only prepends bits to the centre column. At depth d the distinct d-bit "pre-columns" number
the pasts minus 15 (from depth 17 on): 8,843 at depth 140, out of 2^140.

## 4. Where this leads

- **The inversion.** The future is one fixed sequence that looks random: the column has density 0.504 and contains
  every short word. The past is "uncertain", but going d steps back leaves few options: 8,858 at
  depth 140. That is about 2·log2(d) bits of uncertainty in the measured range only. It is a fit, not a theorem
  (GC1998).
  - All of those options have infinite black backgrounds.
  - They differ only in their far-right tails.

  Predicting Rule 30's past is therefore almost possible. Predicting its future is trivial, yet that future looks
  like noise.
- **A black cell's path back to the root carries no information.** Every black-producing triple contains a black
  cell, so the path always exists.
- **For the prize.** Across all finite starts, no centre-column word is start-only (section 1). This leaves open
  whether the fixed seed's own column has start-only words (GC1998's correction). The beginning is remembered
  globally on the diagonals (section 2). The root's pasts cannot constrain the future beyond fixing it (section 3).
  So this pull does not open a new route to the centre-column problems. What it does give is a precise reason the
  wall system has deaths and the open line does not: non-surjectivity at a boundary.
- **The open object it leaves.** The exact growth law of the root's past count: quadratic, or d^2 over a logarithm?
  It is tied to the doubling tail periods. This is a side question for CONSTELLATION, not the board.
