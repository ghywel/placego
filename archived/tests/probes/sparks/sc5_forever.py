#!/usr/bin/env python3
"""sc5_forever.py: spark SC5 (SPARKS.md). For ever, then forever.

RUN-ON:     cpu with network (Python 3, standard library)
COMMAND:    python3 tests/probes/sparks/sc5_forever.py
COST:       two small requests to the Google Books Ngram viewer's JSON endpoint; the data is not stored.

Crossover: with a centred five-year average of each form's yearly frequency (corpora en-US-2019 and en-GB-2019,
1800 to 2019, no smoothing requested), the first year from which "forever" stays above "for ever" in every later
year. Predictions (published in SPARKS.md before this ran): American crossover 1880 to 1940, British 1960 to 2000,
gap of at least 30 years. Fail: gap under ten years, or Britain first.
Control: the two series are checked to have 220 yearly values each and non-zero totals.
"""
import json, urllib.parse, urllib.request

URL = "https://books.google.com/ngrams/json?"


def series(corpus):
    q = urllib.parse.urlencode({"content": "forever,for ever", "year_start": 1800, "year_end": 2019,
                                "corpus": corpus, "smoothing": 0})
    with urllib.request.urlopen(URL + q, timeout=60) as r:
        data = json.load(r)
    out = {d["ngram"]: d["timeseries"] for d in data}
    return out["forever"], out["for ever"]


def avg5(xs):
    return [sum(xs[max(0, i - 2):i + 3]) / len(xs[max(0, i - 2):i + 3]) for i in range(len(xs))]


def crossover(a, b):
    a, b = avg5(a), avg5(b)
    for i in range(len(a)):
        if all(a[j] > b[j] for j in range(i, len(a))):
            return 1800 + i, a, b
    return None, a, b


def main():
    res = {}
    for name, corpus in (("American", "en-US-2019"), ("British", "en-GB-2019")):
        f, fe = series(corpus)
        assert len(f) == len(fe) == 220 and sum(f) > 0 and sum(fe) > 0
        year, a, b = crossover(f, fe)
        res[name] = year
        print(f"{name}: crossover {year}")
        for y in (1800, 1850, 1900, 1925, 1950, 1975, 2000, 2019):
            i = y - 1800
            print(f"  {y}: forever {a[i] * 1e6:6.2f} per million, for ever {b[i] * 1e6:6.2f}, ratio {a[i] / b[i]:6.2f}")
    us, gb = res["American"], res["British"]
    ok = us is not None and gb is not None and 1880 <= us <= 1940 and 1960 <= gb <= 2000 and gb - us >= 30
    refuted = us is None or gb is None or gb - us < 10
    print(f"gap {None if us is None or gb is None else gb - us} years")
    print("PASS" if ok else ("FAIL" if refuted else "PARTIAL: direction right, a predicted window missed"))


if __name__ == "__main__":
    main()
