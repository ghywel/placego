#!/usr/bin/env python3
"""assemble_ether_episode_essay.py (Local, L1267): bind the officially checked M(k) portal source into the essay.

As assemble_gate_clocks_nested_essay.py (L1248), but the source is embedded verbatim as a multi-line Wolfram Language
string, because MarkdownToNotebook iconizes the `(*Iconize["Lean source"]*)` marker only for a multi-line literal, not
for one line with escaped newlines (tested, L1269). That is safe because the source has no double quote, backslash,
backtick fence, tab or other control character, which the script asserts. The front matter's Abstract line becomes
abstract.txt. `--check` verifies the committed essay.md and abstract.txt
without writing. PROSE is pinned when the essay prose is frozen.
"""
from pathlib import Path
import hashlib, json, re, sys
root = Path(__file__).resolve().parents[3]
folder = root / 'reports/wolfram-agents/submissions/ether-episode'
check = '--check' in sys.argv[1:]
SOURCE = 'bd9ade9507a7c16a33fdf6d40842672adc1367ec7a6867c8f316e8b03b93e03e'
PROSE = '3b0ef32d79d25d1e511ee622ba3f2c3ee62578a20c0225f6c048c23bd6a171a5'
src = (folder / 'Rule30Submission.lean').read_bytes()
assert hashlib.sha256(src).hexdigest() == SOURCE, 'source differs from the officially checked one'
prose_data = (folder / 'essay-prose.md').read_bytes()
assert hashlib.sha256(prose_data).hexdigest() == PROSE, 'essay prose differs from the pinned one'
s, prose = src.decode(), prose_data.decode()
assert '\\' not in s and '"' not in s and '```' not in s and not any(ord(c) < 32 and c != '\n' for c in s)
assert prose.count('"%%LEAN%%"') == 1 and prose.count('%%LEAN%%') == 1
abstract = re.search(r'^Abstract: (.*)$', prose, re.M).group(1)
essay = prose.replace('%%LEAN%%', s)
for name, text in [('essay.md', essay), ('abstract.txt', abstract + '\n')]:
    if check:
        assert (folder / name).read_text() == text, name + ' differs'
    else:
        (folder / name).write_text(text)
print('essay', hashlib.sha256(essay.encode()).hexdigest(), len(essay.encode()))
print('abstract', hashlib.sha256((abstract + '\n').encode()).hexdigest(), len(abstract), 'characters,',
      len(abstract.split()), 'words')
