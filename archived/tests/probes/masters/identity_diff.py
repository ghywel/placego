"""identity.sh's comparison: two rgb48le raws (the engine's export and masters.py's) of the same scene.
    identity_diff.py <outdir> <scene> <W> <H>
Prints the largest absolute difference in 16-bit levels and the count of differing samples, for the
source and the truth."""
import pathlib
import sys

import numpy as np

out, sc, W, H = pathlib.Path(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4])

def load(p):
    return np.frombuffer(p.read_bytes(), dtype="<u2").reshape(-1, H, W, 3)[:, :, :, 0].astype(np.int32)

res = []
for what in ("src", "truth"):
    a = load(out / (sc + ".eng." + what)); b = load(out / (sc + ".py." + what))
    if a.shape != b.shape:
        res.append("%s SHAPE %s vs %s" % (what, a.shape, b.shape)); continue
    d = np.abs(a - b)
    res.append("%s: %d frames, max %d level(s), %d of %d samples differ" % (what, a.shape[0], d.max(), int((d > 0).sum()), d.size))
print("%-20s %s | %s" % (sc, res[0], res[1]))
