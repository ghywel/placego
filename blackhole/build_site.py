"""Pack the black-hole series (2026-09-07/08) into a dependency-free static website for external hosting:
hot-drops/blackhole-site/ (index.html, hypersphere.html, media/, scripts/) and hot-drops/blackhole-site.zip. Films are probed for
their size and length, posters are extracted with ffmpeg, the scripts are embedded (escaped) and offered as
downloads. No names, no titles, no external resources.
"""
import html
import os
import pathlib
import shutil
import subprocess
import zipfile

# run from a shell with the project's ffmpeg build and mingw64/bin on PATH, as every tool in tests/ does
HERE = pathlib.Path(__file__).resolve().parent                                     # scripts/blackhole: every packed script lives here
NP = pathlib.Path(os.environ.get("NP_SCRATCH", "E:/nframe-project/np-scratch"))
NPB = NP / "eyes" / "blackhole"                                                    # the renders, logs and run summaries
HD = pathlib.Path(os.environ.get("HOT_DROPS", "E:/nframe-project/hot-drops"))
SCR = REPO = HYP = HERE
SITE = HD / "blackhole-site"
MEDIA, SCRIPTS = SITE / "media", SITE / "scripts"
if SITE.exists():
    shutil.rmtree(SITE)
MEDIA.mkdir(parents=True); SCRIPTS.mkdir()

FILMS = [
    "blackhole-disc-10s.mp4", "blackhole-disc-picture-velocityreading.mp4",
    "blackhole-schwarzschild-5s.mp4", "blackhole-kerr-5s.mp4", "blackhole-jp-5s.mp4",
    "blackhole-triptych-schwarzschild-kerr09-johannsenpsaltis-5s.mp4", "blackhole-triptych-velocityreading-5s.mp4",
    "blackhole-johannsenpsaltis-4k-10s.mp4",
    "hawking-approach-hover-40M-to-2.02M-10s.mp4", "hawking-mode-dipole-quadrupole-10s.mp4",
    "hypersphere-flight-24fps.mp4",
]
STILLS = [
    "blackhole-disc-frame120.png", "blackhole-triptych-frame60.png", "blackhole-johannsenpsaltis-4k-frame120.png",
    "hawking-spectrum-chart.png", "hawking-mode-frame120.png",
    "hawking-approach-r40.00M.png", "hawking-approach-r10.00M.png", "hawking-approach-r4.00M.png",
    "hawking-approach-r2.50M.png", "hawking-approach-r2.10M.png", "hawking-approach-r2.02M.png",
    "hypersphere-inside-frame0.png", "hypersphere-inside-frame240.png", "nball-volume-by-dimension.png",
]
POSTER_FRAME = {"blackhole-disc-picture-velocityreading.mp4": 120, "blackhole-schwarzschild-5s.mp4": 60,
                "blackhole-kerr-5s.mp4": 60, "blackhole-jp-5s.mp4": 60, "blackhole-triptych-velocityreading-5s.mp4": 60,
                "blackhole-johannsenpsaltis-4k-10s.mp4": 120}
POSTER_STILL = {"blackhole-disc-10s.mp4": "blackhole-disc-frame120.png",
                "blackhole-triptych-schwarzschild-kerr09-johannsenpsaltis-5s.mp4": "blackhole-triptych-frame60.png",
                "hawking-approach-hover-40M-to-2.02M-10s.mp4": "hawking-approach-r40.00M.png",
                "hawking-mode-dipole-quadrupole-10s.mp4": "hawking-mode-frame120.png",
                "hypersphere-flight-24fps.mp4": "hypersphere-inside-frame0.png"}
SOURCES = [  # (file, origin, one-line description)
    ("blackhole.py", SCR, "The first tracer: Schwarzschild only, the Binet equation in each ray's own orbital plane, the thin disc, the dust."),
    ("geodesic_disc.py", REPO, "The general tracer: Hamilton's equations, the metric entering as five covariant components; schwarzschild, kerr and jp built in; per-band checkpoints for 4K."),
    ("README.md", REPO, "The general tracer's readme."),
    ("greybody.py", SCR, "Hawking radiation in photons: the Regge-Wheeler equation integrated for the greybody factors, the spectrum, the power (Page 1976 reproduced), and the mode functions at the peak."),
    ("hawkcolor.py", SCR, "Shared pieces: CIE colour from a spectrum, the Hawking spectrum, a tone map, a 5x7 bitmap font."),
    ("hawkapproach.py", SCR, "The hovering approach film: escape cone, lensing table, the glow as a blackbody at the local temperature."),
    ("hawkmode.py", SCR, "The mode film: the l = 1 and l = 2 photon modes at the spectrum's peak, in the equatorial plane."),
    ("hawkchart.py", SCR, "The spectrum chart and the mass ladder."),
    ("hawkrender.sh", SCR, "The driver that ran the three Hawking scripts and encoded the films."),
    ("greybody.log", NPB, "The greybody solver's printed checks, verbatim."),
]


