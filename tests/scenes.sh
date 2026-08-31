# Synthetic test scenes for the ground-truth interpolation benchmark.
# Sourced by bench.sh and visuals.sh.
#
#   scene <case-name> <frame-rate>
#
# Every scene's motion is a pure function of t. That is the whole trick: the
# same expression rendered at 24fps and at 60fps describes the *identical
# physical scene* sampled at two different rates, so the 60fps render is the
# exact correct answer for a 24->60 interpolation of the 24fps render. That
# turns "does this look smudgy" into a measurable error.
#
# Nothing here needs a source video file -- lavfi generates everything.
#
# --- calibration constants these scenes are built around -----------------
# The interpolator's coarse (1/16 res) search reaches step_px * 1.9375
# coarse texels, i.e. 0.75 * 1.9375 * 16 = ~23 full-res px per source frame
# pair. At 24fps that is ~552 px/sec. Velocities below are chosen to sit
# deliberately under, at, and beyond that ceiling.
#
# --- texture periods -----------------------------------------------------
# sin(X/k) has spatial period 2*pi*k px:
#   k=2.5   -> 15.7px  (~= the 16px/frame motion: AMBIGUOUS)
#   k=2.546 -> 16.0px  (exactly the motion: worst case)
#   k=6.366 -> 40.0px  (clearly != the motion: unambiguous)
# A pattern that repeats at roughly the distance the object travels per
# frame is genuinely indistinguishable from no motion at all, using only
# two frames and a local search. See TESTING.md.

# ---------------------------------------------------------------------
# FOURIER-BOUNDARY OBJECT.
#
# Every other object in this file is a rectangle, so every edge is straight
# and axis-aligned. This one is bounded by a Fourier series in polar form:
#
#     r(phi) = R * (1 + SUM a_n cos(n*phi + psi_n))
#
# with a_n = 0.36/n -- a 1/f amplitude spectrum, which is the spectrum of a
# fractal (fractional Brownian) boundary: comparable detail at every scale it
# can represent, rather than one characteristic wiggle size. Harmonics are
# 3, 5, 8, 13, 21, 34 -- deliberately non-harmonic, so no two reinforce into a
# regular polygon, and spread over a decade so the boundary carries coarse
# lobes and fine ripple at once. At R=150 the n=3 term is a 18px excursion
# over a ~314px arc and the n=34 term a 1.6px excursion over a ~28px arc.
#
# This is the geometry the "known limitation" section of TESTING.md used to
# say synthetic scenes could not have. That claim was wrong: a Fourier series
# represents any shape, so irregularity is a matter of writing down enough
# terms, not something only real content can possess.
#
# What it genuinely cannot do, stated precisely: this is the RADIAL form, so
# the curve is single-valued in phi and therefore star-shaped. It cannot
# produce a concavity that doubles back -- a duck's beak, say. That needs the
# PARAMETRIC form, z(s) = SUM c_n exp(i*n*s), which draws any closed curve at
# all but is a curve rather than an inside/outside test, and geq evaluates one
# pixel at a time with no loops to run a crossing test in. So the parametric
# form needs a rasterisation step and an image input; the radial form needs
# nothing and still delivers multi-frequency edges at every orientation, which
# is the property being tested here.
#
# The boundary is BAND-LIMITED, ~2px of soft transition, for the same reason
# scene_rot's cells are: a hard threshold on a curve produces an aliased
# staircase whose exact jagged pattern no resampling can reproduce, which
# would penalise the case by construction rather than measure anything.
#
#   _blob <cx-expr> <cy-expr> <theta-expr> <radius> <rate>
#
# Rotation is inside the expression rather than an overlay, because an overlay
# cannot rotate. Translation could be an overlay, but is kept in the
# expression too so the background has no seam.
# ---------------------------------------------------------------------
_blob() {
  local CX=$1 CY=$2 TH=$3 R=$4 r=$5
  # st()/ld() bind the rotation and the object-frame coordinates once per
  # pixel. Without them the boundary expression re-derives u and v about
  # fourteen times each: measured at 47s against 11s for one 60fps second.
  #   0=cos(theta) 1=sin(theta) 2=u 3=v 4=phi
  local PRE="st(0\,cos($TH))\;st(1\,sin($TH))\;st(2\,(X-($CX))*ld(0)+(Y-($CY))*ld(1))\;st(3\,(0-(X-($CX)))*ld(1)+(Y-($CY))*ld(0))\;st(4\,atan2(ld(3)\,ld(2)))"
  local E="$R*(1+0.1200*cos(3*ld(4)+0.7)+0.0720*cos(5*ld(4)+2.1)+0.0450*cos(8*ld(4)+4.3)+0.0277*cos(13*ld(4)+1.2)+0.0171*cos(21*ld(4)+5.6)+0.0106*cos(34*ld(4)+3.4))"
  echo "nullsrc=s=1280x720:r=$r:d=1,format=gray,geq=lum='$PRE\;30+190*clip(($E-hypot(ld(2)\,ld(3)))/2\,0\,1)',format=yuv420p"
}

