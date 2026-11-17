#!/usr/bin/env python3
"""assemble_gate_clocks_essay.py (Local, L1221): bind the officially checked gate-clock source into the essay prose.

The source is embedded once as a Wolfram Language string (JSON escaping: the source has no backslash, tab or other
control character, so only quotes and newlines are escaped). abstract.txt is the front matter's Abstract line.
`--check` verifies the committed essay.md and abstract.txt without writing."""
from pathlib import Path
import hashlib, json, re, sys
root = Path(__file__).resolve().parents[3]
folder = root / 'reports/wolfram-agents/submissions/gate-clocks'
check = '--check' in sys.argv[1:]
SOURCE = '14372c1de82d95341d0d79d4101552683f8b24e9be332712da44600d8b262eb6'
PROSE = 'e92bf6adddd0153244910ad10284bfc6a12bce8bf3486f9e443595ee46aee3f2'
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
