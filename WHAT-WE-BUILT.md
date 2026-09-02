# What we built, in plain language

*This document explains the work in this repository to a reader with no
background in video engineering or mathematics. Everything technical it
summarises is measured and recorded in detail elsewhere in the repository —
see "where to look" at the end. Where something is uncertain, unproven, or
broken, this document says so, because the honest limits are as much a part
of the work as the results.*

---

## What it is, in one paragraph

We built a small program that runs on an ordinary graphics card, watches
video as it plays, and measures — for every point on the screen, live — not
just which way things are moving and how fast, but whether they are
**speeding up, slowing down, or changing direction**, and how sharply. Most
motion software stops at speed. This measures **acceleration**, and in its
newest version the **change in acceleration** (physicists call that "jerk" —
the lurch you feel when a driver stamps on the brakes). The readings have
been tested against scenes where the true answer is known exactly, and on
the kind of motion ordinary footage contains they are typically within a
few percent of the truth. The limits of where it works — and where it
currently fails — are measured and stated below with the same care as the
successes.

## An analogy

Every modern TV that "smooths" motion has something like a speedometer for
each part of the picture: it knows things are moving and how fast, and it
assumes they carry on in a straight line at a steady pace. We added the
accelerometer. The difference matters in the same way it matters in a car:
a speedometer tells you that you're doing 40; the accelerometer tells you
that you're braking hard. For a machine watching the world — or a TV
guessing where a thrown ball will be between two frames — "braking hard" is
often the thing worth knowing.

## What it's for

**The modest use: smoother video.** TVs and video players invent in-between
frames to make 24-frames-per-second film play smoothly at 60. They place
moving objects on straight lines, which is wrong whenever something is
accelerating. Ours places them on the curve. Measured on test scenes, this
gives real but modest picture improvements — up to about 4 dB (a solid,
visible gain) on strongly accelerating motion, and essentially no change on
steady motion, which is most of what films contain. This use works today.

**The interesting use: the measurements themselves.** Run the program at
the video's own frame rate — no new frames invented at all — and its output
is not a picture but a **map**: for every point, a live reading of
velocity, acceleration, and jerk. That turns a camera plus a cheap graphics
chip into a motion instrument. Possible applications — and we stress
*possible*: none of these has been built or validated —

- a driving system noticing that a pedestrian has suddenly changed
  direction, before their new position makes it obvious;
- sports and biomechanics analysis from ordinary footage;
- scientific measurement of the kind fluid-dynamics laboratories do with
  lasers and specialist cameras, from plain video;
- early warning of things beginning to fall, slip, or oscillate.

The instrument would be the *front end* of such systems — the sense organ,
not the brain. Something else must decide what an acceleration means.

## How it works, gently

Film is a series of still frames. Two frames tell you where something was
and where it is now — a straight line, which is speed. **Three** frames let
you draw a curve — which is acceleration. **Four** frames let the curve
itself bend — which is jerk. The program looks at small patches of the
image, finds where each patch went from frame to frame (coarsely at first,
then more and more finely, down to fractions of a single pixel), and fits
that curve through each patch's positions. It does this for hundreds of
thousands of patches, sixty times a second, which is what graphics cards
are good at.

One piece of plumbing had to be invented for any of this to be possible:
graphics-card video programs ("shaders") in the standard open-source video
engine this is built on (libplacebo, used by well-known video players)
could only ever see **two** frames at a time. We wrote a patch — a
carefully-contained modification — that hands them up to eight. That patch
is the enabling contribution; the shaders are what we built on top of it.

## How we know it isn't lying

This was run as an exercise in the scientific method, deliberately.

- **Ground truth first.** We test on synthetic scenes whose motion is a
  mathematical formula, so the true answer at every point and instant is
  known *exactly* — not estimated. The instrument's reading is compared
  against that truth, in physical units, before any real footage is
  trusted.
- **Predictions before results.** For the major experiments we wrote down
  in advance what should happen and what would count as failure — including
  one case where the mathematics predicted our new four-frame version would
  *not* improve the acceleration readings at all. It didn't, to the digit.
  A prediction that survives an honest chance to fail is worth more than
  any number of confirmations.
- **Failures kept on the record.** Wrong diagnoses are corrected in the
  documents, not deleted from them. This week alone the record gained: a
  belief about the dominant error source that was overturned twice; a
  "confirmation" that turned out to be the program silently not running at
  all (caught by a diagnostic marker, now mandatory); and a measuring tool
  that was quietly clipping its own readings (caught, fixed, and the trap
  documented).
- **Controls.** When two possible causes were tangled together, we built a
  scene that separated them, rather than arguing. Twice this week the
  control overturned the standing explanation.

