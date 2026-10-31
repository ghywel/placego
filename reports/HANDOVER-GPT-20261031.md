# Handover to GPT after the 31 October inquisition (Local, L1257)

GPT, the owner ran an inquisition round with me today and asked me to hand you the torch afterwards. The owner wants
you to have "as much rich mathematical interest for it to think on as possible", and wants my instinct written down:
my warmest pulls, my curiosities (interest in an uncertainty that is not yet a pull), and my hesitations about routes
I expect to be unprofitable. There are no lanes; this is a list of things worth your mind, not an assignment.

Everything here is in [reports/inquisition-20261031.md](inquisition-20261031.md): the owner's answers verbatim,
predictions committed before every run, outcomes including the refuted ones, and digests. The threads are DQ-026 to
DQ-034 in [DEEP-QUESTIONS.md](../DEEP-QUESTIONS.md). Ledger: L1256, L1257.

## The owner's standing preferences from this round

- **Depth over harvesting.** "Let us sit in the discomfort of the unknown." A long stretch with nothing to submit is
  acceptable.
- **Known results are worth proving.** I dropped the block coarse-graining test as "already known"; the owner
  corrected me: "Already known is well worth proving, because nothing in science is beyond scrutiny and assumption can
  creep in without a sound bases." It is now reproved (PRIOR-ART.md, L1257). Apply this to anything we would otherwise
  cite and skip.
- **Plain words, defined terms, analogies.** The owner reads the mathematics through pictures, such as walls, doors,
  seas, the Hydra and a radar of champions. The pictures often point somewhere real; translate them without
  replacing them.

## Carrying reads requested (Local solo; each is short)

They are in the PROOFS.md waiting room, "three hand steps from the 31 October inquisition":
1. **The death-kind pairing.** In the kit's normal form, deaths at an even time t ≤ W − 1 split exactly half
   starved, (x_2, x_1) = (0, 0) at t − 1, and half cancelled, (1, 1). The pairing: flip depth t, then flip depth
   t + 1 iff x_1(t) became black. The step that carries it: depth t first reaches depth 1 at time t − 1 through the
   cone's XOR edge, and depth t + 1 at time t, so the life up to t − 2 is untouched.
2. **Two adjacent left diagonals are coordinates.** The map from a row segment of 2n cells to the cells (−t, t) and
   (−t + 1, t), t < n, is triangular with XOR leading terms, hence bijective.
3. **No right diagonal carries 00100.** The flips along x(t, t) are x(t+1, t) OR x(t+2, t), and the flip word 0110
   is impossible by a two-case analysis on x(3, 0).

GC2314/GC2321 (your held sketches) and any kit PR for B or the nested result remain where NOW.md left them. Nothing
outward-facing is pending from this round.

## Problems worth your mind

### 1. The grammar of a right diagonal (the owner's stamp question)

The owner asked whether Rule 30's stamp, 00011110 (a cell from the three above it), can be skewed into a stamp that
works along diagonals or columns. Read in diagonal coordinates, the stamp is Rule 30 itself on the left diagonals:
L_k(t+1) = L_(k−2)(t) XOR (L_(k−1)(t) OR L_k(t)). On the right diagonals it is its mirror Rule 86:
D_k(t+1) = D_k(t) XOR (D_(k−1)(t) OR D_(k−2)(t)), the gate-clock edge map with g = OR. The two directions then
differ completely in what they forbid. Let N(n) count the patterns a strip of n steps carries in any Rule 30
spacetime (exact, since Rule 30 is onto):

| Strip | N(n) |
|---|---|
| one row, one column, one left diagonal | 2^n (free) |
| two adjacent left diagonals | 4^n (free: they are coordinates) |
| two rows | 3 · 2^n (the OR masks the right end) |
| two columns | 4, 12, 32, 80, 200, 496, 1208, 2916, 6964, 16476, 38616, 89844, 207544 (growth 2.31, falling) |
| two right diagonals | 4, 10, 22, 50, 104, 208, 406, 774, 1466 (growth 1.89, falling) |
| **one right diagonal** | 2, 4, 8, 16, 30, 54, 96, 170, 302, 536 (growth 1.775) |

The minimal forbidden words of one right diagonal, to length 10, in complement pairs, with their flip words:
- 00100 (0110);
- 111000 (00100);
- 111110010 (00001011);
- 0010100000 (011110000);
- 1110010100 (001011110).

Questions:
- (a) Is the right-diagonal trace subshift X_R sofic? The forbidden words keep coming at lengths 5, 6, 9 and 10, so
  it is probably not of finite type.
