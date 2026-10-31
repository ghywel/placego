#!/usr/bin/env python3
"""make_ether_episode_catalog.py: the kit-catalog form of lean/Rule30EtherEpisode.lean, now that PR #69's
Rule30EtherGrounding is on kit main e5e1728 (Local, L1268).

RUN-ON:     cpu, instant
COMMAND:    python3 tests/probes/wolfram/make_ether_episode_catalog.py OUT_FILE

From the reviewed v2 source: `public import Rule30EtherGrounding` beside `Rule30FrozenRuler`; `open Rule30EtherGrounding
(ether ether_step)` in place of the module's verbatim copy of `ether` and its reproof of `ether_step` (same name, same
statement, both in Rule30EtherGrounding's exposed section); no `#print axioms` lines; docstrings that state the claim and
the method without credits or record IDs (the kit's README row carries the credit). The script refuses any other change
to a code line, and any internal reference left in the text.
"""
import hashlib
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SRC = os.path.join(ROOT, 'lean', 'Rule30EtherEpisode.lean')
SRC_SHA = '2ea831a9de66fefc63e621a218f49e53ed4230f41a15577bfa8e4b01c3c95c22'

REMOVE = [
    # the copied definition (and its docstring)
    "/-- PR69's ether (`Rule30EtherGrounding.ether`), copied verbatim: four spatial columns of the\n"
    "one-in-four ether, bit `t` read in time order. -/\n"
    "def ether (i t : Nat) : Bool :=\n"
    "  (match i % 4 with\n"
    "   | 0 => 43 | 1 => 202 | 2 => 178 | _ => 172).testBit (t % 8)\n\n",
]
STEP_START = "/-- PR69's `ether_step` (positive control): the ether is a two-sided solution of the edge rule. -/\n"
STEP_END = "  exact h\n\n"

STRUCTURAL = [
    ("module\n\npublic import Ruliology.CellularAutomata.Rule30FrozenRuler\n",
     "module\n\npublic import Ruliology.CellularAutomata.Rule30FrozenRuler\n"
     "public import Ruliology.CellularAutomata.Rule30EtherGrounding\n"),
    ("open Rule30FrozenRuler\n", "open Rule30FrozenRuler\nopen Rule30EtherGrounding (ether ether_step)\n"),
]

