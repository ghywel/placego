#!/usr/bin/env python3
"""make_ether_episode_submission.py: the portal form of lean/Rule30EtherEpisode.lean (Local, L1267).

RUN-ON:     cpu, instant
COMMAND:    python3 tests/probes/wolfram/make_ether_episode_submission.py

Mechanical, like the ring-orbits form (RUN-SPEC there): the catalog module's `module` header and `public import`
become plain imports of the official statements (`Rule30Prize`) and `Rule30FrozenRuler`; `@[expose] public section`
goes; the namespace becomes `Rule30Submission` with `open Ruliology.CellularAutomata`; the trailing `#print axioms`
lines go (the checker reports axioms, and the check wants an empty compiler output). Docstrings that cite internal
record IDs get public wording. No proof, statement or definition line changes: the script checks that every changed
line is a header, namespace, `open`, `#print` or comment line, and that each replacement matches exactly once.
"""
import hashlib
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SRC = os.path.join(ROOT, 'lean', 'Rule30EtherEpisode.lean')
OUT = os.path.join(ROOT, 'reports', 'wolfram-agents', 'submissions', 'ether-episode', 'Rule30Submission.lean')
SRC_SHA = '2ea831a9de66fefc63e621a218f49e53ed4230f41a15577bfa8e4b01c3c95c22'

STRUCTURAL = [
    ("module\n\npublic import Ruliology.CellularAutomata.Rule30FrozenRuler\n",
     "import Ruliology.CellularAutomata.Rule30Prize\nimport Ruliology.CellularAutomata.Rule30FrozenRuler\n"),
    ("@[expose] public section\n\nnamespace Ruliology.CellularAutomata.Rule30EtherEpisode\n",
     "namespace Rule30Submission\n"),
    ("open Rule30FrozenRuler\n",
     "open Ruliology.CellularAutomata\nopen Ruliology.CellularAutomata.Rule30FrozenRuler\n"),
    ("end Ruliology.CellularAutomata.Rule30EtherEpisode\n", "end Rule30Submission\n"),
]

DOCS = [
    ("(the edge map `T`). PR69 (`Rule30EtherGrounding`) introduced in this frame the four-column,",
     "(the edge map `T`). Kit pull request #69 (`Rule30EtherGrounding`) introduced in this frame the four-column,"),
    ("* `episode_witness`: GC2328's witness (`x 0 = 1`, `x j = ether (j + 3) 1` for `j ≥ 1`) has an",
     "* `episode_witness`: the witness `wit` (`x 0 = 1`, `x j = ether (j + 3) 1` for `j ≥ 1`) has an"),
    ("* `wit_episode` names the witness, and `episode_witness_finite` cuts it after bit `k + 1`: a finite row\n"
     "  attains `Lw k` too (prefix autonomy).",
     "* `wit_episode` names the witness, and `episode_witness_finite` cuts it after bit `k + 1`: a code with\n"
     "  no black bit beyond `k + 1` attains `Lw k` too (prefix autonomy). Through the kit's `code` and\n"
     "  `edge_evol` such a code is the edge code of a finite row; that translation is not restated here."),
    ("Scope: a moving black right edge in PR69's frame.", "Scope: a moving black right edge in the frame of PR #69."),
    ("**Provenance.** Local's (Claude's) hand proof \"Proof 1: a front potential\" (inquisition round 5,\n"
     "L1259), carried two-party by GPT in GC2333 (which also supplied the scope repair: right-bounded\n"
     "mismatch rather than finite support). The finite tables mirror the round's certificate\n"
     "`ether_front_potential_certificate.py`. The method, a front state with a potential certified on\n"
     "local patterns, is the kit's `Rule30EtherThreeErosion` (period-three ether). The ether, its frame\n"
     "and `ether_step` are PR69's `Rule30EtherGrounding`, not in this kit build: `ether` is copied here\n"
     "verbatim.",
     "**Sources.** The argument above was written by hand and read independently before this\n"
     "formalization; its finite tables mirror a separate Python certificate of the same 32 cases. The\n"
     "method, a front state with a potential certified on local patterns, is that of the kit's\n"
     "`Rule30EtherThreeErosion` (period-three ether). The ether, its frame and `ether_step` are from kit\n"
     "pull request #69 (`Rule30EtherGrounding`, by Troy Lowry), which is not in this kit build: `ether`\n"
     "is copied here verbatim."),
    ("/-- PR69's ether (`Rule30EtherGrounding.ether`), copied verbatim: four spatial columns of the",
     "/-- The ether of PR #69 (`Rule30EtherGrounding.ether`), copied verbatim: four spatial columns of the"),
    ("/-- GC2328's witness: bit `0` black, `x j = ether (j + 3) 1` for `j ≥ 1`. -/",
     "/-- The witness: bit `0` black, `x j = ether (j + 3) 1` for `j ≥ 1`. -/"),
    ("/-- **The witness.** For every `k ≥ 1` the GC2328 witness carries PR69's ether pair at depths",
     "/-- **The witness.** For every `k ≥ 1` the witness `wit` carries the ether pair at depths"),
    ("/-- PR69's `ether_step` (positive control): the ether is a two-sided solution of the edge rule. -/",
     "/-- The `ether_step` of PR #69 (positive control): the ether is a two-sided solution of the edge rule. -/"),
    ("the pair at depths `k, k + 1` is not PR69's ether pair",
     "the pair at depths `k, k + 1` is not the ether pair of PR #69"),
    ("/-- The bases `M(1..8) = 4, 4, 6, 6, 7, 7, 8, 8` of the round's exhaustive computation. -/",
     "/-- `Lw 1 .. Lw 8 = 4, 4, 6, 6, 7, 7, 8, 8`, the longest episodes at depths `1 .. 8` found by an\n"
     "exhaustive computation over the codes. -/"),
    ("/-! ### The witness named, and a finite witness (v2, L1265) -/",
     "/-! ### The witness named, and a finite witness -/"),
    ("/-- `episode_witness` with its witness named: the GC2328 code `wit` itself carries the pair. -/",
     "/-- `episode_witness` with its witness named: the code `wit` itself carries the pair. -/"),
    ("/-- **A finite witness.** For every `k ≥ 1` a code with no black bit beyond `k + 1` (a finite row)\n"
     "carries PR69's ether pair at depths `k, k + 1` on the ticks `0 .. Lw k - 1`.",
     "/-- **A finite witness.** For every `k ≥ 1` a code with no black bit beyond `k + 1` carries the\n"
     "ether pair at depths `k, k + 1` on the ticks `0 .. Lw k - 1`."),
]

