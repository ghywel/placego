#!/usr/bin/env python3
"""sc12_element_radicals.py: spark SC12 (SPARKS.md). What the bottle holds, written in the name.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 -I tests/probes/sparks/sc12_element_radicals.py DATA_DIR
COST:       seconds. DATA_DIR holds three downloaded tables, kept outside git: pubchem.csv (PubChem's periodic
            table, rest/pug/periodictable/CSV), wikidata.csv (atomic number and the zh-hans, zh-cn and zh labels of
            every chemical element, from the Wikidata query service) and Unihan.zip (Unicode's Unihan database).

For elements 1 to 118: the simplified name (zh-hans, else zh-cn, else zh), its radical from Unihan's kRSUnicode,
and PubChem's standard state and group block. Radicals: 84 气 (gas), 85 水 or 氵 (liquid), 112 石 and 167 金 or 钅
(solid). Classes: metal (alkali, alkaline earth, transition, post-transition, lanthanide, actinide), non-metal
(nonmetal, halogen, noble gas), metalloid. Predictions (published in SPARKS.md before this ran): no exception to the
state rule among measured states; every metal 钅 or 金 except mercury; every solid non-metal 石; metalloids split, B,
Si, As, Te with 石 and Ge, Sb with 钅; superheavies follow their columns, so oganesson has 气.
Control: hydrogen, bromine, carbon and iron are checked by hand against the expected radicals.
"""
import csv, io, sys, zipfile

RAD = {84: "gas", 85: "liquid", 112: "stone", 167: "metal"}
METAL = {"Alkali metal", "Alkaline earth metal", "Transition metal", "Post-transition metal", "Lanthanide", "Actinide"}
NONMETAL = {"Nonmetal", "Halogen", "Noble gas"}


def radicals(zpath):
    out = {}
    with zipfile.ZipFile(zpath) as z:
        for name in z.namelist():
            for line in io.TextIOWrapper(z.open(name), encoding="utf-8"):
                if "\tkRSUnicode\t" in line:
                    cp, _, val = line.rstrip("\n").split("\t")
                    first = val.split()[0]
                    out[chr(int(cp[2:], 16))] = int(first.split(".")[0].rstrip("'"))
    return out


def main():
    d = sys.argv[1]
    rs = radicals(f"{d}/Unihan.zip")
    names = {}
    for row in csv.DictReader(open(f"{d}/wikidata.csv", encoding="utf-8")):
        n = int(float(row["n"]))
        if 1 <= n <= 118 and n not in names:
            names[n] = row["hans"] or row["cn"] or row["zh"]
    pc = {int(r["AtomicNumber"]): r for r in csv.DictReader(open(f"{d}/pubchem.csv", encoding="utf-8"))}
    assert len(pc) == 118 and len(names) == 118, (len(pc), len(names))
    for n, want in ((1, 84), (35, 85), (6, 112), (26, 167)):
        assert rs[names[n]] == want, (n, names[n], rs.get(names[n]))
    state_x, class_x, metalloid, superheavy, odd = [], [], [], [], []
    for n in range(1, 119):
        r, ch = pc[n], names[n]
        if len(ch) != 1 or ch not in rs:
            odd.append((n, r["Symbol"], ch))
            continue
        kind = RAD.get(rs[ch], f"radical {rs[ch]}")
        st, gb = r["StandardState"], r["GroupBlock"]
        measured = not st.startswith("Expected")
        st_kind = {"gas": "gas", "liquid": "liquid", "solid": "solid"}[st.split()[-1].lower()]
        rad_state = {"gas": "gas", "liquid": "liquid", "stone": "solid", "metal": "solid"}.get(kind, kind)
        tag = (n, r["Symbol"], ch, kind, st, gb)
        if not measured:
            superheavy.append(tag)
        if rad_state != st_kind:
            state_x.append(tag)
        if gb == "Metalloid":
            metalloid.append(tag)
        elif gb in METAL and kind != "metal":
            class_x.append(tag)
        elif gb in NONMETAL and st_kind == "solid" and kind != "stone":
            class_x.append(tag)
    show = lambda xs: "; ".join(f"{s} {c} ({k}, {st.lower()}, {gb.lower()})" for _, s, c, k, st, gb in xs) or "none"
    print(f"names not a single Unihan character: {odd or 'none'}")
    print(f"state exceptions, measured: {show([x for x in state_x if not x[4].startswith('Expected')])}")
    print(f"state exceptions, predicted states only: {show([x for x in state_x if x[4].startswith('Expected')])}")
    print(f"class exceptions: {show(class_x)}")
    print(f"metalloids: {show(metalloid)}")
    print(f"superheavies with predicted states: {show(superheavy)}")
    counts = {}
    for n in range(1, 119):
        ch = names[n]
        counts[RAD.get(rs.get(ch), "other")] = counts.get(RAD.get(rs.get(ch), "other"), 0) + 1
    print(f"radical counts: {counts}")
    m_state = [x for x in state_x if not x[4].startswith("Expected")]
    m_class = [x for x in class_x if x[1] != "Hg"]
    mstone = sorted(x[1] for x in metalloid if x[3] == "stone")
    print("PASS" if not m_state and not m_class and mstone == ["As", "B", "Si", "Te"] else
          ("FAIL" if m_state or len(m_class) > 0 else "PARTIAL: metalloid split differs"))


if __name__ == "__main__":
    main()
