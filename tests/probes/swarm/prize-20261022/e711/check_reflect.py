# Unexpected check: reflection x -> -x maps (m, m+H) onto (-m-H, -m), so the start L-m-F must also be a worst start.
# The sweep code knows nothing of this symmetry.
import subprocess
for n, m, F, L in [(20, 790370, 43, 232792560), (19, 1407302, 40, 232792560), (17, 485749, 34, 12252240),
                   (22, 503104, 49, 232792560), (16, 225, 31, 720720)]:
    mr = L - m - F + 1  # failing window {m+1..m+F-2} reflects to {m2+1..m2+F-2} with m2 = -m-F+1
    out = subprocess.run(["./e711_sweep", str(n), str(mr), "1"], capture_output=True, text=True).stdout.split()
    print("n", n, "m", m, "F", F, "reflected start", mr, "f =", out[out.index("best") + 1])
