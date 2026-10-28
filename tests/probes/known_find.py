#!/usr/bin/env python3
"""known_find.py: search what is already known outside our record (the kit's current main and the portal's listed
submissions) before a new probe or proof, so that a known result is not re-derived.

RUN-ON:     cpu (Python 3 standard library and git); a refresh fetches about 7 MB, a search takes about a second
COMMAND:    python3 tests/probes/known_find.py TERM [TERM ...] [--all] [--per N] [--refresh] [--offline]
            python3 tests/probes/known_find.py --new        (what the last refresh added: the daily portal check)
            python3 tests/probes/known_find.py --selftest   (the controls)

Why. On 2026-10-28 Local hand-proved the degree law (L1072), had it second-read (GC2032) and formalized it in core
Lean (L1074 to L1077). Only then did it find that the kit's own `equivalents/Rule30Equivalents/AlgebraicDegree.lean`
had proved it on 2026-10-18. The record's searches had covered the literature and the record, but not the kit's
`equivalents/` catalog, and the daily portal checks were never turned into a searchable record. The owner asked for a
fix: work is to be based on what we already know and on what the portal lists. `record_find.py` calls this search
too, so the usual pre-work search covers both.

What it searches. Each TERM is a case-insensitive regular expression, and a hit is a unit in which every TERM matches
(the raw text, or a normalized copy with `−` read as `-`, `⋯` as `...`, and `$`, backslashes and backticks dropped).
The units are:
- every row of the kit's catalog tables (`README.md`, `lean/README.md`, `equivalents/README.md`);
- the header docstring of every kit module (`lean/` and `equivalents/`);
- every kit declaration, as its doc comment with its first line;
- every portal entry, as its title, abstract, headline names and kit modules.

The cache. It lives outside git, in `$PLACEGO_KNOWN_CACHE` or else `~/.cache/placego-known`. It holds a shallow
clone of the kit's main and `portal.json`, and it is refreshed when older than six hours. If a refresh fails, the old
cache is used and its age is printed. With no cache at all, it says plainly that novelty cannot be judged. A hit here
is prior art: cite it, and put a new proof in PRIOR-ART.md as "known, reproved here". No hit is not a novelty
certificate, since the literature still has to be searched.
"""
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import time
import urllib.request

signal.signal(signal.SIGPIPE, signal.SIG_DFL)

KIT_URL = 'https://github.com/WolframInstitute/Rule30PrizeKit'
PORTAL_URL = 'https://www.wolframcloud.com/obj/rule-30-prize/Agents/submissions.json'
PORTAL_PAGE = 'https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/'
KIT_BLOB = KIT_URL + '/blob/%s/%s'
MAX_AGE = 6 * 3600
CACHE = os.environ.get('PLACEGO_KNOWN_CACHE') or os.path.join(os.path.expanduser('~'), '.cache', 'placego-known')
KIT_DIR = os.path.join(CACHE, 'kit')
PORTAL = os.path.join(CACHE, 'portal.json')
STAMP = os.path.join(CACHE, 'stamp.json')
PORTAL_SRC = os.path.join(CACHE, 'portal-src')      # each submission's Lean source, by id (fetched once)
CHECKED = os.path.join(CACHE, 'checked.json')       # the index keys at the last --new (the daily portal check)

DECL = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|public|nonrec)\s+)*'
                  r'(theorem|lemma|def|abbrev|structure|inductive|class|instance)\s+([^\s:({\[]+)')
NORM = [('−', '-'), ('⋯', '...'), ('…', '...'), ('$', ''), ('\\', ''), ('`', '')]


def git(*args, cwd=None):
    return subprocess.run(['git'] + list(args), cwd=cwd, capture_output=True, text=True, timeout=180)


