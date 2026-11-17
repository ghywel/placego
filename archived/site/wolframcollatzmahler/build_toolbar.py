#!/usr/bin/env python3
"""build_toolbar.py: stamp the site toolbar from one template into every page.

The toolbar (the Contributors / other-works line, the Problems dropdown and the page links) is written once, in
templates/toolbar.inc. Each page carries it between the markers <!-- TOOLBAR --> and <!-- /TOOLBAR -->, placed
inside its header after the brand. This script fills in the page's relative path to the site root ({root}), marks the
link to the current page with aria-current="page", and marks the Problems menu "current" when the page is one of the
problems. The pages stay plain static files: they open from disk, and nothing runs on the server.

Usage (from anywhere):
    python3 site/wolframcollatzmahler/build_toolbar.py           # stamp every page; prints the pages it changed
    python3 site/wolframcollatzmahler/build_toolbar.py --check   # change nothing; exit 1 if any page is out of date

To add the toolbar to a new page, put <!-- TOOLBAR --><!-- /TOOLBAR --> inside its header and run the script.
The template is not a page: do not upload templates/ to the web server. Standard library only; running it twice changes
nothing.
"""
import argparse, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, 'templates', 'toolbar.inc')
START, END = '<!-- TOOLBAR -->', '<!-- /TOOLBAR -->'
# Pages that should light up another page's link: the worked Rule 30 page belongs under Wolfram.
ALIAS = {'rule30/index.html': 'wolfram.html'}


def stamp(rel, template):
    """The toolbar for the page at rel (a path relative to the site root, with forward slashes)."""
    depth = rel.count('/')
    root = '../' * depth
    current = ALIAS.get(rel, rel)
    html = template.replace('{root}', root).strip()

    def fix(m):
        href = m.group(1)
        target = os.path.normpath(os.path.join(os.path.dirname(rel), href)).replace(os.sep, '/')
        if target == current:
            own = os.path.basename(rel) if target == rel else href    # a link to this very page is written as its file name
            return f'<a href="{own}" aria-current="page">'
        return m.group(0)

    html = re.sub(r'<a href="([^"#:]+)">', fix, html)
    menu = re.search(r'<div class="menu-list">.*?</div>', html, re.S).group(0)
    if 'aria-current' in menu:
        html = html.replace('<details class="menu">', '<details class="menu current">', 1)
    return html


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--check', action='store_true'); a = ap.parse_args()
    template = open(TEMPLATE, encoding='utf-8').read()
    pages = sorted(glob.glob(os.path.join(HERE, '**', '*.html'), recursive=True))
    stale, unmarked = [], []
    for path in pages:
        rel = os.path.relpath(path, HERE).replace(os.sep, '/')
        if rel.startswith('templates/'):
            continue
        s = open(path, encoding='utf-8').read()
        if START not in s:
            if '<nav aria-label="Site">' in s:
                unmarked.append(rel)
            continue
        i, j = s.index(START) + len(START), s.index(END)
        new = s[:i] + stamp(rel, template) + s[j:]
        if new != s:
            stale.append(rel)
            if not a.check:
                open(path, 'w', encoding='utf-8').write(new)
    for rel in unmarked:
        print('has a toolbar but no markers:', rel)
    if a.check:
        print('out of date:' if stale else 'all pages match the template', *stale)
        sys.exit(1 if stale or unmarked else 0)
    print(f'{len(stale)} page(s) stamped' + (': ' + ', '.join(stale) if stale else ''))


if __name__ == '__main__':
    main()
