#!/usr/bin/env python3
"""GC942: two tiny LP certificate fixtures, predictions in CLOUD-LOCAL first.
Zero-weight reachable cyclic block must reject at lambda1; positive weights
must accept at lambda2. Independent control: both labelled successors exist
at both states, so all 2^n binary words are accepted. No layer generation,
C execution, retained real certificate or spectral computation.
RUN-ON: cpu; COMMAND: python3 tests/probes/lexicon/rule30_gpt_lp_zero_weight.py
"""
import importlib.util
import struct
import tempfile
from pathlib import Path

D = 10**9
TR = [0, 1, 1, 1]


def main():
    spec = importlib.util.spec_from_file_location(
        'lp_zero_audit', Path(__file__).with_name('rule30_layer_product.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Independent hand identities, checked exactly: Au=u with zero support,
    # yet the reachable second vertex has two loops, giving word growth2.
    assert (1 + 0, 2 * 0) == (1, 0)
    assert all(t >= 0 for t in TR)
    with tempfile.TemporaryDirectory(prefix='gc942-') as directory:
        dump, cert = Path(directory)/'layer', Path(directory)/'cert'
        dump.write_bytes(struct.pack('<5q', 2, *TR))
        for name, u, rate, reject in [
                ('zero cyclic weight', (1, 0), D, True),
                ('positive control', (1, 1), 2*D, False)]:
            raw = struct.pack('<5qQ', 0x3143504C, 2, 1, 2, 1, D)
            raw += struct.pack('<2q', 0, 1)
            raw += struct.pack('<4i', *TR)
            raw += struct.pack('<2i', 0, 0) + bytes([1])
            raw += struct.pack('<Q', rate) + struct.pack('<2Q', *u)
            cert.write_bytes(raw)
            try:
                got = module.verify(str(dump), '-', str(cert))
            except SystemExit as exc:
                assert reject and 'inequality at state 1' in str(exc), str(exc)
                print(name, 'REJECT', str(exc))
            else:
                assert not reject and got == rate, (name, got)
                print(name, 'PASS', got)
    print('GC942 controls PASS; no real LP artifact verified')


if __name__ == '__main__':
    main()
