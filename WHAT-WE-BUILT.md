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
itself bend — which is jerk. (Five would let the bend itself bend. For
ordinary film that is a frame too far; we have now built the five-frame
version and measured exactly where it does pay — see "what to do next".)
The program looks at small patches of the
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
  documents, not deleted from them. In one week alone the record gained: a
  belief about the dominant error source that was overturned twice; a
  "confirmation" that turned out to be the program silently not running at
  all (caught by a diagnostic marker, now mandatory); and a measuring tool
  that was quietly clipping its own readings (caught, fixed, and the trap
  documented).
- **Controls.** When two possible causes were tangled together, we built a
  scene that separated them, rather than arguing. Twice in that week the
  control overturned the standing explanation.

The headline calibration: at the start of that week, on the gentle motion
that real footage mostly contains, the acceleration readings were wrong by
**more than the value being measured** — an error above 100%. After three
measured improvements (each one tested against the same truth), typical
error is now **a few percent** — one to two percent on a typical frame and
five to ten on the worst, at accelerations of about a pixel per frame per
frame; on our gentlest test, a third of that, it is around 11% (17% before
the neighbour-borrowing repair), because a smaller signal meets the same
noise. The jerk readings — which to our
knowledge no comparable real-time system produces at all — read within about
3% of their peak on every frame checked of the oscillating test scenes, and
under 1% through the native Mac port (an earlier version of this sentence
reported a 7% typical miss and a 60% miss on the last frames; both were the
measuring tool comparing against the wrong instant, since corrected — the
readings themselves were right), and
their noise floor has now been measured directly, on a scene whose true jerk
is exactly zero: between a twentieth and a tenth of a pixel per frame cubed.
That is small, but on the gentle motion of everyday footage we expect the
true jerk to be only a few to ten times larger — expect, because real
footage has been viewed through the jerk reading (the demo app below) but
cannot be calibrated against it: no real scene comes with its true jerk
known — which is the practical limit of the instrument and, as "what to do
next" explains, the reason the frame count stops at four for film.

## What it cannot do — read this as carefully as the good news

- **Rotation is still the weak point — measured, diagnosed in three
  parts, and only one part improved.** A plain edge only reveals motion
  across itself, so a flat turning disc gives a field wrong in direction
  by 60–80 degrees and in size by about 100%, and no repair has moved
  that: it is a physical limit, not a bug. A repeating texture turning in
  place can lock onto its own pattern. And the tracker's coarse steps
  sample the picture without smoothing it, so fine texture moving by a
  fraction of a coarse step confuses them; the obvious fix — smooth first —
  was built and refuted, because the detail it removes is exactly the
  contrast the tracker needs. The neighbour-borrowing repair halves the
  error on a *textured* turning disc, and a closer look the same morning
  changed what the remaining error is: point by point it is noise, not
  bias — the same kind, and less than twice the size, as the noise on a
  straight-moving object, which our calibrations never showed because they
  always averaged over the object. Averaged over a patch 24 pixels across,
  the acceleration of the turning disc reads within about 15% with its
  direction within 6 degrees; point by point it does not. So a turning
  object can be read at patch resolution, not pixel resolution, and a flat
  one cannot be read at all. **A turning vehicle is rotation. Nobody should
  attach this to anything safety-critical.**
- **It can only measure where there is visible pattern.** Blank walls,
  clear sky, smooth surfaces: no reading. This is a physical limit of
  tracking patches, not a bug — but it means the map is sparse, and its
  coverage varies from around 15% to nearly 100% depending on the content.
  The newest variant lets a blank patch borrow the motion of its textured
  neighbours, which fills the map but is a guess there, not a measurement.
- **Lone edges give confidently wrong readings.** An isolated edge only
  reveals motion *across* itself, not along it (a known optical
  limitation), and the instrument does not yet flag those regions — it
  currently reports contaminated values there instead of "no measurement."
  The fix is known and named; its first piece, a gate that stops the
  tracker's middle step from accepting a match that merely slides along an
  edge, is now built, and the reading itself is not yet flagged.