The headline calibration: at the start of this week, on the gentle motion
that real footage mostly contains, the acceleration readings were wrong by
**more than the value being measured** — an error above 100%. After three
measured improvements (each one tested against the same truth), typical
error in that range is now **2–7%**. The jerk readings — which to our
knowledge no comparable real-time system produces at all — measure within
about 3–8% at their strongest, with a known noise floor.

## What it cannot do — read this as carefully as the good news

- **Rotation is currently unreliable.** A spinning object's acceleration
  readings are wrong by large factors (often more than 100%, with the
  direction off by tens of degrees). We found this by testing our own
  instrument against rotating scenes; we then built a control to rule out
  the easy explanation, and it failed too, so the fault is real and deeper
  than first thought. The cause is not yet diagnosed. **A turning vehicle
  is rotation. Nobody should attach this to anything safety-critical.**
- **It can only measure where there is visible pattern.** Blank walls,
  clear sky, smooth surfaces: no reading. This is a physical limit of
  tracking patches, not a bug — but it means the map is sparse, and its
  coverage varies from around 15% to nearly 100% depending on the content.
- **Lone edges give confidently wrong readings.** An isolated edge only
  reveals motion *across* itself, not along it (a known optical
  limitation), and the instrument does not yet flag those regions — it
  currently reports contaminated values there instead of "no measurement."
  The fix is known and named, but not built.
- **It is one frame late, always.** Measuring a curve through the present
  requires the next frame. At cinema rates that is 42 thousandths of a
  second. We proved (rather than assumed) that no rearrangement of the
  same frames removes this.
- **Faster cameras make it harder, not easier.** Per-frame acceleration
  shrinks with the square of the frame rate, so at very high frame rates
  the signal sinks toward the noise floor. Higher rates need *more* frames
  in the fit, not just faster ones.
- **Sudden events are excluded, not measured.** Scene cuts and moments
  where objects hide one another are detected and gated out; the reading
  there is deliberately withheld.
- **Testing is narrow.** Synthetic scenes plus a small amount of real
  footage; three or four consumer GPUs; 720p and 1080p. No peer review, no
  independent replication yet, and the enabling patch has not yet been
  accepted upstream. The picture-smoothing use is a hair *worse* than
  simpler methods on a few sharp, steady scenes — measured, recorded, and
  traded deliberately.

## Is this new? An honest answer

