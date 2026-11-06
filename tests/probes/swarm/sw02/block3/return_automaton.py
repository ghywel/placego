#!/usr/bin/env python3
"""Exact induced E-boundary machines on retained gap DFAs; no window lifting.

Every nondead state accepts. Quotients preserve complete macro continuations,
not unfinished A tails or partial E words. All labels are exact unary orbits.
Source claims retain the original DFA extraction's certification limitations.
"""
import argparse
import collections
import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import networkx as nx

DEAD = -1
A, E = '25', '33535555'


def read(path):
    T = {}
    for line in path.read_text().splitlines():
        p = line.split()
        q = int(p[0])
        assert q not in T
        T[q] = {int(a): int(b) for a, b in (x.split(':') for x in p[2:])}
    assert 0 in T and DEAD not in T
    assert all(v in T for row in T.values() for v in row.values())
    return T


def step(T, q, w):
    for c in w:
        q = T.get(q, {}).get(int(c), DEAD)
    return q


def orbit(T, q, a=A, e=E):
    states, seen, dest = [], {}, []
    while q not in seen:
        seen[q] = len(states)
        states.append(q)
        dest.append(step(T, q, e))
        q = step(T, q, a)
    return {'states': states, 'dest': dest, 'mu': seen[q],
            'period': len(states) - seen[q]}


def nth(o, n):
    return o['dest'][n if n < len(o['dest']) else o['mu'] + (n-o['mu']) % o['period']]


def canonical(values, mu, period):
    """Unique shortest preperiod, then primitive cycle, for an infinite word."""
    cyc = values[mu:mu+period]
    p = next(p for p in range(1, period+1)
             if period % p == 0 and all(cyc[i] == cyc[i % p] for i in range(period)))
    def at(n):
        return values[n] if n < len(values) else cyc[(n-mu) % period]
    m = mu
    while m and at(m-1) == at(m-1+p):
        m -= 1
    return tuple(at(n) for n in range(m)), tuple(at(n) for n in range(m, m+p))


def boundary(T):
    initial = step(T, 0, E)
    assert initial != DEAD
    O, history = {}, {initial: []}
    todo = collections.deque([initial])
    while todo:
        q = todo.popleft()
        o = O[q] = orbit(T, q)
        for n, t in enumerate(o['dest']):
            if t != DEAD and t not in history:
                assert len(history) < 512, 'boundary state stop'
                history[t] = history[q] + [n]
                todo.append(t)
    O[DEAD] = orbit(T, DEAD)
    P = {q: int(q == DEAD) for q in O}
    while True:
        ids = {}
        new = {q: ids.setdefault((q == DEAD, canonical([P[t] for t in o['dest']],
                         o['mu'], o['period'])), len(ids)) for q, o in O.items()}
        if len(set(new.values())) == len(set(P.values())):
            P = new
            break
        P = new
    # Stable readable class IDs by BFS discovery order, rejection stays -1.
    ids = {}
    P = {q: DEAD if q == DEAD else ids.setdefault(P[q], len(ids)) for q in O}
    reps = {P[q]: q for q in reversed(list(O))}
    reps[DEAD] = DEAD
    Q = {}
    for c, q in sorted(reps.items()):
        if c == DEAD:
            continue
        o = O[q]
        pre, cyc = canonical([P[t] for t in o['dest']], o['mu'], o['period'])
        Q[c] = {'representative': q, 'members': [v for v in O if P[v] == c],
                'history': history[q], 'prefix': list(pre), 'cycle': list(cyc)}
    return initial, O, P, Q


def qstep(Q, q, n):
    if q == DEAD:
        return DEAD
    row = Q[q]
    m, p = len(row['prefix']), len(row['cycle'])
    return row['prefix'][n] if n < m else row['cycle'][(n-m) % p]


def paired(T, u, v):
    seen, out, n = set(), [], 0
    while (u, v) not in seen:
        seen.add((u, v))
        out.append((n, step(T, u, E), step(T, v, E)))
        u, v = step(T, u, A), step(T, v, A)
        n += 1
    return out


def distinguish(T, O, P, Q, a, b):
    reps = {q: row['representative'] for q, row in Q.items()} | {DEAD: DEAD}
    todo = collections.deque([(a,b,[])])
    seen = {(a,b)}
    while todo:
        x,y,w = todo.popleft()
        if (x == DEAD) != (y == DEAD):
            return w
        for n,u,v in paired(T,reps[x],reps[y]):
            z = P[u], P[v]
            if z not in seen:
                seen.add(z)
                todo.append((*z,w+[n]))
    return None


def audit(T, initial, O, P, Q):
    # Check the entire raw-to-quotient commuting map on the paired cycles.
    for q,o in O.items():
        if q == DEAD:
            continue
        r = Q[P[q]]['representative']
        assert all(P[u] == P[v] for _,u,v in paired(T,q,r))
        # Independent literal replay, including the first repeated cycle.
        for n in range(o['mu']+2*o['period']+1):
            v = q
            for letter in A*n+E:
                edges = T[v] if v in T else {}
                v = edges[int(letter)] if int(letter) in edges else DEAD
            assert P[v] == qstep(Q,P[q],n)
    witnesses = {}
    for a in Q:
        for b in Q:
            if a >= b:
                continue
            w = distinguish(T,O,P,Q,a,b)
            assert w is not None, 'nonminimal quotient'
            u,v = Q[a]['representative'], Q[b]['representative']
            for n in w:
                u,v = step(T,u,A*n+E), step(T,v,A*n+E)
            assert (u == DEAD) != (v == DEAD)
            witnesses[f'{a},{b}'] = w
    # A wrong table entry must disagree with the literal transition.
    q = P[initial]
    n = next(n for n in range(len(Q[q]['prefix'])+len(Q[q]['cycle']))
             if qstep(Q,q,n) != DEAD)
    assert P[step(T,initial,A*n+E)] != DEAD
    mutant = copy.deepcopy(Q)
    if n < len(mutant[q]['prefix']):
        mutant[q]['prefix'][n] = DEAD
    else:
        mutant[q]['cycle'][(n-len(mutant[q]['prefix'])) % len(mutant[q]['cycle'])] = DEAD
    assert qstep(mutant,q,n) != P[step(T,initial,A*n+E)]
    return {'commutation': True, 'literal_replay': True,
            'corrupt_transition_rejected': True, 'distinguishing_words': witnesses}


