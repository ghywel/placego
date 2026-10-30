#!/usr/bin/env python3
"""GC2302: deterministic plain submission assembly; no Lean/Wolfram execution.

The five pinned preparation files are concatenated after removing only the
listed module/import/public-section lines. The shared namespace bodies and
seven public types stay unchanged. Historical preparation comments are retained
to match the exact plain form examined in L1230. The frozen official stage
remains pending; this script does not run Lean.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'reports/wolfram-agents/submissions/finite-past'
SOURCES = [
    ('Rule30FinitePastDraft.lean', 'a46243a1ac7ed1732f6bbce9986c9434152f934c1e3d62ec251dee3e8c0acf3f',
     ['Ruliology.CellularAutomata.Rule30Realization']),
    ('FiniteParentCriterionDraft.lean', '165e917e7b9265c37b85493641d20fd1bf6dbbc58135c4c8deb9316ce3c9fd67',
     ['Rule30FinitePastDraft']),
    ('NormalizedFinitePastDraft.lean', '4cbba36a4c5e4393ad6f7d964ddfba9ad6e6bb25986b399987514762d231fe43',
     ['Rule30FinitePastDraft']),
    ('FinitePastCountDraft.lean', '230e7f0efcb4364b297bb0dd14f08c3ea3d250ca2b138317ee9b0c3350ec84f6',
     ['NormalizedFinitePastDraft']),
    ('SubmissionHeadlinesDraft.lean', '3375871f2a29a1b484d511608a66fe41dda6502efc78dad0f933b79a57c4742b',
     ['Ruliology.CellularAutomata.Rule30Prize', 'FiniteParentCriterionDraft', 'FinitePastCountDraft']),
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    output = ('import Ruliology.CellularAutomata.Rule30Prize\n'
              'import Ruliology.CellularAutomata.Rule30Realization\n\n'
              '/-! Prepared single-file source, GC2295. UNCOMPILED; not a checker receipt. -/\n'
              '').encode()
    rows = []
    for name, expected, imports in SOURCES:
        raw = (BASE / name).read_bytes()
        if digest(raw) != expected:
            raise SystemExit('Source digest changed: ' + name)
        lines = raw.decode('utf-8').splitlines(keepends=True)
        removed = [line.rstrip('\n') for line in lines
                   if line == 'module\n' or line.startswith('public import ')
                   or line == '@[expose] public section\n']
        wanted = ['module'] + ['public import ' + item for item in imports] + ['@[expose] public section']
        if removed != wanted:
            raise SystemExit('Administrative-line mismatch: ' + name)
        body = ''.join(line for line in lines
                       if line.rstrip('\n') not in wanted).encode('utf-8')
        marker = ('\n/- BEGIN carrying body: ' + name + ' -/\n').encode()
        output += marker
        offset = len(output)
        output += body
        rows.append({'path': name, 'input_sha256': expected, 'body_sha256': digest(body),
                     'body_offset_bytes': offset, 'body_length_bytes': len(body),
                     'removed_lines': removed})
    for row in rows:
        a = row['body_offset_bytes']; b = a + row['body_length_bytes']
        assert digest(output[a:b]) == row['body_sha256']
    manifest = {'checkpoint': 'GC2302', 'status': 'PLAIN_SOURCE_ASSEMBLY_FROZEN_OFFICIAL_STAGE_PENDING',
                'output': 'Rule30Submission.lean', 'output_sha256': digest(output),
                'output_bytes': len(output), 'bodies': rows}
    (BASE / 'Rule30Submission.lean').write_bytes(output)
    (BASE / 'assembly.json').write_text(json.dumps(manifest, indent=2) + '\n')
    assert (BASE / 'Rule30Submission.lean').read_bytes() == output
    print('ASSEMBLED_PLAIN_OFFICIAL_PENDING', digest(output), len(output), 'bytes;', len(rows), 'bodies verified')


if __name__ == '__main__':
    main()
