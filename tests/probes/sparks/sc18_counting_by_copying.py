#!/usr/bin/env python3
"""sc18_counting_by_copying.py: spark SC18 (SPARKS.md). Counting by copying: 木, 林, 森.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 -I tests/probes/sparks/sc18_counting_by_copying.py DATA_DIR
COST:       seconds. DATA_DIR holds Unihan.zip (Unicode's Unihan database) and ids.txt (the CJKVI decomposition
            table, based on CHISE), both downloaded and kept outside git.

A character counts as a copy-character when its first listed decomposition is two copies of one character side by
side or stacked, three in a row, a column, the 品 shape or its upside-down form, or four in a square. Its Unihan
definition is compared with the component's (a component that is itself a copy-character, as 林 is
inside 森, is opened up, so 森 counts as three 木; the first version missed this and its 森 control caught it): related when they share a content word, or when the composite's
definition has a word of quantity or intensity from the list below (fixed before the run). Control: each composite
paired with a random other component that has a definition. Predictions (published in SPARKS.md before this ran): at
least 300 copy-characters; at least half of those with both definitions related; at most 15 per cent of random
pairings sharing a content word. Fail: under 30 per cent related, or no clear gap from the control.
Control check: 林, 森, 炎 and 品 must be found with the right component.
"""
import io, random, re, sys, zipfile

INTENSE = set("many much numerous multitude crowd crowded abundant abundance luxuriant dense flourishing great "
              "intense blazing brilliant plenty plentiful flock herd heap piled rows".split())
STOP = set("a an the of to in and or for with as on by at from be is are it its used name surname variant same also "
           "kind sort type character radical one two three four ancient old form forms used chinese".split())


def defs(zpath):
    out = {}
    with zipfile.ZipFile(zpath) as z:
        for line in io.TextIOWrapper(z.open("Unihan_Readings.txt"), encoding="utf-8"):
            if "\tkDefinition\t" in line:
                cp, _, val = line.rstrip("\n").split("\t", 2)
                out[chr(int(cp[2:], 16))] = val
    return out


def words(d):
    out = set()
    for w in re.findall(r"[a-z]+", d.lower()):
        if w in STOP or len(w) < 3:
            continue
        out.add(w[:-1] if len(w) > 4 and w.endswith("s") else w)
    return out


OPS = {"⿰": 2, "⿱": 2, "⿲": 3, "⿳": 3}


def parse(ids):
    """A decomposition string as a tree: a character, or (operator, [children]); None for other operators."""
    ids = re.sub(r"\[[^\]]*\]", "", ids)
    pos = 0

    def node():
        nonlocal pos
        if pos >= len(ids):
            raise ValueError
        c = ids[pos]; pos += 1
        if c in OPS:
            return (c, [node() for _ in range(OPS[c])])
        if "\u2ff0" <= c <= "\u2fff" or c == "&":
            raise ValueError
        return c
    try:
        t = node()
        return t if pos == len(ids) else None
    except ValueError:
        return None


def leaves(t, first_ids, depth=0):
    """The components of a tree, opening any component that is itself a copy-character (one or two levels)."""
    if isinstance(t, str):
        sub = parse(first_ids.get(t, "")) if depth < 2 else None
        if sub is not None and not isinstance(sub, str):
            inner = leaves(sub, first_ids, depth + 1)
            if inner and len(set(inner)) == 1:
                return inner
        return [t]
    return [x for ch in t[1] for x in leaves(ch, first_ids, depth)]


def copy_base(ids, first_ids):
    t = parse(ids)
    if t is None or isinstance(t, str):
        return None, None
    lv = leaves(t, first_ids)
    if len(set(lv)) == 1 and 2 <= len(lv) <= 4:
        return lv[0], len(lv)
    return None, None


def main():
    d = sys.argv[1]
    D = defs(f"{d}/Unihan.zip")
    first_ids = {}
    for line in open(f"{d}/ids.txt", encoding="utf-8"):
        if line.startswith("#") or "\t" not in line:
            continue
        f = line.rstrip("\n").split("\t")
        if len(f) >= 3:
            first_ids[f[1]] = f[2]
    found = {}
    for ch, ids in first_ids.items():
        base, k = copy_base(ids, first_ids)
        if base and base != ch:
            found[ch] = (base, k)
    for ch, b in (("林", "木"), ("森", "木"), ("炎", "火"), ("品", "口")):
        assert found.get(ch, (None,))[0] == b, (ch, found.get(ch))
    both = {c: v for c, v in found.items() if c in D and v[0] in D}
    rel, shared, inten = [], [], []
    for c, (b, k) in both.items():
        s = bool(words(D[c]) & words(D[b]))
        i = bool(words(D[c]) & INTENSE)
        shared.append(s); inten.append(i); rel.append(s or i)
    bases = sorted({b for b, k in both.values()})
    rng = random.Random(18)
    ctrl = []
    for _ in range(20):
        for c, (b, k) in both.items():
            other = rng.choice(bases)
            while other == b:
                other = rng.choice(bases)
            ctrl.append(bool(words(D[c]) & words(D[other])))
    by_k = {k: sum(1 for v in found.values() if v[1] == k) for k in (2, 3, 4)}
    n = len(both)
    print(f"copy-characters found: {len(found)} (two copies {by_k[2]}, three {by_k[3]}, four {by_k[4]}); "
          f"with both definitions: {n}")
    print(f"related: {sum(rel)} of {n} ({100 * sum(rel) / n:.0f}%); by a shared content word {100 * sum(shared) / n:.0f}%, "
          f"by a word of quantity or intensity {100 * sum(inten) / n:.0f}%")
    print(f"control, random component: shared content word {100 * sum(ctrl) / len(ctrl):.1f}%")
    ex = [c for c in "林森炎焱品晶淼犇鑫驫吅叒双雔" if c in both]
    for c in ex:
        b = both[c][0]
        print(f"  {c} = {both[c][1]} x {b}: {D[c][:60]!r}  <-  {b}: {D[b][:40]!r}")
    miss = [c for c, (b, k) in both.items() if not rel[list(both).index(c)]][:12]
    print("unrelated by the rule, first twelve:", " ".join(f"{c}({both[c][0]})" for c in miss))
    ok = len(found) >= 300 and sum(rel) / n >= 0.5 and sum(ctrl) / len(ctrl) <= 0.15
    bad = sum(rel) / n < 0.3 or sum(shared) / n <= 2 * sum(ctrl) / len(ctrl)
    print("PASS" if ok else ("FAIL" if bad else "PARTIAL"))


if __name__ == "__main__":
    main()
