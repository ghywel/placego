#!/usr/bin/env python3
"""L1031: exact witness delay by left-permutive back-solving; the three remaining short-word questions.

Local, 2026-10-27. Source for GPT's review; it runs only after GPT freezes it, under run_capped.py (CAPPED_OUT set).
No solver, no random sampling. GC1977's conventions: visible index j is physical time 2j, the wall is
x(t,0) = t mod 2, and the right cone starts at cells 1 .. H+1.

Idea (from the possible-pasts discussion, GC1981 and GC1982, applied to our test). A row X at time 0 shows word w at
visible ages a .. a+7. Any row X' whose clamped evolution reaches X at physical time 2 shows w at ages a+1 .. a+8,
because two updates restore the wall phase (GC1977's restart lemma, read backwards). X' is found exactly.
  - Rule 30 is left-permutive: x(t, j-1) = x(t+1, j) XOR (x(t, j) OR x(t, j+1)).
  - From a target row Y with n cells, choose the predecessor's two rightmost cells (positions n, n+1) in 4 ways.
  - Solve leftwards uniquely down to cell 1.
  - Keep the candidate if the wall equation at cell 1 holds: Y(1) = wall(t) XOR (x(1) OR x(2)).
Two such steps (wall values 1, then 0) give at most 16 candidates. Every survivor is checked forward by GC1977's
literal evaluator (notebook_death_gate.replay). A step with no valid candidate means this particular witness row
has no predecessor in the clamped system. That is a fact about that row, not a death.

Targets (GC1983's reduction, checked by Local in L1031). E_34^8 has 28 words: 25 witnessed at 100 in L1030, plus
  P = 00010101 (retained witness at 98), Q = 00101010 (retained witness at 99: the same row), and
  R = 01010100 (retained witness at 99).
One delay of the P/Q row gives P@99 and Q@100. Two delays give P@100. One delay of the R row gives R@100. If all
three succeed, every word of E_34^8 has a replayed age-100 witness, and the gate E_34^8 = E_100^8 closes.

Predictions, written before any run.
  B_A (instrument). The back-solver's candidate set equals the brute-force predecessor set for every target row of
      width 8, under both wall phases, checked exhaustively over all 2^9 predecessor rows. A delayed witness of
      the fixed control 00001000@100 replays to 00001000@101.
  B_B (the question). All three succeed: P@99, Q@100, P@100 and R@100 get replayed witnesses, and the gate closes.
      This is GC1983's rare-survivor reading, reached by an exact route. Gut confidence: about 75%.
  Counterfactual. A retained row has no two-step predecessor at some step. The word is then still possible (other
      rows may work), and only that witness cannot be delayed. It is reported as such, and the word stays UNRESOLVED
      for GC1983's proposed SAT stage. No death is inferred.
GC1985 review amendments: keep all intermediate candidates (at most 256); verify each full one-step reconstruction;
add a guaranteed nonempty constructed positive control; bind full input SHA256; retain all candidate rows and cell-1 traces.
Unexpected check: candidate truncation must not silently discard a second-delay success. No pruning is used.
Caps (frozen in the accompanying GC1985 plan): 60 CPU s, 120 wall s, 256 MiB RSS, 16 MiB disk; one process; retain every candidate and replay.
"""
import hashlib
import itertools
import json
import os
import resource
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import notebook_death_gate as gate
import notebook_witness_pilot as pilot  # frozen CONTROL_ROW (GC1978 q00002)

NW = 8
LATEST_SHA256 = 'ef0ff89cfeee5c4f13def41b9df493d76e5b55f358a1487a27296bffbbccdf90'

def checkpoint():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    if usage.ru_utime + usage.ru_stime > 55:
        raise RuntimeError('55-second stage CPU admission guard')

FIX = {  # retained in cited/l1030-witness-pilot/latest_witnesses.json (literal replay True there)
    'PQ': ('00010101', 98, '846ed258b0a3'),
    'R': ('01010100', 99, '376101d1554f'),
}


def fwd(x, t):
    """One clamped update of a cone row x (cells 1..n as x[0..n-1]); returns n-1 cells."""
    return [gate.TABLE[4 * (t % 2 if i == 0 else x[i - 1]) + 2 * x[i] + x[i + 1]] for i in range(len(x) - 1)]


def back(y, t):
    """All x (n+1 cells) with fwd(x, t) == y (n cells)."""
    n = len(y)
    out = []
    for a, b in itertools.product((0, 1), repeat=2):
        x = [0] * (n + 1)
        x[n - 1], x[n] = a, b
        for j in range(n - 1, 0, -1):          # x[j-1] from y[j], x[j], x[j+1]
            x[j - 1] = y[j] ^ (x[j] | x[j + 1])
        if y[0] == (t % 2) ^ (x[0] | x[1]):
            out.append(x)
    return out


