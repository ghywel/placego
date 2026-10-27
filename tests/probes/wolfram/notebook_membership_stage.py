#!/usr/bin/env python3
"""L1034: the minimal direct-membership stage of GC1987: P@100 and R@100 first, then P@99 only if needed.

Local, 2026-10-27. Source for GPT's freeze; it runs once under run_capped.py (CAPPED_OUT set) after the freeze. It
reuses GC1977's two reviewed encodings (notebook_death_gate.cnf: 'table' and 'or') and its literal evaluator
(notebook_death_gate.replay). Conventions: visible index j is physical time 2j, and the wall is x(t,0) = t mod 2.

Words: P = 00010101, Q = 00101010, R = 01010100. E_34^8 has 28 words; 25 have replayed age-100 witnesses (L1030);
GC1983 and L1031 established the reductions.
  - Shift law: P@(j-1) <=> Q@j for j >= 2.
  - Nestedness: E_(j+1)(w) => E_j(w).
  So an accepted P@100 witness gives P@99 and Q@100 as well.

Query plan, at most 6 external calls, each run in both encodings, in this order.
  1, 2. P@100 in 'table', then in 'or'.
  3, 4. R@100 in 'table', then in 'or'.
  5, 6. P@99 in 'table', then in 'or', made ONLY if P@100 was not accepted.
An answer is ACCEPTED_SAT when both encodings say SAT and every model satisfies every clause and replays physically
(the literal evaluator shows the word at that age). ACCEPTED_UNSAT means both say UNSAT. That is solver-reported
only: binary DRAT is retained and NOT checked here, and the result says so. Any SAT-versus-UNSAT disagreement
between the encodings stops the stage at once. UNKNOWN (a timeout or another return code) never means absence.

Controls, before any solver call (no search).
  C1. The retained P@98 and R@99 rows (cited/l1030-witness-pilot/latest_witnesses.json) give, through the literal
      evaluator, full cone histories. The induced assignment, cells plus the 'or' auxiliaries mirrored in the
      encoder's order, satisfies every clause of both encodings for (P, 98) and (R, 99).
  C2. Negative clause control: the same assignment with the word's last letter flipped violates a unit clause.

Predictions, written before any run.
  M1 (GC1983's reading). P@100 and R@100 are both possible, so the gate E_34^8 = E_100^8 closes in 4 calls.
  M2 (Local, about 50%). At least one of the four calls returns UNKNOWN within 30 s, since 00001001@100 timed out
      before; then the affected word stays unresolved.
  Counterfactual. An ACCEPTED_UNSAT at age 99 or 100 is a death after 43 among E_34^8 words. That bears directly on
      hypothesis G, as finite evidence pending certificate checking, and revises the historical short-word
      plateau.
Caps (GC1987): 6 calls of 30 s CPU and 30 s wall each; the parent admits a call only while own+children CPU is
below 210 s; stage wall 300 s, group RSS 512 MiB, disk 256 MiB, per-file 64 MiB; existing pressure stops. All
CNFs, solver outputs, DRAT files, witnesses and decisions are retained.
"""
import hashlib
import json
import os
import resource
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import notebook_death_gate as gate

P, Q, R = '00010101', '00101010', '01010100'
FIXTURE_SHA256 = 'ef0ff89cfeee5c4f13def41b9df493d76e5b55f358a1487a27296bffbbccdf90'
ROOT = None
LOG = []


def write(name, obj):
    (ROOT / name).write_text(json.dumps(obj, indent=1) + '\n')


def assignment(bits, word, j, encoding):
    """Variable values induced by a physical initial row, mirroring gate.cnf's numbering."""
    h, cells, nv, clauses = gate.cnf(word, j, encoding)
    hist = gate.replay(bits[:h + 1], h)
    val = {cells[t, i]: bool(hist[t][i - 1]) for (t, i) in cells}
    if encoding == 'or':
        aux = len(cells)
        for t in range(h):
            for i in range(1, h - t + 1):
                aux += 1
                val[aux] = bool(hist[t][i - 1] or hist[t][i])
        assert aux == nv
    return clauses, val


def satisfied(clauses, val):
    return all(any(val[abs(v)] == (v > 0) for v in c) for c in clauses)


def controls(latest):
    out = {}
    for word, j in ((P, 98), (R, 99)):
        rec = latest[word]
        assert rec['age'] == j and rec['replayed_literal']
        bits = [int(c) for c in rec['row']]
        for enc in ('table', 'or'):
            clauses, val = assignment(bits, word, j, enc)
            assert satisfied(clauses, val), ('C1 failed', word, j, enc)
            flipped = word[:-1] + ('0' if word[-1] == '1' else '1')
            fclauses, fval = assignment(bits, flipped, j, enc)
            assert not satisfied(fclauses, fval), ('C2 failed', word, j, enc)
            out['%s@%d/%s' % (word, j, enc)] = 'C1 satisfied, C2 violated as required'
    return out


