"""A diagnostic build of a shader, as fielddiag.py makes them: TRI_DIAG set, one full-scale constant set,
every substitution asserted (column-aligned constants defeat naive seds, and a silent miss would read as
a calibration failure).
    diagvariant.py <in.glsl> <TRI_DIAG> <CONST> <value> <out.glsl>
"""
import pathlib
import re
import sys

src, diag, const, value, out = pathlib.Path(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4], pathlib.Path(sys.argv[5])
txt = src.read_text()
assert txt.count("const int TRI_DIAG = 0;") >= 1, "TRI_DIAG = 0 not found"
txt = txt.replace("const int TRI_DIAG = 0;", "const int TRI_DIAG = %d;" % diag)
assert "const int TRI_DIAG = 0;" not in txt
n_old = len(re.findall(r"^const float %s\s*= 2\.0;" % const, txt, re.M))
assert n_old >= 1, "%s not found at 2.0" % const
txt = re.sub(r"^const float %s(\s*)= 2\.0;" % const, lambda m: "const float %s%s= %s;" % (const, m.group(1), value), txt, flags=re.M)
n_new = len(re.findall(r"^const float %s\s*= %s;" % (const, re.escape(value)), txt, re.M))
assert n_new == n_old, "%s substitution missed (%d of %d)" % (const, n_new, n_old)
out.write_text(txt)
print("%s: TRI_DIAG %d, %s = %s (%d site%s) -> %s" % (src.name, diag, const, value, n_new, "" if n_new == 1 else "s", out))