def delay(row):
    """All rows X' with two clamped updates (wall phases 0 then 1) taking X' to row."""
    res = []
    checkpoint()
    for x1 in back(row, 1):
        assert fwd(x1, 1) == row
        for x0 in back(x1, 0):
            assert fwd(x0, 0) == x1
            res.append(x0)
    assert len(res) <= 16
    return res


def visible(row, a):
    h = 2 * (a + NW - 1)
    assert len(row) >= h + 1
    hist = gate.replay(row[:h + 1], h)
    return ''.join(str(hist[2 * (a + k)][0]) for k in range(NW))


def exhaustive_control():
    checks = 0
    for t in (0, 1):
        for y in itertools.product((0, 1), repeat=8):
            y = list(y)
            got = sorted(map(tuple, back(y, t)))
            brute = sorted(x for x in itertools.product((0, 1), repeat=9) if fwd(list(x), t) == y)
            assert got == brute, (t, y)
            checks += 1
    return checks


def main():
    root = Path(os.environ['CAPPED_OUT']) / 'artifacts'
    root.mkdir(exist_ok=False)
    src = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    LATEST = Path(sys.argv[1])  # cited/l1030-witness-pilot/latest_witnesses.json, read back from the store
    raw = LATEST.read_bytes()
    assert len(raw) <= 65536 and hashlib.sha256(raw).hexdigest() == LATEST_SHA256
    lw = json.loads(raw)
    rec = dict(source_sha256=src, gate_sha256=hashlib.sha256(Path(gate.__file__).read_bytes()).hexdigest(),
               pilot_sha256=hashlib.sha256(Path(pilot.__file__).read_bytes()).hexdigest(),
               latest_witnesses_sha256=hashlib.sha256(LATEST.read_bytes()).hexdigest())
    rec['exhaustive_back_checks'] = exhaustive_control()
    # control: delay the frozen age-100 control row by one visible step
    ctrl = [int(c) for c in pilot.CONTROL_ROW]
    assert visible(ctrl, 100) == '00001000'
    dc = delay(ctrl)
    rec['control_candidates'] = len(dc)
    rec['control_delayed_ok'] = any(visible(x, 101) == '00001000' for x in dc)
    # Delayability of the fixed witness is a prediction, not an instrument axiom.
    # Build a guaranteed positive by moving a known row forward before reversing it.
    target = fwd(fwd(ctrl, 0), 1)
    constructed = delay(target)
    assert ctrl in constructed
    rec['constructed_control_candidates'] = len(constructed)
    rec['constructed_control_recovers_original'] = True
    assert all(visible(x, 101) == '00001000' for x in dc)
    rec['control_rows'] = [''.join(map(str, x)) for x in dc]
    results = {}
    for tag, (w, a, sha12) in FIX.items():
        row_s = lw[w]['row']
        assert lw[w]['age'] == a and hashlib.sha256(row_s.encode()).hexdigest()[:12] == sha12
        row = [int(c) for c in row_s]
        assert len(row) == 215 and set(row_s) <= {'0', '1'}
        assert visible(row, a) == w
        steps = {}
        frontier = [row]
        for k in (1, 2) if tag == 'PQ' else (1,):
            nxt = []
            for r in frontier:
                nxt.extend(delay(r))
            assert len(nxt) <= 16 ** k
            ok = []
            traces = []
            for x in nxt:
                if tag == 'PQ':
                    good = visible(x, a + k) == w and (k != 1 or visible(x, 100) == '00101010')
                else:
                    good = visible(x, a + k) == w
                assert good, (tag, k)
                ok.append(''.join(map(str, x)))
                traces.append(''.join(str(r[0]) for r in gate.replay(x, len(x) - 1)))
            steps[a + k] = dict(candidates=len(ok), rows=ok, full_cell1_traces=traces)
            frontier = [[int(c) for c in s] for s in ok]
            if not ok:
                break
        results[tag] = dict(word=w, start_age=a, steps=steps)
    rec['results'] = results
    pq, r = results['PQ']['steps'], results['R']['steps']
    rec['P99_Q100'] = pq.get(99, {}).get('candidates', 0) > 0
    rec['P100'] = pq.get(100, {}).get('candidates', 0) > 0
    rec['R100'] = r.get(100, {}).get('candidates', 0) > 0
    rec['B_A_fixed_delay_prediction'] = rec['control_delayed_ok']
    rec['negative_scope'] = 'Empty frontier rules out extending these retained rows only; no word absence inferred.'
    rec['gate_closed'] = rec['P99_Q100'] and rec['P100'] and rec['R100']
    (root / 'result.json').write_text(json.dumps(rec, indent=1))
    print(json.dumps({k: rec[k] for k in ('exhaustive_back_checks', 'control_candidates', 'control_delayed_ok',
                                          'P99_Q100', 'P100', 'R100', 'gate_closed')}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
