"""GC2795 independent NumPy replay of every exported restricted-code subset.
Predicted no code rejection through32. Reads raw core words, full little-endian
bitmaps and transitions; computes four boundary choices per sampled step.
Fixed-point core membership suffices for positive inclusion; on a rejection,
also recompute the greatest fixed point from the previous core's full lift.
"""
import pathlib, sys
import numpy as np


def replay(folder):
    done = []
    for w in range(16, 33, 2):
        mf = folder / f"code-meta-{w}.txt"
        if not mf.exists():
            break
        n, nb, ns, nc = map(int, mf.read_text().split())
        core = np.array(list(map(int, (folder / f"code-core-{w}.txt").read_text().split())), dtype=np.uint64)
        assert len(core) == n and np.all(core[:-1] < core[1:])
        mask = np.uint64((1 << w) - 1)

        def step(a, x, y):
            # Two literal local Rule30 updates with the prescribed alternating
            # left boundary and free right boundary at each physical tick.
            b = a | (np.uint64(x) << np.uint64(w))
            a = ((b << np.uint64(1)) ^ (b | (b >> np.uint64(1)))) & mask
            b = a | (np.uint64(y) << np.uint64(w))
            return (((b << np.uint64(1)) | np.uint64(1)) ^ (b | (b >> np.uint64(1)))) & mask

        def gap(a, g):
            for k in range(1, g + 1):
                a = np.unique(np.concatenate([step(a, x, y) for x in (0, 1) for y in (0, 1)]))
                a = a[(a & np.uint64(1)) == np.uint64(k == g)]
            return a

        def block(a, k):
            for g in ((5,) if k == 0 else (3, 5, 5, 5)):
                a = gap(a, g)
            return a

        fixed = np.union1d(gap(core, 3), gap(core, 5))
        assert np.array_equal(fixed, core), (w, "CORE_FIXED_POINT")
        tr = [tuple(map(int, line.split())) for line in (folder / f"code-dfa-{w}.txt").read_text().splitlines()]
        assert len(tr) == ns
        raw = np.concatenate([np.fromfile(folder / f"code-bits-{w}-{k}.bin", dtype="<u8") for k in range(nc)])
        assert raw.size == nb * ns
        raw = raw.reshape(ns, nb)

        def decode(i):
            bits = np.unpackbits(raw[i].view(np.uint8), bitorder="little")
            assert not bits[n:].any()
            return core[np.flatnonzero(bits[:n])]

        assert np.array_equal(decode(0), core)
        for i, row in enumerate(tr):
            a = decode(i)
            assert a.size
            for k, j in enumerate(row):
                b = block(a, k)
                if j < 0:
                    assert b.size == 0
                else:
                    assert j < ns and np.array_equal(b, decode(j)), (w, i, k, j)
        for word in ((3, 3), (3, 5, 5, 3)):
            a = core
            for g in word:
                a = gap(a, g)
            assert not len(a)
        print("REPLAY", w, n, ns, "rejected", any(min(row) < 0 for row in tr), flush=True)
        done.append(w)

    bad = folder / "counterexample.txt"
    if bad.exists():
        w, word = bad.read_text().split()
        w = int(w)
        if w > 16:
            # Same projection theorem as GC2794; independent finite computation.
            old = np.array(list(map(int, (folder / f"code-core-{w-2}.txt").read_text().split())), dtype=np.uint64)
            a = np.unique(np.concatenate([old | np.uint64(h << (w-2)) for h in range(4)]))
            for _ in range(1000):
                b = np.union1d(gap(a, 3), gap(a, 5))
                assert np.isin(b, a).all()
                if np.array_equal(a, b):
                    break
                a = b
            else:
                raise AssertionError("CORE_ITER_CAP")
            assert np.array_equal(a, core)
        a = core
        for x in word:
            a = block(a, x == "B")
        assert not a.size
        print("COUNTEREXAMPLE_REPLAY", w, word, flush=True)
    print("S16_CODE_REPLAY_PASS", len(done), flush=True)


if __name__ == "__main__":
    replay(pathlib.Path(sys.argv[1]))
