#!/usr/bin/env python3
"""The full-cell gate (revision 2, 2026-10-24, GC1773: the exception restricted; revision 1, dd2399c4..., was the one APPLIED to submission 14): the W7 revision 2 gate (reference cells pinned
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


SESSION_ID_CELLS = {4}                                                     # revision 2: the exception applies to the LeanEnvironment summary cell only
POSITION_RES = (re.compile(r'LeanEnvironment, \d+, (\d{40,}), EvaluationBox\[\]'),   # the interpretation argument of the summary box
                re.compile(r'BoxID -> (\d{40,}),'))                                   # the BoxID option of the summary box


def boxid_proof(a, b, cell):
    """The only difference between a and b is one per-session identifier of the Wolfram summary box, at exactly its two
    structural positions (the interpretation argument and the BoxID option), in an allowed cell: returns (ok, detail)."""
    detail = {'cell': cell, 'cell_allowed': cell in SESSION_ID_CELLS, 'lengths': (len(a), len(b))}
    if cell not in SESSION_ID_CELLS:
        return False, detail
    ia, ib = sorted(set(BOXID_RE.findall(a))), sorted(set(BOXID_RE.findall(b)))
    detail.update({'ids_in_reference': len(ia), 'ids_in_candidate': len(ib), 'occurrences_reference': sum(a.count(x) for x in ia),
                   'occurrences_candidate': sum(b.count(x) for x in ib)})
    if len(ia) != 1 or len(ib) != 1 or detail['occurrences_reference'] != 2 or detail['occurrences_candidate'] != 2:
        return False, detail
    pos_a = [r.search(a).group(1) if r.search(a) else None for r in POSITION_RES]
    pos_b = [r.search(b).group(1) if r.search(b) else None for r in POSITION_RES]
    detail['at_the_two_structural_positions'] = pos_a == [ia[0], ia[0]] and pos_b == [ib[0], ib[0]]
    detail['equal_after_replacing_the_identifier'] = a.replace(ia[0], '<boxid>') == b.replace(ib[0], '<boxid>')
    return detail['at_the_two_structural_positions'] and detail['equal_after_replacing_the_identifier'], detail


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
        ok, detail = boxid_proof(a, b, i); proofs[i] = {'only_difference_is_one_session_identifier': ok, **detail}
        if not ok: out['proofs'] = proofs; out['verdict'] = 'FAIL'; out['why'] = 'cell %d differs beyond a session identifier' % i; print(json.dumps(out, indent=1)); return 1
    out['session_identifier_proofs'] = proofs
    # the semantic predicates on every cell, re-checked here after both normalisations
    sem = {}
    for i, needles in W.SEMANTIC.items():
        t = W.normalise(i, open(os.path.join(cells, 'cell-%02d.txt' % i), encoding='utf-8').read())
        if i in SESSION_ID_CELLS: t = BOXID_RE.sub('<boxid>', t)
        sem[i] = all(n in t for n in needles)
    out['semantic_predicates'] = sem
    out['verdict'] = 'PASS' if all(sem.values()) and out['w7_gate']['verdict'] in ('pass', 'FAIL') else 'FAIL'
    print(json.dumps(out, indent=1)); return 0 if out['verdict'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