def stamp():
    try:
        with open(STAMP) as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def refresh(force=False, offline=False):
    """Bring the cache up to date when it is stale; return (status line, ok)."""
    st = stamp()
    age = time.time() - st.get('time', 0)
    have = os.path.isdir(os.path.join(KIT_DIR, '.git')) and os.path.exists(PORTAL)
    if have and (offline or (age < MAX_AGE and not force)):
        return status_line(st, age), True
    if offline:
        return 'KNOWN INDEX UNAVAILABLE (offline, no cache): novelty cannot be judged', False
    os.makedirs(CACHE, exist_ok=True)
    errors = []
    if os.path.isdir(os.path.join(KIT_DIR, '.git')):
        r = git('fetch', '-q', '--depth', '1', 'origin', 'main', cwd=KIT_DIR)
        if r.returncode == 0:
            r = git('reset', '-q', '--hard', 'FETCH_HEAD', cwd=KIT_DIR)   # our own cache clone, never a worktree
        if r.returncode:
            errors.append('kit fetch failed: ' + r.stderr.strip()[:200])
    else:
        shutil.rmtree(KIT_DIR, ignore_errors=True)
        r = git('clone', '-q', '--depth', '1', KIT_URL, KIT_DIR)
        if r.returncode:
            errors.append('kit clone failed: ' + r.stderr.strip()[:200])
    try:
        with urllib.request.urlopen(PORTAL_URL, timeout=60) as resp:
            data = resp.read()
        json.loads(data)
        tmp = PORTAL + '.tmp'
        with open(tmp, 'wb') as fh:
            fh.write(data)
        os.replace(tmp, PORTAL)
    except Exception as exc:                                            # keep the old copy
        errors.append('portal fetch failed: %s' % exc)
    errors += fetch_sources()
    have = os.path.isdir(os.path.join(KIT_DIR, '.git')) and os.path.exists(PORTAL)
    if not have:
        return 'KNOWN INDEX UNAVAILABLE (%s): novelty cannot be judged' % '; '.join(errors), False
    if not errors:
        head = git('rev-parse', 'HEAD', cwd=KIT_DIR).stdout.strip()
        with open(PORTAL) as fh:
            updated = json.load(fh).get('updated', '?')
        st = {'time': time.time(), 'kit': head, 'portal': updated}
        with open(STAMP, 'w') as fh:
            json.dump(st, fh)
        return status_line(st, 0), True
    st = stamp()
    return status_line(st, time.time() - st.get('time', 0)) + '  (REFRESH FAILED, using the cache: %s)' % \
        '; '.join(errors), True


def fetch_sources():
    """Fetch the Lean source of every listed submission not yet cached (a submission id's source is fixed)."""
    try:
        with open(PORTAL, encoding='utf-8') as fh:
            entries = json.load(fh).get('entries', [])
    except (OSError, ValueError):
        return []
    os.makedirs(PORTAL_SRC, exist_ok=True)
    failed = 0
    for e in entries:
        url = (e.get('files') or {}).get('lean')
        dest = os.path.join(PORTAL_SRC, re.sub(r'[^A-Za-z0-9-]', '_', e.get('id', '')) + '.lean')
        if not url or os.path.exists(dest):
            continue
        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                data = resp.read()
            with open(dest + '.tmp', 'wb') as fh:
                fh.write(data)
            os.replace(dest + '.tmp', dest)
        except Exception:
            failed += 1
    return ['%d submission source(s) not fetched' % failed] if failed else []


def status_line(st, age):
    return 'known index: kit main @%s, portal updated %s, fetched %.1f h ago' % (
        st.get('kit', '?')[:8], st.get('portal', '?'), age / 3600)


def module_name(rel):
    return rel[:-5].split('/', 1)[1].replace('/', '.') if rel.endswith('.lean') else rel


def lean_units(rel, path, commit):
    """The module header and one unit per declaration (its doc comment plus its first line)."""
    with open(path, encoding='utf-8', errors='replace') as fh:
        lines = fh.read().split('\n')
    url = KIT_BLOB % (commit, rel)
    out, doc, in_doc, header_done = [], [], False, False
    for n, line in enumerate(lines, 1):
        s = line.strip()
        if not in_doc and (s.startswith('/-!') or s.startswith('/--')):
            in_doc, doc, start = True, [line], n
            is_header = s.startswith('/-!')
            if s.endswith('-/') and len(s) > 4:
                in_doc = False
            if not in_doc and is_header and not header_done:
                out.append(('kit module', module_name(rel), '%s#L%d' % (url, start), '\n'.join(doc)))
                header_done = True
            continue
        if in_doc:
            doc.append(line)
            if s.endswith('-/'):
                in_doc = False
                if is_header and not header_done:
                    out.append(('kit module', module_name(rel), '%s#L%d' % (url, start), '\n'.join(doc)))
                    header_done = True
                elif is_header:
                    doc = []
            continue
        m = DECL.match(s)
        if m:
            text = '\n'.join(doc + [line]) if doc else line
            out.append(('kit declaration', '%s.%s' % (module_name(rel), m.group(2)), '%s#L%d' % (url, n), text))
            doc = []
        elif s and not s.startswith('--'):
            doc = []
    return out


