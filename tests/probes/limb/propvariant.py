#!/usr/bin/env python3
"""A PROTOTYPE, patched onto a generated file (not the generator): the 1/8 level's propagation made motion-edge
aware, for the limb (NFRAME-LIMITS.md "The field on real bodies"; limblevels.py located the loss).

The shipped propagation (three passes, AB and B->A fused) replaces each texel's flow with a CONTRAST-weighted mean
of its own (weight 8 c^2) and its 5 x 5 neighbours' (weight = their contrast / distance). A textured still wall is
all high-contrast zeros, so a small moving object's flow is averaged toward zero (the limb: 0.67 at E_raw -> 0.29
after propagation on a textured wall; 0.84 -> 0.78 on a flat one, whose zeros carry no weight).

The change: each neighbour's weight is also multiplied by its flow's AGREEMENT with the texel's own,
1 / (1 + (|f_n - f_own| / TAU)^2), blended in by the texel's own confidence c_own (so a flat texel, whose own flow
means nothing, still fills from its neighbours exactly as before -- the aperture fill the propagation is for).
TAU in the level's texels (1/8 res: 1 texel = 8 px).

    propvariant.py <in.glsl> <out.glsl> [TAU]"""
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
tau = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5
text = open(src, encoding="utf-8").read()
# the neighbour sums take two forms: a sampled texture, FLOW_E_*_tex(uv + o).xy, and (the fused B->A twins of passes
# 2 and 3) a storage image, imageLoad(FLOW_E_BA_PROP_STn, ...(uv + o)...).xy -- both captured whole
pat = re.compile(r"(?P<ind>[ \t]+)acc \+= w \* (?P<expr>(?:FLOW_E_\w+_tex|imageLoad)\(.*?\)\.xy);\n")
n = 0


def sub(m):
    global n
    n += 1
    ind, expr = m.group("ind"), m.group("expr")
    assert "uv + o" in expr, expr
    return (f"{ind}vec2 fn = {expr};\n"
            f"{ind}float dfl = length(fn - own) / PROP_TAU;\n"
            f"{ind}w *= mix(1.0, 1.0 / (1.0 + dfl * dfl), c_own);\n"
            f"{ind}acc += w * fn;\n")


out = pat.sub(sub, text)
k = out.count("const float PROP_SELF_WEIGHT = 8.0;\n")
out = out.replace("const float PROP_SELF_WEIGHT = 8.0;\n", f"const float PROP_SELF_WEIGHT = 8.0;\nconst float PROP_TAU = {tau};\n")
print(f"substituted {n} neighbour sums; PROP_TAU declared in {k} passes")
assert n == 6 and k == 3, (n, k)
# the storage-image pass variants: the B->A halves write through imageStore; their 'own' must exist in scope
assert out.count("float dfl = length(fn - own)") == 6
open(dst, "w", encoding="utf-8").write(out)
