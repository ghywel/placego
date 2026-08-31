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

# The blob again, with a TEXTURED interior riding the body frame. _blob's
# PRE already computes object-frame coordinates u = ld(2), v = ld(3), so a
# texture written in them rotates and translates WITH the body -- which is
# the whole point: R2 measured the field on a rotating FLAT blob at >130%
# vector error, and that confounds two suspects (rotation itself vs the
# aperture problem on its texture-free boundary). This interior is TEX_M2
# in body coordinates; if the field reads well here, the aperture was the
# killer and rotation per se is fine -- the same control-scene move that
# separated jerk from magnitude.
_blobt() {
  local CX=$1 CY=$2 TH=$3 R=$4 r=$5
  local PRE="st(0\,cos($TH))\;st(1\,sin($TH))\;st(2\,(X-($CX))*ld(0)+(Y-($CY))*ld(1))\;st(3\,(0-(X-($CX)))*ld(1)+(Y-($CY))*ld(0))\;st(4\,atan2(ld(3)\,ld(2)))"
  local E="$R*(1+0.1200*cos(3*ld(4)+0.7)+0.0720*cos(5*ld(4)+2.1)+0.0450*cos(8*ld(4)+4.3)+0.0277*cos(13*ld(4)+1.2)+0.0171*cos(21*ld(4)+5.6)+0.0106*cos(34*ld(4)+3.4))"
  local TEXB="128+110*sin(ld(2)/6.366)*sin(ld(3)/6.366)"
  echo "nullsrc=s=1280x720:r=$r:d=1,format=gray,geq=lum='$PRE\;30+(($TEXB)-30)*clip(($E-hypot(ld(2)\,ld(3)))/2\,0\,1)',format=yuv420p"
}

# ---------------------------------------------------------------------
# EXACT-COVERAGE RECTANGLES.
#
# Pixel X spans [X, X+1). A rectangle spanning [x0, x0+w) covers
#
#     clip(min(x0+w, X+1) - max(x0, X), 0, 1)
#
# of it, and the same in Y. That product is EXACT box-filter area sampling,
# not a cosmetic soft edge, and the distinction is the whole point:
#
#   - At an INTEGER position it is 0 or 1 everywhere, so it reproduces a
#     hard-edged rectangle exactly -- no softening, no anti-aliased fringe
#     where there should not be one.
#   - At a FRACTIONAL position it is what an ideal renderer would produce.
#     The 60fps ground truth therefore stops being snapped to a whole even
#     pixel, which is what it was doing until 2026-08-31.
#
# The 24fps SOURCE frames are almost unchanged by this, and where they do
# change the new one is right. Verified frame by frame against the old
# scenes: of 24 source frames, most are byte-identical, and the ones that
# differ are the frames where the old scene put the object in the WRONG
# PLACE. L1 frame 14 is the worked example -- the true left edge is
# 8*14 = 112, the old scene rendered it at 110, this one renders it at 112.
# The cause is in TESTING.md: 14*(1/24) lands a ULP below 7/12, 192*t comes
# out at 111.99999999999998579, and overlay truncated and then snapped that
# to an even pixel. So the old ladder had occasional wrong INPUTS as well as
# a systematically wrong target, which is the full reason the numbers were
# reset rather than merely improved.
#
# Two cases change more than that, both expected: L9, whose positions are
# genuinely fractional at odd source frames and were being snapped, and M1,
# whose texture had to be replaced (see below).
#
# Object-local coordinates are ld(0), ld(1) -- an interior texture must
# translate WITH the object, so it is evaluated at (X-x0, Y-y0) and not at
# (X, Y). Coverage is ld(2).
# ---------------------------------------------------------------------
_rect() {   # <x0> <y0> <w> <h> <bg-gray> <obj-expr using ld(0),ld(1)> <rate>
  local X0=$1 Y0=$2 W=$3 H=$4 BG=$5 OBJ=$6 r=$7
  local CX="clip(min(($X0)+$W\,X+1)-max(($X0)\,X)\,0\,1)"
  local CY="clip(min(($Y0)+$H\,Y+1)-max(($Y0)\,Y)\,0\,1)"
  local PRE="st(0\,X-($X0))\;st(1\,Y-($Y0))\;st(2\,$CX*$CY)"
  echo "nullsrc=s=1280x720:r=$r:d=1,format=gray,geq=lum='$PRE\;($BG)+(($OBJ)-($BG))*ld(2)',format=yuv420p"
}

