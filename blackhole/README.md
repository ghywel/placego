# A black hole that is not Schwarzschild

One script, `geodesic_disc.py`, numpy only, with ffmpeg for the encode. It renders a
thin glowing dust disc around a black hole by tracing every pixel's light ray
backwards through the spacetime, and it does not care which spacetime: the metric
enters as five functions of radius and angle, and the tracer inverts and
differentiates them numerically. Three are built in.

- `schwarzschild`: the control. Horizon at 2 M, innermost stable orbit at 6 M.
- `kerr`: the spinning hole (default spin 0.9). Frame dragging, the shadow
  flattened into a D on its prograde side, the disc reaching in to 2.32 M.
- `jp`: the Johannsen-Psaltis deformation of that Kerr metric (default deviation
  3). It is not a solution of the vacuum Einstein equations at all. It is the
  kind of parametrised non-Kerr black hole astronomers test the no-hair theorem
  against, and its image is whatever integrating its light paths gives.

    ./geodesic_disc.py jp out 120 960 540
    ffmpeg -f rawvideo -pix_fmt rgb24 -s 960x540 -r 24 -i out/frames.rgb -vf format=yuv420p -c:v libx264 jp.mp4

A 960x540 frame traces in about six minutes on one CPU; 3840x2160 takes about two
hours and should be run with four bands (the sixth argument) so it fits in memory.
The disc's inner edge, its rotation and its redshift are all found from the metric,
so dropping a new metric into `metric_cov()` brings its own disc with it.

This lives beside the interpolation project rather than inside it. It was written in
an evening for the owner's curiosity, after the question "can you render a black
hole that is not the Schwarzschild metric", and it stays because the tracer is
general and small. There is no general solution to render: that is numerical
relativity on a supercomputer. This is two steps beyond Schwarzschild, the second of
them beyond any exact solution.
