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

    *) echo "UNKNOWN_CASE"; return 1 ;;
  esac
}

ALL_CASES="L0_static L1_trans_8px L2_trans_16px L3_trans_23px L4_trans_40px \
L5_lowcontrast L6_flat_large L7_textured_large M1_noise_large M2_period40 \
M3_period16_trap M4_belowgate L8_diagonal L9_occlusion"
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