# Gray values are the ORIGINAL colours' RGB bytes, not invented ones: gray g
# becomes Y = 16 + g*219/255 through format=yuv420p, so writing 255 here
# gives the same Y=235 that color=c=white did, 128 gives 0x808080's Y=126,
# and 48/60/51/160 give 0x303030/0x3c3c3c/0x333333/0xa0a0a0. Measured from
# the pre-rewrite scenes rather than assumed.

scene() {
  local CASE=$1 r=$2

  # The texture cases share one object and one motion, so only the interior
  # expression differs -- see "the texture series" in TESTING.md.
  local TEX_L7='128+110*sin(ld(0)/2.5)*sin(ld(1)/2.5)'
  local TEX_M2='128+110*sin(ld(0)/6.366)*sin(ld(1)/6.366)'
  local TEX_M3='128+110*sin(ld(0)/2.546)*sin(ld(1)/2.546)'
  # M1's texture was a floor()-quantised hash before this rewrite. It had to
  # change, and it is the only content change here: a texture quantised to a
  # 4px grid CANNOT be translated to a fractional position -- floor() would
  # snap it back to whole pixels and reintroduce, inside the object, exactly
  # the quantisation this rewrite removes from its boundary. Replaced with a
  # sum of five sines at incommensurate frequencies: still aperiodic with no
  # repeat, which is M1's actual job in the texture series, but band-limited
  # (shortest period 4.6px, comfortably above Nyquist) so it translates
  # exactly. Amplitude matches the old +-110 range.
  local TEX_M1='128+22*(sin(0.15*ld(0)+0.09*ld(1))+sin(0.28*ld(0)-0.21*ld(1))+sin(0.51*ld(0)+0.44*ld(1))+sin(0.83*ld(0)-0.97*ld(1))+sin(1.21*ld(0)+0.64*ld(1)))'

  case "$CASE" in

    # ---- L0: no motion. Must be a perfect passthrough. -------------------
    L0_static)      _rect '400'     '310' 100 100 0 255 "$r" ;;

    # ---- L1-L4: pure horizontal translation, sharp high-contrast edges.
    # The velocity ladder: well under the search ceiling, one coarse texel,
    # at the ceiling, and deliberately past it. ---------------------------
    L1_trans_8px)   _rect '192*T'   '310' 100 100 0 255 "$r" ;;   # 8px/frame
    L2_trans_16px)  _rect '384*T'   '310' 100 100 0 255 "$r" ;;   # 16 = one coarse texel
    L3_trans_23px)  _rect '552*T'   '310' 100 100 0 255 "$r" ;;   # 23 = the search ceiling
    L4_trans_40px)  _rect '960*T'   '310' 100 100 0 255 "$r" ;;   # 40 = beyond it

    # ---- L5: L2's motion, but the object is barely brighter than the
    # background (12/255 = 0.047, above the shader's MIN_CONTRAST of 0.02).
    L5_lowcontrast) _rect '384*T'   '310' 100 100 48 60 "$r" ;;

    # ---- L6-L7 / M1-M3: the texture series. IDENTICAL 300x300 object,
    # IDENTICAL 16px/frame motion -- only the interior texture differs.
    # This is the controlled experiment that isolates what the motion
    # search can and cannot resolve. --------------------------------------
    L6_flat_large)     _rect '384*T' '210' 300 300 0 128        "$r" ;;
    L7_textured_large) _rect '384*T' '210' 300 300 0 "$TEX_L7"  "$r" ;;  # period 15.7px ~= motion
    M1_noise_large)    _rect '384*T' '210' 300 300 0 "$TEX_M1"  "$r" ;;  # aperiodic, no repeat
    M2_period40)       _rect '384*T' '210' 300 300 0 "$TEX_M2"  "$r" ;;  # period 40px: unambiguous
    M3_period16_trap)  _rect '384*T' '210' 300 300 0 "$TEX_M3"  "$r" ;;  # period == motion: worst case

    # ---- M4: contrast BELOW the shader's MIN_CONTRAST gate (3/255 =
    # 0.0118), unlike L5 which sits above it. Tests the gate itself.
    M4_belowgate)   _rect '384*T'   '210' 300 300 48 51 "$r" ;;

    # ---- L8: diagonal motion, to catch axis asymmetry in the search. -----
    L8_diagonal)    _rect '384*T'   '216*T' 100 100 0 255 "$r" ;;

    # ---- L9: two objects crossing in opposite directions -> genuine
    # occlusion, which the forward/backward consistency check must handle.
    # Composited in the same order the old overlay pair used, so the grey
    # box passes in front of the white one.
    #
    # Note this case's SOURCE frames change with the rewrite, unlike every
    # other one: 300+300*t is not an integer at odd source frames, so the
    # old scene was snapping them and the new one places them exactly.
    L9_occlusion)
      local CA="clip(min((300+300*T)+100\,X+1)-max((300+300*T)\,X)\,0\,1)*clip(min(310+100\,Y+1)-max(310\,Y)\,0\,1)"
      local CB="clip(min((900-300*T)+100\,X+1)-max((900-300*T)\,X)\,0\,1)*clip(min(310+100\,Y+1)-max(310\,Y)\,0\,1)"
      echo "nullsrc=s=1280x720:r=$r:d=1,format=gray,geq=lum='st(0\,$CA)\;st(1\,$CB)\;st(2\,255*ld(0))\;ld(2)+(160-ld(2))*ld(1)',format=yuv420p" ;;

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
    # One confound remains even now that these are exact-coverage scenes,
    # and it is not removable by construction: equal mean velocity is not
    # equal difficulty. Error grows faster than linearly with speed, and the
    # ramp spends half its time below the mean and half above, so the mean of
    # the per-frame scores is not the score at the mean speed. It can push
    # the accelerating case either way. Read a twin difference as "what
    # acceleration costs on this trajectory", not as an isolated coefficient.
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
    A1_accel_8mean)  _rect '192*T*T' '310' 100 100 0 255 "$r" ;;  # 0->16px/f, mean 8  -- twin of L1
    A2_accel_16mean) _rect '384*T*T' '310' 100 100 0 255 "$r" ;;  # 0->32px/f, mean 16 -- twin of L2
    A3_accel_23mean) _rect '552*T*T' '310' 100 100 0 255 "$r" ;;  # 0->46px/f, mean 23 -- twin of L3

    # ---- A4-A7: CONSTANT ACCELERATION, TEXTURED, IN THE BAND REAL FOOTAGE
    # OCCUPIES. A1-A3 above have exactly the right magnitudes but a FLAT
    # interior, so the flow -- and therefore the acceleration field -- exists
    # only on their perimeter: measured coverage 2-15%, with the readings that
    # do appear saturating the encoding. They cannot calibrate the field, for
    # the same reason O1-O3 could not and O5 had to be built.
    #
    # These are their textured twins, and they close the one real gap in the
    # ground truth: real footage measures mean |a| 0.55-1.5 px/interval^2,
    # which is precisely where the field is known to be least reliable and
    # where, until these, nothing textured existed to measure it against.
    #
    # x = X0 - 24V*T + 24V*T^2, so velocity sweeps LINEARLY from -V to +V
    # px/frame and acceleration is a constant 2C/fps^2 = V/12. Two properties
    # that matter:
    #   - peak |velocity| is V by construction, so V <= 20 keeps the whole
    #     scene inside the coarse search's ~23px/frame reach. A1-A3 do not
    #     have this property (A3 ends at 46px/f), so their later frames
    #     confound a reach failure with an acceleration failure.
    #   - velocity passes through ZERO mid-scene: a genuine reversal, which
    #     is the case the round-trip trust gate exists to separate from
    #     occlusion. These exercise it against known truth for the first time.
    A4_accel_tex_a033) _rect '400-96*T+96*T*T'   '210' 300 300 0 "$TEX_M2" "$r" ;;  # a=0.333, v -4..+4
    A5_accel_tex_a067) _rect '400-192*T+192*T*T' '210' 300 300 0 "$TEX_M2" "$r" ;;  # a=0.667, v -8..+8
    A6_accel_tex_a133) _rect '400-384*T+384*T*T' '210' 300 300 0 "$TEX_M2" "$r" ;;  # a=1.333, v -16..+16
    A7_accel_tex_a167) _rect '400-480*T+480*T*T' '210' 300 300 0 "$TEX_M2" "$r" ;;  # a=1.667, v -20..+20

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

    # R3: R2's rotation exactly, textured interior. The discriminating
    # control for the R2 failure -- see _blobt above.
    R3_rot_tex)
      _blobt '640' '360' '2.56*T*T' 150 "$r" ;;

    # ---- O1-O3: OSCILLATION -- the tridirectional shader's test ladder.
    #
    # Why oscillation and not a stronger linear ramp: the quadratic
    # correction a 3-frame shader can apply peaks at a/8 px mid-interval
    # (a in px/interval^2), but a linear ramp changes velocity by a px/frame
    # every frame, so any a big enough to matter (>= ~4, for half a pixel)
    # drives the object past the ~23px/frame search reach within about
    # three frames. It cannot be sustained. x = A*sin(w*t) sustains high
    # acceleration indefinitely at bounded velocity -- and it is also the
    # camera-vibration / pan-jitter regime, which is the real-world content
    # class where constant-velocity placement is systematically wrong.
    #
    # Calibration (v_peak = A*w/24 px/frame, a_peak = A*w^2/576 px/int^2,
    # mid-frame placement error = a_peak/8):
    #
    #   case  A(px)  f(Hz)  v_peak  a_peak  mid-err  quadratic validity
    #   O1     40    1.0     10.5     2.7    0.34px  clean (cubic term ~0.1px)
    #   O2     20    2.5     13.1     8.6    1.07px  partial (cubic ~0.9px)
    #   O3     12    4.0     12.6    13.2    1.64px  model edge (cubic > 2px,
    #                                               6 samples/period)
    #
    # All three keep v_peak comfortably under the search ceiling, so any
    # failure is about PLACEMENT, not reach. O3 is deliberately at the edge
    # of what a quadratic (constant-acceleration) model can represent: a
    # win there was never promised by the hypothesis.
    O1_osc_gentle) _rect '600+40*sin(6.2832*T)'  '310' 100 100 0 255 "$r" ;;
    O2_osc_medium) _rect '600+20*sin(15.708*T)'  '310' 100 100 0 255 "$r" ;;
    O3_osc_hard)   _rect '600+12*sin(25.133*T)'  '310' 100 100 0 255 "$r" ;;

    # ---- O4/O5: the same oscillation on a LARGE object, flat and textured.
    #
    # O1-O3 are flat 100x100 boxes, which is the worst possible content for
    # measuring acceleration and was chosen before that was understood. A
    # flat object has no matchable texture in its interior, so the flow field
    # is non-zero only at its edges -- and the edges are exactly where the
    # anchor's two flows fail to cancel (occlusion), which is where an
    # acceleration estimate is meaningless. All signal and all noise land in
    # the same texels. See TRIDIRECTIONAL.md, "the current blocker".
    #
    # O5 puts interior texture 150px from the nearest boundary, so the
    # estimate can be read somewhere occlusion cannot reach. O4 is its
    # control: identical size and motion, flat fill, so O5 minus O4 isolates
    # interior texture exactly the way L6/L7/M1/M2/M3 isolate it for the
    # velocity ladder.
    #
    # Motion is O2's throughout (A=20px, 2.5Hz: v_peak 13.1 px/frame,
    # a_peak 8.6 px/int^2, 1.07px mid-frame placement error), so O4/O5 are
    # also directly comparable to O2 and differ from it only in object size.
    # Texture is M2's period-40px sine product: unambiguous against a 13px
    # travel distance, and band-limited so it translates exactly.
    O4_osc_flat300)     _rect '600+20*sin(15.708*T)' '210' 300 300 0 128       "$r" ;;
    O5_osc_textured)    _rect '600+20*sin(15.708*T)' '210' 300 300 0 "$TEX_M2" "$r" ;;

    # ---- O6: the JERK CONTROL for O5, and the only way to separate two
    # things a single sinusoid confounds by construction.
    #
    # In x = A*sin(w*t) the acceleration is -A*w^2*sin(w*t) and the jerk is
    # -A*w^3*cos(w*t), so |a| is SMALL exactly where jerk is LARGEST (the zero
    # crossing) and largest where jerk vanishes (the peak). Every low-|a|
    # sample in O5 is therefore also a maximum-jerk sample, and the observed
    # error there cannot be attributed to magnitude without a control.
    #
    # O6 has the same texture, same object size and same peak |a| band as O5's
    # low samples, but A*w^3 is 7.8x smaller (40*6.2832^3 against
    # 20*15.708^3). So at a MATCHED |a| ~ 2.2 the two scenes sit at opposite
    # ends of the jerk range: O6 near its peak, O5 near its crossing. That is
    # the controlled comparison.
    #
    # Peak |a| = 40*6.2832^2/576 = 2.74 px/interval^2; peak velocity 10.5px/f,
    # comfortably inside the coarse search's reach.
    O6_osc_tex_gentle)  _rect '600+40*sin(6.2832*T)' '210' 300 300 0 "$TEX_M2" "$r" ;;

    *) echo "UNKNOWN_CASE"; return 1 ;;
  esac
}

