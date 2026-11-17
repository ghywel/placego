#!/usr/bin/env python3
"""CL603 source-binding and tiny negative-control audit, GPT, 2026-10-23.

Record searched: stateCheck|explicit_sound|neg_missing_root (14 hits, 5 files).
Prediction: inherited proof bodies and pilot section 7 agree; the essay embeds
the exact module; three mutated width-6 targets fail literal cell evolution.
Can fail: a missing/misindexed state theorem, inconsistent embedding, mutation
that does not remove a required image, or literal/packed transition mismatch.
Unexpected check: neg_missing_root is positive, not a missing-root negative;
zero scanned words accept vacuously, so the formal coverage premise matters.
Scope: no width-14 DFA regeneration or closure replay, no Lean execution.
Caps: 15 CPU seconds, 15 seconds checked wall time, inputs <= 8 MiB each,
at most 1024 literal width-6 transitions, output < 8 KiB. Stop on any failure;
no patch-and-retry. Memory is bounded by these fixed small reads, not profiled.

OUTCOME (2026-10-23, sole run): PASS source/essay/generic-prefix bindings,
919 range leaves and 918 splits; 263 literal/packed transition checks.
Dead witness (1,0,0,4), swap and dropped-bit witnesses (0,0,0,1);
dropped bit 1. neg_missing_root is positive. No full width-14 replay.
Only this outcome comment was appended after execution.
"""
import ast
import hashlib
import json
from pathlib import Path
import re
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (15, 15))
start = time.monotonic()
base = Path(__file__).resolve().parents[2] / 'reports/wolfram-agents/submissions'


def read(path):
    assert path.stat().st_size <= 8 * 1024**2
    return path.read_text()


full = read(base / 'channel-14/Rule30Submission.lean')
pilot = read(base / 'channel-14/Pilot6.lean')
old = read(base / 'channel-12/Rule30Submission.lean')
body = lambda s: s[s.index('namespace Rule30Submission'):]
assert body(full).split('/-! ## 7.')[0] == body(old).split('/-! ## 6.')[0]
assert body(full).split('/-! ## 8.')[0] == body(pilot).split('/-! ## 8.')[0]
tpl = read(base / 'channel-14/essay-template.md')
essay = read(base / 'channel-14/essay.md')
assert tpl.count('@@LEAN_SOURCE@@') == 1
assert tpl.replace('@@LEAN_SOURCE@@', full.rstrip('\n') + '\n') == essay
assert '"' not in full and '\\' not in full
digest = hashlib.sha256(full.encode()).hexdigest()
assert digest in read(base / 'channel-14/README.md')
receipt = json.loads(read(base / 'channel-14/check.json'))
assert receipt['verdict'] == 'pass' and receipt['replay'] == {'constants': 3961, 'ok': True}
assert receipt['newAxioms'] == [] and len(receipt['headlines']) == 8
assert all(h['ok'] and h['found'] and h['typeMatches'] for h in receipt['headlines'])
assert [int(x) for x in re.findall(r'^theorem s14_(\d+) :', full, re.M)] == list(range(919))
leaf = re.findall(r'^theorem r14_(\d+)_(\d+) :.* := range_one (\d+) s14_(\d+)$', full, re.M)
assert len(leaf) == 919
for a,b,c,d in leaf:
    assert int(a) == int(c) == int(d) and int(b) == int(a)+1
splits = re.findall(r'^theorem r14_(\d+)_(\d+) :.* := range_split (\d+) (\d+) (\d+) r14_(\d+)_(\d+) r14_(\d+)_(\d+)$', full, re.M)
assert len(splits) == 918
known = {(int(a),int(b)) for a,b,_,_ in leaf}
for row in splits:
    lo,hi,a,mid,b,l,m,m2,h = map(int,row)
    assert lo == a == l and hi == b == h and mid == m == m2
    assert (lo,mid) in known and (mid,hi) in known
    known.add((lo,hi))
assert (0,919) in known

# Parse only the tiny pilot tree; the 4.5 MB width-14 bitsets are not replayed.
line = next(l for l in pilot.splitlines() if l.startswith('def T6 :'))
tokens = re.findall(r'BTree\.node|BTree\.leaf|\d+', line.split(':=',1)[1])
it = iter(tokens)
def tree():
    t = next(it)
    if t == 'BTree.leaf':
        return int(next(it))
    assert t == 'BTree.node'
    return (tree(),tree())
t = tree()
assert list(it) == []
def look(i):
    q = t
    while isinstance(q,tuple):
        q,i = q[i % 2],i//2
    return q
sets = [look(i) for i in range(31)]
succ_line = next(l for l in pilot.splitlines() if l.startswith('def succ6 :'))
succ = ast.literal_eval(succ_line.split(':=',1)[1].strip())
assert succ[1] == (3,4) and sets[0] == (1<<64)-1
mutant = int(re.search(r'neg_drop : stateCheck 63 32 (\d+)',pilot).group(1))
removed = sets[3] ^ mutant
assert mutant & ~sets[3] == 0 and removed.bit_count() == 1
calls = 0
def image(s,u,v):
    global calls
    calls += 1
    assert calls <= 1024
    cells = [(s>>k)&1 for k in range(6)]
    for clock,exterior in ((0,u),(1,v)):
        cells = [(cells[k-1] if k else clock) ^
                 (cells[k] | (cells[k+1] if k<5 else exterior)) for k in range(6)]
    out = sum(x<<k for k,x in enumerate(cells))
    def packed(s,clock,exterior):
        return ((s<<1 | clock) ^ (s | s>>1 | exterior<<5)) & 63
    assert out == packed(packed(s,0,u),1,v)
    return out
def violation(source,targets):
    for s in range(64):
        if source>>s & 1:
            for u in range(2):
                for v in range(2):
                    z=image(s,u,v)
                    if not targets[s%2]>>z & 1:
                        return [s,u,v,z]
    return None
results = {}
for name,targets in [('dead',(sets[3],0)),('swap',(sets[4],sets[3])),('drop',(mutant,sets[4]))]:
    results[name] = violation(sets[1],targets)
    assert results[name] is not None
assert violation(sets[0],(sets[1],sets[2])) is None
assert re.search(r'neg_missing_root : .* = true := by decide \+kernel',pilot)
assert time.monotonic()-start < 15
print(json.dumps({'source_sha256':digest, 'bindings':'PASS', 'range_leaves':919,
                  'range_splits':918, 'negative_witnesses_s_u_v_image':results,
                  'dropped_bit':removed.bit_length()-1, 'literal_transition_checks':calls,
                  'neg_missing_root':'positive root control only',
                  'receipt':'Cloud pass read, not independently replayed'},indent=2))
