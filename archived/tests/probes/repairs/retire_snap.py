#!/usr/bin/env python3
"""retire_snap.py <shader.glsl> ...: retire the texel-snap experiment (REPAIRS.md lead L2, 2026-10-04).

SNAP_STRENGTH has been 0.0 for the gate's life ("Not yet confirmed either way"). Measured on the Arc, the full ladder in
one sitting, the base at 1.0 against 0.0: mean 39.53 -> 38.54 dB (capped 34.81 -> 34.69), L1_trans_8px -12.4, L6 -4.2,
P2 -4.2, M2 -4.1, M1 -2.9; up on three cases, the most P5 +0.84. As its own comment predicted, it snaps ordinary content,
not only edges. At 0.0 it changes nothing, but its two full-resolution edge-mask passes (EDGE_A, EDGE_B) ran every frame.

Here, in HAND-MAINTAINED files only (generated files are rebuilt from them): the two EDGE passes, their banner and their
binds go, warp_sample_a/b read their frame straight (mix(x, y, 0.0) is x, so the output is byte-identical), and
edge_consistency, the explanation of the snap and the constant become a dated note. Every edit is counted and asserted.

Then rebuild_generated.py --install: the generators take the base with or without the edge masks (fixed 2026-10-04;
before that gen_variational.py anchored its coherence gate on the EDGE binds and the N-frame generators counted 24
base passes with the masks in them).
"""
import re, sys, pathlib

NOTE = ("// RETIRED 2026-10-04 (REPAIRS.md L2): the texel snap and its edge-consistency\n"
        "// gate. Its strength sat at 0.0 for the gate's whole life ('Not yet confirmed\n"
        "// either way'). Measured at 1.0 against 0.0 on the full ladder (the Arc, one\n"
        "// sitting): mean -0.99 dB, L1_trans_8px -12.4, up on three cases at most +0.84:\n"
        "// as the old note here predicted, it snapped ordinary content, not only edges.\n"
        "// At 0.0 it changed nothing, but its two full-resolution edge-mask passes\n"
        "// (EDGE_A/EDGE_B) ran every frame. They are gone, and warp_sample_a/b read\n"
        "// their frame straight. snap_texel() above stays: it has another caller.\n")


def retire(t):
    blocks = re.split(r"(?m)^(?=//!HOOK\b)", t)
    kept, gone = [], 0
    for b in blocks:
        if re.search(r"(?m)^//!SAVE (EDGE_A|EDGE_B)$", b):
            gone += 1
            # a pass's banner rides at the tail of the pass before it: keep the next pass's (the final pass's)
            lines = b.split("\n")
            i = len(lines)
            while i > 0 and (lines[i - 1].startswith("//") or lines[i - 1] == ""):
                i -= 1
            while i < len(lines) and lines[i] == "":
                i += 1
            kept.append("\n".join(lines[i:]))
            continue
        kept.append(b)
    t = "".join(kept)
    assert gone == 2, f"expected the two EDGE passes, found {gone}"
    # the edge passes' own banner rode at the tail of the pass before them
    t, nh = re.subn(r"\n// -+\n// Edge-consistency reference \(.*?\n// -+\n", "\n", t, flags=re.S)
    assert nh == 1, f"edge-pass banner: {nh}"
    t, nb = re.subn(r"(?m)^//!BIND EDGE_[AB]\n", "", t)
    assert nb == 2, f"expected two EDGE binds, found {nb}"
    assert re.search(r"(?m)^// Final pass: ", t), "the final pass lost its banner"
    pat = re.compile(r"vec4 warp_sample_(a|b)\(vec2 uv\) \{\n    vec2 snapped_uv = snap_texel\(uv, \w+_size\);\n"
                     r"    float expected = EDGE_[AB]_tex\(uv\)\.r;\n    float snapped_edge = EDGE_[AB]_tex\(snapped_uv\)\.r;\n"
                     r"    float strength = SNAP_STRENGTH \* edge_consistency\(expected, snapped_edge\);\n"
                     r"    return mix\((\w+)_tex\(uv\), \2_tex\(snapped_uv\), strength\);\n\}")
    t, nw = pat.subn(lambda m: f"vec4 warp_sample_{m.group(1)}(vec2 uv) {{\n    return {m.group(2)}_tex(uv);\n}}", t)
    assert nw == 2, f"expected warp_sample_a and _b, rewrote {nw}"
    # the snap's explanation, edge_consistency() and the constant become the dated note
    t, ns = re.subn(r"(?ms)^// snap_texel\(\) is a \*discontinuous\*.*?^const float SNAP_STRENGTH = 0\.0;\n", NOTE, t)
    assert ns == 1, f"snap block: {ns}"
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
        out = retire(t)                                   # all asserts pass before anything is written
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(out)
        print(f"  {p.name}: retired")


if __name__ == "__main__":
    main()
