#!/usr/bin/env python3
"""sc19_horse_colours.py: spark SC19 (SPARKS.md). Where attention went: the horse.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 -I tests/probes/sparks/sc19_horse_colours.py DATA_DIR
COST:       seconds. DATA_DIR holds Unihan.zip (Unicode's Unihan database), downloaded and kept outside git.

Characters are counted by the radical in the first value of their kRSUnicode field, simplified radical forms
included: horse 187, cow 93, sheep 123, pig 152, and dog 94 reported without a prediction. A character names a colour
or marking when its kDefinition contains a word from the list below (fixed before the run). Predictions (published
in SPARKS.md before this ran): horse at least 1.5 times each of cow, sheep and pig; at least 15 per cent of horse
characters with a definition name a colour or marking, against at most 6 per cent for each of the other three.
Fail: a horse share no larger than the largest of the other three.
Control check: 騵 must be under radical 187 and its definition must name a colour.
"""
import io, re, sys, zipfile

COLOUR = re.compile(r"\b(black|white|red|yellow|grey|gray|blue|green|brown|piebald|dappled|spotted|speckled|striped|"
                    r"roan|sorrel|chestnut|bay|dun|mane|colour|color|colored|coloured|pale|dark|tawny|sandy)\b", re.I)
RAD = {187: "horse 馬", 93: "cow 牛", 123: "sheep 羊", 152: "pig 豕", 94: "dog 犬"}


def main():
    d = sys.argv[1]
    rad, dfn = {}, {}
    with zipfile.ZipFile(f"{d}/Unihan.zip") as z:
        for name, key, store in (("Unihan_IRGSources.txt", "\tkRSUnicode\t", rad),
                                 ("Unihan_Readings.txt", "\tkDefinition\t", dfn)):
            for line in io.TextIOWrapper(z.open(name), encoding="utf-8"):
                if key in line:
                    cp, _, val = line.rstrip("\n").split("\t", 2)
                    store[chr(int(cp[2:], 16))] = val
    num = {c: int(v.split()[0].split(".")[0].rstrip("'")) for c, v in rad.items()}
    assert num["騵"] == 187 and COLOUR.search(dfn["騵"]), dfn.get("騵")
    res = {}
    for r, name in RAD.items():
        chars = [c for c, n in num.items() if n == r]
        with_def = [c for c in chars if c in dfn]
        col = [c for c in with_def if COLOUR.search(dfn[c])]
        res[r] = (len(chars), len(with_def), len(col))
        print(f"{name}: {len(chars)} characters, {len(with_def)} with a definition, {len(col)} name a colour or marking "
              f"({100 * len(col) / max(1, len(with_def)):.1f}%); e.g. {' '.join(col[:8])}")
    h = res[187]
    share = lambda r: res[r][2] / max(1, res[r][1])
    others = (93, 123, 152)
    ratio = min(h[0] / res[r][0] for r in others)
    print(f"horse count over the largest of cow, sheep, pig: {h[0] / max(res[r][0] for r in others):.2f}")
    ok = ratio >= 1.5 and share(187) >= 0.15 and all(share(r) <= 0.06 for r in others)
    bad = share(187) <= max(share(r) for r in others)
    print("PASS" if ok else ("FAIL" if bad else "PARTIAL"))


if __name__ == "__main__":
    main()
