"""chink.py: a hole in a diagonal wall of the seed's left side (CL748, the owner's question). The seed on K = 165,750
wheels is evolved to tick T0; the cell on wheel W is flipped (the chink); then (a) the chinked wheel is compared with the
original for sixteen ticks (the heal); (b) the chinked configuration is evolved to a multiple of 32 past T0 + 334,181
and its strip and phase are found among ROWSDIR/*.bin (all strips, all 32 phases), allowing for a wall frame moved in
by the number of white wheels at the bottom (a chink on wheel 0); (c) the error process from T0 against that strip
gives the settling tick through the last wheel, and the edge's position every 1,000 ticks. With PNG set, pictures for
one chink in the standard frame: the original, the chinked pattern and their difference over the first LOCAL ticks,
and the difference at scale over SCALE ticks (downsampled), with the error edge drawn.
Usage: python3 chink.py ROWSDIR W T0 [PNGPREFIX] [LOCAL=600] [SCALE=40000]"""
import sys, os, time
import numpy as np
ROWS = sys.argv[1]; W = int(sys.argv[2]); T0 = int(sys.argv[3]); PNG = sys.argv[4] if len(sys.argv) > 4 else None
LOCAL = int(sys.argv[5]) if len(sys.argv) > 5 else 600; SCALE = int(sys.argv[6]) if len(sys.argv) > 6 else 40000
K = 165750; MASK = (1 << K) - 1; P = 32
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
strips = {}
for f in sorted(os.listdir(ROWS)):
    if f.endswith('.bin'):
        r = int.from_bytes(open(f"{ROWS}/{f}", 'rb').read(), 'little') & MASK; c = [r]
        for _ in range(P - 1): c.append(step(c[-1]))
        strips[f[:-4]] = c
# the seed to T0, then the chink
x = 1
for t in range(T0): x = step(x)
orig = x; chk = x ^ (1 << W)
# (a) the heal: the chinked wheel against the original for sixteen ticks, and the wheel above
o, c = orig, chk; heal = None; above = []
for k in range(1, 17):
    o = step(o); c = step(c)
    if heal is None and ((o >> W) & 1) == ((c >> W) & 1): heal = k
    above.append(((o >> (W + 1)) & 1, (c >> (W + 1)) & 1))
first_diff_above = next((k + 1 for k, (a, b) in enumerate(above) if a != b), None)
off = lowbit(chk)                                   # the configuration's wall frame begins at its lowest black wheel
print(f"chink on wheel {W} at tick {T0}: healed after {heal} tick(s) (None = not within 16); wheel {W+1} first differs at +{first_diff_above}; wall frame offset {off}")
# (b) the strip and phase
T1 = T0 + 334181; T1 += (-T1) % P
y = chk
for t in range(T0, T1): y = step(y)
found = None
for name, cyc in strips.items():
    for ph in range(P):
        if ((y >> off) & ((1 << (K - off)) - 1)) == (cyc[ph] & ((1 << (K - off)) - 1)): found = (name, ph)
print(f"  settles on {found[0] if found else None} at strip phase {found[1] if found else None} by tick {T1} (the seed: A0 at phase 0)")
if not found: sys.exit(0)
name, ph = found; cyc = strips[name]
# (c) the error process from T0 against that strip, in the configuration's own frame
KK = K - off; MM = (1 << KK) - 1
x = chk; t = T0; m_prev = -1; marks = []
while True:
    C = cyc[(t - T0 + ph - ((T1 - T0) % P)) % P]       # the strip's row at tick t: at tick T1 the configuration shows cyc[ph]
    e = ((x >> off) ^ C) & MM; m = lowbit(e) if e else KK
    if m >= KK: break
    if (t - T0) % 1000 == 0: marks.append((t - T0, m))
    x = step(x); t += 1
    if t - T0 > 400000: print("  no settling within 400,000 ticks"); break
print(f"  settled through wheel {KK-1} at tick {t} = T0 + {t - T0} (the seed's own settling through 165,749: 220,275)")
print("  edge every 1,000 ticks after T0 (ticks, wheel): " + ", ".join(f"{a}:{b}" for a, b in marks[:12]) + " …")
if PNG:
    from PIL import Image
    # standard frame: cell p at tick t is wheel p + t (lo = 0): window of cells [-T0-LOCAL-4, -T0+LOCAL*2]
    def render(ticks, down, fname, mode):
        lo_c = -(T0 + ticks) - 4; hi_c = -T0 + 2 * ticks + W
        ncell = hi_c - lo_c; wdt = ncell // down; hgt = ticks // down
        img = np.zeros((hgt, wdt), dtype=np.uint8)
        o, c = orig, chk
        for t in range(ticks):
            if t % down == 0:
                row = np.zeros(wdt, dtype=np.uint8)
                tt = T0 + t
                for i in range(wdt):
                    p = lo_c + i * down; j = p + tt
                    if j < 0 or j >= K: continue
                    bo = (o >> j) & 1; bc = (c >> j) & 1
                    row[i] = (bo if mode == 'orig' else bc if mode == 'chink' else bo ^ bc)
                img[t // down] = row
            o = step(o); c = step(c)
        im = Image.fromarray((255 - img * 255).astype(np.uint8), 'L')
        im.save(fname); print(f"  wrote {os.path.basename(fname)} ({wdt}x{hgt}, {down}x downsampled)")
    render(LOCAL, 1, f"{PNG}_local_orig.png", 'orig'); render(LOCAL, 1, f"{PNG}_local_chink.png", 'chink'); render(LOCAL, 1, f"{PNG}_local_xor.png", 'xor')
    render(SCALE, SCALE // 1000, f"{PNG}_scale_xor.png", 'xor')