def catalog_units(rel, path, commit):
    out, heading = [], ''
    with open(path, encoding='utf-8', errors='replace') as fh:
        for n, line in enumerate(fh, 1):
            s = line.rstrip('\n')
            if s.startswith('#'):
                heading = s.lstrip('#').strip()
            elif s.startswith('|') and not re.match(r'^\|[\s:|-]+\|$', s):
                m = re.search(r'\[([^\]]+)\]\(([^)]+\.lean)\)', s)
                name = m.group(1) if m else heading[:60]
                out.append(('kit catalog', name, KIT_BLOB % (commit, rel) + '#L%d' % n, s))
    return out


def portal_units():
    with open(PORTAL, encoding='utf-8') as fh:
        data = json.load(fh)
    out = []
    for e in data.get('entries', []):
        mods = (e.get('kitContribution') or {}).get('modules') or []
        text = '\n'.join([e.get('title', ''), e.get('abstract', '')] + list(e.get('headlines') or []) + mods)
        label = '%s [%s; problem %s, %s]' % (e.get('id', '?'), e.get('status', '?'), e.get('problem', '?'),
                                            e.get('claim', '?'))
        out.append(('portal', label, PORTAL_PAGE + e.get('id', ''), text))
        src = os.path.join(PORTAL_SRC, re.sub(r'[^A-Za-z0-9-]', '_', e.get('id', '')) + '.lean')
        if os.path.exists(src):
            for _, name, _, t in lean_units('x/' + e.get('id', '') + '.lean', src, ''):
                out.append(('portal declaration', '%s %s' % (e.get('id', '?'), name.split('.', 1)[-1]),
                            PORTAL_PAGE + e.get('id', ''), t))
    return out


def all_units():
    if not os.path.isdir(os.path.join(KIT_DIR, '.git')) or not os.path.exists(PORTAL):
        return []
    commit = git('rev-parse', 'HEAD', cwd=KIT_DIR).stdout.strip() or 'main'
    units = []
    for rel in ('README.md', 'lean/README.md', 'equivalents/README.md'):
        p = os.path.join(KIT_DIR, rel)
        if os.path.exists(p):
            units += catalog_units(rel, p, commit)
    for top in ('lean', 'equivalents'):
        for dirpath, _, names in os.walk(os.path.join(KIT_DIR, top)):
            if '.lake' in dirpath:
                continue
            for name in sorted(names):
                if name.endswith('.lean'):
                    p = os.path.join(dirpath, name)
                    units += lean_units(os.path.relpath(p, KIT_DIR), p, commit)
    return units + portal_units()


def norm(text):
    for a, b in NORM:
        text = text.replace(a, b)
    return text


def search(pats, units=None):
    units = all_units() if units is None else units
    return [u for u in units if all(r.search(u[3]) or r.search(norm(u[3])) for r in pats)]


