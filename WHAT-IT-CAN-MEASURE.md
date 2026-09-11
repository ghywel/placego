# What it can measure

The question this answers is "what are these shaders even for", asked 2026-09-10 after a run of measurements
that made the old answer look wrong.

The old answer was an application: cinema, then instrumentation, then perhaps driving or sports. That split
does not survive contact with the numbers. **Perfect per-segment shader selection across eighteen real
segments of two live-action films and a cartoon is worth 0.04 dB.** One file wins fifteen of the eighteen
outright and wins on all three sources separately. For the picture, on real content, the choice of shader in
this family is very nearly a matter of indifference — so a shader cannot be "for cinema" in any sense that
distinguishes it from the others.

There are also indefinitely many applications, as there are indefinitely many synthetic test cases, so a
table indexed by application would never be finished and would not be a specification of anything.

**The axis that does separate these shaders is the DERIVATIVE ORDER of the motion they can report, and how
cleanly they report it.** That axis is short, it is closed, and every row of it has been measured.

## The table

All field figures are from the same textured oscillating square (a 300x300 multi-scale texture at 600, 210)
scored against the analytic derivative at N:N, decoded from the machine modes and averaged over the object
eroded by 40 px. "Reads at" is peak truth divided by the residual after fitting a gain — the honest
signal-to-noise, since a phase answer with a collapsed gain is not an answer.

| you want | frames | shaders | reads at | gain | cost vs linear |
|---|---|---|---|---|---|
| the picture | 2 | all | shader choice worth 0.04 dB on 18 real segments | — | 1.6x |
| velocity | 2 | all | correlation 1.000 at N:N | 0.98 | 1.6x |
| acceleration | 3 | tri and up | 25 to 172 to one, over an 8x range of magnitude | 0.93-1.00 | 2.8x |
| jerk, from four frames | 4 | quad | **3.2 to 4.7 to one** | 0.76-0.99 | 3.2x |
| jerk, from five frames | 5 | quint | **118 to one** | 0.90 | 4.7x |
| snap | 5 | quint (solves it, then discards it) | 20 to one | 0.93 | 4.7x |
| crackle and beyond | — | none | the family's ceiling is degree four | — | — |
| divergence | 2+ | read_view 9 | 93% of truth on matched textured content | 0.93 | 1.6x |
| curl | 2+ | read_view 9 | 95% of truth on matched textured content | 0.95 | 1.6x |
| shear | 2+ | read_view 9 | 96% of truth on matched textured content | 0.96 | 1.6x |

Costs are 720p, 24 to 60, on the RX 6600, timed from a file source with the output discarded. They do not
transfer between machines: on the M2 the six-frame shader is 11x the two-frame base where here it is 3.6x.
Window size dominates, not pass count, so a picker should show the local milliseconds rather than a table
from elsewhere.

## The row that changes what the family is for

**Jerk from four frames reads at about four to one. Jerk from five frames reads at a hundred and eighteen to
one.** Same scene, same full scale, same scorer, a residual of 1.201 against 0.047 — twenty-five times
cleaner. That is the single largest difference any measurement in this project has found between two members
of the family, and it is not a picture difference at all.

The reason is truncation, not noise, and it was established separately (NFRAME-LIMITS.md, "Jerk is not
noise-limited"). A four-frame window fits a cubic through three links, so on any motion richer than a cubic
the next term contaminates the third derivative, and the contamination scales with the jerk itself: across an
eightfold range of jerk magnitude the four-frame signal-to-residual stays flat at 3.2 to 4.7 and never
improves. The five-frame window fits an exact quartic through four links, absorbing one more order, and the
residual collapses.

So **the higher-order shaders are not better interpolators. They are instruments for higher derivatives, and
the fifth frame is where jerk becomes a measurement rather than a rumour.** That is what they are for. It is
also why the eighteen-segment picture test found them worth 0.04 dB: it was asking the wrong question of
them.

## What the family cannot do at all

- **Crackle and above do not exist here.** Six frames do not fit a quintic: the six-frame shader fits a
  quartic again, spending its extra link on overdetermination and a per-texel fit residual instead of another
  order. That was a deliberate choice and the seven-frame analysis argued it on paper.
- **Deformation is measured now, and it works.** One vector per block cannot express a plate of jelly
  wobbling; what distinguishes wobble from sliding is the velocity gradient — divergence, curl and shear.
  All three were scored on matched content 2026-09-10 (NFRAME-LIMITS.md, "The gradient tensor's third
  component") and read 93, 95 and 96 percent of truth, with cross-talk under 10% at worst and under 3% in
  five cases of six. The condition is texture and enough motion: the earlier 30-80% figure for divergence
  came from a flat disc moving under a pixel a frame, and that case is still hard. So a deforming subject is
  supported by evidence, provided it has surface detail to match -- with the boundary drawn the same
  afternoon (NFRAME-LIMITS.md, "Weird geometry"): articulation, transverse waves and similarity motion read
  to a few percent; smooth NON-AFFINE deformation does too, at gain 0.96 and correlation 0.99 on a jelly at three times
  the strain rate that first failed -- provided the content has structure above the coarse level's Nyquist,
  about 40 px at this frame size. Content dominated by a period near that scale, stretched or sheared by more
  than about one percent per frame, reverses in the coarse search and one pixel in five stays wrong
  (NFRAME-LIMITS.md, "The non-affine failure: a cliff", demonstrated by moving the texture's period).

- **The field has never been measured on real content.** Every figure in the table above comes from a
  synthetic scene with an analytic answer. That is the only place an exact answer exists, and it is the right
  place to calibrate — but it means the transfer to real footage is assumed, not shown.

## What follows

An application does not select a shader. It selects a derivative order, and the order selects the shader:

- anything wanting the picture or velocity is served by the two-frame recommendation, and the rest of the
  family is wasted cost;
- anything wanting acceleration wants three frames and gets a solid reading;
- anything wanting jerk wants FIVE, not four, and the difference is twenty-five times;
- anything wanting deformation is supported: all three tensor components read to about five percent on
  textured content that moves.

The shear gap is closed. The one that remains is the larger of the two: no derivative of any order, and no
component of the tensor, has ever been measured on real content. Every number above comes from a synthetic
scene with an analytic answer, which is the only place an exact answer exists and the right place to
calibrate — but the transfer to real footage is assumed, not shown.
