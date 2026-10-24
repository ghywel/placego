#!/usr/bin/env python3
"""assemble.py: build essay.md from essay-template.md by inserting Rule30Submission.lean verbatim into the
LeanImportString cell. Run from this directory: python3 assemble.py. The source must contain no double quote or
backslash (checked), since it sits inside a Wolfram Language string."""
src = open('Rule30Submission.lean', encoding='utf-8').read()
assert '"' not in src and '\\' not in src, 'the Lean source would break the Wolfram string'
tpl = open('essay-template.md', encoding='utf-8').read()
assert tpl.count('@@LEAN_SOURCE@@') == 1
open('essay.md', 'w', encoding='utf-8').write(tpl.replace('@@LEAN_SOURCE@@', src.rstrip('\n') + '\n'))
print('essay.md written:', len(open('essay.md', encoding='utf-8').read()), 'characters')
