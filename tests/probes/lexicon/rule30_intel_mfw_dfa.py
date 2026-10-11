#!/usr/bin/env python3
"""rule30_intel_mfw_dfa.py: the automaton of the visible language's minimal-forbidden-word cutoff X_K for the
forced-only engine (probe FO, CL282 and CL297): the words that avoid every minimal forbidden word of length <= K of
L (phase 0) or L1 (phase 1), read from rule30_visible_language_handoff.md (section 3, and section 4's difference for
L1).
A word of length <= 40 is in the language exactly when it avoids those of length <= 40 (handoff, section 1), so X_40
is exact to length 40 and a superset of the real language at every length (it contains L, as the check-free
conjecture requires). Construction: Aho-Corasick over the words (no word is a factor of another, by minimality),
transitions completing a word removed, then Moore partition refinement to the minimal automaton.
Controls printed: the number of words per length n <= 40 against the handoff's table C_n (section 2), and the
growth rate (log2 of the spectral radius) of the minimal automaton's trimmed part.
Output: 'n_states' then 'next0 next1' per state (-1: no transition), start state 0; the engine's dfa= format.
Usage: python3 rule30_intel_mfw_dfa.py PHASE K OUT.dfa"""
import os, re, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
HANDOFF = os.path.join(HERE, 'rule30_visible_language_handoff.md')
TABLE_L = [2, 3, 5, 8, 12, 17, 25, 36, 50, 68, 91, 119, 156, 199, 251, 316, 393, 487, 596, 721, 875, 1054, 1255,
           1493, 1780, 2111, 2483, 2904, 3378, 3908, 4502, 5153, 5875, 6664, 7541, 8534, 9649, 10876, 12231, 13730]
TABLE_L1 = [2, 3, 5, 8, 12, 17, 25, 36, 49, 65, 88, 115, 148, 188, 237, 296, 365, 452, 549, 668, 807, 976, 1162, 1382,
            1646, 1947, 2288, 2671, 3098, 3578, 4122, 4699, 5348, 6054, 6850, 7747, 8743, 9850, 11063, 12409]

def sections():
    text = open(HANDOFF).read().split('\n'); sec = {}; cur = None
    for line in text:
        m = re.match(r'^#{2,3} (\d+[ab]?)\. ', line)
        if m: cur = m.group(1); sec[cur] = []; continue
        if cur and re.fullmatch(r'\s*[01]+( [01]+)*\s*', line): sec[cur] += line.split()
    return sec

def words(phase):
    s = sections(); L = set(s['3']); assert len(L) == 771, len(L)
    if phase == 0: return L
    add, drop = set(s['4a']), set(s['4b']); assert len(add) == 307 and len(drop) == 246 and drop <= L
    W = (L - drop) | add; assert len(W) == 832; return W

def automaton(F):
    goto = [{}]; term = [False]
    for w in sorted(F):
        v = 0
        for ch in w:
            b = int(ch)
            if b not in goto[v]: goto[v][b] = len(goto); goto.append({}); term.append(False)
            v = goto[v][b]
        term[v] = True
    fail = [0] * len(goto); order = []; queue = [0]
    while queue:
        v = queue.pop(0); order.append(v)
        for b, u in goto[v].items():
            if v == 0: fail[u] = 0
            else:
                f = fail[v]
                while f and b not in goto[f]: f = fail[f]
                fail[u] = goto[f][b] if b in goto[f] and goto[f][b] != u else 0
            queue.append(u)
    delta = [[0, 0] for _ in goto]
    for v in order:
        for b in (0, 1):
            delta[v][b] = goto[v][b] if b in goto[v] else (delta[fail[v]][b] if v else 0)
    dead = term      # a completed word ends the walk; no word is a factor of another, so no suffix link is a word
    # minimise: states = live trie nodes plus one dead state; Moore refinement
    n = len(goto); D = n
    tr = [[(D if dead[delta[v][b]] else delta[v][b]) for b in (0, 1)] for v in range(n)] + [[D, D]]
    cls = [1 if (v == D or dead[v]) else 0 for v in range(n + 1)]
    while True:
        sig = {}; new = []
        for v in range(n + 1):
            key = (cls[v], cls[tr[v][0]], cls[tr[v][1]]); new.append(sig.setdefault(key, len(sig)))
        if len(sig) == len(set(cls)): break
        cls = new
    # relabel: start (trie root) -> 0, dead class -> -1, BFS order from the start
    dcls = cls[D]; ids = {cls[0]: 0}; rep = {}; out = []
    for v in range(n + 1): rep.setdefault(cls[v], v)
    order = [cls[0]]; i = 0
    while i < len(order):
        c = order[i]; v = rep[c]; row = []
        for b in (0, 1):
            cc = cls[tr[v][b]]
            if cc == dcls: row.append(-1); continue
            if cc not in ids: ids[cc] = len(ids); order.append(cc)
            row.append(ids[cc])
        out.append(row); i += 1
    return out

def counts(dfa, nmax):
    v = np.zeros(len(dfa), dtype=object); v[0] = 1; res = []
    for n in range(1, nmax + 1):
        w = np.zeros(len(dfa), dtype=object)
        for s, row in enumerate(dfa):
            if v[s]:
                for t in row:
                    if t >= 0: w[t] += v[s]
        v = w; res.append(int(sum(v)))
    return res

def growth(dfa):
    import scipy.sparse as sp, scipy.sparse.linalg as sla
    n = len(dfa)
    r = [i for i, row in enumerate(dfa) for t in row if t >= 0]; c = [t for row in dfa for t in row if t >= 0]
    A = sp.csr_matrix((np.ones(len(r)), (r, c)), shape=(n, n))
    ev = sla.eigs(A.astype(float), k=1, which='LM', return_eigenvectors=False, maxiter=100000)
    return float(np.log2(abs(ev[0])))

if __name__ == '__main__':
    phase, K, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    F = {w for w in words(phase) if len(w) <= K}
    dfa = automaton(F)
    with open(out, 'w') as f:
        f.write(f"{len(dfa)}\n")
        for row in dfa: f.write(f"{row[0]} {row[1]}\n")
    C = counts(dfa, 40); T = TABLE_L if phase == 0 else TABLE_L1
    nk = min(K, 40); ok = C[:nk] == T[:nk]
    print(f"phase {phase}, K = {K}: {len(F)} minimal forbidden words; minimal automaton {len(dfa)} states; growth "
          f"{growth(dfa):.5f} bits per visible bit; counts n = 1..{nk} {'MATCH' if ok else 'DIFFER'} the handoff table"
          f" -> {out}")
    if not ok: print('  first difference at n =', next(i + 1 for i in range(nk) if C[i] != T[i]), C[:nk], T[:nk])
