# The limb: predictions, written before each run (2026-09-27)

## What was found before these (limblevels.py, no predictions were at stake)

- **K1** is a textured limb sweeping a still textured wall at 12 -> 60 px/frame. The recommendation's coarse search
  (1/16) reads it at gain 0.26 at 18-24 px/frame, the fresh 1/8 search at 0.67, and 1/8 after propagation at 0.29.
  The final field reads 0.35; past 24 it reads 0.
- **K2** is the same limb over a flat dark wall: the final field holds 0.91-1.04 to 36.
- **K3** is K1 with the limb's mean brightness raised: the coarse search holds 0.87 / 0.73 at 18-30, and the final
  field 1.03 / 0.94 / 0.91 to 36.
- **Two mechanisms.**
  - (1) The coarse level is POINT-SAMPLED: one bilinear tap per 16 x 16 footprint. A fine grain moving by anything
    but a multiple of 16 px is sampled at different grain cells in A and B, so the limb's coarse picture scrambles.
    Meanwhile the still wall's taps match exactly at zero.
  - (2) The 1/8 propagation is a contrast-weighted mean. A textured still background's zeros outvote a small moving
    object's flow.

## EDGE_PROP (mechanism 2): the neighbour weight times the flow's agreement, by the texel's own confidence

Prototyped at TAU 0.25 / 0.5 / 1.0 on the limb (5 runs each).
- **K1:** +1.07 dB at 18-24 px/frame and +0.46 at 24-30 (TAU 1.0); nothing beyond 30, where the coarse level has
  already lost the limb.
- **K2:** -0.4 at 18-30, +0.25 to +0.5 above 30.
- **K3:** the 1/8 level keeps 0.61 / 0.50 at 36-48 (shipped: 0.29 / 0.14).

Predictions for the full-ladder gate (best-of-3), written before it ran:
- **G1.** The capped-at-40 mean within +-0.1 dB of the control. The switch touches only texels whose confident
  neighbours move differently.
- **G2.** No case down more than 0.5 dB, except possibly the aperture series (P1-P3). Its fill relies on neighbours
  whose flow differs from a texel's unconstrained own, and the confidence blend should protect it.
- **G3.** The moving-object-over-texture cases (L9 occlusion, E-series) up by 0.2 dB or more.

**Scored (2026-09-27, 17:39): REFUTED.**
- G1: the capped mean fell 0.36 dB, not within 0.1.
- G2: 21 cases down, the period family by 5-12 dB (H1 and V1 -11.6, H2 and V2 -5.8, R3 -4.6, A5 -4.0; A4, A6, A7,
  O5, O6, L1 and M2 by 0.8-2.4).
- G3: L9 fell 0.27. The movers that rose were L3 +0.83, L4 +1.79, A2 +0.34, A3 +0.47, F1 +0.44, M1 +0.58, P1 +1.07.
- **The mechanism.** In the period cases a texel's raw match is confidently wrong, and the propagation's mean
  across disagreeing neighbours is what carries the right basin over it. The agreement weight protects exactly
  the confident, disagreeing texel: right at a motion edge, fatal at an alias.
- **Status.** Kept in gen_variational.py as the design record; it ships nothing.

## The coarse texture-energy channel (mechanism 1): a second channel beside the point-sampled luma