DOCS = [
    ("(the edge map `T`). PR69 (`Rule30EtherGrounding`) introduced in this frame the four-column,",
     "(the edge map `T`). `Rule30EtherGrounding` introduced in this frame the four-column,"),
    ("* `episode_witness`: GC2328's witness (`x 0 = 1`, `x j = ether (j + 3) 1` for `j ≥ 1`) has an",
     "* `episode_witness`: the witness `wit` (`x 0 = 1`, `x j = ether (j + 3) 1` for `j ≥ 1`) has an"),
    ("* `wit_episode` names the witness, and `episode_witness_finite` cuts it after bit `k + 1`: a finite row\n"
     "  attains `Lw k` too (prefix autonomy).",
     "* `wit_episode` names the witness, and `episode_witness_finite` cuts it after bit `k + 1`: a code with\n"
     "  no black bit beyond `k + 1` attains `Lw k` too (prefix autonomy). Through `code` and `edge_evol` such\n"
     "  a code is the edge code of a finite row; that translation is not restated here."),
    ("Scope: a moving black right edge in PR69's frame.",
     "Scope: a moving black right edge in the frame of `Rule30EtherGrounding`."),
    ("**Provenance.** Local's (Claude's) hand proof \"Proof 1: a front potential\" (inquisition round 5,\n"
     "L1259), carried two-party by GPT in GC2333 (which also supplied the scope repair: right-bounded\n"
     "mismatch rather than finite support). The finite tables mirror the round's certificate\n"
     "`ether_front_potential_certificate.py`. The method, a front state with a potential certified on\n"
     "local patterns, is the kit's `Rule30EtherThreeErosion` (period-three ether). The ether, its frame\n"
     "and `ether_step` are PR69's `Rule30EtherGrounding`, not in this kit build: `ether` is copied here\n"
     "verbatim.",
     "**Method.** The finite tables mirror a separate certificate of the same 32 cases. The method, a front\n"
     "state with a potential certified on local patterns, is that of `Rule30EtherThreeErosion`\n"
     "(period-three ether). `ether` and `ether_step` are `Rule30EtherGrounding`'s."),
    ("the pair at depths `k, k + 1` is not PR69's ether pair",
     "the pair at depths `k, k + 1` is not the ether pair"),
    ("/-- GC2328's witness: bit `0` black, `x j = ether (j + 3) 1` for `j ≥ 1`. -/",
     "/-- The witness: bit `0` black, `x j = ether (j + 3) 1` for `j ≥ 1`. -/"),
    ("/-- **The witness.** For every `k ≥ 1` the GC2328 witness carries PR69's ether pair at depths",
     "/-- **The witness.** For every `k ≥ 1` the witness `wit` carries the ether pair at depths"),
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
FORBIDDEN = ['GC2', 'GC1', 'L12', 'L11', 'CL6', "round's", 'round 5', 'Local', 'Proof 1', 'inquisition', 'ledger',
             'PR69', 'copied', 'Lowry', 'Claude', 'GPT']


def code_lines(text, drop):
    res, depth = [], 0
    for ln in text.split('\n'):
        if depth == 0 and not ln.lstrip().startswith('/-') and not any(ln.startswith(d) for d in drop) and ln.strip():
            res.append(ln)
        depth = max(depth + ln.count('/-') - ln.count('-/'), 0)
    return res


def main():
    if len(sys.argv) != 2:
        sys.exit('usage: make_ether_episode_catalog.py OUT_FILE')
    src = open(SRC, encoding='utf-8').read()
    if hashlib.sha256(src.encode('utf-8')).hexdigest() != SRC_SHA:
        sys.exit('REFUSED: source is not the reviewed v2')
    out = src[:src.index(PRINT_BLOCK_START) + 1]
    removed = []
    for block in REMOVE:
        if out.count(block) != 1:
            sys.exit('REFUSED: ether definition block not found exactly once')
        out = out.replace(block, '')
        removed.append(block)
    a, b = out.index(STEP_START), None
    b = out.index(STEP_END, a) + len(STEP_END)
    step_block = out[a:b]
    if 'theorem ether_step (i t : Nat) :' not in step_block or step_block.count('theorem') != 1:
        sys.exit('REFUSED: unexpected ether_step block')
    out = out[:a] + out[b:]
    removed.append(step_block)
    for old, new in STRUCTURAL + DOCS:
        if out.count(old) != 1:
            sys.exit(f'REFUSED: {out.count(old)} matches for {old[:60]!r}')
        out = out.replace(old, new)
    for word in FORBIDDEN:
        if word in out:
            sys.exit(f'REFUSED: {word!r} left at lines {[k + 1 for k, ln in enumerate(out.split(chr(10))) if word in ln]}')
    drop = ('module', 'public import', '@[expose]', 'namespace', 'end Ruliology', 'open ', '#print')
    removed_code = [ln for blk in removed for ln in code_lines(blk, drop)]
    orig = code_lines(src[:src.index(PRINT_BLOCK_START) + 1], drop)
    for ln in removed_code:
        orig.remove(ln)
    if orig != code_lines(out, drop):
        sys.exit('REFUSED: a code line changed beyond the two removed blocks')
    with open(sys.argv[1], 'w', encoding='utf-8') as f:
        f.write(out)
    print(f'{len(orig)} code lines kept, {len(removed_code)} removed (ether, ether_step); wrote {len(out.splitlines())} '
          f'lines, SHA256 {hashlib.sha256(out.encode("utf-8")).hexdigest()}')


if __name__ == '__main__':
    main()
