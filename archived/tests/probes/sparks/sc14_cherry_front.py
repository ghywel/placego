#!/usr/bin/env python3
"""sc14_cherry_front.py: spark SC14 (SPARKS.md). The cherry front.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 -I tests/probes/sparks/sc14_cherry_front.py DATA_DIR
COST:       instant. DATA_DIR holds two downloaded files, kept outside git: past.html (the Japan Meteorological
            Agency's page of past first-bloom dates, sakura003_07.html, which carries the 1991-2020 normals) and the
            agency's station master, ame_master_*.csv (from ame_master.zip, Shift-JIS), for positions and heights.

Stations kept: those with a normal first-bloom date and no substitute species, that is, those observing
Somei-Yoshino (Okinawa and Amami observe the Taiwan cherry, most of Hokkaido the Sargent cherry). The normal date
is fitted against latitude by least squares. Predictions (published in SPARKS.md before this ran): slope 3 to 5
days per degree, R^2 at least 0.75, spread about the line at most 5 days, the southernmost stations later than the
line. Fail: R^2 below 0.5, spread above 7 days, or the far south early.
Control: Tokyo's normal (24 March, day 83), Sapporo's latitude (43 degrees 3.6 minutes) and Takamatsu's (in
Shikoku, not Hakodate airport's station of the same name) are checked by hand.
Post hoc, labelled so in SPARKS.md: the residuals against station height.
"""
import csv, glob, html, math, re, sys

CUM = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]


def blooms(path):
    t = open(path, "rb").read().decode("utf-8", "replace")
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    out = {}
    for line in t.split("\n"):
        f = line.split()
        if len(f) < 4 or f[1] != "*":
            continue
        rest = f[2:]
        sub = []
        while rest and not (rest[-1].isdigit() or rest[-1] == "-"):
            sub.insert(0, rest.pop())
        if not sub and len(rest) >= 2 and rest[-1].isdigit() and rest[-2].isdigit():
            out[f[0]] = CUM[int(rest[-2]) - 1] + int(rest[-1])
    return out


def stations(d):
    path = sorted(glob.glob(f"{d}/ame_master_*.csv"))[-1]
    out, office = {}, set()
    for r in csv.reader(open(path, encoding="cp932")):
        if len(r) > 11 and r[2] == "官":
            # One name can belong to two stations (高松 is also Hakodate airport's); a weather office comes first.
            is_office = "気象台" in r[6]
            if r[3] not in out or (is_office and r[3] not in office):
                out[r[3]] = (int(r[7]) + float(r[8]) / 60, int(r[9]) + float(r[10]) / 60, float(r[11]))
                if is_office:
                    office.add(r[3])
    return out


def fit(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    a = my - b * mx
    res = [y - (a + b * x) for x, y in zip(xs, ys)]
    r2 = 1 - sum(e * e for e in res) / sum((y - my) ** 2 for y in ys)
    return a, b, r2, math.sqrt(sum(e * e for e in res) / (n - 2)), res


def main():
    d = sys.argv[1]
    bl, st = blooms(f"{d}/past.html"), stations(d)
    assert bl["東京"] == 83 and abs(st["札幌"][0] - (43 + 3.6 / 60)) < 1e-9, (bl.get("東京"), st.get("札幌"))
    assert 34 < st["高松"][0] < 35, st["高松"]
    missing = [k for k in bl if k not in st]
    names = sorted((k for k in bl if k in st), key=lambda k: st[k][0])
    lat = [st[k][0] for k in names]
    doy = [bl[k] for k in names]
    a, b, r2, sd, res = fit(lat, doy)
    print(f"{len(names)} Somei-Yoshino stations with normals ({len(missing)} without a position: {missing})")
    print(f"fit: day = {a:.1f} + {b:.2f} x latitude; R^2 {r2:.3f}; spread about the line {sd:.2f} days; "
          f"front speed {111.2 / b:.1f} km a day")
    order = sorted(range(len(names)), key=lambda i: res[i])
    print("earliest against the line:", ", ".join(f"{names[i]} {res[i]:+.1f}" for i in order[:6]))
    print("latest against the line:  ", ", ".join(f"{names[i]} {res[i]:+.1f}" for i in order[-6:][::-1]))
    south = [i for i in range(len(names)) if lat[i] < 33]
    print("south of 33 degrees N:", ", ".join(f"{names[i]} ({lat[i]:.2f} N, day {doy[i]}, {res[i]:+.1f})"
                                                 for i in south))
    north = [i for i in range(len(names)) if lat[i] > 41]
    print("north of 41 degrees N:", ", ".join(f"{names[i]} ({lat[i]:.2f} N, day {doy[i]}, {res[i]:+.1f})"
                                                 for i in north))
    s_mean = sum(res[i] for i in south) / len(south)
    ok = 3 <= b <= 5 and r2 >= 0.75 and sd <= 5 and s_mean > 0
    bad = r2 < 0.5 or sd > 7 or s_mean < 0
    print(f"mean residual south of 33 N: {s_mean:+.1f} days")
    print("PASS" if ok else ("FAIL" if bad else "PARTIAL"))
    hs = [st[k][2] for k in names]
    _, bh, r2h, _, _ = fit(hs, res)
    print(f"post hoc: residual against station height: {bh * 100:+.2f} days per 100 m (R^2 {r2h:.3f}); heights "
          f"{min(hs):.0f} to {max(hs):.0f} m")
    sub = [i for i in range(len(names)) if 33 <= lat[i] <= 41]
    _, b2, r22, sd2, _ = fit([lat[i] for i in sub], [doy[i] for i in sub])
    print(f"post hoc: 33 to 41 degrees N only ({len(sub)} stations): {b2:.2f} days per degree, R^2 {r22:.3f}, "
          f"spread {sd2:.2f} days")


if __name__ == "__main__":
    main()
