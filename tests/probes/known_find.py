#!/usr/bin/env python3
"""known_find.py: search what is already known outside our record (the kit's current main, the portal's listed
submissions and the kit's open pull requests) before a new probe or proof, so that a known result is not re-derived.

RUN-ON:     cpu (Python 3 standard library and git; `gh` if installed); a refresh fetches about 7 MB plus the open PR
            heads, a search takes about a second
COMMAND:    python3 tests/probes/known_find.py TERM [TERM ...] [--all] [--per N] [--refresh] [--offline]
            python3 tests/probes/known_find.py --new        (added or changed sources/entries: the daily portal check)
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
- complete Lean files, so multiline statements and unindexed declarations remain searchable;
- every portal entry, as its title, abstract, headline names and kit modules;
- every open kit pull request (L1149): its title and description, each conversation comment and inline review comment,
  and the Lean files its head adds or changes, indexed like kit files and labelled with the PR number.

Why the pull requests (L1146, L1148). On 2026-10-29 GPT rebuilt a prefix-period bridge at 08:35 that Troy Lowry had
already proved in public: in a comment on our own kit PR #51 at 04:35, and in his open PR #55 at 07:47. Neither the
kit's main nor the portal showed it, and open PRs are public prior art too. Review summaries without a comment body
are not indexed. With `gh` the file lists come from GitHub. Without it, the public API supplies metadata and comments,
and the files are those a head adds or changes relative to the kit's current main, which can include stale copies
of kit files that main has since changed.

The cache. It lives outside git, in `$PLACEGO_KNOWN_CACHE` or else `~/.cache/placego-known`. It holds a shallow
clone of the kit's main (with each open PR head fetched into it at depth one), `portal.json` and `prs.json`, and it
is refreshed when older than six hours. If a refresh fails, the old
cache is used and its age is printed. With no cache at all, it says plainly that novelty cannot be judged. A hit here
is a candidate match: compare its hypotheses and conclusion before marking a result known. No hit is not a novelty
certificate, since the literature still has to be searched.
"""
import hashlib
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
GH_REPO = 'WolframInstitute/Rule30PrizeKit'
API = 'https://api.github.com/'
PRS = os.path.join(CACHE, 'prs.json')               # open pull requests with their comments (L1149)
PR_SRC = os.path.join(CACHE, 'pr-src')              # each open PR head's added or changed Lean files, by head commit

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
    if have and (offline or (age < MAX_AGE and not force and os.path.exists(PRS))):
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
    errors += fetch_prs()
    have = os.path.isdir(os.path.join(KIT_DIR, '.git')) and os.path.exists(PORTAL)
    if not have:
        return 'KNOWN INDEX UNAVAILABLE (%s): novelty cannot be judged' % '; '.join(errors), False
    if not errors:
        head = git('rev-parse', 'HEAD', cwd=KIT_DIR).stdout.strip()
        with open(PORTAL) as fh:
            updated = json.load(fh).get('updated', '?')
        st = {'time': time.time(), 'kit': head, 'portal': updated, 'prs': len(load_prs())}
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


def api_list(path):
    """Every item of a paginated GitHub list endpoint: through `gh api` when it works, else the public API."""
    if shutil.which('gh'):
        r = subprocess.run(['gh', 'api', '--paginate', '--slurp', path], capture_output=True, text=True, timeout=180)
        if r.returncode == 0:
            return [item for page in json.loads(r.stdout) for item in page]
    items, page = [], 1
    while True:
        req = urllib.request.Request('%s%s%spage=%d' % (API, path, '&' if '?' in path else '?', page),
                                     headers={'Accept': 'application/vnd.github+json', 'User-Agent': 'placego-known-find'})
        with urllib.request.urlopen(req, timeout=60) as resp:
            batch = json.loads(resp.read())
        items += batch
        if len(batch) < 100:
            return items
        page += 1


def load_prs():
    try:
        with open(PRS, encoding='utf-8') as fh:
            return json.load(fh).get('prs', [])
    except (OSError, ValueError):
        return []


def pr_dir(pr):
    return os.path.join(PR_SRC, '%d-%s' % (pr['number'], pr['head'][:12]))


