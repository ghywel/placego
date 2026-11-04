"""Locate the shortest fixed contiguous observation that identifies the seed branch.

Compare one snapshot, at a known primitive anchor phase, against the seed at the
same phase. Each competitor must differ at least once in that window at every phase.
"""
import hashlib
import json
import os
from pathlib import Path
import struct

LO, K, P = 11998, 87867, 16
DIGESTS = ('28c4a4cedc03b34a827efc87342e76bbaecdfc5b5127d68f40a42300075c4d40',
           'aef194bcd18ebb0dc44d24abe1b3e0a628d4a6871ba643b0f041aa08b7647b9c',
           '781b5c9eedac7413ec838ff3ab1f309def40be09513db1d26cf8a4952525ae15',
           '0326baea5f28b89ff8229b914149fc78bdab47c0ff024e078d8df692a8b0690a')


def main():
    root = Path(os.environ['WHITE_TREE_DIR'])
    leaves = []
    for i,h in enumerate(DIGESTS):
        data = (root/f'leaf-{i}.u16le').read_bytes()
        assert hashlib.sha256(data).hexdigest() == h
        leaves.append([x for x, in struct.iter_unpack('<H',data)])
    ref = leaves[1]
    assert len(ref) == K-LO
    diffs = [[v ^ w for v,w in zip(ref,leaves[i])] for i in (0,2,3)]
    # Every alternative/phase must have a witness between start and end.
    last = [[None]*P for _ in diffs]
    earliest = [None]*P
    best, matching = K+1, []
    for pos, ds in enumerate(zip(*diffs),LO):
        simultaneous = ds[0] & ds[1] & ds[2]
        for r in range(P):
            if earliest[r] is None and (simultaneous >> r) & 1:
                earliest[r] = pos
        for i,d in enumerate(ds):
            for r in range(P):
                if (d >> r) & 1:
                    last[i][r] = pos
        if any(v is None for row in last for v in row):
            continue
        start = min(min(row) for row in last)
        width = pos-start+1
        if width < best:
            best, matching = width, []
        if width == best:
            matching.append([start,pos])

    def detects(start,width):
        for diff in diffs:
            covered = 0
            for d in diff[start:start+width]:
                covered |= d
            if covered != 65535:
                return False
        return True
    # Independently test every window one tick shorter and every attaining position.
    assert best >= 1 and all(v is not None for v in earliest)
    assert not any(detects(i,best-1) for i in range(len(ref)-(best-1)+1))
    assert matching == [[LO+i,LO+i+best-1] for i in range(len(ref)-best+1) if detects(i,best)]
    assert all((d[53208-LO] | d[58287-LO]) == 65535 for d in diffs)
    a,b = matching[0]
    signatures = []
    for r in range(P):
        vals = [sum(((w[j-LO] >> r) & 1) << (j-a) for j in range(a,b+1)) for w in leaves]
        assert vals[1] not in [vals[0],vals[2],vals[3]]
        signatures.append(vals)
    res = dict(earliest_by_phase=earliest,shortest_width=best,windows=matching,
               example_signatures=signatures,bit_order='lowest wheel = least significant bit')
    (Path(os.environ['CAPPED_OUT'])/'readout.json').write_text(json.dumps(res,indent=2)+'\n')
    print('SPATIAL_READOUT_DONE',best,matching[:2],len(matching))


if __name__ == '__main__':
    main()
