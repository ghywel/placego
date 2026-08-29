#!/usr/bin/env python3
"""Turn a shader into a flow visualiser by replacing only its FINAL hook().

Every pass upstream is untouched, so what this renders is exactly the flow the
given shader computes -- not a re-implementation that could drift from it.
Encoding: f.x -> R, f.y -> G as 0.5 + f*0.05, i.e. +-10 px full scale.
"""
import sys, pathlib

src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
text = src.read_text()
i = text.rfind("vec4 hook() {")
if i < 0:
    sys.exit(f"no final hook() in {src}")
dst.write_text(text[:i] + """vec4 hook() {
    vec2 f = FLOW_H_AB_tex(HOOKED_pos).xy * 2.0;
    return vec4(0.5 + f.x * 0.05, 0.5 + f.y * 0.05, 0.5, 1.0);
}
""")
print(f"  {dst.name}")
