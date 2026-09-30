# Transfer of kinetic energy: inferring what the field cannot see

Opened 2026-09-30 from the owner's question. A Newton's cradle moves its two end balls while the middle ones stay
still, yet the energy has passed through them. Can we infer kinetic energy that we cannot detect? What does that
mean further afield, from astrophysics to quantum mechanics? And how do we detect it?

**Status: parked until there is compute to spare.** Nothing here is built yet. Five investigations follow, each with
its own next steps, the prior art to survey before designing anything (the literature-first rule), what it costs, what
it would buy the project, and its traps. The suggested order is at the end.

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

**Cost.** One GPU reading pass over short clips; the rest is Python. A phone, a tripod and ten minutes of throwing.
On the Mac, best of three for anything that goes through the propagated family (the Mac's reading wanders).

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
