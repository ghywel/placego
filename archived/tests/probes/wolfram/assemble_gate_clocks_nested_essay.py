#!/usr/bin/env python3
"""assemble_gate_clocks_nested_essay.py (Local, L1248): bind the officially checked nested source into the essay.

The source is embedded once as a Wolfram Language string (JSON escaping: the source has no backslash, tab or other
control character, so only quotes and newlines are escaped). abstract.txt is the front matter's Abstract line.
`--check` verifies the committed essay.md and abstract.txt without writing."""
from pathlib import Path
import hashlib, json, re, sys
root = Path(__file__).resolve().parents[3]
folder = root / 'reports/wolfram-agents/submissions/gate-clocks-nested'
check = '--check' in sys.argv[1:]
SOURCE = '5c2e96a50add3b75e45e677a7e5f4d6a51ae1822db34c124002499c0bc5f54d5'
PROSE = '14c2cf375c777711c172a1c1ed960675ec2eaeb8da429155473827de21d44fb2'
src = (folder / 'Rule30Submission.lean').read_bytes()
assert hashlib.sha256(src).hexdigest() == SOURCE, 'source differs from the officially checked one'
prose_data = (folder / 'essay-prose.md').read_bytes()
assert hashlib.sha256(prose_data).hexdigest() == PROSE, 'essay prose differs from the pinned one'
s, prose = src.decode(), prose_data.decode()
assert '\\' not in s and not any(ord(c) < 32 and c != '\n' for c in s)
assert prose.count('%%LEAN%%') == 1
abstract = re.search(r'^Abstract: (.*)$', prose, re.M).group(1)
essay = prose.replace('%%LEAN%%', json.dumps(s, ensure_ascii=False)[1:-1])
for name, text in [('essay.md', essay), ('abstract.txt', abstract + '\n')]:
    if check:
        assert (folder / name).read_text() == text, name + ' differs'
    else:
        (folder / name).write_text(text)
print('essay', hashlib.sha256(essay.encode()).hexdigest(), len(essay.encode()))
