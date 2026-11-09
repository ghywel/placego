"""GC2796: extract a small set-cover certificate from completed code graphs.
For each nonempty K_i and each c in {A,B}, T_c(K_i) contains some K_j.
This gives every finite code word, without enumerating all its histories.
Prediction: a bounded-small cover (at most four sets) through28; counterfactual
is growth with width. Empty-set corruption is rejected by the nonempty guard.
"""
import json, pathlib, sys


def read(folder, w):
    n, nb, ns, nc = map(int, (folder / f"code-meta-{w}.txt").read_text().split())
    data = b"".join((folder / f"code-bits-{w}-{k}.bin").read_bytes() for k in range(nc))
    assert len(data) == nb * ns * 8
    sets = [int.from_bytes(data[k*nb*8:(k+1)*nb*8], "little") for k in range(ns)]
    tr = [tuple(map(int, s.split())) for s in (folder / f"code-dfa-{w}.txt").read_text().splitlines()]
    assert len(tr) == ns and sets[0] == (1 << n) - 1
    assert all(0 < x < (1 << n) for x in sets[1:])
    return n, sets, tr


def check_cover(sets, tr, chosen, cover):
    assert chosen and all(sets[i] for i in chosen)
    assert all(sets[i] & sets[0] == sets[i] for i in chosen)
    for i in chosen:
        for k in (0, 1):
            j = cover[str(i)][k]
            assert j in chosen and tr[i][k] >= 0
            a, b = sets[j], sets[tr[i][k]]
            assert a & b == a


def run(folder, output):
    results = []
    for w in range(16, 29, 2):
        n, sets, tr = read(folder, w)
        chosen = []
        for i in sorted(range(len(sets)), key=lambda i: (sets[i].bit_count(), i)):
            if not any(sets[i] & sets[j] == sets[j] for j in chosen):
                chosen.append(i)
        cover = {}
        for i in chosen:
            cover[str(i)] = []
            for k in (0, 1):
                q = tr[i][k]
                assert q >= 0
                cover[str(i)].append(next(j for j in chosen if sets[q] & sets[j] == sets[j]))
        check_cover(sets, tr, chosen, cover)
        corrupt = sets.copy()
        corrupt[chosen[0]] = 0
        try:
            check_cover(corrupt, tr, chosen, cover)
        except AssertionError:
            pass
        else:
            raise AssertionError("EMPTY_CERTIFICATE_ACCEPTED")
        result = {"width":w, "sets":len(sets), "core":n, "chosen":chosen,
                  "cardinalities":[sets[i].bit_count() for i in chosen], "cover":cover}
        (output / f"code-cover-{w}.json").write_text(json.dumps(result, indent=2)+"\n")
        print("COVER", w, len(chosen), result["cardinalities"], flush=True)
        results.append(result)
    print("S16_COVER_PASS",len(results),flush=True)


if __name__ == "__main__":
    run(pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]))
