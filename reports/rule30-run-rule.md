# One rule behind the map: Rule 30 on runs, and patches of simple histories

Local (Claude on the M5), 26 October 2026, L1000. At the owner's word: turn the orderly structures found on the
"chaotic" side into general rules that answer every state.

**Status.** Two general theorems, R and P, and their consequences. Each is proved by hand below, for every row of
every state. One exhaustive guard, `tests/probes/wolfram/run_rule_check.py` (3.8 s on the M5), replays them on every
state of the stated sizes: ALL CHECKS PASS, exit 0. This is single-party work, awaiting GPT's read.

**Prior art.**
- *R, the run rule.* Not found in the record (searches in the guard's header), nor in two web searches; Wolfram states
  the rule cell by cell. It is elementary and may well be folklore. No novelty is claimed.
- *P, the patch rule.* It is the light cone plus 8.66's damage-front identity, restated for agreement intervals.
- *New in this note:* the map that both theorems give, the edge law for every finite seed (section 4), the bridge law
  for black runs (section 3), and the counting laws (section 5).

Convention: space left to right, time down, black = 1, x′(i) = x(i−1) XOR (x(i) OR x(i+1)). A *run* is a maximal block
of one colour; the *head* of a black run is its leftmost cell.

## 1. Theorem R: Rule 30 acts on each run in place

> **R.** Each run of a row is replaced, in the same cells, by a word that depends only on its colour and length:
>
> | Run | Becomes |
> |---|---|
> | black run of length m | 1 0^(m−1): only its head stays black |
> | white run of length 1 | 0: a lone white cell stays white |
> | white run of length n ≥ 2 | 1 0^(n−2) 1: both end cells turn black, the inside stays white |

**Proof.** A cell's next colour is its left neighbour XOR (itself OR its right neighbour). There are six cases.
- *Black head* (left neighbour white): 0 XOR (1 OR ·) = 1.
- *Other black cell* (left neighbour black): 1 XOR (1 OR ·) = 0.
- *Lone white* (neighbours black): 1 XOR (0 OR 1) = 0.
- *First cell of a longer white run:* 1 XOR (0 OR 0) = 1.
- *Last cell of a longer white run:* 0 XOR (0 OR 1) = 1.
- *Inside a white run:* 0 XOR (0 OR 0) = 0. ∎

So in one sentence: **next step, the black cells are exactly the heads of black runs and the two ends of every white
run longer than one.** Everything else is white. (Guard G1: all 131,068 rings of length 2 to 16.)

## 2. Theorem P: two histories' agreement is eaten from the left at light speed, and holds on the right only on black

> **P.** Let x and y be any two rows, and [a, r] a maximal interval on which they agree, with r ≥ a+1. One step later
> they disagree at a, agree on [a+1, r−1], and agree at r exactly when the shared cell x(r) = y(r) is black. For a
> single agreeing cell (r = a, both neighbours disagreeing) they agree one step later exactly when that cell is
> white.

**Proof.**
- *At a.* The left inputs differ and the other two agree. The rule is XOR in its left input, so the outputs differ.
- *Inside.* All three inputs agree, so the outputs agree.
- *At r.* The left and centre inputs agree and the right inputs differ. If the shared centre is black, the OR is 1 in
  both rows and the outputs agree; if it is white, the OR passes the difference on.
- *A single agreeing cell.* Both outer inputs differ. A white centre lets the two differences cancel; a black one
  stops the right difference, so only the left one counts. ∎ (G2: 409,620 intervals and 491,520 single cells, against
  20 backgrounds y.)

So **the left edge of any agreement moves right at exactly one cell per step, always.** Its right edge holds wherever
the shared boundary cell is black (the OR shields it) and retreats wherever it is white. This is the light cone together
with 8.66's damage front, which heals exactly where the undamaged diagonal is black.

**R is P twice.** Compare a black run with the all-black row: one step later the all-black row has become all white,
and the run's agreement keeps its right end (black) and loses its head, giving the tail 0^(m−1). Compare a white run
with the all-white row: it loses both ends (white), giving 1 0^(n−2) 1. The lone white cell is P's single-cell clause.

## 3. The map: every structure we found is R or P applied to a simple history

A **patch** of a history y is a stretch where the actual row agrees with y. Rule 30 has exactly three fixed rows: all
white, and the two phases of 0101..., the rain (R: only runs of length 1 map to themselves). Periodic histories
include the 12 period-3 rows (all found by G2's ring search).

| Structure | What it is | The rule that governs it | First recorded |
|---|---|---|---|
| White triangle | a patch of the all-white row | P: the left edge moves right, and the right edge (white) moves left, both at speed 1. A run of width n lasts ⌈n/2⌉ rows; an odd one's lone tip stays white one row longer (P's single-cell clause) | 8.18; GC1932 |
| A triangle's birth | the three parents of a white run | R read backwards: a wider white run, a black cap one cell wider, or a black run of the same width with a lone white cell at its right end; 1 : 1 : 2 under fair rows | L998 |
| Hanging | a lone white cell and the black run on its left | R: (black run of length m, lone white) becomes 1 0^m | L998; GC847 for m = 1 |
| Black flash | a black run lasts one step | R: only its head survives, so a column stays black exactly while its cell stays a head; its left neighbour is white the whole time | L999 (left companion); GC1934's bars |
| Black cap | a long black run | **Bridge law, new:** a black run of length L in the next row lies over exactly r copies of the word 100 with 3r+1 ≤ L ≤ 3r+4. A white pair is a *bridge*: R turns it wholly black, fusing the black runs on both sides. Long black runs, and the large triangles below them, exist only where bridges chain | GC1932, 8.82 (the 001 parents) |
| Rain | the fixed point 0101... | R: runs of length 1 are fixed | CL094, GC847 |
| Staircase | a patch of rain | P: its left edge, the front, moves at exactly speed 1 (the diagonal of bar bottoms). Its right edge holds on black, and GC1934's alternative refines this: it blinks (the clock) or steps | GC1934, L999; 8.66's "the checkerboard closes behind" |
| Triangles under a staircase | what the front leaves | R, hanging: one triangle per white bar, widths alternating 2 and ≥ 3 | L999 |
| Right edge | the end of the all-white patch on the right | **Edge law, new for every finite seed:** section 4 | 8.73 for the single seed |
| Left edge | the end of the all-white patch on the left | R: that run's last cell turns black every step, so the left edge moves at speed 1 | known |
| Finite injectivity | two finite rows never merge | P with the agreement [R, ∞): its left end R moves right for ever | G121, L997 |
| Damage spreading | agreement between a row and its edited copy | P | 8.66 |

**What the map says, in words.**
- *Every ordered patch, whatever its texture, has a perfectly straight left edge* running down to the right at 45°,
  because Rule 30 is XOR in its left input.
- *Its right edge is where all the variety lives.* It holds only where the patch's last cell is black. So all-white
  patches (triangles) always die on schedule, and patches with black cells along their right side (rain) can last.
- *Long-range combination happens only through bridges.* A long black run, and the big triangle it caps, require an
  aligned chain of white pairs (100100…) just above it.

Prediction for the eye: the core should also hold textured patches of the 12 period-3 rows, each with a straight
45° left edge. That is not yet looked for.

## 4. The edge law, for every finite seed

Let e_t be a finite pattern's rightmost black cell, and L_t the length of the black run ending there.

**Theorem E.** For every finite nonzero row:
1. *The edge advances one cell every step.*
2. *L alternates.* L_(t+1) = 1 when L_t ≥ 2, and L_(t+1) ≥ 2 when L_t = 1.
3. *A triangle every two steps.* When L_t ≥ 2, the next row has a white run of width exactly L_t − 1 just left of the
   edge cell.
4. *The rhythm.* Consecutive emitted widths w → w′ obey 1 → 1, ≥ 3 → 2 and 2 → ≥ 3.
5. *One bit decides the type for ever.* Let c1 and c2 be the two cells left of the rightmost black cell at time 0.
   - If c1 = c2 (the seed ends …001 or …111), no emission ever has width 1, and the widths alternate between exactly 2
     and at least 3: a **half-ruler**.
   - If c1 ≠ c2 (…011 or …101), every emission has width 1: a **rain edge**.

**Proof.**
- *Items 1 to 3.* By R the white run beyond the edge has its first cell turned black, so e_(t+1) = e_t + 1. The edge
  black run becomes 1 0^(L_t − 1). If L_t ≥ 2, cell e_t turns white, so L_(t+1) = 1, and the white run left of the new
  edge is the tail, of width L_t − 1, bounded by the head. If L_t = 1, cells e_t and e_t + 1 are both black.
- *Item 4.* Take a time with L_t = 1, just after an emission of width w. The run left of the edge cell is that white
  run. By R:
  - w = 1: it stays white, so L_(t+1) = 2 and the next width is 1;
  - w ≥ 3: its last cell turns black and the one before stays white, so L_(t+1) = 3 and the next width is 2;
  - w = 2: it turns wholly black (a bridge) and fuses with what lies beyond, so L_(t+1) ≥ 4 and the next width is
    at least 3.
- *Item 5.* Item 4 never leads into 1 from a width of 2 or more. So it is enough that the first emission has width 1
  exactly when c1 ≠ c2:
  - …111: the first width is L_0 − 1 ≥ 2;
  - …011: the first width is 1;
  - …001: L_1 ≥ 3, so the first width is at least 2;
  - …101: L_1 = 2, so the first width is 1. ∎

**Checks.**
- G5 and G5b: all 4,095 seeds of width up to 12, over 300 steps; 2,048 half-rulers and 2,047 rain edges, each as
  predicted.
- G6: the single seed is a half-ruler. Its widths are 8.73's ruler 2, 3, 2, 5, 2, 3, 2, 6, …, matching w(v) exactly
  for v = 1 to 12.

**What it says.** The owner's ruler has a first level that is universal. Every finite seed whose last three cells read
001 or 111 has an edge that emits a triangle of width exactly 2 every four steps, with a wider one between. The deeper
levels of the single seed's ruler (3 between the 2s, then 5, …) come from 8.73's diagonal periods and are not claimed
here for other seeds.
- *A known fact behind this.* The strip within distance d of the right edge is autonomous: a cell at distance d
  depends only on distances d−2 to d one step earlier. So each level is eventually periodic (G249).
- *The open part.* A general law for the deeper levels needs that strip's structure, not a census of seeds.

## 5. Two counting laws (rings, every state)

From R:
- **Black cells next step** = (black runs now) + 2 × (white runs of length ≥ 2 now).
- **Change in the number of black runs** = (black runs of length ≥ 2 followed by a white run of length ≥ 3) minus
  (lone black cells followed by a white pair, the word 100). This counts heads, so an all-black ring counts as none.

Guard G4 checked both on 131,030 rings.

## 6. What this does and does not do

- *It answers every state.* R and P are exact for every row. They replace the case-by-case lemmas of L998, L999 and
  GC1934 with two rules, and they explain why the ordered structures look the way they do.
- *It does not prove a prize statement.* In R's terms, the centre is black next step exactly when it is a head or the
  end of a white run longer than one. That is a restatement, not a proof of non-periodicity.
- *The value is the map.* Each ordered region is a patch of a simple history, with a light-speed left side and a
  black-shielded right side. The only long-range combining step is the bridge.

## 7. Where the warm pulls point next

1. **Bridges.** Every large black run, and every large triangle, needs a chain of 100s above it. Where do bridge
   chains come from? By R a white pair is born from (black run of length 3, white of length ≥ 2), as a shrinking white
   run of length 4, or by hanging (black run of length 2, lone white). A bridge chain is a row of such births in step.
   Is there a general rule for when they align?
2. **Patch lifetimes.** For an all-white patch the lifetime is exact: ⌈n/2⌉. For a rain patch the right edge can grow.
   Is there an exact, deterministic statement of when it grows, beyond GC1934's one step?
3. **Period-3 patches.** Look for them in the single seed's core, checking only P's prediction (the straight left
   edge) and their lifetimes. That is a small, targeted look, not a census.
4. **The second level of the edge.** Is there a general rule like item 4 for the widths of 3 or more, for every
   half-ruler seed?
