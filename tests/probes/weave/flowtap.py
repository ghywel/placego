#!/usr/bin/env python3
"""A FLOW TAP (ENERGY-TRANSFER.md stage 0f): a diagnostic copy of a shader whose machine reading (read_view 4) shows a
chosen flow texture as it stands right after a chosen pass, instead of the final half-level flow.

    flowtap.py <in.glsl> <out.glsl> <DESC substring of the pass> <texture, e.g. FLOW_Q_AB> <px per texel: 4 at Q, 8 at E, 2 at H> [occurrence=last]

- A tap pass is inserted after the located pass (before the next //!HOOK). It copies the texture into DIAG_TAP at the
  texture's own level.
- The reading tail's READ_FIELD pass is re-pointed from FLOW_H_AB (x 2) to DIAG_TAP (x px per texel).
- read_view is set to 4 (the raw machine velocity, 0.5 + px / 64).
Everything else is byte-for-byte the input, and the script asserts each substitution happened exactly once.
Diagnostic only: never a shipped file.
"""
import re
import sys

src, out, desc, tex, pxt = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], float(sys.argv[5])
occ = sys.argv[6] if len(sys.argv) > 6 else "last"
t = open(src).read()
div = {4.0: "4", 8.0: "8", 2.0: "2", 16.0: "16"}[pxt]

hits = [m.start() for m in re.finditer(re.escape("//!DESC " + desc), t)]
assert hits, f"no pass with //!DESC {desc!r}"
at = hits[-1] if occ == "last" else hits[int(occ)]
nxt = t.index("\n//!HOOK", at) + 1                                  # the start of the next pass
tap = (f"//!HOOK FRAME_MIX\n//!BIND {tex}\n//!SAVE DIAG_TAP\n//!WIDTH HOOKED.w {div} /\n//!HEIGHT HOOKED.h {div} /\n"
       f"//!COMPONENTS 2\n//!DESC [diag] tap {tex} after: {desc}\n"
       f"vec4 hook() {{ return vec4({tex}_tex({tex}_pos).xy, 0.0, 0.0); }}\n\n")
t = t[:nxt] + tap + t[nxt:]

a = "//!BIND HOOKED\n//!BIND FLOW_H_AB\n//!SAVE READ_FIELD\n"
assert t.count(a) == 1, "the reading tail's READ_FIELD binding"
t = t.replace(a, "//!BIND HOOKED\n//!BIND DIAG_TAP\n//!SAVE READ_FIELD\n")
b = "    return vec4(FLOW_H_AB_tex(HOOKED_pos).xy * 2.0, 0.0, 1.0);\n"
assert t.count(b) == 1, "the reading tail's READ_FIELD body"
t = t.replace(b, f"    return vec4(DIAG_TAP_tex(HOOKED_pos).xy * {pxt:.1f}, 0.0, 1.0);\n")
t, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t)
assert n == 1, "read_view's default"
open(out, "w").write(t)
print(f"{out}: tap of {tex} after {desc!r} (occurrence {occ} of {len(hits)}), {pxt:g} px per texel")
