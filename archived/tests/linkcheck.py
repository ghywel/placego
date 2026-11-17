#!/usr/bin/env python3
"""Check every relative link in this directory's documents, as the public copy sees them.

    ./linkcheck.py [root]          (default: the directory above tests/, i.e. scripts/)

The public copy of this project is the CONTENTS of scripts/, so a link is good only if it resolves to a file or
directory inside that root. A link that climbs out of it (`../ROADMAP.md` from the top level) works in the
development repository and is broken in the copy; a check run from the repository cannot see that, which is how
three such links went unnoticed until 2026-10-01. Also checks `#anchors` against the target document's headings,
using GitHub's slug rule (lower case, punctuation dropped, spaces to hyphens).

Prints each bad link with its file and line, then a count; exits 1 if any is bad. Skips AppleDouble `._*` files.
"""
import os
import re
import sys

root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LINK = re.compile(r"\]\(([^)\s]+)\)")


def slug(heading):
    h = heading.strip().lower()
    h = re.sub(r"[^\w\- ]", "", h)          # GitHub keeps letters, digits, underscores, hyphens and spaces
    return h.replace(" ", "-")


def anchors(path):
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return set()
    out, seen = set(), {}
    in_code = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        m = re.match(r"#{1,6} (.*)", line)
        if m and not in_code:
            s = slug(m.group(1))
            n = seen.get(s, 0)
            out.add(s if n == 0 else f"{s}-{n}")   # GitHub numbers repeated headings
            seen[s] = n + 1
    return out


bad, checked = [], 0
for d, dirs, files in os.walk(root):
    dirs[:] = [x for x in dirs if not x.startswith(".") and x != "__pycache__"]
    for f in files:
        if not f.endswith(".md") or f.startswith("._"):
            continue
        path = os.path.join(d, f)
        in_code = False
        for no, line in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
            if line.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            for m in LINK.finditer(line):
                link = m.group(1)
                if re.match(r"[a-z][a-z0-9+.-]*:", link):      # http:, https:, mailto: ...
                    continue
                checked += 1
                target, _, frag = link.partition("#")
                tpath = os.path.normpath(os.path.join(d, target)) if target else path
                rel = os.path.relpath(path, root)
                if not (tpath == root or tpath.startswith(root + os.sep)):
                    bad.append(f"{rel}:{no}: {link} -- leaves the tree")
                elif not os.path.exists(tpath):
                    bad.append(f"{rel}:{no}: {link} -- no such file")
                elif frag and tpath.endswith(".md") and frag not in anchors(tpath):
                    bad.append(f"{rel}:{no}: {link} -- no heading #{frag}")

for b in bad:
    print(b)
print(f"{checked} relative links, {len(bad)} bad")
sys.exit(1 if bad else 0)