def snippet(text, pats, width=230):
    flat = ' '.join(norm(text).split())
    ms = [r.search(flat) for r in pats]
    ms = [m for m in ms if m]
    i = max(0, min(m.start() for m in ms) - width // 3) if ms else 0
    return ('...' if i else '') + flat[i:i + width] + ('...' if i + width < len(flat) else '')


ORDER = ['portal', 'portal declaration', 'kit catalog', 'kit module', 'kit declaration']


def report(terms, per=6, show_all=False, force=False, offline=False, indent=''):
    """Print the hits; return the number of hits (or -1 when the index is unavailable)."""
    line, ok = refresh(force, offline)
    print(indent + line)
    if not ok:
        return -1
    pats = [re.compile(t, re.I) for t in terms]
    hits = search(pats)
    print(indent + 'terms %s: %d hit(s) in the kit and the portal' % (terms, len(hits)))
    for kind in ORDER:
        rows = [h for h in hits if h[0] == kind]
        if not rows:
            continue
        print('\n%s== %s (%d)' % (indent, kind, len(rows)))
        for _, name, url, text in (rows if show_all else rows[:per]):
            print('%s  %s  %s' % (indent, name, url))
            print('%s      %s' % (indent, snippet(text, pats)))
        if not show_all and len(rows) > per:
            print('%s  ... %d more (use --all or --per N)' % (indent, len(rows) - per))
    if hits:
        print('\n%sA hit is prior art: cite it; a new proof goes in PRIOR-ART.md as "known, reproved here".' % indent)
    return len(hits)


def new_since_last():
    """The daily portal check: what was added to the portal and the kit since the last --new on this host."""
    line, ok = refresh(force=True)
    print(line)
    if not ok:
        return 1
    units = {'%s|%s' % (k, n): (k, n, u, t) for k, n, u, t in all_units() if k in ('kit module', 'portal')}
    try:
        with open(CHECKED) as fh:
            last = json.load(fh)
        prev = set(last['keys'])
    except (OSError, ValueError, KeyError):
        last, prev = None, None
    with open(CHECKED, 'w') as fh:
        json.dump({'keys': sorted(units), 'stamp': stamp()}, fh)
    if last is None:
        print('no earlier check on this host: this one is the baseline (%d portal entries and kit modules)' % len(units))
        return 0
    added = sorted(set(units) - prev)
    gone = sorted(prev - set(units))
    print('%d added, %d no longer listed, since the last check (%s)' % (
        len(added), len(gone), status_line(last.get('stamp', {}), time.time() - last.get('stamp', {}).get('time', 0))))
    for key in added:
        kind, name, url, text = units[key]
        print('\n+ %s  %s  %s' % (kind, name, url))
        print('      ' + ' '.join(norm(text).split())[:300])
    for key in gone:
        print('- %s' % key.replace('|', '  '))
    return 0


def selftest():
    """Controls: known results must be found; a nonsense term must not be."""
    line, ok = refresh()
    print(line)
    if not ok:
        print('SELFTEST FAILS: no index')
        return 1
    units = all_units()
    checks = [
        (['algebraic degree', '2t'], lambda h: any('AlgebraicDegree' in x[1] for x in h)),
        (['isGreatest_card_coef_center'], lambda h: any(x[0] == 'kit declaration' for x in h)),
        (['degree', '2t - 1'], lambda h: any(x[0] == 'kit catalog' for x in h)),   # normalized minus sign
        (['stripe', 'four'], lambda h: any(x[0] == 'portal' for x in h)),
        (['FrozenRuler'], lambda h: any(x[0] == 'kit module' for x in h)),
        (['Rule30Submission'], lambda h: any(x[0] == 'portal declaration' for x in h)),
        (['zqxjv-no-such-term'], lambda h: not h),
    ]
    bad = 0
    for terms, good in checks:
        h = search([re.compile(t, re.I) for t in terms], units)
        verdict = good(h)
        bad += not verdict
        print('%s  %s: %d hit(s)' % ('ok  ' if verdict else 'FAIL', terms, len(h)))
    kinds = {k: sum(1 for u in units if u[0] == k) for k in ORDER}
    print('units: %s' % ', '.join('%s %d' % (k, v) for k, v in kinds.items()))
    print('SELFTEST %s' % ('PASSES' if not bad else 'FAILS'))
    return 1 if bad else 0


def main():
    args = sys.argv[1:]
    if '--selftest' in args:
        sys.exit(selftest())
    if '--new' in args:
        sys.exit(new_since_last())
    per = 6
    if '--per' in args:
        per = int(args[args.index('--per') + 1])
        args = args[:args.index('--per')] + args[args.index('--per') + 2:]
    terms = [a for a in args if not a.startswith('--')]
    if not terms:
        print(__doc__)
        sys.exit(1)
    n = report(terms, per, '--all' in args, '--refresh' in args, '--offline' in args)
    sys.exit(2 if n < 0 else 0)


if __name__ == '__main__':
    main()
