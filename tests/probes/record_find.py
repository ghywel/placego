#!/usr/bin/env python3
"""record_find.py: search the whole research record before a new probe, so a known result is not re-derived.

RUN-ON:     cpu (Python 3 standard library), about a second
COMMAND:    python3 tests/probes/record_find.py TERM [TERM ...] [--all] [--per N] [--headings] [--ledgers] [--no-known]

Why. On 2026-10-09 Cloud's SL probe re-derived a result the record already held (the wheel's locked block is forced:
GPT's G205 and G208, Local's LK), though the fact sat in row 6.1 of PERIOD-TWO.md's status board. Context
compaction had dropped it, and nothing made a search happen before the run. The owner asked for a fix. This is the
search half; RECORD-MAP.md is the other.

What it does. Each TERM is a case-insensitive regular expression. A hit is a paragraph (lines between blank lines; a
table row, and a top-level list item, is a paragraph of its own) in which every TERM matches. For each hit it prints
the file and line, the nearest heading above it (which names the result: G205, entry 27, 8.43, ...), the record IDs
in the paragraph, and a snippet. Files are searched in the order a reader should trust them: the map, the board, the
prize record, the proof files, GPT's record, the other research files, the probes, then (with --ledgers, or when
nothing else hits) the ledgers, newest first. --headings matches only heading lines, as a catalogue of named
results.

The rule (WORKFLOW-SAVED-MEMORY.md, literature-before-leaps and record-map): every PREDICTIONS block carries a line
`Record searched: <terms> -> <the hits that matter, or "no hit">`.

What is known outside the record. Since 2026-10-28 (L1078) the same terms are also searched in the kit's current main
and in the portal's listed submissions (`known_find.py`), and those hits are printed after the record's. That day the
degree law was re-derived although the kit had proved it on 2026-10-18, because nothing searched the kit. A hit there
is a candidate prior-art match whose hypotheses and conclusion must be read. `--no-known` skips this search (for offline use only), and an unavailable index is reported, not
silently skipped.
"""
import glob
import os
import re
import signal
import sys

signal.signal(signal.SIGPIPE, signal.SIG_DFL)                     # quiet when piped into head
ITEM = re.compile(r'^(?:[-*] |\d+\. )')

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FIRST = ['RECORD-MAP.md', 'PERIOD-TWO.md', 'RULE30-PRIZE.md', 'PROOFS.md',
         'CO-DISCOVERED-PROOFS.md', 'RULE30-GPT.md', 'PRIZE-PROBLEMS.md', 'COLLATZ-PRIZE.md', 'PRIOR-ART.md',
         'CONSTELLATION.md', 'STATE-OF-THE-PROOF.md', 'SPARKS.md']       # the 2026-10-08 snapshot after the live files
LEDGERS = ('CHAT-LEDGER', 'CLOUD-LOCAL', 'CASUAL-LEDGER')
IDS = re.compile(r'\b(?:GC\d+|G\d+|CL\d+|L\d+|SC\d+|SP\d+|IN\d{3,})\b|\bentr(?:y|ies) \d+|§ ?\d+(?:\.\d+)*|\b8\.\d+\b')


def ledger_key(path):
    base = os.path.basename(path)
    m = re.match(r'(.*?)(?:\.(\d+))?\.md$', base)
    return (LEDGERS.index(m.group(1)) if m.group(1) in LEDGERS else 9, -(int(m.group(2)) if m.group(2) else 10 ** 6))


def volumes(name):
    """The rotated volumes of a notebook (archive/gpt/NAME.1.md, NAME.2.md, ...), oldest first."""
    base = name[:-3]
    vols = glob.glob(os.path.join(ROOT, 'archive', 'gpt', base + '.*.md'))
    return sorted(vols, key=lambda p: int(os.path.basename(p)[len(base) + 1:-3]))


