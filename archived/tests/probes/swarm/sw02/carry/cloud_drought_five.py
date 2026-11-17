# Carry check (Cloud, CL763): column 1 beside the alternating centre has a black cell in every five consecutive samples.
# Sample s reads cell 1 at odd tick 2s+1; five consecutive samples span 8 ticks, so they depend on cells 1..9 of the first row.
# Exhaustive over all 2^9 first rows, at both possible phases of the centre for safety; exact Rule 30 evolution with the cone shrinking.
def run(first_centre):
    worst = 0; bad = []
    for r in range(1 << 9):
        cells = [(r >> i) & 1 for i in range(9)]; c = first_centre; u = [cells[0]]
        for t in range(8):
            cells = [(c if i == 0 else cells[i-1]) ^ (cells[i] | cells[i+1]) for i in range(len(cells) - 1)]
            c ^= 1
            if t % 2 == 1: u.append(cells[0])
        if not any(u): bad.append(r)
    return bad
for fc, name in ((0, "samples at ticks where the centre is white (the kit's odd times)"), (1, "samples at ticks where the centre is black")):
    b = run(fc); print(f"{name}: rows of cells 1..9 with five white samples in a row: {len(b)} of 512 {b[:8]}")