It is the footprint's mean 2-px gradient magnitude on a 4 x 4 grid of taps. The coarse SAD becomes
|dL| + W |dE|, and nothing else reads the channel (energyvariant.py). It is NOT section 8's prefilter, which
REPLACED the taps with a box average and destroyed the load-bearing aliased contrast. Predictions, written before
any run:
- **E1.** On K1 the coarse level holds the limb at 18-30 px/frame (S gain 0.7 or more, near K3's 0.87 / 0.73), and
  the final picture in the limb box rises by 2 dB or more at 18-30.
- **E2.** K2 and K3 are not worse by more than 0.3 dB in any band.
- **E3.** On the ladder:
  - L0_static is unchanged (+-0.05 dB): a still frame's energy is still.
  - The integer-speed fine-texture cases (M1, L2 at 16 px/frame) are unchanged (+-0.3): the luma term still wins
    where the Moire is shift-invariant.
  - The flat cases (L6, L5) are unchanged: there is no energy there.
- **E4 (the risk).** Where energy is uniform (a uniformly textured moving field) the term is a constant and harmless.
  Where energy has its own structure at a period near the coarse texel, it can alias like the luma did. If a case
  falls, look there first.

**Scored (2026-09-27, 18:00).**
- E1, the coarse level holds the limb (0.7 or more at 18-30 px/frame on K1) and the picture rises 2 dB or more:
  REFUTED as stated. At 18-24 the coarse gain goes 0.26 -> 0.44 / 0.60 / 0.64 / 0.72 at W 1 / 2 / 4 / 8, and at 24-30
  only to 0.18-0.44. The final field on K1 barely moves: the 1/8 level aliases the same grain, and propagation
  dilutes it (the mechanisms stack).
- E2, K2 and K3 not worse by more than 0.3: MET. K2's reach extends: 0.87 at 36-42 and 0.69-0.73 at 42-48 px/frame,
  against the committed 0.52 and 0.15.
- E3, the ladder:
  - L0_static unchanged: MET (+0.01; -0.17 at W 8).
  - M1 and L2 unchanged: M1 +0.6 (up); L2 -0.52 / +0.17.
  - L6 and L5 unchanged: within 0.35.
- E4, the risk, where energy has structure near the coarse texel: CONFIRMED. The period family fell 2-7 dB (V1 and
  H1 -2.1 to -2.3, V3 -6.8 at W 8).
- Capped mean -0.11 / -0.12. Real footage level to slightly positive at W 8.
- **A TRADE: kept as the prototype, not generated.**

## B1: the half-period alias where the frame cannot anchor it (written 2026-09-27, 21:50, before any run)

V3's patch over the aperiodic noise panning left at 8 px/frame (scenes.sh `B1_alias_over_pan`). On V3 the global-motion
seed alone holds the basin at every start (27.0 phase-averaged against the recommendation's 22.4), because its
frame-wide cost sum is the patch's own. Here the frame's dominant motion is the background's, and the patch's two
aliases (+12 and -12, down and up) are equidistant from it. v3phase.sh, six starts x three runs, whole-frame PSNR.
- **B1.1.** The cage and the global seed alone LOSE V3's stability here. Both are phase-fragile (a spread over starts
  of 3 dB or more), and both phase-average within 2 dB of the recommendation's own B1.
- **B1.2.** The recommendation is phase-fragile here as on V3 (spread 3 dB or more).
- **B1.3.** COARSE_ENERGY on the cage costs B1 more than the -1.2 it costs V3.
If B1.1 fails (the cage holds B1 too), the global seed is not the whole mechanism, and the leap's target needs
re-finding before any GLSL is written.
- **Instrument note (22:05, before any valid reading).** The first B1 panned the fine 4-px noise. Its frames differ by a
  mean 0.33, over the scene-cut gate's 0.125, so every shader held frames: 10.18 dB, identical to the hundredth. That
  reading is void. B1 was rebuilt: a smooth background (cut statistic 0.09) and a 200-px patch, so that the frame-wide
  cost sum is lowest at the BACKGROUND's motion (0.045 against 0.068 at the patch's). The predictions above stand as
  written.

**Scored (22:35).**
- **B1.1 (the cage and the global seed lose the stability and fall within 2 dB of the recommendation): refuted as
  written for the downward patch, confirmed and exceeded for the upward one.**
  - Down: the cage reads 24.4 and the global seed 24.6, against the recommendation's 21.3, with spreads under 3 dB.
  - Up: the cage reads 20.6 and the global seed 20.5, against the recommendation's 23.0.
  - The mechanism is not the one assumed. The frame's shift on B1 is (+24, +24) px, a probable coarse-level Moire of
    the background, and it biases every alias toward "down".