def files(ledgers):
    out = []
    for f in FIRST:                                 # a rotated notebook's volumes follow its live file
        if os.path.exists(os.path.join(ROOT, f)):
            out.append(os.path.join(ROOT, f))
            out += volumes(f)
    seen = set(out)
    rest = sorted(glob.glob(os.path.join(ROOT, 'proofs', '*.md')))
    rest += sorted(glob.glob(os.path.join(ROOT, 'tests', 'probes', '**', '*.py'), recursive=True))
    rest += [os.path.join(ROOT, 'tests', 'probes', 'PROBES.md')]
    led = []
    # Since the 2026-10-22 spring clean, rotated ledgers, volumes and retired documents live in archive/ and the
    # N-Frame video project's documents in nframe/; they are searched as before, after the root files. The finished
    # notes in reports/ are searched too (the eight-path note and the overlooked-work survey).
    moved = sorted(glob.glob(os.path.join(ROOT, 'nframe', '*.md')))
    moved += sorted(glob.glob(os.path.join(ROOT, 'reports', '**', '*.md'), recursive=True))
    moved += sorted(glob.glob(os.path.join(ROOT, 'archive', '**', '*.md'), recursive=True))
    for f in sorted(glob.glob(os.path.join(ROOT, '*.md'))) + moved:
        # Owner: the break room is closed; never read it, including in fallback searches.
        if os.path.basename(f).startswith('CASUAL-LEDGER'):
            continue
        if f in seen:
            continue
        if os.path.basename(f).startswith(LEDGERS):
            led.append(f)
        else:
            rest.append(f)
    led.sort(key=ledger_key)
    return [f for f in out + rest if os.path.exists(f)], led


def paragraphs(path):
    """Yield (first line number, heading, text) for each paragraph; table rows are paragraphs of their own."""
    heading, buf, start = '', [], 0
    is_py = path.endswith('.py')
    if is_py:
        heading = os.path.basename(path)
    with open(path, encoding='utf-8', errors='replace') as fh:
        for n, line in enumerate(fh, 1):
            s = line.rstrip('\n')
            if not is_py and s.startswith('#'):
                if buf:
                    yield start, heading, '\n'.join(buf)
                    buf = []
                heading = s.lstrip('#').strip()
                yield n, heading, s
                continue
            if not s.strip() or (not is_py and s.startswith('|')):
                if buf:
                    yield start, heading, '\n'.join(buf)
                    buf = []
                if s.strip():
                    yield n, heading, s
                continue
            if buf and not is_py and ITEM.match(s):
                yield start, heading, '\n'.join(buf)
                buf = []
            if not buf:
                start = n
            buf.append(s)
    if buf:
        yield start, heading, '\n'.join(buf)


def search(paths, pats, headings_only):
    hits = {}
    for p in paths:
        for n, head, text in paragraphs(p):
            if headings_only and not (text.startswith('#') or text == os.path.basename(p)):
                continue
            if all(r.search(text) for r in pats):
                hits.setdefault(p, []).append((n, head, text))
    return hits


def snippet(text, pats, width=230):
    flat = ' '.join(text.split())
    m = min((r.search(flat) for r in pats), key=lambda x: x.start() if x else 10 ** 9)
    i = max(0, m.start() - width // 3) if m else 0
    return ('...' if i else '') + flat[i:i + width] + ('...' if i + width < len(flat) else '')


def main():
    args = sys.argv[1:]
    show_all = '--all' in args
    headings_only = '--headings' in args
    want_ledgers = '--ledgers' in args
    per = 6
    if '--per' in args:
        per = int(args[args.index('--per') + 1])
        args = args[:args.index('--per')] + args[args.index('--per') + 2:]
    terms = [a for a in args if not a.startswith('--')]
    if not terms:
        print(__doc__)
        sys.exit(1)
    pats = [re.compile(t, re.I) for t in terms]
    main_files, ledger_files = files(want_ledgers)
    hits = search(main_files, pats, headings_only)
    if want_ledgers or not hits:
        if not hits:
            print('(no hit outside the ledgers; searching the ledgers too)')
        hits.update(search(ledger_files, pats, headings_only))
    total = sum(len(v) for v in hits.values())
    print('terms %s: %d hit(s) in %d file(s)' % (terms, total, len(hits)))
    for p in main_files + ledger_files:
        if p not in hits:
            continue
        rel = os.path.relpath(p, ROOT)
        rows = hits[p]
        print('\n== %s (%d)' % (rel, len(rows)))
        for n, head, text in (rows if show_all else rows[:per]):
            ids = []
            for m in IDS.finditer(text):
                if m.group(0) not in ids:
                    ids.append(m.group(0))
            print('  %s:%d  [%s]%s' % (rel, n, head[:90], ('  ids: ' + ' '.join(ids[:10])) if ids else ''))
            print('      ' + snippet(text, pats))
        if not show_all and len(rows) > per:
            print('  ... %d more (use --all or --per N)' % (len(rows) - per))
    if '--no-known' in args:
        print('\n(the kit and the portal were NOT searched: --no-known)')
        return
    print('\n######## known outside the record: the kit\'s main, the portal and the open kit PRs ########')
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import known_find
    if known_find.report(terms, per, show_all) < 0:
        sys.exit(2)


if __name__ == '__main__':
    main()