def probe(path):
    out = subprocess.run(["ffprobe.exe", "-v", "error", "-select_streams", "v:0", "-count_frames", "-show_entries",
                          "stream=width,height,nb_read_frames", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, check=True).stdout.strip().split(",")
    w, h, n = int(out[0]), int(out[1]), int(out[2])
    return w, h, n


meta = {}
for f in FILMS:
    src = HD / f
    shutil.copy2(src, MEDIA / f)
    w, h, n = probe(src)
    meta[f] = (w, h, n, src.stat().st_size)
    print(f"{f}: {w}x{h}, {n} frames, {src.stat().st_size / 1e6:.1f} MB")
for f in STILLS:
    shutil.copy2(HD / f, MEDIA / f)
posters = {}
for f in FILMS:
    if f in POSTER_STILL:
        posters[f] = POSTER_STILL[f]
    else:
        n = POSTER_FRAME.get(f, 60)
        p = f.replace(".mp4", f"-poster.jpg")
        subprocess.run(["ffmpeg.exe", "-y", "-hide_banner", "-loglevel", "error", "-i", str(HD / f), "-vf", f"select=eq(n\\,{n})",
                        "-frames:v", "1", "-q:v", "3", "-update", "1", str(MEDIA / p)], check=True)
        posters[f] = p
for name, origin, _ in SOURCES:
    shutil.copy2(origin / name, SCRIPTS / name)
HYP_SOURCES = [
    ("glome.py", "The 3-sphere from inside: closed-form great-circle rays against balls at the 600-cell's vertices, a headlamp, the observer's own head; one still or the whole flight."),
    ("nball.py", "The volume of the unit ball in every dimension, drawn with the 5x7 font."),
]
for name, _ in HYP_SOURCES:
    s = (HYP / name).read_text(encoding="utf-8")
    # glome.py and nball.py carry no machine paths since 2026-09-11; the assert below is the guard
    assert "loki" not in s and "nframe" not in s and "E:/" not in s and "C:/" not in s, name
    (SCRIPTS / name).write_text(s, encoding="utf-8", newline="\n")
FFDIR_LINE = 'FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs'
G_LINE = 'NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/eyes/blackhole"; HD="${HOT_DROPS:-/e/nframe-project/hot-drops}"'
# the driver's machine paths become placeholders in the packed copy
drv = (SCRIPTS / "hawkrender.sh").read_text(encoding="utf-8")
drv = drv.replace(FFDIR_LINE, 'FFDIR="${FFDIR:-/path/to/ffmpeg}"          # the directory holding ffmpeg.exe / ffprobe.exe')
drv = drv.replace('export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH"', 'export PATH="$FFDIR:$PATH"')
drv = drv.replace(G_LINE, 'G=$(pwd); HD=$G/out; mkdir -p "$HD"')
assert "loki" not in drv and "nframe" not in drv
(SCRIPTS / "hawkrender.sh").write_text(drv, encoding="utf-8", newline="\n")
lg = (SCRIPTS / "greybody.log").read_text(encoding="utf-8").replace("E:/nframe-project/np-scratch/eyes/blackhole/", "")
(SCRIPTS / "greybody.log").write_text(lg, encoding="utf-8", newline="\n")
(SCRIPTS / "jp-4k-summary.txt").write_text(
    (NPB / "full4k_jp" / "summary.txt").read_text(encoding="utf-8").strip() + "\n"
    "traced 8294400 rays in 6238 s: 3498121 hit the disc, 150703 fell in, 4645576 escaped (3840x2160, 240 frames, 4 bands)\n",
    encoding="utf-8")


def mb(f):
    return f"{meta[f][3] / 1e6:.0f} MB"


def video(f, caption):
    w, h, n, _ = meta[f]
    return (f'<figure><video controls preload="metadata" poster="media/{posters[f]}" width="{w}" height="{h}">'
            f'<source src="media/{f}" type="video/mp4"></video>'
            f'<figcaption><code>{f}</code> &middot; {w}&times;{h}, {n} frames at 24 fps, {mb(f)}. {caption}</figcaption></figure>')


def image(f, caption, cls=""):
    return f'<figure class="{cls}"><a href="media/{f}"><img src="media/{f}" alt="{html.escape(caption)}" loading="lazy"></a><figcaption><code>{f}</code>. {caption}</figcaption></figure>'


def source_block(name, desc):
    text = (SCRIPTS / name).read_text(encoding="utf-8")
    kb = len(text.encode("utf-8")) / 1024
    return (f'<details><summary><code>{name}</code> <span class="dim">({kb:.0f} kB)</span> &middot; {desc} '
            f'<a class="dl" href="scripts/{name}" download>download</a></summary><pre>{html.escape(text)}</pre></details>')


CSS = """
:root { --bg:#0b0b0d; --ink:#e6e3dc; --dim:#9a968f; --rule:#2a2a2f; --accent:#f0a24a; --link:#8ec2ff; --code:#141418; }
* { box-sizing:border-box; }
html { color-scheme:dark; }
body { margin:0; background:var(--bg); color:var(--ink); font:17px/1.55 Georgia,'Times New Roman',serif; }
header { padding:64px 24px 32px; text-align:center; border-bottom:1px solid var(--rule); }
header h1 { font-size:2.6em; margin:0 0 8px; font-weight:normal; letter-spacing:0.01em; }
header p { color:var(--dim); margin:0; }
nav { position:sticky; top:0; background:rgba(11,11,13,0.94); border-bottom:1px solid var(--rule); padding:10px 24px; font:15px system-ui,sans-serif; z-index:2; }
nav a { color:var(--link); text-decoration:none; margin-right:18px; }
main { max-width:1100px; margin:0 auto; padding:16px 24px 80px; }
section { padding:40px 0; border-bottom:1px solid var(--rule); }
h2 { font-weight:normal; font-size:1.9em; margin:0 0 4px; }
h3 { font-weight:normal; font-size:1.3em; margin:32px 0 8px; color:var(--accent); }
.lede { color:var(--dim); font-style:italic; margin-top:0; }
p { max-width:78ch; }
figure { margin:24px 0; }
figure video, figure img { width:100%; height:auto; display:block; background:#000; border:1px solid var(--rule); }
figcaption { font:14px/1.5 system-ui,sans-serif; color:var(--dim); margin-top:8px; }
.strip { display:grid; grid-template-columns:repeat(3,1fr); gap:12px; }
.strip figure { margin:0; }
.row { display:grid; grid-template-columns:repeat(3,1fr); gap:12px; }
.row figure { margin:0; }
table { border-collapse:collapse; font:15px/1.45 system-ui,sans-serif; margin:16px 0; width:100%; }
th, td { text-align:left; padding:6px 10px; border-bottom:1px solid var(--rule); vertical-align:top; }
th { color:var(--dim); font-weight:normal; }
td.num, th.num { text-align:right; font-variant-numeric:tabular-nums; }
code { font:0.92em ui-monospace,Consolas,monospace; color:#d8d4cc; }
pre { background:var(--code); border:1px solid var(--rule); padding:14px; overflow:auto; font:13px/1.45 ui-monospace,Consolas,monospace; max-height:70vh; }
details { margin:10px 0; border:1px solid var(--rule); border-radius:4px; padding:6px 12px; }
summary { cursor:pointer; font:15px/1.5 system-ui,sans-serif; }
.dim { color:var(--dim); }
.dl { color:var(--link); margin-left:8px; }
a { color:var(--link); }
.note { border-left:3px solid var(--accent); padding:4px 14px; color:var(--dim); font-size:0.95em; }
footer { color:var(--dim); font:14px/1.5 system-ui,sans-serif; text-align:center; padding:32px 24px; }
@media (max-width:760px) { .strip, .row { grid-template-columns:1fr 1fr; } body { font-size:16px; } }
"""

page = []
A = page.append
A("<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>")
A("<title>Black holes, rendered</title><style>" + CSS + "</style></head><body>")
A("<header><h1>Black holes, rendered</h1><p>Three spacetimes traced by hand, and the light a black hole makes for itself.<br>"
  "numpy and one CPU; nothing in the pictures is painted on. Where a feature appears, the equations put it there.</p></header>")
A("<nav><a href='#one'>1. Schwarzschild</a><a href='#two'>2. Not Schwarzschild</a><a href='#three'>3. Hawking radiation</a><a href='hypersphere.html'>4. The 3-sphere &rarr;</a><a href='#scripts'>Scripts</a><a href='#colophon'>Colophon</a></nav>")
A("<main>")

# ---- 1 ----------------------------------------------------------------------------------------------------------
A("<section id='one'><h2>1. A Schwarzschild black hole with a disc</h2><p class='lede'>The control: the simplest black hole, seen the way the famous pictures see it.</p>")
A("<p>Geometric units, G = c = 1, the mass M = 1: the horizon at r = 2, the photon sphere at 3, the innermost stable "
  "circular orbit at 6. A thin, opaque, glowing dust disc from 6 M to 18 M; a camera at 40 M, 78 degrees off the disc's "
  "axis, so the far side of the disc is lensed over and under the shadow. Every pixel's light ray is integrated once, "
  "backwards from the camera, in its own orbital plane with the Binet equation u'' = &minus;u + 3u&sup2; (u = 1/r), "
  "fourth-order Runge-Kutta, 921,600 rays, until it falls through the horizon (black), escapes to a faint star field "
  "looked up by its exit direction, or crosses the disc's plane between the two radii. A crossing keeps the disc's "
  "radius and azimuth there and the redshift factor g = &radic;(1 &minus; 3/r) / (1 + &Omega; b<sub>z</sub>) of a "
  "Keplerian emitter, which carries the gravitational and the Doppler shift together. Only the first crossing counts: "
  "the disc is opaque.</p>")
A("<p>Each frame is then a lookup: emission g&#8308; (1 &minus; &radic;(6/r)) r<sup>&minus;3</sup> times a multi-octave "
  "dust pattern in (log r, &phi;) that winds up under differential rotation, coloured by the observed temperature on a "
  "warm ramp. The picture has what the famous ones have because the physics puts it there: the shadow, the disc in "
  "front, its far side lensed into an arch above and a lobe below, the approaching side beamed bright, and the thin "
  "photon ring inside the shadow.</p>")
A(video("blackhole-disc-10s.mp4", "The Schwarzschild disc. The dust winds up under differential rotation, one turn in four seconds at the inner edge."))
A(image("blackhole-disc-frame120.png", "Frame 120 of the film."))
A("<h3>The same film through a motion-field reader</h3>")
A("<p>This work sits beside a video-interpolation project whose shaders estimate a velocity per texel in real time and "
  "can paint that estimate over the picture: hue for direction, opacity for speed. The black hole's disc is a warped, "
  "differentially rotating surface, and this is its field as the shader reads it: the picture on the left, the "
  "velocity reading on the right.</p>")
A(video("blackhole-disc-picture-velocityreading.mp4", "Picture and velocity reading side by side."))
A("</section>")

# ---- 2 ----------------------------------------------------------------------------------------------------------
A("<section id='two'><h2>2. Black holes that are not Schwarzschild</h2><p class='lede'>Every exact solution sets something to zero. Render one that is not the Schwarzschild metric.</p>")
A("<p>There is no general black hole to render: the general case exists only in numerical relativity, and even there as "
  "two holes merging on a supercomputer. What can be done is two steps out from Schwarzschild, the second of them "
  "beyond any exact solution. The second tracer, <code>geodesic_disc.py</code>, does not care which spacetime it is "
  "given. It integrates Hamilton's equations for a null geodesic in the full four dimensions, "
  "H = &frac12; g<sup>&mu;&nu;</sup> p<sub>&mu;</sub> p<sub>&nu;</sub> = 0, with the metric entering only as its five "
  "covariant components g<sub>tt</sub>, g<sub>t&phi;</sub>, g<sub>rr</sub>, g<sub>&theta;&theta;</sub>, "
  "g<sub>&phi;&phi;</sub> as functions of (r, &theta;). The inverse is taken numerically and the derivatives by central "
  "differences, so any stationary axisymmetric metric can be dropped in without deriving anything. The step shrinks "
  "toward the horizon and toward the coordinate poles (without the latter a seam appears at the top of the shadow, "
  "where rays pass over the pole). The disc's innermost stable orbit, orbital frequency and u<sup>t</sup> are found "
  "numerically from the metric, so a new metric brings its own disc; the redshift is Cunningham's "
  "g = 1 / (u<sup>t</sup> (1 &minus; &Omega; p<sub>&phi;</sub>)). The same camera as before: a zero-angular-momentum "
  "observer at 40 M, 78 degrees off the axis.</p>")
A("<table><tr><th>metric</th><th>what it is</th><th class='num'>horizon</th><th class='num'>innermost stable orbit</th><th>rays at 960&times;540: hit / fell / escaped</th></tr>"
  "<tr><td>schwarzschild</td><td>a = 0, the control; the general tracer reproduces the first one</td><td class='num'>2.000</td><td class='num'>6.00</td><td>186,972 / 27,470 / 303,958</td></tr>"
  "<tr><td>kerr</td><td>spin a = 0.9: frame dragging, the shadow flattened into a D on its prograde side, the disc reaching in to a third of the radius</td><td class='num'>1.436</td><td class='num'>2.32</td><td>213,379 / 16,055 / 288,966</td></tr>"
  "<tr><td>jp</td><td>Johannsen &amp; Psaltis (2011): that Kerr metric with the deformation h = &epsilon;<sub>3</sub> M&sup3; r / &Sigma;&sup2; in g<sub>tt</sub>, g<sub>t&phi;</sub>, g<sub>rr</sub>, g<sub>&phi;&phi;</sub>, &epsilon;<sub>3</sub> = 3. It solves no vacuum field equation; it is the kind of parametrised non-Kerr black hole astronomers test the no-hair theorem against</td><td class='num'>1.436</td><td class='num'>1.46</td><td>218,648 / 9,415 / 290,337</td></tr></table>")
A(video("blackhole-triptych-schwarzschild-kerr09-johannsenpsaltis-5s.mp4", "The three metrics from one camera: Schwarzschild, Kerr at a = 0.9, and the Johannsen-Psaltis deformation. The JP disc is smaller and dimmer and reaches almost to the horizon: its image is whatever integrating its light paths gives, nothing else."))
A(image("blackhole-triptych-frame60.png", "Frame 60 of the triptych."))
A("<div class='row'>" + video("blackhole-schwarzschild-5s.mp4", "Schwarzschild alone.") + video("blackhole-kerr-5s.mp4", "Kerr, a = 0.9, alone.") + video("blackhole-jp-5s.mp4", "Johannsen-Psaltis, a = 0.9, &epsilon;<sub>3</sub> = 3, alone.") + "</div>")
A("<h3>The Johannsen-Psaltis hole at 4K</h3>")
A("<p>The same tracer at 3840&times;2160: 8,294,400 rays in 6,238 seconds on one CPU, traced in four horizontal bands "
  "with a checkpoint per band (a run that is interrupted resumes where it stopped). 3,498,121 rays hit the disc, "
  "150,703 fell in, 4,645,576 escaped.</p>")
A(video("blackhole-johannsenpsaltis-4k-10s.mp4", "The Johannsen-Psaltis black hole at 4K. A large file."))
A(image("blackhole-johannsenpsaltis-4k-frame120.png", "Frame 120 at full resolution (3 MB)."))
A("<h3>The triptych through the motion-field reader</h3>")
A(video("blackhole-triptych-velocityreading-5s.mp4", "The three discs as the interpolation shader reads them."))
A("</section>")

# ---- 3 ----------------------------------------------------------------------------------------------------------
A("<section id='three'><h2>3. Hawking radiation, rendered as far as the mathematics allows</h2><p class='lede'>Hawking radiation is undetectable in nature because it is fainter than the cosmic background. A synthetic space has no background. Can a black hole be rendered close enough to see the never-seen glow?</p>")
A("<p>The answer has a negative half, computed rather than quoted, and two honest pictures.</p>")
A("<h3>The negative half</h3>")
A("<p><code>greybody.py</code> integrates the electromagnetic Regge-Wheeler equation for the photon modes born at the "
  "horizon, at 260 frequencies and eight multipoles: fourth-order Runge-Kutta in the tortoise coordinate from "
  "r = 3000 M in to r &minus; 2M = 10<sup>&minus;7</sup>, with the outgoing and ingoing parts separated at the horizon "
  "end to give the transmission. The checks: the transmission tends to 1 at high frequency; the dipole's goes as "
  "&omega;<sup>4.1</sup> at low frequency (theory: 4); the multipole sum tends to the capture cross-section 27&omega;&sup2; "
  "above &omega; ~ 1/M; and the total photon power comes out 3.364&times;10<sup>&minus;5</sup> &#8463;c&#8310;/G&sup2;M&sup2; "
  "against Page's 1976 value of 3.36&times;10<sup>&minus;5</sup>.</p>")
A(image("hawking-spectrum-chart.png", "The greybody factors by multipole (top) and the photon power spectrum (bottom) against the blackbody it is usually drawn as."))
A("<p>The potential barrier at r = 3M throws the long wavelengths back in, so the photon spectrum peaks at "
  "&omega;M = 0.243, six times the Hawking temperature where a blackbody peaks at 2.8, and that is a wavelength of "
  "25.8 M, which is 12.9 horizon radii <em>for a hole of any mass</em>. 98% of the power is in the &#8467; = 1 dipole "
  "(transmission 0.415 at the peak; the quadrupole's is 0.0004). A black hole radiating at its own peak is a pure "
  "dipole. Its light carries no image of it, at any distance, in any instrument: an emitter thirteen times smaller "
  "than its light is a point, and going closer never changes that. The wished-for render of a hole lit by its own "
  "Hawking glow does not exist, not for lack of signal but for lack of wavelength.</p>")
A("<table><tr><th>quantity</th><th>value</th></tr>"
  "<tr><td>photon power, this solver / Page 1976</td><td>3.364&times;10<sup>&minus;5</sup> / 3.36&times;10<sup>&minus;5</sup> &#8463;c&#8310;/G&sup2;M&sup2; (24% of the blackbody over the capture area)</td></tr>"
  "<tr><td>spectrum peak</td><td>&omega;M = 0.243 = 6.1 T<sub>H</sub>; wavelength 25.8 M = 12.9 horizon radii</td></tr>"
  "<tr><td>share of the power by multipole</td><td>&#8467; = 1: 98.0%, &#8467; = 2: 2.0%, the rest nothing</td></tr>"
  "<tr><td>mean photon energy</td><td>5.7 T<sub>H</sub></td></tr></table>")
A("<p>The mass ladder, photons only, the peak wavelength 25.8 GM/c&sup2;:</p>")
A("<table><tr><th>mass</th><th class='num'>T<sub>H</sub></th><th class='num'>horizon</th><th class='num'>peak wavelength</th><th class='num'>power</th><th>note</th></tr>"
  "<tr><td>10<sup>18</sup> kg</td><td class='num'>123,000 K</td><td class='num'>1.5 nm</td><td class='num'>19 nm</td><td class='num'>0.58 mW</td><td>ultraviolet</td></tr>"
  "<tr><td>2.0&times;10<sup>19</sup> kg</td><td class='num'>6,000 K</td><td class='num'>30 nm</td><td class='num'>392 nm</td><td class='num'>1.4 &micro;W</td><td>the Sun's colour; visible at arm's length as a bright star</td></tr>"
  "<tr><td>6.1&times;10<sup>19</sup> kg</td><td class='num'>2,000 K</td><td class='num'>91 nm</td><td class='num'>1.2 &micro;m</td><td class='num'>150 nW</td><td>the film's hole: a 35-km asteroid's mass; a faint orange star at arm's length</td></tr>"
  "<tr><td>10<sup>21</sup> kg</td><td class='num'>123 K</td><td class='num'>1.5 &micro;m</td><td class='num'>19 &micro;m</td><td class='num'>0.58 nW</td><td>infrared</td></tr>"
  "<tr><td>4.5&times;10<sup>22</sup> kg</td><td class='num'>2.73 K</td><td class='num'>67 &micro;m</td><td class='num'>0.86 mm</td><td class='num'>0.28 pW</td><td>T<sub>H</sub> equals the cosmic background: heavier holes absorb more than they emit, which is the observation problem in one line</td></tr>"
  "<tr><td>the Moon</td><td class='num'>1.7 K</td><td class='num'>0.11 mm</td><td class='num'>1.4 mm</td><td class='num'>0.11 pW</td><td></td></tr>"
  "<tr><td>the Earth</td><td class='num'>0.02 K</td><td class='num'>8.9 mm</td><td class='num'>11 cm</td><td class='num'>1.6&times;10<sup>&minus;17</sup> W</td><td></td></tr>"
  "<tr><td>the Sun</td><td class='num'>6.2&times;10<sup>&minus;8</sup> K</td><td class='num'>2.95 km</td><td class='num'>38 km</td><td class='num'>1.5&times;10<sup>&minus;28</sup> W</td><td></td></tr></table>")
A("<h3>Picture one: the approach</h3>")
A("<p>Ray optics, honest for the short-wavelength tail of the spectrum and stated as such. A static, hovering observer "
  "descends from 40 M to 2.02 M looking straight down and straight up. Every direction, traced backwards, either came "
  "from the horizon, carrying the Hawking glow (uniform: a blackbody at T<sub>H</sub> / &radic;(1 &minus; 2M/r), the same "
  "in every direction for a static observer), or from infinity, carrying nothing but starlight, lensed and blueshifted. "
  "That is the Unruh state, an evaporating hole in empty space: exactly the no-background case of the question. The "
  "border is the escape cone, sin &psi;<sub>e</sub> = (3&radic;3 M / r) &radic;(1 &minus; 2M/r), analytic and confirmed "
  "by the tracer on every frame.</p>")
A("<p>So <strong>the glow is the shadow</strong>: the disc that is black under external light is precisely the set of "
  "directions that carry Hawking flux, seven degrees across at 40 M, half the sky at 3 M, and at 2.02 M everything but "
  "a fifteen-degree cone straight up, into which the whole universe is compressed, Einstein rings at its rim. The colour "
  "runs orange-red (2000 K) through white (4900 K at 2.4 M) to blue-white (20,100 K at 2.02 M) while the camera's "
  "exposure drops 17 stops; the caption counts them. The thrust needed to hover ends at 2.46 c&#8308;/GM, five hundred "
  "thousand billion billion g, and there the glow's temperature T<sub>H</sub> / &radic;(1 &minus; 2M/r) tends to "
  "a / 2&pi;: the hovering observer's thermometer reads the Unruh temperature of its own acceleration. At the horizon, "
  "Hawking's radiation and Unruh's are one thing.</p>")
A(video("hawking-approach-hover-40M-to-2.02M-10s.mp4", "The descent. Left: looking down at the hole. Right: looking up, away from it. The glow eats the sky."))
A("<div class='strip'>" + "".join(image(f"hawking-approach-r{r}M.png", f"r = {r} M") for r in ("40.00", "10.00", "4.00", "2.50", "2.10", "2.02")) + "</div>")
A("<p class='note'>Stated limits. The glow is drawn as a blackbody, not as the greybody-filtered spectrum above, because "
  "the filter is the barrier at 3 M (a hoverer inside it sees the unfiltered flux) and because the filter is the same "
  "wave effect that forbids this picture's sharp edge: the blackbody is the one spectrum consistent with ray optics. "
  "The stars are drawn at fixed brightness with their true colour shift; under the auto-exposure that holds the glow "
  "they would vanish within a few M. The free-falling observer is not rendered: what a falling detector registers is a "
  "literature of its own, and the naive Doppler bookkeeping is not the whole answer.</p>")
A("<h3>Picture two: the mode itself</h3>")
A("<p>The thing ray optics cannot draw. The &#8467; = m = 1 photon mode at the peak frequency in the equatorial plane, "
  "Re[&psi;(r*) e<sup>i(&phi; &minus; &omega;t)</sup>], the flux-normalised amplitude: born at the horizon with unit "
  "amplitude, 41% transmitted through the barrier and 59% reflected (a near-standing wave inside 3 M), a spiral wave "
  "outside with a wavelength thirteen times the horizon. Beside it the &#8467; = m = 2 mode at the same frequency, "
  "trapped. Near the horizon the crests pile up (the tortoise coordinate runs to minus infinity) and peel off at the "
  "coordinate speed 1 &minus; 2M/r: the trans-Planckian side of Hawking's derivation, to scale.</p>")
A(video("hawking-mode-dipole-quadrupole-10s.mp4", "The dipole gets out; the quadrupole is trapped. Black disc: the horizon. Dashed ring: the barrier's peak at r = 3 M. Warm is positive, cool is negative."))
A(image("hawking-mode-frame120.png", "Frame 120 of the mode film."))
A("</section>")

# ---- 4: the hand-over to the second page ----------------------------------------------------------------------
A("<section id='four'><h2>4. <a href='hypersphere.html'>How would Einstein have felt to fly through his 3-Sphere with these miraculous machines we have made</a></h2>"
  "<p class='lede'>A separate page. Not a black hole: the shape of the universe Einstein first proposed, flown through from the inside.</p>")
A("<p>The same evening's question, one step further out. Einstein's first cosmology, in 1917, was a 3-sphere, chosen "
  "so that space could be finite without having an edge. The natural extension of the point, the circle and the sphere "
  "is generally held to be impossible to picture. The page argues that seeing it all at once is impossible for a reason "
  "that has nothing to do with the fourth dimension, that knowing it is already finished, and that flying through it is "
  "an ordinary three-dimensional render with one line changed; then it does the flight. "
  "<a href='hypersphere.html'>Read it and fly &rarr;</a></p>")
A("<a href='hypersphere.html'>" + image("hypersphere-inside-frame0.png", "Standing inside a 3-sphere. The grey grid behind everything is the back of the observer's own head, seen by light that has gone all the way round.") + "</a>")
A("</section>")
# ---- scripts ----------------------------------------------------------------------------------------------------
A("<section id='scripts'><h2>The scripts</h2><p class='lede'>numpy only; ffmpeg for the encodes. Each is a single file with its method in the docstring.</p>")
for name, _, desc in SOURCES:
    A(source_block(name, desc))
A(source_block("jp-4k-summary.txt", "The 4K run's summary line."))
A("<h3>Running them</h3><pre>"
  "python blackhole.py out 240 1280 720                # Schwarzschild disc, a few minutes\n"
  "python geodesic_disc.py jp out 120 960 540           # jp | kerr | schwarzschild; about six minutes\n"
  "python geodesic_disc.py jp out4k 240 3840 2160 4     # the 4K film, about two hours, resumable\n"
  "python greybody.py                                   # writes greybody.npz; half a minute\n"
  "bash hawkrender.sh                                   # the approach film, the mode film, the chart\n"
  "ffmpeg -f rawvideo -pix_fmt rgb24 -s 960x540 -r 24 -i out/frames.rgb -vf format=yuv420p -c:v libx264 out.mp4</pre>")
A("</section>")

# ---- colophon ---------------------------------------------------------------------------------------------------
A("<section id='colophon'><h2>Colophon</h2>")
A("<p>Geometric units throughout, G = c = 1 and, for the Hawking work, &#8463; = k<sub>B</sub> = 1 as well, with the mass "
  "M = 1; a mass in kilograms enters only when a temperature or a wavelength is quoted in ordinary units. What was "
  "checked: the general tracer reproduces the Schwarzschild control (horizon 2.000, innermost stable orbit 6.00); the "
  "greybody solver reproduces Page's 1976 photon power, the &omega;&#8308; law and the capture cross-section; the "
  "escape cone's analytic form agrees with the traced rays on every frame of the descent; flux is conserved through the "
  "barrier to one part in ten thousand for the dipole. What is not claimed: any picture of Hawking radiation itself. "
  "Such a picture does not exist, and the reason is the wavelength, not the noise.</p>")
A("<p>Computed, rendered and written over an evening and the following morning in September 2026, in a working "
  "session between the project's author and Claude, beside a video-interpolation project the black holes have nothing "
  "to do with. The dust is random; the rest is the equations.</p>")
A("</section></main>")
A("<footer>Black holes, rendered &middot; numpy, ffmpeg, one CPU</footer></body></html>")

(SITE / "index.html").write_text("\n".join(page), encoding="utf-8")

# ---- page two: the 3-sphere ---------------------------------------------------------------------------------------
TITLE2 = "How would Einstein have felt to fly through his 3-Sphere with these miraculous machines we have made"
page = []
A = page.append
A("<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>")
A("<title>" + html.escape(TITLE2) + "</title><style>" + CSS + "</style></head><body>")
A("<header><h1>" + html.escape(TITLE2) + "</h1><p>The 3-sphere is the shape of space in Einstein's first universe, 1917. This is the answer to a "
  "question about dimension, and a flight through the thing the question said could not be flown through.</p></header>")
A("<nav><a href='index.html'>&larr; Black holes</a><a href='#question'>The question</a><a href='#answers'>Three answers</a>"
  "<a href='#inside'>Inside</a><a href='#einstein'>Einstein's universe</a><a href='#scripts2'>Scripts</a><a href='#colophon2'>Colophon</a></nav>")
A("<main>")
# ---- the question -------------------------------------------------------------------------------------------------
A("<section id='question'><h2>The question, as it was put</h2><p class='lede'>Asked by the project's author, who has been asking it since a book on 3-D engine design at seventeen.</p>")
A("<p>A point shows all its detail to the eye at once. So does a line, and so does a map: pan and zoom as far as you "
  "like, everything is there on the plate. But a perspective frustum on a three-dimensional object reveals only a "
  "fragment. Look at the side of a mug and only that side is seen; the far side could carry any pattern at all. From "
  "below it might be solid; from above the cavity appears and the sides recede. The only way to know the mug is to turn "
  "it in time and remember, and even that is not the whole of it: the mug is atoms, and the space between the atoms. "
  "We call ourselves three-dimensional creatures in a three-dimensional world, and we are, but the eye is stolidly a "
  "two-dimensional camera. A true three-dimensional viewer would see all of a solid at once.</p>")
A("<p>So the fourth dimension is hard to think about, because each slice we can see holds so much less of it. The "
  "rendered hypercube falls into this trap: the animation is cute and it is not the object. And the hypersphere, the "
  "natural extension of point, circle, sphere, the shape it is speculated our universe really is, the one that wears "
  "&pi; the way every circle does, cannot be pictured at all. What is a sphere pushed into another addressable "
  "dimension, twice? There seems not even to be a name for it. Whichever way the system is traversed, rendering four "
  "dimensions to the two the eye receives loses all coherence of what the object represents. Is it simply "
  "unknowable? Or is it?</p>")
A("</section>")
# ---- three answers ------------------------------------------------------------------------------------------------
A("<section id='answers'><h2>Three answers, because it is three questions</h2><p class='lede'>Seeing it all at once; knowing it; flying through it. One is impossible, and not for the reason supposed; one is finished; one is a render.</p>")
A("<h3>Every creature sees one dimension fewer than it lives in</h3>")
A("<p>That is the wall, and it does not belong to the fourth dimension. A Flatlander, with a one-dimensional retina, "
  "sees a square as a line segment and can never see its interior; we look down on Flatland and see the whole square, "
  "inside and out, at once. A four-dimensional creature, with a three-dimensional retina, sees the mug the way we see a "
  "drawing on paper: both sides, the cavity, the base, every point of the glaze, all at once and without turning it. "
  "So a true three-dimensional viewer is not impossible in principle. It is not us. And that creature cannot see its "
  "<em>own</em> world all at once either, and is perplexed by the 4-sphere in exactly the way we are by the 3-sphere. "
  "The wall is not in front of the hypersphere; it is the shape of every eye, met at precisely the rung where it "
  "should be.</p>")
A("<h3>Two limits are tangled in the mug, and only one is about dimension</h3>")
A("<p>The atoms are a resolution problem: a four-dimensional creature would see the whole mug, at its own resolution, "
  "and be as ignorant of the lattice as we are. Set that aside and the mug's geometry is fully recoverable by exactly the "
  "method the question proposes. Turn it and remember: projections from every angle are complete information, which is "
  "the theorem a CT scanner runs on. The question was righter than it thought.</p>")
A("<h3>It has a name, and the construction in the question was correct</h3>")
A("<p>Mathematicians call it the 3-sphere, counting the dimension of the surface, because the surface is where one "
  "would live. Two things about the sequence: it does not begin with a point, since the zeroth sphere is a "
  "<em>pair</em> of points, the boundary of a segment; and the bowl construction in the question needs one more step, "
  "not a new idea. Two discs glued rim to rim make a sphere. Two solid balls glued skin to skin, every point of one "
  "surface to the matching point of the other, make the 3-sphere. The gluing cannot be performed in our space without "
  "crushing, but the object it defines is exact, and living in it is simple to say: walk out of ball A through its "
  "skin and arrive in ball B at the matching point; walk on, leave B, and arrive back in A at the antipode of the "
  "point of departure; walk on and arrive home, never having turned. Dante described precisely this around 1320: nine "
  "spheres of the heavens about the Earth, nine circles of angels about the point of light, the two systems sharing "
  "their outermost shell. The construction is seven centuries old, and it was made without the mathematics.</p>")
A("<h3>The ouroboros is not a metaphor; it is the definition</h3>")
A("<p>A circle is a line whose two ends are joined at a single point at infinity. A sphere is the plane plus one point, "
  "which is why a flat map of the Earth loses exactly the pole. The 3-sphere is ordinary space plus one point: go far "
  "enough in any direction whatever and arrive at the same place. So a complete map of it is already in hand. It is "
  "the space we are sitting in, read with the understanding that all of infinity is one point. Angles on that map are "
  "right, sizes far out are wrong, as Greenland is on Mercator, and it loses exactly one point. The question asked "
  "for an infinite map that could be panned and zoomed. That is it.</p>")
A("<h3>&pi; is the signature of Pythagorean distance</h3>")
A("<p>A sphere is the set of points at one distance; distance is a quadratic; the integral of a quadratic exponential "
  "is &radic;&pi;. A cube is the set of points within one distance measured by the largest coordinate instead, and "
  "there is no &pi; anywhere in it. That is why &pi; is all over physics: it appears wherever distance is quadratic, "
  "and the interval of relativity is quadratic too, so the question was right about the root. The chart carries the "
  "consequence. The volume of the unit ball rises to a peak in five dimensions and then falls to zero for ever; in a "
  "thousand dimensions it is 10<sup>&minus;886</sup>, and almost all of that lies within a hair of the skin. Every "
  "number on the chart is exact, and not one past three can be pictured. That is the whole of the argument that "
  "knowing and seeing are different things, and that knowing is the one we have.</p>")
A(image("nball-volume-by-dimension.png", "V<sub>n</sub> = &pi;<sup>n/2</sup> / &Gamma;(n/2 + 1): the volume of the unit n-ball, orange, and the surface of the unit (n&minus;1)-sphere, blue. The volume peaks at n = 5 (5.264), the surface at n = 7 (33.07)."))
A("</section>")
# ---- inside -------------------------------------------------------------------------------------------------------
A("<section id='inside'><h2>Inside: the flight</h2><p class='lede'>The 3-sphere's surface is three-dimensional. A creature living in it lives in a three-dimensional world with one rule changed: straight lines come back.</p>")
A("<p>That is what makes it renderable. A camera inside it is an ordinary camera; the renderer is a game engine with a "
  "single line altered, the ray. In four coordinates a straight line from p in the direction d is p&thinsp;cos&thinsp;t + "
  "d&thinsp;sin&thinsp;t rather than p + d&thinsp;t, and after t = 2&pi; it is home. A ball of angular radius &rho; about "
  "a centre c is entered where &lang;ray, c&rang; first reaches cos&thinsp;&rho;, which along a great circle is "
  "R&thinsp;cos(t &minus; &phi;) = cos&thinsp;&rho; with R and &phi; from two dot products: a closed form, no marching. "
  "The objects are the 120 vertices of the 600-cell, the four-dimensional icosahedron, each an 8-degree ball; the camera "
  "flies once round a great circle chosen to pass no closer than 17.3 degrees to any of them; a headlamp at the eye is "
  "the only light. Three things are true in there, and the film shows all three.</p>")
A("<p><strong>There is no horizon and no sky.</strong> Every direction ends on something, at most 2&pi; away, and a ray "
  "that misses every ball comes back to where it started. So the farthest thing in every direction is the back of "
  "one's own head, and the observer is drawn as a 3-degree ball just behind the eye: that is the grey grid behind "
  "everything. It is lit by the observer's own lamp after a trip round, at ninety times the brightness of anything a "
  "quarter of the way out, because light from a point reconverges not only at the antipode but at its source. The "
  "first render had a white sky, which is the one thing a closed universe cannot have; it was this, and the head was "
  "darkened and gridded so that it reads as what it is.</p>")
A("<p><strong>The antipode fills the view.</strong> Every path from a point reconverges at the point opposite, so an "
  "object there is enormous and, under a headlamp whose irradiance goes as 1/sin&sup2;d, brilliantly lit. And an "
  "object a quarter of the way round and one three-quarters round look identical in size and brightness in a still. "
  "Only motion separates them: the near ones sweep outward past the camera, the antipodal ones drift inward toward "
  "the centre, because the parallax rate changes sign at the equator. Watch a ball straight ahead: if it grows and "
  "sweeps out, it is near; if it grows and drifts in, it is at the far side of the universe.</p>")
A(video("hypersphere-flight-24fps.mp4", "One full circuit, twenty seconds, home from behind and never having turned. Reinhard exposure, headlamp only, one bounce."))
A("<div class='row'>" + image("hypersphere-inside-frame0.png", "Frame 0: standing still. The grid's warp toward the centre is the antipode.")
  + image("hypersphere-inside-frame240.png", "Frame 240: halfway round.") + "</div>")
A("<p class='note'>Stated limits. Direct lighting only, no interreflection, and a headlamp at the eye is the only source; "
  "the 600-cell is a choice of furniture, not physics; the colours label the balls by an angle about one fixed plane and "
  "mean nothing else; the exposure is a fixed Reinhard curve, noted in the caption. What is exact: the geodesics, the "
  "intersections, the 1/sin&sup2;d law and the fact that every ray terminates, which the renderer asserts on every "
  "frame.</p>")
A("</section>")
# ---- einstein -----------------------------------------------------------------------------------------------------
A("<section id='einstein'><h2>Einstein's universe, honestly</h2><p class='lede'>The title asks a question that cannot be answered. Here is what can be.</p>")
A("<p>Einstein's first cosmology, the 1917 paper that founded the subject, took space to be a 3-sphere: finite, so that "
  "the field equations would not need conditions at an infinity he distrusted, and without an edge, because a sphere "
  "has none. When Hubble's expansion made the static model untenable he gave up the stillness before the shape: his "
  "1931 model was an expanding and recontracting 3-sphere, and only the 1932 model with de Sitter went flat. He held "
  "both, which is exactly where the measurements now stand. Space is flat to within a fraction of a percent. If it "
  "is a 3-sphere after all, its radius of curvature is at least some two hundred billion light years against an "
  "observable radius of forty-six, so we would be seeing at most about seven percent of the way round; and the "
  "ouroboros has been looked for directly, since a space that closed within sight would show the same circle of the "
  "microwave sky twice, from two directions. WMAP and Planck were searched for matched circles and none were found. "
  "So <em>speculated</em>, in the question, is the right word.</p>")
A("<p>How he would have felt, flying through it, is not knowable, and the page will not pretend. What is knowable is "
  "this. The space in the film is the spatial section of his 1917 universe with the matter taken out and the light "
  "traced by the rule he wrote down, that light follows geodesics. Its two strange properties, that every path from a "
  "point refocuses at the antipode and that an observer's own light returns to them, are consequences he could "
  "compute and never see; the remark that in his universe one would see the back of one's own head is nearly as old "
  "as the model. He is also the physicist who at sixteen tried to picture riding beside a beam of light, and built a "
  "theory out of what the picture would not let him have. A machine that rides the beam round his universe and shows "
  "what arrives is, at the least, his kind of instrument. The one honest speculation is that he would have wanted to "
  "check the film against the calculation, and that the check passes: the head is lit at 1/sin&sup2;(6&deg;), the "
  "antipodal balls subtend arcsin(sin&thinsp;8&deg; / sin&thinsp;d), and the flight arrives home.</p>")
A("</section>")
# ---- scripts ------------------------------------------------------------------------------------------------------
A("<section id='scripts2'><h2>The scripts</h2><p class='lede'>numpy only; ffmpeg for the encodes; the caption font is <code>hawkcolor.py</code> from the black-hole page, which sits beside them.</p>")
for name, desc in HYP_SOURCES:
    A(source_block(name, desc))
A("<h3>Running them</h3><pre>"
  "python glome.py path                     # the flight circle and its clearance from the balls\n"
  "python glome.py still one.png 0          # one frame, a few seconds\n"
  "python glome.py film flight.mp4 480      # the circuit: 480 frames at 2.4 s each on one CPU, then the encode\n"
  "python nball.py nball.png                # the chart</pre>")
A("</section>")
# ---- colophon -----------------------------------------------------------------------------------------------------
A("<section id='colophon2'><h2>Colophon</h2>")
A("<p>The 3-sphere is the unit sphere in four coordinates; distances are angles, so a ball's size is an angle and a "
  "journey round the universe is 2&pi;. What was checked: the 600-cell comes out as 120 distinct unit vectors with an "
  "edge of exactly 36 degrees; the flight circle clears every ball by 17.27 degrees against a ball-plus-head of 11; "
  "every ray on every frame terminates, asserted, since a ray that escaped would mean the universe had a hole in it; "
  "the first frame's nearest hit is 19.9 degrees and its farthest 356.1, which is the back of the head. What is not "
  "claimed: anything about the real universe beyond the measured bounds quoted above, or anything about how Einstein "
  "would have felt.</p>")
A("<p>Written, rendered and packed in a single morning in September 2026, in a working session between the project's "
  "author and Claude, as a tangent from the black holes and from the video-interpolation project both have nothing to "
  "do with. The author's own construction, two bowls glued at the rim, was the right one; it needed one more rung and "
  "a lamp.</p>")
A("</section></main>")
A("<footer><a href='index.html'>Black holes, rendered</a> &middot; the 3-sphere &middot; numpy, ffmpeg, one CPU</footer></body></html>")
(SITE / "hypersphere.html").write_text("\n".join(page), encoding="utf-8")
total = sum(p.stat().st_size for p in SITE.rglob("*") if p.is_file())
print(f"site: {SITE} ({total / 1e6:.0f} MB, {sum(1 for p in SITE.rglob('*') if p.is_file())} files)")

zp = HD / "blackhole-site.zip"
with zipfile.ZipFile(zp, "w") as z:
    for p in sorted(SITE.rglob("*")):
        if p.is_file():
            comp = zipfile.ZIP_STORED if p.suffix in (".mp4", ".png", ".jpg") else zipfile.ZIP_DEFLATED
            z.write(p, f"blackhole-site/{p.relative_to(SITE).as_posix()}", compress_type=comp)
print(f"zip: {zp} ({zp.stat().st_size / 1e6:.0f} MB)")
