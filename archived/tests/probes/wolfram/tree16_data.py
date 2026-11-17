"""tree16_data.py: Proposition 8's tree realized as rows (CL738, stage 1). On 894,236 wheels: settle the single black cell (the
row returns after 32 ticks), take it at a multiple of 32 ticks as A0 at phase 0; then for each strip, its 32-row cycle and
words, its white wheels with the parity of the farther word (even: a fork, odd: a doubling), and for each fork above the
strip's own creation the sibling row (the child bit complemented), evolved until it returns after 32 ticks and taken at a
multiple of 32; the forced front at phase 0 by the walk; the lag-32 settling tick; digests. One strip per invocation, state in
a scratch directory (not in git; the rows are cited by digest). Predictions P-A1 … P-A3 in CL738.
Usage: python3 tree16_data.py STATEDIR init | step | report    (step: one queue item; loop until "queue empty")."""
import sys, os, json, time, hashlib
import numpy as np
K = 894236; MASK = (1 << K) - 1; P = 32
STATE = sys.argv[1]; CMD = sys.argv[2]
os.makedirs(f"{STATE}/rows", exist_ok=True)
SJ = f"{STATE}/state.json"
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def digest(x): return hashlib.sha256(format(x, 'x').encode()).hexdigest()[:16]
def load(): return json.load(open(SJ))
def save(st): json.dump(st, open(SJ, 'w'), indent=1)
def rowpath(name): return f"{STATE}/rows/{name}.bin"
def load_row(name): return int.from_bytes(open(rowpath(name), 'rb').read(), 'little')
def save_row(name, x): open(rowpath(name), 'wb').write(x.to_bytes((K + 7) // 8, 'little'))
def settle(x, t_max=3_000_000):
    """evolve x until it returns after 32 ticks, then on to a multiple of 32; return (row, first return tick, final tick)."""
    ring = [x]; t = 0; first = None
    while True:
        x = step(x); t += 1; ring.append(x)
        if len(ring) > P + 1: ring.pop(0)
        if first is None and t >= P and x == ring[0]: first = t
        if first is not None and t % P == 0: return x, first, t
        if t > t_max: raise RuntimeError("no return by the horizon")
def cycle_of(x):
    c = [x]
    for _ in range(P): c.append(step(c[-1]))
    assert c[P] == x
    return c[:P]
def words_of(c):
    w = np.zeros(K, dtype=np.int64)
    for r in range(P):
        bits = np.unpackbits(np.frombuffer(c[r].to_bytes((K + 7) // 8, 'little'), dtype=np.uint8), bitorder='little')[:K]
        w += bits.astype(np.int64) << r
    return w
def rot(c, q): return ((c >> q) | (c << (P - q))) & ((1 << P) - 1)
def minperiod(c):
    for q in (1, 2, 4, 8, 16):
        if rot(c, q) == c: return q
    return P
def front_at_end(words):
    """the forced front F(K-1) at phase 0 by the walk: pointer on wheel 1 at tick 1 … (F(0)=0, F(1)=1)."""
    w = words
    j, t = 1, 1                 # wheel 1 is reached at tick 1
    F1 = 1; last = {}
    # walk: pointer at wheel j from tick t; it moves at a black cell of wheel j; arrival at wheel j+1 = F(j+1)
    # the recursion with max(F(j-1),F(j)) = F(j) by monotonicity; a white wheel holds the pointer: F(j+1) = F(j) there
    # we implement the recursion directly (fast enough): F(j+2) = F(j+1) + wait + 1 or F(j+1)
    F = 1; Fp = 0
    for jj in range(1, K - 1):              # computes F(jj+1) from F(jj) (=F) and word of wheel jj
        word = int(w[jj]); m = F
        if word == 0: Fn = m
        else:
            r = 0
            while not (word >> ((m + r) % P)) & 1: r += 1
            Fn = m + r + 1
        Fp, F = F, Fn
    return F                                 # F(K-1)
def edge_cross(name_x, x0, target):
    """evolve x0 and report the first tick after which the lag-32 difference below `target`+1 stays zero (settling of wheels <= target)."""
    ring = [x0]; t = 0; mask = (1 << (target + 1)) - 1; last_nonzero = 0
    while True:
        x = step(ring[-1]); t += 1; ring.append(x)
        if len(ring) > P + 1: ring.pop(0)
        if t >= P:
            if (x ^ ring[0]) & mask: last_nonzero = t
            elif t - last_nonzero > 4 * P and t > P: return last_nonzero
        if t > 3_000_000: return None
if CMD == 'init':
    t0 = time.time()
    x, first, t = settle(1)
    save_row('A0', x)
    st = {'strips': {'A0': {'parent': None, 'fork': 0, 'first_return': first, 'phase_tick': t, 'digest': digest(x)}},
          'queue': [['analyze', 'A0']], 'order': ['A0'], 'log': [f"init: seed settled, first return at tick {first}, row taken at tick {t} ({time.time()-t0:.0f} s)"]}
    save(st); print(st['log'][-1])
elif CMD == 'step':
    st = load()
    if not st['queue']: print("queue empty"); sys.exit(0)
    item = st['queue'].pop(0); t0 = time.time()
    if item[0] == 'analyze':
        name = item[1]; x = load_row(name); c = cycle_of(x); w = words_of(c)
        whites = [int(j) for j in np.where(w == 0)[0] if j >= 2]
        ev = []
        for wh in whites:
            a = int(w[wh - 1]); q = minperiod(a); par = bin(a & ((1 << q) - 1)).count('1') % 2
            kind = 'fork' if par == 0 else 'doubling'
            ok = None
            if wh + 1 < K:
                ch = int(w[wh + 1]); comp = (~ch) & ((1 << P) - 1)
                ok = (rot(ch, q) == comp) if kind == 'doubling' else (rot(ch, q) == ch and rot(ch, q) != comp)
            ev.append([wh, q, kind, ok])
        fork = st['strips'][name]['fork']
        forks_above = [e[0] for e in ev if e[2] == 'fork' and e[0] > fork]
        doublings_above = [e[0] for e in ev if e[2] == 'doubling' and e[0] > max(fork, 399)]
        F = front_at_end(w)
        st['strips'][name].update({'whites': ev, 'forks_above': forks_above, 'doublings_above': doublings_above, 'front': int(F),
                                   'return16': c[16] == x})
        for wh in forks_above:
            child = f"{name}.{wh}"
            st['queue'].append(['settle', child, name, wh])
        st['log'].append(f"analyze {name}: whites {[(e[0], e[2]) for e in ev]}, F(K-1) = {F}, siblings at {forks_above} ({time.time()-t0:.0f} s)")
    elif item[0] == 'settle':
        child, parent, wh = item[1], item[2], item[3]
        x = load_row(parent) ^ (1 << (wh + 1))
        y, first, t = settle(x)
        save_row(child, y)
        st['strips'][child] = {'parent': parent, 'fork': wh, 'first_return': first, 'phase_tick': t, 'digest': digest(y)}
        st['order'].append(child); st['queue'].append(['analyze', child])
        st['log'].append(f"settle {child} (from {parent}, child bit {wh+1} complemented): first return at tick {first}, row taken at tick {t} ({time.time()-t0:.0f} s)")
    save(st); print(st['log'][-1])
elif CMD == 'edge':
    # the single cell's lag-32 settling tick through 894,235 (P-A2), a separate long invocation
    t0 = time.time(); tick = edge_cross('seed', 1, K - 1)
    st = load(); st['seed_edge'] = tick; st['log'].append(f"seed: lag-32 differences below {K} last seen at tick {tick} ({time.time()-t0:.0f} s)"); save(st); print(st['log'][-1])
elif CMD == 'report':
    st = load()
    P8_forks = [53207, 58286, 72575, 165748, 174449, 179399, 243767, 350243, 445474, 482608, 485619, 537692, 563842, 603582, 760454]
    P8_exits = [87867, 183184, 196189, 229338, 253537, 271596, 291257, 527724, 551910, 555813, 575211, 634886, 645655, 667052, 770532, 894235]
    print(f"K = {K} wheels, period {P}; strips: {len(st['strips'])}")
    forks = []; dbl = []
    for name in st['order']:
        s = st['strips'][name]
        print(f"{name}: parent {s['parent']}, created at fork {s['fork']}, first return {s['first_return']}, row at tick {s['phase_tick']}, digest {s['digest']}")
        if 'whites' in s:
            print(f"   whites: {[(e[0], e[1], e[2], e[3]) for e in s['whites']]}")
            print(f"   forks above {s['forks_above']}, doubling above {s['doublings_above']}, F({K-1}) = {s['front']}, returns after 16: {s['return16']}")
            forks += s['forks_above']; dbl += s['doublings_above']
    print(f"fork wheels found {sorted(forks)}")
    print(f"P-A1 forks = Prop. 8's branch depths: {sorted(forks) == P8_forks}")
    print(f"doubling wheels found (white wheel below the doubled child) {sorted(dbl)}")
    print(f"P-A1 doublings + 1 = Prop. 8's exits: {sorted(d + 1 for d in dbl) == P8_exits}")
    fr = [st['strips'][n]['front'] for n in st['order'] if 'front' in st['strips'][n]]
    print(f"fronts at {K-1}: min {min(fr)} max {max(fr)}; P-A2 fronts within [1760000, 1820000]: {all(1760000 <= f <= 1820000 for f in fr)}")
    print(f"seed edge: {st.get('seed_edge')}")
    for l in st['log']: print("  log:", l)