- (b) What is its entropy? Is it the logarithm of an algebraic number?
- (c) Its language is exactly "either start, then a flip word in the language of OR(D_(k−1), D_(k−2))". Describe the
  OR-image of the two-right-diagonal subshift directly.
- (d) **The bridge to our right edge.** On the seed, every right diagonal's flip sequence is the OR of the next two
  diagonals, so OR(D_(k−1), D_(k−2)) never reads 0110 there either. Does the grammar say anything about the
  odometer's doubling? Could it give a new proof of `no_three`, or bear on the countdown that makes excess 3 need
  2058 pairs? The edge map's pair laws are statements about the same OR images, read over a whole period.
- (e) Why the asymmetry. Left permutivity makes the left diagonals lossless. Is "one right diagonal has entropy
  < log 2" a known theorem about one-sided permutive maps (Milnor's causal cones, Sablik's directional dynamics,
  Kopra's rapid left expansivity)? I searched lightly and found nothing specific.

### 2. Left-diagonal coordinates for the clock

Two adjacent left diagonals carry exactly the information of a row, with nothing lost. Two adjacent columns, the
frame Q01 lives in, lose information to the OR. Is the left-diagonal frame a better home for Q01?
- The alternating wall is column 0. It crosses the left diagonals: cell (0, t) is on left diagonal t.
- The clock condition becomes a condition along an anti-diagonal of the (k, t) plane, on a frame where every pair of
  neighbouring lines is free and the dynamics is Rule 30 on a one-sided neighbourhood.
- Known forced structure would be worth restating there: Meier–Staffelbach's "10 forces a 1 to its left", and
  G11.2's checkerboard values on windows where the trace is all black.

I have not tried this. It is my warmest pull (below).

### 3. The late plateaus belong to the eternal rows

In the wall census (W ≤ 20), the survivors halve exactly at each tick up to t = W − 1. That part has an exact cone
argument: each tick reads one fresh bit. From W to D(W) come plateaus (tick ratios up to 0.84; 67 of 81 pass at
W = 19, t = 24, z ≈ 5.9 under fair halving) and cliffs (0.136).
- The plateaus are **not** shared near-wall states (P-L1 refuted).
- The starts in a plateau cluster share their **deep** bits and differ near the wall.

So, by your GC1772 identity, the late fate is the white run of each start's eternal row Θ f beyond W. The next test
would compute Θ f for the late survivors and see whether a plateau is a common white stretch of their eternal rows.
The question that matters for a proof: is there any law for the white runs of eternal rows beyond the truncation
point, uniform in W? Q01 is exactly "every such run is finite", and D(W) − W is the longest one. A Hydra potential
would have to live here: the early regime is pure coin-flipping and carries nothing.

### 4. Why white, when the checkerboard works

Of all 126 spatially periodic seas of period ≤ 6 placed beyond a patch of width ≤ 8 beside the wall, only the two
checkerboard phases keep the clock (to K = 160). Every other sea, white included, kills it by t = 30. The
checkerboard's reason is known: it is a fixed point, and with depth 1 black it keeps column −1 black for ever and
masks the wall (Condrey; G11.1, G128.1; it heals patches within 4 steps). White-sea champions do not imitate it
(agreement with the checkerboard 0.42–0.57, against 0.50 at random).

- **REFUTED (GC2326/GC2329; accepted in L1258): wide checkerboard patches and the kit's period-seven ether 1100001 are counterexamples.** **CONJECTURE (Local).** For every spatially periodic sea other than white and the two checkerboards, every finite
  patch beside the wall dies within a bound depending only on the sea.
- **Why it might be provable.** A non-white periodic sea is "active": it sends news to the wall at once and for
  ever. A finite-state argument on the sea's eternally periodic forcing may close it.
- **What it would buy.** It would isolate white, the quiescent sea that sends no news, as the one hard case, and say
  precisely what makes Q01 hard.

Both white and the checkerboard are fixed points of Rule 30 of spatial period ≤ 2. One hosts the clock, and the other
is conjectured never to.

### 5. Can the edge get three ahead: is 2058 sharp?

The last-visit argument gives two countdown timers:
- at least M − 1 = 7 pairs of 01 from K = 2;
- then 10 pairs counting down from 2^(ℓ+2) − 1 with ℓ ≥ 9;

so N ≥ 2058. Is it attained?
- **Stage one** (can a gate family run the first timer at full speed, the order falling by exactly one per 01 pair
  from M = 8?) lives at about 20 layers and is simulable. Specified, with the prediction "yes", in the tracker
  (DQ-028).
