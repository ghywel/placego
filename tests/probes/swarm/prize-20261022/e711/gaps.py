# Coverage completion. Parts cover [0,c0) and [h,h+c1) (h = L/2). Reflection rho(m) = L-F+1-m (verified) maps worst
# starts to worst starts, so if c0+c1 > h the union of the parts and their reflections misses only (h-F, h) and
# (L-F, L) for any F <= 200. Sweep those windows (and 200 more on each side) exactly.
import subprocess, sys, math
from functools import reduce
n = int(sys.argv[1]); c0 = int(sys.argv[2]); c1 = int(sys.argv[3])
L = reduce(lambda a, b: a * b // math.gcd(a, b), range(1, n + 1), 1); h = L // 2
assert L % 2 == 0 and c0 + c1 > h + 400, "coverage condition fails"
for m0 in (h - 400, L - 400):
    out = subprocess.run(["./e711_sweep", str(n), str(m0), "800" if m0 == h - 400 else "400"], capture_output=True, text=True).stdout
    print("gap sweep from", m0, ":", out.split("\n")[0][:120])
