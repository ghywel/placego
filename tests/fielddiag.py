"""The FIELD ACCEPTANCE, done through the instrument it was calibrated on.

The reading tail's machine modes (read_view 4/5/6) are NOT that instrument:
they run at 1/8 resolution (every tail pass is HOOKED.w/8) and are pooled for
display, which costs about a third of the peak amplitude on a textured
oscillation. The calibrated instrument is the PICTURE path's own diagnostic —
TRI_DIAG with its full scale, at full resolution — which is what gen.sh's sed
builds and what fieldaccept.sh always measured. With read_view 0 the whole
reading tail is skipped, so a TRI_DIAG build renders exactly that.

    python3 fielddiag.py [--legacy]

--legacy runs the same thing through the pre-2026-09-08 fixed window, so the
window rule can be A/B'd on one instrument with everything else held.
"""
import math, os, pathlib, re, subprocess, sys

TESTS = pathlib.Path(__file__).resolve().parent
REPO = TESTS.parent.parent                      # .../nframe
SRC = REPO / "scripts/shaders/quaddirectional-interpolation.glsl"
GEN = TESTS / "gen_metal.py"
QUAD = REPO / "scripts/metal-demo/.build/release/QuadDemo"
# Working root: big scratch never goes on the system disk (the raws are
# 130-330 MB apiece). Override with FIELDDIAG_OUT.
W = pathlib.Path(os.environ.get(
    "FIELDDIAG_OUT",
    str(REPO.parent / "np-scratch/fielddiag")))
G = W / "graphs"
G.mkdir(parents=True, exist_ok=True)
ENV = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
LEGACY = "--legacy" in sys.argv

base = SRC.read_text()


def build(name, diag, const, value):
    """gen.sh's diag recipe, every substitution asserted (column-aligned shader
    constants defeat naive seds, and a silent miss reads as a calibration
    failure rather than as a typo)."""
    out = G / name
    if (out / "graph.json").exists():
        print("  graph %s: cached" % name); return out
    txt = base.replace("const int TRI_DIAG = 0;", "const int TRI_DIAG = %d;" % diag)
    assert txt.count("const int TRI_DIAG = %d;" % diag) == 1, "TRI_DIAG sed missed"
    old = re.search(r"^const float %s\s*= 2\.0;" % const, txt, re.M)
    assert old, "%s not found at 2.0" % const
    txt = re.sub(r"^const float %s(\s*)= 2\.0;" % const,
                 lambda m: "const float %s%s= %s;" % (const, m.group(1), value), txt, flags=re.M)
    assert ("= %s;" % value) in txt, "%s sed missed" % const
    p = W / (name + ".glsl"); p.write_text(txt)
    r = subprocess.run([sys.executable, str(GEN), str(p), str(out), "--compile"],
                       capture_output=True, text=True, env=ENV)
    line = (r.stdout.strip().splitlines() or ["(none)"])[-1]
    print("  graph %s (TRI_DIAG %d, %s %s): %s" % (name, diag, const, value, line))
    if r.returncode != 0:
        print(r.stdout[-1200:], r.stderr[-1200:]); sys.exit(1)
    return out


def scene(case, fps):
    r = subprocess.run(["bash", "-c",
                        '. "%s/scenes.sh"; scene %s %d' % (TESTS, case, fps)],
                       capture_output=True, text=True, env=ENV)
    return r.stdout.strip()


def render(graph, case, out):
    src = W / "src.raw"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", scene(case, 24),
                    "-pix_fmt", "rgb48le", "-f", "rawvideo", str(src)], env=ENV, check=True)
    cmd = [str(QUAD), "--graph", str(graph), "--param", "read_view=0",
           "--input", str(src), "--export", str(W / out),
           "--out-fps", "24", "--size", "1280x720"]
    if LEGACY:
        cmd.insert(3, "--legacy-window")
    subprocess.run(cmd, env=ENV, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def check(case, rawname, frame, fs, field="accel", centre=None):
    env = dict(ENV, SRC_FPS="24", OUT_FPS="24", FIELD=field,
               PYTHONPATH=ENV.get("PYTHONPATH", ""))
    if centre is not None:
        env["JERK_CENTRE"] = str(centre)
    r = subprocess.run([sys.executable, str(TESTS / "accelcheck.py"), case,
                        rawname, str(frame), str(fs)],
                       capture_output=True, text=True, env=env, cwd=str(W))
    tru = mea = pct = "?"
    for line in r.stdout.splitlines():
        if line.startswith("true"):        tru = line.split()[2]
        if line.startswith("measured a_x"): mea = line.split()[2]
        if line.startswith("error where"):
            m = re.search(r"\(([-\d.]+)% of true\)", line)
            pct = m.group(1) if m else line.split()[4]
    return tru, mea, pct


REF = {("A4_accel_tex_a033", "accel"): 6.6, ("A5_accel_tex_a067", "accel"): 2.5,
       ("A6_accel_tex_a133", "accel"): 2.4, ("A7_accel_tex_a167", "accel"): 1.8,
       ("O6_osc_tex_gentle", "accel"): 0.7, ("O5_osc_textured", "accel"): 5.6,
       ("O5_osc_textured", "jerk"): 3.6}

print("window: %s   (JERK_CENTRE left at accelcheck's default -0.5)"
      % ("LEGACY [i-1..i+2]" if LEGACY else "the patch's rule"))
g_a4 = build("acc_fs4", 2, "ACCEL_DIAG_FS", "4.0")
g_a16 = build("acc_fs16", 2, "ACCEL_DIAG_FS", "16.0")
g_j8 = build("jerk_fs8", 5, "JERK_DIAG_FS", "8.0")
g_j2 = build("jerk_fs2", 5, "JERK_DIAG_FS", "2.0")

tag = "leg" if LEGACY else "pat"
JOBS = [("A4_accel_tex_a033", g_a4, 9, 4.0, "accel"),
        ("A5_accel_tex_a067", g_a4, 12, 4.0, "accel"),
        ("A6_accel_tex_a133", g_a4, 12, 4.0, "accel"),
        ("A7_accel_tex_a167", g_a4, 12, 4.0, "accel"),
        ("O6_osc_tex_gentle", g_a4, 4, 4.0, "accel"),
        ("O5_osc_textured", g_a16, 10, 16.0, "accel"),
        ("O5_osc_textured", g_j8, 10, 8.0, "jerk"),
        ("A6_accel_tex_a133", g_j2, 9, 2.0, "jerk"),
        ("A6_accel_tex_a133", g_j2, 12, 2.0, "jerk")]

print()
print("%-22s %-6s %5s %9s %9s %9s %9s" %
      ("case", "field", "fr", "true", "measured", "err %", "ffmpeg %"))
for case, g, fr, fs, field in JOBS:
    name = "%s_%s_%s_%.0f.raw" % (tag, case, field, fs)
    if not (W / name).exists():
        render(g, case, name)
    tru, mea, pct = check(case, name, fr, fs, field)
    ref = REF.get((case, field))
    print("%-22s %-6s %5d %9s %9s %9s %9s" %
          (case, field, fr, tru, mea, pct, ("%.1f" % ref) if ref else "  null"))
for f in W.glob("._*"):
    f.unlink()