scene() {
  local CASE=$1 r=$2 W=1280 H=720 DUR=1
  local BG="color=c=black:s=${W}x${H}:r=$r:d=$DUR"
  case "$CASE" in

    # ---- L0: no motion. Must be a perfect passthrough. -------------------
    L0_static)
      echo "$BG[bg];color=c=white:s=100x100:r=$r:d=$DUR[bx];[bg][bx]overlay=x=400:y=310:shortest=1,format=yuv420p" ;;

    # ---- L1-L4: pure horizontal translation, sharp high-contrast edges.
    # The velocity ladder: well under the search ceiling, one coarse texel,
    # at the ceiling, and deliberately past it. ---------------------------
    L1_trans_8px)   # 8px/frame
      echo "$BG[bg];color=c=white:s=100x100:r=$r:d=$DUR[bx];[bg][bx]overlay=x='192*t':y=310:shortest=1,format=yuv420p" ;;
    L2_trans_16px)  # 16px/frame = exactly one coarse-level texel
      echo "$BG[bg];color=c=white:s=100x100:r=$r:d=$DUR[bx];[bg][bx]overlay=x='384*t':y=310:shortest=1,format=yuv420p" ;;
    L3_trans_23px)  # 23px/frame = at the computed coarse-search ceiling
      echo "$BG[bg];color=c=white:s=100x100:r=$r:d=$DUR[bx];[bg][bx]overlay=x='552*t':y=310:shortest=1,format=yuv420p" ;;
    L4_trans_40px)  # 40px/frame = deliberately beyond it
      echo "$BG[bg];color=c=white:s=100x100:r=$r:d=$DUR[bx];[bg][bx]overlay=x='960*t':y=310:shortest=1,format=yuv420p" ;;

    # ---- L5: L2's motion, but the object is barely brighter than the
    # background (12/255 = 0.047, above the shader's MIN_CONTRAST of 0.02).
    L5_lowcontrast)
      echo "color=c=0x303030:s=${W}x${H}:r=$r:d=$DUR[bg];color=c=0x3c3c3c:s=100x100:r=$r:d=$DUR[bx];[bg][bx]overlay=x='384*t':y=310:shortest=1,format=yuv420p" ;;

    # ---- L6-L7 / M1-M3: the texture series. IDENTICAL 300x300 object,
    # IDENTICAL 16px/frame motion -- only the interior texture differs.
    # This is the controlled experiment that isolates what the motion
    # search can and cannot resolve. --------------------------------------
    L6_flat_large)      # no interior texture at all
      echo "$BG[bg];color=c=0x808080:s=300x300:r=$r:d=$DUR[bx];[bg][bx]overlay=x='384*t':y=210:shortest=1,format=yuv420p" ;;
    L7_textured_large)  # periodic, period 15.7px ~= the motion
      echo "$BG[bg];nullsrc=s=300x300:r=$r:d=$DUR,format=gray,geq=lum='128+110*sin(X/2.5)*sin(Y/2.5)',format=yuv420p[bx];[bg][bx]overlay=x='384*t':y=210:shortest=1,format=yuv420p" ;;
    M1_noise_large)     # aperiodic blocky noise: rich texture, no repeat
      echo "$BG[bg];nullsrc=s=300x300:r=$r:d=$DUR,format=gray,geq=lum='mod(floor(abs(sin(floor(X/4)*12.9898+floor(Y/4)*78.233))*43758.5453),256)',format=yuv420p[bx];[bg][bx]overlay=x='384*t':y=210:shortest=1,format=yuv420p" ;;
    M2_period40)        # periodic, period 40px: unambiguous
      echo "$BG[bg];nullsrc=s=300x300:r=$r:d=$DUR,format=gray,geq=lum='128+110*sin(X/6.366)*sin(Y/6.366)',format=yuv420p[bx];[bg][bx]overlay=x='384*t':y=210:shortest=1,format=yuv420p" ;;
    M3_period16_trap)   # periodic, period EXACTLY the motion: worst case
      echo "$BG[bg];nullsrc=s=300x300:r=$r:d=$DUR,format=gray,geq=lum='128+110*sin(X/2.546)*sin(Y/2.546)',format=yuv420p[bx];[bg][bx]overlay=x='384*t':y=210:shortest=1,format=yuv420p" ;;

    # ---- M4: contrast BELOW the shader's MIN_CONTRAST gate (3/255 =
    # 0.0118), unlike L5 which sits above it. Tests the gate itself.
    M4_belowgate)
      echo "color=c=0x303030:s=${W}x${H}:r=$r:d=$DUR[bg];color=c=0x333333:s=300x300:r=$r:d=$DUR[bx];[bg][bx]overlay=x='384*t':y=210:shortest=1,format=yuv420p" ;;

    # ---- L8: diagonal motion, to catch axis asymmetry in the search. -----
    L8_diagonal)
      echo "$BG[bg];color=c=white:s=100x100:r=$r:d=$DUR[bx];[bg][bx]overlay=x='384*t':y='216*t':shortest=1,format=yuv420p" ;;

    # ---- L9: two objects crossing in opposite directions -> genuine
    # occlusion, which the forward/backward consistency check must handle.
    L9_occlusion)
      echo "$BG[bg];color=c=white:s=100x100:r=$r:d=$DUR[b1];color=c=0xa0a0a0:s=100x100:r=$r:d=$DUR[b2];[bg][b1]overlay=x='300+300*t':y=310:shortest=1[s1];[s1][b2]overlay=x='900-300*t':y=310:shortest=1,format=yuv420p" ;;

    # ---- A1-A3: ACCELERATION. Every case above moves at a constant
    # velocity, so the block match's core assumption -- that one offset
    # describes the whole interval between two source frames -- is exactly
    # true, and the linear lift of the flow to an intermediate time
    # (flow_ab * mix_t in the warp) is exactly right. Neither holds under
    # acceleration, and nothing here tested that until now.
    #
    # Each pairs with a constant-velocity twin above: x = c*t^2 covers the
    # same total distance in the same second as x = c*t, so mean velocity,
    # object, and start and end positions are IDENTICAL to L1/L2/L3, and the
    # velocity ramps 0 -> 2c instead of holding at c.
    #
    # That twinning is USEFUL BUT NOT CLEAN, and the difference matters when
    # reading a result. Two confounds, both measured rather than suspected:
    #
    #   1. Equal mean velocity is not equal difficulty. Error grows faster
    #      than linearly with speed, and the ramp spends half its time below
    #      the mean and half above, so the average of the per-frame scores is
    #      not the score at the average speed. This can push the accelerating
    #      case either way and did: A2 scored ABOVE its twin.
    #   2. These are overlay scenes, so their ground truth is snapped to even
    #      pixels, and two different velocity profiles accumulate that
    #      snapping error differently. See F2 below for the version without
    #      this confound, and TESTING.md for the measurement.
    #
    # So read A1-A3 as "does acceleration break anything dramatic, on the same
    # object the velocity ladder uses", and read F2 minus F1 as the actual
    # cost of acceleration.
    #
    # Calibration, so a result maps onto a mechanism. Over one 24fps source
    # interval the true mid-frame position and the linear interpolation of
    # the endpoints differ by a*dt^2/8 = a/4608 px. That is 0.08px at A1,
    # 0.17px at A2, 0.24px at A3 -- deliberately sub-pixel, because any
    # acceleration large enough to make it a whole pixel also throws the
    # object past the coarse search's reach within the second and would
    # confound the two failures. On a hard edge a tenth of a pixel is not
    # nothing: it is ~10% of full contrast on the boundary texel.
    #
    # Motion stays a pure function of t, so ground truth is exact as always.
    A1_accel_8mean)   # ramps 0->16px/frame, mean 8   -- twin of L1
      echo "$BG[bg];color=c=white:s=100x100:r=$r:d=$DUR[bx];[bg][bx]overlay=x='192*t*t':y=310:shortest=1,format=yuv420p" ;;
    A2_accel_16mean)  # ramps 0->32px/frame, mean 16  -- twin of L2
      echo "$BG[bg];color=c=white:s=100x100:r=$r:d=$DUR[bx];[bg][bx]overlay=x='384*t*t':y=310:shortest=1,format=yuv420p" ;;
    A3_accel_23mean)  # ramps 0->46px/frame, mean 23  -- twin of L3
      echo "$BG[bg];color=c=white:s=100x100:r=$r:d=$DUR[bx];[bg][bx]overlay=x='552*t*t':y=310:shortest=1,format=yuv420p" ;;

    # ---- F1: irregular boundary, otherwise L6. Same flat interior, same
    # 16px/frame translation, same ~300px object -- only the boundary
    # differs, straight and axis-aligned in L6 against a 1/f Fourier curve
    # here. So F1 minus L6 isolates the cost of edge irregularity alone,
    # the same way the L6/L7/M1/M2/M3 series isolates interior texture.
    # Centred at 200, not L6's 150: the boundary reaches R*1.2924 = 194px at
    # its furthest, so a centre of 150 would clip the object against the left
    # frame edge and manufacture a straight edge in a case that exists to
    # not have one.
    F1_fourier_edge)
      _blob '200+384*T' '360' '0' 150 "$r" ;;

    # F2: F1's twin under acceleration -- same object, same mean velocity,
    # same start and end position, velocity ramping 0 -> 32px/frame. This is
    # the CLEAN acceleration measurement, and the reason it exists is that
    # A1-A3 above are not: they are overlay scenes, so their ground truth is
    # snapped to even pixels, and an accelerating object and a constant one
    # accumulate that snapping error differently. F2 minus F1 has no such
    # confound, since both are analytic and exact.
    F2_fourier_accel)
      _blob '200+384*T*T' '360' '0' 150 "$r" ;;

    # ---- R1-R2: ROTATION AS THE MOTION. Not to be confused with scene_rot
    # below, which rotates a pattern and its translation together by a fixed
    # angle to probe grid alignment -- the motion there is still a pure
    # translation. These are the only cases in this file where the scene
    # actually turns.
    #
    # Block matching searches over TRANSLATIONS, so rotation is a motion the
    # estimator cannot represent exactly anywhere except instantaneously and
    # locally: the true flow diverges across the object, and only a
    # sufficiently local match can follow it.
    #
    # The object has to be the Fourier blob rather than a disc, because a
    # rotating disc is indistinguishable from a stationary one -- there is
    # no feature whose motion could be recovered.
    #
    # Calibrated on rim speed, so it sits on the same scale as the velocity
    # ladder: at R=150 an angular rate of 2.56 rad/s is 384 px/s at the rim,
    # i.e. L2's 16px/frame. R2 covers the same total rotation as R1 in the
    # same second, ramping 0 -> 32px/frame at the rim -- the rotational twin
    # of the A-series, and the only case here with both a non-translational
    # motion and a changing one.
    R1_rot_const)
      _blob '640' '360' '2.56*T' 150 "$r" ;;
    R2_rot_accel)
      _blob '640' '360' '2.56*T*T' 150 "$r" ;;

    *) echo "UNKNOWN_CASE"; return 1 ;;
  esac
}

