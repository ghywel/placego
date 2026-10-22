#!/usr/bin/env python3
"""doc_links.py: every relative link in the record's markdown points at a file and a heading that exist.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/doc_links.py [--verbose]        (from anywhere inside the repository)
COST:       about a second.

Why (the spring clean of 2026-10-22). The owner asked for the documentation to be made clean and browsable: the
rotated ledgers, the frozen volumes of GPT's notebooks and retired documents went to archive/, and the N-Frame
video project's documents to nframe/. Every relative link was rewritten then, and this check ended at 0 broken.
Run it before pushing a change that moves, renames or splits a document, or that adds links, so it stays at 0.

What it checks. In every tracked .md file: inline links and images [text](target), reference definitions
[id]: target, and href="..." / src="..." attributes. A target that is not a URL must name an existing file or
folder, resolved from the linking file's folder; a #fragment on a markdown target must match one of that file's
headings, as GitHub forms them (lower case, punctuation dropped, spaces to hyphens, -1, -2 for repeats), or an
<a name> / <a id>. Links inside fenced code blocks are ignored. Bare mentions such as "RULE30-PRIZE.md 8.59" are not
links and are not checked: a moved file keeps its name, so its mentions still find it.
Control: a synthetic pair of files (one good link, one missing file, one missing heading) must give 1 and 1.
Exit status 1 if anything is broken.
"""
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter

LINK = re.compile(r'\[(?:[^\]\[]|\[[^\]]*\])*\]\(\s*<?([^)\s>]+)>?(?:\s+"[^"]*")?\s*\)')
REFDEF = re.compile(r'(?m)^[ ]{0,3}\[[^\]\n]+\]:[ \t]*<?([^\s>]+)>?')
HREF = re.compile(r'(?:href|src)="([^"]+)"')


def slug(text):
    text = text.strip().lower().replace('`', '')
    text = re.sub(r'[^\w\- ]', '', text, flags=re.UNICODE)
    return text.replace(' ', '-')


def anchors(path, cache={}):
    if path not in cache:
        found, seen, fence = set(), Counter(), False
        with open(path, encoding='utf-8', errors='replace') as fh:
            for line in fh:
                if line.lstrip().startswith(('```', '~~~')):
                    fence = not fence
                if fence:
                    continue
                m = re.match(r'#{1,6}\s+(.*?)\s*#*\s*$', line)
                if m:
                    s = slug(m.group(1))
                    found.add(s if not seen[s] else f'{s}-{seen[s]}')
                    seen[s] += 1
                found.update(re.findall(r'<a\s+(?:name|id)="([^"]+)"', line))
        cache[path] = found
    return cache[path]


def strip_fences(text):
    out, fence = [], False
    for line in text.split('\n'):
        if line.lstrip().startswith(('```', '~~~')):
            fence = not fence
            out.append('')
            continue
        out.append('' if fence else line)
    return '\n'.join(out)


def check(root):
    files = subprocess.run(['git', '-C', root, 'ls-files', '-z', '*.md'], capture_output=True, text=True,
                           check=True).stdout.split('\0')
    total, broken, bad_anchor = 0, [], []
    for f in filter(None, files):
        text = strip_fences(open(os.path.join(root, f), encoding='utf-8', errors='replace').read())
        refs = [t for t in REFDEF.findall(text) if not re.search(r'[(),;]', t)]   # "[a,b]: (5,7,9)" is maths
        for t in LINK.findall(text) + refs + HREF.findall(text):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', t) or t.startswith('//'):
                continue
            total += 1
            path, _, frag = t.partition('#')
            target = f if not path else os.path.normpath(os.path.join(os.path.dirname(f), path.replace('%20', ' ')))
            full = os.path.join(root, target)
            if path and not os.path.exists(full):
                broken.append((f, t))
            elif frag and target.endswith('.md') and os.path.isfile(full):
                if frag.lower() not in anchors(full) and slug(frag) not in anchors(full):
                    bad_anchor.append((f, t))
    return total, broken, bad_anchor


def control():
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(['git', '-C', d, 'init', '-q'], check=True)
        open(os.path.join(d, 'A.md'), 'w').write('# Title\n## Before the energy (2026-09-30)\n')
        open(os.path.join(d, 'C.md'), 'w').write('[ok](A.md#before-the-energy-2026-09-30) [x](A.md#nope) [y](B.md)\n'
                                                 '```\n[not a link](Z.md)\n```\n')
        subprocess.run(['git', '-C', d, 'add', '.'], check=True)
        total, broken, bad = check(d)
        assert (total, len(broken), len(bad)) == (3, 1, 1), (total, broken, bad)


def main():
    control()
    root = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True,
                          check=True).stdout.strip()
    total, broken, bad = check(root)
    for f, t in (broken + bad)[: None if '--verbose' in sys.argv else 20]:
        print(f'BROKEN  {f} -> {t}')
    print(f'{"DOC LINKS PASS" if not broken and not bad else "DOC LINKS FAIL"}: {total} relative links, '
          f'{len(broken)} missing targets, {len(bad)} missing headings')
    sys.exit(1 if broken or bad else 0)


if __name__ == '__main__':
    main()