- **B1.2 (the recommendation phase-fragile, spread 3 dB or more): refuted.** The spread is 2.6 down and 4.2 up, with
  no bimodality.
- **B1.3 (energy costs the cage more than on V3): refuted for the downward patch.** The cage with energy reads 26.4
  against the cage's 24.4. The upward patch was not run with it.
- The clause "if B1.1 fails, re-find the leap's target before any GLSL" was honoured. Re-found: the target stands, a
  local carry. And a new target joins it, the global prior deciding local ties.

## The alias prior and carry in the shader (written 2026-09-28, 06:00, before the chain's first reading)

`ALIAS_PRIOR=1` (on the cage) and `ALIAS_CARRY=1` (on the cage with the prior, and on the bare recommendation);
tests/alias_carry.py. Measured by alias-chain.sh:
- V3 and B1, each both ways (v3phase.sh, six starts x three runs);
- the full ladder, three runs;
- real footage;
- the Mac clock.

A smoke run found the first carry build choosing V3's ALIAS across the cage's interior. h1 was scored between texels
and h2 on the lattice, a coherent faint preference. Scoring both on the lattice fixed it: V3's flipped start is right
from frame 2 on both bases. The predictions:
- **A1, the prior alone (the cage with the prior, against the cage).**
  - V3 down and up: unchanged within 1 dB (the frame's shift IS one of V3's basins).
  - B1 up: rises to within 1 dB of the recommendation's 23.0.
  - B1 down: falls from 24.4 toward the recommendation's 21.3.
  - B1's two directions end within 1.5 dB of each other: the coincidence removed, nothing yet put in its place.
- **A2, the carry.**
  - The recommendation with the carry: V3 phase-averaged 26 or more, both ways (the recommendation reads 22.9 down,
    about 20 up).
  - The cage with prior and carry: V3 not below the cage's 27.4.
  - B1, both bases: 25 or more both ways, the two directions within 1 dB of each other.
- **A3, the ladder.**
  - Each carry against its own base: every non-periodic case within 0.3 dB.
  - The periodic cases (V1-V3, H1-H2, P1-P5, L7, M2, M3) up or level.
- **A4, real footage.** Each carry within 0.05 dB PSNR of its base on all four clips (offline it changed 0.02-1.9% of
  cells).
- **A5, time.** The carry costs at most 10% on the cage at 720p. The scan passes run one invocation per line (four per
  line), latency-bound: the risk is here.
- **Build history (06:40), before the full chain's reading.** The carry was revised twice after its first V3 readings.
  So A2's V3 and B1 figures are **no longer blind**; A3 (the ladder), A4 (real footage) and A5 (time) still are.
  - **Build 1** carried the level's own flow as the first hypothesis. V3 down: the recommendation 22.7 -> 27.4, but
    the cage 27.5 -> 24.5. V3 up: 19.5 -> 21.9 and 28.4 -> 22.3. The cage's B->A flipped to the alias every fourth
    frame. The cause: cells at the patch's SIDES, where the level's flow is junk, anchored on it along every row.
  - **Build 2** made such cells breakers. The cage recovered moving down, but moving up both stayed short
    (21.2 / 26.0): the decisive END's cells also had junk flow, and as breakers their evidence was lost.
  - **Build 3** carries each cell's OWN two basins (the 1/8 curve's best and rival, both refined at the quarter
    level) and maps the chosen basin back to the level's flow only for output. On the quick sweep (six starts in 8-px
    steps x three runs), V3 reads 29.1-29.3 both ways on both bases (every start 28.3-29.5). B1 down reads 24.9 / 25.1
    (the recommendation 21.6); B1 up reads 22.4 on both, level with the recommendation. Offline, B1 up also loses
    cells to the carry (winner-takes-all 83-95% by its lucky tie-break, the carry 66-93%): B1's ends sit against a
    background moving differently, and cells straddling that edge make mixed anchors -- the ownership rule the survey
    names (a boundary votes only if it moves with the pattern), not yet built.