ALL_CASES="L0_static L1_trans_8px L2_trans_16px L3_trans_23px L4_trans_40px \
L5_lowcontrast L6_flat_large L7_textured_large M1_noise_large M2_period40 \
M3_period16_trap M4_belowgate L8_diagonal L9_occlusion \
A1_accel_8mean A2_accel_16mean A3_accel_23mean \
F1_fourier_edge F2_fourier_accel R1_rot_const R2_rot_accel"

# The six added 2026-08-31 are in ALL_CASES deliberately rather than in a
# group of their own: a case that is not run by default is a case that rots.
# They cost more than the rest -- the blob's boundary is evaluated per pixel
# by geq, at roughly 11s per 60fps second against well under a second for a
# rectangle overlay. Their rows are additive, so every historical number for
# the fourteen cases above remains directly comparable.
ACCEL_CASES="A1_accel_8mean A2_accel_16mean A3_accel_23mean"
SHAPE_CASES="F1_fourier_edge F2_fourier_accel R1_rot_const R2_rot_accel"
#
# GAP THESE FILL: every scene in the original ladder puts the moving object
# on a FLAT BLACK background. That hides exactly the failure real content
# shows, because flow smeared across an object's boundary lands in a region
# where any error self-conceals. Real material -- especially cartoons -- has
# structure on BOTH sides of every moving edge, so smearing flow across a
# boundary damages the background too, and the edge loses definition.
#
# All backgrounds here are static (zero flow) while the object moves, so
# there is a hard, exactly-known motion discontinuity at the object edge.

