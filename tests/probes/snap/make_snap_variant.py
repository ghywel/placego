"""A scratch variant of the quint that reports its SNAP row as a machine field (2026-09-08, the owner's
"jerk, snap, crackle, pop" question for the Metal demo): TRI_DIAG 10 = 0.5 + snap / (2 SNAP_DIAG_FS) in R and G,
the same encoding as the acceleration and jerk machine modes. The quint already solves the quartic's fourth
coefficient (sx.w, sy.w) and uses it only as an alarm (SNAP_MAX_PX); this hoists it out of the block and paints it.
Not a repo change: the measurement decides whether a snap reading is worth building.

    make_snap_variant.py <quint.glsl> <out.glsl> [SNAP_DIAG_FS=4.0]
"""
import pathlib
import sys

src = pathlib.Path(sys.argv[1]); dst = pathlib.Path(sys.argv[2])
fs = float(sys.argv[3]) if len(sys.argv) > 3 else 4.0
t = src.read_text(encoding="utf-8")

hoist_at = "    vec2 accel = accel_c, jerk = jerk_c;\n"
assert t.count(hoist_at) == 2, t.count(hoist_at)
t = t.replace(hoist_at, "    vec2 snap_row = vec2(0.0);\n" + hoist_at)

after = "            float snap_px = length(vec2(sx.w, sy.w) / HOOKED_pt);\n"
assert t.count(after) == 2, t.count(after)
t = t.replace(after, after + "            snap_row = vec2(sx.w, sy.w);\n")

diag6 = "        if (TRI_DIAG == 6)\n"
assert t.count(diag6) == 2, t.count(diag6)
t = t.replace(diag6, "        if (TRI_DIAG == 10)\n            return vec4(0.5 + (snap_row / HOOKED_pt) * (0.5 / SNAP_DIAG_FS), 0.5, 1.0);\n" + diag6)

jfs = "const float JERK_DIAG_FS  = 2.0;\n"
assert t.count(jfs) == 2, t.count(jfs)
t = t.replace(jfs, jfs + f"const float SNAP_DIAG_FS  = {fs};\n")

main_diag = "const int TRI_DIAG = 0;\n"
assert t.count(main_diag) == 1, t.count(main_diag)
t = t.replace(main_diag, "const int TRI_DIAG = 10;\n")

dst.write_text(t, encoding="utf-8", newline="\n")
print(f"{dst}: snap machine mode at FS {fs}, main pass TRI_DIAG 10; read_view default untouched (0)")
