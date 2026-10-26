"""antilatch_check.py: the period-one latch beside an alternating wall (Local, 2026-10-26, L997; DEEP-QUESTIONS GC1921 pull).

Standard orientation, x(t+1,i) = x(t,i-1) XOR (x(t,i) OR x(t,i+1)). Wherever a column reads white at t and black at t+1,
its right neighbour y and next neighbour z satisfy y(t+2) = NOR(y(t), z(t), z(t+1)) (hand algebra). With the column
alternating on [t, t+3], its left neighbour white at t forces it black at t+2: the "00" half of the kit's
free_bits_no00_no11111 for the coupled period-two problem.

Prediction (written before the run): zero violations of either statement on random finite rows.
Counterfactual: any violation means an orientation or phase slip in the hand derivation.
Record searched: "anti-latch" 0, "y(t+2)" 0, "right neighbour.{0,40}NOR" 0, "forbids 00" 1 (CL637 section 5, the kit's
free_bits_no00_no11111), "Garden of Eden" 3 (no record use; full-line finite injectivity is G121).

Outcome (2026-10-26 19:40 GMT, M5, about 30 s): identity checked 1,973,892 times, 0 violations; no-00 consequence
checked 511,928 times, 0 violations. Prediction held. Elementary algebra; a guard on orientation, not a new theorem.
Run: python3 -I tests/probes/wolfram/antilatch_check.py
"""
import random
def step(row):
    n = len(row)
    return [ (row[i-1] if i > 0 else 0) ^ (row[i] | (row[i+1] if i+1 < n else 0)) for i in range(n)]
random.seed(1997)
N, T = 401, 120
viol_nor = viol_no00 = checked_nor = checked_no00 = 0
for trial in range(300):
    row = [0]*N
    for i in range(150, 251): row[i] = random.randint(0, 1)
    hist = [row]
    for t in range(T): hist.append(step(hist[-1]))
    for t in range(T-3):
        a, b, c, d = hist[t], hist[t+1], hist[t+2], hist[t+3]
        for i in range(2, N-3):
            if a[i] == 0 and b[i] == 1:
                checked_nor += 1
                if c[i+1] != 1 - (a[i+1] | a[i+2] | b[i+2]): viol_nor += 1
                if c[i] == 0 and d[i] == 1:
                    checked_no00 += 1
                    if a[i-1] == 0 and c[i-1] != 1: viol_no00 += 1
print("anti-latch identity checked", checked_nor, "violations", viol_nor)
print("no-00 under 4-step alternation checked", checked_no00, "violations", viol_no00)