scene_edge() {
  local CASE=$1 r=$2 W=1280 H=720 DUR=1
  # aperiodic 4px-cell noise, static in the source's own frame
  local NOISE="geq=lum='mod(floor(abs(sin(floor(X/4)*12.9898+floor(Y/4)*78.233))*43758.5453),256)'"
  local NOISE2="geq=lum='mod(floor(abs(sin(floor(X/5)*39.3468+floor(Y/5)*11.135))*24634.6345),256)'"
  case "$CASE" in

    # E1: textured object on a TEXTURED STATIC background. The background
    # cannot conceal smeared flow, unlike the flat-black ladder.
    E1_edge_on_texture)
      echo "nullsrc=s=${W}x${H}:r=$r:d=$DUR,format=gray,$NOISE,format=yuv420p[bg];nullsrc=s=300x300:r=$r:d=$DUR,format=gray,$NOISE2,format=yuv420p[bx];[bg][bx]overlay=x='384*t':y=210:shortest=1,format=yuv420p" ;;

    # E2: cartoon-like. Flat mid-grey object with a hard dark outline, over a
    # static background of flat bands with hard boundaries -- large flat
    # areas separated by high-contrast edges, which is what animation is.
    E2_cartoon_edge)
      echo "nullsrc=s=${W}x${H}:r=$r:d=$DUR,format=gray,geq=lum='if(lt(mod(Y\,140)\,70)\,170\,95)',format=yuv420p[bg];color=c=0x9a9a9a:s=260x260:r=$r:d=$DUR,drawbox=x=0:y=0:w=260:h=260:color=0x1a1a1a:t=5,format=yuv420p[bx];[bg][bx]overlay=x='384*t':y=230:shortest=1,format=yuv420p" ;;

    # E3: two objects, adjacent and touching, moving in OPPOSITE directions.
    # A motion discontinuity with no background gap to hide it -- the worst
    # case for a diffusion kernel that averages across the boundary.
    E3_opposing)
      echo "nullsrc=s=${W}x${H}:r=$r:d=$DUR,format=gray,$NOISE,format=yuv420p[bg];nullsrc=s=200x400:r=$r:d=$DUR,format=gray,$NOISE2,format=yuv420p[l];nullsrc=s=200x400:r=$r:d=$DUR,format=gray,geq=lum='mod(floor(abs(sin(floor(X/3)*21.77+floor(Y/3)*47.31))*31517.19),256)',format=yuv420p[rr];[bg][l]overlay=x='440+192*t':y=160:shortest=1[s1];[s1][rr]overlay=x='640-192*t':y=160:shortest=1,format=yuv420p" ;;

    # E4: thin high-contrast lines on a flat field, moving. Cartoon outlines
    # are thin; a 1/16-res kernel averages a 3px line into near-nothing, so
    # luma-guided edge preservation has almost no signal to work with there.
    E4_thin_lines)
      echo "nullsrc=s=${W}x${H}:r=$r:d=$DUR,format=gray,geq=lum='150',format=yuv420p[bg];nullsrc=s=300x300:r=$r:d=$DUR,format=gray,geq=lum='if(lt(mod(X\,40)\,3)+lt(mod(Y\,40)\,3)\,30\,150)',format=yuv420p[bx];[bg][bx]overlay=x='384*t':y=210:shortest=1,format=yuv420p" ;;

    *) echo UNKNOWN_CASE; return 1 ;;
  esac
}
EDGE_CASES="E1_edge_on_texture E2_cartoon_edge E3_opposing E4_thin_lines"

