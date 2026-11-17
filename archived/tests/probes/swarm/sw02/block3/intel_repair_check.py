#!/usr/bin/env python3
"""Validate retained smoke, plus fail-closed dump controls; no repeated lift."""
import os
import contextlib
import io
import runpy
import sys
from pathlib import Path

B = Path(__file__).resolve().parent
old = Path(sys.argv[1]).resolve()
def run(name, args):
    sys.argv = [str(B / name)] + list(map(str, args))
    runpy.run_path(str(B / name), run_name='__main__')
run('intel_validate.py', [old, 'smoke'])
# Its own directory is capped; retained smoke data are read-only inputs.
missing = Path(os.environ['CAPPED_OUT']) / 'missing-dumps'
missing.mkdir()
for name, args, message in [
    ('check_lift.py', ['--targets', B / 'targets.txt', '--mode', 'xx', '--wmax', '16',
                       '--scc', old / 'xx/scc_xx.jsonl', '--dumps', missing], 'missing/truncated dump'),
    ('tails.py', [B / 'control_rows.txt', B.parent, B / 'targets.txt', missing, 'xx', '30'], 'no core dumps')]:
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            run(name, args)
        except AssertionError as exc:
            assert message in str(exc), str(exc)
        else:
            raise AssertionError('missing negative-control rejection: ' + name)
print('PASS: retained smoke, missing-dump mutant and empty-tail mutant')
