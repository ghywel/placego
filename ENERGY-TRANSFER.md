# Transfer of kinetic energy: inferring what the field cannot see

Opened 2026-09-30 from the owner's question. A Newton's cradle moves its two end balls while the middle ones stay
still, yet the energy has passed through them. Can we infer kinetic energy that we cannot detect? What does that
mean further afield, from astrophysics to quantum mechanics? And how do we detect it?

> **Status (2026-10-01).** Opened on 2026-09-30 as five investigations parked for spare compute. All five were run
> that day as far as they go without a camera; the results follow each investigation. Still owed: the camera steps
> (the real throw, pendulum and bounce; a pool table; real collisions; the cradle rig and its sound) and the app-side
> steps of investigation 4 (4.3-4.5). The prior art is in
> [PRIOR-ART.md, "Before the energy-transfer investigations"](PRIOR-ART.md#before-the-energy-transfer-investigations-surveyed-2026-09-30); what it changed is
> ["What the survey changed"](#what-the-survey-changed-2026-09-30). From ["The shared stage"](#the-shared-stage-finding-the-region-one-motion-governs-begun-2026-09-30-late-night) on, this document records the
> interpolation leads the investigations produced, numbered as in ["Suggested order"](#suggested-order-cheapest-and-readiest-first):
> - lead 1, the slow-print outline prior (`OUTLINE_ADOPT`): in the Cadence player since 2026-10-01;
> - lead 2, the impact mode as a shader: parked for the player on 2026-10-01, nothing built;
> - lead 3, the rigid-region repair (2.5 to 2.5e): parked;
> - lead 4, listed first as the per-level trust gate for fast prints, then used for the fast fine-print fix: built as
>   `PRINT_LATTICE` with a cost cap, now the Cadence player's default (High) quality tier; the trust gate itself is
>   parked and has never been built.
>
> Which shader each player tier uses: [SHADERS.md, "Which one to use"](SHADERS.md#which-one-to-use). Related records:
> [NFRAME-LIMITS.md](NFRAME-LIMITS.md) ("The weave", where leads 1 and 4 were found);
> [MOLTENVK-NONDETERMINISM-INVESTIGATED.md](MOLTENVK-NONDETERMINISM-INVESTIGATED.md) (the Mac wander noted in 1.1 and 1.4); [THREEDIMENSIONAL.md](THREEDIMENSIONAL.md) (what a 2D field
> says about motion in depth). Paths under `np-scratch/`, and the Cadence tree's CADENCE.md, are private working files,
> not part of this repository.
>
> *Originally:* **Status: parked until there is compute to spare.** Nothing here is built yet. Five investigations follow, each with
> its own next steps, the prior art to survey before designing anything (the literature-first rule), what it costs, what
> it would buy the project, and its traps. The suggested order is at the end.

**Contents**

- [The short answer, kept for reference](#the-short-answer-kept-for-reference)
- [1. Conservation laws as free truth on real footage](#1-conservation-laws-as-free-truth-on-real-footage) (results 1.1, then 1.5 and 1.4 in simulation)
- [2. Hidden spin: the energy a centre tracker misses](#2-hidden-spin-the-energy-a-centre-tracker-misses) (2.1-2.3; 2.5-2.5d, the rigid region; the 2.4 pre-registration, whose [results](#results-24-in-simulation-the-pool-shot-2026-09-30-the-reading-on-the-arc) sit under 3)
- [3. Impacts: where the impact falls inside the frame, and "teleported momentum"](#3-impacts-where-the-impact-falls-inside-the-frame-and-teleported-momentum) (3.1-3.6c)
- [4. The held ball: bodies that are coupled share their acceleration](#4-the-held-ball-bodies-that-are-coupled-share-their-acceleration)
- [5. Seeing the cradle's middle](#5-seeing-the-cradles-middle) (5.1-5.2c)
- [What the survey changed (2026-09-30)](#what-the-survey-changed-2026-09-30)
- [The warm lead: the impact placer as a shader](#the-warm-lead-the-impact-placer-as-a-shader-recorded-2026-09-30-the-owners-call-after-the-science-explorations)
- [Suggested order (cheapest and readiest first)](#suggested-order-cheapest-and-readiest-first)
- [The shared stage: finding the region one motion governs](#the-shared-stage-finding-the-region-one-motion-governs-begun-2026-09-30-late-night)
  - [Stage 0a-0f: the instrument, and why the default's own carry does not fix the weave](#pre-registered-stage-0a-the-instrument-before-it-ran)
  - [The specification has a name: the survey's unwrapping form](#the-specification-has-a-name-the-surveys-unwrapping-form-2026-09-30-late-night), then stage 1a and [STAGE v1, frozen](#stage-1a-concluded-the-taxonomy-the-refine-and-stage-v1-frozen)
  - [Stage 1b: the GPU-shaped stand-ins](#pre-registered-stage-1b-the-gpu-shaped-stand-ins-offline-before-it-ran)
  - [Stage 1c: the GLSL form](#stage-1c-first-the-insertion-point-and-one-simplification-offline), [complete: OUTLINE_ADOPT](#results-stage-1c-complete-outline_adopt-identical-and-affordable), [no harm on real footage](#results-stage-1c-no-harm-on-real-footage-the-nass-arc)
  - [2.5e: lead 3's selection rule, and the lead parked](#results-25e-lead-3s-selection-rule-the-m5-r1-and-r2-missed-the-lead-is-parked-with-its-reason)
  - [Lead 4 on a rotating print, and steps 1d-1g](#pre-registered-lead-4s-re-score-on-a-rotating-print-before-it-ran)
  - [OUTLINE_ADOPT adopted for the player (2026-10-01)](#outline_adopt-adopted-for-the-player-2026-10-01-the-4k-twin-and-the-metal-port)
  - [Lead 4, steps 1h-1l and 1k2](#pre-registered-lead-4s-step-1h-the-lattice-from-the-18-levels-rival-basins-route-1-before-it-ran)
  - [Lead 4, the GLSL form (PRINT_LATTICE) and its gates](#the-glsl-form-built-testsprint_latticepy-print_lattice1-and-a-second-instrument-fault-found-by-g1)
  - [Lead 4, step 1r and the cost cuts](#pre-registered-lead-4s-step-1r-a-lattice-vector-must-be-an-isolated-minimum-before-it-ran)
  - [Fusion, and the fused form's gates](#results-fewer-passes-then-fusion-one-pass-carries-both-directions-identical-output-throughout)
  - [The owner's two decisions (2026-10-01), and the tiers' costs](#the-owners-two-decisions-2026-10-01-morning-and-the-tiers-costs)
  - [The lattice's cost cap](#pre-registered-the-lattices-cost-cap-the-owners-go-2026-10-01-before-it-ran)
  - [The per-level trust gate, parked](#parked-by-the-owner-2026-10-01-morning-the-per-level-trust-gate-to-return-to-within-hours)
  - [The per-level trust gate, returned to: the cut gate found, the gate built](#the-per-level-trust-gate-returned-to-2026-10-01-afternoon-t0-the-diagnosis-before-the-build), and [where it stands](#where-the-per-level-trust-gate-stands-2026-10-01-evening)
- [Sources](#sources)

## The short answer, kept for reference

**The middle balls do move, only too little and too fast to see.** Worked by Hertz contact theory for two steel
balls of 25 mm diameter meeting at 1 m/s (E = 200 GPa, Poisson 0.3):

    contact time      t ~ 2.87 (m*^2 / (R* E*^2 v))^(1/5)  ~ 77 us
    peak compression  d ~ (15 m* v^2 / (16 E* sqrt(R*)))^(2/5)  ~ 26 um

- **Time.** The pulse crosses a five-ball chain in well under a millisecond, which is a small fraction of one frame at
  60 fps (16.7 ms). Even 240 fps slow motion (4.2 ms) is about fifty contact times long.
- **Distance.** Each middle ball is pushed forward a few tens of micrometres and stops. On a phone filming a 15 cm
  cradle at 1080p, a pixel is about 80 um, so the step is roughly a third of a pixel.
- **Stored energy.** Part of the energy in flight is not kinetic at all: it is strain in the squashed contacts, with
  no motion. No motion field can see that part directly.

So the energy is undetected, not undetectable. It is below the camera's resolution in time and in space, which is the
N-frame line's own limit: motion faster than the frame rate. The pulse is a solitary wave in a chain of Hertzian
contacts (Nesterenko). Herrmann and Seitz explain the one-in, one-out behaviour: the first collision is slightly
dispersive, and the gaps it opens make every later one dispersion-free. A real cradle ends with every ball swinging
together for two reasons (Hutzler et al.): the line breaks up at the first collision because the balls respond
elastically over a finite time, and viscoelastic losses in the impacts then damp the balls' motion relative to
each other. (CORRECTED 2026-09-30 by the citation check: the first version said energy 'leaks' into the middle
balls and builds until visible, which is not the paper's explanation. The rocking is energy LOST, not a hidden
transfer accumulating.)

**What each of the field's channels sees**, once multiplied by mass:

    channel        physical quantity                     what it reveals
    velocity       momentum, kinetic energy              what moves
    acceleration   force (F = m a) = -grad(potential)    stored energy and invisible sources (a string, gravity)
    jerk           rate of change of force ("yank")      couplings switching on or off: contacts, impacts, clicks

A pendulum at the top of its swing has zero velocity, but its energy is in its height, and acceleration is at its
largest there. The field sees hidden energy through its force, never through its motion.

**How science infers the invisible**, three methods, all working from the boundary:

1. **Count at the ends.** Pauli's neutrino (1930, from energy missing in beta decay; detected 1956). The LHC's
   missing transverse momentum: sum everything visible, and the imbalance is the invisible particle.
2. **A strange motion means hidden mass or a wrong law.** Neptune (1846, from Uranus's drift) against "Vulcan"
   (Mercury's drift, which was general relativity, not a planet). Dark matter against modified gravity is the same
   fork today; the Bullet Cluster (Clowe et al. 2006), a collision of two galaxy clusters that separated the gas from
   the mass, is the strongest evidence. Collisions sort things by how they interact.
3. **Add up over time until it shows.** Pulsar timing took fifteen years of pulses from 67 pulsars to find EVIDENCE
   (about 3-4 sigma, not yet a detection) for the gravitational-wave background (NANOGrav, 2023).

**Further afield**, in one paragraph each (the conversation of 2026-09-30 has the long form):

- *Dark matter:* a velocity field turned into a mass map. Galaxy rotation too fast for the visible mass (Rubin);
  v^2 / r = G M / r^2 gives the hidden mass.
- *Dark energy:* inferred from the expansion's ACCELERATION (the 1998 supernovae). Cosmography expands the scale factor
  in exactly our channels: the Hubble rate, the deceleration parameter, the jerk parameter j. A pure cosmological
  constant gives j = 1 exactly in the flat model (it follows from Visser 2004's equations; Sahni et al. 2003 state it
  directly, as the statefinder r), so the cosmic jerk tests what dark energy is. DESI leans towards dark energy
  weakening: 2.5-3.9 sigma in its first release (2024), 2.8-4.2 sigma in its second (2025; 3.1 for BAO with the
  CMB alone), and a later recalibration of the DES supernovae lowered the top figure to about 3.2. Measured model-free, j0
  itself is consistent with 1 on DESI DR2 alone, and 3.4-5.4 sigma away from it once the supernova catalogues are
  added (Rodrigues et al. 2025); fits tied to Planck hold it near 1. The trap: counting at the ends needs energy
  conservation, which comes from time symmetry (Noether), and an expanding universe has none. The method fails at
  cosmic scale.
- *Standard model:* forces are carried by exchanged particles that are never observed; the S-matrix is built only
  from what goes in and what comes out, a theory of the end balls. Phonons are the quantum cousin of the cradle's
  pulse, and superconducting electron pairs (BCS) use the lattice as their middle balls.
- *Quantum mechanics:* the middle has no definite path until measured. Weak measurement (Aharonov, Albert and Vaidman
  1988; Kocsis et al. 2011 reconstructed average photon paths through two slits). The two-state vector formalism puts
  a system between a prepared start and a selected end: bookended. The inverse is the Elitzur-Vaidman bomb tester
  (1993): detection with no energy passing through.
- *String theory:* nothing directly testable here. Extra-dimension models (Arkani-Hamed, Dimopoulos and Dvali 1998;
  Randall and Sundrum 1999, two papers) predict energy leaking out of our three dimensions, seen as missing momentum at the LHC,
  and none is found. Holography (Maldacena, preprint 1997, published 1998) encodes everything inside a volume on its boundary: the middle
  rebuilt from the ends, in its strongest form.

---

## 1. Conservation laws as free truth on real footage

**The idea.** The ladder is synthetic because real footage has no true motion field. Physics supplies partial truth
anyway. An object in free flight (thrown, dropped, between bounces) has an acceleration of exactly g downward and a
jerk of exactly zero. A pendulum conserves its energy within a swing. A collision conserves momentum. Any departure
is the instrument's error, less a small drag term for a dense ball on a short flight. This is the silent-failure
guard "a control that must not move", supplied by physics.

**What we have.**
- The quadratic ladder cases already have zero jerk by construction, and the demo's `bounce-gravity` scene has a
  constant acceleration between impulses (its first-cut velocity reading 0.95). Those are the synthetic half.
- The jerk record (NFRAME-LIMITS, "Jerk is not noise-limited, it is truncation-limited", 2026-09-09) found every jerk
  figure on sinusoids contaminated by truncation, and noted that no case separates noise from truncation. **A parabola
  does**: a cubic fit to a parabola is exact, so the jerk residual in free flight is pure noise. A real thrown ball is
  the parabola the ladder never had at a useful size.

**Next steps.**
1. *The synthetic control first.* On `bounce-gravity`, read acceleration and jerk between bounces; report the
   acceleration against the scene's g and the jerk residual. This is the number the real clip is judged against.
   Pre-register: acceleration within 5 percent, jerk residual at the oscillations' level (0.05-0.2 px/frame^3).
2. *Shoot the clip* when the camera is free. A dense ball marked with high-contrast texture (a plain ball has no
   texture and falls to the aperture problem), tossed ACROSS the frame with the flight's plane parallel to the
   sensor. A tripod, a short shutter, 60 fps and 240 fps, and a metre stick in the flight's plane for scale.
3. *Read the field on the ball.* Fit a parabola to each flight. Report:
   - the acceleration's constancy over the flight (its spread);
   - the jerk residual, the first real-footage noise floor with a truth attached;
   - g in m/s^2 through the metre stick.

   Pre-register g within a figure set after step 1. The same arithmetic runs the other way: a = g x (px per metre) /
   fps^2, so with the frame rate known a thrown ball is a free ruler, and with the scale known it checks the timing.
4. *A pendulum* (a weight on a string). The sum 1/2 v^2 + g h should hold within a swing; damping is slow and
   monotone, so any wobble within a swing is instrument error. It also exercises the turning points, where velocity
   is zero and acceleration is largest.
5. *A bounce.* The parabolas before and after an impact each extrapolate to the floor; where they meet is the impact's
   time inside the frame interval. This feeds investigation 3.

**Prior art to survey first.** Video analysis in physics teaching (the Open Source Physics "Tracker" tool fits
parabolas to thrown balls; the classroom measurement of g from video). Any vision work that calibrates a camera's scale
or timing from gravity or from projectile motion (to find).

*2026-10-01: surveyed on 2026-09-30: [PRIOR-ART.md, "Before the energy-transfer investigations"](PRIOR-ART.md#before-the-energy-transfer-investigations-surveyed-2026-09-30); what it
changed is ["What the survey changed"](#what-the-survey-changed-2026-09-30).*

**Cost.** One GPU reading pass over short clips; the rest is Python. A phone, a tripod and ten minutes of throwing.
On the Mac, best of three for anything that goes through the propagated family (the Mac's reading wanders).

*2026-10-01: superseded: with MoltenVK's two switches set, best of three is retired and one Mac run is a measurement
again ([MOLTENVK-NONDETERMINISM-INVESTIGATED.md](MOLTENVK-NONDETERMINISM-INVESTIGATED.md), section 8).*

**What it buys.** The first acceleration and jerk noise floors measured on real footage against a truth. The ladder
has always been the only calibrated place; this would be the real-footage counterpart.

**Traps.**
- **Perspective.** A throw towards or away from the camera is not a polynomial in image space. The projection alone
  adds jerk that the physics does not have.
- **Rolling shutter.** The rows are exposed at different times, which skews a fast mover.
- **Blur and lens distortion.** Motion blur needs a short shutter; lens distortion needs the flight kept central.
- **Drag.** A light ball decelerates visibly; use a dense one.

### Results: 1.1, the synthetic control (2026-09-30)

`tests/probes/energy/gravity.py`: the master scene `bounce-gravity` (a textured box on the flat black ground,
1280x720, 120 source frames, g = 0.5689 px/frame^2). The four-frame propagated shader's reading tail was switched
to machine acceleration and jerk (as `probes/jerk/jerksweep.sh` does) and rendered at N:N on the M5 through
MoltenVK. It was scored inside the box, eroded 12 px, over the 100 frames more than 2 source frames from a hit.
This is a single run; the Mac wanders in the propagated family, so best of three belongs before any comparison to
the tenth.

*2026-10-01: superseded: with MoltenVK's two switches set, best of three is retired and one Mac run is a measurement
again ([MOLTENVK-NONDETERMINISM-INVESTIGATED.md](MOLTENVK-NONDETERMINISM-INVESTIGATED.md), section 8).*

    truth frame   acc y median     % of g    per-frame p10..p90    acc x median   jerk median (x, y)    |jerk| p90
    k             +0.5466          96.1%     +0.328..+0.703        -0.019         (+0.0001, +0.0546)    0.48
    k - 1         +0.5310          93.3%     +0.328..+0.720        -0.015         (+0.0079, +0.0624)    0.52
    k + 1         +0.5154          90.6%     +0.311..+0.736        -0.027         (-0.0116, +0.0275)    0.63

**Best of three (the same day, two more runs):** 96.1, 94.7 and 97.5 percent of g. That spread is 2.8 points, all
within 5 percent. The jerk medians are +0.055, +0.066 and +0.082 in y, and the per-frame p90 0.42-0.48. One run
had a single bad frame (p10 +0.04).

**Against the prediction.**
- **Acceleration within 5 percent: PASSED** on all three runs (94.7-97.5 percent), with the field aligned to its own frame.
- **Jerk residual at the oscillations' level (0.05-0.2 px/frame^3): PASSED for the median, MISSED per frame.** The
  median jerk sits at (0.000, +0.055), and a parabola has zero truncation, so that is the noise's bias. Frame by
  frame, the box's median jerk reaches 0.48 at the 90th percentile, above the band.

**What it gives the real-footage test.** The number to judge a thrown ball against, on this instrument:
- g to about 4 percent from a median over some 100 frames;
- any single frame's acceleration only to about +-30 percent;
- any single frame's jerk only to about 0.5 px/frame^3.

g here is 0.57 px/frame^2, close to the size of the peak-locking floor measured on static scenes (0.52). A real
throw filmed large and fast enough to give several px/frame^2 would read better. That is a design constraint for
step 1.2: fill the frame with the flight.

## 2. Hidden spin: the energy a centre tracker misses

**The idea.** A tracker that follows centres sees only the centre's travel. A dense field also sees rotation, as curl
in the flow on the body. By Koenig's theorem the total kinetic energy splits exactly into the centre's share and the
share about the centre. For a body rolling without slipping, the rotational share is:
- a uniform disc (I = M R^2 / 2): 1/3;
- a solid sphere (2/5): 2/7;
- a hoop or ring: 1/2.

A centre tracker misses that share entirely. A body spinning in place is the extreme: the tracker reports zero energy
and the field reports all of it.

**What we have.**
- `tests/probes/verbs/rolling.sh`: the rolling wheel (R 150 px, v 8 px/frame). Velocity reads 97-100 percent of truth
  down to 3.7 px/frame and 87 percent at 1.6, along one diameter.
- The velocity gradient tensor (read_view 9, `tests/tensorcheck.py`, `tests/probes/shear/matched.sh`). Its curl reads
  95 percent of truth on a matched rotation, with cross-talk under 10 percent.
- The demo's spin scenes: `spin-constant`, `spin-accelerating`, `spin-pendulum`. In the last, the rotational energy
  swings between zero and its maximum, visible only in curl.
- The Blender bridge (headless, Metal): a 3D ball with its true flow from Blender's vector pass.

**Next steps.**
1. *The energy split on `rolling.sh`*, with pixel area as mass. The dense route: total = sum of 1/2 |u|^2 over the
   disc, centre = 1/2 N |mean u|^2, spin = the difference. The curl route: omega = curl / 2 from the inner 70 percent
   of the disc, spin = N R^2 omega^2 / 4. **The two routes must agree; that is the check.** Pre-register: the dense
   route 0.32-0.34, and the curl route within 5 percent of it. The small-flow floor bites near the contact point, but
   the energy weights by v^2, so the slow region contributes little.
2. *Spin in place and spin that swings.* On `spin-constant` the centre tracker reports nothing and the field reports
   everything. On `spin-pendulum`, the energy's swing should be read in curl, and it should agree with the scene's own
   law.
3. *A ball, not a disc.* In Blender: a textured sphere rolling, with the vector pass as the true flow. The field only
   shows the visible hemisphere, foreshortened, so recovering spin needs the sphere's model: fit the angular velocity
   vector to the flow on a known sphere, u = (omega x r) projected, by least squares. Pre-register 2/7.
4. *A pool ball, real.*
   - A plain ball's spin is INVISIBLE to any field: it has no texture, and its specular highlight stays put rather than
     turning with it. A spotted training cue ball (sold as a "measles" ball) makes the spin visible.
   - With a plain ball the spin has to be inferred from its consequences, which is the cradle's method. After a cue
     ball hits an object ball, it leaves at about 90 degrees to the object ball's path if it was sliding, and at about
     30 degrees over a wide range of cut angles if it was rolling (the 90 and 30 degree rules). So the departure angle
     reads the hidden spin.
   - The test: film both on a table and compare the angle's inference with the spotted ball's measured spin.
5. *Whether rotation helps interpolation* is a separate question. A region whose curl is uniform while divergence and
   shear are zero is a rigid rotation, and could be moved as one. The record's rotation section ("Rotation is not
   wobble, not order, and mostly not rotation") bears on whether that would pay. Do not assume it.

**Prior art to survey first.**
- Koenig's theorem (classical).
- Pool physics: Alciatore, *The Illustrated Principles of Pool and Billiards*, and his 90 and 30 degree rules.
- Spin measured from video in sport: baseball spin rate from seams, table tennis from the logo. To survey.

*2026-10-01: surveyed on 2026-09-30: [PRIOR-ART.md, "Before the energy-transfer investigations"](PRIOR-ART.md#before-the-energy-transfer-investigations-surveyed-2026-09-30); what it
changed is ["What the survey changed"](#what-the-survey-changed-2026-09-30).*

**Cost.** Step 1 is minutes of CPU on an existing probe. Steps 2-3 are small renders. Step 4 needs a table.

**What it buys.** A quantity the family can report and a trajectory tracker cannot, demonstrated with a closed-form
truth. It is a candidate row for WHAT-IT-CAN-MEASURE.md (the owner's call).

**Traps.**
- **Use the raw 1/8-res field, not the pooled one.** The pooled 13x13 window damped the disc's curl to 0.21, 0.13 and
  0.03 in Lead E.
- **The rim.** Curl dies at the rim with the texture's alias band.
- **Area is not always mass.** Area as mass assumes uniform density and a flat body.

### Results: steps 2.1 and 2.2 (2026-09-30)

**The data.** No render was needed. The field tier of 2026-09-12 (`tests/probes/masters/fieldtier.sh`) had kept the
machine velocity of the master scenes, read through both the Metal app and libplacebo at frames 12, 48 and 84, with
the closed-form truth beside it (`np-scratch/ladder2/field/<scene>/`). The scenes:
- `roll-12`: a uniform disc rolling at half vmax, about 9.6 px/frame at the centre;
- `roll-wagon`: the same disc at full vmax, its rim reaching 38 px/frame;
- `spin-constant`: a disc spinning in place.

The script is `tests/probes/energy/koenig.py`. It uses pixel area as mass and the same 6 px boundary erosion on the
truth and on the reading, so it compares instrument against truth on the same pixels. The eroded disc's true spin
share is 0.316 rather than 1/3, because the erosion takes the fastest pixels, at the rim.

    roll-12                  spin share                             omega (rad/frame)       noise
    host     k    truth   dense   rigid   curl        truth   rigid   curl       px RMS
    metal   12    0.316   0.371   0.308   0.308       0.0475  0.0440  0.0440     3.4
    metal   48    0.316   0.389   0.316   0.292       0.0475  0.0434  0.0410     3.7
    metal   84    0.316   0.413   0.327   0.307       0.0475  0.0438  0.0418     4.0
    placebo 12    0.316   0.353   0.291   0.299       0.0475  0.0431  0.0440     3.4
    placebo 48    0.316   0.391   0.318   0.293       0.0475  0.0434  0.0410     3.7
    placebo 84    0.316   0.414   0.328   0.314       0.0475  0.0438  0.0425     4.0

**The prediction MISSED, and the miss is the finding.**
- **What was predicted:** the dense route at 0.32-0.34, and the curl route within 5 percent of it.
- **What happened:** the dense route read 0.35-0.41, high on every row.
- **Why:** Koenig's split counts ANY scatter around the mean velocity as energy about the centre. So the field's own
  per-pixel noise, 3.4-4.0 px RMS on this disc (mostly the gross outliers the field tier counted), is booked as spin.
  The dense route overstates hidden energy by exactly the noise's energy, N s^2 / 2.
- **The fix is a model, not more data.** Fitting the rigid motion (a translation plus a rotation, by least squares)
  and setting the residual aside gives 0.29-0.33 against the truth's 0.316, a mean of 0.31, on both hosts. This is
  algebraically the dense route with the residual's energy removed, since the residual is orthogonal to the fit.
- **Lesson:** a dense field's raw kinetic energy is biased upward by its noise. Any energy bookkeeping on the field
  needs a motion model, or an independent noise estimate, first.

**Omega reads 91-93 percent of truth** on the rolling disc by the rigid fit, and 86-93 percent by the curl route.
- The first run took the curl from differences one pixel apart and read half of truth, in quantised steps. The field
  is computed on a grid of 8 px cells, so most one-pixel differences fall inside a cell. Differences must span the
  cells, 8 px apart, as Lead E computed them.
- The centre's speed under-reads by a similar amount, 8.6-9.2 against about 9.6, so the SHARE survives the under-read
  better than either part does.

**Spin in place (step 2.2): the centre tracker recovers nothing, the field about 86 percent.**
- On `spin-constant` the centre reads (0.0, 0.0) +- 0.07 px/frame, so every route gives a spin share of 1.000. A
  tracker of centres reports no kinetic energy at all.
- The field reads omega at 0.0475-0.0478 against 0.0511, 93 percent, by the rigid fit (curl 89-95 percent).
- Since energy goes with omega squared, the field recovers about 86 percent of the spin energy, where a tracker
  recovers none.
- Both hosts read their best against truth k - 1 here: the off-by-one the field tier recorded.

**Out of reach, energy hides too: `roll-wagon` is not a spin test.**
- Its top half runs at 19-38 px/frame, beyond the field's reach of about 23-24 px. The centre reads at about 53
  percent of its speed, omega at 22-35 percent, and the noise at 10 px RMS.
- It is the known reach cliff (NFRAME-LIMITS, the reach at 24+ px/frame), seen as missing energy: fast content does
  not show up as fast.

**Metal and libplacebo agree** to about 0.02 in share and 0.001 rad/frame in omega. The same instrument reads the same
on both.

**What follows for the rest of this document:**
- Every energy or momentum ledger in investigations 1, 3 and 4 must fit a motion model first, or subtract a measured
  noise energy. The raw field will always show hidden energy that is really its own noise.
- The 7-9 percent under-read of omega and of speed is a scale error. It cancels in shares and ratios but not in
  absolute energies.

### Results: 2.3, the sphere fit on a ball spinning in place (2026-09-30)

This is a first step before the rolling ball the plan names; spinning in place isolates the geometry.
- **The render:** `tests/probes/energy/sphere_blender.py`, headless Blender 5.2 on Metal (EEVEE). A unit sphere,
  250 px radius, orthographic, black ground. An emission-only noise texture turns with the ball, so brightness does
  not change with the angle. 2 degrees a frame (0.0349 rad) about one axis, 48 frames.
- **The fit:** `spherefit.py` runs the four-frame field at N:N and fits omega x r, projected on the visible
  hemisphere (Z = -sqrt(R^2 - X^2 - Y^2)), by least squares within 0.9 R, per frame. Beside it, the curl on the
  8-px grid within 0.7 R, halved.

    spin axis                          sphere fit omega (rad/frame)            |omega|    axis error   curl / 2
    vertical (IN the image plane)      (-0.00006, -0.03491, -0.00007)         100.0 %     0.2 deg      -0.1 %
    line of sight (the control)        (-0.00005, +0.00011, +0.03374)          96.7 %     0.2 deg     +97.9 %
    truth                              (0, -0.03491, 0) / (0, 0, +0.03491)

- **A ball spinning about an axis in the image plane is invisible to a 2-D reading of spin.** The curl says -0.1
  percent: no spin at all. Its whole spin energy (1/2 I omega^2, I = 2/5 M R^2) is hidden from curl and from any
  centre tracker. The sphere fit recovers it at 100.0 percent, with the axis to 0.2 degrees and a frame-to-frame
  spread of 0.00006 rad/frame.
- **On the control axis, both routes read the spin:** the fit 96.7, curl 97.9 percent, curl's known performance.
- **Why the fit works so well here:** the surface speeds lie in the field's comfortable range (0 at the limb to 8.7
  px/frame at the face), and the fit averages thousands of pixels through a model with three unknowns.

**Next (2.3 proper):**
- the ROLLING ball (translation locked to spin; the pre-registered 2/7 share of the energy);
- a tilted axis;
- perspective rather than orthographic, with the model's Z taken from the camera;
- then a real ball (2.4).

### Pre-registered: 2.3, the rolling ball from above (2026-09-30, before the render)

The broadcast pool-table view.
- **The render:** Blender, orthographic, the camera looking straight down. A unit sphere (250 px) rolls along +x at
  v = 5 px/frame, spinning about the world y axis at omega = v/R = 0.02 rad/frame. That axis lies IN the image
  plane, and the top of the ball moves at 2v = 10 px/frame, inside the field's reach.
- **The fit:** five unknowns per frame, the translation (tX, tY) plus omega, on the visible (top) hemisphere, with
  the ball's centre segmented from each frame.
- **The energy split:** a centre tracker sees 1/2 M |t|^2; the ball also holds 1/2 (2/5 M R^2) |omega|^2. Truth:
  a spin share of exactly 2/7 = 0.286.

The predictions:
- **S1:** |t| and |omega| each within 5 percent of truth.
- **S2:** the fitted spin share within 0.02 of 2/7.
- **S3:** the curl route reads near zero spin (the axis is in the image plane), so a 2-D reading would put the
  whole of the ball's energy in its travel.

### Results: 2.3, the rolling ball from above (2026-09-30)

    quantity                      truth              fit (median over frames 4-43)
    translation (px/frame)        (5.000, 0)         (+5.178, -0.003)    103.6 %
    omega (rad/frame)             (0, -0.0200, 0)    (-0.00003, -0.01871, -0.00009)   93.6 %, axis 0.3 deg
    spin share of the energy      2/7 = 0.2857       0.2454  (frame spread 0.019)
    curl / 2                      (in-plane axis)    0.0000  (0.0 %)

**Against the predictions.**
- **S1 HALF PASSED:** the translation is within 5 percent (103.6); omega is 1.4 points outside it (93.6).
- **S2 MISSED:** the share reads 0.245 against 0.286. The two errors compound through the squares:
  0.2 x 0.936^2 / (0.5 x 1.036^2 + 0.2 x 0.936^2) = 0.246.
- **S3 PASSED:** curl reads exactly zero spin. A 2-D reading, or a centre tracker, puts the whole of a rolling
  ball's energy in its travel.

**Why the fit trades spin for travel here, and not in spin-in-place.**
- From above, the travel term (tX) and the spin term (omega_y Z) are nearly collinear over the visible hemisphere.
  Z barely changes near the middle, where most of the fitted pixels are.
- A small difference in how the field reads the rim (5 px/frame) and the top of the ball (10 px/frame) therefore
  moves energy from spin into travel.
- Spinning in place had no travel term to trade with (100.0 percent).

**So the method recovers about 86 percent of the hidden spin energy (0.245 of 0.286), where the 2-D routes recover
none.** Tightening it needs one of three things:
- a speed-dependent gain correction from the rolling-wheel profile (97-100 percent between 3.7 and 16 px/frame);
- weighting the fit towards the rim, where travel is isolated;
- the ball's known rolling constraint (t = omega R) as a prior when rolling is the question.

### Results: 2.3, why the rolling fit traded spin for travel, and the fix (2026-09-30, later)

**The field was not at fault.** Band by band across the rolling ball, from the centre to 0.97 R, the field reads
the true flow u = t + omega sqrt(R^2 - r^2) at 98.7-101.3 percent.

**The fit was ill-conditioned.** From above, spin shows only as the CONTRAST between the top of the ball (t + omega R,
10 px/frame) and the limb (t, 5 px/frame). A profile about 1 percent flatter (98.7 at the centre, 101.3 at 0.9 R)
moves the fitted omega by -5 percent and t by +2 percent: exactly the first run's 93.6 and 103.6. So the fit must
reach towards the limb, where only the travel is left (`FIT_R`, default 0.9):

    fit reach   omega      t         spin share (truth 0.2857)
    0.90 R      93.5 %    103.6 %    0.245
    0.95 R      94.5 %    102.9 %    0.251
    0.97 R      96.5 %    101.4 %    0.265

**At 0.97 R, S1 passes** (both within 5 percent). **S2 misses by 0.0006** (0.0206 against 0.02).

**The finding for pool footage (2.4):** measuring a rolling ball's spin from the broadcast overhead view is
intrinsically ill-conditioned. It needs the limb resolved, or a side view, where the spin axis is the line of sight
and curl reads it directly. Or it needs the rolling constraint (t = omega R) assumed, which is only fair when rolling,
and not sliding, is not itself the question.

### Pre-registered: 1.5 in simulation, the bounce's parabolas and the unit-free witness (2026-09-30 evening, before it ran)

`tests/probes/energy/twodrop.py`, on the Intel Mac's RX 6600 (the MoltenVK switch set). The camera steps 1.2-1.3
will lean on the survey's unit-free witness, so it is tested on a closed form first. The scene:
- a textured box dropped from rest, drifting 1.5 px/frame sideways, with PHYSICAL restitution 0.8 on the floor;
- 240 source frames: seven contacts, six whole flights from 54 frames long down to 18;
- the masters' own bounce is not used, because it keeps its speed at a wall hit.

The method uses only what an interpolator has:
- centres by segmentation on a flat ground, or by static-background subtraction (the temporal median) on a textured
  one;
- a free parabola per flight, fitted without the lowest frame, whose side is ambiguous;
- contact times where neighbouring parabolas intersect;
- T and h per whole flight from the fits.

The predictions:
- **D1:** every contact is found, with tau within 0.05 source frames of the closed form (median) on the flat ground.
- **D2 (the witness):** T^2 / h is constant across the flights within 2 percent (SD over mean), and the pairwise
  (T_i / T_j)^2 against h_i / h_j is within 2 percent (median).
- **D3:** g from the fits' curvature is within 1 percent. g from the field's velocity slope (1.1's route) is within
  5 percent over a flight.
- **On the textured ground:** the same with every threshold doubled.

### Results: 1.5 in simulation, the bounce's parabolas and the unit-free witness (2026-09-30 evening, the Intel Mac's RX 6600)

**On the flat ground, every prediction PASSED.**

    contact (lowest frame)   tau        closed form   error
    34                        33.751     33.750        +0.001
    88                        87.750     87.750        -0.000
    131                      130.938    130.950        -0.012
    166                      165.505    165.510        -0.005
    193                      193.137    193.158        -0.021
    215                      215.295    215.276        +0.018
    233                      233.028    232.971        +0.057

    flight   T (truth)          h px (truth)       T^2/h (8/g = 14.0625)   g: curvature   g: the field's slope
    1        53.999 (54.000)    207.46 (207.36)    14.055                   0.5692         0.5573
    2        43.188 (43.200)    132.76 (132.71)    14.050                   0.5694         0.5528
    3        34.567 (34.560)     84.85 (84.93)     14.083                   0.5681         0.5558
    4        27.632 (27.648)     54.45 (54.36)     14.023                   0.5705         0.5511
    5        22.158 (22.118)     34.76 (34.79)     14.125                   0.5664         0.5319
    6        17.733 (17.695)     22.60 (22.27)     13.912                   0.5750         0.4968   (truth g 0.5689)

- **D1 PASSED:** all seven contacts found; tau within 0.012 frames of the closed form (median), 0.057 at worst.
  Where the two parabolas meet IS the contact, as 1.5 proposed.
- **D2 PASSED:** T^2 / h is constant across the six flights to 0.47 percent (SD over mean), and 0.15 percent from
  8/g. The pairwise (T_i / T_j)^2 against h_i / h_j: 0.50 percent (median), 1.54 at worst over 15 pairs.
- **D3 PASSED, the second half narrowly:** g from the fits' curvature +0.15 percent; from the field's velocity
  slope (1.1's route) -4.9 percent, and worst on the shortest flight (-12.7 percent on 18 frames).
- **What it means for the camera:** with clean centres, the unit-free witness holds to half a percent with no g,
  no scale and no frame rate. The positions carry it; the field's slope is the weaker witness, as 1.1 found.

**On the textured ground, with static-background subtraction, D1 and D2 MISSED; the instrument failed.**
- The centres were off by 4-8 px (median; 58 at worst). The per-pixel temporal median is the box itself
  wherever the box dwells, which is near the floor through the late, low bounces.
- So tau erred by 0.15 frames (median; 0.40 at worst), T^2/h spread 12 percent, and the pairwise ratios 12.5
  percent. g from the curvature was -11.5 percent.
- The field's slope held (-6.0 percent, inside the doubled 10). The field does not use the segmentation's
  centres, only its region.
- The lesson for the camera clip: a static background model needs the object to move ON. Film a stretch of
  empty frame first, or take the region from the field (tried next, labelled as added after the miss).

**Two more instruments on the textured ground, both added after that miss:**
- **The field's own moving region FAILED too.** The ground is still, so everything moving should be the box. But
  spurious regions put a centre up to 245 px away, the region lags about half a frame's motion, and the lowest-point
  rule split the flights into fragments. The probe's own guard (a flight too short to fit) stopped it rather than
  fit them.
- **A CLEAN PLATE worked** (the ground filmed empty before the throw, subtracted). Vertical centres were within
  1.05 px (median, 3.4 at worst); x was biased by 6.7 px where the box's texture matches the ground, which a
  vertical witness never uses. Against the doubled thresholds:
  - **D1 PASSED:** tau within 0.037 frames (median), 0.087 at worst.
  - **D3 PASSED:** g by curvature -1.3 percent, the field's slope -5.1 percent.
  - **D2 MISSED:** T^2/h spread 5.2 percent against 4, and the pairwise ratios 5.0 percent (median). The flights
    tell why:

        flight      1       2       3       4       5       6
        h px        207     133     85      54      35      22
        T^2/h      14.13   14.13   13.76   14.42   13.46   15.81   (8/g = 14.06)

    A centre error of about 1 px is 0.5 percent of the first rise and 11 percent of the last. The witness's error is
    the centre error over the rise, so it needs rises at least 50 times the centre error for 2 percent. On the
    first four flights (rise 54 px and up) the spread is 1.9 percent. That reading was taken AFTER the miss.
- **For the camera (1.2-1.3):**
  - shoot a clean plate before the throw;
  - use drops whose rise is at least 50 times the centre's error (with a 1-px error, at least 50 px; at 1080p, a
    drop of 20 cm or more with a metre-wide frame);
  - weight flights by their rise, or drop the short ones before the ratio is taken.

### Pre-registered: 1.4 in simulation, the pendulum's energy (2026-09-30, before the render)

`pendulum_blender.py` / `pendulumfit.py`:
- **The render:** a textured bob (R 60 px) swings on an invisible rod, L = 400 px, from 30 degrees, in exact
  simple-pendulum motion (RK4). g = 3.05 px/frame^2 gives a 72-frame period. Side view, orthographic, a dim
  textured wall behind; the bob's texture turns with the swing.
- **The measurement:** its speed from the field (RGB in, the zero check on the still wall), its height from its
  segmented centroid, and E = 1/2 v^2 + g h on every frame. The truth is constant.

The predictions:
- **E1:** the measured E stays constant within 5 percent (max - min over mean, the clip's edges excluded).
- **E2:** the kinetic energy at the bottom of the swing reads within 5 percent of the truth.

### Results: 1.4 in simulation, the pendulum's energy (2026-09-30)

The reading, exact on the Arc (RGB in; the zero check on the still wall), over 90 frames (the edges out):

    measured E / m      mean 163.81 (truth 163.45, constant): +0.2 %
                        p5-p95 155.5 .. 171.2 (-4.9 .. +4.8 %); max - min 11.6 % of the mean
    kinetic energy at the bottom of the swing (14 frames): 157.19 against 160.84, -2.3 %
    speed read / truth, median over the swing: 0.992; height error +0.60 px median (the pixel-centre convention)
    speed dropouts (read < 80 % of a truth above 8 px/frame): 0 of 65

- **E1 MISSED as worded:** max - min is 11.6 percent, not under 5. The measured energy's MEAN is right to 0.2
  percent, and its p5-p95 band is +-4.8 percent. The spread is the per-frame speed noise, squared in 1/2 v^2.
- **E2 PASSED:** -2.3 percent at the bottom of the swing.
- **For real footage:** a pendulum's energy is a working "control that must not move". The field's mean holds it
  to 0.2 percent, and any single frame to about 5.

**A finding for the Mac side, from the same frames.** The M5 read this pendulum through the same RGB path with NINE
speed dropouts: frames reading 6-8 px/frame where the truth was 14-17, at different frames on each run. The Arc read
it with none. So the MoltenVK wander (TESTING.md, the Linux witness) is not small noise. It is intermittent GROSS
failures on a fast body, reading about 40 percent of its speed. That clue goes to the parked root cause.

*2026-10-01: the root cause was found from this clue: two MoltenVK hazards, each removed by one of MoltenVK's own
switches ([MOLTENVK-NONDETERMINISM-INVESTIGATED.md](MOLTENVK-NONDETERMINISM-INVESTIGATED.md), sections 4-6).*

**The free-flight control, exact on the Arc** (gravity.py, RGB in, a 16-bit source): **98.8 percent of g**, per-frame
p10-p90 0.42-0.72 (against the M5's three runs through the 8-bit path, 94.7-97.5, and 0.33-0.75). The jerk median is
(-0.014, +0.090) with a per-frame p90 of 0.36.

### Pre-registered: 2.3, a tilted axis and a perspective camera (2026-09-30, before the renders)

Both with the orthographic sphere model of the fits so far, fitting within 0.97 R.
- **`tilt`:** spin about an axis halfway between vertical and the line of sight (world (0, 1, 1)/sqrt 2).
  - **T1:** |omega| within 5 percent and the axis within 2 degrees.
  - **T2:** curl reads only the line-of-sight part, cos 45 = 70.7 percent of |omega|.
- **`persp`:** the vertical-axis spin under a 50 mm perspective camera, with the ball 250 px in radius at the frame
  centre.
  - **T3:** using the orthographic model anyway costs under 5 percent of |omega|.

### Results: 2.3, a tilted axis and a perspective camera (2026-09-30)

    case                         truth omega                    fit (orthographic model, 0.97 R)          curl / 2
    tilt (axis 45 deg in depth)  (0, -0.02468, +0.02468)        (+0.00013, -0.02454, +0.02365)  97.6 %,   68.5 % of |omega|
                                                                axis 1.1 deg                              (the sight part: 97 %)
    persp (vertical, 50 mm)      (0, -0.03491, 0)               (-0.00013, -0.03999, +0.00005) 114.6 %,   0.0 %
                                                                axis 0.2 deg

- **T1 PASSED:** the tilted axis is recovered at 97.6 percent, the axis to 1.1 degrees.
- **T2 PASSED:** curl reads 68.5 percent of |omega| against the predicted cos 45 = 70.7. That is 97 percent of the
  line-of-sight component, and none of the rest.
- **T3 MISSED, predictably.** Under a 50 mm perspective camera with the ball at 7.11 radii, the orthographic model
  over-reads the spin by 14.6 percent, though the axis stays at 0.2 degrees. The front of the ball is nearer the
  camera than its silhouette (D - R against about D), so it is magnified by D / (D - R) = 1.16 relative to the
  silhouette the model is scaled from.
- **What it means for real footage:** the spin's AXIS survives the wrong model, but its magnitude needs either a
  perspective sphere model or that factor. The factor follows from the ball's known size and the lens.
- **The fix, tested the same hour:** a PINHOLE sphere model (`PERSP_F`, the focal length in px). The distance comes
  from the silhouette (sin alpha = R / D, tan alpha = r_px / f). Each pixel's ray meets the sphere at P, the spin
  moves P at omega x (P - C), and its image velocity f (V P_z - P V_z) / P_z^2 is still linear in omega. On the
  same render it reads **98.6 percent**, axis 0.2 degrees; the factor D / (D - R) predicted 98.5. For real
  footage the lens's focal length and the ball's silhouette are enough.

### Pre-registered: 2.5, does moving a rigid rotation as one pay? (2026-09-30 evening, before it ran)

`tests/probes/energy/rotwarp.py`, on the M5 (the MoltenVK switches set: one run is exact). The same design as 3.2's
placer: the region is GIVEN (the disc), so the question is only whether a region known to be rigid is better drawn
by one rotation than by the family's per-block field. Four ways, all through the same yuv420p + libplacebo round
trip, scored inside the disc (PSNR-Y against the closed form) on the interpolated output frames, 24 -> 60:
- **rec:** the Cadence default as shipped;
- **true:** the disc moved by the TRUE rigid motion from source frames k and k + 1, blended (the upper bound);
- **fit:** the same warp driven by the field's rigid fit (trimmed least squares, the field's own off-by-one);
- **reg:** fit's rotation refined by registering frame k + 1 against frame k rotated back.

Scenes: `spin-constant`, `spin-pendulum`, `spin-orbit`, `roll-12`, `roll-12-fast` (the rim beyond the reach), each on
the aperiodic `noise` texture and the smooth `sines`.

The predictions:
- **T1 (the stake):** true beats rec inside the disc by at least 3 dB (median) on every scene within the reach.
  The record says rotation fails through aperture, period locking and the pyramid, none of which a given rigid
  region suffers.
- **T2 (the field alone is not enough):** fit's gain over rec is less than half of true's. The field reads the
  rotation at 91-93 percent (2.2), which leaves about 0.7 px at the rim of `spin-constant` in mid-interval.
- **T3 (registration closes it):** reg recovers at least 70 percent of true's gain within the reach.
- **T4 (beyond the reach):** on `roll-12-fast`, true's gain is the largest of all (at least 6 dB), and fit fails
  (the field reads the fast rim at 22-35 percent). Whether reg recovers depends on its 0-to-3x search reaching the
  truth: no prediction.
- **The scoring path was replaced before the batch ran** (after the first two scenes): see the results.
- **T5 (added before its run, on the Intel Mac's RX 6600): the textures the record says fail.** `spin-constant`
  and `roll-12` on `lattice` (period 40 px, the record's period-locking case) and `weave` (fine).
  - On `lattice`, rec's field locks to the period, so true's gain over rec is LARGER than on `noise` (above 3 dB).
  - fit fails there too: a rigid fit of a locked field reads the wrong rotation.
  - reg's registration may lock to a period as well: no prediction.

### Results: 2.5, moving a given rigid rotation as one (2026-09-30 late evening; the M5, the lattice on the Intel's RX 6600)

**The scoring path had to be rebuilt first, and the rebuild is now the rule for any probe that draws its own frames.**
- The first design built the warps from the 16-bit source and pushed them through an 8-bit round trip. rec blends
  two 8-bit frames in float and pays half the input's quantisation noise and one output dither; the warps paid a
  full quantisation plus the dither. On `spin-pendulum` that put rec ABOVE its own exact-frame level.
- The equal-footing path gives every method the same 8-bit frames the shader receives (swscale's Y, read back),
  and reads rec out of libplacebo at 16 bits (`format=gray16le`; checked on a random image: no shift, identical
  levels, 18 of 16384 pixels differing where Y = 236 is clipped).
- The control: rec on exact source frames equals its 8-bit input at 73-75 dB on every run.
- 3.2's placer was re-scored the same way (above): its result stands.

Inside the disc, median PSNR-Y (dB) over the 173 interpolated frames. true / fit / reg are bilinear, as a shader
samples; true3 / reg3 the same with a cubic-spline resampler (added after the first two scenes). The last column is
the field's rotation per interval against the truth (fit's input):

    texture   scene           rec     true    fit     reg     true3   reg3    true-rec  field's rotation
    noise     spin-constant   48.92   51.80   51.79   51.80   52.23   52.23   +2.88     0.981
    noise     spin-pendulum   53.17   51.93   51.91   51.91   52.32   52.31   -1.24     0.950
    noise     spin-orbit      47.89   48.80   48.66   48.68   49.41   49.26   +0.91     0.975
    noise     roll-12         36.32   38.44   38.43   38.44   41.27   41.26   +2.12     0.988
    noise     roll-12-fast    29.56   37.93   37.24   37.89   40.16   40.11   +8.37     0.963
    sines     spin-constant   50.85   50.31   50.31   50.31   51.04   51.04   -0.54     0.963
    sines     spin-pendulum   53.44   50.52   50.47   50.49   51.30   51.28   -2.92     0.908
    sines     spin-orbit      46.74   47.58   47.44   47.45   48.22   48.08   +0.84     0.942
    sines     roll-12         34.52   36.74   36.63   36.73   39.71   39.71   +2.22     0.971
    sines     roll-12-fast    28.31   36.48   35.18   36.47   38.99   38.97   +8.17     0.949
    lattice   spin-constant   19.62   47.85   40.73   47.84   --      --     +28.23     0.700   (T5)
    lattice   roll-12         34.47   36.94   36.93   36.94   --      --      +2.47     0.991   (T5)
    weave     spin-constant   13.77   37.69   15.00   17.30   --      --     +23.92     0.016   (T5)
    weave     roll-12         19.61   34.73   24.87   34.73   --      --     +15.12     0.435   (T5)

**Against the predictions.**
- **T1 MISSED:** within the reach, true's gain is -2.9 to +2.9 dB, never 3. Where the family's field already
  follows the rotation (smooth or aperiodic texture, in reach), moving the region as one adds little. On the slow
  pendulum it loses, because two bilinear resamplings blur more than rec's small displacements do. A better
  resampler is worth 0.4-3 dB to every warp (true3 against true), the most on the rolling discs.
  - **A caveat found by 2.5b's control, the `static` scene:** rec's interpolated frames read 51.95 dB there, 0.4
    ABOVE its own 8-bit input (51.53), while the warps sit exactly on the input. The field's small noise makes rec
    sample at sub-pixel offsets, and bilinear sampling low-passes the input's quantisation noise against a
    CONTINUOUS truth. rec gets that "free denoise" on every slow frame; a warp that lands on the pixel grid does
    not. It is a synthetic-truth effect (a real truth frame is itself quantised), and it is part of rec's margin on
    the slow scenes.
- **T2 REFUTED:** fit matches true almost everywhere. The field's rigid fit reads the rotation at 91-99 percent
  (the trimmed fit, not 2.2's raw 86-93), and what is left costs at most 0.15 dB within the reach.
- **T3 PASSED:** reg equals true everywhere (the rotation exact to 0.01 px at the rim).
- **T4 half PASSED:** beyond the reach (`roll-12-fast`) true's gain is the largest of the registered five, +8.2
  to +8.4 dB. **But fit does NOT fail, and that is the finding:** the field reads this wheel's rotation at 95-96
  percent, although its top half moves faster than the field can follow. The trimmed rigid fit rejects the
  unreachable cells as outliers and extrapolates the rotation from the reachable ones: the rigid-body constraint
  recovers motion the field cannot see. That is the Newton's-cradle question answered in small: a model of the
  body infers the motion the instrument misses. fit gains +7.7 and +6.9 dB, reg +8.3.
- **T5 PASSED on the spin:** on the period-40 lattice, rec collapses to 19.6 dB (the record's period locking) and
  the true rigid warp scores 47.9: **+28.2 dB**. The field's own rigid fit, reading the rotation at only 70 percent,
  still gains +21.1; registration seeded by it, searching 0 to 3 times its value, found the truth without locking
  to a period (+28.2). On the rolling lattice the field did not lock (99 percent) and the gain is +2.5, like noise.
- **The weave is worse still (T5's second texture).** On the spinning weave the field reads 1.6 percent of the
  rotation: it is BLIND to it, and rec collapses to 13.8 dB. The true rigid warp scores 37.7 (+23.9).
  - fit has nothing to fit (+1.2).
  - reg fails too (+3.5). Seeded at about zero, its search (0 to 3 times the seed, plus 0.02 rad) never reaches
    the truth, 0.051.
  - On the rolling weave the field reads 44 percent. rec is at 19.6, fit gains +5.3, and reg, seeded at 44
    percent, finds the truth: +15.1, equal to true.
  - So registration rescues a field that is wrong but not blind. A blind field needs a seed from somewhere else,
    or a wide search, which risks the period locking the lattice showed.
  - The weave (a woven-fabric pattern) is also a finding for NFRAME-LIMITS: the family's field is blind to it in
    rotation. Fabric in motion is common footage.
  - **T6, a side check (registered before it ran):** is the weave a ROTATION failure, or does the Cadence default
    fail on woven texture in translation too? `masters/check.sh` (the master tier, exact truth, hold and linear
    beside) on `bounce-constant`, `bounce-oscillating`, `spin-constant` and `roll-12`, textured ground, with
    TEXTURE=weave against TEXTURE=noise. The prediction: in translation (the bounces) weave scores within 3 dB of
    noise, and the collapse is rotation's alone.
  - **T6 REFUTED (the M5, 2026-09-30 20:58):** the weave collapse is NOT rotation's alone. The master tier's ladder
    mean (full frame, textured ground, 240 frames), the Cadence default against linear:

        scene                 noise: rec / linear    weave: rec / linear
        bounce-constant       51.15 / 39.16          26.42 / 25.26
        bounce-oscillating    53.89 / 42.10          27.47 / 28.82   (below linear)
        spin-constant         52.76 / 42.80          20.39 / 21.16   (below linear)
        roll-12               45.42 / 30.08          29.49 / 24.78

    On aperiodic texture the default beats linear by 12-15 dB. On the weave it gains about 1 dB in translation and
    falls below linear on two scenes. The weave has threads of period 14 px and a 28-px over-under checkerboard,
    below Nyquist at the coarse levels. It is very likely a two-dimensional case of the record's periodic-interior
    front (V3). It is recorded in NFRAME-LIMITS as a data point: the master tier had only ever been scored on sines.

**What it means.**
- A rigid-region mode would be a REPAIR, not a refinement: worth 8-28 dB exactly where the family fails (period
  locking, beyond the reach), and worth little or worse where it already works.
- The field's own rigid fit is enough to drive it, and a registration refines it to exact.
- What the family actually lacks is the region: which pixels belong to one rigid body. The region was GIVEN here.
  On the lattice the field that would have to find it is the locked one.
- The rolling scenes' gains include the given region's exact boundary (the occlusion at the rim), so part of them
  is region knowledge, not rotation. The spins in place have no occlusion and are the clean measure.
- **A second lead, recorded beside the warm one:** a rigid-region mode for wheels and spinning periodic texture. It
  is the same shape as the impact placer (a model of the body, drawn from the frames), and it has the same open
  question: finding the region in real footage.

### Pre-registered: 2.5b, can the field FIND the rigid region? (2026-09-30 late evening, before it ran)

2.5 gave the region. Both leads (the impact placer and a rigid-region mode) need it found from the field alone.
`rotwarp.py`'s new variant `found` takes nothing from the scene:
- per field frame, RANSAC for a similarity model over the moving cells (|u| > 0.5 px/frame), inliers within
  1 px/frame, the largest connected inlier set, closed and hole-filled;
- the warp over [k, k + 1] takes that region at k and field k + 1's model, applied about the region's centroid;
- scored as the other variants (inside the true disc, and the full frame).

The scenes are the 2.5 set, plus `static` as the control.

The predictions:
- **F1:** within the reach on noise and sines, the found region's IoU with the true disc is at least 0.85, and
  found's PSNR is within 1 dB of fit's (the given region).
- **F2:** beyond the reach (`roll-12-fast`), the region misses the unreachable top (IoU 0.4-0.7), yet found
  still gains at least 4 dB over rec inside the disc (half of fit's +7).
- **F3:** on the spinning lattice, the locked field yields a fragmented region (IoU under 0.5) and found gains
  under 5 dB (fit had +21 with the region given).
- **The control that must not move:** on `static` no region is found, and found equals rec exactly.

### Results: 2.5b, finding the rigid region from the field (2026-09-30 late evening, the M5)

The `found` variant beside rec and fit (fit has the region given), inside the true disc, median PSNR-Y (dB), with the
found region's IoU against the true disc:

    texture   scene           rec     fit     found   found-rec (median per frame)   IoU
    noise     spin-constant   48.92   51.79   49.10   -0.04                          0.921
    noise     spin-pendulum   53.17   51.91   52.49   -0.74                          0.937
    noise     spin-orbit      47.89   48.66   47.90   -0.03                          0.939
    noise     roll-12         36.32   38.43   36.70   +0.23                          0.815
    noise     roll-12-fast    29.56   37.24   29.18   -0.18                          0.385
    sines     spin-constant   50.85   50.31   50.54   -0.31                          0.582
    sines     spin-pendulum   53.44   50.47   52.70   -0.73                          0.633
    sines     spin-orbit      46.74   47.44   46.71   -0.05                          0.578
    sines     roll-12         34.52   36.63   34.67   +0.07                          0.187
    sines     roll-12-fast    28.31   35.18   28.16   -0.08                          0.125
    lattice   spin-constant   19.75   43.68   20.04   +0.42                          0.641
    lattice   spin-pendulum   29.57   48.78   48.12   +6.70                          0.988
    lattice   spin-orbit      22.77   46.93   24.79   +0.96                          0.828
    lattice   roll-12         34.36   36.93   34.98   +0.26                          0.880
    lattice   roll-12-fast    17.25   16.56   17.22   -0.02                          0.368
    weave     spin-constant   13.77   15.00   14.05   (+0.28 of medians)             0.102   (the Intel)
    weave     spin-pendulum   18.49   22.43   18.58   (+0.09)                        0.306
    weave     spin-orbit      15.18   20.57   15.75   (+0.57)                        0.158
    weave     roll-12         19.61   24.87   20.33   (+0.72)                        0.485
    weave     roll-12-fast    14.43   14.36   14.60   (+0.17)                        0.168
    (static, the control: no usable region; found = rec on every frame)
    On the weave the true rigid warp scores 34.6-37.9 on every scene: +15 to +24 dB over rec, which is at
    13.8-19.6 throughout. Registration recovers most of it where the field is partly right (the pendulum 37.5,
    the orbit 31.1, roll-12 34.7) and nothing where it is blind (spin-constant, roll-12-fast).

**Against the predictions.**
- **F1 MISSED:** the region reaches IoU 0.92-0.94 only on the aperiodic spins. On sines it is 0.58-0.63, and on the
  rolling sines 0.19. Even where the region is good, found gains almost nothing: spin-constant on noise, IoU 0.92,
  is 49.10 against fit's 51.79.
- **F2 MISSED:** beyond the reach the region is worse than predicted (IoU 0.13-0.39) and found gains nothing.
- **F3 half:** the lattice spin's region is not fragmented (0.64), but it is driven by the locked field, and
  found gains +0.4 (predicted under 5).
- **The control HELD:** on `static` found equals rec exactly.
- **The one clear win:** the lattice pendulum, IoU 0.99, found 48.1 against rec 29.6. When the field can see the
  body whole, the found region carries almost all of the given region's gain.

**Why found fails where its region looks good (the diagnosis, spin-constant on noise, one frame).** Where found
drew, it equals fit (mean difference 0.00004). But it covered 91.6 percent of the disc against fit's 99.1. The
missing 8 percent is the outer ring, about 15 px wide. The rim is where rec's errors are largest, so it is where
the whole gain lives. The field's cells that straddle the edge mix the body's motion with the ground's, so they are
never rigid inliers, and the region stops short of the rim. This is the motion-boundary problem, the oldest in
optical flow. A cell-level region cannot reach a pixel-level edge.

**So the region has to be finished at the pixel level.** The natural test is photo-consistency: in a ring outside
the found region, a pixel belongs to the body if the rigid model's two samples of it (from frame k and from frame
k + 1) agree. That is tried next, labelled as added after this result (2.5c).

### Pre-registered: 2.5c, finishing the region at the pixel level (2026-09-30 late evening, AFTER 2.5b's diagnosis, before it ran)

`found2`: the found region dilated by 4 cells (32 px), and a pixel of that ring kept only where the rigid model's
two samples of it (frame k and frame k + 1) agree within 0.03. The found region's own cells are kept as before.
Same scenes, same scoring.

The predictions:
- **C1:** on the aperiodic spins (IoU 0.92-0.94), found2 recovers at least half of fit's gain over rec.
- **C2 (do no harm):** found2 never scores more than 1 dB below rec, on any scene. The agreement test refuses the
  pixels the model gets wrong.
- **The control:** on `static`, found2 equals rec.

### Results: 2.5c, the region finished at the pixel level (2026-09-30 night, the M5; the weave on the Intel)

found2 (the found region plus a 4-cell ring kept by photo-consistency) against rec and fit (the region given),
inside the disc, median PSNR-Y (dB):

    texture   scene           rec     fit     found   found2   found2 - rec   share of fit's gain
    noise     spin-constant   48.92   51.79   49.10   50.93    +2.01          70%
    noise     spin-pendulum   53.17   51.91   52.49   50.80    -2.37          (fit loses too)
    noise     spin-orbit      47.89   48.66   47.90   48.35    +0.46          60%
    noise     roll-12         36.32   38.43   36.70   37.45    +1.13          54%
    noise     roll-12-fast    29.56   37.24   29.18   30.06    +0.50           7%
    sines     spin-constant   50.85   50.31   50.54   49.92    -0.93          (fit loses too)
    sines     spin-pendulum   53.44   50.47   52.70   50.40    -3.04          (fit loses too)
    sines     spin-orbit      46.74   47.44   46.71   47.01    +0.27          39%
    sines     roll-12         34.52   36.63   34.67   34.96    +0.44          21%
    sines     roll-12-fast    28.31   35.18   28.16   28.51    +0.20           3%
    lattice   spin-constant   19.75   43.68   20.04   26.71    +6.96          29%
    lattice   spin-pendulum   29.57   48.78   48.12   48.00   +18.43          96%
    lattice   spin-orbit      22.77   46.93   24.79   30.18    +7.41          31%
    lattice   roll-12         34.36   36.93   34.98   36.00    +1.64          64%
    lattice   roll-12-fast    17.25   16.56   17.22   17.41    +0.16          --
    weave     spin-constant   13.77   15.00   14.05   15.87    +2.10          (the Intel; true +23.9)
    weave     spin-pendulum   18.49   22.43   18.58   20.26    +1.77          (true +19.4)
    weave     spin-orbit      15.18   20.57   15.75   18.06    +2.88          (true +22.3)
    weave     roll-12         19.61   24.87   20.33   22.32    +2.71          (true +15.1)
    weave     roll-12-fast    14.43   14.36   14.60   14.73    +0.30          (true +20.2)
    (static, every texture: found2 = rec exactly; the control held)
    On the weave the found region is too poor (IoU 0.10-0.49) for the ring to rescue: +0.3 to +2.9 dB of the
    +15 to +24 a true rigid warp would give. The field that has to find the region is the locked one.

**Against the predictions.**
- **C1 two of three:** on the aperiodic spins, found2 recovers 70 and 60 percent of fit's gain (spin-constant,
  spin-orbit). On the pendulum there is no gain to recover: rec beats even the given region there.
- **C2 (do no harm) MISSED:** found2 falls 2.4 and 3.0 dB below rec on the slow pendulums, and 0.9 on the smooth
  spin.
- **The control HELD:** on `static` found2 equals rec.

**What it says about the design.**
- The pixel-level finish works. On the lattice it turns a found region worth +0.3 to +2 dB into +7 to +18.
- Beyond the reach it recovers little (3-7 percent). The region there is too poor (IoU 0.13-0.39) for the ring to
  reach the unreachable top.
- **The losses are where the region REPLACES a shader that was already right.** On the slow pendulums rec's own
  field follows the rotation, rec gets its "free denoise" (above), and the rigid warp only resamples.
- **So a rigid mode must be a REPAIR in the literal sense:** take over only the cells where the family's own field
  DISAGREES with the region's rigid model, and leave rec where they agree. That is the region-level analogue of 3.2's
  lesson (a placer only at the impact). It is a design statement for the lead, not yet a measurement.

### Pre-registered: 2.5d, the rigid mode as a literal repair (2026-09-30 night, AFTER 2.5c, before it ran)

`found3`: found2's pixels, but only where the cell they come from DISAGREES with the region's rigid model. That is
where the field's own velocity differs from the model's prediction there by more than 1 px/frame, grown by one cell.
Everywhere else rec stands. Same scenes, same scoring.
- **R1 (do no harm):** found3 never falls more than 0.5 dB below rec, on any scene. On the pendulums the field
  follows the rotation, so it agrees with the model and rec is kept.
- **R2 (the repair survives):** on the lattice, found3 keeps at least 80 percent of found2's gain over rec.
- **Added before the batch, after a one-scene check:** on the pendulum found3 was still 2.0 dB below rec. At
  mid-swing the field's own noise exceeds 1 px/frame on about 20 percent of the core's cells (its 90th percentile is
  1.3-1.4), and the one-cell growth spreads that to about 60 percent. So `found4` goes beside it: 2 px/frame (the
  record's gross line) and no growth. **R3:** found4 is never more than 0.5 dB below rec, and it keeps at least 80
  percent of found2's lattice gain.

### Results: 2.5d, the repair masks (2026-09-30 night, the M5; the weave on the Intel)

    texture   scene           rec     found2   found3   found4   f2 - rec   f3 - rec   f4 - rec
    noise     spin-constant   48.92   50.93    51.08    50.55    +2.01      +2.16      +1.63
    noise     spin-pendulum   53.17   50.80    51.00    51.23    -2.37      -2.17      -1.94
    noise     spin-orbit      47.89   48.35    48.43    48.25    +0.46      +0.54      +0.36
    noise     roll-12         36.32   37.45    37.43    36.83    +1.13      +1.11      +0.51
    noise     roll-12-fast    29.56   30.06    30.05    30.04    +0.50      +0.49      +0.48
    sines     spin-constant   50.85   49.92    49.96    50.21    -0.93      -0.89      -0.64
    sines     spin-pendulum   53.44   50.40    50.53    51.16    -3.04      -2.91      -2.28
    sines     spin-orbit      46.74   47.01    47.04    47.01    +0.27      +0.30      +0.27
    sines     roll-12         34.52   34.96    34.96    34.69    +0.44      +0.44      +0.17
    sines     roll-12-fast    28.31   28.51    28.51    28.44    +0.20      +0.20      +0.13
    lattice   spin-constant   19.75   26.71    25.58    23.38    +6.96      +5.83      +3.63
    lattice   spin-pendulum   29.57   48.00    37.75    31.05   +18.43      +8.18      +1.48
    lattice   spin-orbit      22.77   30.18    29.41    26.36    +7.41      +6.64      +3.59
    lattice   roll-12         34.36   36.00    35.90    35.13    +1.64      +1.54      +0.77
    lattice   roll-12-fast    17.25   17.41    17.43    17.44    +0.16      +0.18      +0.19
    weave     spin-constant   13.77   15.87    15.85    15.66    +2.10      +2.08      +1.89   (the Intel)
    weave     spin-pendulum   18.49   20.26    20.07    19.37    +1.77      +1.58      +0.88
    weave     spin-orbit      15.18   18.06    18.05    17.32    +2.88      +2.87      +2.14
    weave     roll-12         19.61   22.32    22.27    21.46    +2.71      +2.66      +1.85
    weave     roll-12-fast    14.43   14.73    14.72    14.52    +0.30      +0.29      +0.09
    (static: all three equal rec exactly, every texture)

**Against the predictions.**
- **R1 MISSED:** found3 still falls 2.2 and 2.9 dB below rec on the pendulums.
- **R2 MISSED as worded:** found3 keeps 84-94 percent of found2's lattice gain on three scenes, but only 44
  percent on the lattice pendulum.
- **R3 MISSED on both halves:** found4 still loses 1.9 and 2.3 dB on the pendulums, and keeps only 8-52 percent of
  the lattice gain.

**Why a disagreement mask is the wrong trust signal.** On the slow pendulum, the cells where the field disagrees with
the rigid model by more than 2 px are mostly the RIM, where the cells mix the body's motion with the ground's. rec
handles that rim well at slow speed, so repairing it there does harm. "The field disagrees here" mistakes boundary
mixing for failure.

**The signal a repair needs** is the classic motion-selection rule: per pixel, the two candidate motions (the
family's and the region's model) compared by their own matching cost, meaning how well frames k and k + 1 agree
under each, with the lower one drawn. found2's ring test was half of it (the model's own agreement), without the
comparison against the family's. That is a design statement for the rigid-region lead, recorded here rather than
tested: 2.5 has had four post-hoc variants, and the next is a design, not a measurement.

### Pre-registered: 2.4 in simulation, the pool shot (2026-09-30, before the render)

`tests/probes/energy/pool_sim.py` (the physics) and `pool_blender.py` (the render), then `poolfit.py` (the reading).
- **The physics** (Alciatore, TP A.4). Equal balls with a frictionless ball-ball contact: at a half-ball hit (a 30
  degree cut) the object ball leaves along the line of centres, and the cue ball keeps the tangential component and
  its spin. Cloth friction mu g then acts against the slip at the cloth contact, and the slip shrinks along a FIXED
  direction at 7/2 mu g. So the path is a parabola until rolling resumes after t_s = 2|u0| / (7 mu g).
- **Two shots:**
  - `roll`: the cue ball rolls naturally into the hit and ends 33.7 degrees from its original line;
  - `stun`: no spin at contact; it goes straight along the tangent line, 60 degrees from its original line and 90 to
    the object ball.
- **The scale:** slowed to the field's reach, as a high-speed camera would. Ball radius 80 px, the cue ball at
  8 px/frame, mu g = 0.1 px/frame^2, so t_s = 19.8 frames. Top-down, orthographic, textured balls on a dim ground.

The predictions:
- **P1:** the field's velocities after rolling resumes give the departure angle within 2 degrees: 33.7 for roll, 60
  for stun.
- **P2:** the per-frame sphere fit (travel plus spin, reaching 0.97 R) reads the slip at the cloth contact as clearly
  non-zero after the hit and near zero after t_s. It places the sliding-to-rolling transition within 3 frames of
  19.8. The ill-conditioning from above (2.3) is the risk.
- **P3:** during sliding the field's velocity DIRECTION turns smoothly from 60 degrees towards 33.7 (roll), the
  parabola, and stays at 60 for stun.

*2026-10-01: the results of 2.4 are under investigation 3:
[Results: 2.4 in simulation, the pool shot](#results-24-in-simulation-the-pool-shot-2026-09-30-the-reading-on-the-arc).*

## 3. Impacts: where the impact falls inside the frame, and "teleported momentum"

**The idea.** A collision is where the field's smooth model breaks: the velocity steps inside one frame interval,
and jerk shows an impulse. The demo's `bounce-constant` is the clean case: "jerk is an impulse at each bounce and
nothing between". Two uses follow.
- **(a) Placing the impact inside the interval.** The motion before and after an impact is each smooth. Extrapolate
  both, and they meet at the wall at a sub-frame time. An interpolator that knows this draws the ball touching the
  wall. One that draws a straight chord between the two frames cuts the corner: the ball never arrives. This is a
  picture-quality question for the product, and every piece of sport or play footage has bounces.
- **(b) Transfer between bodies.** Suppose momentum (area x mean velocity) vanishes from one body and appears in
  another in the same frame, with stillness between. The field has then seen a hidden coupling, and the gap's length
  over one frame bounds the coupling's speed from below. For a 5-ball cradle at 60 fps that bound is about 6 m/s
  (0.1 m in 16.7 ms); the real pulse runs at hundreds of metres a second.

**What we have.**
- The demo's bounce scenes, a box with walls:
  - `constant`: the cleanest impulse;
  - `gravity`: a constant acceleration between impulses;
  - `hardjerk`;
  - `oscillating`;
  - `masses`: walls that return different shares of the normal speed, so |v| is conserved and the angle is not.
- The reading already segments a mover: the stairs clip shows the man as one figure against the pan.
- **No scene has two bodies colliding.** Every bounce is against a wall, which does not move.

**Next steps.**
1. *Measure the corner-cutting on `bounce-constant`.* Compare the interpolated frames beside each impact with the
   truth, for hold, linear and each shader. Pre-register for linear: at an impact a fraction tau into the interval,
   with normal speed v_n, the chord's closest approach stops v_n x min(tau, 1 - tau) short of the wall, up to v_n / 2.
   The polynomial families' behaviour at a kink is unknown: measure it, do not guess.
2. *A sub-frame impact placer, offline in Python* on the read field, not a shader:
   - detect an impulse (jerk above a gate, with small acceleration either side);
   - fit the motion on each side from the window's frames;
   - solve for the time and place where the two fits meet;
   - redraw the path.

   Score it on all five bounce scenes. A shader version comes only if this pays (steps before leaps).
3. *Build body-to-body scenes*, with truth by construction (instantaneous transfer):
   - two equal discs head-on: the mover stops and the target leaves (a two-ball cradle);
   - a five-disc cradle with the middle three still;
   - unequal masses (the ledger weights by area);
   - an oblique hit between equal discs: the 90 degree departure.
4. *The ledger detector.* Per segment: momentum = area x mean velocity. Look for a step in one segment matched by an
   equal step in the same direction in another segment in the same frame, with the region between below the floor.
   That is a transfer event, reported with its speed bound. Test the false positives on independent movers that
   happen to start and stop in the same frame; the party recordings are full of them, and only numbers leave the
   machine.
5. *Real footage.* A pool break, a curling takeout (equal stones: a head-on hit with no spin stops the shooter dead),
   and a desk cradle filmed on a phone.

**Prior art to survey first.**
- **Hawk-Eye-class line calling**, which reconstructs a bounce point between frames by fitting the trajectory on each
  side (to verify the published method and accuracy).
- **Impulse-based rigid-body simulation** (Mirtich's thesis, 1996).
- **Sub-frame event timing** in high-speed sports video (to find).

*2026-10-01: surveyed on 2026-09-30: [PRIOR-ART.md, "Before the energy-transfer investigations"](PRIOR-ART.md#before-the-energy-transfer-investigations-surveyed-2026-09-30); what it
changed is ["What the survey changed"](#what-the-survey-changed-2026-09-30).*

**Cost.** Step 1 is analysis of renders that exist or are cheap to redo. Steps 2 and 4 are Python. Step 3 is a scene
build and small renders.

**What it buys.** A measured answer to whether the family cuts corners at impacts, which has never been tested for
sharpness, and possibly a fix that lands the ball on the wall.

**Traps.**
- **The environment is a body.** A wall has infinite mass, so the ledger must allow the environment as a sink.
- **Touching bodies need separating**: the still balls from the moving ones (easy, since only the moving ones move).
- **Area as mass** assumes equal density and depth.
- **Impact blur.** Motion blur is worst exactly at the impact.

### Results: step 3.1, the free first look (2026-09-30)

**A correction to the prediction.** Step 3.1 pre-registered the chord's miss for "linear". The ladder's `linear`
is libplacebo's plain linear BLEND, a cross-fade with no motion (bench.sh). It ghosts on every frame alike and has
no corner to cut. The chord-following interpolator is the family's two-frame bidirectional shader. The formula
v_n x min(tau, 1 - tau) belongs to it, with the caveat that the variational-propagated recommendation is not a pure
chord either.

**The effect is there, and it is large.** The master tier kept each scene's per-frame PSNR (24 -> 60, against the
truth) for every shader, but not the pictures. The wall hits are exact in the scene's closed form (masters.py's
`trajectory`). `tests/probes/energy/impactdips.py` bins each output frame by its distance to the nearest hit, in
source frames:

    median PSNR-Y (dB)        within 0.5   0.5-1    1-2    beyond 2    dip
    bounce-constant  rec (metal)    42.50   46.62   50.86    51.49    -8.99
                     rec (placebo)  42.42   46.56   50.24    50.80    -8.38
                     quad (metal)   43.92   45.89   49.42    50.48    -6.56
                     hold           32.33   32.06   32.37    32.30    +0.03
                     linear blend   37.41   38.48   38.34    37.90    -0.49
    bounce-gravity   rec (metal)    41.32   50.99   53.61    55.39   -14.07
                     quad (metal)   43.84   47.31   54.45    54.45   -10.61
                     linear blend   41.23   38.63   41.82    39.90    +1.33
    bounce-masses    rec (metal)    44.25   48.44   50.92    52.13    -7.88
    bounce-hardjerk  rec (metal)    51.26   53.82   56.51    56.24    -4.98

(rec = bidirectional-interpolation-variational-propagated; quint matches quad to 0.1 dB; the full table is the
script's output on `np-scratch/ladder2/batch1/textured`.)

- **The impact frames are the family's worst, by 4 to 14 dB.** Hold and the blend do not dip, because they are
  equally poor everywhere.
- **Gravity dips most.** The trajectory folds hardest there: the vertical velocity reverses at its largest.
- **The recommended two-frame shader dips more than the four- and five-frame ones** on constant speed and gravity
  (-9 and -14 against -6.5 and -10.6). The wider window sees the fold coming.
- **Metal and libplacebo agree** within about 1 dB.
- **What the dip costs.** The frames within half a source frame of a hit are only about 4 percent of the clip, so the
  whole-clip average hides the dip. It is still a visible artefact at every bounce, in every piece of sport or play
  footage.
- **What it justifies.** The render for the miss distance, the step's real measure, is now worth spending. The
  prior art (split at the impact, fit each side, intersect) gives a known method aimed at exactly these frames.

### Pre-registered: 3.1, the miss distance (2026-09-30, before the render)

`tests/probes/energy/corner.py`:
- **What it renders:** `bounce-constant` and `bounce-gravity` on the flat black ground, 240 source frames, 24 -> 60,
  through hold, the linear blend, the plain two-frame bidirectional shader (bi), the recommendation (rec) and the
  four-frame propagated shader (quad).
- **What it measures:** the box's edges in every output frame, against the closed form.
- **The chord:** the straight line between the true positions at the two source frames either side, which is what
  a pure constant-velocity two-frame interpolator draws.

The predictions:
- **P1, the control:** hold, on output frames that land exactly on a source frame, reads within 1 px of the truth.
  If not, the segmentation is wrong and nothing else counts.
- **P2:** on smooth frames (more than 2 source frames from any hit), rec and quad read within 1 px (median |error|).
- **P3:** within 0.5 source frames of a hit, bi follows the chord: its median wall-side error is within 30 percent
  of the chord's.
- **P4:** quad's median wall-side error at those frames is closer to zero than the chord's. Its window sees the
  bounce coming, which is what the PSNR dips suggested.

### Results: 3.1, the miss distance (2026-09-30)

240 source frames each, 24 -> 60; wall-side edge error at the frames within half a source frame of a hit
(negative = short of the true position, positive = beyond it); "smooth" is the median of each frame's WORST edge
error on frames more than 2 source frames from any hit.

    bounce-constant (9 hits, 22 impact frames)     median   worst short  worst beyond   smooth
      chord (the prediction's model)                -1.73      -6.21          --          --
      hold      CONTROL on source frames 0.95 px    -2.14     -11.47        +6.46        6.77
      linear blend                                  +0.42      -5.25        +6.46       10.15
      bi   (plain two-frame)                        +0.57      -3.66        +7.46        2.65
      rec  (the recommendation)                     +0.74      -3.47        +5.21        2.28
      quad (four-frame propagated)                  +0.18      -4.25        +7.46        2.02
    bounce-gravity (6 hits, 16 impact frames)
      chord                                         -2.48      -5.71          --          --
      hold      CONTROL on source frames 0.94 px    -1.12     -14.42        +4.58        4.64
      bi                                            +1.27      -5.04        +8.58        2.76
      rec                                           -1.18      -4.13        +4.58        1.60
      quad                                          +0.78      -5.04        +4.72        1.88

**Against the predictions.**
- **P1 PASSED.** The segmentation is within 1 px on exact frames, so the instrument holds.
- **P2 MISSED.** Smooth frames read 1.6-2.3 px, not under 1. The metric is strict (each frame's worst edge, from a
  threshold that faint ghosts also cross); the family is within about 2 px of the true edges away from impacts.
- **P3 MISSED, and that is the finding.** The plain two-frame shader does NOT follow the chord. The chord falls
  1.7-2.5 px short in the median. The shader lands +0.6 to +1.3 px beyond, with worst cases 3.5-5 px short and
  4.6-8.6 px beyond.
- **P4 PASSED trivially.** No shader behaves like the chord, so being closer to zero than it says little.

**So the family does not cut the corner, and the 4-14 dB impact dips are not a position error.** Seen on the four
frames around the first bounce (`np-scratch/energy/corner/bounce-constant/compare-73-76.png`, and `diff-73-76.png`
amplified 8x), the recommendation's error is in two places:
1. **A one-pixel outline round the whole box:** the box drawn about a pixel off, consistent with the medians above.
2. **A bright blob at the contact edge.** The box's texture is smeared into the wall where it touches it, a wavy
   band the truth does not have.

The frame that lands almost on a source frame is nearly clean. The damage is at the CONTACT, where the motions
before and after the impact meet inside one interval. That is exactly where the prior art's method acts (split at
the impact, fit each side, intersect).

**What follows for 3.2.** The impact placer's first job is not to move the box (it is within a pixel or two). It
is to stop the contact region drawing from a flow that averages two motions: each side should be drawn from the
source frame on its own side of the impact. The measure for 3.2 is therefore the contact region's error (the
difference image's blob), not the edge position. A template-registration metric (the true box, shifted to its
best fit, and the residual after the fit) would split "where" from "how damaged" properly; the bounding box
conflates them.

### Pre-registered: 3.2, the impact placer prototype (2026-09-30, before it ran)

`tests/probes/energy/placer.py`, offline, on `bounce-constant`. It uses only what an interpolator has: the source
frames, and the field's own velocity (read_view 4, the four-frame propagated shader, N:N). The closed form scores it
and nothing else.
1. The box's centre in each source frame, by segmentation.
2. An impact lies in [k, k+1] where the frame-to-frame displacement's normal component reverses.
3. The velocity before comes from the field at k - 1, and after from k + 2, both clear of the impact.
4. The two lines intersect at the impact time tau.
5. Each output frame in (k, k+1) is drawn from the source frame on its own side of tau, shifted by that side's
   velocity, and quantised to 8 bits as the shaders' pipeline is.

Scored as PSNR-Y against the truth on the output frames within half a source frame of a hit, beside the
recommendation's and the four-frame shader's own frames. The control: hold on exact source frames.

The predictions:
- **Q1:** tau is found within 0.1 source frames of the closed form's hit.
- **Q2:** the placed impact frames recover most of the dip, to within 3 dB of the shaders' smooth-frame level (the
  4-14 dB dips of the first look).
- **Q3:** the placed frames beat both shaders at every impact frame.

### Results: 3.2, the impact placer prototype (2026-09-30)

`tests/probes/energy/placer.py` on `bounce-constant`: 96 source frames, 3 wall hits, 24 -> 60, the four-frame
field's velocities. Three runs, two of them fixing the probe; each fix is commented in the script:
- **First run:** the reversal rule also fired in the interval AFTER each impact, with its tau clamped to the
  boundary. That cost one frame. The placed frames were also quantised by hand and read 69 dB on exact frames,
  against 56.7 through the real path.
- **Second run:** through swscale's round trip, which put the placer 6.5 dB behind on the path alone.
- **Third run:** through libplacebo like the shaders' frames. This is the fair one:

    impact found   tau      closed form   error
    [29,30] y      29.870   29.886        -0.016
    [40,41] x      40.785   40.766        +0.019
    [77,78] y      77.680   77.667        +0.013

    out frame   t       placed   rec     quad    (PSNR-Y dB against the truth)
     74        29.60    45.42    35.25   36.32
     75        30.00    62.69    63.15   63.15   <- an exact source frame: every method shows the source
    101        40.40    46.87    34.81   36.56
    102        40.80    53.57    32.39   33.01
    103        41.20    51.89    50.31   41.17
    193        77.20    51.68    36.32   39.54
    194        77.60    51.59    30.80   32.09
    195        78.00    62.71    63.17   63.17   <- exact
    median              51.78    35.78   38.05   (smooth frames: rec 47.90, quad 46.68; hold's control 56.66)

**Against the predictions.**
- **Q1 PASSED:** tau within 0.02 source frames on all three hits.
- **Q2 PASSED, and more:** the placed impact frames read 51.8 dB, ABOVE the shaders' own smooth-frame level (47.9),
  so the whole dip is recovered.
- **Q3 MISSED as worded, 6 of 8.** The two exceptions are the exact source frames, near-ties (0.5 dB, the input
  path). On all six frames between a source frame and the impact, the placer beats both shaders, by 1.6 to 21 dB.

**What it means, and its limit.** Splitting at the impact and drawing each side from its own source frame lifts a
bounce's impact frames by about 15 dB on this scene. The method is the prior art's (fit each side, intersect), fed
by the family's own field, and the field's velocities were good enough to place the impact within 0.02 frames.

But this is the easiest case for a placer: one rigid body, one translation per side, a black ground that
segments itself. It is an UPPER BOUND on what is at stake at a rigid bounce. It is not a measure of what a
per-pixel shader version would recover on real content (many bodies, a textured ground, occlusion, deformation).
That version is the design question:
- a one-sided derivative mode, triggered where the jerk spikes;
- for each output pixel, drawn from the source frame on its own side of the impact.

It should be tested first on the textured-ground masters (`batch1/textured`), where the contact smear was measured,
and then on real footage.

**A fourth run, on the equal-footing scoring path (2026-09-30 late evening, the Intel Mac).** 2.5 found that this
path handicapped a probe's own frames: they were placed from the 16-bit source and then pushed through an 8-bit
round trip, while the shaders blend two 8-bit frames in float and pay less. `placer.py` now gives every method the
same 8-bit frames the shader receives and reads the shaders at 16 bits (PLACER_PATH=legacy reproduces the third
run). The control: rec on exact source frames equals its 8-bit input at 84.8 dB. **The result stands:** placed
51.83 dB median on the impact frames against rec 35.76 and quad 37.99 (the third run: 51.78, 35.78, 38.05), and the
placer beats both on the same 6 of 8. On a black ground the old path's handicap was negligible.

### Pre-registered: 3.3-3.4, body-to-body collisions and the momentum ledger (2026-09-30, before they ran)

`tests/probes/energy/collide.py`, run on the NAS's Arc (a single run is exact there).
- **The scenes:** sliding textured discs (pucks, curling stones: no roll) on black, 1280x720, 24 fps, every contact
  exact from the laws:
  - `pair`: an equal disc hits one at rest; the mover stops and the target leaves at the same speed;
  - `cradle5`: one disc hits four resting touching discs; the fifth leaves, and the middle three NEVER move;
  - `unequal`: masses as areas (r 70 against r 100); the light disc rebounds at -0.342 v and the heavy one leaves at
    +0.658 v.
- **The renders:** 24 -> 60 through hold, the linear blend, the recommendation, the four-frame propagated shader and
  the Cadence default (global-cage-energy-carry), scored per frame against the truth.
- **The ledger:** the field at N:N (the four-frame shader's raw velocity). Each disc's momentum is its area times
  its median velocity; a transfer event is momentum leaving one disc and arriving at another in the same frame.

The predictions:
- **C1:** frames within half a source frame of a contact dip as much as the wall bounces did (4-14 dB against the
  same shader's smooth frames), because the contact holds two motions.
- **C2:** in `cradle5` the middle three discs read still (|v| under 0.2 px/frame) on every frame. The ledger finds
  one transfer event per contact, from disc 1 to disc 5, across the three still discs: the "teleported momentum",
  with a speed bound of 480 px in one frame.
- **C3:** in `unequal` the ledger's total momentum is conserved across the contact within 10 percent (the field's
  velocity accuracy).

### Results: 3.3-3.4, body-to-body collisions and the momentum ledger (2026-09-30, on the Arc)

Picture scores, PSNR-Y dB: the median of the frames within 0.5 source frames of the contact (2 per scene) against
the frames more than 2 away.

    scene     shader                  contact   smooth    dip
    pair      rec                     35.73     46.80    -11.07
              quad                    37.13     46.45     -9.32
              carry (Cadence 1.0.3)   35.71     46.92    -11.21
    unequal   rec                     36.59     48.91    -12.32
              quad                    38.07     48.61    -10.54
              carry                   36.58     49.05    -12.47
    cradle5   rec                     47.63     50.48     -2.86
              quad                    44.34     50.56     -6.22
              carry                   48.45     50.83     -2.37
    (hold and the linear blend do not dip: they are equally poor everywhere)

**C1 PASSED for pair and unequal** (dips of 9-12.5 dB, as large as the wall bounces). **Cradle5 dips far less for
rec and carry (2.4-2.9 dB).** Its contacts are gentler for the family: disc 1 stops against a disc that never moves,
and disc 5 starts from rest, with no region where two opposed motions meet. The four-frame shader is the exception
there (-6.2).

**The ledger** (the field's median velocity per disc times its area, the four-frame shader at N:N):
- **C2 PASSED:**
  - at k = 15 the ledger records ONE transfer, disc 1 -> disc 5, across the three still discs, 480 px apart in one
    frame. That is the teleported momentum, with its speed bound, measured by the field alone.
  - Over frames 3-56 the middle discs read EXACTLY 0.000 px/frame. The only exceptions are the clip's first frame
    (7.8 at k = 0) and a spurious event at k = 59, where the four-frame window runs off the clip; the edges are now
    excluded.
- **C3 PASSED:** the total momentum is conserved across every contact: pair -0.4 percent, cradle5 +1.1, unequal +1.9
  (the light disc's rebound and the heavy disc's departure both read).
- **The first NAS run of the ledger was INVALID** (a limited-range read path on Linux). It was caught by the values,
  not by an alarm, and rerun with RGB input and the zero-level alarm (c646384). The picture scores were unaffected.

### Pre-registered: 3.3b, collisions on a textured ground (2026-09-30, before the run)

`collide.py` with a textured ground (the masters' dim five-sine ground) and `rows3`: three independent equal pairs
stacked at y = 160, 360, 560, whose contacts fall at 26.2, 26.5 and 26.8 source frames. That gives three contact
phases and three times the contact frames of `pair`. On the Arc.
- **C1b:** the contact dips on the textured ground are at least as deep as on black (-9 to -12 dB for rec, quad and
  carry). A textured ground adds a third motion (still) beside the two opposed ones.
- **C2b:** the ledger finds three transfers, one per row. The still textured ground reads |v| under 0.05 px/frame
  away from the discs.

### Results: 3.3b, collisions on a textured ground (2026-09-30, on the Arc)

    scene (textured ground)   rec dip   quad dip   carry dip   ledger
    pair                      -10.38     -8.75     -10.43      1 transfer; momentum -0.0 %
    unequal                   -10.17     -9.04     -10.16      1 transfer; momentum +2.6 %
    cradle5                    -1.28     -5.39      -1.05      1 transfer, 1 -> 5 across 3 discs reading 0.000; +0.5 %
    rows3 (3 pairs, contacts at 26.2 / 26.5 / 26.8)
                               -5.48     -5.63      -5.39      3 transfers, one per row; +0.3 %
    the still ground away from the discs: median |u| 0.0005 px/frame on every scene

- **C1b MISSED, narrowly:** a textured ground does NOT deepen the contact dip (pair -10.4 against -11.1 on black,
  unequal -10.2 against -12.3). The smear is the two opposed motions, not the third, still one.
- **The contact's phase matters.** With contacts at 0.2, 0.5 and 0.8 of an interval (rows3), the dip is half as deep
  (-5.5), because output frames near a source frame suffer little.
- **C2b PASSED:** three transfers found, one per row. The textured ground reads 0.0005 px/frame. Momentum is
  conserved within 2.6 percent everywhere.

### Results: 2.4 in simulation, the pool shot (2026-09-30, the reading on the Arc)

    shot   P1 departure (read / truth)   P2 slip: before / sliding / rolling (truth)        transition (truth)   P3 direction while sliding
    roll   33.4 / 33.7 deg                1.75 (0) / 3.61 (3.08) / 0.85 (0)                   k 37 (39.8)          49 59 51 54 55 54 49 46 50 45 46 44 43 34 42
                                                                                                                   (truth 54 -> 36, smoothly)
    stun   57.9 / 60.0 deg                7.96 (8.00) / 0.80 (1.55) / 0.58 (0)                k 27 (31.4)          58 63 60 60 60 62 61 (truth 60)

(The M5 read the same within its wander: roll 34.5 degrees, stun 57.7.)
- **P1:** roll PASSED (0.3 degrees); stun MISSED by 0.1 (2.1 degrees).
- **P2:**
  - Roll PASSED: the transition is 2.8 frames early, and the sliding slip reads about 4x the rolling one.
  - Stun MISSED: 4.4 frames early. Its sliding slip (1.55 px/frame) sits inside the fit's bias floor (0.6-1.8 px/frame
    on a rolling ball: the top-down ill-conditioning of 2.3).
  - The large slip, the stun ball arriving without spin (8.00), reads 7.96.
- **P3 PASSED in shape:** the roll's direction turns from about 55 towards 42 as the truth turns 54 -> 36, with about
  5 degrees of per-frame noise. The stun's holds at 58-63 against 60.

**What it says about hidden spin in a real pool shot:**
- The departure angle, the visible consequence, reads within about 2 degrees, and it separates a rolling cue ball
  (33.7) from a stunned one (60) with a wide margin. The prior art's inference route works on our field.
- The spin itself, read from the ball's own flow from above, is readable only when the slip is large (above about
  2 px/frame at this scale).
- A real shot needs a high-speed camera to bring the speeds within reach. Pool cameras usually look straight down,
  exactly where spin is ill-conditioned, so the side view, or the departure angle, is the better witness.

### Pre-registered: 3.6, an impact census of real films (2026-09-30 evening, before it ran)

How often does the contact smear's cause, a local velocity reversal inside one frame interval, occur in real
content? That is what the warm lead (the impact placer as a shader) is worth. `tests/probes/energy/census.py`:
- **Where:** on the NAS, where the footage lives (mounted read-only into the container; numbers only).
- **The field:** the four-frame propagated shader's raw velocity at N:N, RGB in, 1280 wide.
- **An event** at frame k: at least 16 contiguous 8-px cells whose motion at k - 1 and at k + 2 (the frames clear of
  a straddling window) point in opposite directions, each faster than 2 px/frame, the change over 4 px/frame.
  Reversals over 20 percent of the frame are counted apart as global (camera shake); frames near a cut are excluded.
- **The controls, first, and a hard stop if they fail:** `bounce-constant` must fire at its wall hits, while
  `static` and `spin-constant` must never fire.
- **The prediction (genuinely uncertain):** local reversals in 0.5-5 percent of live-action frames, and more in
  animation, where motion is snappier.

### 3.6, the census's instrument (2026-09-30 evening): three tries to pass its own controls

The controls stopped the census twice before it touched a film, which is what they are for:
- **Opposite motion at k - 1 and k + 2 alone** fired on 51 of 93 frames of `bounce-constant`, at the box's LEADING
  edge. Cells going from background noise to the box's speed look like a reversal.
- **Adding SYMMETRY** (comparable speeds either side, |ua + ub| < 0.5 (ub - ua), which still admits a bounce with
  restitution down to about 0.4) left 16 events. Among them were small false ones (17-28 cells, against 490-1000 for
  a real hit), and the clip's edges.
- **Adding PERSISTENCE** (k - 2 like k - 1, k + 3 like k + 2: steady motion either side), with the clip's first and
  last 4 frames out, PASSED. `bounce-constant` fires on exactly 28-30, 39-41 and 76-78 (three frames around each hit
  at 29.89, 40.77, 77.67) and nowhere else; `static` and `spin-constant` never fire.

A real impact shows on three consecutive frames: the window straddles it.

### Pre-registered: 3.6b, do the census's flagged frames MATTER on real footage? (2026-09-30 evening, before it ran)

The census has no ground truth on real films, and its first four films flagged far more than predicted: 22 percent
of frames raw, about 10 percent in short runs, plus long runs. The self-supervised test gives real ground truth
without a camera:
- keep a film extract's EVEN frames (12 fps from 24);
- interpolate the odd frames back with the Cadence default (global-cage-energy-carry) through libplacebo;
- score each against the REAL odd frame, PSNR-Y;
- label an odd frame n as a reversal frame when the census (on the full 24 fps field) flagged n - 1 or n.

The predictions:
- **H1:** reversal-labelled odd frames score at least 3 dB below the unlabelled ones (median), on most films.
- **H2:** frames in the long runs (oscillation or alias) score below the unlabelled ones too, but less than the
  short-run (impact-like) frames.

### Results, preliminary: 3.6 and 3.6b on the first five sources (2026-09-30 evening, the census still running)

**The census (raw, the pre-registered number):** 22 percent of live-action frames flagged over the first four films,
about 10 percent in short runs (up to 4 frames, impact-like) and 12 percent in long runs. **The prediction (0.5-5
percent) MISSED, far low.** Local reversals are common in real footage: speech, gestures, heads and hands, not only
collisions. The long runs were read apart AFTER the first film showed them (census_runs.py).

**The half-rate test, real ground truth** (12 -> 24 fps with the Cadence default; the odd frames against the real
ones; the alignment control, even frames, at 60-64 dB on every extract):

    source (extract t0)              none           short (impact-like)   long (oscillation / alias)
    Ballad of Songbirds (6775)       51.21 (500)    39.91 (20)            30.82 (13)
    Ballad of Songbirds (5968)       42.08 (382)    33.21 (33)            26.82 (118)
    Sonic the Hedgehog (4341)        47.37 (427)    41.02 (53)            34.11 (53)
    Sonic the Hedgehog (865)         41.89 (458)    33.75 (72)            31.67 (3)
    Legally Blonde 2 (2909)          35.45 (224)    35.34 (160)           30.81 (149)
    Legally Blonde 2 (2460)          41.57 (387)    35.40 (115)           31.87 (31)
    Chicago (3366)                   30.22 (395)    27.18 (115)           27.74 (23)
    Chicago (2623)                   36.89 (266)    33.45 (98)            30.96 (169)
    Laputa (3248, 6548; anime)       26.25 / 28.17  (2 flagged frames each)
    ALL                              37.31 (4101)   33.48 (670)           30.82 (559)      median PSNR-Y dB (count)

- **H1 PASSED:** short-run frames score 3.8 dB below the unflagged ones overall, and at least 3 dB below on 8 of the 10
  extracts.
- **H2 MISSED, in an informative direction:** long-run frames are WORSE, 6.5 dB below, not between. Oscillation and
  alias hurt the family more than a single reversal.
- **The anime** has almost no flagged frames and low scores everywhere. Cel animation held for two or three frames
  breaks the half-rate test itself; this is the record's "content on twos".
- **THE CONFOUND, not yet removed:** the detector requires fast motion, and fast frames are harder anyway. The full
  run compares flagged against unflagged frames of MATCHED motion before this counts as the reversal's own cost.
- **If it survives that:** reversal frames are about a fifth of real footage and score 4-6 dB worse. That is the warm
  lead's real-world case, and it names a second target, the long runs.

### Results, interim: 3.6b's confound, motion-matched, on seven sources (2026-09-30 evening)

The half-rate test again, on the census's first seven sources (`halfrate.py` on the census log so far). Each odd
frame is also given a MOTION PROXY: the mean absolute difference between the two real frames it bridges (n - 1 and
n + 1, on a 160-wide grey thumbnail). The labels are then compared within five bands (quintiles) of that proxy:

    band (proxy)       none            short (impact-like)   long           short - none   long - none
    0.000-0.005        48.92 (1480)    43.12 (13)            -- (0)         -5.80          --
    0.005-0.012        40.69 (1412)    40.61 (80)            -- (1)         -0.08          --
    0.012-0.023        35.56 (1115)    36.38 (329)           37.82 (49)     +0.82          +2.26
    0.023-0.044        31.24 (740)     32.58 (445)           32.92 (308)    +1.34          +1.68
    0.044-0.775        23.92 (784)     26.04 (228)           28.32 (481)    +2.12          +4.40
    ALL (raw)          38.27 (5528)    33.42 (1095)          30.64 (838)    -4.85          -7.63
    median PSNR-Y dB (count)

- **The raw gap is the motion, not the reversal.** At matched motion the short-run frames are level with the
  unflagged ones (mean within-band gap -0.32 dB; -0.08 to +2.12 in the four populated bands, the quietest band's
  -5.80 resting on 13 frames). The long-run frames score BETTER (+2.78 dB mean over three bands).
- **So H1's pass above does not survive the control it was waiting for.** On real films, a frame the census
  flags is no harder for the family than any other frame moving as much.
- **Caveats of a frame-level proxy.** Cuts land in "none" in the fastest band (the census excludes them from
  events), which flatters the flagged frames there. A whole-frame difference cannot tell a local reversal from a pan
  or a flash. And the flagged cells may cover a small part of a flagged frame, so a real local cost is diluted in a
  whole-frame PSNR. The decisive form is local (3.6c, pre-registered below).
- **What it does to the warm lead:** on this evidence the impact placer's real-world case is weak. The synthetic
  upper bound (3.2, about 15 dB at a rigid bounce) stands, but real footage has not yet shown that reversals, as
  detected, cost the family anything beyond their speed. 3.6c decides.

### Pre-registered: 3.6c, the local test: flagged CELLS against unflagged cells of the same speed (2026-09-30 evening, before it ran)

`tests/probes/energy/census_local.py`, on the NAS, over the census's seeded sources and extracts:
- one pass per extract reads the four-frame field at N:N (RGB in, 1280 wide, the census's own detector and
  thresholds, with the zero-level alarm), and records for every 8-px cell at every frame whether the detector
  flags it (the cell-level event mask, before the 16-cell connectivity rule and after it);
- the half-rate interpolation of the same extract (the Cadence default, 12 -> 24) gives each odd frame's per-cell
  error against the real frame: the mean squared luma error over the cell, 1280 wide;
- **the matching variable is the cell's own speed:** the field's median |u| over the cell at n - 1 and n + 1 (the
  two real frames the odd frame bridges), in bands of 2 px/frame up to 24;
- out: frames within 3 of a cut and the clip's first and last 4 frames (the census's own rules), and cells within
  16 px of the frame border. (Corrected before it ran: the first wording put the 16 px on the cut.)

The predictions:
- **L1:** flagged cells (after connectivity) score WORSE than unflagged cells of the same speed band, by at least 2 dB
  (the cell MSE converted to PSNR, median per band, averaged over the bands holding at least 50 cells of each).
  If this fails, the census's reversals are not a cost of their own, and the warm lead loses its real-world case.
- **L2:** the gap grows with speed (it is larger in the faster half of the bands than in the slower half).
- **The control that must not move:** unflagged cells split at random into two halves score within 0.3 dB of each
  other in every band.

### Results: 3.6b final, all 20 sources, and 3.6c, the local test (2026-09-30 night, the NAS's Arc)

**3.6b at frame level, all 20 sources (40 extracts), motion-matched** (`halfrate.py` on the full census log; the
alignment control, even frames, at 60-64 dB throughout):

    band (proxy)       none            short            long           short - none   long - none
    0.000-0.003        52.81 (4320)    49.53 (16)       --             -3.28          --
    0.003-0.007        45.06 (4199)    42.03 (136)      --             -3.03          --
    0.007-0.016        39.16 (3862)    37.61 (447)      39.18 (27)     -1.55          +0.02
    0.016-0.033        34.50 (2883)    34.83 (1071)     34.35 (381)    +0.33          -0.15
    0.033-0.775        26.13 (2284)    29.27 (771)      29.63 (1281)   +3.14          +3.50
    ALL (raw)          41.41 (17548)   34.24 (2441)     30.74 (1689)   -7.17          -10.67

The interim reading holds. Raw, flagged frames are 7-11 dB worse; at matched motion the short runs average -0.88 dB
and the long runs +1.12. In the two slowest bands the short-run frames are about 3 dB worse, but those are only 152 of
2441.

**3.6c, flagged CELLS against unflagged cells of the same speed** (`census_local.py`, merged by
`census_local_merge.py`). 34 of the 40 extracts; the other six (the 25 and 29.97 fps sources) were dropped by the
alignment control and re-run separately, below. The guards held on every extract: the mask reproduced
census.detect's count on every frame, and the flagged frames matched the census log.

    cell speed px/f   flagged          unflagged (A / B)                     flagged - unflagged   A - B
    0-2               43.93 (4142)     53.18 / 53.18 (80.3 M each)           -9.25                 +0.00
    2-4               39.83 (43159)    45.43 / 45.43 (8.8 M)                 -5.60                 +0.00
    4-6               37.62 (67841)    42.88 / 42.88 (5.0 M)                 -5.25                 +0.00
    6-8               36.98 (75861)    41.48 / 41.48 (3.4 M)                 -4.50                 +0.00
    8-10              35.17 (67832)    40.18 / 40.18 (2.4 M)                 -5.00                 +0.00
    10-12             34.38 (51879)    38.62 / 38.62 (1.7 M)                 -4.25                 +0.00
    12-14             33.67 (39442)    37.52 / 37.52 (1.2 M)                 -3.85                 +0.00
    14-16             33.52 (30523)    37.12 / 37.08 (0.97 M)                -3.58                 +0.05
    16-18             33.33 (23278)    34.98 / 35.02 (0.78 M)                -1.67                 -0.05
    18-20             32.77 (16960)    33.23 / 33.33 (0.53 M)                -0.50                 -0.10
    20-22             33.38 (13162)    32.08 / 32.12 (0.39 M)                +1.27                 -0.05
    22-24             32.92 (10096)    30.77 / 30.82 (0.29 M)                +2.12                 -0.05
    median cell PSNR-Y, dB (cells)

- **L1 PASSED:** a flagged cell scores 3.34 dB below unflagged cells of the same speed, averaged over the twelve
  bands. The gap is 4-9 dB in the slow and middle bands, where most flagged cells are.
- **The gap is consistent across the footage:** 23 of the 26 extracts with enough cells are worse, 18 of them by more
  than 2 dB; the median is -2.9. The anime has too few flagged cells to score (content on twos), except one
  extract at +2.8.
- **L2 MISSED:** the gap SHRINKS with speed and turns positive above 20 px/frame. The likely reason is a selection
  effect. The detector needs steady, readable motion on both sides of a reversal, so the fast cells it flags are
  ones the field can read. The fast unflagged cells include the field's own failures near the reach (about 24
  px/frame), which pulls their median down.
- **The control HELD:** the unflagged halves agree within 0.10 dB in every band.

**All 40 extracts (the three 25 and 29.97 fps sources re-run with `-fps_mode passthrough`; the two-process pipe
had been converting each output back to the source's rate).** Their alignment controls read 60.7-62.4, and Shrek's
old .avi 40.9 and 45.2, as the single-graph half-rate run also read it: the source's frames do not pass through bit
for bit. Merged:
- **L1 PASSED, -3.06 dB** over the twelve bands.
- **L2 MISSED:** -5.23 in the slower half, -0.89 in the faster.
- **The control HELD:** within 0.05 dB.
- 28 of the 32 extracts with enough cells are worse, 20 of them by more than 2 dB; the median is -2.79.
- The three re-run sources alone read -0.95 dB, within the spread across sources (Star Wars ran from -8.4 to 0.0
  between its two extracts).

**Why the frame-level test saw nothing: dilution.** Flagged cells are 444 thousand of about 211 million scored,
0.2 percent. In a frame, a few hundred cells 3-9 dB worse do not move a whole-frame PSNR. The eye is not a
whole-frame PSNR, though: the damage sits on the hands, heads and props that reverse.

**What it means for the warm lead.** The real-world case is re-established, in its true size:
- a local reversal costs the family 3-5 dB on the cells where it happens;
- such reversals touch about 0.2 percent of real footage's cells, in roughly one live-action frame in seven;
- 3.2's placer recovers about 15 dB of such a dip on a rigid bounce.

So the placer, if it works per block on real content, is a local repair of a real, consistent, small-area fault.
The frame-level metric cannot see it, so it has to be judged per region, and by eye.

## 4. The held ball: bodies that are coupled share their acceleration

**A correction to the conversation.** The party's lit balls are HELD in the hand (the "wand" idea, in LilysParty's
ball tracker), not swung on tethers. So the tether idea (a swung ball's acceleration points along its tether to the
hand) does not apply to them. It is kept below for real poi.

**The idea.** A ball gripped in a hand moves rigidly with that hand. Its velocity and acceleration therefore track the
holding hand's, and not the other hand's. It is the cradle's inference in its simplest form: motion shared across a
coupling reveals the coupling. Perception calls it common fate: things that move together belong together (Gestalt,
Wertheimer).

**What we have.**
- The ball tracker assigns each ball to the nearest hand, with one ball per hand, and lets a ball go after 0.4 s far
  from its holder's hands.
- The recorded sessions (on the machine only) and the live session of 2026-09-29.
- The owed items this bears on:
  - the small-child "hand off" flicker;
  - the ball finder's known-truth check;
  - the rig's arm error (24-31 degrees measured, where the forearm ends at the ball).

**Next steps.**
1. *Offline on recorded sessions.* Compute smoothed velocity and acceleration for each ball and each wrist, then the
   correlation between each ball and each wrist over a sliding window (about 0.5 s). Pre-register, on the first clean
   run: when a ball is clearly held in one hand and moving, the holder's correlation is above 0.8 and the other hand's
   below 0.3.
2. *Where the nearest-hand rule and shared motion disagree.* Those moments should be the flicker and the crossing-hands
   cases. Truth: hand-labelled frames on a short clip, from the owner's own runs for anything that leaves the machine.
   The children's recordings never leave it, and no images are made from them.
3. *A combined rule, if step 2 favours it.* The nearest hand is the prior, shared motion is the evidence, and a
   hysteresis stops the assignment flipping on a single frame.
4. *Fusion.* Once the holder is known, the ball's clean track can steady the wrist's noisy one: a rigid-offset
   constraint in a small filter. The arms are the rig's largest error, and the ball sits exactly where the forearm
   ends.
5. *Real poi, if they ever appear.* The ball's centripetal acceleration, v^2 / r, points along the tether to the
   hand, and locates the hand even when it is out of view.

**Prior art to survey first.** Multi-target data association (JPDA; Bar-Shalom and Fortmann). Hand-object interaction
tracking in vision. Common fate in perception.

*2026-10-01: surveyed on 2026-09-30: [PRIOR-ART.md, "Before the energy-transfer investigations"](PRIOR-ART.md#before-the-energy-transfer-investigations-surveyed-2026-09-30); what it
changed is ["What the survey changed"](#what-the-survey-changed-2026-09-30).*

**Cost.** CPU on recorded data. No camera is needed for steps 1-3.

**What it buys.** A physics-based fix for owed LilysParty defects. The Golden Snitch uses the ball as its cursor, so
every assignment error is a missed catch.

**Traps.**
- **Still hands tell nothing.** When both hands are at rest the correlation says nothing: fall back to the nearest
  hand.
- **Whole-body motion.** Walking moves both hands together; correlate the motion relative to the torso.
- **Timing.** Vision's pose and the ball finder run at different latencies: align the timestamps first.

### Results: 4.1-4.2, the held ball on the live session (2026-09-30)

`tests/probes/energy/heldball.py`:
- **The data:** the two recorded sessions of the 2026-09-29 evening. The recorder's frames give the wrists at ~30 Hz;
  the live lab's telemetry gives the balls at 10 Hz. Numbers only: no picture read or written, and the data stays on
  the machine.
- **The clock check:** the offset between the two clocks is found as the one at which the balls sit closest to a
  wrist of their child.
- **Per moving ball:** one-second windows (speed RMS above 150 px/s), and the vector correlation of the ball's
  velocity with each wrist of that child.

    session   windows   holder r (median, p25)   other r (median, p75)   rel. speed holder/other   r>0.8 & <0.3
    18:36       93          0.95  (0.93)             -0.08  (0.15)            0.38 / 1.03              80 of 93
    19:56       18          0.10  (-0.04)            -0.13  (0.23)            1.01 / 1.00               0 of 18

**The 18:36 session: the prediction PASSED** (80 of 93 windows).
- The clock offset is +0.10 s, with balls a median 75 px from the nearest wrist: in the hand, a little beyond the
  wrist point.
- A held ball moves with its holder's hand at r = 0.95. The other hand is unrelated (-0.08).
- The three answers to "which hand" agree almost always: the tracker with shared motion in 92 of 93 windows, the
  nearest wrist with it in 91 of 93. Where one child held one ball in view, distance was already right, and shared
  motion confirms it.

**The 19:56 session: no hand of the tracked child moves with the ball.**
- Only one child was tracked (one track id in 33 s).
- At no clock offset in +-3 s do the ball sightings come near that child's wrists: a median of at least 117 px.
- Neither hand correlates (0.10, -0.13), and the two rules disagree with each other in 8 of 18 windows.
- That is what a ball held by someone the tracker did NOT see would look like, credited to the nearest tracked
  hand. Shared motion flags it, where distance cannot. It is a hypothesis: the session recorded no picture, and one
  would not be looked at for this anyway.

**What it gives the app (4.3):**
- Shared motion over a second is a strong, cheap confirmation of the holder when it is there.
- Its ABSENCE is a new signal: "this ball is not moving with any tracked hand", so do not credit it to one.
- Both need the ball moving. A still ball falls back to the nearest hand.

## 5. Seeing the cradle's middle

**The idea.** Each collision at 1 m/s moves the middle balls a few tens of micrometres, about a third of a pixel on a
phone at 1080p, for well under a millisecond. That gives two separate targets:
- **the step:** the net displacement, which persists;
- **the pulse:** too fast for any phone camera.

**What we have.**
- The small-flow floor measured as a curve (the rolling wheel: 87 percent at 1.6 px/frame).
- The snap finding: on a textured body in rigid motion, the estimator's sub-pixel bias is phase-locked and travels
  with the body, so it cancels in differences rather than adding. A step on a textured ball may therefore read better
  than an independent-noise model predicts.
- Cadence's audio-video timing machinery.

**Next steps.**
1. *A synthetic threshold sweep first.* A still textured ball steps by s px in one frame, with its neighbours still,
   for s = 0.05, 0.1, 0.2, 0.3, 0.5 and 1.0. Where does the step clear the floor? Pre-register before running: the
   threshold lies between 0.2 and 0.5 px.
2. *A phase-based method on the same sweep*: the complex steerable pyramid's phase, as motion magnification uses it
   (Wadhwa et al. 2013). Compare its sensitivity against the block match at each step size. This is a
   literature-first import, not a new design.
3. *The sound.* A phone microphone samples at 48 kHz, 21 us a sample: 800 times finer than 60 fps video, and fine
   enough to resolve the ~80 us contacts. A real cradle's clack is several contacts in quick succession, because the
   balls are not perfectly touching, and the audio may separate them. Pre-register the click train's spacing against
   the measured gaps.
4. *Fusion: the audio says when, the video says where.* The impact's sub-frame time from the sound could feed the
   impact placer of investigation 3.
   - This is a measurement-rig idea, not a player feature: film sound effects are often added in post and are not
     reliably in sync with the picture.
5. *The real rig.* A desk cradle, a tripod, the phone at 240 fps, high-contrast marks on the middle balls. Measure:
   - the step per collision;
   - its pattern over repeated swings;
   - the balls' relative motion damping out over a long clip, into the in-phase swing (Hutzler et al.: viscoelastic
     losses in the impacts), measured as a decay rate.
6. *Parked: photoelastic discs* (Majmudar and Behringer 2005), which show the force chains as fringes under polarised
   light. They need birefringent material and polarisers: a party-app demo more than an instrument.

**Prior art to survey first.**
- The cradle: Herrmann and Seitz 1982; Hutzler et al. 2004.
- Solitary waves in bead chains: Nesterenko; Coste, Falcon and Fauve 1997.
- Seeing small motions in video:
  - Eulerian video magnification (Wu et al. 2012);
  - phase-based motion processing (Wadhwa et al. 2013);
  - the visual microphone (Davis et al. 2014) and visual vibrometry (Davis et al. 2015).

*2026-10-01: surveyed on 2026-09-30: [PRIOR-ART.md, "Before the energy-transfer investigations"](PRIOR-ART.md#before-the-energy-transfer-investigations-surveyed-2026-09-30); what it
changed is ["What the survey changed"](#what-the-survey-changed-2026-09-30).*

**Cost.** Steps 1-2 are a small render plus CPU. Steps 3 and 5 need the phone and a cradle, an afternoon.

**What it buys.** The field's sub-pixel detection threshold, measured on a step, which no ladder case isolates; and a
direct answer to the owner's question on the object that raised it.

**Traps.**
- **The step is the size of the floor.** It is about the size of the estimator's own sub-pixel bias (the Metal
  demo's measured 0.52 px acceleration floor on a static scene): a still ball's reading may wander by as much as the
  step.
- **Physical noise.** Table vibration and air currents move the balls; the cradle's frame flexes.
- **Compression.** Phone video compression smears sub-pixel detail: record at the highest bit rate available.

### Results: 5.1, the one-frame step sweep (2026-09-30)

`tests/probes/energy/substep.py`:
- **The scene:** two 300x300 squares of the masters' five-sine texture on black. The mover steps s px right at frame
  24; the control never moves. The texture is evaluated analytically at the shifted coordinates, so a sub-pixel step
  is exact.
- **The rendering:** N:N through the four-frame propagated shader's reading, raw field (read_view 4) and pooled
  (read_view 7).
- **What is scored:** the median over each square, eroded 16 px (about 270x270).

**Without noise, no threshold exists, and the prediction's premise was wrong.** Static synthetic frames are
bit-identical, so the field reads exactly 0.000 on them and the signal-to-noise is infinite at every step. What
that run measured instead:
- **The GAIN:** the raw field reads the step at frame 23 (the forward chord) at 63 percent of s at 0.05 px, 78 at
  0.2, 83 at 0.3, 87 at 0.5 and 94 at 1 px. That is the small-flow floor again.
- **The field's sub-pixel QUANTUM, 1/32 px.** The readings are whole multiples of it: 0.032, 0.063, 5/32, 8/32,
  14/32, 30/32.
- **The pooled reading is the wrong view for one-frame events.** It barely registers a step below 0.5 px, and then
  holds it for several frames: its memory smooths time.

**With camera-like noise** (Gaussian, sigma in 8-bit levels, fresh each frame), the raw field:

    sigma   noise of the square's median   0.05 px    0.1 px    0.2 px    0.3 px    0.5 px    1 px     (S/N)
    1       0.0076 px                      4.2 YES    8.5       20.5      32.9      61.7      127
    2       0.0091                         3.4 YES    7.0       17.5      28.1      50.0      106
    4       0.0159                         2.0 no     4.0 YES    9.4      17.8      26.0       56

**The prediction (a threshold of 0.2-0.5 px) MISSED, on the good side.** On a well-textured region about 270 px
across, the field detects a one-frame step of 0.05-0.1 px, up to 4 levels of noise. What limits it:
- the 1/32 px quantum;
- a small bias under noise: static frames read -1/64 to -1/32 px.

A 25 mm ball filmed in a 15 cm frame at 1080p is about 320 px across, the same scale. So a cradle's
third-of-a-pixel middle-ball step would read at S/N 18-30. That holds only if the balls carry high-contrast marks:
chrome has no texture to match, only reflections.

**Not tested here:**
- real sensor noise, which is not white;
- compression, which smears sub-pixel detail;
- motion blur, and a rolling shutter that splits the step across rows.

Those are step 5.5's, with the real cradle.

### Pre-registered: 5.2, a phase-based estimator on the same sweep (2026-09-30, before it ran)

`tests/probes/energy/phasestep.py`, run on the Intel Mac's CPU (the pooled machines):
- **The scenes:** 5.1's (two 300x300 squares of the five-sine texture, a one-frame step of s px), with the same
  seeded noise (sigma 1, 2, 4).
- **The estimator:** the shift between consecutive frames of each square's region, by the Fourier shift theorem. A
  weighted least-squares fit of the cross-power spectrum's phase against frequency, over the bins where the
  texture has energy.
- **What it asks:** for a rigid region this is close to the best any estimator can do, so it measures how far the
  family's block match sits from that bound.

The predictions:
- **Q1:** the phase slope reads the step at 95-105 percent of s at every step size (no small-flow floor).
- **Q2:** at sigma 4 it detects a 0.05 px step at S/N above 10, five times the field's 2.0.

### Results: 5.2, the phase slope against the field (2026-09-30, on the Intel Mac's CPU)

S/N of a one-frame step on the same squares (field = 5.1's raw field; phase = the phase slope):

    sigma   0.05 px       0.1          0.2          0.3          0.5          1.0          noise of the reading
            field/phase   field/phase  field/phase  field/phase  field/phase  field/phase  field / phase (px)
    1       4.2 / 10.2    8.5 / 20.0   20.5 / 42.3  32.9 / 59.5  61.7 / 103   127 / 206    0.0076 / 0.0049
    2       3.4 / 5.6     7.0 / 10.8   17.5 / 21.6  28.1 / 31.6  50.0 / 52.2  106 / 103    0.0091 / 0.0091
    4       2.0 / 2.9     4.0 / 5.5     9.4 / 10.9  17.8 / 16.3  26.0 / 26.9  56.1 / 53.6  0.0159 / 0.0181

The phase slope's gain: 94.7-104.5 percent at every step size, against the field's 63-94 percent.

**Against the predictions.**
- **Q1 PASSED** (one cell at 94.7, 0.3 points under the band): the phase slope has no small-flow floor.
- **Q2 MISSED.** At sigma 4 the phase slope detects 0.05 px at S/N 2.9, not above 10. It is barely better than the
  field (2.0) on small steps and slightly WORSE on large ones.

**So the family's block match sits AT the bound for a rigid textured region in heavy noise, and within about 2.4x of
it in light noise.**
- The field's noise grows slower with sigma than the phase slope's (0.0076 -> 0.0159 against 0.0049 -> 0.0181): a
  robust match beats a linear fit when noise is high.
- Its losses in light noise come from its 1/32 px quantum and its small-step gain (63 percent at 0.05 px), not from
  noise.
- For the cradle's middle balls (5.5): at a third of a pixel either method reads at S/N 16-60 on a marked ball, so
  the measurement does not need a new estimator.
- The field's weak spot is steps below a tenth of a pixel in clean footage. There the quantum could be refined: a
  sub-1/32 px parabolic refinement of the match is the obvious next step, if it is ever wanted.

### Pre-registered: 5.2b, detection against region size (2026-09-30, before it ran)

The same one-frame steps, scored over square regions of 268, 128, 64 and 32 px inside the moving square. The phase
slope runs on the Intel Mac's CPU; the field is read over the same regions.
- **R1:** both estimators' noise grows roughly as 1 / side as the region shrinks (averaging), until the field's
  8-px cells dominate.
- **R2:** at 32 x 32 px, a 0.3 px step at sigma 2 is still detected (S/N above 3) by the field.

### Results: 5.2b, detection against region size (2026-09-30: the field on the Arc, the phase slope on the Intel CPU)

The field sweep ran through the portable path: RGB in, the source pre-quantised to 8-bit Y, the zero check on the
static control square. It never fired. At 268 px it agrees with the M5's earlier run (for example 4.5 against 4.2 at
0.05 px, sigma 1).

    side sg           0.05           0.1           0.2           0.3           0.5           1.0
     268  1     4.5 [  63%]    9.0 [  63%]   21.8 [  78%]   35.5 [  83%]   62.2 [  87%]  133.3 [  94%]
     268  2     3.4 [  63%]   10.3 [  94%]   19.7 [  94%]   30.0 [  94%]   49.3 [  94%]   98.7 [  94%]
     268  4     2.0 [  63%]    6.1 [  94%]   11.9 [  94%]   18.0 [  94%]   29.8 [  87%]   56.1 [  91%]
     128  1     4.1 [  63%]    8.2 [  63%]   24.2 [  94%]   32.3 [  83%]   56.6 [  87%]  120.5 [  94%]
     128  2     2.5 [  63%]    7.3 [  94%]   14.8 [  94%]   22.4 [  94%]   37.2 [  94%]   74.3 [  94%]
     128  4     1.1 [  63%]    2.2 [  63%]    5.4 [  78%]    9.4 [  94%]   15.2 [  87%]   30.3 [  91%]
      64  1     3.1 [  63%]    8.7 [  94%]   17.9 [  94%]   26.0 [  83%]   42.9 [  87%]   98.7 [  94%]
      64  2     2.9 [ 126%]    5.3 [ 125%]    9.7 [ 109%]   12.0 [  94%]   20.7 [  94%]   43.1 [  97%]
      64  4     2.4 [ 251%]    3.6 [ 187%]    4.7 [ 125%]    6.6 [ 114%]   10.0 [ 106%]   18.4 [  97%]
      32  1     2.5 [ 155%]    2.5 [  78%]    5.0 [  78%]    8.0 [  83%]   12.5 [  81%]   30.1 [  91%]
      32  2     2.3 [ 249%]    2.3 [ 124%]    2.8 [  78%]    4.7 [  83%]    7.3 [  81%]   15.7 [  91%]
      32  4     1.6 [ 312%]    1.6 [ 156%]    1.9 [  94%]    2.5 [  83%]    4.0 [  81%]    8.6 [  87%]

    side sg           0.05           0.1           0.2           0.3           0.5           1.0
     268  1    10.2 [ 100%]   20.0 [  97%]   42.3 [  98%]   59.5 [  97%]  102.7 [  97%]  206.1 [  97%]
     268  2     5.6 [ 102%]   10.8 [  99%]   21.6 [  98%]   31.6 [  97%]   52.2 [  97%]  103.4 [  97%]
     268  4     2.9 [ 104%]    5.5 [ 100%]   10.9 [  98%]   16.3 [  98%]   26.9 [  97%]   53.6 [  97%]
     128  1     7.7 [  96%]   14.6 [  92%]   31.1 [  92%]   42.4 [  90%]   74.7 [  90%]  149.1 [  90%]
     128  2     4.3 [  97%]    8.1 [  95%]   16.3 [  92%]   24.2 [  92%]   39.3 [  91%]   78.6 [  90%]
     128  4     2.3 [ 105%]    4.4 [  98%]    8.3 [  94%]   12.3 [  93%]   20.2 [  91%]   40.0 [  91%]
      64  1     1.4 [  38%]    3.9 [  53%]    8.0 [  53%]   11.5 [  52%]   20.4 [  55%]   40.6 [  55%]
      64  2     0.3 [  16%]    1.6 [  39%]    3.7 [  46%]    6.3 [  50%]   10.7 [  52%]   22.0 [  54%]
      64  4     0.1 [ -12%]    0.5 [  23%]    1.7 [  42%]    2.9 [  47%]    5.1 [  49%]   10.8 [  52%]
      32  1     0.5 [  38%]    1.5 [  53%]    2.1 [  38%]    3.1 [  38%]    5.7 [  41%]   12.0 [  44%]
      32  2     0.2 [  26%]    0.5 [  34%]    1.1 [  39%]    2.0 [  45%]    3.4 [  47%]    6.3 [  46%]
      32  4     0.2 [  52%]    0.3 [  48%]    0.6 [  42%]    1.1 [  51%]    1.6 [  45%]    3.1 [  44%]

(The field's percentages above 100 at small regions and high noise are its 1/32 px quantum on a handful of cells: a
0.05 px step read as 4/32 is "251 percent".)

**R2 PASSED:** at 32 x 32 px the field detects a 0.3 px step at sigma 2 (S/N 4.7). The phase slope cannot (2.0).

**R1 roughly PASSED for the field, not for the phase slope.**
- From 268 to 32 px the field's S/N at 0.3 px, sigma 2, falls 6.4x (30.0 -> 4.7), close to the 8.4x that pure
  averaging predicts.
- The phase slope's falls 15.8x (31.6 -> 2.0). Its Hann-windowed spectrum cannot hold the texture's longer
  wavelengths (47-173 px) in a small region, so its gain collapses to 40-55 percent at 64 px and below.

**So the order reverses with size.** On large regions the phase slope matches or slightly beats the field (5.2). On
regions of 64 px and below, the size of the marks on a ball, the family's block match is 2-3x better, because its
median over 8-px cells does not need the texture's longest wavelength to fit.

**For the cradle (5.5):** marks about 64 px across read a middle ball's third-of-a-pixel step at S/N about 12
(sigma 2), and 32 px marks at about 5. The field is the right estimator, with no new method needed.

### Pre-registered: 5.2c, a LOCAL phase estimator on the small regions (2026-09-30, before it ran)

`localphase.py`, on the Intel Mac's CPU. Horizontal complex Gabor filters (quadrature pairs, wavelengths 12, 24 and
48 px, Gaussian envelope sigma = wavelength / 2). The per-pixel phase difference between consecutive frames gives a
horizontal shift, weighted by the response amplitudes and pooled over the region: the local-phase idea of motion
magnification, as against the global phase slope (5.2b).
- **L1:** at 32 x 32 px, a 0.3 px step at sigma 2 reads at S/N above the field's 4.7, so local phase beats the block
  match where the global phase slope could not.

### Results: 5.2c, local phase on the small regions (2026-09-30, the Intel Mac's CPU)

`localphase.py`: Gabor quadrature (wavelengths 12/24/48 px). The shift is taken as the phase difference over the
LOCAL phase gradient (Fleet and Jepson), after two fixes, each commented in the script:
- using the filters' nominal frequency read a noiseless 0.3 px step at 68 percent;
- 5.1's hard square edges jump a whole column for any fractional step, which the filters' 72 px reach saw. The frames
  here have anti-aliased edges; the small regions sit 134 px inside, beyond both methods' reach.

S/N, field / global phase slope / LOCAL phase (the local method's gain in brackets):

    step 0.3 px   268 px             128 px             64 px              32 px
    sigma 1       35.5 / 59.5 / 104  32.3 / 42.4 / 53   26.0 / 11.5 / 33   8.0 / 3.1 / 19.3 (96 %)
    sigma 2       30.0 / 31.6 / 50   22.4 / 24.2 / 25   12.0 / 6.3 / 17    4.7 / 2.0 / 10.9 (94 %)
    sigma 4       18.0 / 16.3 / 26    9.4 / 12.3 / 12    6.6 / 2.9 / 8.3   2.5 / 1.1 / 5.1 (86 %)
    step 1.0 px, sigma 2, 32 px: 15.7 / 6.3 / 37.6 (98 %)
    step 0.05 px, sigma 2, 32 px: 2.3 / 0.2 / 0.9 (48 %)     <- the one regime where the field wins

- **L1 PASSED:** at 32 x 32 px a 0.3 px step at sigma 2 reads at S/N 10.9 by local phase, against the field's 4.7.
- **For steps of 0.3-1 px, local phase is the best of the three at every region size and noise level:** 1.2-2.9x the
  field, with a gain of 86-100 percent. It needs no whole wavelength in the region (unlike the global slope), and it
  has no 1/32 px quantum (unlike the field).
- **For tiny steps (0.05 px) on small regions in noise, the field keeps the edge:** its median over cells is robust
  where local phase's gain collapses (12-68 percent).
- **For the cradle (5.5):** marks of 32-64 px read a middle ball's third-of-a-pixel step at S/N 11-17 by local phase
  (sigma 2), about twice the field.
- **A LEAD for the family itself:** a phase-based sub-pixel refinement of the field's final match. The block match
  finds the integer-and-1/32 answer; a local-phase step inside the matched block would take the last fraction.
  Recorded, not designed (steps before leaps).

---

## What the survey changed (2026-09-30)

The prior art is surveyed and recorded in PRIOR-ART.md ("Before the energy-transfer investigations"). What it
changes here, per investigation:

1. **Conservation laws.**
   - Geometry, not frame rate, is what breaks a g-test on real footage: errors up to 40 percent in teaching labs.
   - Fit in the throw's plane through a homography, and timestamp each rolling-shutter row.
   - Make the unit-free two-drop ratio (t1^2 / t2^2 = h1 / h2) the primary witness: it needs no g, scale or frame
     rate.
   - Nothing was found that scores optical flow by physical constancy on real video. This direction may be new;
     PIV's uncertainty methods are the nearest neighbour and a second witness.
2. **Hidden spin.**
   - Curl sees only line-of-sight spin, which is what 2.1 and 2.2 measured (discs in the image plane). A ball's
     other spin axes need the sphere fit of step 2.3; gyrospin never shows; spin above half the frame rate aliases.
   - The pool test gets sharper. After contact the cue ball runs on a parabola for about 0.75 s, then straight
     (Alciatore). In our field that is a constant acceleration that drops to zero when it starts rolling, so
     investigations 1 and 2 meet on one clip.
3. **Impacts.**
   - Every working system splits at the impact and intersects the fits (Hawk-Eye/ITF, Tracking by Deblatting,
     FBDepth). FBDepth reaches a few milliseconds from 30 fps, and its authors state that frame interpolation cannot
     cross a collision. Step 3.1 measures that claim for our family.
   - Step 3.2's placer is the published method, so import it rather than design it. The shader-side counterpart is a
     one-sided derivative mode, triggered by a jerk spike.
   - One 24 fps frame (42 ms) sits inside the ~60-70 ms tolerance of Michotte's launching impression; two frames do
     not.
4. **The held ball.**
   - A hand and the object it holds are the textbook case where JPDA merges tracks, so do not match them as rivals
     by position.
   - They belong together while their relative velocity and acceleration stay near zero over a window. A release is
     an impulse event, as in 3.
   - Common fate from motion energy beats 40 deep flow models at grouping (Tangemann et al., 2024), which supports
     using the field itself as the grouping signal.
5. **The cradle's middle.**
   - It is an OPEN measurement: nothing was found filming the middle balls, or timing the click, at high speed.
   - The realistic sub-pixel floor for phase-based methods is about 0.01 px, and 0.001 px needed high-speed,
     controlled scenes. A third of a pixel is therefore comfortably detectable in principle; our own block-match
     floor is the question step 5.1 asks.
   - Timing by sound needs about 2.9 ms per metre of travel, plus each device's audio-video offset (about 1 ms on an
     iPhone).
   - Rolling shutter can time the impact finer than the frame rate: measure the readout time once, with a flash.

## The warm lead: the impact placer as a shader (recorded 2026-09-30, the owner's call: after the science explorations)

The prototype (3.2) worked on one rigid box on black, and knew the box from the picture. A shader has none of that:
it works pixel by pixel (block by block, in this family), on any footage. The shader version of the same idea:
1. **Find the impacts per region.** A block whose one-sided velocities before and after the interval disagree (the
   jerk spike the reading already computes) holds an impact inside that interval.
2. **Time each impact.** Intersect the block's two one-sided motions, as the prototype did, for tau.
3. **Draw each side from its own frame.** An output pixel in that block is taken from the source frame on its own
   side of tau, moved by that side's velocity, instead of the two-sided blend that smears the contact (3.1).
4. **Change nothing else.** Every block without an impact stays exactly as the family draws it now.

What it could win: about 15 dB on the impact frames of a rigid bounce (the prototype's upper bound). What it must
survive: textured grounds, several bodies, occlusion, deformation. That is why the first tests would be the textured
masters (`batch1/textured`), then the body-to-body scenes of 3.3, then real footage. It would ship as a VARIANT
behind a switch, with the full-ladder gate on the Arc, where a single run is exact.

*2026-10-01: parked for the player, nothing built (["The owner's two decisions"](#the-owners-two-decisions-2026-10-01-morning-and-the-tiers-costs)); its prior art is
[PRIOR-ART.md, "Before lead 2"](PRIOR-ART.md#before-lead-2-the-impact-mode-as-a-shader-one-source-per-pixel-chosen-by-the-side-of-tau-surveyed-2026-10-01-0405-by-a-research-subagent-read-and-checked-before-it-was-filed).*

## Suggested order (cheapest and readiest first)

1. ~~**2.1**, the energy split on `rolling.sh`~~ DONE 2026-09-30 on the field tier's existing data, with 2.2 (see the
   results under investigation 2): the prediction missed, and the lesson (noise books as energy) now binds 1, 3 and 4.
2. ~~**3.1**, corner-cutting on the bounce scenes~~ DONE 2026-09-30: the impact frames are 4-14 dB worse, and the
   damage is a smear at the contact, not a cut corner. 3.2 (the placer) now aims at the contact region.
3. ~~**1.1**, the `bounce-gravity` control~~ DONE 2026-09-30: g to 96 percent over 100 frames, +-30 percent per
   frame; jerk median ~0.05. The real throw (1.2) waits for the camera.
4. ~~**4.1-4.2**, shared motion on the party data~~ DONE 2026-09-30: r = 0.95 for the holder against -0.08 on
   the clean session; on the other, no tracked hand moves with the ball (a mis-credit shared motion can flag).
5. ~~**5.1**, the sub-pixel step sweep~~ DONE 2026-09-30: 0.05-0.1 px detectable on a large textured region up to
   4 levels of noise; the 1/32 px quantum is the floor. A marked cradle's middle balls should read.

Then, when the camera is free: 1.2-1.4 (the throw, the pendulum), 5.5 (the cradle), and 2.4 (pool, if a table is
handy). Before designing any of it, survey the prior art named in its section and record it in PRIOR-ART.md.

*2026-10-01: 1.4 and 2.4 have since run in simulation (their results are above); their camera parts remain. The prior
art was surveyed the same day ([PRIOR-ART.md](PRIOR-ART.md#before-the-energy-transfer-investigations-surveyed-2026-09-30)).*

**Done since, the evening and night of 2026-09-30 (without the camera, across the three machines):**
- 1.5 in simulation (the bounce's parabolas; the unit-free witness T^2/h to 0.5 percent; the camera recipe).
- 2.5 to 2.5d (a rigid region moved as one: a repair of 7-28 dB where the family fails, harm where it works; the
  field finds the region only on aperiodic bodies; the repair needs per-pixel motion selection).
- 3.2 re-scored on the equal-footing path (it stands).
- 3.6b final and 3.6c (a local reversal costs 3.1 dB on the cells where it happens, 0.2 percent of the picture).
- A side finding for NFRAME-LIMITS, the weave (a slow fine print puts the default BELOW the blend; the edge
  carried inward repairs it by 22-30 dB).

**What is left is building, and the order is the owner's call.** Every candidate would be a variant behind a
switch, gated on the Arc:
1. **The slow-print outline prior** (NFRAME-LIMITS, the weave). The largest measured win, +22 to +30 dB, on a case
   where the default is worse than doing nothing.
2. **The impact placer as a shader** (the warm lead). 3.2's +15 dB bound at a rigid bounce, and 3.6c's real-footage
   case: 3 dB on 0.2 percent of cells.
3. **A rigid-region repair** (2.5). 7-28 dB where the family fails, but it needs a per-pixel motion selection that
   is not yet designed.
4. **The per-level trust gate** (NFRAME-LIMITS section 8, never built). The only candidate for fast prints.

The four share one open problem: finding the region (or the block set) that one motion model governs, and drawing it
only where it beats the family pixel by pixel.

*2026-10-01: item 1 is `OUTLINE_ADOPT`, [adopted for the player](#outline_adopt-adopted-for-the-player-2026-10-01-the-4k-twin-and-the-metal-port); item 2 is parked for the player
(["The owner's two decisions"](#the-owners-two-decisions-2026-10-01-morning-and-the-tiers-costs)); item 3 is parked ([2.5e](#results-25e-lead-3s-selection-rule-the-m5-r1-and-r2-missed-the-lead-is-parked-with-its-reason)); item 4, the per-level trust gate, is
[parked](#parked-by-the-owner-2026-10-01-morning-the-per-level-trust-gate-to-return-to-within-hours). From 2.5e on, "lead 4" names the fast-print fix, built in the gate's place as `PRINT_LATTICE`.*

## The shared stage: finding the region one motion governs (begun 2026-09-30, late night)

All four candidate builds need one stage: find the pixels a single motion model governs, and draw them only where
that beats the family. By the owner's orchestration rule, it is built ONCE, frozen and versioned. Every lead's
variant then differs from the default in that lead alone, and a change to the stage bumps its version and re-runs
all four. The stages below are serial; the leads fan out only after the stage passes.

### Pre-registered: stage 0a, the instrument (before it ran)

Every probe tonight read the field from the QUAD shader and repaired the DEFAULT's output: two different shaders.
The stage must read the field of the shader it repairs. The default carries its own machine velocity
(`read_view 4`: "the two-frame family ... its warp uses one flow", decoded as the quad's is). `weavesweep.py`, with
FIELD_STEM set to the default, on the translating box at 5 and 11 px/frame:
- **I1 (calibration):** on noise the default's field reads within 0.5 px (median) at both speeds, and is not zero
  (the alarm).
- **I2 (informative, no threshold):** where the default's field locks on the weave, against the quad's (the quad
  locked at 5 and 11).

### Results: stage 0a (the M5): a confound caught, the edge cue was the quad's

    tex     v    field (the DEFAULT's read_view 4)     gross   edge ring   core     (the quad's, for comparison)
    noise   5    +4.84, median error 0.51              0.0%     1.3%        0.0%
    noise  11   +10.39, median error 0.75              0.0%     8.4%        0.0%
    weave   5   +32.00 (full scale: about 33 clipped)  90.8%    64.7%       96.8%    (quad: edge 16.4%, core 73.7%)
    weave  11   -16.75 (v - 28)                        94.5%    68.8%      100.0%    (quad: edge 67.1%, core 99.8%)

- **I1 MISSED as worded, and the field is sound:** median error 0.51 and 0.75 px, with no gross texels. The
  default's smoothed field reads speed 3-6 percent low, the scale under-read 2.1 recorded. It is not zero.
- **I2:** the default locks at the same speeds and to the same aliases as the quad. At 11 px/frame it reads v - 28.
  At 5 it reads +32.00, the machine encoding's full scale (32 px), so about 5 + 28 clipped.
- **THE CONFOUND:** at 5 px/frame the default's EDGE RING is 64.7 percent gross, where the quad's was 16.4. The
  outline cue that the weave's E1 carried inward for +22-30 dB was a property of the quad's raw matcher. The
  default's variational smoothing spreads the interior's locked vector out to the edge and erases it.
- **For the stage:** the edge and region cues must come from a RAW (unsmoothed) match, not from the default's final
  flow. Step 0b looks for one inside the default: the match before its variational and propagation stages, exposed
  as a diagnostic in a variant file, as `diagvariant.py` does for the quad. If none can be exposed, the stage
  carries its own raw matcher, and that becomes part of what every lead's variant adds.

### Pre-registered: stage 0b, why the default's own carry does not fix the weave (before it ran)

**The survey of tools found the stage half-built.** The default already carries ALIAS_CARRY (tests/alias_carry.py,
2026-09-28, the "carry" in its name):
- each 1/8-level cell's cost curve is searched over +-3 texels (+-24 px) for a RIVAL basin behind a ridge;
- cells whose margin is under ALIAS_TAU are flagged TIED;
- a semi-global min-sum at the quarter level carries each pattern's unambiguous END into its tied interior.

That is the region-level prior "the interior follows its outline", built for the half-period alias (V3 8 -> 100
percent). So the first question is why it does not engage on the weave, not how to build a new one.
`tests/probes/limb/ambiguity.py --clips` (the offline twin of the 1/8 level's flag) on the translating box
(lossless clips of the sweep's sources; the flat ground is untextured, so its textured cells are the box):
- **A1:** on the slow weave (5 px/frame) the flag fires on under 20 percent of the box's cells. The alias sits
  where the search cannot pair it as a clean rival, so the carry never engages. On noise at 5 it fires on under 2
  percent.
- **If the flag fires on most of the box instead (over 50 percent),** the carry sees the tie and fails for another
  reason: its anchors. The default's edge is locked too (stage 0a), so there is no right answer at the end to carry.

### Results: stage 0b (the M5): the carry never engages on the weave because the tie is not tight enough

    clip (the translating box)   flagged at margin < 0.05 (the carry's TAU)   < 0.15    < 0.30    textured cells
    weave, 5 px/frame            4.0%                                          14.8%     57.4%     11940
    weave, 11 px/frame           4.4%                                          15.2%     55.5%     11940
    weave, 8 px/frame (immune)   0.0%                                           0.1%      3.6%     11880
    noise, 5 px/frame            0.1%                                           0.2%      0.4%     11940

- **A1 PASSED:** at the carry's own threshold (alias_carry.py TAU = 0.05), 4 percent of the weave box is flagged
  tied, so the carry has almost nothing to carry into.
- **But the weave's interior DOES show two basins:** at a margin of 0.30, 55-57 percent of the box has a rival. The
  wrong basin wins by a margin of 0.05-0.30: a faint preference, above the tie line. The carry takes it as
  confidence and leaves the cells to it. At the immune speed there is no rival (0 percent), and on noise none.
- **Next (stage 0c), a single-constant change:** the default regenerated with the carry's TAU raised (0.05 -> 0.30).
  - Does the default's EXISTING carry then fix the slow weave?
  - What does it cost the ladder?
  - The control first: the default regenerated at TAU 0.05 must match the committed file byte for byte.

### Pre-registered: stage 0c, the default's own carry with a looser tie (before it ran)

**One constant changes:** the carry's tie threshold, 0.05 -> 0.30 (`ALIAS_TAU_CARRY`, a new override in
alias_carry.py that moves the carry alone; the prior's gate keeps 0.05).

**The control, already run:** the default regenerated by its own recipe matches the shipped file BYTE FOR BYTE. The
recipe needs a 7th argument, `bidirectional-interpolation-propagated.glsl` (the base), which the file's header
omits: a documentation gap, recorded rather than fixed, since fixing the header would change the shipped bytes.

**The variant is asserted to differ from the default only in that constant.**
- **C1:** on the slow weave (3 and 5 px/frame) the variant's box PSNR rises at least 10 dB over the default: the
  carry engages and carries the edge in.
- **C2 (no harm where there is no rival):** on noise, at the sweep's speeds, within 0.3 dB of the default.
- **C3 (the gate, if C1 and C2 pass):** the full 42-case ladder on the Arc, with the capped mean within 0.1 and no
  case down more than 1 dB.
- **If C1 fails,** the carry's ANCHORS are the problem. The ends it carries from sit in the 1/8 basins, and whether
  they hold the truth on the weave is the next measurement.

### Results: stage 0c (the M5): C1 MISSED, a looser tie changes nothing

    weave, v px/frame   the default   the variant (carry TAU 0.30)   change
     3                  20.27         20.54                          +0.27
     5                  16.23         16.23                           0.00
    11                  15.94         15.97                          +0.03
    (PSNR-Y on the box, dB; the same sources, deterministic path)

- **C1 MISSED:** loosening the carry's tie threshold six-fold does not move the weave. C2 and C3 are moot.
- **So the tie was not the only obstacle.** The pre-registered alternative is the carry's ANCHORS: the ends it
  carries from. If they hold the wrong answer on the weave, and stage 0a found the default's EDGE 65 percent locked,
  carrying them inward carries the lock.
- **Next (stage 0d), offline:** at the carry's own level, for the weave box's edge cells against its interior cells,
  whether the truth is the best basin, the rival, or neither.

### Pre-registered: stage 0d, the carry's anchors on the weave (before it ran)

`tests/probes/weave/anchors.py`, on the 1/8 level as the carry's offline twin emulates it. For the weave box's edge
cells (within 16 px of the boundary) against its interior (more than 32 px inside): is the best basin the truth or the
alias, and do the ANCHORS (textured cells with no rival or a margin of at least the carry's 0.05) hold the truth?
- **D1:** at 3 and 5 px/frame, fewer than half the edge cells' best shift is the truth. The 1/8 level aliases the
  14-px print at the edge as well, so the carry's anchors carry the lock. The quad's truthful edge at slow speeds
  (W4) then came from its FINER levels, which the carry never consults.
- **The control:** noise at 5 px/frame, where the best is the truth nearly everywhere; and the weave at the immune
  8 px/frame.

### Results: stage 0d (the M5): D1 PASSED, and the 1/8 level is confidently wrong, not tied

    clip              edge: best = truth / alias / anchors (truth among them)    interior: best = truth / alias / anchors (truth)
    weave  3          25.9% / 74.1% / 92.9% (24.7%)                               0.3% / 99.7% / 98.9% (0.2%)
    weave  5          33.5% / 66.5% / 93.3% (32.1%)                               0.2% / 99.8% / 98.6% (0.0%)
    weave 11          25.9% / 74.1% / 92.7% (24.6%)                               0.3% / 99.7% / 98.8% (0.2%)
    weave  8 immune   100 / 0 / 100 (100)                                          100 / 0 / 100 (100)
    noise  5          84.9% / 15.1% / 100 (84.9%)                                 98.1% / 1.9% / 100 (98.1%)

- **D1 PASSED:** at the carry's level the weave's edge holds the truth on a quarter to a third of its cells, and its
  anchors are mostly wrong.
- **The interior is not tied at all:** 99 percent of its cells are confident ANCHORS (margin at least 0.05), and
  99.7 percent hold the alias. The carry's premise, a tied interior with truthful ends, is absent at 1/8. That is
  why no threshold could help (0c).
- **The truth at slow speeds lives only at the FINER levels.** The 1/4 level's 4-px texels resolve a 14-px print
  unaliased, and the quad's truthful edge (W4) must come from there.
- **The default already holds the finer-level answer's machinery:** QZERO_MOIRE (NFRAME-LIMITS, the cage). The quarter
  level refines from ZERO where the 1/8 level sees a Moire, and the zero descent wins as the smaller of two good
  matches with a ridge between. At 5 px/frame that descent should find the truth (1.25 quarter texels) against the
  alias (33 px).
- **Next (stage 0e):** does that gate fire on the weave, and if it does, why does the lock survive? Like the carry,
  it is built and not engaging.

### Pre-registered: stage 0e, QZERO_MOIRE's gate forced open (before it ran)

**One constant:** the Moire score above which the quarter level runs its zero descent, 0.25 -> 0.0 (always).
`QZERO_MOIRE_MIN` is a new override. The control: the default regenerates byte-identical with it unset.
- **Z1:** with the gate forced open, the slow weave (3 and 5 px/frame) rises at least 10 dB. The obstacle was then
  DETECTION: the 14-px print's Moire score sits near the 0.25 line.
- **If Z1 fails,** the competition rejects the zero descent: both matches good, a ridge, and the smaller motion. On
  a print whose true motion (5 px) is a GOOD match and whose alias (33 px) is too, the smaller-motion rule should
  pick the truth, so a failure would point at the ridge or goodness thresholds, or at the search radius.

### Results: stage 0e (the M5): Z1 MISSED; the zero descent, even forced open, leaves the weave unchanged

    v px/frame   weave: default / gate forced open     noise: default / gate forced open
     3           20.27 / 20.27                         51.06 / 51.06
     5           16.23 / 16.23                         43.37 / 43.37
    11           15.94 / 15.92                         48.44 / 48.44

- **The counterfactual first:** both 0c's and 0e's variants were what ran. The files the sweep loaded hash to the
  variant files, differ from the default, and carry the changed constant.
- **Z1 MISSED:** with the Moire gate forced open everywhere, the slow weave does not move by a hundredth. So the
  obstacle is not detection. Either the competition never passes on the weave (both matches good, a ridge, the
  smaller motion), or a LATER stage erases the zero descent's answer. The candidates are the quarter level's carry
  and semi-global pick, the variational iterations (Q = 8), and the half level seeded from the quarter.
- **The stage's barrier holds.** No lead has been spawned; stage 0 has not passed. Two built mechanisms (the carry,
  the zero descent) exist for this case and neither engages. Why is the stage's next question.
- **Next (stage 0f):** a diagnostic variant that exposes the quarter level's flow at each step: after its refine,
  after the zero descent, after the carry, after the variational iterations. Where does the truth appear, and where
  is it lost?

### Results: stage 0f (the M5): the default's flow, stage by stage, on the slow weave

`tests/probes/weave/flowtap.py` builds a diagnostic copy whose machine reading shows a chosen flow texture right
after a chosen pass. The control: tapping the final flow reproduces the default's own reading exactly (noise +4.84,
weave +32.00, edge 64.7, core 96.8). Each tap differs from the default by the same 15 lines.

    stage (A->B)                                  weave 3: edge / core     weave 5: edge / core     noise 5: edge / core
    T0  1/8 after propagation and data check      68.7% / 90.3%            76.7% / 98.3%            41.0% / 0.1%
    T1  quarter refine (with the zero descent)    17.2% / 78.5%            57.7% / 95.3%             9.8% / 0.1%
    T2  after the carry's pick                    23.8% / 80.1%            59.5% / 95.4%             9.8% / 0.1%
    T3  after the quarter variational (8 iters)   29.9% / 89.0%            68.5% / 97.7%             3.9% / 0.0%
    T4  half-level refine                         16.3% / 83.3%            63.7% / 96.8%             1.6% / 0.0%
    (gross: more than 2 px from the truth; the edge ring 0-16 px inside the box, the core 32+ px inside)

**What the taps say.**
1. **The lock is born at the coarse levels, and nothing later undoes it.** The interior is 90-98 percent wrong by the
   1/8 level (T0), and stays wrong through every stage.
2. **The quarter refine RECOVERS the edge at 3 px/frame** (68.7 -> 17.2 percent) but only partly at 5 (57.7). The
   quad recovered it at 5 too (W4: 16.4), so the default's quarter search is the weaker one there.
3. **The variational iterations push the interior's lock OUTWARD** (the edge 23.8 -> 29.9 and 59.5 -> 68.5
   percent): smoothing carries the majority, and the majority is the lock.
4. **The carry cannot offer the truth.** A rival must lie at least 2 coarse texels (16 px) from the best, and a slow
   print's truth sits about 2 texels from its alias (periods 14-28 px). Its interior's two hypotheses are the alias
   and something else.

**The design the stage needs.** It must act at or after the quarter level, where the edge is right. It must let a
region's OUTLINE override its interior even where the interior is CONFIDENT, not only where it is tied. And it must
come before the variational smoothing, or be protected from it. In one sentence: a region-level consistency test at
the quarter level, "inside a closed outline that moves as one, a confident interior that disagrees with the outline
is an alias". The rigid-region, placer and weave leads all consume that one mechanism.

**Where the orchestration stands.** Stage 0 has not passed, and no lead has been spawned. What stage 0 has produced
is the mechanism's specification, measured. The next step is to build that one mechanism, offline first, then as a
switch in the generator.

### The specification has a name: the survey's UNWRAPPING form (2026-09-30, late night)

PRIOR-ART.md's periodic-interior survey (2026-09-27) named two forms for the leap:
- **the SGM form**, built as the carry (0b-0f show it cannot reach a slow print);
- **the UNWRAPPING form, never built:** "jump-flood a reference from the anchor cells ... then lift each flagged cell
  as d = w + P round((r - w) / P)".

That is stage 0f's specification almost word for word. It corrects CONFIDENT aliases, not only ties. It needs a
reliable reference r, which the quarter level's outline supplies at slow speeds (T1). And it needs the print's
period P, the weave's lattice of (28, 0), (0, 28) and (14, 14). At 5 px/frame, w = +33 and r = +5: r - w = -28, one
period, and the lift gives +5. The survey's warning holds: vector-only validation "passes a coherent wrong alias".
The lift escapes it because its reference comes from a different measurement, the outline.

### Pre-registered: stage 1a, the unwrapping form offline (before it ran)

`tests/probes/weave/unwrap.py`, on the default's own quarter-level flow after the refine (T1's tap), per 1/8 cell:
- **the region:** the moving cells' connected component; the reference r is the median flow of its edge ring;
- **the period lattice:** from the region's texture, the two strongest non-zero peaks of the source frame's
  autocorrelation over the region;
- **the lift:** each cell's w moved by the lattice vector nearest r - w, only where that vector is non-zero AND the
  lifted d matches the frames at least as well as w (a 5 x 5 SAD test). An independent motion is never a period
  away, and the SAD test refuses it.

The predictions:
- **U1:** on the slow weave (3 and 5 px/frame), the core's gross falls from 78-95 percent to under 20 percent.
- **U2:** on noise no period is found, nothing is lifted, and the core's gross stays under 1 percent.
- **U3 (the control that must not move):** a noise patch inside the weave box moving at its own velocity (the box at
  +5, the patch at -4) keeps its own motion: under 10 percent of its cells lifted.

### Results: stage 1a (the M5): the unwrapping form works offline, short of its line

    case                        core gross before -> after   ring gross before -> after   lattice found   the patch (U3)
    weave  3 px/frame           70.0% -> 44.0%               17.3% -> 11.4%               36 of 36        --
    weave  5                    88.8% -> 22.3%               44.3% -> 13.6%               36 of 36        --
    noise  5                     0.6% ->  0.6%               15.4% -> 15.1%               36 of 36 (!)    --
    weave  5 + a noise patch    70.1% -> 22.2%               38.8% -> 11.9%               36 of 36        0.1% lifted; error 1.16 -> 1.16 px
    weave 11 (fast)             98.5% -> 97.1%               63.7% -> 62.5%               36 of 36        --
    (the default's quarter flow after its refine, T1; per 1/8 cell; frames 6-41)

- **U1 MISSED as worded, with large gains:** the slow weave's core falls from 70 to 44 percent gross at 3 px/frame
  and from 89 to 22 at 5. The line was 20.
- **U2 half PASSED, with a flaw:** nothing on noise was lifted (the core stays 0.6 percent). But the period detector
  found a "lattice" on noise in all 36 frames. A smooth autocorrelation's highest values sit at the edge of the
  excluded centre, and they read as peaks. Only the matching-cost guard kept it harmless. The detector needs a real
  periodicity test: a peak separated from the centre by a dip.
- **U3 PASSED:** the independent patch inside the unwrapped box keeps its own motion (0.1 percent of its cells
  lifted, its error unchanged), while the box around it falls from 70 to 22 percent.
- **The fast weave is not helped (98.5 -> 97.1),** as the design said: its reference ring is locked too. That is
  the per-level trust gate's band.

**Where the stage stands.** The unwrapping form is the stage's mechanism, and it survives its control. Before it
becomes a shader switch, three things are owed:
1. a true periodicity test (U2's flaw);
2. why 44 percent of the 3 px/frame core stays wrong;
3. then the GLSL form at the quarter level, BEFORE the variational smoothing (0f), gated on the full ladder.

### Stage 1a, the second form (after the first form's flaw; post-hoc, labelled)

**First, the anatomy of one frame (3 px/frame, frame 20).** Much of the core counted wrong there is NOT aliasing.
The largest groups read 4, 5 and 6 px against a true 3: over-reads of 1-3 px, a bias the unwrapping cannot and should
not fix. The true aliases sit at 29-31 px (3 + 28), and the lift corrects them when it has the lattice.

**The fix for U2's flaw.**
- A periodicity test: the autocorrelation must dip between the centre and a peak.
- Then, since the found region's bounding box holds black ground at its margins and dilutes a plain
  autocorrelation, a MASKED, overlap-normalised autocorrelation over the region's own pixels.

    case                        core gross before -> after   ring gross before -> after   lattice found   the patch
    weave  3                    70.0% -> 45.5%               17.3% -> 15.2%               36 of 36        --
    weave  5                    88.8% -> 41.6%               44.3% -> 24.5%               36 of 36        --
    noise  5                     0.6% ->  0.6%               15.4% -> 15.4%                0 of 36        --
    weave  5 + a noise patch    70.1% -> 40.2%               38.8% -> 22.5%               36 of 36        0.0% lifted, error unchanged

- **U2's flaw is fixed:** no lattice on noise (0 of 36), a lattice on every weave frame.
- **U3 still holds.**
- **But the slow weave at 5 px/frame lifts LESS well (22 -> 42 percent).** The detector now finds A lattice, not
  necessarily the basis the aliases follow: the weave's autocorrelation also peaks at half-periods such as (14, 0),
  which are not true periods of the print.
- **The open issue:** choose the basis that EXPLAINS the cells' observed alias offsets (the common non-zero values
  of w - r that are also autocorrelation peaks), not the strongest peaks alone. That is the next refinement, before
  the GLSL form.

### Stage 1a, the third form, and where the loop stops (post-hoc, labelled)

**The third form:** the periodicity test only GATES. The lifts are the observed common offsets of w from r over the
region, each kept only where the texture repeats (masked autocorrelation above 0.5).

    core gross (before 70.0 / 88.8 / 0.6 / 70.1)   form 1 (plain AC,       dip test only   form 2 (dip + masked   form 3 (observed
                                                   nearest lattice)                        AC, nearest lattice)   offsets)
    weave  3                                       44.0%                   56.4% (20/36)   45.5%                  54.6%
    weave  5                                       22.3%                   --              41.6%                  36.6%
    noise  5 (lattice found)                       0.6% (36/36, false)     0.6% (0/36)     0.6% (0/36)            0.6% (0/36)
    weave  5 + patch (patch cells lifted)          22.2% (0.1%)            --              40.2% (0.0%)           35.1% (0.0%)

- **Each change was measured on its own, except form 2.** Form 2 bundled the dip test with the masked
  autocorrelation. The dip test alone was run on 3 px and noise, and there it lost the weave's lattice on 16 of 36
  frames.
- **Form 1 remains the best on the weave.** Its false lattices on noise were harmless: the matching-cost guard
  refused every wrong lift.
- **The loop stops here.** Three forms is enough guessing. The next step is a per-cell TAXONOMY of what stays wrong
  under form 1:
  - over-reads that are not aliasing (3 px/frame's 4-6 px cells);
  - aliases not lifted, and why (no lattice, the matching guard, a biased reference);
  - wrong lifts.
  The mechanism is then fixed on evidence, and only then written in GLSL.
- **The stage's verdict so far:** the unwrapping form is the right mechanism. At its best offline it quarters the
  slow weave's locked interior (89 -> 22 percent), and it leaves independent motion alone in every form tried. Its
  period detection is the part not yet right.

### Stage 1a concluded: the taxonomy, the refine, and STAGE v1 (frozen)

**The taxonomy (form 1: what stays wrong in the core, and why).**

    what stays wrong                                      3 px/frame   5 px/frame
    a lift refused by the matching guard                  49.8%        69.9%
    near-truth over-reads (not aliasing)                  31.8%        14.6%
    wrong lifts                                           14.3%        14.7%
    the nearest lattice lift is zero                       4.1%         0.8%

- **The guard's refusals dominate, and the cost check explained them** (frame 20, three core cells): the truth
  costs 0.0000, the alias 0.02-0.025. But the lift d = w + l carries w's sub-pixel error, and on a steep print
  that costs about what the alias's mismatch does, so the guard became a coin toss.
- **The fix is the standard coarse-to-fine step, not a threshold:** lift to the basin, then REFINE to its bottom
  (+-1 px in half-pixel steps) before the guard compares.

**Form 1r (the refine) and form 4r (the masked periodicity test as the gate, form 1's lattice for the lift, the
refine):**

    case                        core gross before -> after   ring before -> after   lattice found   the patch
    weave  3                    70.0% -> 29.4%               17.3% ->  9.8%        36 of 36        --
    weave  5                    88.8% ->  5.4%               44.3% ->  7.5%        36 of 36        --
    noise  5                     0.6% ->  0.6%               15.4% -> 15.4%         0 of 36        --
    weave  5 + a noise patch    70.1% -> 12.6%               38.8% ->  8.3%        36 of 36        0.1% lifted; error unchanged
    (form 4r; form 1r's weave rows are identical, but it false-fires a lattice on noise, harmlessly)

- **U1 on the post-hoc form:** 5 px/frame falls from 89 to 5.4 percent, under the 20 line. At 3 px/frame the rest
  (29.4 percent) is mostly the over-read, which is not aliasing and not this mechanism's job.
- **U2:** no lattice on noise, and nothing lifted.
- **U3:** the independent patch is untouched.

**STAGE v1, the shared stage's offline specification (tests/probes/weave/unwrap.py, UNWRAP_FORM=4
UNWRAP_REFINE=1), frozen.** At the quarter level, on the default's own flow after its refine, per region:
1. **the region:** the largest connected component of moving cells, holes filled;
2. **the reference r:** the median flow of its edge ring (2 cells);
3. **the gate:** a masked, overlap-normalised autocorrelation of the region's texture with a true peak (a dip
   between the centre and the peak);
4. **the lattice:** the plain autocorrelation's two strongest non-collinear peaks;
5. **the lift:** the lattice vector nearest r - w;
6. **the refine:** +-1 px around the lifted motion;
7. **the guard:** the lifted motion must match the frames no worse than w.

Any change to it is v2, and every consumer re-runs.

**What is next, and why it is a design step.** The GLSL form cannot copy the offline one: connected components and an
FFT autocorrelation have no cheap per-pixel form. The shader needs local stand-ins, and each is a trade to measure:
- a windowed reference in place of a global region's ring;
- the 1/8 level's two basins (ALIAS_E) in place of a lattice from an autocorrelation;
- a small sub-pixel refine.
It is also the first point where render time enters (the owner's rule: measure time before any ship decision).

### Pre-registered: stage 1b, the GPU-shaped stand-ins, offline (before it ran)

v1's two global pieces are replaced by forms a shader can run, still in numpy, and scored against v1. This is FORM 5
of `unwrap.py`.
- **The reference by nearest anchor, as jump flooding computes it.** ANCHORS are moving cells with a still cell within
  2 cells: the boundaries of moving regions. Each anchor's value is the median of the anchors within 2 cells of it.
  Every moving cell takes the value of its nearest anchor; no global component.
- **No lattice at all.** Each moving cell ADOPTS the reference: d = r, refined by +-1 px, and kept only where it
  matches the frames at least as well as w, and differs from w by more than 2 px. The lattice's job was to keep
  independent motion from being lifted, and the matching guard may do that alone: an independent patch matches its
  own motion far better than its outline's.

The predictions:
- **G1:** the weave's core gross within 5 points of v1 (29.4 percent at 3 px/frame, 5.4 at 5, 12.6 in the patch box).
- **G2 (U3's control):** the independent patch keeps its own motion, under 1 percent of its cells changed.
- **G3 (noise):** the core's gross within 0.2 points of the default's, and under 1 percent of the box's cells changed
  by more than 2 px.
- **If G2 or G3 fails,** the lattice (or a periodicity gate) is load-bearing, and the shader needs one.

### Results: stage 1b (the M5): the naive GPU stand-ins fail, and show what is load-bearing

    case                        v1 core   form 5 core (before -> after)   ring            cells changed > 2 px
    weave  5                     5.4%     88.8% -> 53.7%                  44.3 -> 36.2%   30.1% of the box
    weave  3                    29.4%     70.0% -> 14.7%                  17.3 ->  7.6%   39.7%
    weave  5 + a noise patch    12.6%     70.1% -> 42.4%                  38.8 -> 31.8%   25.0%; the patch 4.8% (error 1.16 -> 1.09)
    noise  5                     0.6%      0.6% ->  0.4%                  15.4 ->  8.5%    4.1%

- **G1 MISSED at 5 px/frame (53.7 against v1's 5.4), and better than v1 at 3 (14.7 against 29.4).**
  - At 5 px/frame the edge ring is only about 56 percent right. v1's reference was the median over the WHOLE ring,
    where the right answer is the majority. A cell's nearest anchors are often a locked stretch.
  - **A region-wide robust vote is load-bearing.**
  - At 3 px/frame the edge is mostly right, and adopting it also fixes the near-truth over-reads the lift left
    alone.
- **G2 and G3 MISSED:** without a periodicity gate, adopting the outline's motion changes 4-5 percent of the noise
  box's and the patch's cells. The changes IMPROVE them (the noise ring 15.4 -> 8.5 percent, the patch's error
  1.16 -> 1.09 px). But a switch must not change what it was not built for, so **a periodicity gate is load-bearing
  too.**
- **The shader's natural candidates:**
  - **for the gate:** the 1/8 level's own rival-basin test (ALIAS_E's margin). At margin 0.3 it covers 55 percent of
    the weave box and 0.4 percent of noise (0b), and its offline twin is ambiguity.py;
  - **for the reference:** a WIDE median of the anchors, which a coarse level makes cheap.

### Pre-registered: stage 1b', the gate and the wide reference (before it ran)

Form 6 of `unwrap.py` is form 5 with two changes.
- **A wide reference:** the median of the anchor values within +-15 cells (+-120 px) of the nearest anchor.
- **The gate:** only cells whose 1/8 cost curve has a rival basin within margin 0.3, grown by one cell, may adopt.
  This is ambiguity.py's analyse(), the offline twin of ALIAS_E.

The predictions:
- **G1':** the weave's core within 5 points of the better of v1 and form 5, at each speed (5 px: 10.4; 3 px: 19.7;
  the patch box: 17.6).
- **G2':** the patch under 1 percent changed.
- **G3':** noise under 1 percent changed.

### Results: stage 1b' (the M5): the gate closes the side effects, and the reference needs REACH

    case                        v1 core   form 6, +-15 cells              form 6, +-30 cells              cells changed (+-30)
    weave  3                    29.4%     70.0 -> 5.7%  (ring 2.3)        70.0 -> 2.4%  (ring 0.9)        49.0%
    weave  5                     5.4%     88.8 -> 32.5% (ring 16.9)       88.8 -> 9.7%  (ring 7.5)        66.5%
    weave  5 + a noise patch    12.6%     70.1 -> 21.3%; patch 0.0%       70.1 -> 7.0%; patch 0.1%        53.6%
    noise  5                     0.6%      0.6 -> 0.6%; 0.0% changed       0.6 -> 0.6%; 0.0% changed        0.0%

- **G2' and G3' PASSED at both reaches:** the rival-basin gate confines the change to the print. Noise is untouched
  (0.0 percent changed), and so is the independent patch (0.0-0.1 percent).
- **G1' PASSED at +-30 cells, MISSED at +-15:** at 5 px/frame, where the edge is only half right, the vote must pool
  enough of the whole outline for the right answer to be its majority. At +-30 cells (+-240 px at 1280 wide) it
  does: 9.7 percent against the line of 10.4. The reach is a single parameter, measured rather than guessed
  (UNWRAP_WIDE).
- **Against v1 (the global form):** better at 3 px/frame (2.4 against 29.4, since adopting also fixes the
  over-reads) and in the patch box (7.0 against 12.6); a little behind at 5 px/frame (9.7 against 5.4).

**STAGE v2, GPU-shaped (unwrap.py UNWRAP_FORM=6 UNWRAP_WIDE=30), frozen; v1 is superseded.** At the quarter level,
on the default's own flow after its refine:
1. **ANCHORS:** moving cells with a still cell within 2 cells, each valued as the median of the anchors within 2;
2. **the REFERENCE:** each cell's nearest anchor (jump flooding), read through a WIDE median of the anchor values
   within +-240 px (a coarse level makes it cheap). The reach scales with the picture's width;
3. **the GATE:** the 1/8 level's rival basin within margin 0.3 (ALIAS_E's margins, already in the default), grown
   by one cell;
4. **ADOPT:** the reference, refined +-1 px in half-pixel steps, kept only where it matches the frames at least as
   well as the cell's own flow and differs from it by more than 2 px.

Next, stage 1c: this in GLSL as a generator switch, byte-identical when off. Then its own tests: the weave sweep, the
patch, the full ladder on the Arc, and the time.

### Stage 1c, first: the insertion point, and one simplification (offline)

**The insertion point.** v2 was measured on the quarter flow after the refine (T1). The GLSL form goes after the
carry's pick (T2), so the carry cannot undo an adoption, and before the variational smoothing (which pushes the
lock outward, 0f). v2 run on T2:

    case                        core gross before -> after   ring before -> after   cells changed   the patch
    weave  3                    72.0% -> 2.4%                21.0% -> 0.9%         53.9%           --
    weave  5                    89.8% -> 9.2%                45.5% -> 7.1%         68.4%           --
    noise  5                     0.6% -> 0.6%                15.4% -> 15.3%         0.0%           --
    weave  5 + a noise patch    73.8% -> 7.1%                40.0% -> 3.4%         56.6%           0.1% lifted

The same as on T1, so the insertion point is VALIDATED.

**A note on v2's own definition, found while writing the switches:** its wide median pooled the anchors' OWN flows.
The per-anchor local median was computed and never used. So v2 needs no local median, and the GLSL form has one step
fewer. `UNWRAP_LOCALMED` defaults to v2's behaviour.

**The simplification under test:** the wide median centred on the CELL itself (+-240 px) instead of on its nearest
anchor. That would remove the jump flood, about ten passes per direction, and dispatch count is the engine's cost.
For regions up to about 500 px across, the cell's own window reaches the whole outline. Beyond that it finds no
anchor and adopts nothing, which is the safe side.

### Stage 1c: the cell-centred reference (offline), and the GLSL form pre-registered

**The cell-centred reference (UNWRAP_CENTRE=cell, on T2) matches the anchor-centred one:** weave 3 px/frame 72.0 ->
2.2 percent (anchor-centred 2.4), 5 px/frame 89.8 -> 9.3 (9.2), noise untouched. So the GLSL form drops the jump
flood: **STAGE v3 = v2 with the reference centred on the cell** (frozen; unwrap.py UNWRAP_FORM=6 UNWRAP_WIDE=30
UNWRAP_CENTRE=cell).

**The GLSL form: `tests/outline_adopt.py`, the generator switch OUTLINE_ADOPT=1 (needs ALIAS_CARRY=1).** Four passes
per direction, after the carry's pick and before the variational iterations:
1. anchors;
2. 32-px coarse histograms of the anchors' flow in one-pixel bins;
3. the reference: the median off the summed histograms within +-256 px (the GLSL grid's nearest to v3's +-240);
4. adopt: the gate on ALIAS_E's own margins, the refine by a 5 x 5 quarter-level SAD, the guard.

The controls, already run: with the switch off the generator reproduces the shipped default byte for byte, and with it
on the file gains exactly the eight passes (hooks 76 -> 84), braces and parentheses balanced.

The predictions, before any number:
- **A1:** on the slow weave (3 and 5 px/frame) the variant's box PSNR rises at least 10 dB over the default.
  Offline, the edge-driven warp over a GIVEN region gave +22 to +30; this one finds its own region.
- **A2:** noise at 3, 5 and 11 px/frame: within 0.3 dB of the default (the gate).
- **A3:** the fast weave (11, 19): within 0.5 dB of the default, since there the outline is locked too.
- **A4 (the gate for any switch):** the full 42-case ladder on a deterministic host, with the capped mean within 0.1 and
  no case down more than 1 dB.
- **A5 (time):** measured against the default from a file source, interleaved (the record's method), and reported. No
  threshold: the owner's rule is to measure before any ship decision.

### Results: stage 1c, A1-A3 (the M5): the GLSL form repairs the slow weave

The first build did not compile: a pass may not ask for its own output's _pos. The harness's compile alarm stopped it
rather than let libplacebo fall back to its own mixer. The fix: gl_FragCoord, and the grid from the histograms.

    case (box PSNR-Y, dB)   the default   OUTLINE_ADOPT   linear   change
    weave  3                20.27         39.70           26.74    +19.43
    weave  5                16.23         26.05           21.33     +9.82
    weave 11                15.94         15.83           13.86     -0.11
    weave 19                15.66         15.83           14.32     +0.17
    noise  3                51.06         51.06           30.46     +0.00
    noise  5                43.37         43.43           27.31     +0.06
    noise 11                48.44         48.26           25.17     -0.18
    noise 19 (unregistered) 44.48         43.98           24.08     -0.50

- **A1 half PASSED:** +19.4 dB at 3 px/frame. At 5 it gains +9.8, 0.18 short of the 10 line. Both lift the slow
  weave from BELOW the blend to well above it (3 px: 20.3 -> 39.7 against linear's 26.7).
- **A2 PASSED:** noise within 0.2 dB at the registered speeds.
- **A3 PASSED:** the fast weave is unchanged, as designed. Its outline is locked too, which is the trust gate's
  band.
- **Noise at 19 px/frame moves -0.5 dB** (outside the registered set). The full ladder decides whether that is a
  pattern.
- A4 (the full ladder on the Arc) and A5 (the time) are running.

### Results: stage 1c, A5 (the M5, 720p): the first GLSL form costs too much

    probes/weave/timing_adopt.sh (probes/cost/timing.sh's method: an ffv1 source, -f null, three interleaved rounds;
    O5_osc_textured, 180 output frames; MoltenVK's own defaults)
    linear           1.78 ms per output frame
    the default      9.06 ms
    OUTLINE_ADOPT   17.46 ms   (+8.4 ms, +93 percent; past the 16.7 ms a 60-fps output allows, where the default fits)

**Where the cost is, from the design:**
- the reference pass sums a 17 x 17-cell window of 65-bin histograms for every coarse cell, about 35 million texture
  fetches per output frame over both directions;
- the three upstream passes run on EVERY output frame, about 2.5 per source pair, although the adopt pass reuses its
  cached result whenever the pair has not changed.

**Two optimisations that cannot change a result:**
1. a SEPARABLE wide sum: a horizontal +-8-cell pass, then a vertical one (about 8 times fewer fetches, the same sums);
2. an early return in the upstream passes when the pair is unchanged, as the carry's passes already do.

The control: every box PSNR of the sweep must reproduce to the hundredth (the M5 path is deterministic).

### Results: stage 1c, A4 (the NAS's Arc, deterministic): the full ladder PASSES

The first GLSL form against the default, same host, same build (the default's afternoon ladder as the baseline;
`gatetable.py`, capped at 40):
- **the capped mean 38.357 against 38.298: +0.06** (the line: within 0.1);
- **no case down more than 1 dB:** the worst is L8_diagonal -0.75, then M2_period40 -0.49 and R1_rot_const -0.42;
- **8 cases up more than 0.3 dB,** most of them the periodic family the switch is for: P1_stairs_along_v4 +2.91,
  L1_trans_8px +2.58, L7_textured_large +1.92, P5 +1.31, P3 +1.27, F2 +0.73, L3 +0.51, P2 +0.47.

**A4 PASSED.** This was the unoptimised form. The optimised one carries it only if its identity control holds (the
weave sweep reproducing to the hundredth).

### Results: stage 1c complete: OUTLINE_ADOPT, identical and affordable

**The optimised form (separable wide sum; early returns upstream when the pair is unchanged).**
- **Its identity control PASSED:** all six sweep cases reproduce the first form to the hundredth (weave 39.70, 26.05,
  15.83; noise 51.06, 43.43, 43.98). A4's ladder pass therefore carries over.
- **The time (M5, 720p, the same method):** linear 1.78, the default 8.97, OUTLINE_ADOPT **9.83 ms per output frame:
  +0.86 ms, +9.6 percent** (the first form: +93).

**Where the switch stands.** `OUTLINE_ADOPT=1` on the default's recipe:
- the slow weave's box +19.4 dB (3 px/frame) and +9.8 (5 px/frame), from below the blend to above it;
- noise within 0.2 dB, and the fast weave unchanged;
- the full ladder passed (the capped mean +0.06, the worst case -0.75, eight periodic cases up by up to +2.9);
- +10 percent in time at 720p.

**Still owed before any adoption (the owner's call):**
- no harm on REAL footage (running: the half-rate test on the census's 40 film extracts, against the default's own run);
- the 4K form (scale_shader.py);
- the Metal port under the lockstep rule, if it is ever adopted.

### Pre-registered: 2.5e, lead 3's selection rule (after stage 1c, before it ran)

2.5d concluded that a rigid mode must choose per pixel between the family's motion and the region's model, by their
matching cost. One correction before it is built: on a periodic print the two TIE, because the alias matches as well as
the truth (the cage's lesson, section 8 and NFRAME-LIMITS). A pure cost rule would give up exactly the lattice and weave
gains. So `found5` in rotwarp.py:
- the candidate pixels are found2's (the found region plus its photo-consistent ring);
- the rigid draw's cost is its two views' disagreement; the family's cost is the same for the DEFAULT's own flow (its
  read_view 4, the k + 1 convention); both are box-filtered 5 x 5;
- the rigid draw replaces rec where it is CLEARLY cheaper (by 0.005), or on a TIE (within 0.005) where the pixel is on
  a print (the 1/8 rival-basin gate, margin under 0.3, as stage v3) AND the two motions differ by more than 2 px.
  Everywhere else rec stands.

The predictions:
- **R1':** found5 is never more than 0.5 dB below rec, on any scene (the pendulums included).
- **R2':** on the lattice it keeps at least 70 percent of found2's gain over rec.
- **R3':** on `static`, found5 equals rec.
- **Changed before the batch, after two smoke cases (labelled):** the first rule lost 1.19 dB on the noise pendulum
  and kept 97 percent of found2's gain on the lattice spin. On the pendulum even the TRUE rigid warp loses 1.2 dB
  (2.5): where the two motions AGREE, rec simply draws better. So both branches now also require the motions to
  DISAGREE by more than 2 px. The predictions stand as written.

### Results: stage 1c, no harm on real footage (the NAS's Arc)

The half-rate test (3.6b's; 12 -> 24 fps, the odd frames against the real ones) on all 40 of the census's film
extracts: OUTLINE_ADOPT (optimised) against the default's own run of the same extracts.
- **Per extract, the unflagged frames' median:** -0.02 to +0.46 dB, mean +0.057. None is down more than 0.3 dB; two
  are up more than 0.3 (SNL UK +0.46, Chicago +0.32).
- **Over all odd frames:** unflagged 41.41 -> 41.46, short runs 34.24 -> 34.32, long runs 30.74 -> 30.77.
- The alignment controls are unchanged (the even frames, 58-66 dB).

**The switch is harmless on real footage, and slightly positive.** Its adoption file is complete but for the 4K form
and the Metal port:
- the slow weave +19.4 / +9.8 dB;
- the ladder passed;
- real footage level to up;
- +9.6 percent in time.
Adoption is the owner's call.

### Results: 2.5e, lead 3's selection rule (the M5): R1' and R2' MISSED; the lead is PARKED, with its reason

    texture   scene           rec     found2   found5   found5 - rec   found2 - rec
    noise     spin-constant   48.92   50.93    51.30    +2.38          +2.01
    noise     spin-pendulum   53.17   50.80    51.84    -1.33          -2.37
    noise     spin-orbit      47.89   48.35    48.47    +0.58          +0.46
    noise     roll-12         36.32   37.45    36.77    +0.45          +1.13
    sines     spin-constant   50.85   49.92    50.36    -0.49          -0.93
    sines     spin-pendulum   53.44   50.40    51.46    -1.98          -3.04
    lattice   spin-constant   19.75   26.71    24.63    +4.88          +6.96
    lattice   spin-pendulum   29.57   48.00    33.95    +4.38         +18.43
    lattice   spin-orbit      22.77   30.18    27.81    +5.04          +7.41
    lattice   roll-12         34.36   36.00    35.08    +0.72          +1.64
    (static: equal to rec on every texture; the rolls beyond the reach within 0.5 of found2)

- **R1' MISSED:** the rule roughly halves the slow pendulums' harm (-2.4 -> -1.3, -3.0 -> -2.0) but does not remove
  it.
- **R2' MISSED on most:** it gives up much of the lattice gain (the lattice pendulum +18.4 -> +4.4).
- **R3' HELD.**
- **Why, and why it is parked rather than tuned.** The rule judges rec by its FIELD, a proxy. rec's real drawing is
  better than its field suggests at slow speeds and at the rim (the free denoise, its gates, its occlusion handling).
  No offline proxy of rec's field can see that.
- **The comparison has to be made INSIDE the shader, against the candidate the shader would actually draw.** That is
  a design question for a GLSL form, not another offline variant. Per the owner's rule (a well-understood obstacle is
  documented and parked), lead 3 stops here.
- **Its periodic cases may not need it at all:** lead 4's menu re-score is per cell and local, so it should handle a
  rotating print too. That is the cheaper route to the lattice and weave gains, and it is worth checking there first.

### Pre-registered: lead 4's re-score on a ROTATING print (before it ran)

If lead 4's menu re-score, which is per cell and local, repairs a spinning print, it covers lead 3's largest gains
(the lattice, +5 to +18 dB) without lead 3's selection problem. `tests/probes/weave/rescore_disc.py` runs rescore1.py's
step 1c, unchanged, on the default's quarter flow (the T2 tap) of `spin-constant` and `spin-pendulum` on the lattice.
The truth is the masters' own chord per cell; the core is the disc more than 32 px inside its rim.
- **D4:** the core's gross falls by at least half on both scenes.
- **D5 (a control that must not move):** `spin-constant` on noise, where the default's flow is already right: under
  1 percent of the core's cells change.

### Results: lead 4's re-score on a rotating print (the M5): D4 MISSED, and worse; D5 about held

The equivalence check first: rescore_disc.py's box mode, through the shared rescore_cell, reproduces rescore1.py's
own number exactly (weave 11 px/frame, core 98.2 -> 4.9 percent). So the disc numbers are step 1c's.

    case                     core gross before -> after   core cells changed
    spin-constant, lattice   53.2% -> 58.8%               59.0%
    spin-pendulum, lattice   28.1% -> 41.1%               40.3%
    spin-constant, noise      7.5% ->  6.5%                1.1%

- **D4 MISSED, and in the wrong direction:** on the rotating lattice the re-score makes the field WORSE.
- **D5 about held:** noise improves, with 1.1 percent of its core changed (the line was 1).
- **The reason is the survey's warning.** The `lattice` texture is EXACTLY periodic (a product of sines, with no fine
  noise). The weave is not, and step 0's margin came from its fine noise. On an exact print the truth and its
  aliases tie, and the data alone cannot choose. Rotation adds to it: a translated 16 x 16 block cannot match a
  rotated one exactly, so another alias can beat the locked w by more than the 0.004 margin, and the pick goes to a
  different wrong answer.
- **Two lessons:**
  1. **The re-score needs a UNIQUENESS test:** the winner must beat every other candidate by the margin, not only w.
     On an exact print that is a tie, and it keeps w. That is the lossless fallback the survey asked for, and it is
     owed before any GLSL form.
  2. **Lead 3 (a rigid model from outside the data) stays necessary for exactly periodic rotating prints.** Lead 4
     cannot replace it there.

### Pre-registered: lead 4's step 1d, the uniqueness test (before it ran)

In rescore_cell, the pick must now beat the RUNNER-UP among all the refined candidates (w and the two best aliases)
by 0.004, as well as w; otherwise the cell keeps w. RESCORE_STEP=1d; 1c stays reproducible. On the box (weave 3, 5,
11, 13, 19; noise 11) and the discs (spin-constant and spin-pendulum on the lattice; spin-constant on noise):
- **U4:** the rotating lattice is no worse than the default's own flow (within 2 points of its core gross).
- **U5:** the fast weave keeps at least 80 percent of step 1c's reduction in core gross.
- **U6:** noise, under 1 percent of the core's cells changed.

### Results: lead 4's step 1d (the M5): U4, U5 and U6 PASSED; lead 4 has its offline mechanism

    case                     core gross before -> after (1d)   step 1c for comparison   core cells changed
    box, weave 11            98.2% -> 19.1%                    4.9%                     79.7%
    box, weave 13            99.5% -> 26.8%                    13.3%                    73.6%
    box, weave 19            97.6% -> 11.4%                    8.4%                     87.1%
    box, weave  3            70.8% -> 14.1%                    9.4%                     61.5%
    box, weave  5            91.5% -> 26.5%                    24.1%                    67.6%
    box, noise 11             3.5% ->  3.5%                    --                        0.0%
    spin-constant, lattice   53.2% -> 53.3%                    58.8% (worse)             3.6%
    spin-pendulum, lattice   28.1% -> 28.4%                    41.1% (worse)             1.3%
    spin-constant, noise      7.5% ->  7.5%                    6.5%                      0.0%

- **U4 PASSED:** the uniqueness test stops the harm on exact rotating prints; within 0.3 points of the default.
- **U5 PASSED:** the fast weave keeps 84-97 percent of step 1c's reduction (98-99 percent wrong -> 11-27).
- **U6 PASSED:** noise is untouched (0.0 percent changed). Step 1c's incidental refinement of noise is gone with
  the strict test.

**Lead 4's offline mechanism (rescore1.py rescore_cell, RESCORE_STEP=1d), for a switch's GLSL form:**
- a MENU: the cell's own flow and its 3 x 3 neighbours', plus the print's lattice points within 45 px;
- every candidate refined +-0.5 px before it is ranked; the best two, and w, refined +-1 px;
- the pick only if it beats w AND the runner-up by 1/255, so an exact tie keeps w.

The GLSL form's open parts:
- the lattice without a per-cell FFT (a coarse-cell self-match over sparse shifts, tested offline first);
- the gate (the 1/8 rival basins);
- the cost.
Exact periodic prints stay unrepaired by it: that is lead 3's territory, parked.

### Pre-registered: lead 4's step 1e, the lattice as a shader could find it (before it ran)

One change: the per-cell lattice (a 64 x 64 FFT self-match) becomes a COARSE-cell self-match of the kind a shader
can afford.
- It is computed once per 32-px cell.
- Over shifts on a 2-px grid within 8-40 px, scored by the SAD of an 8 x 8 subsample (4-px spacing) of the cell's
  32 x 32 patch.
- The two lowest non-collinear shifts are kept if under 0.3 of the patch's mean absolute deviation, each refined to
  the pixel (+-1 px).
RESCORE_LATTICE=coarse; step 1d otherwise unchanged.
- **E1:** every case within 5 points of step 1d's core gross (the fast weave 19.1 / 26.8 / 11.4; the slow 14.1 /
  26.5), and the controls (noise, the rotating lattice) still within 1 percent changed / 2 points.

### Results: lead 4's step 1e (the M5): E1 MISSED; the lattice's precision is load-bearing

    case              step 1d (the per-cell lattice)   step 1e (the coarse-cell lattice)
    weave 11          19.1%                            35.3%
    weave 13          26.8%                            40.8%
    weave 19          11.4%                            27.1%
    weave  3          14.1%                            20.6%
    weave  5          26.5%                            34.9%
    noise, rotating lattice: unchanged in both (0.0 percent changed; within 0.3 points)

- **E1 MISSED:** the coarse-cell self-match costs 6-16 points on every weave case. The safety properties survive:
  the uniqueness test still keeps every exact print and noise untouched.
- **So the lattice's precision matters.** A fixed 32-px grid, a 2-px shift grid and an 8 x 8 subsample give vectors
  good enough to keep the gate honest but not to reach the truth as often.
- **For the GLSL form:** the lattice should be found in the cell's OWN neighbourhood (as the per-cell form did). The
  candidates for doing that affordably are:
  - a separable or two-stage search (coarse shifts, then refined);
  - or the quarter level's own basins (ALIAS_Q's two hypotheses), which the carry already computes per quarter cell.
  Each is measured offline against step 1d before any GLSL.

### Pre-registered: lead 4's step 1f, a two-stage lattice in the cell's own neighbourhood (before it ran)

One change against step 1d: the per-cell lattice by a TWO-STAGE search on the cell's own 32 x 32 neighbourhood, a
shader's affordable form (RESCORE_LATTICE=two).
- Coarse shifts on a 4-px grid within 8-40 px, scored by the SAD of an 8 x 8 subsample (4-px spacing).
- The six best refined to the pixel (+-2 px) by the SAD of a 16 x 16 subsample (2-px spacing).
- The two lowest non-collinear shifts kept if under 0.3 of the patch's mean absolute deviation.
- **E2:** every case within 5 points of step 1d (the fast weave 19.1 / 26.8 / 11.4; the slow 14.1 / 26.5), and the
  controls untouched (noise 0 percent changed; the rotating lattice within 2 points).

### Results: lead 4's step 1f (the M5): E2 MISSED on the fast cases; the dense lattice is the form that works

    case              step 1d (the per-cell FFT)   step 1f (two-stage, own neighbourhood)   step 1e (coarse cell)
    weave 11          19.1%                        28.9%                                    35.3%
    weave 13          26.8%                        34.5%                                    40.8%
    weave 19          11.4%                        20.0%                                    27.1%
    weave  3          14.1%                        16.8%                                    20.6%
    weave  5          26.5%                        28.6%                                    34.9%
    controls (noise; the rotating lattice): untouched in all three

- **E2 MISSED on the fast cases** (7.7-9.8 points behind step 1d, against a line of 5) and PASSED on the slow ones
  (2-3 points). The safety holds in every form.
- **The loop on cheaper lattices stops at two tries.** The dense per-cell search (every shift, by mean squared
  difference) is the form that works.
- **It only has to run where the gate opens** (the cells on a print), so its real cost depends on how much of a
  frame is print. That is measured in the shader itself, as A5 measured OUTLINE_ADOPT's, not guessed offline.
- **The GLSL form of lead 4 is therefore:**
  - the gate (the 1/8 rival basins);
  - a dense per-cell lattice search on gated cells;
  - the menu (the cell's and its neighbours' flows plus the lattice points);
  - refine before ranking;
  - the uniqueness test;
  - full-resolution scoring;
  - and then the same tests as OUTLINE_ADOPT (the sweep, the ladder on the Arc, real footage, the time).

### Pre-registered: lead 4's step 1g, the lattice per TILE, the form a shader can afford (before it ran)

The cost check behind it:
- the dense per-cell search is about a million fetches per cell in a shader (the FFT is what made it cheap offline);
- the two-stage search is about 54 thousand per cell.
Both are too heavy where a print covers much of a frame. A lattice belongs to the TEXTURE, so a shader can estimate
it once per 128-px tile instead (about 135 tiles at 1080p, roughly 7 million fetches per source pair).

RESCORE_LATTICE=tile: the two-stage search of step 1f on a 64 x 64 patch at the tile's centre (4-px spacing), cached
per tile. One change against step 1d.
- **E3:** every case within 5 points of step 1d, with the controls untouched. If it fails, lead 4's GLSL form needs a
  different lattice source, and the 1/8 level's rival basins (ALIAS_E, already computed per cell) are next.

### Results: lead 4's step 1g (the M5): E3 MISSED; the lattice must come from the object's own neighbourhood

    case        1d (per-cell FFT)   1f (two-stage, own)   1e (coarse cell)   1g (per 128-px tile)
    weave 11    19.1%               28.9%                 35.3%              57.4%
    weave 13    26.8%               34.5%                 40.8%              60.4%
    weave 19    11.4%               20.0%                 27.1%              50.8%
    weave  3    14.1%               16.8%                 20.6%              36.4%
    weave  5    26.5%               28.6%                 34.9%              55.6%
    controls (noise; the rotating lattice): untouched in all four

- **E3 MISSED, and badly:** prints do not line up with tiles. A tile's centre patch often falls partly or wholly
  outside the moving object, and it finds no lattice or the wrong one.
- **The lattice stand-ins stop here, at three tries.** Ranked by accuracy: the per-cell FFT (unaffordable in a
  shader), the two-stage search in the cell's own neighbourhood (8-10 points behind, about 54 thousand fetches per
  gated cell), then the coarse cell and the tile.

**LEAD 4's OPEN DESIGN PROBLEM, stated for the next session.** The offline mechanism works (step 1d: the fast weave
98-99 -> 11-27 percent, with exact prints and noise untouched). Its GLSL form needs a lattice from the object's own
neighbourhood at a shader's cost. Two routes, each to be measured against 1d:
1. **the 1/8 level's RIVAL basins (ALIAS_E):** already computed per cell, and the best-minus-rival offset is one
   lattice vector to 8 px, refined at full resolution. Free to fetch, and object-aligned;
2. **step 1f's two-stage search, run only on gated cells, with its time measured in the shader** (it may be
   affordable where prints are a small part of the frame, and it degrades gracefully where they are not).

### OUTLINE_ADOPT adopted for the player (2026-10-01): the 4K twin and the Metal port

The owner, at 02:00: *"Adopt the woven-texture switch - clear benefits without realworld downside in the Cadence use
case."* Shipped as `shaders/...-global-cage-energy-carry-adopt.glsl` and its `-4k` (SHADERS.md). The generator
reproduces the tested file byte for byte (md5 2f82ca2c), and the 1.0.3 default still regenerates unchanged.

**The 4K twin.** scale_shader.py carried every new pass but one: the adoption's 32-px coarse grid
(`HOOKED.w 31 + 32 /`) was left at full size. That is correct, since the cells beyond the quarter level read empty,
but it does four times the work. The grid now takes the quarter level's factor (64 px at factor 2). The sweep at twice
the size (weavesweep.py `WEAVE_SCALE=2`: the frame, the box, the speeds and the print all doubled, so the twin sees the
720p case in its own texels):

    box PSNR-Y, dB      1.0.3's -4k   the adopted -4k   change    (at 720p, for reference)
    weave  3            20.29         41.49             +21.20    +19.43
    weave  5            16.18         23.83              +7.65     +9.82
    weave 11            15.84         15.71              -0.13     -0.11
    noise 3 / 5 / 11    45.25 / 41.59 / 42.36   45.20 / 41.65 / 42.41   within 0.06

**The Metal port** (gen_metal.py: 88 passes, all compile; the demo engine's CLI through weavesweep.py `REC_METAL`):

    box PSNR-Y, dB            Metal: 1.0.3   adopted   libplacebo, rgb48le in: 1.0.3   adopted   libplacebo, YUV in: adopted
    weave 3                   20.36          38.77     20.41                           38.75     39.70
    weave 5                   16.19          18.98     16.19                           19.54     26.05
    weave 11                  15.95          15.83     --                              --        15.83
    noise 3 / 5 / 11          44.45 / 41.27 / 43.75   44.45 / 41.33 / 43.79   (YUV in: 51.06 / 43.43 / 48.26)

- **The engines agree on the same input:** weave 3 within 0.02 dB, weave 5 within 0.56. The carry's own column agrees
  to 0.05.
- **The input path matters at 5 px/frame:** libplacebo given the 8-bit YUV converts it itself, and the adoption gains
  +9.8 dB. Given swscale's rgb48le of the same frames, it gains +3.3; Metal gains +2.8. The 5-px adoption is a
  tie-break on the quarter level's cost ("no worse than the texel's own flow"), so sub-LSB differences flip it.
  It is a gain on every path, and the 3-px case (+18 to +19) is robust.
- **The noise columns** differ between the input paths (51 against 44 dB), for both graphs alike. That comes from
  the conversion to rgb48le, not from either engine.
- **Time on the demo engine** (1080p, 24 -> 48, three interleaved rounds, end to end): 31.6 / 31.3 / 30.7 fps against
  1.0.3's 32.1 / 31.8 / 31.2, about 1.6 percent.

### Pre-registered: lead 4's step 1h, the lattice from the 1/8 level's rival basins (route 1; before it ran)

On 2026-10-01 the owner adopted OUTLINE_ADOPT for the player and asked for the fast fix next. This is route 1 of the
open design problem. One change against step 1d: where the lattice comes from (RESCORE_LATTICE=rival).
- **The basins:** the 1/8 level's cost curve per cell, as ALIAS_E computes it in the shader. Offline this is
  ambiguity.py's emulation: luma at each 1/8 texel's centre, a 5 x 5 SAD, every shift within +-3 texels. Each cell
  has a best shift and its lowest RIVAL behind a ridge, with the margin.
- **The offsets:** 8 x (rival - best) px, from the cell and its 3 x 3 neighbours whose margin is under 0.3 (the
  adopt gate's threshold). Sign-folded and deduplicated within 4 px.
- **Each offset refined at full resolution** by the self-match of frame k's own 32 x 32 neighbourhood, a 16 x 16
  subsample at 2-px spacing: +-4 px on a 2-px grid, then +-1 px. Kept if under 0.3 of the patch's mean absolute
  deviation.
- **The lattice:** the two lowest non-collinear vectors, or the lowest alone when all are collinear.
- **No rival nearby means no lattice,** and the cell keeps w. So the gate is built in; step 1d had none.
- **Cost:** 34 shifts x 256 fetches per distinct offset, about 9 thousand. One to three offsets per gated cell
  gives 9-26 thousand, against step 1f's 54 thousand.

The predictions:
- **E4:** every case within 5 points of step 1d (the fast weave 19.1 / 26.8 / 11.4; the slow 14.1 / 26.5). The
  controls stay untouched: noise 0 percent changed, the rotating lattice within 2 points.
- **Reported, not gated:** on the weave, the share of the core's gated cells with at least one raw offset within
  4 px of a true lattice vector (n (14, 14) + m (14, -14)), and with a refined vector within 1 px of one.
- **The expectation, written down before the run:** the 1/8 level's 8-px texel aliases a 14-px thread. Its basins
  may belong to the moire rather than the print, so the raw offsets may miss the lattice by more than the refine
  can reach. If E4 misses for that reason, route 2 comes next: step 1f's two-stage search on gated cells only,
  timed in the shader.

### Results: lead 4's step 1h (the M5): E4 MISSED; the rival offsets are true lattice vectors, but long ones

    case                     1d (per-cell FFT)   1h (the rival basins)   core changed   the offsets (core cells that found any)
    box, weave 11            19.1%               88.3%                   15.2%          raw within 4 px of the lattice 96.6%; refined within 1 px 88.2%; two directions 44.8%
    box, weave 13            26.8%               62.6%                   39.8%          95.6 / 95.6 / 51.3
    box, weave 19            11.4%               54.4%                   47.3%          96.4 / 96.3 / 45.9
    box, weave  3            14.1%               47.8%                   29.5%          96.5 / 88.2 / 45.1
    box, weave  5            26.5%               51.4%                   45.5%          95.6 / 95.6 / 51.8
    box, noise 11             3.5%                3.5%                    0.0%
    spin-constant, lattice   53.3%               53.0%  (default 53.2)    8.8%
    spin-pendulum, lattice   28.4%               29.3%  (default 28.1)    5.0%
    spin-constant, noise      7.5%                7.5%                    0.0%

- **E4 MISSED,** by 20-70 points on the weave. The controls held: noise unchanged, both rotating lattices within
  2 points of the default.
- **My written expectation was wrong.** The 1/8 level's basins do NOT belong to the moire: 96 percent of the raw
  offsets lie within 4 px of a true lattice vector, and the refine lands within 1 px of one in 88-96 percent.
- **The failure is completeness, not accuracy.** On weave 11, where the truth drops out of the core's wrong cells:
  - the truth is not in the menu: 72 percent (one direction found: 40; two directions found: 32);
  - no lattice at all: 14 percent;
  - offered to the pick: 12 percent.
- **Why two directions are not enough:** the 1/8 curve's best and rival sit 5 texels apart (raw (40, +-16) and
  (40, 0)), which refine to (42, +-14). That is three lattice steps each. Together the pair spans a SUBLATTICE of index
  3, which lacks (28, 0), the step from the locked (-16, 0) to the truth (11, 0). The single-direction cells have
  only the multiples of one vector.

### Pre-registered: lead 4's step 1i, the rival lattice COMPLETED (before it ran)

One change against step 1h: a completion stage after the refine (RESCORE_LATTICE=rival2).
- **Probes:** the short representatives of the cosets a/2 and a/3 for each valid vector. For each non-collinear
  pair also (a + b)/2, (a - b)/2, (a + b)/3, (a - b)/3, a - b and a + b.
- **Each probe** (8-40 px, not within 2 px of one already held) is refined +-1 px by the same self-match and kept
  under 0.3 of the patch's MAD. Up to three rounds, while new vectors appear.
- **The basis** is then the SHORTEST valid vector and the shortest valid one not collinear with it. Without
  completion the shortest would mean nothing, so it belongs to the change.
- **E5:** every case within 5 points of step 1d (the fast weave 19.1 / 26.8 / 11.4; the slow 14.1 / 26.5). The
  controls stay untouched: noise 0 percent changed, the rotating lattices within 2 points of the default.
- **Reported:** the self-match fetches per cell that found offsets (the cost; route 2's two-stage search is about
  54 thousand), and the two-direction share.
- **The expectation, before the run:** cells with two directions should recover to near step 1d. Cells with one
  direction cannot be completed, because nothing supplies the second. So E5 may miss on the fast weave by about the
  single-direction share. If it does, the backward curve's basins (ALIAS_E's B -> A, computed in the shader anyway)
  are the natural second source.

### Results: lead 4's step 1i (the M5): E5 MISSED; completion mends the sublattice, and two faults remain

    case                     1d (per-cell FFT)   1h (rival)   1i (rival, completed)   self-match fetches per cell (1i)
    box, weave 11            19.1%               88.3%        62.4%                   33 thousand
    box, weave 13            26.8%               62.6%        62.6%                   24
    box, weave 19            11.4%               54.4%        54.5%                   23
    box, weave  3            14.1%               47.8%        34.8%                   33
    box, weave  5            26.5%               51.4%        51.4%                   25
    box, noise 11             3.5%                3.5%         3.5% (0.0% changed)
    spin-constant, lattice   53.3%               53.0%        53.1%  (default 53.2)
    spin-pendulum, lattice   28.4%               29.3%        29.4%  (default 28.1)
    spin-constant, noise      7.5%                7.5%         7.5% (0.0% changed)

- **E5 MISSED** (by 15-43 points). The controls held.
- **Completion works where it applies.** On weave 11 the truth missing from the menu with two directions found went
  from 32 to 1 percent of the wrong cells, and the truth offered to the pick from 12 to 42 percent. Weave 3 likewise.
  On 13, 19 and 5 the raw offsets were already short ((16, -16) -> (14, -14)), so there was nothing to complete.
- **Two faults remain** (the anatomy of weave 11 and 13, scratch scripts):
  1. **One direction (40-41 percent of the wrong cells).** The 3 x 3 neighbourhood shows a single lattice
     direction, plus the 1/8 level's spurious (16, 0) or (40, 0), which the refine rejects. Nothing can complete one
     direction.
  2. **The uniqueness test refuses a right answer** (7.5 percent on weave 13). Two candidates refine into the SAME
     basin, for example 12.8 and 13.2 px for a truth of 13; the second counts as the runner-up, and the pick fails
     its 1/255 margin over itself. The test was written to protect exact prints, where DIFFERENT basins tie. This
     fault is in step 1d too.

### Pre-registered: lead 4's steps 1j and 1k, one change each (before they ran)

- **1j, against 1i (RESCORE_LATTICE=rival3):** the offsets come from the 5 x 5 neighbourhood (40 px) instead of the
  3 x 3. The lattice is the texture's, and a larger window of a print shows both directions.
  - **E6:** every weave case at least 10 points below 1i. The controls stay untouched (noise 0 percent changed, the
    rotating lattices within 2 points of the default). Against step 1d's line (within 5 points), reported.
- **1k, against 1d AND against 1i (RESCORE_STEP=1k):** the runner-up in the uniqueness test is the best of a
  DIFFERENT basin, more than 2 px from the pick. Two refinements of one answer are not a tie.
  - **U7 (on 1d's per-cell FFT lattice):** no weave case worse than 1d by more than 1 point. The controls stay
    untouched, the rotating lattices above all, since protecting them is the test's purpose.
  - **U8 (on 1i):** every weave case improves, and the controls stay untouched.
- If both hold, their combination (1j + 1k) is the candidate for the GLSL form. It is measured against step 1d + 1k,
  the better offline reference.

### An instrument fault, found by step 1j, and the re-runs

rescore1.py cached lattices (steps 1e, 1g) and the 1/8 basins (1h onward) by the frames' MEMORY ADDRESSES, the
2026-09-30 fix for `id()` of a reused view. One case's frames are freed when the next loads, and a later case's frames
can land at the same addresses and read the earlier case's entries. Step 1j's batch showed it: weave 5 found offsets
in 1,426 core cells, FEWER than step 1i found with a smaller window, which cannot happen. Run alone, weave 5 read
29.7 percent wrong, not 83.8.
- **The fix:** every array whose address keys a cache entry is held, so no later array can take its address, and
  rescore_disc.py empties every cache at each case.
- **The re-runs (np-scratch/weave/rerun/):** steps 1e, 1g, 1h, 1i and 1k-on-1i reproduce their recorded numbers
  exactly, case for case. Only 1j's weave 5 was hit. Steps 1c, 1d, 1f and 1k-on-1d use no cache.

### Results: lead 4's steps 1j and 1k (the M5): E6 PASSED, U7 PASSED on its purpose, U8 MISSED on the pendulum

    core gross             1d      1i      1j (5 x 5)   1d + 1k   1i + 1k   default
    box, weave 11          19.1%   62.4%   29.2%         6.6%     57.1%
    box, weave 13          26.8%   62.6%   30.5%        16.1%     57.0%
    box, weave 19          11.4%   54.5%   17.3%         8.7%     53.3%
    box, weave  3          14.1%   34.8%   17.7%         9.4%     32.4%
    box, weave  5          26.5%   51.4%   29.7%        24.9%     50.2%
    box, noise 11           3.5%    3.5%    3.5%         2.9%      3.5%     3.5%
    spin-constant, lattice 53.3%   53.1%   53.2%        53.7%     53.5%    53.2%
    spin-pendulum, lattice 28.4%   29.4%   29.1%        29.3%     31.2%    28.1%
    spin-constant, noise    7.5%    7.5%    7.5%         6.5%      7.5%     7.5%

- **E6 PASSED (1j):** every weave case 17-37 points below 1i. Noise is untouched and the rotating lattices sit within
  1 point of the default. With 25 cells' offsets, 86-95 percent of cells find two directions (45-52 before). The
  lattice costs 38-59 thousand self-match fetches per cell.
  - Against step 1d's line (within 5 points): 13, 3 and 5 pass, while 11 (+10) and 19 (+6) do not.
- **U7 (1k on step 1d's lattice): every weave case improves,** by 1.6-12.5 points. Weave 11 reaches 6.6 percent.
  - The rotating lattices stay within 2 points of the default, which is the test's purpose.
  - Noise moved: 1.0-1.1 percent of its core changed, all for the better (3.5 -> 2.9, 7.5 -> 6.5). So "untouched"
    is missed as worded, at step 1d's own 1 percent line.
- **U8 MISSED (1k on 1i):** the weave improves by 1-5 points, but the pendulum lattice is 3.1 points worse than the
  default (the line is 2).
- **So the uniqueness test's runner-up should come from a different basin,** at least on a lattice that finds the
  truth. Whether it is safe on the rival lattice is what the combination must show.

### Pre-registered: lead 4's step 1l, the combination (before it ran)

RESCORE_LATTICE=rival3 with RESCORE_STEP=1k, measured against step 1d + 1k (the better offline reference).
- **E7:** every weave case within 5 points of 1d + 1k (6.6 / 16.1 / 8.7 / 9.4 / 24.9).
- **The controls:** noise under 1 percent changed; the rotating lattices within 2 points of the default (the
  pendulum above all, where 1i + 1k failed).
- **If E7 holds and the controls do,** 1l is the offline mechanism for the GLSL form, with its cost (the lattice's
  fetches plus the menu's) to be cut there.

### Results: lead 4's step 1l (the M5): E7 MISSED on two cases, and the pendulum slips

    core gross             1d + 1k   1j      1l (1j + 1k)   default   the menu (1l, mean candidates per cell)
    box, weave 11           6.6%     29.2%   18.1%                    66
    box, weave 13          16.1%     30.5%   20.5%                    88
    box, weave 19           8.7%     17.3%   14.9%                    38
    box, weave  3           9.4%     17.7%   13.5%                    96
    box, weave  5          24.9%     29.7%   28.2%                    55
    box, noise 11           2.9%      3.5%    3.5% (0.0% changed)
    spin-constant, lattice 53.7%     53.2%   53.7%          53.2%
    spin-pendulum, lattice 29.3%     29.1%   30.7%          28.1%
    spin-constant, noise    6.5%      7.5%    7.5% (0.0% changed)

- **E7 MISSED on 11 (+11.5) and 19 (+6.2);** 13, 3 and 5 are within 5 points.
- **The pendulum lattice is 2.6 points worse than the default** (the line is 2), as with 1k on 1i (3.1).
- **So 1k on the rival lattice lets wrong picks through on rotating exact prints.** The likely route: both candidates
  offered fall in one basin (an alias), so the only rival left is w, and on a rotating print one alias can beat w by
  the margin locally.
- **The cost is the menu:** 38-96 candidates per cell, each ranked by nine 16 x 16 SADs. That is roughly 200-450
  thousand fetches per gated cell, before the lattice's 40-60 thousand. A shader cannot pay that.

### Pre-registered: lead 4's step 1k2 and three cost cuts, one change each (before they ran)

- **1k2 (RESCORE_STEP=1k2):** the two candidates OFFERED are different basins. The second is the best-ranked one
  more than 2 px from the first, so the uniqueness test always meets a real rival when the menu holds one.
  - Measured on step 1d's lattice (against 1d + 1k) and on 1j's (against 1l).
  - **U9:** the weave within 2 points of its reference, and the pendulum lattice within 2 points of the default on
    both lattices.
- **The cost cuts, each alone against step 1l:**
  - **1m (RESCORE_RANK=exact):** each candidate ranked by one SAD at its own position, not nine over +-0.5 px. That
    makes ranking 9 times cheaper. The ranking is no longer by integer rounding, which was 1b's fault.
  - **1n (RESCORE_MENU=small):** the menu is the DISTINCT neighbour flows (within 1 px) and the nearest lattice steps
    only (n, m in -1..1).
  - **1o (RESCORE_SELF=sparse):** the lattice's self-match on 8 x 8 samples at 4 px, not 16 x 16 at 2, which is 4
    times cheaper.
  - **C1 (each):** every weave case within 3 points of 1l, and the controls as in 1l (noise under 1 percent changed;
    the rotating lattices no further from the default than in 1l).
  - **Reported:** the menu size and the self-match fetches per cell.

### Results: lead 4's step 1k2 and the three cost cuts (the M5)

    core gross             1d+1k   1k2 (FFT)   1l      1k2 (1j)   1m exact   1n small   1o sparse   default
    box, weave 11           6.6%    6.8%       18.1%   18.3%      37.5%      16.6%      17.7%
    box, weave 13          16.1%   16.3%       20.5%   20.7%      40.7%      17.9%      20.5%
    box, weave 19           8.7%    8.8%       14.9%   15.0%      48.5%      12.8%      15.0%
    box, weave  3           9.4%    9.8%       13.5%   13.9%      30.6%      12.2%      13.4%
    box, weave  5          24.9%   24.9%       28.2%   28.2%      61.3%      22.8%      28.2%
    box, noise 11           2.9%    2.8%        3.5%    3.5%       3.5%       3.5%       3.5%       3.5%
    spin-constant, lattice 53.7%   53.4%       53.7%   53.3%      53.6%      53.8%      53.7%      53.2%
    spin-pendulum, lattice 29.3%   28.5%       30.7%   29.7%      30.7%      31.0%      30.7%      28.1%
    spin-constant, noise    6.5%    6.5%        7.5%    7.5%       7.5%       7.5%       7.5%       7.5%

- **U9 PASSED on both lattices.** Offering two distinct basins keeps the weave within 0.4 points of its reference
  and brings the pendulum lattice back inside the 2-point line (29.7 on the rival lattice; 28.5 on the FFT one).
- **1m (exact ranking) MISSED, badly:** 17-34 points worse. The +-0.5 px search before ranking is load-bearing:
  without it a candidate half a pixel off loses to an alias, which is stage 1a's and 1c's lesson a third time.
- **1n (the small menu) is BETTER on every weave case** (1.3-5.4 points), with 16-41 candidates instead of 38-96: fewer
  distractors. Its controls sit 0.1 / 0.3 further from the default than 1l's on the rotating lattices, so C1 is
  missed as worded, by 0.3 at most.
- **1o (the sparse self-match) PASSED:** within 0.5 points of 1l, the controls identical, at 10-15 thousand
  self-match fetches per cell instead of 38-59.

### Pre-registered: lead 4's steps 1p and 1q, and the GLSL form's equivalence check (before they ran)

- **1p (RESCORE_RANK=sparse):** the ranking's SAD on every other pixel of its 16 x 16 block, a quarter of the
  fetches, with the +-0.5 px search kept. Alone, against 1l. **C2:** every weave case within 3 points of 1l, and the
  controls as in 1l.
- **1q, the combination for the GLSL form:** 1k2 + the rival lattice of 1j + 1n + 1o (RESCORE_STEP=1k2
  RESCORE_LATTICE=rival3 RESCORE_MENU=small RESCORE_SELF=sparse). Also 1q + 1p.
  - **E8:** every weave case at or below 1l. The controls: noise under 1 percent changed; the rotating lattices
    within 2 points of the default.
- **G1, the GLSL form** (tests/print_lattice.py, the switch PRINT_LATTICE=1, built as 1q). On the default's recipe
  WITHOUT OUTLINE_ADOPT, so its input is 1q's input; its flow tapped after its apply pass.
  - **The box's core gross within 5 points of 1q on every weave case.** The emulations differ in small ways: ALIAS_E's
    magnitude prior, luma from RGB, and a bounded completion.
  - **Then the picture** (the sweep's box PSNR), the ladder on the Arc, real footage and the time, as for
    OUTLINE_ADOPT.

### The GLSL form built (tests/print_lattice.py, PRINT_LATTICE=1), and a second instrument fault, found by G1

**The switch** (three passes per direction: the lattice and the re-score at the 1/8 grid, cached per source pair, and
the apply at the quarter level; after the adoption's passes). On the default's recipe both 1.0.3 and the adopted
default still regenerate byte-identical with it off. It compiles, and it changes the picture (no silent fallback).

**G1, first reading:** the box's core gross through a tap after its apply was 20.9 / 32.7 / 14.6 / 17.4 / 15.3
percent (weave 11 / 13 / 19 / 3 / 5), noise 3.5. Weave 13 was 15 points behind offline 1q.

**The fault, located through four diagnostic shaders** (np-scratch/weave/variants/print-lattice-diag*.glsl):
- **The reading samples its 1/8 field at pixel 8i + 4.5.** So every tapped value is bilinear: 15/16 of its own cell
  and 1/16 of the next, right and below. A known per-cell pattern read back as 0.25 / 4.25 / 8.25 / 11.25 for
  0 / 4 / 8 / 12.
- **Deconvolved** (six Jacobi sweeps under the bilinear model):
  - the shader's own 1/8 offsets match the offline emulation in 1,496 of 1,506 core cells;
  - its lattice is the full one wherever it was computed that frame.
- **The cause of the gap:** every offline step from 1b to 1q took its INPUT field through that same tap, so each
  cell's seeds and w carried 1/16 of a neighbour. That made the menu slightly richer than any shader's. Offline 1q
  on the deconvolved input: 21.7-27.6 percent per frame on weave 13. The shader, deconvolved: 23.3-28.6. **G1 holds
  on the corrected instrument, within 1.6 points per frame.**
- **rescore1.py now has RESCORE_UNBLEED=1,** off by default so the recorded steps reproduce. The re-measures of 1q,
  the shader and the 1k2-on-FFT reference with it are running.

### Results: the picture, PRINT_LATTICE on the adopted default (the M5, weavesweep.py, equal footing)

    box PSNR-Y, dB    the default (adopted)   + PRINT_LATTICE   linear   change
    weave  3          39.70                   39.80             26.74     +0.10
    weave  5          26.05                   37.78             21.33    +11.73
    weave 11          15.83                   20.24             13.86     +4.41
    weave 13          15.12                   19.56             13.09     +4.44
    weave 19          15.83                   23.79             14.32     +7.96
    noise 3/5/11/13/19   51.06 / 43.43 / 48.26 / 45.33 / 43.98   identical   0.00 at every speed

- **Weave 5 (+11.7 dB):** the adoption's half-repaired case. Its picture is now repaired.
- **The fast weave gains 4.4-8.0 dB.**
- **Noise is untouched.**
- No prediction was registered for these numbers beyond "measure".

### Pre-registered: PRINT_LATTICE's gates, as OUTLINE_ADOPT's (before they ran)

- **L1 (the full ladder, the NAS's Arc, against the adopted default in the same sitting):** the capped mean within
  0.1 of it or above, and no case down more than 1 dB.
- **L2 (real footage, the half-rate test on the census's 40 film extracts):** no extract's unflagged median down more
  than 0.3 dB.
- **L3 (time):** reported on O5 (no print in the frame) and on the weave box. The switch's cost is where the gate
  opens, so both are needed.
- **L4 (Metal):** the demo engine on the same frames as libplacebo (REC_RGBIN), the weave box within 0.5 dB.

### Results: the corrected instrument (RESCORE_UNBLEED=1), and L1 on the Arc

    core gross (deconvolved)  T2 (input)   offline 1q   the shader (G1)   1k2 on the FFT lattice
    box, weave 11             97.9%        17.3%        18.9%              9.1%
    box, weave 13             99.1%        28.1%        29.7%             27.6%
    box, weave 19             96.6%        12.7%        13.1%              8.7%
    box, weave  3             58.3%        11.4%        13.3%             11.2%
    box, weave  5             88.6%        19.9%        13.3%             22.1%
    box, noise 11              4.0%         4.0%         4.0%              3.1%
    spin-constant, lattice    51.6%        51.9%        51.8%
    spin-pendulum, lattice                               29.0%

- **G1 PASSED:** the shader is within 2 points of offline 1q on every weave case (5 better on weave 5), with noise and
  the rotating lattice untouched.
- **The bleed had flattered every offline number:** weave 13 was 16-18 percent and is 28. On true input the rival
  lattice is close to the FFT lattice (within 8 points at worst, on weave 11).

**L1 MISSED, badly** (the full ladder on the Arc, PRINT_LATTICE on the adopted default, same sitting; 4 min each):
- **The capped mean is 38.174 against 38.357 (-0.18).** 10 cases are down more than 0.3 dB.
- **One-dimensional prints are hit hardest:** V1_bars_sine24_v6 -13.0, H1_bars_sine24_h6 -10.4; the stairs H2 / V2 / V3
  -2.2 to -2.5, and P4 -2.3.
- **Small losses on textured cases:** L7 -0.65, O6 -0.52, P1 -0.50, O5 -0.41. R1 is up 0.70 and R2 up 0.31.
- **The mechanism, by design reading:**
  - on stripes every shift ALONG the stripe matches, so the self-match accepts along-stripe vectors as "lattice"
    vectors;
  - the completion multiplies them;
  - the menu then offers candidates that are right across the stripes and wrong along them;
  - one wins by a small SAD difference, which is invisible inside the stripes but tears the moving patch's ends.
- **The weave sweep could not show this:** its print is two-dimensional. The ladder was the right gate.

### Pre-registered: lead 4's step 1r, a lattice vector must be an ISOLATED minimum (before it ran)

One change, to the lattice (offline RESCORE_ISOLATE=1; in the shader, the same rule in the lattice pass): a kept
vector's self-match cost must rise on every side. Its 8 neighbours at +-2 px must all cost at least max(2 c, c + 0.15
MAD). An along-stripe vector fails it, since moving along the stripe costs nothing; a weave vector passes.
- **R4 (offline, the corrected instrument):** every weave case within 3 points of 1q; noise and the rotating lattice
  untouched.
- **R5 (the ladder on the Arc):** L1's lines, the capped mean within 0.1 of the adopted default and no case down more
  than 1 dB.
- Then the picture again, L2 (real footage), L3 (time) and L4 (Metal).

### Results: lead 4's step 1r: R4 and R5 PASSED, L4 PASSED, L3 MISSED by a wide margin

- **R4 (offline, deconvolved):** 1r equals 1q on every weave case within 0.1 point. Noise and the rotating lattices
  are unchanged.
- **R5 (the ladder on the Arc, against the adopted default):**
  - the capped mean is 38.342 against 38.357 (-0.015);
  - one case is down more than 0.3 (L7_textured_large -0.65) and none more than 1 dB;
  - every stripe case is back to 0.00 (V1, H1, V2, H2, V3, P4); R1 and R2's small gains are gone too.
- **The picture (the sweep, YUV in, against the adopted default):**
  - the weave +0.10 / +11.18 / +4.37 / +4.36 / +7.73 dB (3 / 5 / 11 / 13 / 19 px/frame);
  - noise 0.00 except +0.63 at 5 px/frame.
- **L4 (Metal, the demo engine, on the same rgb48le frames as libplacebo):** the weave 5 / 11 / 13 / 19 within
  +0.23 / +0.01 / -0.05 / +0.37 dB.
  - On that input path weave 5 reads 29.9 dB against the adopted default's 19.0: the lattice also repairs the
    5-px case that the adoption repairs only on libplacebo's own YUV path.
- **L3 (time, the M5, timing_adopt.sh, three interleaved rounds, ms per output frame at 720p):**

      source                       the adopted default   + PRINT_LATTICE   change
      O5 (synthetic, no print)     10.28                 21.27             +107%
      the weave box at 11 px       8.29                  32.70             +294%
      avengers, 3 s                11.73                 15.29             +30%
      bttf, 3 s                    11.54                 16.63             +44%
      street, 3 s                  12.08                 18.88             +56%

  - Profiled on O5: the gate and the offsets' gather +0.7 ms, the lattice +2.5, the re-score +7.6.
  - **Two causes:** the gate opens on ordinary texture (O5's sines), and each opened cell runs one long serial loop
    (about 30 candidates x 9 positions x 256 taps) on ONE thread. Few cells mean a latency-bound GPU, many cells mean
    the work itself.
  - **The adoption cost +9.6 percent; this costs 3-5 times its budget.** It is not adoptable as built.

**Next, the cost, in measured steps (each quality-checked offline and on the ladder, and timed):**
1. a two-stage ranking: a cheap 4 x 4-sample SAD over the whole menu, then the full 16 x 16 for the best four;
2. one thread per candidate instead of per cell (the menu written to a texture, ranked in parallel);
3. a tighter gate: the cell's OWN margin, not any of its 5 x 5 cells.

### Pre-registered: the cost cuts C1 and C3, offline, one change each against 1r (before they ran)

- **C1 (RESCORE_RANK2=1):** the two-stage ranking. 4 x 4 samples at 4 px over the whole menu with the +-0.5 px search,
  then the best four by the full rough rank.
- **C3 (RESCORE_GATE=own):** a cell opens only where its OWN 1/8 margin is under 0.3. The offsets are still gathered
  from its 5 x 5 cells.
- **Each:** every weave case within 3 points of 1r (deconvolved), and the controls as in 1r.
- **Then in the shader:** the time on O5 and the three clips, against L3's line (the adoption's +10 percent as the
  order of a default's budget).

### Results: C1 PASSED, C3 MISSED; L2 PASSED; where the cost really is

    core gross (deconvolved)   1r      C1 (two-stage ranking)   C3 (own margin)
    box, weave 11              17.3%   17.4%                    43.8%
    box, weave 13              28.1%   28.2%                    54.2%
    box, weave 19              12.6%   13.8%                    42.5%
    box, weave  3              11.4%   11.6%                    29.6%
    box, weave  5              19.9%   21.4%                    43.1%
    controls (noise, the rotating lattices): as 1r in both

- **C1 PASSED** (within 1.5 points). **C3 MISSED, badly:** the weave's interior needs the 5 x 5 window. Many of its
  cells have no low margin of their own.
- **L2 PASSED (1r's form, the NAS's Arc, all 40 film extracts against the adopted default):** the unflagged medians move
  +0.00 to +0.08 dB, and only 2 extracts change at all. On real footage the switch is harmless and almost never acts.
- **The shader with C1 + C3 (time, the M5):** real clips +19 / +23 / +27 percent (from +30 / +44 / +56), O5 +80, the
  weave box +116. Profiled on the street clip, the LATTICE pass is almost all of it.
- **Why real footage pays for nothing:** the 5 x 5 gate opens on 28-60 percent of a real clip's cells. Their offsets
  are refined, and the isolation test then rejects nearly all of them.
- **How many of a cell's 25 cells have a margin under 0.3** (the share of opened cells with at least M):

      M                    1      3      5      8      12
      weave 5 core         100    99.9   99.6   96.7   82.3
      weave 11 core        100    100    99.5   95.7   80.6
      weave 19 core        100    100    99.3   93.8   76.0
      avengers (1 s)       100    42.1   22.1   9.5    3.1
      bttf                 100    72.6   55.1   36.0   18.7
      street               100    66.2   45.4   25.1   10.4

### Pre-registered: the cost cuts C4 and C5, offline, one change each against 1r (before they ran)

- **C4 (RESCORE_GATE=ext5):** a cell opens only if at least 5 of its 5 x 5 cells have a margin under 0.3. A print is
  extended; real footage's rivals are sporadic. By the table it keeps over 99 percent of the weave's core.
- **C5 (RESCORE_SELF=coarse):** the lattice's +-4 px stage on 4 x 4 samples (16 taps), with the 8 x 8 kept for the
  final +-1 px and the isolation test.
- **Each:** the weave within 3 points of 1r, and the controls as 1r.
- **Then the shader with C1 + C4 + C5,** timed (O5, the three clips, the weave box) and gated on the ladder.

### Results: C4 and C5 PASSED; the shader made cheaper, step by step (time on the M5, ms per output frame, 720p)

- **C4 (at least 5 of 25 low margins) and C5 (the coarse self-match), offline:** within 0.3 points of 1r on the weave;
  the controls unchanged.
- **The shader, each row one change; every restructure checked IDENTICAL** (md5 of 60 rendered frames on the weave
  5 / 11 / 19 and noise):

      change against the adopted default        O5      avengers   bttf     street   the weave box
      1r (PRINT_LATTICE as gated)                +107%   +30%       +44%     +56%     +294%
      + C1 + C4 + C5                             +83%    +12%       +20%     +22%     +156%
      + the lattice's offsets one thread each    +83%    +9.3%      +15.4%   +11.9%   +149%    (4 passes per direction)
      + the re-score split across threads        +40%    +14%       +16%     +16%     +87%     (8 passes per direction)
      + one gather, no writes when idle          +41%    +15%       +18%     +17%     +91%     (9 passes per direction)

- **What the profile and the rows say:**
  - on real footage the lattice pass was nearly all the cost, and C4 + C5 + one thread per offset brought it to
    +9-15 percent;
  - on prints the re-score's serial loops were the cost, and splitting them across threads halves it;
  - but every extra pass costs on real footage, because the passes run on every OUTPUT frame (about 2.5 per source
    pair) even when they only return their cache. Dispatch count is the floor, as the cost probe found before.
- **Not yet within a default's budget** (the adoption: +9.6 percent). Next: fewer passes (the selection merged into the
  refine and the decision), and a cheaper refine, offline first.

### Results: fewer passes, then FUSION (one pass carries both directions), identical output throughout

      change against the adopted default        O5      avengers   bttf     street   the weave box
      7 passes per direction (selection merged)  +41%    +12.9%     +15.1%   +15.9%   +87%
      the dispatch floor (7 passes, never active)         -          -        +11-12%     -
      FUSED: 6 passes for both + 2 applies       +28%    +10.0%     +13.0%   +12.3%   +55%

- **The floor probe settled it:** with nothing ever active, the 14 per-direction passes alone cost about 11 percent on
  the street clip. On real footage the cost was dispatch, not work.
- **The fusion is mechanical** (print_lattice.py `_fuse`: the two per-direction bodies in one pass, the texel's half
  of the output picking the direction). It is md5-identical on the weave 5 / 11 / 19 and noise.
  - The first build failed to compile (a global declared after its use), and libplacebo SILENTLY fell back to its
    own mixer. The md5 check caught it: the output differed even on noise, where the switch never acts.
- **The fused form (C1 + C4 + C5, md5 143811e7):**
  - **the picture:** the weave +0.10 / +11.64 / +4.32 / +4.34 / +7.44 dB (3 / 5 / 11 / 13 / 19 px/frame); noise 0.00 at
    every speed, so C4 removed 1r's +0.63 at 5 px;
  - **Metal** (the demo engine, the same rgb48le frames): within 0.42 dB on the weave and noise;
  - **the ladder and real footage** are running on the Arc.
- **The time is now at the adoption's level on real footage** (+10-13 percent against +9.6). It runs +28 percent on
  O5's synthetic texture, and +55 percent where a print fills the frame's moving region (the weave box).

### Results: the fused form's gates (the NAS's Arc): L1 and L2 PASSED

- **L1 (the full ladder, against the adopted default, same build):**
  - the capped mean is 38.336 against 38.357 (-0.021);
  - one case is down more than 0.3 dB, L7_textured_large at -0.88 (inside the 1 dB line; 1r's form had -0.65); every
    stripe case holds.
  - **L7 is an exact periodic print** (period 15.7 px) moving at about its own period, M3's trap. Its aliases tie
    up to interpolation error, so the uniqueness test cannot fully protect it. It is lead 3's territory, recorded
    as open.
- **L2 (real footage, all 40 film extracts):** the unflagged medians move -0.01 to +0.08 dB, only 2 extracts change at
  all, and the even-frame control is untouched.

**Where PRINT_LATTICE stands (the fused form, np-scratch/weave/variants/print-lattice10.glsl):**
- **The picture:** the fast weave +4.3 to +7.4 dB, and the adoption's half-repaired 5-px case +11.6 (+10.9 on Metal's
  input path). Noise is untouched.
- **The gates:** the ladder passed, real footage passed, Metal agrees.
- **Time:** +10-13 percent on real footage (the adoption's level), +28 percent on synthetic texture, +55 percent where
  a print fills the moving region.
- **Owed before any adoption (the owner's call):**
  - the 4K twin: scale_shader.py has no rules yet for these passes' frame-pixel constants (8-px cells, 16 x 16 blocks,
    the 8-40 px lattice);
  - the Cadence bundle and the lockstep;
  - L7's -0.88.

### The owner's two decisions (2026-10-01, morning), and the tiers' costs

- **Lead 2 (the impact mode) is not for Cadence.** A four-frame window goes beyond simple film footage and would
  likely be too slow for real time; its applications are most likely scientific. It is parked for the player.
- **The tier rule:** when several candidates are fit for purpose, performance decides. Candidates whose cost is very
  close collapse into one; the rest become quality tiers in the player's Settings, with the 4K twin chosen by the
  source.
- **The lattice's 4K twin is built** (d3c0015). **Its costs were measured on three machines** (the Cadence tree's
  CADENCE.md, "The quality tiers").
  - On ordinary footage it costs 2-15 percent over the default.
  - **On a frame filled by a moving print it is UNBOUNDED:** 37 ms at 1080p and 70 ms at 4K on the M5, against 11
    and 14 for the default.
- **Lead 4's next item is therefore a cost cap,** a runtime self-gate (a reduction pass counting the opened cells,
  then a rotating subset above a share), measured on the full-frame weave pan.

### Pre-registered: the lattice's COST CAP (the owner's go, 2026-10-01; before it ran)

The target is the Apple-silicon Mac. The owner's word: the Intel Mac's eGPU and the Arc are not target systems. The
cost is unbounded because every cell the print gate opens runs the full lattice and re-score. The cap bounds the
NUMBER of such cells, at run time, with no pre-flight:
- **A gate pass** flags each cell that would open (moving; at least 5 of its 25 cells' margins low; an offset), and
  two small passes count the flags per direction (rows, then the frame).
- **Over a budget of B = 4000 cells per direction** (about an eighth of a 1080p frame's 1/8 grid; the weave box at
  1080p opens about 2,300), only the cells on a stride grid run, s = ceil(sqrt(N / B)): one cell in s x s, at a FIXED
  phase so the same cells run on every pair (no flicker).
- **The other opened cells borrow:** a propagation pass tries the nearest running cell's correction (its lattice
  step, the re-scored vector minus its flow) on the cell's own flow. It is kept only if it beats the flow by the same
  1/255 margin at full resolution (a +-0.5 px search). A cell on an exact print, where the two tie, keeps its flow.
- **Under the budget nothing changes:** every opened cell runs, as now.

The predictions:
- **K1:** the output is md5-identical to the uncapped form wherever fewer than B cells open (the street clip, the weave
  box).
- **K2:** the full-frame weave pan at 1080p on the M5 (Metal) within 16.7 ms per output frame (real time at 60;
  uncapped: 37.1). At 4K within 20.8 (real time at 48; uncapped 69.7).
- **K3:** on the full-frame weave pan, the capped form keeps at least 70 percent of the uncapped form's PSNR gain over
  the default (weavesweep.py, a full-frame mode).

### Results: the cost cap (the M5, Metal, the player's path): K1 and K3 PASSED; K2 PASSED at 1080p, MISSED at 4K

- **K1 PASSED:** md5-identical to the uncapped form on the weave 5 / 11 / 19, noise, and the 1080p street and
  weave-box clips (all under the budget).
- **K3 PASSED** (the full-frame weave pan, weavesweep.py WEAVE_FULL=1, 720p, PSNR over the frame):

      speed   linear   the default   uncapped        B = 4000 (stride 2)     B = 1600 (stride 3)
      11      13.97    15.30         21.86 (+6.56)   21.49 (+6.19, 94%)      20.09 (+4.79, 73%)
      5 / 19  22.28 / 14.69   19.18 / 12.36   no gain (+0.00) in any form
      noise 5 / 11 / 19: identical in every form

  - **A side finding:** on a print filling the frame, the lattice repairs 11 px/frame but not 5 or 19, where the
    default stays below the blend. Recorded as open.
    *2026-10-01, afternoon: explained. It was not the field: at 5 and 19 px/frame the scene-cut gate held a frame on
    every pair, so nothing the lattice computed was drawn ([C1](#the-per-level-trust-gate-returned-to-2026-10-01-afternoon-t0-the-diagnosis-before-the-build)).*
- **The first capped build was 20.0 ms (full-frame pan, 1080p) against the uncapped 37.2.** The profile found the
  borrowing pass cheap (0.6 ms) and the subset itself expensive: 3,400 cells scattered on a stride grid cost 8.4 ms,
  where the weave box's 2,300 contiguous cells cost 1.8. A stride grid puts a few busy lanes into almost every SIMD
  group.
  - **Fix (labelled, after the profile):** the running cells are PACKED. Thread (x, y) works on cell (x, y) x s, and the
    intermediate textures are indexed compactly. The output is md5-identical to the scattered form on both
    full-frame sources.
- **K2, packed** (ms per output frame, 24 -> 60, the median of three rounds):

      clip               the default   capped + packed   (uncapped)
      street 1080p       9.93          10.39 (+4.6%)     10.37
      weave box 1080p    7.16          9.07              9.07
      full-frame 1080p   10.91         16.18 (+48%)      37.16     K2 PASSED (under 16.7: real time at 60)
      static 1080p       10.10         10.24             10.28
      street 4K          11.92         13.47             13.68
      weave box 4K       9.06          12.37             13.28
      full-frame 4K      13.39         24.83 (+85%)      70.31     K2 MISSED (over 20.8)


### Pre-registered: a smaller budget, B = 2000 (labelled follow-up to K2's 4K miss; before it ran)

- **K2':** the full-frame pan at 4K within 20.8 ms (real time at 48) and at 1080p within 16.7, the M5, packed.
- **K3':** at the stride a 1080p or 4K frame then gets (4), the full-frame weave keeps at least 70 percent of the
  uncapped gain. Emulated at 720p with B = 900; B = 2000 at 720p is reported too.

### Results: B = 2000: K2' PASSED, K3' MISSED; the shipped choice, a budget per size

    full-frame pan (the M5, ms)   the default   B = 4000   B = 2000
    1080p                         10.91         16.22      13.75
    4K                            13.38         24.83      19.70     (K2' PASSED: under 20.8)
    street 1080p / 4K             9.91 / 11.89  10.38 / 13.42   10.23 / 12.90   (B = 2000 engages on real footage too)

- **K3' MISSED:** the stride a 1080p frame gets at B = 2000 (4, emulated at 720p with B = 900) keeps 60 percent of the
  uncapped gain on the full-frame weave (19.25 against 21.86 and the default's 15.30). At stride 3 it keeps 73 percent.
- **The budget is a straight trade between time and gain on frame-filling prints.** The shipped files take one per
  size:
  - the 1080p graph keeps B = 4000: the full-frame pan in 16.2 ms, real time at 60, about 73 percent of the gain on
    such a frame;
  - the 4K twin gets B = 2000: scale_shader.py divides the budget by the frame factor, since a 4K cell's samples lie
    twice as far apart and cost about twice as much. That gives 19.7 ms, real time at 48, at about 60 percent.
- **Under the budget nothing changes.** The shipped 4K twin is md5-identical to the uncapped one on the weave box at
  twice the size, and the 1080p file to the tested one.
- **The capped files' gates (the NAS's Arc):**
  - **the ladder:** identical to the uncapped form (capped -0.021, the worst L7 -0.88); every case is under the
    budget;
  - **real footage (the 40 extracts):** -0.01 to 0.00 against the default. One extract crossed the budget and gave up
    the uncapped form's +0.08 there.
- **The lattice, capped, is a valid candidate for a quality tier on the target machine** (the Apple-silicon Mac):
  real time at 1080p60 and 4K48 even on a frame-filling print pan, and +2-15 percent on ordinary footage.

### Parked by the owner (2026-10-01, morning): the per-level trust gate, to return to within hours

Never built. Lead 4's re-score was built in its place for fast prints. The trust gate stays the candidate for what the
lattice cannot reach: a print filling the frame at 5 and 19 px/frame, where the default sits below the blend and the
lattice gains nothing. Its design is in PRIOR-ART.md "Before lead 4", item 2:
- a per-level, per-texel contrast test (point-sampled against box-filtered);
- a flagged level gives flat data and no seed;
- the first unflagged level searches wide.
Its risk: the interior still ties at the quarter level, so the lattice or the outline carry would follow it. Lead 3
(the rigid repair) stays parked for its own reason (the in-shader comparison).

*2026-10-01, evening: returned to and built ([below](#the-per-level-trust-gate-returned-to-2026-10-01-afternoon-t0-the-diagnosis-before-the-build)). The frame-filling pan turned out to be the scene-cut gate's; the trust gate, with its aliasing flag and lead 4's uniqueness test, passes the ladder and real footage ([where it stands](#where-the-per-level-trust-gate-stands-2026-10-01-evening)).*

### The per-level trust gate, returned to (2026-10-01, afternoon): T0, the diagnosis before the build

The owner's word on his return: continue the per-level trust gate "to its natural conclusion", using the three
machines.

**T0, a diagnostic.** No prediction was registered; it reads, it does not decide. `tests/probes/trust/leveltap.py`
taps the player's default (the High tier, `...-carry-adopt-lattice.glsl`) right after each stage: the global shift,
the four 1/16 seeds, the 1/8 level's two basins and margin, the 1/8 refine and its check, the quarter refine, the
carry's pick, the adoption, the lattice's gate and apply, and the final half-level field in both directions. Each
quantity is copied by an exact texel fetch at the 1/8 grid and read through the reading tail at N:N, on
weavesweep.py's scene (the box, or with `WEAVE_FULL=1` the frame-filling pan).

**What it found first, on the parked target (the frame-filling weave pan, the M5):**

    v px/f   final field A->B: exact / gross   B->A: exact / gross   the scene-cut statistic (per frame)
     5        66.3% / 21.0%                    69.9% / 18.6%         0.15-0.17
    11        61.6% / 22.3%                    62.8% / 21.4%         0.11-0.13 (median 0.118)
    19        73.5% / 12.5%                    76.0% / 11.0%         0.15-0.17
    (exact: the cell reads the true vector to the nearest pixel; gross: more than 2 px off)

- **The field on a frame-filling print is mostly RIGHT at 5 and 19 px/frame,** as right as at 11 px/frame, where the
  lattice's picture gained 6.6 dB.
- **The scene-cut statistic reads 0.15-0.17 there.** It is the mean |A - B| on a sparse grid of the 1/16 level, and
  above 0.125 the warp is a hard switch to the nearer source frame (TESTING.md, "Scene cuts"): a HOLD. At 11 px/frame
  the print moves only 3 px out of phase (14 - 11), the statistic sits around 0.118, and the warp runs.
- **So the parked target is not a lock of the field: it is the cut gate.** The gate measures how different two frames
  are, not whether motion explains the difference, and a high-contrast print panning by about half its period looks
  like a cut. The lattice "gained nothing" at 5 and 19 because nothing it computed was drawn.

**Pre-registered: C1, the counterfactual (before it ran).** The same shader with the cut gate out of reach (the one
constant `SCENE_CUT_DIFF` set to 1e9, asserted), `weavesweep.py` with `WEAVE_FULL=1`, the weave and noise at 5, 11
and 19 px/frame, on the NAS's Arc (deterministic), against the unchanged shader in the same sitting:
- **C1a:** at 5 and 19 px/frame the picture rises from below the blend to at least 3 dB above it.
- **C1b (the control):** at 11 px/frame it moves by less than 0.5 dB. Most frames' statistic is under the threshold,
  and only the few above it can move.
- **C1c:** noise is unchanged wherever its statistic stays under 0.125 (T0 reads it on the same frames).
- **If C1a fails,** the field's 12-21 percent gross is enough to sink the warp, and the trust gate's target stands as
  parked.

**Results: C1 PASSED on all three (the NAS's Arc, one sitting).**

    full-frame pan, PSNR-Y over the frame (dB)   linear   the default   the cut gate out of reach   change
    weave  5                                     22.28    19.18         25.81                       +6.63
    weave 11                                     13.97    21.71         21.72                       +0.01
    weave 19                                     14.69    12.36         23.23                      +10.87
    noise 5 / 11 / 19                            44.92 / 37.07 / 32.17   54.73 / 53.47 / 51.82   identical   0.00

- **C1a PASSED:** at 5 and 19 px/frame the picture goes from 3.1 and 2.3 dB below the blend to 3.5 and 8.5 dB above it.
- **C1b PASSED:** at 11 px/frame it moves by 0.01 dB.
- **C1c PASSED:** noise is identical.
- **The finding:** the side finding recorded under the cost cap ("on a print filling the frame, the lattice repairs
  11 px/frame but not 5 or 19") was not the field. The field was right, and the warp never drew it: the cut gate
  held a frame. Its fix is a cut gate that asks whether motion explains the difference (C2, below), not a trust gate.

**T0 on the box (the M5), while C1 ran: the lock enters at the coarsest level, at every speed.** On the weave box the
four 1/16 seeds are wrong at every speed: +18 to +32 px at 3 and 5 px/frame (the moire's own motion, not a period of
the print) and v - 28 at 11 and 13. The 1/8 level's best basin is wrong too (-24 or -16 px, with every margin low).
Only the adoption (the outline, at 3 and 5) and the lattice (at 11) pull the field back, and the half level loses
some of the lattice's gain again (weave 11: 20.8 percent gross after the lattice, 31.7 in the final field).

**Pre-registered: T1, which flag says "this level is aliased here" (offline, before it ran).**
`tests/probes/trust/flag.py` builds each level as the shader does (the point sample) and beside it the box over the
texel's footprint, and computes three candidate flags per texel over the level's 5 x 5 window: A, the range of the
box against the range of the point samples; B, the same for variances; C, the window's rms frequency (Rice's mean
frequency, from the full-resolution gradient) against the level's Nyquist. Each is reported as the share of textured
texels it fires on, per level, on the ladder's and the masters' textures (the Intel Mac's CPU) and on 8 frames from
each of the census's 20 real sources (the NAS).
- **F1:** flag C at kappa 1 fires on at least 80 percent of the weave's textured texels at the levels W2 and W3
  located (P = 10 and 14: 1/8 and 1/16; P = 20: 1/16 only) and on at most 20 percent elsewhere (P = 20 at 1/8; every
  P at 1/4).
- **F2:** flags A and B separate those levels less cleanly. A box 8 px wide keeps about half of a 14-px thread's
  amplitude, so at 1/8 the weave P = 14 is not far from unaliased content on these two.
- **F3:** on the masters' noise, cells and wood (aperiodic, broadband) flag C fires on at most 20 percent at 1/8.
- **F4, real footage (no confident number):** natural images put much of their gradient energy at fine scales, so
  flag C may fire widely: over 50 percent of textured texels at 1/16, between 30 and 60 at 1/8. If it does, a flag
  of fine detail is not a flag of a misleading level, since an aperiodic texture aliases into a decorrelated coarse
  image, not a coherent moire. The gate would then need a second, periodicity term before it is specific.

**Pre-registered: T2 offline, the first honest level's wide search (before it ran).** For P = 14 the quarter level is
the first that sees the weave unaliased (T1). `tests/probes/trust/wide.py` emulates what the gate would do there on
the weave box's core: every whole-texel offset within +-24 px, the 5 x 5 window's mean absolute difference plus a
small-motion prior lambda per px, the best refined by a parabola. At 1/4 the print's aliases still tie up to its fine
noise, so the search cannot be asked for the truth everywhere; it is asked for a TRUE ALIAS (the truth plus a lattice
vector), which the lattice's full-resolution re-score can then resolve, and for the truth where the truth is the
shortest alias.
- **W1:** with a small lambda, the truth (within 2 px) on at least 90 percent of the core at 3, 5, 11 and 13 px/frame,
  where the truth is the shortest alias.
- **W2:** at 15, 16, 17 and 19 px/frame, a true alias (the truth or another) on at least 90 percent. There a shorter
  alias exists ((v - 14, +-14), or -9 at 19), so the prior will pick it and the lattice must turn it back.
- **W3 (the control):** noise read right on at least 95 percent at every speed and every lambda.
- **If the share on true aliases is low,** the quarter level cannot even separate the lattice from the garbage between
  it, and the gate in this form is dead.

**Results: T1 (the Intel Mac's CPU and the NAS): F1 and F3 PASSED, F2 half, F4 as feared.**

    share of textured texels flagged      1/16                      1/8                       1/4
                                          C>1     A<0.7   B<0.5     C>1     A<0.7   B<0.5     C>1     A<0.7
    weave P = 10                          100     100     100       100     100     100         0       0
    weave P = 14                          100     100     100       100     100     100         0       0
    weave P = 20                          100     100     100         0       0.9     0         0       0
    noise / cells / wood                    0 / 0 / 0  (A, B: 0-2)    0 / 0 / 0                 0       0
    TEX_M1 (five sines)                   100     100     100       100      97     100        69      23
    TEX_L7, TEX_M3 (periods 15.7, 16)     100     100     100       100     100     100         0       0
    real film, 20 sources x 8 frames
      median (largest)                    62 (88) 21 (39) 19 (32)   32 (63) 14 (36) 12 (30)   3 (20)  3 (15)

- **F1 PASSED:** the rms-frequency flag fires exactly at the levels W2 and W3 located (P = 10 and 14 at 1/8 and 1/16;
  P = 20 at 1/16 only) and nowhere else on the weave.
- **F2 half:** the box flags separate the same levels, but only at looser thresholds than registered: at 1/8 the
  weave P = 14 keeps 50-70 percent of its range in the box (A between 0.5 and 0.7), close to where unaliased content
  sits.
- **F3 PASSED:** none fires on the aperiodic broadband textures at 1/8.
- **F4, as feared:** on real film the frequency flag fires on a median 32 percent of textured texels at 1/8 and 62 at
  1/16; the box flag on 14 at 1/8. **No image-only flag is specific to a print.** It flags fine detail, which a real
  frame is full of, and fine aperiodic detail aliases into a decorrelated coarse image, not a coherent moire. The
  specificity has to come from the level's own AMBIGUITY: T0 shows the 1/8 level's rival-basin margin at 0.25 on the
  weave at every speed and at its ceiling (30) on noise. That is the lattice's own gate (5 of the 25 cells under 0.3),
  and it rarely opens on film.

**Results: T2 offline (the M5's CPU): W1 and W2 PASSED, W3 MISSED as worded; the prior must stay light.**

    the weave box's core: the truth / a true alias (the truth plus a lattice vector) / neither, percent
    v px/f    lambda 0           lambda 0.0005      lambda 0.002       lambda 0.008
     3        81 / 19 /  0       100 /  0 /  0      100 /  0 /  0      100 /  0 /  0
     5        80 / 20 /  0       100 /  0 /  0      100 /  0 /  0      100 /  0 /  0
    11        81 / 19 /  0        90 / 10 /  0       99 /  1 /  0       34 /  0 / 66
    13        80 / 20 /  0        90 / 10 /  0       99 /  1 /  0        0 /  0 /100
    15        81 / 19 /  0        68 / 32 /  0       22 / 78 /  0        0 /  0 /100
    16       100 /  0 /  0       100 /  0 /  0      100 /  0 /  0        0 / 76 / 24
    17        80 / 20 /  0        65 / 35 /  0       19 / 81 /  0        0 / 21 / 79
    19        81 / 19 /  0        36 / 64 /  0        1 / 99 /  0        0 / 98 /  2
    noise, read right at 3-19 px/f:  100 (lambda 0)   99.8-100 (0.0005)   52-99 (0.002)   0-13 (0.008)

- **W1 PASSED** (lambda 0.002: the truth on 99-100 percent at 3, 5, 11 and 13) and **W2 PASSED** (a true alias on
  100 percent at 15-19). At the quarter level the print's aliases are separated from everything between them on
  every texel: the first honest level is honest.
- **W3 MISSED as worded:** at 0.002 the prior drags noise towards small vectors (52-99 percent right), and at 0.008
  it collapses both. At 0.0005 noise is right on 99.8-100 percent and the weave lands on the truth or a true alias on
  100 percent at every speed. **The design value is 0.0005.** The prior does not decide between aliases there (the
  truth on 36-100 percent); the lattice's full-resolution re-score does.
- Unflagged at lambda 0 the search falls on the print's long alias (v - 28) a fifth of the time, so some prior is
  needed even on the weave.

**What the gate should do with the search, and T2b (pre-registered before it ran).** Replacing the flow with the wide
search's best would hand 11-13 px/frame the truth but hand 15-17, which read right today, a shorter alias for the
lattice to undo. Keeping the flow unless it is off the lattice would fix only the slow band's moire. The third way
is the record's own: the quarter level OFFERS, full resolution DECIDES (step 0: at full resolution the truth beats
every alias on 100 percent of blocks). `wide.py RANK=full`: the three best distinct minima of the quarter level's
13 x 13 surface (lambda 0.0005), each ranked by the 16 x 16 block's mean absolute difference at full resolution over
+-0.5 px.
- **W4:** the truth (within 2 px) on at least 95 percent of the weave box's core at every speed from 3 to 19.
- **W5 (the control):** noise right on at least 99.5 percent.

**Results: T2b (the M5's CPU): W4 and W5 PASSED.** The quarter level offering its three best distinct minima, full
resolution deciding: the truth (within 2 px) on 98.2-100 percent of the weave box's core at every speed from 3 to 19,
15-17 included; noise 99.9-100. The default's final field there is 0-34 percent gross.

**The GLSL form: `TRUST_GATE=1` (`tests/trust_gate.py`), two passes per direction,** after the carry's pick and before
the adoption and the lattice:
1. **the offer and the decision** (the 1/8 grid, one thread per cell, cached per source pair):
   - the gate: at least 5 of the 5 x 5 cells' rival-basin margins under 0.3 (the lattice's own gate);
   - the offer: every whole quarter texel within +-24 px, the 5 x 5 window's mean absolute difference plus 0.0005 per
     px, and its three best distinct local minima;
   - the decision: the 16 x 16 block centred on the cell at full resolution, each minimum and the cell's own flow over
     +-0.5 px; the best replaces the flow only if it beats the flow by 1/255 a pixel (the lossless fallback);
2. **apply** (the quarter level): the cell's 2 x 2 quarter texels take the decided vector.

With the switch off the default regenerates byte-identical. A first tap on the weave box at 11 px/frame: the gate
decides on about three quarters of the core's cells and leaves 29.5 percent gross; the adoption then takes it to 9.3
and the lattice to 0.4. The final field is 0.3 percent gross, against the default's 31.7.

**Pre-registered: T3, the picture and the gates (before they ran), `trust1` against the default in the same sitting.**
- **T3a (the field):** the weave box's final field at most 5 percent gross at every speed from 3 to 19.
- **T3b (the picture, weavesweep.py, the M5):** the weave box up at least 3 dB at 5, 11, 13 and 19 px/frame, and
  within 0.5 dB at 3, 15, 16 and 17, which read right today. Noise identical (its margins are high, so the gate never
  opens).
- **T3c (the frame-filling pan, the Intel Mac's RX 6600):** up at least 3 dB at 13 px/frame, where the warp runs; 5 and
  19 unchanged, since the cut gate still holds those frames.
- **L1 (the ladder, the NAS's Arc):** the capped mean within 0.1 of the default or above, and no case down more than 1 dB.
- **L2 (real footage, the 40 extracts' half-rate test):** no extract's unflagged median down more than 0.3 dB.
- **L3 (time, the M5):** reported on real footage, the weave box and the frame-filling pan. The gate opens only where
  the 1/8 level is ambiguous, so real footage should cost little; a frame-filling print is the worst case, and a cost
  cap like the lattice's would follow.

**Pre-registered: C2a, does the final flow explain the difference where the cut gate fires? (before the study ran)**
`tests/cut_motion.py` adds one pass before the warp: on the cut statistic's own 24 x 24 grid, the mean |A(x) - B(x +
f(x))| with the final flow f, over the mean |A(x) - B(x)| (the share of the difference the motion leaves). The switch
`CUT_MOTION=1` would hold a frame only when the statistic is over 0.125 AND that ratio is over a threshold.
`tests/probes/trust/cutstat.py` reads the statistic, the ratio and ffmpeg's scdet score (a cut at 10 or more) for every
pair of the census's 40 real extracts (the NAS), the three local clips (the M5) and the weave pans.
- **C2a:** on real cuts the ratio stays high, with a median near 0.7 and at least 90 percent of them above 0.45. On the
  frame-filling weave pans it is at most 0.3. A threshold between them separates the two.
- **If cuts reach down into the pans' range,** the final flow "explains" a cut by chance matches, and a motion veto is
  unsafe: the fix would then need another cue (the scdet-like score, or the field's coherence).
- A smoke run (8 s of one clip, its one cut) read 0.61 on the cut and at most 0.21 on any other pair.

**Interim (the M5 and the Intel Mac), recorded as they came in:**

    weave box, PSNR-Y (dB)   3       5       11      13      15      16      17      19
    the default              39.80   37.69   20.15   19.46   30.48   37.34   36.74   23.25
    TRUST_GATE (trust1)      42.69   45.58   32.08   31.98   36.74   37.34   38.60   31.89
    change                   +2.89   +7.89  +11.93  +12.52   +6.26    0.00   +1.86   +8.64
    final field, gross       0.0     0.0     0.3     0.0     0.0     0.0     0.0     0.6 percent (the default: 0-34)
    noise                    identical at 7 of 8 speeds; -0.03 dB at 17

- **T3a PASSED:** the final field is at most 0.6 percent gross at every speed.
- **T3b PASSED where gains were registered** (+7.9 to +12.5 dB at 5, 11, 13 and 19), and **MISSED "within 0.5 dB" in
  the good direction** at 3, 15 and 17 (+1.9 to +6.3; 16 unchanged). Noise moves by 0.03 dB at one speed: the gate
  opened on a few of its cells.
- **The frame-filling pan at 3 px/frame** (the Intel Mac's RX 6600, a speed the cut gate does not hold): 27.82 ->
  39.08 dB.
- **L3, time (the M5, 720p, 24 -> 60, ms per output frame, the default -> trust1):** a real clip 12.40 -> 13.92
  (+12 percent), O5 12.77 -> 15.67 (+23), the weave box 12.29 -> 14.65 (+19), the frame-filling weave 27.16 -> 29.22
  (+8: the frame is dominated by the lattice there).
- **Where the gate opens on film** (a tap of its own condition, 3 s of each clip): 5.7, 16.7 and 6.0 percent of the
  cells (an action clip, a 1985 film, a cartoon), and it replaces the flow on 0.7-1.3 percent. The cost is the
  full-resolution decision on every opened cell.

**Pre-registered: a cost cut, `TRUST_DECIDE=two` (trust2), one change.** The decision scores every candidate at its
own position first, and refines only the best and the cell's own flow over +-0.5 px: 5,120 samples a cell against
9,216.
- **K1:** the weave box's picture within 0.1 dB of trust1 at every speed; noise identical to trust1.
- **K2:** the gate's cost on the real clip (trust minus the default) at least 30 percent lower than trust1's.

**K1 MISSED by 5 dB (trust2, the M5):** the weave box at 11 and 13 px/frame reads 26.60 and 27.09 against trust1's
32.08 and 31.98 (3, 5 and 15 within 0.7). The offered minima sit on the quarter level's 4-px grid, so scoring them at
their own positions puts a candidate up to 2 px off the motion it stands for. On a 14-px print with 3-px noise, that
error decides the ranking. trust1's +-0.5 px refine of EVERY candidate was hiding the offer's coarseness. The two-stage
form is rejected as built.

**Pre-registered (one change each): the offer made sub-texel, `TRUST_OFFER=parab`.** Each offered minimum carries its
parabola's position in x and y (from its neighbours' costs, clipped to half a texel), as the offline emulation's did.
- **P1 (trust1p = trust1 + the parabola):** the weave box within 0.1 dB of trust1 or above at every speed; noise
  identical to trust1.
- **K1' (trust3 = the parabola + the two-stage decision):** within 0.1 dB of trust1 at every speed (K1 again), and
  **K2'**: its cost on the real clip at least 30 percent under trust1's.

**K2 MISSED too (trust2's time):** interleaved against trust1, trust2 saves 0.39 ms on the real clip and 1.1 ms on the
weave box. The full-resolution decision is not where most of the gate's cost lives (below).

**Results: L1 MISSED (trust1, the full ladder, the NAS's Arc, against the default in the same sitting):**
- **The capped mean is 38.219 against 38.336 (-0.117).** 11 cases are down more than 0.3 dB, 4 up.
- **Down, on EXACT prints and rotating texture:** V3_stairs_sq24_v12 -10.97, R3_rot_tex -8.89, A6 -3.58, A5 -2.07, O6
  -1.86, A7 -1.28, A4 -1.22, P4 -1.01, O5 -0.77, R1 -0.62, H2 -0.35.
- **Up:** L7_textured_large **+20.44** (25.53 -> 45.97: the exact 15.7-px print at 16 px/frame, the record's open trap,
  "lead 3's territory"), P5 +4.32, P1 +4.19, P3 +0.41.
- **The mechanism, by design reading:** on an exact print the aliases tie at full resolution, and trust1's decision
  only asks the winner to beat the cell's own flow. A candidate whose sub-pixel fit happens to be a little better wins
  by more than 1/255 and replaces a right flow with an alias. **Lead 4 learned this at step 1d** (the uniqueness test:
  beat the runner-up of a different basin too), and trust1 left it out: my omission, caught by the ladder.

**Pre-registered: the uniqueness test, `TRUST_UNIQUE=1` (trust4 = trust1 + that one change).** The winner must also
beat the best candidate more than 2 px from it by 1/255; on a tie the cell keeps its flow. The ladder on the M5
(deterministic with tests/mvk-env.sh), trust4 and trust1 against the default in one sitting:
- **U1:** the cases trust1 lost come back within 0.3 dB of the default, the capped mean within 0.1 of it or above, and
  no case down more than 1 dB.
- **U2:** the weave box keeps trust1's gains within 0.5 dB. The weave is not an exact print: its truth wins by 0.019 a
  pixel at full resolution, almost five times the margin.
- **U3:** L7's +20 shrinks: an exact print's aliases tie, so it should keep less than half of it.

**Results: U1 MISSED on one case, U3 MISSED in the good direction (trust4, the ladder on the M5, one sitting):**
- **The capped mean is +0.131 over the default** (trust1 in the same sitting: -0.147). V3 is back (+0.09), A4-A7, O5
  and O6 within 0.03, R1 -0.26.
- **Still down:** R3_rot_tex **-7.33**, P4 -0.64, H2 -0.33.
- **Up:** L7 **+12.35** (U3 predicted less than half of trust1's +20.7; it kept 60 percent), P1 +0.62, P3 +0.36.

**R3, diagnosed (`tests/probes/trust/r3diag.py`, the M5).** R3 is a disc with an EXACT sin x sin print of period 40
px, its rotation ramping the rim from 0 to 32 px/frame. Against the exact rotation, by radius:

    radius     replaced   the flow it replaced   its replacement   final field gross: trust4 / the default
    0-50       35%        1.7 px                 25.3 px           39.6% /  2.1%
    50-90      44%        2.0                    26.0              65.8% / 13.2%
    90-130     48%        2.4                    25.7              66.3% / 25.7%
    (median errors over the replaced cells)

- **The gate opens on a third to a half of the disc and replaces a right flow with one 25 px wrong.** The print's
  alias (20, 20) lies inside the offer's +-24 px, and on an exact print it ties the truth at full resolution. The
  offered minima sit on the quarter level's 4-px grid and are refined only in half-pixel steps, so the "tie" is broken
  by sub-pixel quantisation (and the block's own rotation), by more than 1/255, and the uniqueness test cannot see a
  tie that quantisation has turned into a margin. The weave survives only because its truth wins by a real margin
  (0.019 a pixel).
- **What a sound guard looks like:** a RELATIVE margin. A difference is significant only against the size of the scores
  themselves; quantisation and rotation add to every candidate's score alike.

**Pre-registered: U5, offline (`tests/probes/trust/decide.py`, before it ran).** The GLSL decision emulated per cell
(whole-texel offers, half-pixel refinement), the ratio winner / runner-up of a different basin, on the weave box at
3-19 px/frame and on R3.
- **U5:** there is a ratio threshold that keeps at least 90 percent of the weave's right winners and refuses at least
  90 percent of R3's wrong ones: the weave's right winners at a median ratio under 0.6, R3's wrong winners over 0.85.
- **If no threshold separates them,** the decision has to compare candidates on an equal footing (a finer common
  refinement) before any margin can mean anything.

**Results: U5 MISSED: no ratio separates them** (the M5's CPU, 2,151 cells a weave speed, 1,442 on R3):

    winner / runner-up of a different basin, percentiles 5 / 25 / 50 / 75 / 95
    weave (every speed but 16)   right winners (98-100% of cells)   0.57 0.67 0.74 0.80 0.91
    R3                           right winners (34% of cells)       0.21 0.48 0.70 0.90 0.98
                                 wrong winners                      0.36 0.61 0.80 0.92 0.99
    a threshold of 0.8 keeps 70-74 percent of the weave's right decisions and refuses only 51 percent of R3's wrong ones

- **The weave's right wins are not large in ratio** (a median 0.74: the truth's own residual, from quantisation, is
  most of the score), **and R3's decision is close to a coin toss** (34 percent right) whose wrong winners spread over
  the same range. A relative margin cannot rescue a decision that has no business being made.
- **The parked design already said where it has no business:** the gate is a PER-LEVEL trust gate. R3's print
  (period 40; 28 px along its diagonal) and V3's stairs (period 24) are ambiguous at 1/8 but NOT aliased there (T1:
  the box flag fires on 0 percent of them at 1/8), so the 1/8 level measures them honestly and its seed should stand.
  trust1 dropped the aliasing flag because T1 found it non-specific on film; the ladder shows ambiguity alone is not
  specific to a misleading level either. **The gate needs both:** aliasing (is this level dishonest here?) and
  ambiguity (is this a print, not film detail?).

**Pre-registered: trust5 = trust4 + the aliasing flag (`TRUST_ALIAS=0.7`), one change.** The gate opens only where the
1/8 level's 5 x 5 window around the cell is also ALIASED: the range of its box-filtered values (the mean over each
texel's 8 x 8 footprint, a new pass per frame) is under 0.7 of the range of its point samples (T1's flag A, at 1/8).
The ladder on the M5 against the default and trust4, one sitting:
- **A1:** R3, V3, P4 and H2 within 0.3 dB of the default (the gate shut: unaliased at 1/8), the capped mean at or above
  the default's, no case down more than 0.3 dB.
- **A2:** L7 keeps trust4's gain within 1 dB (its print is aliased at 1/8: T1, 100 percent), and the weave box keeps
  trust1's gains within 0.5 dB (100 percent aliased).
- **A3:** P1 and P5 lose trust1's gains (their stairs are not aliased at 1/8).

**Results: trust5 on the ladder (the M5, one sitting with the default): A1 and A3 PASSED, A2's L7 half MISSED.**
- **Every case but L7 is within 0.01 dB of the default** (R3, V3, P4, H2 +0.00; M4, P1, P3 +0.01). The capped mean is
  +0.208 over the default.
- **L7 +8.73** (trust4 kept +12.35: A2 asked for its gain within 1 dB). The aliasing flag shuts the gate on part of
  L7's print.
- **P1 and P5 lose trust1's gains** (A3), as their stairs are not aliased at 1/8.
- **trust5 is the first form to pass the ladder.**

**Results: C2a PASSED (the census's 40 extracts on the NAS and the three local clips on the Intel Mac; 58,080 pairs).**

    the share of the difference the final flow leaves (where the cut gate fires), percentiles 0 / 10 / 50 / 90 / 100
    real cuts (scdet 10 or more; 474 of 517 fired on: recall 92 percent)   0.37 0.54 0.64 0.78 0.99
    non-cuts it fires on (64)                                              0.17 0.30 0.56 0.67 0.97
    the frame-filling weave pans at 5 and 19 px/frame (93)                 0.14 0.17 0.20 0.24 0.26

- **The cuts' median is 0.64** (registered: near 0.7) and 90 percent of them are above 0.54 (registered: above 0.45).
- **Every real cut reads 0.37 or more and every pan 0.26 or less.** A threshold of 0.3 holds all 474 cuts the gate fires
  on, releases the pans, and releases 7 of the 64 non-cut firings. `CUT_EXPLAINED` is set to 0.3.

**Pre-registered: the cut gate's switch, `CUT_MOTION=1` (before its gates ran).**
- **CM1 (the frame-filling pan, the Intel Mac, one sitting with the default):** weave 5 and 19 px/frame at least 3 dB
  above the blend (C1's counterfactual gave +3.5 and +8.5); 3, 11, 13 and noise within 0.5 dB of the default.
- **CM2 (the ladder, the M5):** every case within 0.01 dB of the default. No ladder pair should cross the cut gate.
- **CM3 (real footage, the 40 extracts' half-rate test with every frame's PSNR, against the default in the same
  queue):** the output changes on under 1 percent of the frames, never on a frame whose bridged pair holds a real cut,
  and the changed frames' median PSNR does not fall.

**Results: trust5 on the weave box (the M5): noise identical at every speed; A2's weave half MISSED (about half of
trust1's gain kept).**

    weave box, PSNR-Y (dB)   3       5       11      13      15      16      17      19
    the default              39.80   37.69   20.15   19.46   30.48   37.34   36.74   23.25
    trust1                   42.69   45.58   32.08   31.98   36.74   37.34   38.60   31.89
    trust5                   39.80   40.73   25.88   29.81   36.75   37.34   36.89   28.34
    trust5 - the default      0.00   +3.04   +5.73  +10.35   +6.27    0.00   +0.15   +5.09

- The uniqueness test and the aliasing flag, which made the gate safe on the ladder, cost about half of the weave's gain
  (trust4, the uniqueness test alone: 29.79 at 11). trust5 still lifts the fast weave by 5-10 dB and never moves noise.

**Results: CM2 PASSED (the cut gate's switch on the ladder, the M5):** every case within 0.01 dB of the default
(H1 +0.01; M2, P3, R3 -0.01); the capped mean identical.

**Results: CM3 (the cut switch on real footage, the NAS's Arc, every odd frame of the 40 extracts against the default
in the same queue; `tests/probes/trust/framediff.py`):**
- **88 of 21,678 frames change (0.41 percent; registered: under 1)**, and **none bridges a real cut** (scdet's ground
  truth from C2a's census).
- **Most changes are rounding-level** (the median -0.01 dB: the extra pass recompiles the warp). The decision flips are
  the large ones: +8 to +11.5 dB where a non-cut the old gate held is now interpolated, and one frame at -0.77.
- **The changes sum to +117.9 dB; no extract's unflagged median moves by more than 0.01 dB.**
- CM3 PASSED on its count and its cuts. Its third clause (the changed frames' median does not fall) is MISSED by 0.01
  dB, which is rounding, not a decision.

**Results: CM1 PASSED, and the two switches together (the frame-filling weave pan, the Intel Mac's RX 6600, one
sitting):**

    PSNR-Y over the frame (dB)   3       5       11      13      19      noise 3-19
    linear                       28.73   22.28   13.97   13.17   14.69
    the default                  27.82   19.18   21.54   16.74   12.36   54.76 53.47 ... identical in every column
    CUT_MOTION                   27.82   25.57   21.54   16.74   23.21
    trust5                       39.09   19.18   29.27   29.85   12.36
    both                         39.09   31.99   29.27   29.85   26.03
    both - the default          +11.27  +12.81   +7.73  +13.11  +13.67

- **CM1 PASSED:** the cut switch lifts 5 and 19 px/frame to 3.3 and 8.5 dB above the blend and changes nothing else.
- **The two compose.** Once the cut gate lets the frames be drawn, the trust gate adds 6.4 and 2.8 dB more at 5 and 19.
  Together they take every speed of the frame-filling print from at or below the blend to 7-17 dB above it.

**Results: L2 PASSED as registered for trust5 (the NAS's Arc, the 40 extracts against the default in the same queue),
and the frame-by-frame view shows what the medians hide.**
- **The registered gate:** the unflagged medians move -0.04 to +0.10 dB, and no extract falls 0.3.
- **Frame by frame** (framediff.py; not a registered gate, the instrument is new today):
  - 6,876 of 21,678 frames change by more than 0.01 dB: the gate opens on 6-17 percent of a film frame's cells and
    decides on about 1 percent, so most frames move a little;
  - the changes are mostly small (10th to 90th percentile -0.08 to +0.12 dB), up on 3,658 frames and down on 3,218, with
    a net +90.3 dB;
  - **the local extremes are real:** +3.14 at best, and **-3.26 at worst**, with **a run of frames in one extract
    (Sonic the Hedgehog @4341, frames 815-833) at -2.4 to -3.0 dB**;
  - 6 changed frames bridge a real cut, all within 0.02 dB.
- The lattice was adopted on medians alone; nobody has looked at its frames this way.

### Where the per-level trust gate stands (2026-10-01, evening)

**Built, gated, and two findings beside it.** In the order the evidence came:
1. **The parked target was not the trust gate's (T0, C1).** On a frame-filling print at 5 and 19 px/frame the field was
   mostly right and the scene-cut gate held a frame: the gate measures how different two frames are, not whether
   motion explains the difference.
2. **The cut gate fixed: `CUT_MOTION=1` (`tests/cut_motion.py`).** It holds a frame only if the final flow also leaves
   more than 0.3 of the difference unexplained. That threshold was set on 58,080 real pairs: every one of 474 real cuts
   read 0.37 or more, every pan 0.26 or less.
   - **Its gates:** the pans +3.3 and +8.5 dB above the blend (CM1); the ladder within 0.01 (CM2); real footage, 88 of
     21,678 frames changed, none on a cut, with flips of up to +11.5 dB (CM3).
   - **Its cost:** +0.4 ms a frame at 720p on the M5 (+3 percent), in one single-invocation pass that could be spread
     over threads.
3. **The per-level trust gate: `TRUST_GATE=1 TRUST_UNIQUE=1 TRUST_ALIAS=0.7` (`tests/trust_gate.py`, the form
   "trust5").** Where the 1/8 level is both AMBIGUOUS (the lattice's margin gate) and ALIASED (the parked design's own
   flag: the box keeps under 0.7 of the point samples' range), the quarter level offers its three best minima within
   +-24 px and full resolution decides, with lead 4's uniqueness test.
   - **The way there:**
     - ambiguity alone opened the gate on exact prints the 1/8 level sees honestly (the ladder: V3 -11, R3 -8.9);
     - the uniqueness test alone could not stop a tie that quantisation had turned into a margin (R3 -7.3; no ratio
       separates them, U5);
     - the aliasing flag, the parked design's own term, did.
   - **Its gates:**
     - the ladder: +0.21 capped, no case down, L7 +8.7 (the record's period-16 trap);
     - the weave box: +3 to +10 dB at 5-19 px/frame, noise identical;
     - the frame-filling pan: +7.7 to +13.1 dB where the warp runs;
     - real footage: L2 passed, with the frame-level swings above.
   - **Its cost:** +1.0 ms a frame on film at 720p (+8 percent), +2-3 ms where a print fills the region: about half
     fixed (the passes and the gate), half the decision on opened cells.
   - **The price of its safety:** trust1, without the two guards, had about twice the weave gain and failed the ladder.

**The owner's decisions, and what each would need:**
- **`CUT_MOTION` for the player** (every tier: the cut gate is in every shader): the 4K twin (scale_shader.py's frame
  conversion rule covers its one flow read), the Metal port and the lockstep.
- **`TRUST_GATE` (trust5) as a tier, or inside High:** the same three, plus a look at the Sonic frames first.

**Open:**
- the Sonic run (@4341, frames 815-833);
- the half of the weave gain the guards cost;
- the gate's time (its fixed half, and the decision);
- the cut pass spread over threads.

### The decisions (2026-10-01, evening): CUT_MOTION adopted for every tier; the trust gate held

**The owner's word:** *"Adopt cut-fix - it looks to me supported by the data but i am still less convinced by
trust-gate - that one is your decision."*

**CUT_MOTION is adopted in every tier of the player.** There are three new files, each its tier plus `CUT_MOTION=1`,
with their 4K twins; `smoke.sh` checks that all six regenerate byte-identical:
- `bidirectional-interpolation-variational-propagated-global-cage-energy-carry-adopt-lattice-cut.glsl`, High. It is
  md5-identical to the file CM1-CM3 gated.
- `…-carry-adopt-cut.glsl`, Standard.
- `bidirectional-interpolation-variational-propagated-cut.glsl`, Low.

The plain recommendation stays as it was, the reference the science is measured against.
- **The ladder needs no new run for the other tiers.** The cut decision changes only on pairs whose cut statistic is
  over 0.125. That statistic is the same pass in every tier, and CM2 found no ladder pair over it.
- **The tiers' own flows on real cuts** (the three local clips, 110 cuts, the M5):
  - the Low tier holds all 104 cuts its gate fires on (the lowest ratio 0.47, the median 0.67);
  - the Standard tier holds all 104 (the lowest 0.49).
  - The threshold is 0.3, so each tier's cuts stay above it by a wide margin, as the High tier's did in C2a.
- **The 4K twin** (the High tier's, on the frame-filling weave pan at twice the size, the M5):
  - 5 px/frame 19.17 -> 23.19 (+4.0, now 0.9 above the blend);
  - 19 px/frame 12.38 -> 23.09 (+10.7);
  - 11 px/frame and noise identical.
- **The Metal port** (NFrameDemo's engine, the frame-filling pan): 5 px/frame 19.17 -> 25.14, 19 px/frame
  12.36 -> 23.29, 11 identical. libplacebo gives 25.6 and 23.2: the engines agree within 0.7 dB.
- **The cost** on the demo's Metal engine is within its 0.1 ms resolution at 720p (8.2 ms either way) and +0.7 ms
  at 4K. Through libplacebo it is +0.4 ms at 720p, its pass being one invocation.

**The trust gate (`TRUST_GATE`, trust5) is held, not adopted (the assistant's decision, delegated by the owner):**
- **It costs about 8 percent on film for gains on content rare in film.** The gains are fine prints in fast motion.
- **It has one unexplained real-footage harm:** the Sonic run (@4341, frames 815-833, -2.4 to -3.0 dB).
- **The cut fix answers most of the frame-filling case on its own.**
- It stays built behind its switch, gated and recorded. It comes back to the owner if the Sonic run is explained and
  its cost comes down.

## Sources

**Checked 2026-09-30** against publisher pages, DOIs, arXiv and ADS: none fabricated. Corrections applied (the
Hutzler et al. mechanism, Nesterenko's dates, DESI's range, Maldacena's year, titles, and 25 mm as a diameter);
the Hertz numbers were recomputed independently (76.7 us, 26.1 um; Johnson, *Contact Mechanics*, 1985, 11.4).

- The cradle:
  - F. Herrmann and M. Seitz, "How does the ball-chain work?", Am. J. Phys. 50(11), 977-981 (1982),
    doi:10.1119/1.12936.
  - S. Hutzler, G. Delaney, D. Weaire and F. MacLeod, "Rocking Newton's cradle", Am. J. Phys. 72(12), 1508-1516
    (2004).
- Solitary waves in bead chains:
  - V. F. Nesterenko, "Propagation of nonlinear compression pulses in granular media", J. Appl. Mech. Tech. Phys.
    24(5), 733-743 (1983), doi:10.1007/BF00905892; *Dynamics of Heterogeneous Materials*, Springer (2001). The
    term "sonic vacuum" is his, from about 1992-93, not the 1983 paper.
  - C. Coste, E. Falcon and S. Fauve, "Solitary waves in a chain of beads under Hertz contact", Phys. Rev. E 56(5),
    6104 (1997), doi:10.1103/PhysRevE.56.6104.
- Photoelasticity: T. S. Majmudar and R. P. Behringer, "Contact force measurements and stress-induced anisotropy in
  granular materials", Nature 435, 1079-1082 (2005), doi:10.1038/nature03805.
- Small motions in video:
  - H.-Y. Wu et al., "Eulerian Video Magnification for Revealing Subtle Changes in the World", SIGGRAPH 2012.
  - N. Wadhwa et al., "Phase-Based Video Motion Processing", SIGGRAPH 2013.
  - A. Davis et al., "The Visual Microphone: Passive Recovery of Sound from Video", SIGGRAPH 2014 (ACM TOG 33(4),
    79). MIT News quotes motions of about 0.1 um, about 0.005 px; the paper's own figure is not yet checked.
  - A. Davis, K. L. Bouman, J. G. Chen et al., "Visual Vibrometry: Estimating Material Properties From Small Motion
    in Video", CVPR 2015, 5335-5343.
- Yank, the time derivative of force: D. C. Lin, C. P. McGowan, K. P. Blum and L. H. Ting, J. Exp. Biol. 222(18),
  jeb180414 (2019).
- Pool physics: D. G. Alciatore, *The Illustrated Principles of Pool and Billiards*, Sterling (2004), sections 3.03
  and 3.04. The 30 degree rule holds for a cue ball rolling without skid, between a quarter-ball and a three-quarter-ball
  hit (27.3 degrees at the ends, 33.7 at a half-ball hit).
- Cosmology:
  - M. Visser, "Jerk, snap and the cosmological equation of state", Class. Quantum Grav. 21(11), 2603-2616 (2004).
  - V. Sahni et al., the statefinder, JETP Lett. 77, 201 (2003): r (the jerk) = 1 for flat LambdaCDM, stated.
  - D. Clowe et al., "A Direct Empirical Proof of the Existence of Dark Matter", ApJ 648, L109-L113 (2006).
  - G. Agazie et al. (NANOGrav), "The NANOGrav 15-year Data Set: Evidence for a Gravitational-Wave Background",
    ApJL 951, L8 (2023).
  - DESI DR1: A. G. Adame et al., JCAP 02 (2025) 021, arXiv:2404.03002. DR2: M. Abdul-Karim et al., Phys. Rev. D
    112, 083515 (2025), arXiv:2503.14738.
- Quantum mechanics:
  - Y. Aharonov, D. Albert and L. Vaidman, "How the result of a measurement of a component of the spin of a
    spin-1/2 particle can turn out to be 100", PRL 60(14), 1351-1354 (1988): the weak value.
  - Y. Aharonov, P. G. Bergmann and J. L. Lebowitz, "Time Symmetry in the Quantum Process of Measurement", Phys.
    Rev. 134, B1410 (1964): its precursor. The two-state vector formalism proper: Aharonov and Vaidman, PRA 41, 11
    (1990).
  - S. Kocsis et al., "Observing the Average Trajectories of Single Photons in a Two-Slit Interferometer", Science
    332 (2011).
  - A. C. Elitzur and L. Vaidman, "Quantum mechanical interaction-free measurements", Found. Phys. 23, 987-997
    (1993).
- Extra dimensions and holography:
  - N. Arkani-Hamed, S. Dimopoulos and G. Dvali, "The hierarchy problem and new dimensions at a millimeter", Phys.
    Lett. B 429, 263 (1998).
  - L. Randall and R. Sundrum, "A Large Mass Hierarchy from a Small Extra Dimension", PRL 83, 3370, and "An
    Alternative to Compactification", PRL 83, 4690 (1999).
  - J. Maldacena, "The Large N Limit of Superconformal Field Theories and Supergravity", Adv. Theor. Math. Phys. 2,
    231 (1998), arXiv:hep-th/9711200 (1997).
- Data association: Y. Bar-Shalom and T. Fortmann, *Tracking and Data Association* (1988).
- Rigid-body simulation: B. Mirtich, impulse-based dynamic simulation, PhD thesis, UC Berkeley (1996).
