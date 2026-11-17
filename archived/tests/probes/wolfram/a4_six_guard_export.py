#!/usr/bin/env python3
"""Pure strict exporter for the carried/certified GC2613 six-cell clause.

The caller supplies physical-cell metadata and a parsed, immutable host
CNF. Positive variable IDs denote black cells. No root/path units enter
the returned proof. This module performs no file writes or subprocesses.
"""

COORDS = ([(0, j) for j in range(7)] + [(1, j) for j in range(1, 8)]
          + [(2, j) for j in range(2, 7)] + [(3, j) for j in range(3, 6)] + [(4, 4)])
GATE_COORDS = ([(0, j) for j in range(1, 6)] + [(1, j) for j in range(2, 7)]
               + [(2, j) for j in range(3, 6)] + [(3, 4)])
H = (-1, -2, -3, 4, -5, -6)
ADDITIONS = (
    ((17, -18, 22), (99, 100)),
    ((17, -19, 22), (98, 100)),
    ((-17, -18, -22), (103, 104)),
    ((-17, -19, -22), (102, 104)),
    ((-10, -11, 12, 22), (63, 113, 114, 69, 75, 76)),
    ((10, -11, 12, -22), (59, 115, 116, 69, 75, 76)),
    (H + (-8,), (8,)),
    (H + (-9,), (15,)),
    (H + (-10,), (22,)),
    (H + (11,), (28,)),
    (H + (-12,), (39, 40)),
    (H + (-15,), (119, 120, 121, 41)),
    (H + (16,), (120, 121, 122, 50)),
    (H + (17,), (121, 122, 123, 59)),
    (H + (20,), (124, 125, 126, 84)),
    (H + (-21,), (125, 126, 95, 96)),
    (H + (-22,), (121, 122, 123, 118)),
    (H + (23,), (127, 128, 129, 109)),
)


class Unsupported(ValueError):
    pass


def _require(test, message):
    if not test:
        raise Unsupported(message)


def _positive_int(value):
    return type(value) is int and value > 0


def _gate(vs):
    a, b, c, d = vs
    for k in range(8):
        bits = ((k >> 2) & 1, (k >> 1) & 1, k & 1)
        value = bits[0] ^ (bits[1] | bits[2])
        yield tuple(-v if bit else v for v, bit in zip((a, b, c), bits)) + (d if value else -d,)


def export(host, cells, gate_rows, t, x, first_id=None):
    """Return all18 remapped additions only after the entire support validates.

    host: positive clause ID -> ordered literal tuple.
    cells: (time,position) -> positive host variable ID, black=true.
    gate_rows: (input time,output position) -> eight host clause IDs,
      in increasing binary input order 000,...,111.
    The cell metadata itself must come from the trusted host encoder;
    a bare CNF does not identify physical coordinates.
    """
    _require(type(t) is int and t >= 0 and type(x) is int, 'BAD_PLACEMENT')
    _require(bool(host) and all(_positive_int(i) for i in host), 'BAD_HOST_IDS')
    if first_id is None:
        first_id = max(host) + 1
    _require(_positive_int(first_id) and first_id > max(host), 'NONFRESH_ADDITION_IDS')
    physical = [(t + dt, x + dx) for dt, dx in COORDS]
    _require(all(c in cells for c in physical), 'MISSING_CELL')
    vm = {i + 1: cells[c] for i, c in enumerate(physical)}
    _require(all(_positive_int(v) for v in vm.values()), 'BAD_CELL_ID')
    _require(len(set(vm.values())) == 23, 'ALIASED_CELLS')
    cm = {}; support = {}
    for k, (dt, dx) in enumerate(GATE_COORDS):
        key = (t + dt, x + dx)
        _require(key in gate_rows, 'MISSING_GATE')
        ids = gate_rows[key]
        _require(len(ids) == 8 and all(_positive_int(i) and i in host for i in ids), 'MISSING_GATE_ROW')
        parent_coords = ((key[0], key[1]-1), (key[0], key[1]),
                         (key[0], key[1]+1), (key[0]+1, key[1]))
        _require(all(c in cells for c in parent_coords), 'MISSING_GATE_CELL')
        vs = tuple(cells[c] for c in parent_coords)
        for j, (cid, expected) in enumerate(zip(ids, _gate(vs))):
            _require(cid not in support, 'ALIASED_GATE_ROWS')
            _require(tuple(host[cid]) == expected, 'GATE_BYTES_MISMATCH')
            cm[1 + 8*k + j] = cid
            support[cid] = expected
    _require(len(support) == 112, 'WRONG_SUPPORT_SIZE')
    proof = []
    for i, (clause, hints) in enumerate(ADDITIONS):
        cid = first_id + i
        mapped = tuple(vm[abs(v)] * (1 if v > 0 else -1) for v in clause)
        hs = tuple(cm[h] for h in hints)
        _require(all(h in support or first_id <= h < cid for h in hs), 'NON_GATE_DEPENDENCY')
        proof.append((cid, mapped, hs)); cm[113 + i] = cid
    return {'placement': (t, x), 'variables': vm, 'support_ids': sorted(support),
            'clause': proof[-1][1], 'proof': proof}