def admit():
    a = resource.getrusage(resource.RUSAGE_SELF)
    b = resource.getrusage(resource.RUSAGE_CHILDREN)
    used = a.ru_utime + a.ru_stime + b.ru_utime + b.ru_stime
    if used >= 210:
        raise RuntimeError('aggregate CPU admission guard (210 s) reached: %.1f s' % used)
    return used


def solve(word, j, enc):
    used = admit()
    h, cells, nv, clauses = gate.cnf(word, j, enc)
    tag = 'q%02d_%s_%d_%s' % (len(LOG) + 1, word, j, enc)
    p = ROOT / tag
    p.mkdir()
    with (p / 'input.cnf').open('w') as f:
        f.write('p cnf %d %d\n' % (nv, len(clauses)))
        for c in clauses:
            f.write(' '.join(map(str, c)) + ' 0\n')

    def limits():
        resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    start = time.monotonic()
    with (p / 'solver.txt').open('w') as f:
        try:
            r = subprocess.run(['kissat', '-q', str(p / 'input.cnf'), str(p / 'proof.drat')],
                               stdout=f, stderr=subprocess.STDOUT, timeout=30, preexec_fn=limits)
            code = r.returncode
        except subprocess.TimeoutExpired:
            code = None
    status = {10: 'SAT', 20: 'UNSAT'}.get(code, 'UNKNOWN')
    rec = dict(query=tag, word=word, visible_index=j, encoding=enc, status=status, returncode=code,
               wall_s=time.monotonic() - start, cpu_used_before_s=used, variables=nv, clauses=len(clauses),
               cnf_sha256=hashlib.sha256((p / 'input.cnf').read_bytes()).hexdigest(),
               witness_checked=False, proof_checked=False)
    if status == 'SAT':
        vals = {}
        for line in (p / 'solver.txt').read_text().splitlines():
            if line.startswith('v '):
                for x in map(int, line[2:].split()):
                    if x:
                        vals[abs(x)] = x > 0
        assert all(any(vals.get(abs(v)) == (v > 0) for v in c) for c in clauses), 'invalid SAT model'
        bits = [int(vals[cells[0, i]]) for i in range(1, h + 2)]
        hist = gate.replay(bits, h)
        assert all(bool(hist[t][i - 1]) == vals[v] for (t, i), v in cells.items()), 'physical cone mismatch'
        assert ''.join(str(hist[2 * (j + k)][0]) for k in range(len(word))) == word
        (p / 'witness.json').write_text(json.dumps(dict(initial_right=''.join(map(str, bits)), outside_right='zero',
                                        visible_trace=''.join(str(hist[t][0]) for t in range(0, h + 1, 2))),
                                        indent=1) + '\n')
        rec['witness_checked'] = True
    LOG.append(rec)
    write('queries.json', LOG)
    print(json.dumps({k: rec[k] for k in ('query', 'status', 'wall_s')}), flush=True)
    return status


def ask(word, j):
    a = solve(word, j, 'table')
    b = solve(word, j, 'or')
    if {a, b} == {'SAT', 'UNSAT'}:
        raise RuntimeError('encoding disagreement on %s@%d: %s vs %s' % (word, j, a, b))
    if a == b == 'SAT':
        return 'ACCEPTED_SAT'
    if a == b == 'UNSAT':
        return 'ACCEPTED_UNSAT (solver-reported; DRAT retained, not checked)'
    return 'UNRESOLVED (%s, %s)' % (a, b)


def main():
    global ROOT
    ROOT = Path(os.environ['CAPPED_OUT']) / 'artifacts'
    ROOT.mkdir(exist_ok=False)
    fixture = Path(sys.argv[1])
    assert hashlib.sha256(fixture.read_bytes()).hexdigest() == FIXTURE_SHA256
    latest = json.loads(fixture.read_text())
    src = dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               gate_sha256=hashlib.sha256(Path(gate.__file__).read_bytes()).hexdigest(),
               fixture_sha256=FIXTURE_SHA256)
    write('controls.json', dict(src, controls=controls(latest)))
    decision = {}
    try:
        decision['P@100'] = ask(P, 100)
        decision['R@100'] = ask(R, 100)
        if decision['P@100'] != 'ACCEPTED_SAT':
            decision['P@99'] = ask(P, 99)
        stop = 'PLAN_COMPLETE'
    except RuntimeError as e:
        stop = 'STOPPED: %s' % e
    implied = {}
    if decision.get('P@100') == 'ACCEPTED_SAT':
        implied = {'P@99': 'by nestedness', 'Q@100': 'by the shift law Q@j <=> P@(j-1)'}
    elif decision.get('P@99') == 'ACCEPTED_SAT':
        implied = {'Q@100': 'by the shift law'}
    gate_closed = (decision.get('P@100') == 'ACCEPTED_SAT' and decision.get('R@100') == 'ACCEPTED_SAT')
    write('result.json', dict(src, decision=decision, implied=implied, gate_closed=gate_closed, stop=stop,
                              calls=len(LOG), proofs_checked=False))
    print(json.dumps(dict(decision=decision, implied=implied, gate_closed=gate_closed, stop=stop)))
    return 0 if stop == 'PLAN_COMPLETE' else 1


if __name__ == '__main__':
    sys.exit(main())