def resets(Q):
    # Track every state's periodic output position, not a guessed global cutoff.
    seen, values, n = {}, [], 0
    while True:
        phase = tuple(n if n < len(r['prefix']) else len(r['prefix'])+
                     (n-len(r['prefix'])) % len(r['cycle']) for r in Q.values())
        if phase in seen:
            return {'mu': seen[phase], 'period': n-seen[phase], 'values': values}
        assert n < 10000, 'joint reset orbit stop'
        seen[phase] = n
        images = [qstep(Q,q,n) for q in Q]
        nondead = sorted(set(images)-{DEAD})
        values.append({'n':n, 'images':images, 'total_reset':len(set(images))==1 and
                       images[0]!=DEAD, 'survivor_sync':len(nondead)==1})
        n += 1


def clock(Q):
    G = nx.DiGraph()
    G.add_nodes_from(Q)
    for q,row in Q.items():
        for n,t in enumerate(row['prefix']+row['cycle']):
            if t != DEAD and not G.has_edge(q,t):
                G.add_edge(q,t,n=n,cost=34+7*n)
    best, attaining, count = None,None,0
    for cyc in nx.simple_cycles(G):
        count += 1
        assert count <= 10000, 'cycle stop'
        es = [(q,cyc[(i+1)%len(cyc)]) for i,q in enumerate(cyc)]
        mean = Fraction(sum(G[u][v]['cost'] for u,v in es),len(cyc))
        if best is None or mean < best:
            best,attaining = mean,es
    assert best is not None
    h = {q:Fraction(0) for q in Q}
    for _ in range(len(Q)-1):
        for u,v,d in G.edges(data=True):
            h[v] = min(h[v],h[u]+d['cost']-best)
    assert all(d['cost']-best >= h[v]-h[u] for u,v,d in G.edges(data=True))
    edges = [dict(source=u,target=v,**d) for u,v,d in G.edges(data=True)]
    cycstates = set().union(*(set(c) for c in nx.simple_cycles(G)))
    live = {q for q in Q if any(nx.has_path(G,q,c) for c in cycstates)}
    return {'min_mean_sampled':str(best), 'potential':{q:str(v) for q,v in h.items()},
            'potential_oscillation':str(max(h.values())-min(h.values())),
            'attaining': [dict(source=u,target=v,**G[u][v]) for u,v in attaining],
            'edges':edges, 'simple_cycles':count, 'infinite_return_states':sorted(live)}


def controls():
    assert canonical([0,1,0,1,0],3,2) == ((),(0,1))
    assert canonical([9,0,1,0,1],1,4) == ((9,),(0,1))
    T = {0:{2:1,3:0},1:{2:2},2:{2:0,3:0}}
    o = orbit(T,0,'2','3')
    assert (o['mu'],o['period'],o['dest']) == (0,3,[0,-1,0])
    # Equal next-letter sets can conceal unequal next-next-letter sets.
    Q = {0:{'prefix':[1,2],'cycle':[-1]},1:{'prefix':[1,1],'cycle':[-1]},
         2:{'prefix':[2],'cycle':[-1]}}
    assert {n for n in range(3) if qstep(Q,0,n)!=-1} == {0,1}
    assert {n for n in range(3) if qstep(Q,1,n)!=-1} == {0,1}
    assert qstep(Q,qstep(Q,0,1),1)==-1 and qstep(Q,qstep(Q,1,1),1)!=-1
    return True


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--packet',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    assert controls()
    out={'controls':True,'widths':{}}
    for W in (38,39,40,41):
        path=args.packet/'dfa2'/f'dfa_xx_W{W}_c0.txt'
        T=read(path)
        assert step(T,0,'55'+A*4+E+A*4+'3') == DEAD
        assert (step(T,0,'55'+A*4+E+A*6+'3') != DEAD) == (W==38)
        initial,O,P,Q=boundary(T)
        r={'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
           'raw_dfa_states':len(T),'raw_return_states':len(O)-1,
           'initial_raw':initial,'initial_class':P[initial], 'quotient':Q,
           'raw_orbits':O, 'class_map':P, 'audit':audit(T,initial,O,P,Q),
           'resets':resets(Q),'clock':clock(Q)}
        out['widths'][W]=r
        print(json.dumps({'width':W,'raw_return_states':len(O)-1,'quotient':Q,
                          'resets':r['resets'],'clock':r['clock']}),flush=True)
    def structure(r):
        return [(q,row['prefix'],row['cycle']) for q,row in r['quotient'].items()]
    out['equal_39_40_41']=all(structure(out['widths'][39])==structure(out['widths'][w])
                              for w in (40,41))
    args.out.mkdir(parents=True,exist_ok=True)
    (args.out/'return.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':
    main()
