#!/usr/bin/env python3
"""sc11_keloid.py: spark SC11 (SPARKS.md). Cheloid before keloid?

RUN-ON:     cpu with network (Python 3, standard library)
COMMAND:    python3 tests/probes/sparks/sc11_keloid.py
COST:       two small requests to the Google Books Ngram viewer's JSON endpoint; the data is not stored.

Corpora en-2019 and fr-2019, 1800 to 2019, case ignored, no smoothing requested. Reports the first year each
spelling appears, the English crossover (as in SC5: the first year from which a centred five-year average of
"keloid" stays above "cheloid" in every later year) and the French spellings decade by decade. Predictions
(published in SPARKS.md before this ran): "cheloid" at least ten years before "keloid" in English, an English
crossover between 1880 and 1920, and "chéloïde" ahead of "kéloïde" in every decade 1820 to 1950. Fail: "keloid" in
English print no later than "cheloid".
Control: each series has 220 yearly values, and the case-insensitive total is at least the lower-case series.
"""
import json, urllib.parse, urllib.request

URL = "https://books.google.com/ngrams/json?"


def series(words, corpus):
    q = urllib.parse.urlencode({"content": ",".join(words), "year_start": 1800, "year_end": 2019, "corpus": corpus,
                                "smoothing": 0, "case_insensitive": "true"})
    with urllib.request.urlopen(URL + q, timeout=60) as r:
        data = json.load(r)
    out = {}
    for w in words:
        allcase = [d for d in data if d["ngram"] == f"{w} (All)"]
        lower = [d for d in data if d["ngram"] == w]
        ts = allcase[0]["timeseries"] if allcase else (lower[0]["timeseries"] if lower else [0.0] * 220)
        assert len(ts) == 220
        if allcase and lower:
            assert sum(ts) >= sum(lower[0]["timeseries"]) * (1 - 1e-9)
        out[w] = ts
    return out


def first(ts):
    return next((1800 + i for i, x in enumerate(ts) if x > 0), None)


def avg5(xs):
    return [sum(xs[max(0, i - 2):i + 3]) / len(xs[max(0, i - 2):i + 3]) for i in range(len(xs))]


def crossover(a, b):
    a, b = avg5(a), avg5(b)
    return next((1800 + i for i in range(len(a)) if all(a[j] > b[j] for j in range(i, len(a)))), None)


def decade(ts, d):
    return sum(ts[d - 1800:d - 1790]) / 10


def main():
    en = series(["cheloid", "keloid"], "en-2019")
    fr = series(["chéloïde", "kéloïde"], "fr-2019")
    fc, fk = first(en["cheloid"]), first(en["keloid"])
    cross = crossover(en["keloid"], en["cheloid"])
    print(f"English: first 'cheloid' {fc}, first 'keloid' {fk}; crossover {cross}")
    print("  first ten nonzero years, cheloid:", [1800 + i for i, x in enumerate(en["cheloid"]) if x > 0][:10])
    print("  first ten nonzero years, keloid: ", [1800 + i for i, x in enumerate(en["keloid"]) if x > 0][:10])
    print(f"French: first 'chéloïde' {first(fr['chéloïde'])}, first 'kéloïde' {first(fr['kéloïde'])}")
    fr_ok = True
    print("decade   en cheloid  en keloid   fr chéloïde  fr kéloïde   (per million words)")
    for d in range(1800, 2020, 10):
        row = [decade(en["cheloid"], d), decade(en["keloid"], d), decade(fr["chéloïde"], d), decade(fr["kéloïde"], d)]
        print(f"{d}s  " + "  ".join(f"{x * 1e6:10.4f}" for x in row))
        if 1820 <= d <= 1950 and not row[2] > row[3]:
            fr_ok = False
    en_first = fc is not None and (fk is None or fk - fc >= 10)
    window = cross is not None and 1880 <= cross <= 1920
    print(f"cheloid first by ten years or more: {en_first}; crossover in 1880 to 1920: {window}; "
          f"French chéloïde ahead every decade 1820 to 1950: {fr_ok}")
    refuted = fk is not None and (fc is None or fk <= fc)
    print("FAIL" if refuted else ("PASS" if en_first and window and fr_ok else "PARTIAL"))


if __name__ == "__main__":
    main()