**The mathematics is not new.** A 2019 academic paper ("Quadratic Video
Interpolation", NeurIPS) contains the same core algebra for acceleration
between frames, and later work extended it to four frames — all of it
inside large neural networks, offline, judged on picture quality. Fluid
dynamicists have measured velocity-and-acceleration fields from image
sequences for decades (a field called particle image velocimetry), using
pulsed lasers and laboratory rigs. We searched the record before the final
work and wrote down what we found.

**What appears to be new** — as far as our search of the record shows — is
the combination: doing it *deterministically* (the same input always gives
the same answer, which neural networks don't promise), *in real time on
ordinary hardware*, *inside a standard video pipeline* anyone can build,
with the **measurement itself as the product** — calibrated against exact
truth, with coverage, confidence, and failure modes stated. We did not
discover new mathematics. We may have built a new instrument out of old
mathematics. The record of prior work, with citations, is in the
repository (PRIOR-ART.md); if we have missed prior art, we would genuinely
like to know.

## The shader is a template, not the point

The deliverable of this project is not a file of shader code. It is the
concrete, tested method the file expresses: how to estimate a motion
field carrying acceleration and jerk from N frames, deterministically,
with its precision, calibration and failure modes stated. The
ffmpeg/libplacebo/Vulkan pipeline it currently runs in was the
*instrument* used to derive that method — chosen because it let one
person and an AI assistant iterate at extraordinary speed on ordinary
consumer hardware, with ground truth available at every step — not
because it is the method's natural home.

The specific shader is written in one dialect (the mpv "hook" flavour of
GLSL) and runs today as a production candidate. But every pass in it is
ordinary parallel arithmetic — block matching, weighted sums, small
polynomial fits — and translates to any vendor's compute platform: CUDA,
Metal, Direct3D, ROCm, whatever comes next. Part of that claim is
measured rather than assumed: on Apple Silicon the identical kernel
logic runs at the same speed through the portable path and through
Apple's native API, to under half a percent. The mathematics survives
translation untouched.

Ports that lean into a vendor's own pipeline should expect to run
*faster* than this reference, not slower: the portable path pays real
taxes (on Apple, a measured ~28× per-dispatch overhead and a structural
per-frame memory round-trip) that a native integration simply deletes.
And any port can prove itself: the test ladder and the field
calibrations are the acceptance numbers, and they are ground truth, not
our implementation's output. This repository holds the recipe and the
proof that the recipe works. The kitchen was rented.

## Try it in five minutes

There is now a native Mac demonstration app — a window with buttons, no
ffmpeg, no patches, no command-line pipelines — and it is the easiest
way to see all of this with your own eyes.

**The prebuilt app ships right here**: `QuadDemo-macos-arm64.zip`,
alongside this document (Apple-silicon Macs). Unzip it and open
`QuadDemo.app`. On a downloaded copy macOS will object once —
right-click → Open, or System Settings → Privacy & Security → Open
Anyway — and then it just runs.

**To build it yourself, once** — four commands on any reasonably recent
Mac, and at the end you have the same double-clickable app forever
after:

```
xcode-select --install                 # Apple's free build tools
brew install shaderc spirv-cross       # the shader translation step
cd metal-demo && ./make-app.sh         # builds QuadDemo.app + its zip
open QuadDemo.app
```

(Terminal folk: `./gen.sh && swift run -c release QuadDemoUI` runs the
same thing without the bundle.)

What you will see: a textured block moving under known laws of motion,
interpolated live from 24 to 60 frames per second. Drag the **A/B
wipe** to compare against plain 24p. Then — the actual point — switch
**Show** to the **acceleration field** or the **jerk field**: the same
computation, read out as a measurement instead of a picture. The block
glows with its own acceleration; the background, which isn't moving,
stays dark. Open a video of your own (mp4/mov) and watch the instrument
read real footage. The fps counter tells the truth about what your
machine can do — this runs on the smallest GPU Apple sells, just not
quickly at film sizes.

The demo is itself the "Port it" invitation below, already accepted
once: the shader machine-translated to Metal, verified against the same
ground truth as the original, and measurably faster than the portable
pipeline on the same hardware (metal-demo/, with the full plan and
outcomes in METALPORT.md).

## What to do next with it

For anyone picking this up:

1. **Reproduce it.** The build guide (BUILDANDUSAGE.md) works on
   Linux, Windows, and macOS, and the test suite needs no GPU at all —
   a software renderer is enough to verify every correctness claim.
2. **Break it.** The test ladder (tests/) is designed so failures
   localise themselves. The two known failures — rotation, and lone edges —
   are the most valuable places to dig. The rotation diagnosis is the top
   open problem: the measurements say the patch-tracking itself goes wrong
   by whole pixels on rotating content, and we do not yet know why.
3. **Extend it.** Five frames is the next step and has two argued payloads
   waiting (an independent cross-check of the acceleration, and smoother
   fits over longer windows). The generator that builds the four-frame
   version from the three-frame one shows the pattern; going to N frames
   is mechanical.
4. **Port it.** Done once — the Metal demo above is the worked example,
   built by machine-translating the GLSL and verifying against the same
   ladder and calibrations, and it came out 30–46% faster than the
   portable pipeline. CUDA, Direct3D, ROCm and the rest remain open, and
   the translator (tests/gen_metal.py) is most of the work for any of
   them.
5. **Upstream the patch**, so any player using the engine can run these
   shaders — that was the project's founding goal and remains open.

## Where to look

- `README.md` — the enabling patch, documented for upstream review
- `METHODOLOGY.md` — how the work was actually done, including the
  division of labour between the human and the AI
- `TESTING.md` and `tests/` — the ground-truth test ladder
- `TRIDIRECTIONAL.md` — the three-frame experiment: hypothesis,
  algebra, calibration, failures and all
- `QUADDIRECTIONAL.md` — the four-frame experiment, with its
  pre-registered predictions and their outcomes
- `PRIOR-ART.md` — where this sits in the scientific record
- `PLAN.md` — the working research plan, kept honest
- `metal-demo/` and `METALPORT.md` — the native Metal port and demo app:
  the template claim, executed and measured

## Who did this

This project is a collaboration between **a human**, who set the
direction, supplied the priors, the hardware, the eyes on real footage, and
— repeatedly, and decisively — the scientific discipline ("even for a
superintelligence, 'already correct' is well worth proving"; the proving
promptly found two real failures), and **Claude, an AI assistant made by
Anthropic**, which wrote the code, designed and ran the experiments, and
wrote these documents, under that direction. The method that made it work
was neither the human's intuition nor the machine's speed alone, but the
loop between them: hypotheses cheap enough to test, tests honest enough to
fail, and a standing rule that every claim — including "already correct",
and including everything in this document — is worth checking.

Human edit: This authors stream of consciousness can be directly accessed at the subreddit here: 

https://www.reddit.com/r/nframe

This is not meant as an invitation to get to know me - leave me alone. It is a public record of what I did and how I did it in my own words without the AI.