- **Build 4 (07:15), still before any full ladder reading.** Build 3's first ladder run (one run of three, then
  stopped):
  - The carry against the recommendation: L7 +23, P5 +16, V3 +2.9 / V1 and H1 about -21 (55 -> 34 dB), P1 -9,
    R3 -7.6, P4 -3.8, P3 -2.9.
  - V1's field showed why. Build 3 REPLACED the level's flow whenever it lay outside the chosen basin, including in
    untied cells whose margin the scans outvoted. Near a pattern's ends a cell's 1/8-level basins can both be wrong,
    so right flows were overwritten.
  - Build 4 only SWITCHES ALIASES: in a TIED cell (both data costs exactly 0) whose own flow lies in one of its two
    basins, the flow may move to the other. Everywhere else the level's flow stands.
  - A quick single run on the moved cases: V3 26.5 -> 29.5, V1 +2.1, H1 +0.7, M2 +0.9, M3 +1.0, P3 +0.9, P5 +0.4,
    P4 +0.1, L7 -0.04 (build 3's +23 came from overriding untied cells), P1 -0.5, R3 -0.75.
  - The ladder predictions (A3) stay as written and are now scored against build 4.

**Scored against build 4 (09:00; alias-chain.sh: v3phase six starts x three runs, the ladder three runs, real.sh,
timing.sh).** vp = the recommendation, vpc = + carry, cage, cprior = cage + prior, ccarry = cage + prior + carry.

    phase-averaged        vp     vpc    cage   cprior  ccarry
    V3 down             22.6   28.6    27.6    27.2    28.7
    V3 up               19.7   28.0    28.3    28.5    28.6
    B1 down             21.4   24.2    24.5    23.1    25.3
    B1 up               23.0   22.4    20.6    21.3    21.8

- **A1, the prior alone. Partly met.**
  - V3 unchanged within 1 dB: MET (27.6 -> 27.2 down, 28.3 -> 28.5 up).
  - B1 up to within 1 dB of the recommendation's 23.0: NOT MET (21.3; the coincidence is gone, but the frame's
    Moire still costs the cage elsewhere).
  - B1 down falls toward 21.3: MET (24.5 -> 23.1).
  - The two directions within 1.5 dB: MET (23.1 / 21.3).
- **A2, the carry. Met on V3, partly on B1.**
  - The recommendation's V3 at 26 or more both ways: MET (28.6 / 28.0).
  - The cage's V3 not below 27.4: MET (28.7 / 28.6).
  - B1 at 25 or more both ways, the directions within 1 dB: NOT MET (vpc 24.2 / 22.4, ccarry 25.3 / 21.8). B1's
    ends face a background moving otherwise: the ownership rule, unbuilt.
- **A3, the ladder, blind. Met on the cage, refuted on the bare recommendation.**
  - ccarry against the cage: capped +0.09, 14 up and 1 down (P5 -0.47, at 43 dB). No non-periodic case falls 0.3.
  - vpc against vp: capped +0.14, but 13 cases down 0.3-0.8 (F2 -0.80, P3 -0.76, R3 -0.74, M2 -0.62, P1 -0.61,
    F1 -0.50 and seven smaller), part of it the Mac's wander. On the bare recommendation the carry is a TRADE.
- **A4, real footage, blind. Refuted in both directions.**
  - vpc: street +0.01, avengers +0.12, bttf +0.28, bluey -0.05, a gain on the films.
  - ccarry against the cage: 0, -0.06, -0.15, 0 in PSNR. SSIM is level (-0.0006 to +0.0003).
- **A5, time, blind. Met on the cage.**
  - ccarry +4.9% over the cage (+5.5% over cprior) at 720p.
  - vpc +15.4% over vp.
  - A noisy session: the cage alone read x1.17 of vp, where it read x1.09 the night before.