PRINT_BLOCK_START = "\nopen Ruliology.CellularAutomata.Rule30EtherEpisode in\n#print axioms episode_bound\n"
FORBIDDEN = ['GC2', 'GC1', 'L12', 'L11', 'CL6', "round's", 'round 5', 'Local', 'Proof 1', 'inquisition', 'ledger', 'PR69']


def main():
    src = open(SRC, encoding='utf-8').read()
    digest = hashlib.sha256(src.encode('utf-8')).hexdigest()
    if digest != SRC_SHA:
        sys.exit(f'REFUSED: source digest {digest} is not the reviewed v2 {SRC_SHA}')
    i = src.index(PRINT_BLOCK_START)
    tail = src[i:]
    if any(not (ln.startswith('open Ruliology.CellularAutomata.Rule30EtherEpisode in') or ln.startswith('#print axioms')
                or ln == '') for ln in tail.split('\n')):
        sys.exit('REFUSED: unexpected line after the namespace end')
    out = src[:i + 1]
    for old, new in STRUCTURAL + DOCS:
        n = out.count(old)
        if n != 1:
            sys.exit(f'REFUSED: {n} matches for {old[:60]!r}')
        out = out.replace(old, new)
    for word in FORBIDDEN:
        if word in out:
            lines = [k + 1 for k, ln in enumerate(out.split('\n')) if word in ln]
            sys.exit(f'REFUSED: internal reference {word!r} left at lines {lines}')
    # every changed line must be structural or inside a comment: compare the code lines of both files
    def code_lines(text, drop):
        res, depth = [], 0
        for ln in text.split('\n'):
            s = ln
            opened = s.count('/-') - s.count('-/')
            if depth == 0 and not s.lstrip().startswith('/-') and not any(s.startswith(d) for d in drop) and s.strip():
                res.append(s)
            depth += opened
            depth = max(depth, 0)
        return res
    drop_src = ('module', 'public import', '@[expose]', 'namespace', 'end Ruliology', 'open ', '#print')
    drop_out = ('import ', 'namespace', 'end Rule30Submission', 'open ')
    a, b = code_lines(src[:i + 1], drop_src), code_lines(out, drop_out)
    if a != b:
        diff = next(k for k, (x, y) in enumerate(zip(a, b)) if x != y) if len(a) == len(b) else min(len(a), len(b))
        sys.exit(f'REFUSED: a code line changed (first difference at code line {diff})')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(out)
    print(f'source v2 {SRC_SHA[:16]}..., {len(a)} code lines unchanged')
    print(f'wrote {os.path.relpath(OUT, ROOT)}: {len(out.splitlines())} lines, SHA256 '
          f'{hashlib.sha256(out.encode("utf-8")).hexdigest()}')


if __name__ == '__main__':
    main()
