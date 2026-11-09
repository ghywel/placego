"""GC2800: regression for the exempt-word guard, using only saved automata.
Prediction: no G1 witness16-28; toy forbidden basis F+{m} gives exactly m.
No core construction, physical trajectories or new widths.
"""
import json, pathlib, resource, runpy, sys

producer, kit, saved = map(pathlib.Path, sys.argv[1:])
sys.argv = [str(producer), str(kit)]  # load definitions; empty width list
ns = runpy.run_path(str(producer), run_name="gpt_review_import")
check = ns["g1_product"]
F = ns["F"]


def avoid(forbidden):
    words = {""}
    for word in forbidden:
        words.update(word[:k] for k in range(1, len(word)))
    states = sorted(words, key=lambda w: (len(w), w))
    ids = {s:i for i,s in enumerate(states)}
    tr = []
    for p in states:
        row = []
        for y in "35":
            w = p + y
            if any(w.endswith(f) for f in forbidden):
                row.append(-1)
            else:
                q = max((s for s in states if w.endswith(s)), key=len)
                row.append(ids[q])
        tr.append(row)
    return ns["np"].array(tr, dtype="int64")


rows = []
for w in range(16, 29, 2):
    tr = ns["np"].loadtxt(saved / f"dfa-{w}.txt", dtype="int64")
    n, bad = check(tr)
    assert not bad, (w, bad)
    rows.append({"width":w,"product_states":n,"bad":bad})

strings = {"".join(map(str, f)) for f in F}
assert check(avoid(strings))[1] == []
m = "355535355535353"
toy = check(avoid(strings | {m}))[1]
assert toy == [m], toy
print(json.dumps({"saved_checks":rows,"synthetic_witness":toy}), flush=True)
print("S16_G1_REVIEW_PASS", flush=True)
