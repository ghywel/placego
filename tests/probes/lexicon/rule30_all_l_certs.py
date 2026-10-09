#!/usr/bin/env python3
"""rule30_all_l_certs.py: ALC, DRAT-checked certificates for the all-L slab's fixed UNSAT cases (GPT's GC746 asks for
the two K = 10 cases; L387's loop-5 case and GC744's four columns are added). Local's run (chat L388), with these
predictions pushed before it.

RUN-ON:     cpu (Python 3, kissat, drat-trim; NL's cone via rule30_all_l_slab_sat.py); a minute
COMMAND:    python3 tests/probes/lexicon/rule30_all_l_certs.py [OUTDIR]

Each case is ALX's exact query (NL's mode-A cone, entrance 111001, the visible word L^K and its closing 1, and one clause
saying that some named cell of loop k differs from the 155-ring's). The CNF is written to OUTDIR (default
~/np-scratch-int/rule30-al, outside git: no data files in the repository), kissat writes a DRAT proof, and drat-trim
checks it. The CNF's SHA-256 is printed, so anyone can rebuild it from this script and compare.
  C10-3: K = 10, loop 3, sites 5 .. 6 (GC746: sites 5 .. 6 from time 30 in any infinite all-L history).
  C10-2: K = 10, loop 2, site 5 (GC746: site 5 from time 20).
  C7-5:  K = 7, loop 5, sites 5 .. 6 (L387: five L's behind, one ahead).
  C2-0:  K = 2, loop 0, sites 2 .. 4 (GPT's GC744, the four columns).

PREDICTIONS (Local's, published before the run): ALC-P1, all four instances are UNSAT and drat-trim prints
s VERIFIED for each (confidence 0.9; each was already UNSAT without a proof in ALX/ALF).
OUTCOME: not yet run.
"""
import hashlib
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rule30_all_l_slab_sat as alx                                   # noqa: E402
import rule30_neutral_concat as nl                                    # noqa: E402

CASES = [('C10-3', 10, 3, (5, 6)), ('C10-2', 10, 2, (5,)), ('C7-5', 7, 5, (5, 6)), ('C2-0', 2, 0, (2, 3, 4))]


def cnf(K, k, sites, ref):
    cons, Tend = nl.targets('L' * K, 'A', 0)
    cons = cons + [(0, i, v) for i, v in zip(range(2, 7), (1, 1, 0, 0, 1))]
    body, ncl, nv, off, width = nl.base(Tend, max(max(sites), 6, max(i for _, i, _ in cons)))
    lits = [(-(off[10 * k + s] + i) if ref[(s, i)] else off[10 * k + s] + i) for s in range(10) for i in sites]
    units = ['%d 0' % (off[t] + i if v else -(off[t] + i)) for t, i, v in cons] + [' '.join(map(str, lits)) + ' 0']
    return 'p cnf %d %d\n' % (nv, ncl + len(units)) + body + '\n'.join(units) + '\n'


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/np-scratch-int/rule30-al')
    os.makedirs(out, exist_ok=True)
    ref = alx.ring_cols(8)
    allok = True
    for name, K, k, sites in CASES:
        text = cnf(K, k, sites, ref)
        path, proof = os.path.join(out, name + '.cnf'), os.path.join(out, name + '.drat')
        with open(path, 'w') as f:
            f.write(text)
        r = subprocess.run(['kissat', '-q', '-f', '--no-binary', '--time=3600', path, proof], capture_output=True, text=True)
        v = subprocess.run(['drat-trim', path, proof], capture_output=True, text=True)
        verified = r.returncode == 20 and any(l.strip() == 's VERIFIED' for l in v.stdout.splitlines())
        allok &= verified
        print('%s: K = %d, loop %d, sites %s: kissat %s, drat-trim %s; cnf sha256 %s, proof %d bytes' % (
            name, K, k, sites, {20: 'UNSAT', 10: 'SAT'}.get(r.returncode, r.returncode),
            'VERIFIED' if verified else 'NOT VERIFIED', hashlib.sha256(text.encode()).hexdigest()[:16],
            os.path.getsize(proof)), flush=True)
    print('ALC-P1', 'HELD' if allok else 'REFUTED')
    print('COMPLETE')


if __name__ == '__main__':
    main()
