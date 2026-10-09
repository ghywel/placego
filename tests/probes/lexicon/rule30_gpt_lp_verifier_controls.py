#!/usr/bin/env python3
"""GC887: tiny synthetic certificate controls of the separately written LP verifier.
RUN-ON: cpu, Python3; COMMAND: python3 tests/probes/lexicon/rule30_gpt_lp_verifier_controls.py
Predictions in CLOUD-LOCAL before execution: loops/bridge/acyclic valid; false
split of a two-cycle rejected. Countercontrol: no actual large certificate is
verified. OUTCOME: all six fixtures pass their expected acceptance/rejection.
Temporary binary fixtures stay outside git; no layer generation or spectral run.
"""
import importlib.util
import struct
import tempfile
from pathlib import Path

D = 10**9


def main():
    path = Path(__file__).with_name('rule30_layer_product.py')
    spec = importlib.util.spec_from_file_location('lp_audit', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with tempfile.TemporaryDirectory(prefix='gc887-') as directory:
        def check(name, tr, cc, cy, R, u, answer=None, reject=None):
            n = len(cc)
            dump, cert = Path(directory)/'layer', Path(directory)/'cert'
            dump.write_bytes(struct.pack('<q', n) + struct.pack('<%dq' % len(tr), *tr))
            raw = struct.pack('<5qQ', 0x3143504C, n, 1, n, len(cy), D)
            raw += struct.pack('<%dq' % n, *range(n))
            raw += struct.pack('<%di' % len(tr), *tr)
            raw += struct.pack('<%di' % n, *cc) + bytes(cy)
            raw += struct.pack('<%dQ' % len(R), *R) + struct.pack('<%dQ' % n, *u)
            cert.write_bytes(raw)
            try:
                got = module.verify(str(dump), '-', str(cert))
            except SystemExit as exc:
                assert reject and reject in str(exc), (name, str(exc))
                print(name, 'REJECT', str(exc))
            else:
                assert reject is None and got == answer, (name, got)
                print(name, 'PASS', got)
        check('two labels one loop', [0,0], [0], [1], [2*D], [1], answer=2*D)
        check('multiplicity tamper', [0,0], [0], [1], [D], [1], reject='inequality')
        check('one-way bridge', [0,1,1,-1], [1,0], [1,1], [D,D], [1,1], answer=D)
        check('one block two-cycle', [1,-1,0,-1], [0,0], [1], [D], [1,1], answer=D)
        check('false split two-cycle', [1,-1,0,-1], [1,0], [0,0], [0,0], [0,0], reject='cross-block')
        check('finite acyclic', [1,-1,-1,-1], [1,0], [0,0], [0,0], [0,0], answer=0)
    print('GC887 synthetic verifier controls PASS; no large certificate replay')


if __name__ == '__main__':
    main()
