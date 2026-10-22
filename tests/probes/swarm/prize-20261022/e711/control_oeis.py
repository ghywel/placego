# Control 1: the sweep must reproduce OEIS A390246 = f(n,n), n=1..66 (data copied from the OEIS page).
import subprocess
A = [2,3,4,6,6,9,9,11,13,15,15,17,16,19,20,25,24,27,26,29,30,31,30,33,36,38,40,43,42,46,45,50,49,48,50,55,54,55,
     58,60,59,61,60,62,66,67,66,73,72,77,76,79,78,82,82,89,88,87,86,91,90,89,98,105,104,103]
bad = []
for n in range(1, 65):  # bitmask supports n <= 64
    out = subprocess.run(["./e711_sweep", str(n), str(n), "1"], capture_output=True, text=True).stdout
    f = int(out.split()[out.split().index("best") + 1])
    if f != A[n-1]: bad.append((n, f, A[n-1]))
print("mismatches:", bad if bad else "none", "(n=1..64)")