- **It is at least one frame late, always.** Measuring a curve through the
  present requires the next frame. At cinema rates that is 42 thousandths
  of a second; the five-frame version, which looks two frames ahead, is 83.
  We proved (rather than assumed) that no rearrangement of the same frames
  removes this.
- **Faster cameras make it harder, not easier.** Per-frame acceleration
  shrinks with the square of the frame rate, so at very high frame rates
  the signal sinks toward the noise floor. Higher rates need *more* frames
  in the fit, not just faster ones — or, more simply, more widely spaced
  ones; the rule for the spacing is under "what to do next".
- **Sudden events are excluded, not measured.** Scene cuts and moments
  where objects hide one another are detected and gated out; the reading
  there is deliberately withheld.
- **Testing is narrow.** Synthetic scenes plus a small amount of real
  footage; five consumer GPUs (two Intel, two AMD, one Apple); 720p and
  1080p. No peer review, no independent replication yet, and the enabling
  patch has not yet been accepted upstream. For picture smoothing, every one
  of our current shaders beats or matches the standard straight-line method
  on every test scene; on one — motion too small to detect — simply
  repeating frames scores a little better than any of them: measured,
  recorded, and traded deliberately. The synthetic test ladder itself is an
  instrument of continuous refinement - new tests find new problems. 

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
*faster* than this reference: the portable path pays real
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
alongside this document (Apple-silicon Macs(tested); Intel Macs
(untested) use the build path below). Unzip it and open `QuadDemo.app`.
On a downloaded copy macOS will object once — right-click → Open, or
System Settings → Privacy & Security → Open Anyway — and then it just
runs. You can check the code yourself if you are worried about about
doing this.

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
2. **Break it** The test ladder (tests/) is designed so failures localise 
   themselves. The first repair to the tracker's coarsest step is now built,
   as a separate variant that costs about a tenth more time: it weighs two
   more candidate motions instead of following the first it finds, and on
   the test scenes that is worth a few decibels on most of them and costs
   nothing measurable on the rest; on real footage the difference is small
   but consistent. A second repair on top of it lets featureless patches
   borrow the motion of their textured neighbours, checked against both
   frames; on hand-drawn animation that is worth up to two decibels more, and a
   setting of it tuned for animation matches the recommended shader there
   at a third of the work. A third repair, found while chasing rotation,
   removes a quarter-pixel bias the tracker's finest step had on any
   repeating pattern; on such patterns the field readings are two to
   three times steadier point by point, and the picture gains a little on
   most test scenes. The turning disc's map then exposed a blind spot in the
   tracker's coarsest step -- motion along the diagonal of a repeating
   pattern -- and in our test scenes, every one of which had moved
   horizontally. The repair is built into the measuring shaders: the
   tracker's middle step now also tries "no motion" as a starting guess,
   and keeps it only where the coarse guess was fooled by a pattern too
   fine for it, or where it is plainly the better match and not merely
   sliding along an edge -- that last test being the edge gate this
   document had listed as known but unbuilt. Diagonal scenes are joining
   the ladder. SHADERS.md says when to use each.
3. **Extend it** The engine is designed to be N-frame extensible,
   but more frames does not necessarily mean better output. See
   NFRAME-LIMITS.md for more detail. One exception was found on paper and
   then built: a fifth frame placed *symmetrically* around the measurement
   removes most of the acceleration error on fast repetitive motion and
   makes the jerk reading two to three times cleaner on slow motion.
   Measured, it reads the acceleration on tiny fast oscillations three to
   seven times more accurately and its jerk noise floor is three times
   lower, at the cost of a fifth more render time (QUINTDIRECTIONAL.md).
4. **Port it.** Done once — the Metal demo above is the worked example,
   built by machine-translating the GLSL and verifying against the same
   ladder and calibrations, and it came out 30–46% faster than the
   portable pipeline. CUDA, Direct3D, ROCm and the rest remain open, and
   the translator (tests/gen_metal.py) is most of the work for any of
   them.
5. **Upstream the patch**, so any player using the engine can run these
   shaders — that was the project's founding goal and remains open.

