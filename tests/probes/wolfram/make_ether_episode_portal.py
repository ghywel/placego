#!/usr/bin/env python3
"""make_ether_episode_portal.py: the portal form of the M(k) module for the verifier's image 14 at kit e5e1728e,
which includes Rule30EtherGrounding (Local, L1271, after GC2338).

RUN-ON:     cpu, instant
COMMAND:    python3 tests/probes/wolfram/make_ether_episode_portal.py

Supersedes make_ether_episode_submission.py, whose form copied PR #69's `ether` for the verifier's earlier kit 842b756f.
This form starts from the catalog form of kit PR #71 (kit-pr/Rule30EtherEpisode.lean, which GPT passed in GC2338) and
changes only its frame: plain imports of the official statements (`Rule30Prize`), `Rule30FrozenRuler` and
`Rule30EtherGrounding`; no `@[expose] public section`; the namespace `Rule30Submission` with `open
Ruliology.CellularAutomata`, and the two `open` lines written with full names. The script refuses any other change to a
code line and checks that each replacement matches exactly once.
"""
import hashlib
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
FOLDER = os.path.join(ROOT, 'reports', 'wolfram-agents', 'submissions', 'ether-episode')
SRC = os.path.join(FOLDER, 'kit-pr', 'Rule30EtherEpisode.lean')
OUT = os.path.join(FOLDER, 'Rule30Submission.lean')
SRC_SHA = '615998d207a495dc2b15f69ff0ed73474303bd500868860dbcfe6d8a43b6883a'

STRUCTURAL = [
    ("module\n\npublic import Ruliology.CellularAutomata.Rule30FrozenRuler\n"
     "public import Ruliology.CellularAutomata.Rule30EtherGrounding\n",
     "import Ruliology.CellularAutomata.Rule30Prize\nimport Ruliology.CellularAutomata.Rule30FrozenRuler\n"
     "import Ruliology.CellularAutomata.Rule30EtherGrounding\n"),
    ("@[expose] public section\n\nnamespace Ruliology.CellularAutomata.Rule30EtherEpisode\n", "namespace Rule30Submission\n"),
    ("open Rule30FrozenRuler\nopen Rule30EtherGrounding (ether ether_step)\n",
     "open Ruliology.CellularAutomata\nopen Ruliology.CellularAutomata.Rule30FrozenRuler\n"
     "open Ruliology.CellularAutomata.Rule30EtherGrounding (ether ether_step)\n"),
    ("end Ruliology.CellularAutomata.Rule30EtherEpisode\n", "end Rule30Submission\n"),
]


def code_lines(text, drop):
    res, depth = [], 0
    for ln in text.split('\n'):
        if depth == 0 and not ln.lstrip().startswith('/-') and not any(ln.startswith(d) for d in drop) and ln.strip():
            res.append(ln)
        depth = max(depth + ln.count('/-') - ln.count('-/'), 0)
    return res


def main():
    src = open(SRC, encoding='utf-8').read()
    if hashlib.sha256(src.encode('utf-8')).hexdigest() != SRC_SHA:
        sys.exit('REFUSED: the catalog form is not the one passed in GC2338 (615998d2)')
    out = src
    for old, new in STRUCTURAL:
        if out.count(old) != 1:
            sys.exit(f'REFUSED: {out.count(old)} matches for {old[:60]!r}')
        out = out.replace(old, new)
    a = code_lines(src, ('module', 'public import', '@[expose]', 'namespace', 'end Ruliology', 'open '))
    b = code_lines(out, ('import ', 'namespace', 'end Rule30Submission', 'open '))
    if a != b:
        sys.exit('REFUSED: a code line changed')
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(out)
    print(f'catalog form {SRC_SHA[:16]}..., {len(a)} code lines unchanged; wrote {os.path.relpath(OUT, ROOT)}: '
          f'{len(out.splitlines())} lines, SHA256 {hashlib.sha256(out.encode("utf-8")).hexdigest()}')


if __name__ == '__main__':
    main()