# ---------------------------------------------------------------------
# GRID-ALIGNMENT scenes.
#
# THE GAP THESE FILL: every other scene in this file uses axis-aligned
# rectangles, so every edge is exactly horizontal or vertical -- lined up
# with both the pixel grid and the flow field's block grid. That is the one
# case a square flow grid can represent exactly, and it is not what real
# content looks like. Real edges sit at arbitrary angles.
#
# Pattern AND motion rotate together, so the geometry is IDENTICAL at every
# angle -- same checkerboard, same speed, same edge-to-motion relationship --
# and the only thing that changes is how it sits on the square grid. Rotating
# the pattern alone would confound this with the aperture problem, since at 0
# degrees the horizontal edges would run parallel to the motion.
#
# The cells are band-limited (a soft-clipped product of sines, ~3px edges)
# rather than hard-thresholded. A hard threshold produces an ALIASED
# staircase at an angle, whose exact jagged pattern no resampling can
# reproduce, which would penalise angled cases by construction.
#
#   scene_rot <angle-radians> <rate>
# ---------------------------------------------------------------------
scene_rot() {
  local A=$1 r=$2
  local U="(X*cos($A)+Y*sin($A)-384*T)"
  local V="((0-X)*sin($A)+Y*cos($A))"
  echo "nullsrc=s=1280x720:r=$r:d=1,format=gray,geq=lum='130+75*clip(8*sin(2*PI*$U/80)*sin(2*PI*$V/80)\,-1\,1)',format=yuv420p"
}
ROT_ANGLES="0 0.174533 0.392699 0.785398"   # 0, 10, 22.5, 45 degrees
