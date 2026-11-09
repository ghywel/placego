"""GC2801: independent scalar-cell review of ALL S16 certificate data.
Prediction: 3316 lift windows,13264 closed edges, exact752-start layers ending
empty, and three advertised witness paths.
No Lean or Wolfram execution; their exact-source receipts are checked separately.
"""
import ast, hashlib, json, pathlib, re, sys

kit, package, output = map(pathlib.Path, sys.argv[1:])
src = (package / "Rule30GateTrapLift.lean").read_text()
portal = (package / "Rule30Submission.lean").read_text()
trap_source = (kit / "lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean").read_text()
trap = set(map(int, re.findall(r"\d+", re.search(r"def trapCodes : List Nat := \[(.*?)\]", trap_source, re.S)[1])))
assert len(trap) == 829
lift = {a | (h << 16) for a in trap for h in range(4)}
table = (0, 1, 1, 1, 1, 0, 0, 0)


def tick(a, centre, exterior, width):
    row = [(a >> i) & 1 for i in range(width)]
    return sum(table[4*(row[i-1] if i else centre) + 2*row[i] + (row[i+1] if i+1 < width else exterior)] << i
               for i in range(width))


def move(a, x, y, width):
    return tick(tick(a, 0, x, width), 1, y, width)


edges = {}
for a in lift:
    row = []
    for x in (0, 1):
        for y in (0, 1):
            b = move(a, x, y, 18)
            assert b in lift
            row.append(b)
    assert len({b & 65535 for b in row}) == 1  # exterior cannot reach low16 in two ticks
    edges[a] = row


def bits(gaps):
    return [1] + [v for g in gaps for v in ([0]*(g-1)+[1])]


word = bits([3, 5, 3, 5, 3, 5, 3])
literal = {m[1]: list(map(int, re.findall(r"\d+", m[2])))
           for m in re.finditer(r"def (lift\d+(?:_\d+)?) : List Nat := \[(.*?)\]", src, re.S)}
actual = []
for i in range(27):
    name = f"lift{i}"
    if name in literal:
        a = literal[name]
        assert len(a) <= 192
    else:
        expression = re.search(r"def " + name + r" : List Nat := ([^\n]+)", src)[1]
        names = expression.split(" ++ ")
        assert names == [name+"_"+str(j) for j in range(len(names))]
        assert all(0 < len(literal[n]) <= 192 for n in names)
        a = sum((literal[n] for n in names), [])
    assert a == sorted(set(a)) and set(a) <= lift
    actual.append(set(a))
assert sum(map(len, actual)) == 4644
expression = src.split("def liftLayers : List (List Nat) := ",1)[1].split("\n\ntheorem liftStart",1)[0]
assert re.sub(r"\s+", "", expression) == "[" + ",".join(f"lift{i}" for i in range(27)) + ",[]]"
S = {x for x in lift if x & 1}
assert len(S) == 752
sizes = [len(S)]
for i in range(28):
    assert S == (actual[i] if i < 27 else set()), (i, "LAYER_MISMATCH")
    if i < 27:
        S = {v for x in S for v in edges[x] if (v & 1) == word[i+1]}
        sizes.append(len(S))

paths = []
for name, width, gaps in [("path16_3535353",16,[3,5,3,5,3,5,3]),
                          ("path18_353535",18,[3,5,3,5,3,5]),
                          ("path18_535353",18,[5,3,5,3,5,3])]:
    m = re.search(r"def " + name + r" : Nat × List \(Bool × Bool\) :=\s*\((\d+), \[(.*?)\]\)", src, re.S)
    a = int(m[1]); assert a < 1 << width and (a & 65535) in trap
    pairs = [(x == "true", y == "true") for x,y in re.findall(r"\((true|false), (true|false)\)", m[2])]
    heads = [a & 1]
    for x,y in pairs:
        a = move(a, x, y, width)
        assert (a & 65535) in trap
        heads.append(a & 1)
    assert heads == bits(gaps)
    paths.append({"name":name,"samples":len(heads),"final":a})

tag = "/-! ## Windows of eighteen columns -/"
body1 = src.split(tag,1)[1].rsplit("end Ruliology.CellularAutomata.Rule30GateTrapLift",1)[0]
body2 = portal.split(tag,1)[1].rsplit("end Rule30Submission",1)[0]
assert body1 == body2
assert not re.search(r"\b(sorry|admit|axiom|native_decide|unsafe)\b", body1)
result = {"lift_windows":len(lift),"closed_edges":sum(map(len,edges.values())),"exact_layer_sizes":sizes,
          "data_windows":sum(map(len,actual)),"paths":paths,"new_body_identical":True,
          "source_sha256":hashlib.sha256(src.encode()).hexdigest(),"oracle":"literal 8-entry truth table, two ticks"}
(output / "certificate-audit.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result),flush=True)
print("S16_RELEASE_CERTIFICATE_PASS",flush=True)
