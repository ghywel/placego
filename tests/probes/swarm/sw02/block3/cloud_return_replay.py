# Cloud's independent replay of GC2706/GC2709 on the retained X gap DFAs (CL753; own code). Argument: the directory holding dfa_xx_W38..41_c0.txt from the shared store packet cited/gpt/gc2706-bridge-return-20261106.tar.gz (inputs/).
import sys, itertools
from collections import deque
A = [2,5]; E = [3,3,5,3,5,5,5,5]
DEAD = -1
def read(path):
    T, cnt = {}, {}
    for ln in open(path):
        p = ln.split()
        if not p: continue
        q = int(p[0]); cnt[q] = int(p[1])
        T[q] = {int(a): int(b) for a,b in (x.split(':') for x in p[2:])}
    return T, cnt
def step(T, q, word):
    for g in word:
        if q == DEAD: return DEAD
        q = T.get(q, {}).get(g, DEAD)
    return q
def unary(T, q):
    """states q, qA, qA^2, ... until repeat: returns (states, mu, period)"""
    seen, states = {}, []
    while q not in seen and q != DEAD:
        seen[q] = len(states); states.append(q); q = step(T, q, A)
    if q == DEAD:
        states.append(DEAD); return states, len(states)-1, 1   # dead absorbs
    return states, seen[q], len(states)-seen[q]
def fn_seq(T, q):
    """f_n(q) = delta(q, A^n E) as (prefix list, cycle list) over n."""
    states, mu, per = unary(T, q)
    dest = [step(T, s, E) for s in states]
    return dest[:mu], dest[mu:mu+per]
def at(seq, n):
    pre, cyc = seq
    return pre[n] if n < len(pre) else cyc[(n-len(pre)) % len(cyc)]
def boundary_states(T, q0):
    B, todo = {q0}, deque([q0]); F = {}
    while todo:
        q = todo.popleft(); F[q] = fn_seq(T, q)
        for s in F[q][0] + F[q][1]:
            if s != DEAD and s not in B: B.add(s); todo.append(s)
    return B, F
def minimize(B, F):
    # Moore refinement on the infinite alphabet N via the ultimately periodic successor sequences.
    N = max(len(F[q][0]) for q in B) + 1
    L = 1
    for q in B:
        l = len(F[q][1]); 
        import math; L = L*l//math.gcd(L,l)
    horizon = N + 2*L            # comparing n < horizon decides equality of the ultimately periodic class sequences
    cls = {q: 0 for q in B}; cls[DEAD] = -1
    while True:
        sig = {q: (cls[q], tuple(cls[at(F[q], n)] for n in range(horizon))) for q in B}
        keys = sorted(set(sig.values()))
        new = {q: keys.index(sig[q]) for q in B}; new[DEAD] = -1
        if all(new[q] == cls[q] for q in B): return cls, horizon
        cls = new
def describe(F, q, horizon, cls):
    out = {}
    for n in range(horizon):
        d = at(F[q], n)
        out.setdefault(cls[d] if d != DEAD else 'dead', []).append(n)
    return out
def nfa_grammar(thr_S):
    """Two-state return grammar as a gap NFA over letters; every state initial & accepting (factor language).
       NFA state: (mode in {R,S}, k = A's since last E saturating at 7, pos in current block or None)"""
    # We encode positions inside blocks: block A = [2,5], E = [3,3,5,3,5,5,5,5].
    states = set(); trans = {}
    def add(s, g, t): trans.setdefault((s,g), set()).add(t); states.add(s); states.add(t)
    for mode in 'RS':
        for k in range(8):
            base = (mode, k, 'b')           # at a block boundary with k A's read since last E
            # read an A block
            add(base, 2, (mode, k, 'a1')); add((mode, k, 'a1'), 5, (mode, min(k+1,7), 'b'))
            # read an E block if allowed
            allowed = (mode=='R' and (k==4 or k>=6)) or (mode=='S' and k>=thr_S)
            if allowed:
                nm = 'S' if (mode=='R' and k==4) else 'R'
                prev = base
                for i,g in enumerate(E):
                    nxt = (nm, 0, 'b') if i == len(E)-1 else (mode, k, f'e{i+1}')
                    add(prev, g, nxt); prev = nxt
    return states, trans
def nfa_step(trans, S, g):
    out = set()
    for s in S: out |= trans.get((s,g), set())
    return out
def compare_factor(T, states, trans):
    """Compare factor languages: DFA with all states initial vs NFA with all states initial, by product BFS on subsets."""
    letters = [2,3,5]
    start = (frozenset(T.keys()), frozenset(states))
    seen = {start}; todo = deque([start]); pairs = 0
    while todo:
        Sd, Sn = todo.popleft(); pairs += 1
        if (len(Sd) > 0) != (len(Sn) > 0): return False, pairs, (Sd, Sn)
        if not Sd: continue
        for g in letters:
            nd = frozenset(t for q in Sd for t in [T[q].get(g, DEAD)] if t != DEAD)
            nn = frozenset(nfa_step(trans, Sn, g))
            key = (nd, nn)
            if key not in seen: seen.add(key); todo.append(key)
    return True, pairs, None
for W in (38,39,40,41):
    T, cnt = read(f"{sys.argv[1]}/dfa_xx_W{W}_c0.txt")
    q0 = step(T, 0, E)
    B, F = boundary_states(T, q0)
    cls, horizon = minimize(B, F)
    ncls = len(set(cls[q] for q in B))
    print(f"\n=== W={W}: DFA states {len(T)}, q0 after E = {q0} ({cnt[q0]} windows), raw boundary states {len(B)}, quotient classes {ncls}, horizon {horizon}")
    reps = {}
    for q in sorted(B): reps.setdefault(cls[q], q)
    for c, q in sorted(reps.items()):
        d = describe(F, q, horizon, cls)
        summ = {k: (v[:6] + ['...'] if len(v) > 6 else v) for k, v in d.items() if k != 'dead'}
        print(f"  class {c} (rep raw {q}, members {sorted(x for x in B if cls[x]==c)}): next n -> class: {summ}")
    # counterwords, factor sense (from any state)
    for name, word in [("55 A^4 E A^4 3", [5,5]+A*4+E+A*4+[3]), ("55 A^4 E A^6 3", [5,5]+A*4+E+A*6+[3]), ("E A^4 E A^7 E", E+A*4+E+A*7+E), ("E A^6 E A^4 E", E+A*6+E+A*4+E)]:
        live = any(step(T, q, word) != DEAD for q in T)
        print(f"  factor {name}: {'present' if live else 'absent'}")
    # full factor-language comparison with the two-state grammar (threshold for S: 6 at 38, 7 otherwise)
    thr = 6 if W == 38 else 7
    states, trans = nfa_grammar(thr)
    eq, pairs, wit = compare_factor(T, states, trans)
    print(f"  factor language == two-state grammar (S threshold {thr}): {eq} ({pairs} reachable subset pairs; NFA states {len(states)})")
    # raw fibres under C = A^4 E A^7 E from q0, and reset thresholds
    C = A*4+E+A*7+E
    q = q0; chain = [(q, cnt[q])]
    for _ in range(4):
        q = step(T, q, C); chain.append((q, cnt.get(q)))
    print(f"  raw fibre chain under C from q0: {chain}")
    for n in (6,7,8,9,12):
        dests = {step(T, q, A*n+E) for q in B}
        print(f"    n={n}: destinations over all boundary states {sorted(dests)} -> {'common reset to raw '+str(list(dests)[0])+' ('+str(cnt.get(list(dests)[0]))+' windows)' if len(dests)==1 else 'no common reset'}")
