#!/usr/bin/env python3
"""GPT's bounded NL certificate audit, GC613.
Run: python3 tests/probes/lexicon/rule30_nl_certificate_audit.py DATA_DIR DRAT_TRIM
Data stays outside git. Regenerate published cones, compare exact hashes,
replay six witnesses with independent list updates, and check both DRAT proofs.
Prediction: all gates pass. Counterfactual: copied verification logs suffice.
Unexpected control: earlier-age witnesses must satisfy all sparse targets.
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path
import rule30_neutral_concat as nl

PAT = '0..00..1....0..1..1..1'
HASHES = {
    'nl_A_LLLLLSS.cnf': '5a411e2eb3f93c8f780fb4368dfd8244d7f4f224fd36f347e17dd23a5a3f4047',
    'nl_A_LLLLLSS.drat': 'd00fbcb1b20c0fb2c1d71d51563244ec796c955feb7eb1064bee17367117d465',
    'nl_P_s6.cnf': '668b4d16520bbc1f7445619845eb38ae36d9a5649aa148f9732ae0e46bcc9db9',
    'nl_P_s6.drat': '10a5d44df30caf0991f38d3b652849b5ca628a3535e06422470c162c0dcd2a6b',
}

def main():
    data, checker = Path(sys.argv[1]), sys.argv[2]
    for name, expected in HASHES.items():
        assert hashlib.sha256((data / name).read_bytes()).hexdigest() == expected, name
    print('Four supplied artifact hashes PASS')
    cons, horizon = nl.targets('LLLLLSS', 'A', 0)
    text, _ = nl.cnf_text(cons, horizon)
    assert text.encode() == (data / 'nl_A_LLLLLSS.cnf').read_bytes()
    cons = [(2*(6+k), 1, int(c)) for k, c in enumerate(PAT) if c != '.']
    text, _ = nl.cnf_text(cons, max(t for t, _, _ in cons))
    assert text.encode() == (data / 'nl_P_s6.cnf').read_bytes()
    print('Both regenerated cones byte-identical PASS')
    witnesses = re.findall(r's0 ([0-5]): ([01]+)', (data / 'README-nl-cert.txt').read_text())
    assert sorted(int(s) for s, _ in witnesses) == list(range(6))
    for start, bits in witnesses:
        start = int(start)
        horizon = 2*(start + len(PAT)-1)
        row = [0] + [int(c) for c in bits] + [0]*(horizon+2)
        trace = []
        for t in range(horizon+1):
            if t % 2 == 0:
                trace.append(row[1])
            if t < horizon:
                row = [(t+1) % 2] + [row[i-1] ^ (row[i] | row[i+1]) for i in range(1,len(row)-1)] + [0]
        assert all(c == '.' or trace[start+k] == int(c) for k,c in enumerate(PAT)), start
    print('Six earlier-age witnesses independent replay PASS')
    for stem in ('nl_A_LLLLLSS', 'nl_P_s6'):
        result = subprocess.run([checker, str(data/(stem+'.cnf')), str(data/(stem+'.drat'))], capture_output=True, text=True, timeout=60)
        (data/(stem+'.gpt-verification.txt')).write_text(result.stdout + result.stderr)
        assert result.returncode == 0 and re.search(r'^s VERIFIED\s*$', result.stdout, re.M), stem
        print(stem, 'independent DRAT verification PASS')
    print('ALL CHECKS PASS')

if __name__ == '__main__':
    main()
