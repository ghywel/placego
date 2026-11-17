#!/usr/bin/env python3
"""L1440 (Local, 2026-11-03): replay the exported perturbation-census certificates (GC2543's retention request).
Run: python3 tests/probes/wolfram/a4_census_cert_check.py DATA.json CERT.json
Checks, independently of the census run: (1) A4's closure in DATA is closed under both inputs, every state keeps a difference,
and its psi satisfies psi(s') - psi(s) = P * motion + (P - S) on every edge; (2) each own closure likewise, with its own psi;
(3) every entry's state lies in the closure it names, with the stated psi for A4 entries; (4) the entries are exactly the
nonzero patterns below 2 ^ WP. The entry states themselves come from the exact simulation in a4_perturbation_census.py.
"""
import json
import sys

data = json.load(open(sys.argv[1])); cert = json.load(open(sys.argv[2]))
orb = [tuple(o) for o in data['orb']]; q = len(orb); N = data['N']; r0, s0 = data['r'], data['s']
P, S = data['P'], data['S']
assert (cert['P'], cert['S'], cert['W'], cert['r'], cert['s']) == (P, S, data['W'], r0, s0)
rule = lambda a, b, c: a ^ (b | c)


def transitions(state):
    tq, dq, strip = state; L = len(strip)
    Eb = lambda i, dt=0: orb[(tq + dt + s0) % q][((dq + dt - i) + r0) % N]
    outs = []
    for b in (0, 1):
        cell = lambda i: Eb(i) if i <= 0 else (strip[i - 1] if i <= L else b)
        new = {i: rule(cell(i - 1), cell(i), cell(i + 1)) for i in range(0, L + 1)}
        if new[0] != Eb(0, 1):
            ns = tuple(new[i] for i in range(0, L)); ndq = (dq + 2) % N; mv = -1
        else:
            ns = tuple(new[i] for i in range(1, L + 1)); ndq = (dq + 1) % N; mv = 0
        Enew = lambda i: orb[(tq + 1 + s0) % q][((ndq - i) + r0) % N]
        if not any(ns[i] != Enew(i + 1) for i in range(len(ns))):
            return None
        outs.append((((tq + 1) % q, ndq, ns), mv))
        if mv == -1:
            break
    return outs


def check_closure(states, psi, label):
    pos = {st: i for i, st in enumerate(states)}
    for st in states:
        outs = transitions(st)
        assert outs is not None, '%s: a state loses its difference' % label
        for n, mv in outs:
            assert n in pos, '%s: not closed' % label
            assert psi[pos[n]] - psi[pos[st]] == P * mv + (P - S), '%s: potential fails on an edge' % label
    return pos


dec = lambda e: (e[0], e[1], tuple(int(ch) for ch in e[2]))
A4 = [(s[0], s[1], tuple(s[2])) for s in data['states']]
posA4 = check_closure(A4, data['lo'], 'A4 closure'); assert data['lo'] == data['hi']
print('A4 closure: %d states, closed under both inputs, every state keeps a difference, exact potential: PASS' % len(A4))
owns = []
for o in cert['own_closures']:
    sts = [dec(e) for e in o['states']]; assert o['psi'] is not None
    owns.append(check_closure(sts, o['psi'], 'own closure')); assert dec(o['start']) in owns[-1]
    print('own closure: %d states, closed, every state keeps a difference, exact potential: PASS' % len(sts))
pats = sorted(e[0] for e in cert['entries'])
assert pats == list(range(1, 1 << cert['WP'])), 'entries are not all nonzero patterns'
nA4 = nown = 0
for pat, tc, st, kind, psi in cert['entries']:
    st = dec(st)
    if kind == 'A4':
        assert st in posA4 and data['lo'][posA4[st]] == psi; nA4 += 1
    else:
        assert any(st in p for p in owns); nown += 1
print('entries: all %d nonzero patterns on [0,%d); in A4\'s closure %d, in an own closure %d: PASS' % (
    len(pats), cert['WP'], nA4, nown))
print('A4_CENSUS_CERT_CHECK_DONE')
