# Carry of GC2775 (Cloud, CL758): the kit's gate trap (829 width-16 windows at odd times, bit i = column i+1, centre white at
# odd ticks, black at even; column 17 takes two free values x1, x2 over the double step) replayed with own code: closure,
# and the path sets of the words 3353 (15 samples) and E = 33535555 (35 samples) inside the trap. Own code.
import sys
codes = [int(x) for x in open(sys.argv[1]).read().split()]
T = set(codes); assert len(T) == 829
def tick(cells, c):
    """cells: list of 0/1 for columns 1..n (plus known column n+1 appended by caller); c = centre (column 0). Returns columns 1..n-1."""
    n = len(cells); out = []
    for i in range(n - 1):
        left = c if i == 0 else cells[i - 1]; mid = cells[i]; right = cells[i + 1]
        out.append(left ^ (mid | right))
    return out
def step2(w, x1, x2):
    cells = [(w >> i) & 1 for i in range(16)] + [x1]           # columns 1..17 at the odd tick
    e = tick(cells, 0)                                          # even tick: columns 1..16, centre white at the odd tick
    e = e + [x2]                                                # column 17 at the even tick free
    o = tick(e, 1)                                              # next odd tick: columns 1..16, centre black at the even tick
    return sum(b << i for i, b in enumerate(o))
# closure
bad = 0; edges = 0
succ = {}
for w in codes:
    succ[w] = set()
    for x1 in (0, 1):
        for x2 in (0, 1):
            v = step2(w, x1, x2); edges += 1
            if v not in T: bad += 1
            succ[w].add(v)
print(f"closure: {edges} transitions, {bad} leave the trap; distinct successor pairs {sum(len(s) for s in succ.values())}")
# the empty right half enters at tick 293 with window 49415 (kit entry_empty): replay by direct evolution of the white row
row = [0] * 400; c_seq = []
def evolve_row(row, t):
    c = 1 if t % 2 == 0 else 0
    n = len(row); new = [0] * n
    for i in range(n):
        left = c if i == 0 else row[i - 1]; right = row[i + 1] if i + 1 < n else 0
        new[i] = left ^ (row[i] | right)
    return new
cur = row[:]; first = None
for t in range(1, 320):
    if t % 2 == 1:
        w = sum(cur[i] << i for i in range(16))
        if w in T and first is None: first = (t, w)
    cur = evolve_row(cur, t)
print("empty right half: first odd-time trap window", first, "(kit: tick 293, code 49415)")
# path sets of a sampled word inside the trap: layer k = trap windows reachable along trap edges whose column 1 matches the word
def pathsets(word_bits):
    layer = {w for w in T if (w & 1) == word_bits[0]}; sizes = [len(layer)]
    for b in word_bits[1:]:
        nxt = set()
        for w in layer:
            for v in succ[w]:
                if (v & 1) == b: nxt.add(v)
        layer = nxt; sizes.append(len(layer))
        if not layer: break
    return sizes
def bits_of_gaps(gaps):
    u = [0] * (sum(gaps) + 1); p = 0; u[0] = 1
    for g in gaps: p += g; u[p] = 1
    return u
print("3353 path-set sizes in the trap:", pathsets(bits_of_gaps([3, 3, 5, 3])), "(GPT: 188,191,186,68,68,69,17,21,21,18,21,29,40,41,0)")
print("E = 33535555 path-set sizes:", pathsets(bits_of_gaps([3, 3, 5, 3, 5, 5, 5, 5])))
print("A = 25 path-set sizes:", pathsets(bits_of_gaps([2, 5])), "(gap 2 impossible after entry by gaps_of_entry)")
print("gap-3 word 333 and gap-5 word 555 path-set sizes:", pathsets(bits_of_gaps([3, 3, 3])), pathsets(bits_of_gaps([5, 5, 5])))
