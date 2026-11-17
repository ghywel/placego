#!/usr/bin/env python3
"""assemble_words.py: build <dir>/essay.md for a word submission from essay-words-template.md and the module in <dir>.

    python3 assemble_words.py words-A "Excluded column words of length 11 to 16, beyond the kit's table" "11 to 16" '{"00000000000001", 8, 2}, {"00000001111", 10, 4}'
    python3 assemble_words.py words-B "Excluded column words of length 17 and 18, beyond the kit's table" "17 and 18" '{"00000000000000011", 8, 2}, {"000000000000000001", 8, 2}'

Run from this directory. The word list and its widths are read from the module's `words8` and `words10`, so the essay
lists exactly what the Lean proves. The Lean source must contain no double quote or backslash (checked), since it
sits inside a Wolfram Language string."""
import re, sys
d, title, lengths, examples = sys.argv[1:5]
src = open(f'{d}/Rule30Submission.lean', encoding='utf-8').read()
assert '"' not in src and '\\' not in src, 'the Lean source would break the Wolfram string'
def words(name, K):
    m = re.search(r'def ' + name + r' : List \(ℕ × List ℕ\) := \[(.*?)\]\n\n', src, re.S)
    return [(''.join(w.replace(' ', '').split(',')), K) for w in re.findall(r'\[([01, ]+)\]', m.group(1))]
ws = words('words8', 8) + words('words10', 10)
wl = '{' + ', '.join(f'{{"{w}", {K}}}' for w, K in ws) + '}'
tpl = open('essay-words-template.md', encoding='utf-8').read()
for k, v in [('@@TITLE@@', title), ('@@COUNT@@', str(len(ws))), ('@@LENGTHS@@', lengths), ('@@WORDS@@', wl),
             ('@@EXAMPLES@@', '{' + examples + '}'), ('@@LEAN_SOURCE@@', src.rstrip('\n') + '\n')]:
    assert k in tpl, k
    tpl = tpl.replace(k, v)
assert '@@' not in tpl.replace('@@ ', '')  # Wolfram's Apply is "@@ " with a space
open(f'{d}/essay.md', 'w', encoding='utf-8').write(tpl)
print(f'{d}/essay.md written: {len(ws)} words, {len(tpl)} characters')
