# Full-period sweep: F(n) = max over m in [0, lcm(1..n)) of f(n,m), n = 1..18.
import subprocess, math, time
from functools import reduce
def lcm(a, b): return a * b // math.gcd(a, b)
t0 = time.time()
for n in range(1, 19):
    L = reduce(lcm, range(1, n + 1), 1)
    out = subprocess.run(["nice", "-n", "10", "./e711_sweep", str(n), "0", str(L), "300"], capture_output=True, text=True).stdout
    print("L", L, out.strip().replace("\n", " | "), flush=True)
    if time.time() - t0 > 500: print("stopping on time"); break
