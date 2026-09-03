# Three dimensions: what a 2D motion field says about 3D motion

Status: **DESIGN, written 2026-09-03 before any 3D scene had been rendered.**
Everything in sections 1-3 is derivation, checked numerically on the CPU and
then adversarially reviewed; section 4 is a scene family drafted to the
ladder's rules but not yet through scenecheck; section 5 is a set of
pre-registered predictions; section 9 holds measurements as they arrived on the same day (steps 1-5,
with their predictions scored, several refuted). Read sections 1-8 as the
plan and section 9 as what happened to it.

The question, as the project owner put it: a camera or an eye takes a 2D
plate of a 3D scene; the motion it encodes is purely two-dimensional, but the
thing moving is moving in three. What, then, does the field measure?

## 0. The answer in one paragraph

The field measures the image-plane derivatives of each material point's
projected trajectory: velocity, acceleration and jerk of the *picture* of the
point, in pixels per frame interval. It does not measure 3D acceleration.
Under perspective, an object moving at perfectly constant 3D velocity with
any component along the optical axis has a non-zero, growing image
acceleration and a non-zero image jerk, manufactured by the 1/Z projection
and nothing else. What the field does carry, exactly and without knowing
depth, speed, focal length or object size, is a family of scale-free
quantities: time to contact and its rate of change, the dimensionless
braking number of an approach, relative depth within a rigid patch, and
angular rates in absolute units. What it can never carry, without an
external ruler, is absolute scale: a scene twice as large moving twice as
fast projects to identical pixels at every derivative order.

## 1. The projection algebra

Pinhole camera at the origin, focal length f in pixels, image x = f X/Z,
y = f Y/Z. Rather than grind quotient rules, note x Z = f X and apply Leibniz
to the n-th derivative:

    x^(n) = f X^(n)/Z  -  sum_{k<n} C(n,k) x^(k) Z^(n-k) / Z

