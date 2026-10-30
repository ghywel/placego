#!/usr/bin/env python3
"""assemble_finite_past_essay.py (Local, L1233): bind the officially checked finite-past source (plain form, GC2302) into the essay prose.

The source is embedded once as a Wolfram Language string (JSON escaping: the source has no backslash, tab or other
control character, so only quotes and newlines are escaped). abstract.txt is the front matter's Abstract line.
`--check` verifies the committed essay.md and abstract.txt without writing."""
from pathlib import Path
import hashlib, json, re, sys
root = Path(__file__).resolve().parents[3]
folder = root / 'reports/wolfram-agents/submissions/finite-past'
check = '--check' in sys.argv[1:]
SOURCE = '33c82f323c6629dce45206087bedac12f1fc69ca1e2c4a64f65332da8b525d99'
PROSE = '6b3783f1a896f2dd97611f8c5adeef3e602a528f6afd5f06d77ae2d6a89f8dbe'
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
