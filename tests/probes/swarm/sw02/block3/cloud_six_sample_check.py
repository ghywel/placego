# Empirical check of the six-sample label theorem (Cloud, CL755), independent of the window code: random right halves beside
# the alternating centre (centre black at even ticks), evolved exactly; wherever column 1 is black at T-26, T-12, T+2, T+6 and
# white at T-2, T+20 (T odd), the column-8 word over ticks T..T+13 (low bit first) must be 4520.
import numpy as np, sys
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
N_HIST, WIDTH, TICKS = 4000, 1200, 700          # width 1200 cells keeps cells 1..~500 exact through 700 ticks
hits = 0; bad = 0; labels = {}
for h in range(N_HIST):
    row = rng.integers(0, 2, WIDTH, dtype=np.uint8)
    col1 = np.zeros(TICKS + 1, dtype=np.uint8); col8 = np.zeros(TICKS + 1, dtype=np.uint8)
    col1[1] = row[0]; col8[1] = row[7]
    cur = row
    for t in range(1, TICKS):
        c = 1 if (t % 2 == 0) else 0                 # centre at tick t: black at even ticks
        left = np.empty_like(cur); left[0] = c; left[1:] = cur[:-1]
        right = np.empty_like(cur); right[:-1] = cur[1:]; right[-1] = 0
        cur = left ^ (cur | right)
        col1[t + 1] = cur[0]; col8[t + 1] = cur[7]
    for T in range(29, TICKS - 21, 2):           # T odd, and the row at tick T-28 >= 1 exists (the free-row premise of the DAG arc)
        if col1[T-26] and col1[T-12] and col1[T+2] and col1[T+6] and not col1[T-2] and not col1[T+20]:
            lab = int(sum(int(col8[T + k]) << k for k in range(14)))
            hits += 1; labels[lab] = labels.get(lab, 0) + 1
            if lab != 4520: bad += 1
print(f"histories {N_HIST}, width {WIDTH}, ticks {TICKS}: six-sample occurrences {hits}, label counts {labels}, violations {bad}")
print("SIX-SAMPLE CHECK", "PASS" if bad == 0 and hits > 0 else "FAIL")