**One case deserves singling out, because the usual conclusion reverses.**
For ordinary film — where things move smoothly across many frames — each
extra frame we add buys less than the one before, and four is about where it
stops being worth it. But for motion that *repeats quickly* — something
vibrating, resonating, or a small particle jiggling in a flow or a trap —
that reasoning inverts. When a full cycle of the motion takes only about six
frames to complete, the higher-order terms stop shrinking: each one carries
as much signal as the last, and only noise decides when to stop. Our own test
scenes show it plainly. Across thirty-two cases, the four-frame version beat
the three-frame version clearly in exactly one — the fastest oscillation we
test, six frames per cycle — and its jerk reading there is accurate to about
one percent. Everywhere else the fourth frame is mostly noise.

So a laboratory looking at fast, small, repetitive motion is in a different
regime from a television set smoothing a film, and should expect a different
answer: more frames keep paying, and a fifth does. The
practical advice is to choose a frame rate — or use every k-th frame — so
that the motion of interest is captured **six to ten times per cycle**.
Faster and the measurement drowns in noise; slower and the curve cannot be
represented at all. The five-frame version now exists, and on the six- and
eight-frames-per-cycle test scenes it reads acceleration three to seven
times closer to the truth than the four-frame one; on ordinary film it adds
nothing to the picture and costs a fifth more time.

**The instrument's yardsticks are the pixel and the frame, and that has a
consequence anyone changing camera should know.** Every rule inside it — how
far it will look for a match, how big a patch it compares, how fine a pattern
its coarsest glance can resolve, where the painted view starts to show a
reading — is measured in pixels per frame, not in metres per second. So the
same scene filmed at four times the resolution moves four times as many
pixels per frame while the tracker's reach stays where it was, and a
repeating pattern that was coarse enough to resolve becomes one it cannot;
and the same scene filmed at three times the frame rate has one ninth the
acceleration per frame while the noise per reading stays the same, so a
reading that was clear at 24 frames per second sinks toward the noise at 72.
We saw both at once when we rendered the turning disc at 4K: the velocity
map grew four large wrong patches where the coarsest step was fooled, and
the acceleration map dissolved into noise. Neither is a new failure; both
are the old limits at a new scale. The practical advice joins the advice
above: the tracker's yardsticks should be scaled with the frame — a deeper
coarse step and a longer reach at 4K, thresholds in proportion — and the
frame rate, or the stride through the frames, chosen so the motion of
interest is sampled six to ten times per cycle rather than as fast as the
camera allows. Shaders tuned to the resolution and rate of the camera are the
same idea as shaders tuned to film or to the laboratory; that scaling has
not been built yet, and the 4K disc is the test it will be judged on.

## Where to look

- `HANDOVER.md` — how to get up to speed and take one of the open leads,
  for a person or for an assistant
- `README.md` — the enabling patch, documented for upstream review
- `METHODOLOGY.md` — how the work was actually done, including the
  division of labour between the human and the AI
- `tests/TESTING.md` and `tests/` — the ground-truth test ladder
- `TRIDIRECTIONAL.md` — the three-frame experiment: hypothesis,
  algebra, calibration, failures and all
- `QUADDIRECTIONAL.md` — the four-frame experiment, with its
  pre-registered predictions and their outcomes
- `QUINTDIRECTIONAL.md` — the five-frame experiment: where a fifth frame
  pays and where it does not
- `NFRAME-LIMITS.md` — where the frame count stops paying and why, what
  "wobble" (the acceleration itself changing within the few frames being
  fitted) really costs, and the rotation diagnosis with its control scenes
  and the sampling defect they uncovered
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

This is not meant as an invitation to get to know me - leave me alone. It is a public record of
what I did and how I did it in my own words without the AI.

Everybody - The proof is in the seeing - You won't believe your eyes. Go find a m-series apple
computer, run the app, and see for yourselves if i'm making all of this up.

Edit: The actual shader that is baked in to the app is now actually very old. It would
probably be more awesome with an update. The first iteration probably took about 10 minutes
to produce. The second iteration took a few eyeball glance-overs to check the UX worked
properly. If you want an update I am not going to build it for you, you have to build it
yourselves. Good luck.