def fetch_prs():
    """Index the kit's open PRs: metadata and comments, and each head's added or changed Lean files (fetched once per
    head commit). On any failure the previous index is kept and the failure is reported."""
    repo = 'repos/' + GH_REPO
    try:
        pulls = api_list(repo + '/pulls?state=open&per_page=100')
        comments = {p['number']: [] for p in pulls}
        for c in api_list(repo + '/issues/comments?per_page=100'):
            n = int(c['issue_url'].rsplit('/', 1)[1])
            if n in comments:
                comments[n].append(('comment', c))
        for c in api_list(repo + '/pulls/comments?per_page=100'):
            n = int(c['pull_request_url'].rsplit('/', 1)[1])
            if n in comments:
                comments[n].append(('review comment', c))
    except Exception as exc:
        return ['PR index fetch failed: %s' % exc]
    prs = []
    for p in sorted(pulls, key=lambda q: q['number']):
        prs.append({'number': p['number'], 'title': p['title'], 'body': p.get('body') or '',
                    'author': (p.get('user') or {}).get('login', '?'), 'head': p['head']['sha'],
                    'url': p['html_url'], 'updated': p['updated_at'],
                    'comments': [{'kind': k, 'author': (c.get('user') or {}).get('login', '?'),
                                  'at': c.get('created_at', ''), 'url': c.get('html_url', ''),
                                  'body': c.get('body') or ''} for k, c in comments[p['number']]]})
    errors, need = [], [p for p in prs if not os.path.exists(os.path.join(pr_dir(p), 'DONE'))]
    if need:
        r = git('fetch', '-q', '--depth', '1', 'origin',
                *['+refs/pull/%d/head:refs/pr/%d' % (p['number'], p['number']) for p in need], cwd=KIT_DIR)
        if r.returncode:
            errors.append('PR head fetch failed: ' + r.stderr.strip()[:200])
            need = []
    for p in need:
        ref = 'refs/pr/%d' % p['number']
        if git('rev-parse', ref, cwd=KIT_DIR).stdout.strip() != p['head']:
            errors.append('PR #%d head moved during the fetch' % p['number'])
            continue
        try:
            if shutil.which('gh'):
                files = [f['filename'] for f in api_list('%s/pulls/%d/files?per_page=100' % (repo, p['number']))
                         if f.get('status') != 'removed']
            else:
                files = git('diff', '--name-only', '--diff-filter=AM', 'HEAD', ref, cwd=KIT_DIR).stdout.split()
        except Exception as exc:
            errors.append('PR #%d file list failed: %s' % (p['number'], exc))
            continue
        d = pr_dir(p)
        shutil.rmtree(d, ignore_errors=True)
        lean = sorted(f for f in files if f.endswith('.lean'))
        for rel in lean:
            blob = subprocess.run(['git', 'show', '%s:%s' % (ref, rel)], cwd=KIT_DIR, capture_output=True, timeout=60)
            if blob.returncode == 0:
                os.makedirs(os.path.dirname(os.path.join(d, rel)) or d, exist_ok=True)
                with open(os.path.join(d, rel), 'wb') as fh:
                    fh.write(blob.stdout)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, 'FILES.json'), 'w') as fh:
            json.dump({'files': files, 'lean': lean}, fh)
        with open(os.path.join(d, 'DONE'), 'w') as fh:
            fh.write(p['head'])
    keep = {os.path.basename(pr_dir(p)) for p in prs}
    if os.path.isdir(PR_SRC):
        for name in os.listdir(PR_SRC):
            if name not in keep:
                shutil.rmtree(os.path.join(PR_SRC, name), ignore_errors=True)
    os.makedirs(CACHE, exist_ok=True)
    with open(PRS + '.tmp', 'w', encoding='utf-8') as fh:
        json.dump({'fetched': time.time(), 'prs': prs}, fh)
    os.replace(PRS + '.tmp', PRS)
    return errors


def status_line(st, age):
    return 'known index: kit main @%s, portal updated %s, %s open kit PRs, fetched %.1f h ago' % (
        st.get('kit', '?')[:8], st.get('portal', '?'), st.get('prs', '?'), age / 3600)


def module_name(rel):
    if not rel.endswith('.lean'):
        return rel
    parts = rel[:-5].split('/', 1)
    return parts[-1].replace('/', '.')


def lean_units(rel, path, commit):
    """Full source, module header and declaration doc comments with first lines."""
    with open(path, encoding='utf-8', errors='replace') as fh:
        lines = fh.read().split('\n')
    url = KIT_BLOB % (commit, rel)
    out, doc, in_doc, header_done = [('kit source', module_name(rel), url, '\n'.join(lines))], [], False, False
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
            for kind, name, _, t in lean_units('x/' + e.get('id', '') + '.lean', src, ''):
                out.append(('portal source' if kind == 'kit source' else 'portal declaration', '%s %s' % (e.get('id', '?'), name.split('.', 1)[-1]),
                            PORTAL_PAGE + e.get('id', ''), t))
    return out


def pr_units():
    """Each open PR's description, its comments, and its head's Lean files labelled with the PR number."""
    out = []
    for p in load_prs():
        tag = '#%d' % p['number']
        out.append(('open PR', '%s %s: %s' % (tag, p['author'], p['title']), p['url'], p['title'] + '\n' + p['body']))
        for c in p['comments']:
            out.append(('open PR comment', '%s %s %s %s' % (tag, c['kind'], c['author'], c['at'][:16]),
                        c['url'] or p['url'], c['body']))
        d = pr_dir(p)
        try:
            with open(os.path.join(d, 'FILES.json')) as fh:
                lean = json.load(fh)['lean']
        except (OSError, ValueError, KeyError):
            continue
        for rel in lean:
            path = os.path.join(d, rel)
            if os.path.exists(path):
                for kind, name, url, t in lean_units(rel, path, p['head']):
                    out.append((kind.replace('kit', 'PR'), '%s %s' % (tag, name), url, t))
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
    return units + portal_units() + pr_units()


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