## Build 5, the aperture rule, and the energy combination (written 2026-09-28, 09:20, before their readings)

ownerdump.py read the carry's inputs cell by cell on B1 moving up (the cage + prior + carry, frame 8). At the patch's
ends, and in the interior within reach of them, the RIGHT alias's hypothesis carries a junk horizontal component: inside
horizontal stripes x is unmeasurable, and the background in the window pulls it. The wrong alias maps the background
onto x-free bars and keeps x = 0. The carry's penalty compared whole vectors, so the right chain paid P2 at every junk
step: the top end voted the wrong way, the bottom end the right way, and the interior split in half. Moving down the
same bias was hidden: the 1/8 level already held "down" there.

The rule (apcarry.py offline, then alias_carry.py build 5): the penalty and the pick ignore a step's component along
the cell's stripes (the structure tensor's minor axis, weighted by coherence; the more coherent of two cells decides),
and a switched flow keeps the level's own component along them. Offline: B1 up 83% -> 99%, B1 down 95% -> 100%, M3
58% -> 61%, V3 and the period family unchanged, real footage 0.02-1.82% of cells changed (build 4's rule 0.05-1.86%).

Two of B1 up's six starts were read (the first build-5 chain) before this was written; everything else is blind.
- **B5.1, B1 up.** The cage + prior + carry at or above the recommendation's 23.0, phase-averaged (build 4: 21.8).
  Not blind: starts 100 and 104 read 23.6 and 23.9.
- **B5.2, B1 down.** Not below build 4's 25.3 by more than 0.3.
- **B5.3, V3 both ways.** Within 0.5 dB of build 4 (28.7 down, 28.6 up), on the cage and on the recommendation.
- **B5.4, the ladder** (three runs, the cage the control).
  - The cage + prior + carry: capped not below +0.05. No non-periodic case down 0.3. Build 4's single loser (P5 -0.47)
    no worse.
  - The same with the energy channel against the cage + energy: the same bars.
- **B5.5, real footage.** Each carry within 0.05 dB PSNR of build 4's reading on its base.
- **B5.6, time.** Build 5 within 2% of build 4 (a 7 x 7 tensor per quarter cell, both directions).
- **B5.7, the energy combination** (cage + energy + prior + carry, against the cage + energy). V3 phase-averaged 28 or
  more both ways (the cage + energy reads 26.2 down), because the carry re-derives V3 every frame whatever the coarse
  seed says; B1 at 23 or more both ways.

**Build 5 scored (10:45; b5-chain.sh, gate5-chain.sh: v3phase six starts x three runs, the ladder three runs with the
cage the control, real.sh, timing.sh).**
- **B5.1, B1 up: MET.** 23.7 (build 4 21.8; the recommendation 22.8 this session).
- **B5.2, B1 down: MET.** 27.0 (build 4 25.3).
- **B5.3, V3: MET.** The cage's carry 28.6 / 28.6 (build 4 28.3 / 28.6); the recommendation's 27.8 / 28.5 (28.0 / 28.6).
- **B5.4, the ladder: REFUTED.**
  - The cage's carry is capped +0.08 against the cage, 9 up / 5 down. P5 is no worse (-0.01). But four
    non-periodic cases fall: A6 -1.21, A7 -0.65, O5 -0.58, R1 -0.32. A6 and O5 hold these to the hundredth over the
    three runs (A6 49.14 / 48.88 / 49.11 against the cage's 50.26 / 50.26 / 50.24).
  - With energy against the cage + energy: capped +0.11, 12 up / 5 down (A6 -1.35, O5 -0.78, O2 -0.42, F1 -0.33,
    A7 -0.31).
  - **The cause** (cases.sh, the rule switched off, then in the scans only, then with a strict coherence): A6, A7 and
    O5 carry the ladder's M2 texture, sin x sin y with a 40-px period. The tensor's 20-px window is half a period,
    which near the texture's zero lines reads as stripes, so the rule threw away a component those cells could
    measure. The strict threshold and the scans-only form both kept the loss. Part of A6's loss (about 0.8, not
    stable run to run) belongs to the carry itself, with or without the rule.
- **B5.5, real footage within 0.05 dB of build 4: REFUTED, both ways.** avengers +0.20, bttf -0.10, street and the
  cartoon within 0.01. A single run each; the films' middle segments move 0.3-1.2 dB between shaders of this family.
- **B5.6, time: MET.** +0.8% over build 4 (x1.239 against x1.229 of the recommendation).
- **B5.7, the energy combination: MET.** V3 29.1 / 29.1, B1 27.4 / 24.5; the best of every shader measured on all
  four readings.

## Build 6: the tensor over 40 px (written 11:05, before its gate)

Build 6 reads the structure tensor over the 1/8 level's 5 x 5 window (40 px, one period of M2's texture), not the
quarter level's (20 px). Seen before this was written (cases.sh, two runs each, one start): A6 50.29, A7 49.53, O5
42.58, M2 53.51 (the cage + energy 50.47, 49.13, 42.55, 53.06); B1 up 24.46, down 27.32; V3 29.46 / 29.27. Blind:
- **B6.1, the ladder.** The cage + energy + prior + carry against the cage + energy: capped +0.05 or more, and no
  non-periodic case down more than 0.3 except A6 (the carry's own, up to 0.8). The cage + prior + carry against the
  cage: the same bars.
- **B6.2, V3 and B1, phase-averaged.** Within 0.5 dB of build 5 on both bases (the cage's: V3 28.6 / 28.6, B1 27.0 /
  23.7; with energy: V3 29.1 / 29.1, B1 27.4 / 24.5).
- **B6.3, real footage.** Each carry within 0.15 dB of its own base on every clip.
- **B6.4, time.** Within 2% of build 5.

**Build 6 scored (12:07; gate6-chain.sh).**
- **B6.1, the ladder: MET on the means and on the M2 cases; three non-periodic cases 0.32-0.35 below.**
  - The cage + energy + prior + carry against the cage + energy: capped +0.08, 9 up / 6 down. The M2 cases are
    back: A6 -0.16, O5 +0.04, A7 +0.54. Down: P2 -0.63, H1 -0.61, P3 -0.58 (periodic, all above 54 dB), and L3 -0.35,
    A1 -0.32, A3 -0.32 (at the Mac's run-to-run level; not in build 5's list).
  - Against the cage, the player's default until today: capped +0.17, 26 up / 3 down (H1 -1.61, V1 -0.47 at 55 dB,
    L0 -0.48 at 79 dB).
  - The cage + prior + carry against the cage: capped +0.07, 11 up / 4 down (M1 -0.62, M2 -0.51, L0 -0.49, L5
    -0.33).
- **B6.2, V3 and B1: MET.** The cage's carry V3 28.7 / 28.6, B1 26.9 / 23.6; with energy V3 29.1 / 29.2, B1 27.4 /
  24.4 (build 5: 28.6 / 28.6, 27.0 / 23.7; 29.1 / 29.1, 27.4 / 24.5).
- **B6.3, real footage: MET.** With energy against the cage + energy: street +0.03, avengers +0.10, bttf 0.00, the
  cartoon -0.07. The cage's carry against the cage: -0.01, +0.08, -0.10, +0.08.
- **B6.4, time: MET.** -0.6% and -0.2% against build 5. The combination is x1.29 of the recommendation, +20% over the
  cage, +12% over the cage + energy.

2026-10-01: alias-chain.sh, b5-chain.sh, gate5-chain.sh and gate6-chain.sh, cited above as the runs behind the build
4, 5 and 6 scores, were not committed and are not in this repository. Each citation lists the steps its wrapper ran;
the drivers named there (v3phase.sh, real.sh, timing.sh) are in this folder.
