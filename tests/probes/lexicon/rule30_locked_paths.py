"""GC372: exact finite-strip path projections, with arbitrary exterior input.
Distinct from departure SAT; unresolved strip states do not prove global continuations.
"""
import json
import re
from pathlib import Path


def step(state, m, t, u, unext, ext):
    row = (t % 2) | (u << 1) | (state << 2) | (ext << (m + 1))
    nxt = (row << 1) ^ (row | (row >> 1))
    if ((nxt >> 1) & 1) != unext:
        return None
    return (nxt >> 2) & ((1 << (m - 1)) - 1)


def literal(state, m, t, u, unext, ext):
    row = [t % 2, u] + [(state >> i) & 1 for i in range(m - 1)] + [ext]
    nxt = [row[x-1] ^ (row[x] | row[x+1]) for x in range(1, m+1)]
    if nxt[0] != unext:
        return None
    return sum(nxt[x-1] << (x-2) for x in range(2, m+1))


def audit(m, N, U):
    transitions = []
    for p in range(56):
        transitions.append([tuple(sorted({c for e in (0, 1)
                 if (c := step(s, m, p, U[p], U[(p+1)%56], e)) is not None}))
                 for s in range(1 << (m-1))])
    if m == 4:
        for p in range(56):
            for s in range(8):
                for e in (0,1):
                    assert step(s,m,p,U[p],U[(p+1)%56],e)==literal(s,m,p,U[p],U[(p+1)%56],e)
    forward = [set(range(1 << (m-1)))]
    for t in range(N-1):
        forward.append({c for s in forward[-1] for c in transitions[t%56][s]})
    assert forward[-1]
    viable = [None] * N
    viable[-1] = forward[-1]
    for t in range(N-2,-1,-1):
        viable[t] = {s for s in forward[t] if any(c in viable[t+1] for c in transitions[t%56][s])}
        assert viable[t]
    counts = [sum(len({(s>>i)&1 for s in states}) == 1 for states in viable)
              for i in range(m-1)]
    complete = [i+2 for i in range(m-1) if all(len({(s>>i)&1 for s in viable[t]})==1
                 for t in range(N//3,2*N//3))]
    period_conflicts = sum(1 for i in range(m-1) for t in range(N-56)
        if len(a := {(s>>i)&1 for s in viable[t]}) == 1
        and len(b := {(s>>i)&1 for s in viable[t+56]}) == 1 and a != b)
    assert all(v <= f for v,f in zip(viable,forward))
    return dict(width=m,N=N,singleton_counts=counts,complete_middle_columns=complete,
                known_period56_conflicts=period_conflicts,
                states_at_middle=len(viable[N//2]),
                forward_states_at_middle=len(forward[N//2]))


def main():
    text=Path('tests/probes/lexicon/rule30_wheel_left.py').read_text()
    U=[int(c) for c in re.search(r'^U = "([01]+)"',text,re.M).group(1)]
    print(json.dumps([audit(m,168,U) for m in (4,8,12)],indent=2))

if __name__ == '__main__':
    main()