ORDER = ['portal', 'portal declaration', 'kit catalog', 'kit module', 'kit declaration',
         'kit source', 'portal source', 'open PR', 'open PR comment', 'PR module', 'PR declaration', 'PR source']


def report(terms, per=6, show_all=False, force=False, offline=False, indent=''):
    """Print the hits; return the number of hits (or -1 when the index is unavailable)."""
    line, ok = refresh(force, offline)
    print(indent + line)
    if not ok:
        return -1
    pats = [re.compile(t, re.I) for t in terms]
    hits = search(pats)
    print(indent + 'terms %s: %d hit(s) in the kit, the portal and the open kit PRs' % (terms, len(hits)))
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
        print('\n%sHits are candidate prior art: read hypotheses and conclusions before deciding equivalence.' % indent)
    return len(hits)


def snapshot_units(units):
    """Track full source and portal metadata, not moving commit URLs or declaration names alone."""
    return {'%s|%s' % (k, n): (k, n, u, t) for k, n, u, t in units
            if k in ('kit source', 'portal source', 'portal', 'open PR', 'open PR comment', 'PR source')}


def fingerprints(units):
    return {key: hashlib.sha256(unit[3].encode('utf-8')).hexdigest() for key, unit in units.items()}


def snapshot_changes(previous, current):
    return (sorted(current.keys() - previous.keys()),
            sorted(k for k in current.keys() & previous.keys() if current[k] != previous[k]),
            sorted(previous.keys() - current.keys()))


def new_since_last():
    """Report new or changed source files and portal entries since this host's last complete check."""
    line, ok = refresh(force=True)
    print(line)
    if not ok or 'REFRESH FAILED' in line:
        print('Daily checkpoint NOT advanced: refresh incomplete; cached searches remain available.')
        return 1
    units = snapshot_units(all_units())
    current = fingerprints(units)
    try:
        with open(CHECKED) as fh:
            last = json.load(fh)
        previous = last.get('fingerprints')
    except (OSError, ValueError):
        last, previous = None, None
    if previous is None:
        print('No content baseline (first check or old key-only format): establishing baseline; '
              'earlier changes cannot be inferred (%d entries/files).' % len(units))
    else:
        added, changed, gone = snapshot_changes(previous, current)
        print('%d added, %d changed, %d no longer listed since the last complete check' %
              (len(added), len(changed), len(gone)))
        for prefix, keys in [('+', added), ('~', changed)]:
            for key in keys:
                kind, name, url, text = units[key]
                print('\n%s %s  %s  %s' % (prefix, kind, name, url))
                print('      ' + ' '.join(norm(text).split())[:300])
        for key in gone:
            print('- %s' % key.replace('|', '  '))
    tmp = CHECKED + '.tmp'
    with open(tmp, 'w') as fh:
        json.dump({'fingerprints': current, 'stamp': stamp()}, fh)
    os.replace(tmp, CHECKED)
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
    # L1149 controls, frozen before the first run. They depend on the live PR list: while #55 is open, "prefix clock"
    # must find it (after a merge, the kit's own module must), and while #51 is open, Troy Lowry's 04:35 comment on it
    # must be found as an open PR comment.
    nums = {p['number'] for p in load_prs()}
    checks += [
        (['prefix clock'], lambda h: any(x[1].startswith('#55 ') for x in h) if 55 in nums
            else any(x[0].startswith('kit') and 'PrefixClock' in x[1] for x in h)),
        (['arbitrary-finite-seed bridge'], lambda h: any(x[0] == 'open PR comment' and x[1].startswith('#51 ')
            for x in h) if 51 in nums else True),
        # Repaired after the first run (L1149): the original third control asked for a 'PR module' unit, whose text is
        # only the header docstring, and #55's header does not name its own module. It now asks for the source unit.
        (['RightPrefixClock'], lambda h: any(x[0] == 'PR source' and
            x[1] == '#55 Ruliology.CellularAutomata.Rule30RightPrefixClock' for x in h) if 55 in nums else True),
        (['evol_right_diagonal_half'], lambda h: any(x[0] == 'PR declaration' and x[1] ==
            '#55 Ruliology.CellularAutomata.Rule30RightPrefixBound.evol_right_diagonal_half' for x in h)
            if 55 in nums else True),
    ]
    bad = 0
    if not nums:
        print('FAIL  the open PR index is empty or missing')
        bad = 1
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
