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

## The rest of this directory

Moved beside the tracer on 2026-09-11 from the scratch tree, so the record's scripts are in the record's
repository. Each line is the script's own first docstring line. They write renders and logs outside the tree
under `NP_SCRATCH/eyes/blackhole/` and drops under `HOT_DROPS`; `build_site.py` packs the lot into the
static site and its zip.

- `bhrender.sh` -- The black hole: encode the traced frames to an mp4 for the eyes, then put it through the human reading
- `blackhole.py` -- A Schwarzschild black hole with a thin, opaque, glowing dust disc, seen from a camera near the disc's plane
- `build_site.py` -- Pack the black-hole series (2026-09-07/08) into a dependency-free static website for external hosting:
- `glome.py` -- Fly through the 3-sphere: an honest render from INSIDE (2026-09-10).
- `greybody.py` -- Hawking radiation of a Schwarzschild black hole in photons: the greybody factors, the spectrum, the power, and
- `hawkapproach.py` -- The approach: a static (hovering) observer descends toward a Schwarzschild black hole that is radiating Hawking
- `hawkchart.py` -- The chart: photon greybody factors and the Hawking photon spectrum against the blackbody it is usually drawn as,
- `hawkcolor.py` -- Shared pieces for the Hawking renders (2026-09-08): colour from a spectrum, the Hawking spectrum from greybody.npz,
- `hawkmode.py` -- The Hawking mode itself, at the wavelength it is actually emitted at (2026-09-08).
- `hawkrender.sh` -- Hawking radiation, rendered as far as the mathematics honestly allows (2026-09-08): the hovering approach film,
- `kerr.py` -- Black holes that are NOT Schwarzschild, rendered from the same camera by one metric-agnostic geodesic tracer
- `kerr4k.py` -- THE 4K FORM of kerr.py (the owner, 2026-09-08: "a 4K render of the Johannsen-Psaltis by itself, regardless of
- `kerr4krender.sh` -- 
- `kerrrender.sh` -- Encode the three metrics' frames: one mp4 each, a triptych video (Schwarzschild | Kerr 0.9 | Johannsen-Psaltis),
- `nball.py` -- The volume of the unit ball in n dimensions, drawn in numpy with the Hawking caption font (2026-09-10).
- `run4k.sh` -- 