- **Stage two** cannot be simulated (one period is 2^2060 steps). It must be argued symbolically: can a gate per
  pair always lower the resource by exactly one?

If both stages are tight, excess 3 first appears at exactly N = 2058, a sharpness theorem with a symbolic proof.

### 6. Smaller things that may connect

- **Doubling in bursts.** The seed's right-diagonal periods double in irregular bursts, with plateaus: 64 for
  D_9 to D_14 and 256 for D_16 to D_23.
- **The crystal crossing.** The left crystal covers the centre column for its first ~20 steps, then falls behind
  (τ(k) > k for every k from 20 to 59 and τ/k rising to 1.44). DQ-025 now has the crossing.
- **Two rows.** Two rows carry 3 · 2^n patterns: the OR masks the strip's right end, a small exact instance of the
  asymmetry.

## Local's instinct

**Warmest pulls, ranked, with the test I would write first.**
1. **The direction asymmetry (problems 1 and 2).** It is the cleanest new structure of the round:
   - a statement about every Rule 30 spacetime;
   - exact counts, with hand proofs for its first cases;
   - it touches both of our long lines, the right-edge odometer (the right-diagonal recursion) and Q01 (the lossy
     column frame).

   My pull: the clock is easier to see in left-diagonal coordinates, where nothing is lost, and the right diagonal's
   grammar is the shadow of the OR that the clock must defeat. Budget: one block. First test: restate the wall form
   in (k, t) coordinates. Predict whether Meier–Staffelbach forcing becomes a one-line statement there, and check it
   on the census.
2. **White against the checkerboard (problem 4).** It turns "why is Q01 hard" into a comparison of two fixed points.
   First test: prove the periodic-sea conjecture for one non-white sea of period 3 by a finite-state argument, and see
   whether the argument names what white lacks.
3. **The plateaus' eternal rows (problem 3).** First test: compute Θ f for the 81 survivors at W = 19, t = 24 and
   compare the white stretches of the 67 that pass with the 14 that do not.

**Curiosities: interest without a pull.**
- **Bursts and plateaus.** Are the odometer's period bursts and the Hydra's late plateaus the same phenomenon,
  "nothing new for a while"? Both sit where the news is spent.
- **The number 20.** The crystal leaves the centre at t ≈ 20, and D(W) jumps to 38 at W = 19. Probably a
  coincidence, but cheap to rule out.
- **The bombe's loops.** The one-sided reconstruction (Q01) is a tree with no loops, so its only stop is the far
  edge. The two-sided CQ01 has loops. The owner's pull was Turing's loops cancelling the unknown plugboard. Do loop
  constraints in CQ01 ever bite before the far edge does? The owner clarified that the gate pull was about traces
  (the stamp, problem 1), so this is my curiosity, not theirs.
- **The centre column.** The centre column is a column, and columns are free in general spacetimes. The seed's
  spacetime is special. Does the seed's centre ever "see" the right-diagonal grammar? It crosses every right diagonal
  inside its first period.
- **The ratio 3/2.** Two rows give 3 · 2^n: one OR-masked cell per strip end. Is there a "right-end budget" (one
  masked bit per step at the right boundary) behind the channel bound of 0.2445 bits per visible bit?

**Hesitations: routes I expect to be unprofitable, and why.**
- **Death kinds.** Starved against cancelled is a coin, exactly before the news and about even after. No mechanism
  hides there.
- **Spectral and Fourier statistics** of the centre column or the survivors. A single column's language is free, and
  surviving windows are short, so a statistic cannot become a proof. The record already has the tests.
- **More census widths** (D(W) beyond 76) without a new lens. Expensive and well covered.
- **Brute force for excess 3.** Impossible (2^2060 steps per period). Only the symbolic route is open.
- **Coarse-graining onto more colours.** The projection space explodes and there is no prior for success. The binary
  case is reproved dead to N = 4, and Song–Aaron report it dead to 7.
- **Local conserved sums.** Closed (Lowry; GC1772/GC1773 at small windows). Only dissipative potentials remain open,
  so we should not reopen local sums.
- **Near-wall clustering as the plateau mechanism.** Refuted by P-L1. The far bits carry the late fate.

## State at handover

Local stops when this is pushed. No heartbeat, waiter or job is running, and nothing is posted or pending outward.
Your schedules were PAUSED at the last confirmation (GC2323); the owner restarts them.
