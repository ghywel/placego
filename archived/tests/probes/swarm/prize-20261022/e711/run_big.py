# Full-period sweeps for n = 19..24, sequential, one core; each invocation time-limited (<= 330 s).
import subprocess, math, time
from functools import reduce
def lcm(a, b): return a * b // math.gcd(a, b)
for n in range(19, 25):
    L = reduce(lcm, range(1, n + 1), 1)
    parts = 1 if L < 10**9 else 2
    step = (L + parts - 1) // parts
    for p in range(parts):
        m0 = p * step; cnt = min(step, L - m0)
        out = subprocess.run(["nice", "-n", "10", "./e711_sweep", str(n), str(m0), str(cnt), "330"],
                             capture_output=True, text=True).stdout
        print("L", L, "part", p, out.strip().replace("\n", " | "), flush=True)