ALL_CASES="L0_static L1_trans_8px L2_trans_16px L3_trans_23px L4_trans_40px L5_lowcontrast L6_flat_large L7_textured_large M1_noise_large M2_period40 M3_period16_trap M4_belowgate L8_diagonal L9_occlusion A1_accel_8mean A2_accel_16mean A3_accel_23mean F1_fourier_edge F2_fourier_accel R1_rot_const R2_rot_accel O1_osc_gentle O2_osc_medium O3_osc_hard O4_osc_flat300 O5_osc_textured A4_accel_tex_a033 A5_accel_tex_a067 A6_accel_tex_a133 A7_accel_tex_a167 O6_osc_tex_gentle R3_rot_tex"

# The six added 2026-08-31 are in ALL_CASES deliberately rather than in a
# group of their own: a case that is not run by default is a case that rots.
# They cost more than the rest -- the blob's boundary is evaluated per pixel
# by geq, at roughly 11s per 60fps second against well under a second for a
# rectangle overlay. Their rows are additive, so every historical number for
# the fourteen cases above remains directly comparable.
ACCEL_CASES="A1_accel_8mean A2_accel_16mean A3_accel_23mean"
# The textured constant-acceleration twins and the jerk control, added
# 2026-08-31. A1-A3 carry the right magnitudes but a FLAT interior, so the
# acceleration field exists only on their perimeter -- measured coverage
# 2-15%, with the few readings saturating the encoding -- and they cannot
# calibrate it. These carry TEX_M2, hold |velocity| inside the coarse search's
# reach, and pass through a genuine reversal, which is the case the round-trip
# trust gate exists to separate from occlusion. O6 is the JERK CONTROL for O5:
# same texture, same object, same peak-|a| band, 7.8x less jerk -- the only way
# to separate magnitude from rate-of-change, which one sinusoid welds together
# by construction.
FIELD_CASES="A4_accel_tex_a033 A5_accel_tex_a067 A6_accel_tex_a133 A7_accel_tex_a167 O6_osc_tex_gentle"
SHAPE_CASES="F1_fourier_edge F2_fourier_accel R1_rot_const R2_rot_accel"
OSC_CASES="O1_osc_gentle O2_osc_medium O3_osc_hard O4_osc_flat300 O5_osc_textured"
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
