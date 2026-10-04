#!/usr/bin/env python3
"""retire_snap.py <shader.glsl> ...: retire the texel-snap experiment (REPAIRS.md lead L2, 2026-10-04).

SNAP_STRENGTH has been 0.0 for the gate's life ("Not yet confirmed either way"). Measured on the Arc, the full ladder in
one sitting, the base at 1.0 against 0.0: mean 39.53 -> 38.54 dB (capped 34.81 -> 34.69), L1_trans_8px -12.4, L6 -4.2,
P2 -4.2, M2 -4.1, M1 -2.9; up on three cases, the most P5 +0.84. As its own comment predicted, it snaps ordinary content,
not only edges. At 0.0 it changes nothing, but its two full-resolution edge-mask passes (EDGE_A, EDGE_B) ran every frame.

Here, in HAND-MAINTAINED files only (generated files are rebuilt from them): the two EDGE passes and their binds go,
warp_sample_a/b read their frame straight (mix(x, y, 0.0) is x, so the output is byte-identical), edge_consistency
goes, and the constant becomes a dated note. Every edit is counted and asserted.

NOT YET RUNNABLE END TO END (2026-10-04): two generators depend on what this removes. gen_variational.py anchors the
coherence gate beside the snap code, and the N-frame generators count the base's passes with the edge masks in them.
Fix those first (REPAIRS.md L2), or rebuild_generated.py fails and installs nothing.
"""
import re, sys, pathlib

NOTE = ("// RETIRED 2026-10-04 (REPAIRS.md L2): the texel snap. Measured at 1.0 against\n"
        "// 0.0 on the full ladder (the Arc, one sitting): mean -0.99 dB, L1_trans_8px\n"
        "// -12.4, up on three cases at most +0.84. At 0.0 it changed nothing but its\n"
        "// two full-resolution edge-mask passes ran every frame; they are gone, and\n"
        "// warp_sample_a/b read their frame straight.\n")


def retire(t):
    blocks = re.split(r"(?m)^(?=//!HOOK\b)", t)
    kept, gone = [], 0
    for b in blocks:
        m = re.search(r"(?m)^//!SAVE (EDGE_A|EDGE_B)$", b)
        if m:
            gone += 1
            continue
        kept.append(b)
    t = "".join(kept)
    assert gone == 2, f"expected the two EDGE passes, found {gone}"
    t, nb = re.subn(r"(?m)^//!BIND EDGE_[AB]\n", "", t)
    assert nb == 2, f"expected two EDGE binds, found {nb}"
    pat = re.compile(r"vec4 warp_sample_(a|b)\(vec2 uv\) \{\n    vec2 snapped_uv = snap_texel\(uv, \w+_size\);\n"
                     r"    float expected = EDGE_[AB]_tex\(uv\)\.r;\n    float snapped_edge = EDGE_[AB]_tex\(snapped_uv\)\.r;\n"
                     r"    float strength = SNAP_STRENGTH \* edge_consistency\(expected, snapped_edge\);\n"
                     r"    return mix\((\w+)_tex\(uv\), \2_tex\(snapped_uv\), strength\);\n\}")
    t, nw = pat.subn(lambda m: f"vec4 warp_sample_{m.group(1)}(vec2 uv) {{\n    return {m.group(2)}_tex(uv);\n}}", t)
    assert nw == 2, f"expected warp_sample_a and _b, rewrote {nw}"
    t, ne = re.subn(r"(?m)^float edge_consistency\(float expected, float snapped\) \{\n    return 1\.0 - abs\(expected - snapped\);\n\}\n\n?", "", t)
    assert ne == 1, f"edge_consistency: {ne}"
    t, ns = re.subn(r"(?m)^const float SNAP_STRENGTH = 0\.0;\n", NOTE, t)
    assert ns == 1, f"SNAP_STRENGTH: {ns}"
    code = "\n".join(ln for ln in t.splitlines() if not ln.lstrip().startswith("//"))
    assert not re.search(r"EDGE_[AB]|SNAP_STRENGTH|edge_consistency", code), "a snap reference survived in code"
    return t


def main():
    for a in sys.argv[1:]:
        p = pathlib.Path(a)
        t = p.read_text(encoding="utf-8")
        assert "GENERATED FILE" not in t[:400], f"{p.name} is generated: rebuild it instead"
        if "//!SAVE EDGE_A" not in t:
            print(f"  {p.name}: no snap"); continue
        p.write_text(retire(t), encoding="utf-8", newline="\n")
        print(f"  {p.name}: retired")


if __name__ == "__main__":
    main()
