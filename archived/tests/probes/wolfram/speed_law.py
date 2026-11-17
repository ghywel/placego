#!/usr/bin/env python3
"""speed_law.py T NALIGN: M2. Lab-frame leftward speed of the mismatch front for an inserted black edge (and a single flip) on
periodic ring backgrounds and on a fair random background; the heal/jump statistics of the diagonal identity; the torus density.
Cloud, Block 19."""
import sys, numpy as np
T, NAL = int(sys.argv[1]), int(sys.argv[2])
rng = np.random.default_rng(20261102)
def step(r):
    n = np.zeros_like(r); n[1:-1] = r[:-2] ^ (r[1:-1] | r[2:]); return n
def step_periodic(r):
    return np.roll(r, 1) ^ (r | np.roll(r, -1))
def ring_orbit(word):
    y = np.array([int(c) for c in word], dtype=np.uint8); N = len(y)
    def cst(s): return s ^ (np.roll(s, 1) | np.roll(s, 2))   # frame rule c on the ring: s_j' = s_j XOR (s_{j-1} OR s_{j-2})
    orb = [y.copy()]; cur = cst(y)
    while not np.array_equal(cur, y): orb.append(cur.copy()); cur = cst(cur)
    return np.array(orb), N
def g16_ring():
    from pysat.solvers import Solver
    N, r = 128, 72; yv = lambda i: (i % N) + 1; cl = []; nv = N
    for n in range(N):
        nv += 1; o = nv; a, b = yv(n-1), yv(n-2); cl += [[-a, o], [-b, o], [a, b, -o]]
        x, z = yv(n-r), yv(n); cl += [[-x, z, o], [-x, -z, -o], [x, -z, o], [x, z, -o]]
    ds = []
    for i in range(N // 2):
        nv += 1; d = nv; a, b = yv(i), yv(i + N // 2); ds.append(d); cl += [[-d, a, b], [-d, -a, -b]]
    cl.append(ds)
    with Solver(name='cadical195', bootstrap_with=cl) as s:
        assert s.solve(); m = s.get_model(); return ''.join('1' if m[i] > 0 else '0' for i in range(N))
BACK = {'G8': '1000', 'classic_7_28': '1000000', 's7_63': '1010000', 's9_57': '100100000', 's12_68': '100100000000', 'G16': g16_ring()}
def run(bg_row, pert_row, T, periodic=False):
    """both rows evolve; returns x_min(t) (leftmost mismatch, absolute index) for t = 0..T."""
    f = step_periodic if periodic else step
    a, b = bg_row.copy(), pert_row.copy(); xm = np.zeros(T+1, dtype=np.int64)
    for t in range(T+1):
        d = np.flatnonzero(a ^ b); xm[t] = d.min() if d.size else -1
        if t < T: a, b = f(a), f(b)
    return xm
def stats(xm, T, x0):
    # current front: lab leftward speed over [T/2, T]; first-arrival front: running minimum of x_min (deepest ever)
    v = -(xm[T] - xm[T//2]) / (T - T//2)
    xmm = np.minimum.accumulate(xm); vmax = -(xmm[T] - xmm[T//2]) / (T - T//2)
    k = xm + np.arange(T+1); dk = np.diff(k)[T//2:]
    assert dk.min() >= 0, "k_min fell"
    heal = dk > 0
    return v, heal.mean(), (dk[heal].mean() if heal.any() else 0.0), np.bincount(dk, minlength=6)[:6], vmax
def lab_row(orb, N, W, offs_x, offs_t):
    """lab row of width W from the ring orbit: the frame row at time offs_t, cell at depth j <-> lab x = -j; tiled."""
    s = orb[offs_t % len(orb)]
    idx = (np.arange(W) - W//2) * -1 + offs_x       # depth of lab index i: j = -(i - W//2) + offs_x
    return s[idx % N].astype(np.uint8)
print(f"T={T}, alignments per background {NAL}; speeds over [T/2, T]; plain arrays, left margin 2T+100 (the boundary wave moves right at light speed), right margin T+60")
WL = 2*T + 100; WR = T + 60; W = WL + WR
for name, word in BACK.items():
    orb, N = ring_orbit(word); q = len(orb); rho = orb.mean()
    res = []
    for a in range(NAL):
        ox, ot = int(rng.integers(N)), int(rng.integers(q))
        bg = lab_row(orb, N, W, ox, ot)
        pert = bg.copy(); c = WL; pert[c] = 1; pert[c+1:] = 0      # edge at index WL (lab x = 0), white to the right
        xm = run(bg, pert, T); res.append(stats(xm, T, c))
    vs = [r[0] for r in res]; vm = [r[4] for r in res]
    print(f"{name}: N={N} q={q} rho={rho:.4f} mean-field 1-2rho={1-2*rho:+.3f}; v_cur by alignment {np.round(vs,4).tolist()}; mean {np.mean(vs):.4f}; v_max by alignment {np.round(vm,4).tolist()}; mean {np.mean(vm):.4f}; "
          f"P(heal) {np.mean([r[1] for r in res]):.4f}; E[jump|heal] {np.mean([r[2] for r in res]):.4f}; jump hist (0..5) {np.sum([r[3] for r in res], axis=0).tolist()}", flush=True)
# uniform background: inserted edge and single flip
for kind in ('edge', 'flip'):
    vs = []; ph = []; ej = []; hist = np.zeros(6, dtype=np.int64); vm = []
    for a in range(NAL):
        bg = rng.integers(0, 2, W).astype(np.uint8); pert = bg.copy(); c = WL
        if kind == 'edge': pert[c] = 1; pert[c+1:] = 0
        else: pert[c] ^= 1
        xm = run(bg, pert, T); v, p, e, h, vx = stats(xm, T, c); vs.append(v); ph.append(p); ej.append(e); hist += h; vm.append(vx)
    print(f"uniform ({kind}): rho=0.5 mean-field 0.000; v_cur by sample {np.round(vs,4).tolist()}; mean {np.mean(vs):.4f} +- {np.std(vs)/np.sqrt(len(vs)):.4f}; v_max mean {np.mean(vm):.4f} +- {np.std(vm)/np.sqrt(len(vm)):.4f}; "
          f"P(heal) {np.mean(ph):.4f}; E[jump|heal] {np.mean(ej):.4f}; jump hist (0..5) {hist.tolist()}", flush=True)
print("SPEED_LAW_DONE")
