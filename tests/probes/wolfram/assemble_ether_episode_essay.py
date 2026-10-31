#!/usr/bin/env python3
"""assemble_ether_episode_essay.py (Local, L1267): bind the officially checked M(k) portal source into the essay.

As assemble_gate_clocks_nested_essay.py (L1248): the source is embedded once as a Wolfram Language string (JSON
escaping: the source has no backslash, tab or other control character, so only quotes and newlines are escaped), and
the front matter's Abstract line becomes abstract.txt. `--check` verifies the committed essay.md and abstract.txt
without writing. PROSE is pinned when the essay prose is frozen.
"""
from pathlib import Path
import hashlib, json, re, sys
root = Path(__file__).resolve().parents[3]
folder = root / 'reports/wolfram-agents/submissions/ether-episode'
check = '--check' in sys.argv[1:]
SOURCE = '37733e44c5febb72abb0fd214a9839ca564f4f7ce55a4cbe566d42ee18cb584e'
PROSE = 'PINNED-WHEN-FROZEN'
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
print('abstract', hashlib.sha256((abstract + '\n').encode()).hexdigest(), len(abstract), 'characters,',
      len(abstract.split()), 'words')
