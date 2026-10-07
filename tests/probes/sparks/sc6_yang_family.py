#!/usr/bin/env python3
"""sc6_yang_family.py: spark SC6 (SPARKS.md). A family that survived the redrawing.

RUN-ON:     cpu (Python 3, standard library), with two downloaded tables
COMMAND:    python3 -I tests/probes/sparks/sc6_yang_family.py DATA_DIR
            where DATA_DIR holds Unihan.zip (https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip) and ids.txt
            (https://raw.githubusercontent.com/cjkvi/cjkvi-ids/master/ids.txt); neither is kept in git.
COST:       seconds.

Take every character whose ideographic description (IDS) contains 昜 (U+661C) at any depth, and whose Unihan
kSimplifiedVariant differs from it; ask whether each simplified form contains 𠃓 (U+200D3), the shorthand of 昜.
Predictions (published in SPARKS.md before this ran): at least 75 per cent do, at most ten do not, and the exceptions
include 陽 -> 阳 and a group with 𠂉 over 力 (傷 -> 伤, 殤 -> 殇, 觴 -> 觞). Fail: under 60 per cent.
Control: 揚 must be found, simplify to 扬, and 扬 must be found to contain 𠃓.
"""
import re, sys, zipfile, pathlib
from functools import lru_cache

YANG, SHORT = "昜", "\U000200d3"
IDC = set(chr(c) for c in range(0x2FF0, 0x3000))


def load(data):
    ids = {}
    for line in (data / "ids.txt").read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or "\t" not in line:
            continue
        f = line.split("\t")
        comps = set()
        for s in f[2:]:
            s = re.sub(r"\[[^\]]*\]", "", s)
            s = re.sub(r"&[^;]+;", "", s)
            comps |= {ch for ch in s if ch not in IDC and ch != f[1]}
        ids[f[1]] = comps
    simp = {}
    with zipfile.ZipFile(data / "Unihan.zip") as z:
        for line in z.read("Unihan_Variants.txt").decode("utf-8").splitlines():
            if "\tkSimplifiedVariant\t" in line:
                cp, _, vals = line.split("\t")
                c = chr(int(cp[2:], 16))
                simp[c] = [chr(int(v[2:], 16)) for v in vals.split()]
    return ids, simp


def main():
    data = pathlib.Path(sys.argv[1])
    ids, simp = load(data)

    @lru_cache(maxsize=None)
    def contains(c, target, depth=8):
        if c == target:
            return True
        if depth == 0:
            return False
        return any(contains(x, target, depth - 1) for x in ids.get(c, ()))

    assert "扬" in simp.get("揚", []) and contains("扬", SHORT), "control failed"
    family = sorted(c for c in ids if c != YANG and contains(c, YANG))
    pairs, unchanged = [], []
    for c in family:
        s = [x for x in simp.get(c, []) if x != c]
        (pairs.append((c, s)) if s else unchanged.append(c))
    keep = [(c, s) for c, s in pairs if any(contains(x, SHORT) for x in s)]
    leave = [(c, s) for c, s in pairs if not any(contains(x, SHORT) for x in s)]
    print(f"characters containing 昜: {len(family)}; with a different simplified form: {len(pairs)};"
          f" no simplified form listed: {len(unchanged)}")
    print("kept 𠃓: " + " ".join(f"{c}→{''.join(s)}" for c, s in keep))
    print("left the family: " + " ".join(f"{c}→{''.join(s)}" for c, s in leave))
    share = len(keep) / len(pairs)
    print(f"share keeping 𠃓: {share:.0%} ({len(keep)} of {len(pairs)}); exceptions: {len(leave)}")
    named = {"陽": "阳", "傷": "伤", "殤": "殇", "觴": "觞"}
    found = {c: (c, s) in [(a, b) for a, b in leave] or any(a == c for a, _ in leave) for c in named}
    print("predicted exceptions present: " + ", ".join(f"{c}→{named[c]} {'yes' if found[c] else 'no'}" for c in named))
    # Added after the first run, and labelled as such in SPARKS.md: an exception whose simplified form has no
    # decomposition in the table is unknown, not shown to have left the family.
    known = [(c, s) for c, s in leave if any(ids.get(x) for x in s)]
    unknown = [(c, s) for c, s in leave if not any(ids.get(x) for x in s)]
    print(f"post hoc: exceptions whose simplified form has no decomposition in the table: {len(unknown)};"
          f" genuine: " + " ".join(f"{c}→{''.join(s)} ({' '.join(sorted(ids[s[0]]))})" for c, s in known))
    print(f"post hoc share keeping 𠃓 among forms the table describes: {len(keep)}/{len(keep) + len(known)}"
          f" = {len(keep) / (len(keep) + len(known)):.0%}")
    ok = share >= 0.75 and len(leave) <= 10 and all(found.values())
    print("PASS" if ok else ("FAIL" if share < 0.60 else "PARTIAL: see the lines above"))


if __name__ == "__main__":
    main()
