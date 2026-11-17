#!/usr/bin/env python3
"""Meta-controls for S0 revision 2's client fault controls (Local, 2026-10-24, L877): each control must FAIL when the client defect it
guards is planted. Three plants, each in a fresh interpreter state: (1) the write-all loop writes once and stops; (2) the run-wide
cleanup closes nothing; (3) the stream check reports silence whatever is buffered or closed. No GPU. Usage: python3 s0_client_meta.py
OUTCOME (Local, 2026-10-24, first run, unsupervised development check): CLIENT META PASS 3. Each plant made exactly its guarded
controls fail (single_write: short_writes_complete; no_cleanup: forced_failure_closes_live_server; always_silent:
trailing_partial_bytes_detected and early_eof_is_not_silence) while every other client control still passed."""
import importlib, json, os, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def fresh():
    import s0_serve_controls as S
    return importlib.reload(S)


def plant_single_write(S):
    def send(self, data, deadline):
        os.write(self.p.stdin.fileno(), bytes(data[:1 << 16])); self.writes += 1; return 'ok'
    S.Server.send = send


def plant_no_cleanup(S):
    S.close_all = lambda: []


def plant_always_silent(S):
    S.Server.quiet = lambda self: 'silence'


PLANTS = {   # plant -> the controls that must fail under it
    'single_write': (plant_single_write, ['short_writes_complete']),
    'no_cleanup': (plant_no_cleanup, ['forced_failure_closes_live_server']),
    'always_silent': (plant_always_silent, ['trailing_partial_bytes_detected', 'early_eof_is_not_silence']),
}

if __name__ == '__main__':
    out = {}
    for name, (plant, must_fail) in PLANTS.items():
        S = fresh(); plant(S)
        with tempfile.TemporaryDirectory() as t:
            r = S.client_controls(t)
        S.close_all() if hasattr(S, 'close_all') else None
        for x in list(S.LIVE): x.close()
        out[name] = {'must_fail': must_fail, 'failed': [k for k in must_fail if r.get(k) is False],
                     'others_still_pass': sorted(k for k, v in r.items() if not k.startswith('_') and k not in must_fail and v is True)}
    ok = all(len(v['failed']) == len(v['must_fail']) for v in out.values())
    print(json.dumps(out, indent=1)); print('CLIENT META', 'PASS' if ok else 'FAIL', len(out)); sys.exit(0 if ok else 1)
