#!/usr/bin/env python3
"""The full-cell gate as applied to submission 14 (Local, 2026-10-24, L859): the W7 revision 2 gate (reference cells pinned
by byte digest, LeanLink's per-run temporary module name normalised in cells 4 and 10, the semantic predicates) plus ONE
further documented normalisation found necessary at the first real comparison: the Wolfram summary boxes of the
LeanEnvironment and Success cells carry a per-session object identifier (a 40-plus-digit integer, as the `BoxID` option and
once more among the box's interpretation arguments). The gate first proves that the identifier is the ONLY difference
(exactly one such integer per file, the same number of occurrences, texts equal after replacing it) and records that proof,
then normalises it. Everything else is W7 revision 2's `cell_gate`, imported (nothing runs on import).

usage: python3 nb_gate.py CELLS_DIR REF_DIR
"""
import json, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tests', 'probes', 'wolfram'))
import w7_notebook as W

BOXID_RE = re.compile(r'\b\d{40,}\b')


def boxid_proof(a, b):
    """The only difference between a and b is one per-session identifier: returns (ok, detail)."""
    ia, ib = sorted(set(BOXID_RE.findall(a))), sorted(set(BOXID_RE.findall(b)))
    detail = {'ids_in_reference': len(ia), 'ids_in_candidate': len(ib), 'occurrences_reference': sum(a.count(x) for x in ia),
              'occurrences_candidate': sum(b.count(x) for x in ib), 'lengths': (len(a), len(b))}
    if len(ia) != 1 or len(ib) != 1 or detail['occurrences_reference'] != detail['occurrences_candidate']:
        return False, detail
    detail['equal_after_replacing_the_identifier'] = a.replace(ia[0], '<boxid>') == b.replace(ib[0], '<boxid>')
    return detail['equal_after_replacing_the_identifier'], detail


def main(cells, ref):
    okref, got = W.verify_reference(ref)
    out = {'reference_bound': okref}
    if not okref:
        out['verdict'] = 'FAIL'; out['why'] = 'reference payloads not the pinned bytes'; print(json.dumps(out, indent=1)); return 1
    # the W7 revision 2 gate first, unchanged
    v1, rep1 = W.cell_gate(cells, ref)
    out['w7_gate'] = {'verdict': v1, 'problems': rep1['problems']}
    # the per-session identifier proof on the cells W7 reported as differing
    proofs = {}
    for prob in rep1['problems']:
        m = re.match(r'cell (\d+) differs', prob)
        if not m: out['verdict'] = 'FAIL'; out['why'] = 'a problem other than a cell difference: ' + prob; print(json.dumps(out, indent=1)); return 1
        i = int(m.group(1))
        a = W.normalise(i, open(os.path.join(ref, 'cell-%02d.txt' % i), encoding='utf-8').read())
        b = W.normalise(i, open(os.path.join(cells, 'cell-%02d.txt' % i), encoding='utf-8').read())
        ok, detail = boxid_proof(a, b); proofs[i] = {'only_difference_is_one_session_identifier': ok, **detail}
        if not ok: out['proofs'] = proofs; out['verdict'] = 'FAIL'; out['why'] = 'cell %d differs beyond a session identifier' % i; print(json.dumps(out, indent=1)); return 1
    out['session_identifier_proofs'] = proofs
    # the semantic predicates on every cell, re-checked here after both normalisations
    sem = {}
    for i, needles in W.SEMANTIC.items():
        t = BOXID_RE.sub('<boxid>', W.normalise(i, open(os.path.join(cells, 'cell-%02d.txt' % i), encoding='utf-8').read()))
        sem[i] = all(n in t for n in needles)
    out['semantic_predicates'] = sem
    out['verdict'] = 'PASS' if all(sem.values()) and out['w7_gate']['verdict'] in ('pass', 'FAIL') else 'FAIL'
    print(json.dumps(out, indent=1)); return 0 if out['verdict'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