Written out (and the same in y):

    x'   = f X'/Z   - (Z'/Z) x
    x''  = f X''/Z  - 2(Z'/Z) x'  - (Z''/Z) x
    x''' = f X'''/Z - 3(Z'/Z) x'' - 3(Z''/Z) x' - (Z'''/Z) x

Every term kept. Each line splits into exactly three kinds of term:

- **genuine lateral** derivative, f X^(n)/Z: scaled by 1/Z and nothing else;
  the only term that survives at the principal point;
- **genuine axial** derivative, -(Z^(n)/Z) x: attenuated by x/f = tan(theta),
  exactly zero on the optical axis, and independent of focal length;
- **purely kinematic** cross terms, -2(Z'/Z)x' at second order and
  -3(Z'/Z)x'' - 3(Z''/Z)x' at third: they contain no n-th derivative of the
  world trajectory at all and are manufactured by the projection.

**Constant 3D velocity.** Set every second and third world derivative to
zero. The genuine terms vanish and the kinematic ones remain:

    x'' = -2 (Z'/Z) x'          x''' = 6 (Z'/Z)^2 x'

In the shader's own units (px per frame interval, rho = -Z'/(Z fps) = 1/TTC_f
with TTC_f the instantaneous time to contact in frames), for a texel at image
radius r from the focus of expansion:

    v = r / TTC_f       a = 2 v / TTC_f = 2 r / TTC_f^2       j = 6 v / TTC_f^2 = 6 r / TTC_f^3

Focal length, depth and object size cancel entirely. Verified (derivation):
against Richardson-extrapolated differences of an exact trajectory with an
off-axis focus of expansion, v to 4e-13, a to 7e-11, j to 1e-8, as vectors;
the cancellation holds to eight decimals across f = 500-6000 px and
Z = 5-200 m. In the shader's own discrete differences the relation
2v/a = TTC_f is *exact* for constant closing speed, with no convention
correction, and the centred second difference over-reads the continuous
acceleration by 1/(1 - rho^2), i.e. +0.1% at TTC_f = 32.

**General approach.** With tau = -Z/Z' (seconds) and the dimensionless
3D acceleration q = Z Z''/Z'^2 (zero for constant speed, positive for
braking, negative for an accelerating approach):

    v = r/tau       a = r (2 - q)/tau^2       j = 6 r (1 - q)/tau^3

from which three scale-free invariants follow, each checked to 1e-13:

    G = r a / v^2          = 2 - q            (needs the focus of expansion)
    K = div(a) / div(v)^2  = 1 - q/2          (needs no FOE; linear in q)
    H = j v / a^2          = 6(1-q)/(2-q)^2   (needs no FOE; quadratic in q,
                                               so a consistency check, not
                                               an estimator)

G is Lee's tau-dot in disguise: G = 1 - d(tau)/dt exactly, so "acceleration
of the optical flow used to reason about approach" has been a named
psychophysical variable for fifty years (section 3). Constant 3D velocity is
q = 0, hence G = 2, K = 1, H = 3/2 at every instant, radius, depth and lens.

**Axial versus lateral 3D acceleration.** A genuine acceleration A along
the optical axis reads -(A/Z) x, i.e. r/f = tan(theta) times what the same A
applied laterally reads (f A/Z). It nulls on the axis and it is lens-free;
the lateral term scales with f. Numbers at 24 fps, Z = 20 m, A = g = 9.81:
lateral 1.51 px/interval^2 on a 50 mm-equivalent lens (f = 1778 px at 1280
wide), 0.48 on a 16 mm-equivalent -- so a wide lens puts free fall *below*
the field's 0.5 px/interval^2 reliability threshold; axial 0 on the axis,
0.26 at r = 300 px, 0.63 at the frame corner, on any lens. But the
*divergence* of the axial field is -2 Z''/(Z fps^2), uniform across the
frame and free of both f and r, so a patch fit recovers Z''/Z with no
attenuation at all. There is no information blindness at the centre; there
is a per-texel one.

**The looming signature against the instrument's floor.** For constant
closing speed the image acceleration at radius r is 2 r/TTC_f^2 and the
jerk 6 r/TTC_f^3. With the record's floors (acceleration unreliable below
~0.5 px/interval^2, jerk floor 0.05-0.1 px/interval^3):

    TTC_f  TTC @24fps   |a| >= 0.5 outside r =   |j| >= 0.1 outside r =
     24      1.0 s          144 px                   230 px
     32      1.33 s         256 px                   546 px
     48      2.0 s          576 px                 1843 px (never)
     72      3.0 s         1296 px (never)          --

A "blind disc" around the focus of expansion of radius a_min TTC_f^2/|2-q|
shrinks as the square of time to contact. So the acceleration field sees an
approach only in its last second or two, and only away from the point being
approached; the jerk field sees it only in the last second and only at the
rim. A constant-speed approach at a survivable time to contact never puts
its jerk above the floor across a whole clip. That is physics, not a design
slip, and it is why the D-series calibrates jerk on exactly one scene.

## 2. What is recoverable, and what is provably not

### 2.1 Scale

The monocular depth-speed ambiguity is a *symmetry* of the projection, not a
shortage of equations: P(t) -> lambda P(t) leaves x(t) = f X/Z unchanged for
all t, hence every temporal derivative of the image unchanged. No derivative
of the image can break it (the scale direction lies in the kernel of the
measurement Jacobian to 1e-17 at orders 1, 2, 3). As a counting matter it
gets *worse* per texel with order: 1 + 3k unknowns against 2k equations,
deficit 1 + k. For a rigid patch of n texels the count gives n = 5 for
velocity alone (the classical calibrated five-point count) and n = 4 once
acceleration is included, so acceleration pays when shared. Rotation is
scale-free: angular velocity and angular acceleration come out in absolute
rad/s and rad/s^2 while every translational quantity carries lambda.

The scale is broken the moment any external magnitude is supplied, and the
acceleration order is where the cheapest ruler attaches. For a free-flying
object with P'' = g known, the second derivative adds two equations and no
unknowns: with A = f g_X - x g_Z and B = f g_Y - y g_Z,

    a_x + 2 u w = A/Z       a_y + 2 v w = B/Z       (w = Z'/Z)

is linear in (w, 1/Z) and returns absolute depth *per texel*, no patch and
no rigidity, degenerate only when the image velocity is parallel to the
projected gravity. Gravity is a ruler, and it consumes the acceleration
field rather than needing new inputs. (Corrected on review: the first draft
said acceleration pays "only when shared across a rigid patch"; it pays in
two ways.)

Rulers, ranked by fit to a local, per-texel, real-time instrument: a known
ground plane and camera height (Z = h f/(y - y_horizon), closed form, one
calibration); known ego-motion (every flow vector becomes a depth); known
object size (needs recognition); gravity (above); stereo (best physically,
doubles the hardware); structure from motion over a long window (worst fit,
contradicts the four-frame design, still leaves lambda free).

### 2.2 Time to contact, first order

For a rigid fronto-parallel patch every image position scales as
c(t) = f/Z(t), so u = sigma x with sigma = -Z'/Z, and

    div(u) = 2 sigma        tau_1 = 2 / div(u) = -Z/Z'

Lee's tau, with neither Z nor Z' known. **This is a pooled patch quantity,
not a per-texel one.** The reviewers' simulation on the D1 geometry: a robust
affine fit of the velocity field over the object mask returns 48.02 / 42.00
/ 36.00 / 30.00 / 25.00 frames at frames 0 / 6 / 12 / 18 / 23, exact to 0.05%
at sigma_f = 0.10 px even with an 8-texel correlation length; the same
divergence taken by per-texel finite differences returns ~14.5 frames at
every frame with an interquartile range of 20-53. The per-texel form
2|v|^2/(a.v) is usable only where the object's own acceleration clears the
field's floor, i.e. outside the blind disc above, and has roughly a
thousandth of the pooled estimator's SNR.

Three qualifications carry weight. It is tau_1, not tau: 2v/a = 2 tau/(2-q),
so a moderate brake (q = 1/3) over-reads by 20% and q = 2 diverges. Roll
about the optical axis leaves div(u) untouched but inflates 2|v|/|a| by
+26% at Omega tau ~ 1. A slanted surface with lateral motion biases tau_1 by
(s/2)(V_lat/V_close): measured +6%, +22%, +97% across a tilt grid, and the
first-order system cannot remove it in general.

### 2.3 Time to contact, second order -- the centrepiece

Let Z'' be constant over the window and kappa = Z'' Z/Z'^2 (= q). Dividing
Z + Z' T + Z'' T^2/2 = 0 by Z:

    tau_2 = tau_1 (1 - sqrt(1 - 2 kappa)) / kappa

tau_2 -> tau_1 as kappa -> 0. The discriminant is a collision test:
kappa >= 1/2 means the approach brakes to a stop short of contact, with
closest approach Z_min/Z = 1 - 1/(2 kappa) at t = tau_1/kappa -- a genuinely
scale-free miss distance, "you will stop at 17% of your current distance"
without knowing the distance.

Which measured quantities give kappa is the trap. The field's acceleration
is the *material* derivative of the flow, so its spatial gradient is not the
time derivative of the flow's gradient. The exact identity is

    grad(a) = D(grad u)/Dt + (grad u)^2

verified analytically on a looming-plus-rolling plane. With the four
first-order invariants D = u_x + v_y, w = v_x - u_y (curl), d1 = u_x - v_y,
d2 = v_x + u_y (deformation) and Da = div(a):

    tau_1 = 2/D
    kappa = 2 (1 - Da/D^2) + (d1^2 + d2^2 - w^2)/D^2
    collision iff kappa < 1/2, tau_2 as above

Getting the identity wrong -- taking Da/2 as the rate of sigma -- gives
kappa_naive = kappa_true - 1, always negative, so every scene reads as an
accelerating approach and tau reads 0.73 s where truth is 1.00 s. The curl
term is not cosmetic: a looming patch rolling at Omega inflates the
uncorrected kappa by exactly (Omega tau_1)^2, and at tau_1 = 1 s, Omega =
1.5 rad/s a colliding object (true kappa 0.333) is reported as a MISS
(2.58). There is also an exact discrete estimator, from the two measured
Jacobians A+ = I + Ja/2 + Ju and A- = I + Ja/2 - Ju with det(A) = (c'/c)^2
for a similarity, that returns TTC in source intervals with no
continuous-time approximation (0.0000% in every case tested, including
rolling ones).

How wrong first order is: braking from 15 m at 15 m/s with 5 m/s^2
(kappa = 1/3), true contact 1.268 s, tau_1 reads 0.998 s (-21%), tau_2
reads 1.267-1.269 s; harder brake (kappa = 1/2), true 2.0 s, tau_1 still
0.999 s (-50%); an *accelerating* approach at -5 m/s^2, true 0.873 s, tau_1
0.998 s, +14% *late* -- the dangerous direction; a gentle distant brake at
30 m, 8 m/s, 0.5 m/s^2, true 4.34 s, tau_1 3.75 s (-14%).

What it costs. Monte Carlo at sigma_f = 0.10 px (now measured at 0.07 on the
matcher's best content, NFRAME-LIMITS.md section 8), affine fit over a disc
of radius R with correlation length 8 texels: R = 240 px gives kappa
0.333 +/- 0.027 and tau_2 = 1.267 +/- 0.039 s; R = 120 px, +/- 0.073 and
+/- 0.117 s; at R = 60 px the discriminant is unreliable and 30% of trials
call MISS on a colliding object. First-order tau_1 is far more robust
(+/- 0.001-0.008 s). The second-order term is a real but expensive upgrade:
it needs a patch of order a hundred pixels' radius.

### 2.4 Null spaces, stated at the right level

The depth law Z = K/(t + c), i.e. q = 2 held for all t, gives image motion
that is exactly linear -- a real 3D deceleration (Z(0) = 20 m, Z'(0) = -15
m/s, Z''(0) = +22.5 m/s^2 in the reviewers' example) whose single-texel
image acceleration and jerk are identically zero, surviving discretisation
exactly. But that is a *pointwise* degeneracy of one texel's temporal
derivatives, one ray of the per-texel null space the rank count already
established ("any 3D motion whose projection is a straight line traversed
at constant speed"). At the field level it is not hidden at all: K = 1 - q/2
recovers q = 2 outright from div(a) and div(v). More generally, a constant
3D acceleration -- gravity, steady braking, the physically generic case --
nulls the image acceleration at *one instant* (q(t) passes through 2) and
carries j = -6 r/tau^3 at exactly that instant, so the jerk field breaks the
degeneracy the acceleration field momentarily has.

### 2.5 Divergence, curl, deformation, and their rates

For a planar patch with inverse depth 1/Z = 1/Z0 + p x + q y and velocity V:

    D  = -2 V_z/Z0 + f (p V_x + q V_y)      looming, plus slant x lateral motion
    w  = -2 Omega_z + f (p V_y - q V_x)     roll rate, in absolute rad/s
    d1 = f (p V_x - q V_y),  d2 = f (p V_y + q V_x)

so divergence is time to contact only for a fronto-parallel patch or purely
axial motion. The *time derivatives* of these are what this instrument
uniquely supplies in real time: dD/dt gives Z''/Z and hence second-order
TTC; curl(a) = D(w)/Dt + w D gives the axial angular acceleration in
absolute rad/s^2, scale-free; the deformation rate is the signature of a
turning surface.

### 2.6 Honest limits

Global scale is never recoverable without a ruler. A growing object and an
approaching object are indistinguishable monocularly; every TTC statement
assumes rigidity. Divergence conflates looming with slant times lateral
motion. Per-texel 3D does not exist: only pooled patch quantities are
meaningful, so any 3D layer is a segmentation-and-robust-fit stage on top of
the field, and a plain least-squares trace over a heavy-tailed field is the
"mean over a 23-sigma tail" trap the record already documents. Divergence at
an occlusion boundary is meaningless. The bas-relief ambiguity trades depth
against rotation at small fields of view. The field is one interval late, so
tau must have one interval subtracted (4% at tau = 1 s, 17% at 0.25 s). And
a looming object presents a continuum of image speeds from zero at the focus
of expansion to r/tau at the rim -- see section 7 for what that does and
does not imply for the matcher.

## 3. Prior art, stated narrowly

Old, and older than computer vision: Lee (1976) showed that the ratio of an
image feature's size to its rate of expansion is time to contact, needing
neither depth, speed nor calibration, and his braking result is already
second-order -- tau-dot is the control variable, and tau-dot = -0.5 is the
constant-deceleration soft-landing law. G above *is* 1 - tau-dot. Standard
in three separate fields: looming neurophysiology (locust LGMD/DCMD; Sun &
Frost 1998 found pigeon nucleus-rotundus cells computing tau, absolute
expansion rate and eta as three distinct variables); structure and motion
(Longuet-Higgins & Prazdny 1980, Koenderink & van Doorn, reading depth from
divergence, curl and deformation; Avidan & Shashua's trajectory
triangulation reconstructs a conic -- constant 3D acceleration -- from a
monocular sequence); and scene flow (Vedula et al.), normally stereo or
learned, a velocity field whose temporal derivative is not a standard
product. Automotive TTC from monocular scale change is deployed and
patented, and dense TTC from flow divergence, including GPU implementations,
exists.

Particle image velocimetry, which PRIOR-ART.md already names as the closest
discipline, supplies the sharpest borrowing: four-pulse PIV measures
*material* acceleration and is rigorous about Du/Dt = du/dt + (u . grad) u.
Here that is not cosmetic. On a looming field the local and convective
terms are exactly equal, so an implementation that differences two stored
flow fields at a fixed texel reads **exactly half** the true image
acceleration on constant-velocity looming, and exactly the right value on a
lateral translation. This shader's a = f(0 -> 1) + f(0 -> -1) follows the
material point and should read the full value. The 2D ladder cannot detect
this trap; the D-series can (prediction P3D-4).

What the searches did not find, stated no larger than PRIOR-ART.md's
existing claim: a dense per-texel second- and third-order temporal fit --
acceleration and jerk, not tau on a segmented object -- computed
deterministically, in real time on commodity hardware, inside a stock video
pipeline, and offered as a calibrated instrument with coverage and
conditional accuracy against analytic truth. Existing dense TTC work is
first-order; existing second-order work is per-object, offline, or
model-fitted. The mathematics above is not new; a scene ladder that
isolates it is.

## 4. The D-series (drafted, not yet validated)

Camera: pinhole, f = 1200 px at 1280x720 (56 degree horizontal field), principal
point (640, 360). Every object is a fronto-parallel rectangular plate, so its
image is an axis-aligned rectangle of size f S/Z -- exactly what the ladder's
exact-coverage formula renders exactly -- and its texture is written in
*metres on the plate*, so it scales with perspective as a painted surface
would. The helper `_plate <Z> <Xc> <Yc> <SW> <SH> <BG> <OBJ> <rate>` binds
the scale and image rectangle once per pixel, as `_blob` binds its rotation.
The full file is `scenes-3d.sh` (kept outside `tests/` until it has been
through scenecheck).

    case               Z(t) m               q            tau s        corner v px/f   corner a px/i^2   j px/i^3   discriminates
    D0_loom_flat       7.2 - 2.4t           0            3.00->2.00   5.0->11.3       +0.14->+0.47      (below)    flat control for D1 (PSNR only; no interior field)
    D1_loom_const      7.2 - 2.4t           0            3.00->2.00   5.0->11.3       +0.14->+0.47      +0.006->+0.029   THE LOOMING DISCRIMINATOR: zero 3D accel, non-zero image accel
    D2_wall_approach   10.1 - 3.5t (wall)   0            2.89->1.89   10.6->16.2      +0.31->+0.72      +0.013->+0.048   whole-frame divergent flow, no boundary anywhere
    D3_loom_accel      6.9 - 1.2t - 1.2t^2  -11.5->-0.83 5.75->1.25   2.7->19.2       +0.27->+1.82      +0.011->+0.235   real axial acceleration; the ONLY jerk-calibrating case
    D4_loom_decel      7.5 - 3.6t + 1.2t^2  +1.39->+8.5  2.08->4.25   6.9->5.0        +0.09->-0.32      --         braking; image accel NULLS at t = 0.345 s; true miss (stops at 4.8 m)
    D5_oblique         7.5 - 1.8t, Xc drifts 0           --           8.9->15.3       +0.18->+0.40      --         focus of expansion off-frame at (-160, 360)
    D6_lateral         6 (fixed), Xc drifts 0            inf          12.5 exactly    0                 0          the validated 2D case as a control; separates non-integer speed from aliasing
    D7_depth_on_bg     as D1, textured static background                                                           occlusion boundary with a real depth step
    D8_dolly_twoplane  wall 9.0-2.4t, panel 5.4-2.4t                                                              relative depth from the field, with a square-law self-check
    D9_recede_alias    12 + 6t, receding    0            --           --              --                --         texture crosses the 32 px coarse Nyquist at t = 0.5 s: the instrument-defect boundary, deliberately
    D10_soft_landing   0.45 (4-t)^2         0.5 exactly  --           6.3->14.8       +0.20->+0.62      --         Lee's tau-dot = -0.5 law; G = 1.5 constant, a second exactly-constant invariant

D1, D3 and D4 are matched at t = 0.5 s in Z and Z': they render a
bit-identical frame with identical image velocity and differ only in the
second derivative, with corner accelerations +0.240 / +0.541 / -0.060
px/interval^2 (ratio exactly 2.25, sign reversed). That is the cleanest
discriminator in the family, and the whole signal separating D1 from D3 is
0.129 px of differential displacement at the rim over one interval.

**Ladder assumptions, checked at design time.** *Reach:* image speed varies
across a looming object, which is new; every scene keeps the far corner
under 20 px/frame (worst D3, 19.2 at t = 1 -- read D3 at t <= 0.9 and treat
the tail as a reach test, as rotcheck does past R2 frame 17). *Aliasing:*
plate texture image periods run 59-120 px, at most 0.27 cycles per coarse
texel against a Nyquist of 0.5, sub-Nyquist at every level for the whole
shot; the textures are axis-aligned sine products and never rotate. D9 is
the deliberate exception. *Interior texture:* every calibration case is
textured; D0 is the flat control. *Ground truth:* motion is a pure function
of T and edges are exact coverage, so a 60 fps render is the exact answer.
*New caveat, patch dilation:* SAD matching models a translation, but a patch
on an approaching plate also dilates by dt/tau per interval -- across the
5x5 patch that is 5 dt/tau of its own texels at every level, 0.08-0.21 here,
about half of what R2's rim already survives. Keep tau >= ~0.5 s.

**Corrections from review that bind the protocol.** (i) At exact N:N the
three-frame window is {k-1, k, k+1} and the four-frame host queue on ffmpeg
is {k-2 .. k+1}, so frame 0 has no window and frame 23 of a 24-frame render
needs frame 24: render 25 source frames (d = 25/24 s) and test frames 2-22;
a reading at frame 23 from a 24-frame render is the last frame repeated
into slot 2 and reads a large *inward* acceleration -- a manufactured
refutation, wrong in sign and magnitude. (ii) The ffmpeg host's jerk is the
third difference anchored half an interval *before* slot 1 (JERK_CENTRE =
-0.5; +0.5 on Metal), and on a 1/(2-T) hyperbola that offset is 5-7% of the
value: jerk truth must be evaluated at the anchor, not at the frame instant,
exactly as accelcheck.py already does. (iii) Only D3 clears the jerk floor;
report no jerk numbers from D1, D5 or D10. (iv) The shipped warp's jerk
deadband (3.0 / 6.0 px/interval^3) is sixteen times D1's peak jerk, so the
four-frame shader's jerk correction is identically zero on every D-series
scene, and the two-frame shader's placement truncation on D1 is only 0.047 px
RMS -- at or below sigma_f -- because 24 -> 60 samples interval phases 0 /
0.4 / 0.8 and never the t = 0.5 peak. So on D1 **all four PSNR arms will fall
inside the harness's 0.05 dB**; the interpolation benchmark cannot see the
temporal model on looming and the D-series is a *field* experiment.
(v) A bonus already in the ladder: R1_rot_const (`_blob '640' '360'
'2.56*T' 150`) carries a true, purely centripetal image acceleration of
1.7067 px/interval^2 at r = 150 (1.7050 as the exact discrete difference),
constant in time, that rotcheck.py cannot parse because its regex demands
theta = C T^2. Widening the regex on a scratch copy is worth doing, with the
prediction that R1 reads *better* than R2/R3, since its truth is radial and
radial is the observable component on a rim.

## 5. Pre-registered predictions

Numbers to hold the measurements to. Each names what would refute it.

- **P3D-1 (the field reads the projection).** On D1 at N:N, the pooled
  acceleration field over the plate interior is radial-outward from
  (640, 360) to within 15 degrees at the median, linear in r, and its slope
  matches 2/TTC_f^2 to within 20% at frames 2-22 -- 20% and not "a few
  percent" because D1's accelerations (0.14-0.47 px/interval^2) sit in the
  band where A4 (a = 0.333) calibrates to ~17%. Refuted if the field is
  uniform across the plate, or points inward, or its slope is off by more
  than a factor of 1.5.
- **P3D-2 (time to contact, first order).** tau_1 = 2/div(v) from a robust
  affine fit of D1's velocity field recovers TTC_f = 10 Z(t) frames to
  within 2% at every frame 2-22. Refuted above 5%.
- **P3D-3 (image acceleration is not 3D acceleration).** At t = 0.5 s, D1,
  D3 and D4 -- one identical frame, one identical velocity field -- give
  pooled K = div(a)/div(v)^2 of 1.00, 2.25 and -0.25 respectively (q = 0,
  -2.5, +2.5), i.e. G = 2, 4.5, -0.5. Refuted if D3 and D4 are not
  separated by at least a factor of 3 in |K| with opposite sign.
- **P3D-4 (the Eulerian trap).** The shader reads the full Lagrangian value:
  D1's pooled slope is 2/TTC_f^2, not 1/TTC_f^2. A reading near half is
  the trap and would be a defect in the estimator, not the scene.
- **P3D-5 (the control).** D6 reads a = 0 within the acceleration floor and
  j = 0 within the jerk floor across the plate, at a velocity of exactly
  12.5 px/frame -- a non-integer coarse-texel speed on sub-Nyquist texture,
  which per NFRAME-LIMITS.md section 8 must track cleanly.
- **P3D-6 (the collision test).** On D4 the pooled kappa from the
  acceleration field, with the curl and deformation terms included, reads
  above 1/2 at every measurable frame (MISS -- correct, it stops at 4.8 m);
  on D1 it reads 0 +/- 0.15 (so tau_2 = tau_1). Refuted if D4 reads below
  1/2 or D1 reads above 0.3.
- **P3D-7 (jerk, on the one scene that can carry it).** On D3 at t = 0.8-0.9
  the pooled jerk is radial and its slope matches 6(1-q)/TTC_f^3 within 30%,
  with H = j v/a^2 at the median within 30% of 6(1-q)/(2-q)^2 (1.04 at
  t = 0.5, 1.37 at t = 1). Refuted if the jerk field is indistinguishable
  from the A6 null floor.
- **P3D-8 (the defect boundary in a 3D scene).** On D9 the velocity field is
  clean while the texture's image period is above 32 px and degrades once
  it falls below, at t = 0.5 s -- the point-sampled-pyramid failure entered
  by texture scaling rather than by speed. Refuted if the field is equally
  good, or equally bad, on both sides.
- **P3D-9 (the benchmark is blind here).** On D1 the two-, three- and
  four-frame shaders and the LSQ variant score within 0.1 dB of one another.
  Refuted by any arm winning by 0.3 dB.

## 6. Experiment order

Cheapest and most discriminating first; each step is a single render or two.

1. `scenecheck` the D-series (the rule: a misaligned benchmark does not
   fail, it lies). Nothing else until this passes.
2. D1 and D6, velocity and acceleration fields, stock four-frame shader at
   N:N, 25 source frames, pooled readback: P3D-1, -2, -4, -5.
3. D1 / D3 / D4 acceleration at t = 0.5: P3D-3.
4. D4 and D1 kappa with the full first-order invariants: P3D-6.
5. D3 jerk at t = 0.8-0.9 with the anchor-corrected truth: P3D-7.
6. D9: P3D-8.
7. The PSNR ladder over the D-series, all arms: P3D-9.
8. Widen rotcheck's regex on a scratch copy and calibrate R1.
9. Only then real footage: a dash-cam approach or a thrown object, tau_1
   pooled first, second order only on patches of >= 100 px radius.

## 7. What is blocked, and what is not

NFRAME-LIMITS.md section 8 leaves the block matcher with an open defect: its
coarse pyramid is point-sampled and the obvious fix made things worse. A
looming object presents every coarse-texel speed at once, so the first draft
of this document assumed 3D measurement was blocked until that is fixed.
Review corrected the scope: the pyramid failure is gated by *texture spatial
frequency*, not by speed. Speed only decides whether an already-aliased level
can still be shift-matched. The ladder's own A4-A7 boxes carry sub-Nyquist
texture and sweep continuously through every non-integer speed from -20 to
+20 px/frame on the current build, and they are its working acceleration
calibration (1.4-2.7%). The D-series is designed sub-Nyquist throughout, so
it runs on the current build. What *is* blocked is 3D measurement on real
footage with fine texture -- the trust gate comes before that, not before
this.

## 8. Refuted on review, kept on the record

Fifteen of thirty-six adversarial reviews completed before the usage limit
cut the run; the synthesis stage did not run and this document was written
by hand from the three derivations and the reviews that finished. Every
review that finished returned "refuted", and in every case the algebra
survived and a prediction, a test or an absolute did not:

- D1's endpoint frames 0 and 23 have no temporal window; the headline number
  sat on frame 23.
- The jerk truth table was anchored at the frame instant; the host anchors
  half an interval earlier (5-7% on the hyperbola).
- "No temporal derivative can ever break the scale ambiguity" and
  "acceleration pays only when shared across a patch": both false the moment
  a known magnitude (gravity) is supplied -- absolute depth per texel.
- "A large real 3D deceleration reads as zero": true of one texel's temporal
  derivatives on one depth law, false at the field level (K recovers q = 2).
- Per-texel TTC = 2|v|/|a| silently swapped for the pooled 2/div(v), which
  has about a thousand times the SNR; only the pooled form is an estimator.
- The axial acceleration "weak everywhere": below the 0.5 threshold over the
  inner ~86% of a 50 mm frame, never below the lateral term on a wide lens,
  and its divergence is not attenuated at all.
- "Looming is the rotation failure in a new costume": it is the speed-comb
  failure in a new costume, and only for super-Nyquist texture (section 7).
- R1's predicted 100-220% error band was inverted: R1 should read better.
- bi's placement truncation on D1 is 0.047 px RMS, not 0.03-0.13; all four
  PSNR arms fall inside 0.05 dB (now P3D-9).
- "Max 19.2 px/frame" was the right-edge midpoint; the far corner is 19.6.

## 9. Measurements

### 9.1 Step 1, scenecheck -- 2026-09-03

D0_loom_flat, D1_loom_const, D2_wall_approach, D6_lateral: one exact to
rounding (a max delta of 1 on one anti-aliased edge texel), the rest
bit-identical between the 24 and 60 fps renders. The plate helper is
ground truth. D3/D4 checked at the start of step 3.

### 9.2 D1_loom_const -- 2026-09-03, RX 6600, stock four-frame shader, N:N

25 source frames, frames 2-22 read; pooled over the plate interior (inset
40 px; robust affine fit for the divergences, median radial projection for
the slopes). Velocity is the forward straddle flow, so its instant is half
an interval after the frame's; the acceleration is centred on the frame.

    P3D-2  TTC_f = 2/div(v) against tau_f = 10 Z(t) frames: frames 6-22 read
           -2.4% to +0.9% (18 of 21 inside 2%); frames 2-5 read -3.0 to -4.6%.
           The half-interval anchoring accounts for -0.7 to -1.0% of the
           systematic sign, after which frames 6-22 sit within about 1%.
           NOT REFUTED (nothing above 5%); the "within 2% at every frame"
           wording fails on the first four frames.
    P3D-1  Pooled slope against 2/TTC_f^2: median +12% over-read; 14 of 21
           frames inside 20%, worst +44% (frames 3-4) and -32% (frame 21);
           nothing near the factor-1.5 refutation line. Direction at the
           TEXEL level: the median vector sits 55-72 degrees off radial.
           That is not a surprise, it is section 1's blind-disc table: D1's
           true |a| never exceeds 0.36 px/interval^2 even at the rim, below
           the 0.5 floor everywhere, and 36-41% of live texels read
           |a_r| > 0.5 where the truth is <= 0.36. The per-texel half of
           P3D-1 is REFUTED at this signal level; the pooled half HOLDS.
    K      div(a)/div(v)^2, truth 1.00: median 1.00 over frames 2-22,
           interquartile about 0.88-1.11, excursions 0.52 and 1.50. The
           FOE-free invariant that says "constant closing speed" reads its
           value from a field whose individual texels are mostly noise.
    P3D-4  The pooled slope is 2/TTC_f^2 (+12%), not 1/TTC_f^2 (-50%): the
           shader reads the Lagrangian value. CONFIRMED.
    G      Per-texel r a_r/v_r^2, truth 2: medians 1.8-3.8, interquartile
           roughly -8 to +10. Not an estimator at this signal level;
           recorded so nobody tries it.

Scored: P3D-2 partial (early frames), P3D-1 pooled holds and per-texel
refuted, P3D-4 confirmed. D1 is the gentlest scene in the family (tau
2-3 s), so this is the field at its weakest, rescued entirely by pooling --
exactly the shape the reviewers predicted when they replaced per-texel
time to contact with the pooled form. The early-frame TTC deficit (-3 to
-4.6% on the smallest plate) is unexplained; the 40 px inset leaves the S
level's 5x5 patch (+/-32 px) touching the edge, and a 64 px inset is used
from step 3 onward.

### 9.3 Step 3: the control, real acceleration, and braking -- 2026-09-03

D3 and D4 scenecheck bit-identical. Inset raised to 64 px; velocity truth
taken at t + 1/48 s (the forward straddle's instant). D1 re-read at the new
inset: TTC -0.1 / -1.1 / -2.7 / +1.2 / +0.2% at frames 2 / 6 / 12 / 18 / 22
-- the early-frame deficit of 9.2 was edge contamination at 40 px, and is
gone.

**D6_lateral, the control (P3D-5).** Velocity 12.44-12.50 against exactly
12.5 (<= 0.5%), v_y -0.015; pooled div(v) = 1.5e-4 and div(a) = -1e-4
against 0 (D1's div(v) is 3e-2 for scale). Pooled: CONFIRMED. Per texel:
median |a| = 0.40-0.61 px/interval^2 on a scene whose true acceleration is
zero, with 39-55% of texels above 0.5 -- AT the floor, not within it. The
per-texel half is REFUTED, and the cause is the texture (below).

**D3_loom_accel, real 3D acceleration (P3D-2 under q != 0).** TTC = 2/div(v)
within +/- 2.5% at all 21 frames, typically under 1%, while tau_f runs
112 -> 33 frames and q from -8.3 to -1.0. The first-order estimator tracks
the *instantaneous* time to contact under strong 3D acceleration, as the
algebra says it must: q enters 2v/a, not div(v). Pooled slope median +2%,
range -9 to +17%. K tracks the truth's decay from 5.2 to 1.5 (measured 6.70
-> 1.20) within about +/- 25%.

**D4_loom_decel, braking (P3D-3, P3D-6).** TTC within +/- 4.3% while tau
*grows* from 51 to 92 frames. K crosses zero and goes negative -- **the
image acceleration reverses sign while the object is still approaching** --
measured from frame 13 (t = 0.54 s) against a true crossing at frame 8-9
(t = 0.345 s). At the crossing the true rim acceleration is below 0.04
px/interval^2, so a three-frame localisation is what the floor allows. From
frame 13 on, K reads -0.53 / -0.69 / -0.10 / -0.66 / -1.03 / -1.23 / -0.80 /
-1.30 / -1.76 / -2.36 against -0.34 / -0.44 / -0.56 / -0.69 / -0.85 / -1.03 /
-1.24 / -1.50 / -1.81 / -2.19: within +/- 0.4. The collision test kappa =
2(1 - K) > 1/2 -- MISS, correctly, D4 stops at 4.8 m -- holds on 19 of 21
frames; frames 5-6 read K = 1.27 / 0.94 where the true acceleration slope is
1e-4 per pixel of radius, i.e. nothing to measure.

**P3D-3 at the pre-registered instant, frame 12 (t = 0.5 s).** K = 1.22 /
2.78 / +0.16 for D1 / D3 / D4 against 1.00 / 2.25 / -0.25. The D3/D1 ratio
is 2.28 (truth 2.25). D4's sign is not reversed at frame 12; it is by frame
13. PARTIAL: the separation and the D3 ratio hold at the named instant, the
D4 sign does not, and the null is measured three frames late. **P3D-6:**
19 of 21 MISS on D4; on D1 kappa = 2(1 - K) scatters +/- 0.6, not the
+/- 0.15 predicted. PARTIAL.

**The finding: the D-series texture is the limiter, not the instrument.**
sigma_f on D6's plate, the stock four-frame shader's velocity field against
the exact (12.5, 0): robust std 0.28-0.36 px, median error 0.40, p99 2.7-3.0,
36-42% of texels beyond 0.5 px, and *identical* at 40 and 120 px inset --
against 0.070 px on M1 (NFRAME-LIMITS.md section 8). TEX_D is TEX_M2's form,
a product of two sines, at twice the period (80 px at Z = 6 m against 40),
and it costs four to five times the flow noise: half the gradient, a nearly
linear 5x5 patch with no curvature to locate a sub-pixel minimum, and at
1/16 resolution only 0.2 cycles per coarse texel of contrast. Acceleration
noise of sqrt(2) x 0.3 = 0.45 is exactly the per-texel floor seen on every
D scene including the zero-truth control. The sub-Nyquist criterion in
section 4 was necessary and not sufficient; the texture also needs gradient
everywhere. Every pooled number above survives this; every per-texel number
is bounded by it.

**Step 4, pre-registered.** Replace TEX_D on D0-D8 and D10 with a
two-component texture, periods 0.24 and 0.36 m with offset phases (48 and
72 px at Z = 6, sub-Nyquist at the coarsest level for Z <= 9 m, no shared
zero-gradient lines); D9 keeps TEX_D because its purpose is the Nyquist
crossing. Predictions: sigma_f on D6 below 0.15 px; D6's per-texel median
|a| below 0.3; D1's K interquartile inside +/- 0.15; D3 and D4's K errors
halved; D4's sign crossing within two frames of frame 9. Refuted if
sigma_f stays above 0.25 -- in which case the floor is the plate geometry
(dilation) or the matcher, not the texture.

### 9.4 Step 4: the richer texture -- 2026-09-03

TEX_D2 (two sine products, 0.24 and 0.36 m, offset phases; 48 and 72 px at
Z = 6 m) on D1 / D3 / D4 / D6, same protocol. Scored against the section 9.3
pre-registration:

    sigma_f on D6 < 0.15 px          REFUTED: 0.246-0.264 (from 0.28-0.36)
    D6 per-texel median |a| < 0.3    REFUTED: 0.42-0.56 (from 0.40-0.61)
    D1 K interquartile inside 0.15   HOLDS:   0.84-1.09, median ~0.97
    D3 K errors halved               HOLDS:   ~7% median (from ~25%);
                                              at t = 0.5, K = 2.45 (truth 2.25)
    D4 K errors halved               REFUTED late: |K| over-read ~45% from
                                              frame 16 (from ~20% under)
    D4 sign crossing within 2 frames HOLDS:   negative from frame 10 against
                                              a true crossing at 8-9; and now
                                              reversed AT the pre-registered
                                              frame 12: K = 1.09 / 2.45 / -0.71
                                              for D1 / D3 / D4 (truth 1.00 /
                                              2.25 / -0.25), D3/D1 = 2.25.
                                              P3D-3 now holds in full.
    D4 collision test                21 of 21 MISS.

So the texture was not the dominant cause of the per-texel floor: a 15%
improvement in sigma_f, not the two- to four-fold predicted, and the
per-texel acceleration floor unchanged. It did sharpen every pooled
invariant. Two things it changed that were not predicted: the pooled time
to contact now over-reads systematically -- D1 +1.4 to +7.8% (was -0.1 to
-2.7), D3 +13% at the start decaying to 0% at the end (was within 2.5%),
D4 +2 to +6.5% (was within 4.3%) -- so the pooled divergence carries a
texture-dependent bias of a few percent that P3D-2's "within 2%" did not
allow for; and D4's late K over-reads where it under-read before. A
sub-pixel estimator biased toward the texture's own phase ("pixel
locking", well known in particle image velocimetry) would produce a
texture-dependent ripple in the radial velocity profile and hence a net
bias in the fitted divergence; that is a candidate, not a finding.

With texture largely excluded and no dilation on D6 (it translates at fixed
depth), the one remaining difference from M1's 0.070 px is speed: D6 moves
at 12.5 px/frame, 0.78 of a coarse texel, where M1 moves at exactly one.
The review's correction in section 7 -- that non-integer coarse speed on
sub-Nyquist texture is fine -- was made on the A-series' *median* accuracy,
and a median can be exact while the spread is not. Step 5 tests it
directly: the same plate and texture at exactly 16 px/frame and at 8.
Pre-registered: if sigma_f at 16 px/frame falls to ~0.1 or below and stays
~0.25 at 8 and 12.5, the per-texel spread is speed-gated by the point-sampled
pyramid even on sub-Nyquist texture, section 7's blocker assessment is too
narrow, and per-texel 3D readings wait for the trust gate after all; if all
three read ~0.25, the floor belongs to the plate family or the matcher on
this content class and is not about the pyramid.

### 9.5 Step 5: speed, on the same plate and texture -- 2026-09-03

D6's plate and TEX_D2 at 8, 12.5 and 16 px/frame (0.5, 0.78 and exactly
1.0 coarse texels per frame); all three bit-identical under scenecheck.
sigma_f, robust std of the velocity field against exact truth:

    speed px/frame   sigma_f    p99     beyond 0.5 px
      8              0.261      ~2.6    ~35%
     12.5            0.246      ~2.7    ~35%
     16              0.190      0.97    21%

Neither pre-registered branch cleanly. The integer coarse speed helps --
the gross tail halves and its 99th percentile drops threefold -- but the
core spread falls only from 0.25 to 0.19, nowhere near M1's 0.070 at the
same 16 px/frame. So the per-texel floor on these plates has two parts.
One is the point-sampled pyramid, gated by speed exactly as NFRAME-LIMITS.md
section 8 says, and it owns the tail. The other is full-resolution
gradient: the sub-Nyquist criterion that keeps the coarse levels honest
*forces* gentle gradients at full resolution (TEX_D2's finest period is 48
px against TEX_M1's 4.6), and sub-pixel precision scales with gradient.
Fine texture buys precision and aliases coarsely; smooth texture matches
cleanly and locates poorly; M1 at one coarse texel per frame has both,
because integer speed makes its aliasing harmless. The two findings of the
day are one finding.

**Where this leaves the 3D programme.** Every pooled quantity -- time to
contact first order, the invariant K, the sign reversal under braking, the
collision test -- reads correctly on the current build through a per-texel
field that is mostly noise, and that is the design the reviewers insisted
on. Per-texel 3D readings (a texel's own acceleration vector, G, the blind
disc) are floor-limited at sigma_f ~0.2-0.25 on sub-Nyquist plates whatever
the pyramid does, and on fine-textured real footage by the pyramid as well.
Section 7 stands for pooled work and is too optimistic for per-texel work.
The next 3D steps are D2 (whole-frame divergence, no boundary), D9 (the
Nyquist crossing entered by scaling), D3's jerk with the anchor-corrected
truth (P3D-7), and the PSNR arms (P3D-9); the next instrument step is the
trust gate, which now has a second customer.

## 10. Method notes

Derivations and reviews ran CPU-only while the GPU worked the instrument
backlog (NFRAME-LIMITS.md section 8). Every reviewer re-derived the algebra
it was handed -- by Leibniz, by exact rational arithmetic, by complex-step
Jacobians, by Richardson-extrapolated differences -- and the algebra held in
every case; what failed was always the step from algebra to a testable
number on this instrument. That is the same shape as 2026-09-02's ladder
work, where predictions were right where they were derived and wrong where
they assumed something about the instrument. The scripts are in the session
scratch `d3/` folder and are not part of the repository; the scene file is
the one durable artefact and is kept beside this document until scenecheck
passes.
