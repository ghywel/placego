"""Find one short, explicit physical counterexample per candidate word outside the 24.
Then replay the certificate by inverse row scans, independent of how a witness was found.
"""
from pathlib import Path
import hashlib
import json
import os

from rain_window_histories import invert_window, B11, PATTERNS, encode

positive = B11 | {encode(pattern) for pattern in PATTERNS}


def check_witness(word, w):
    r, L = w["ticks"], w["L"]
    assert L >= 2 and w["source_low"] & 1 and w["source_low"] < (1 << L)
    top = L + 9
    high = top + 3*r + 4
    row = [(w["source_low"] >> j) & 1 for j in range(L)]
    row += [(word >> j) & 1 for j in range(11)]
    while len(row) <= high:
        row.append(1-row[-1])
    for _ in range(r):
        pred = []
        for j, cell in enumerate(row):
            prev = pred[j-1] if j >= 1 else 0
            older = pred[j-2] if j >= 2 else 0
            pred.append(cell ^ (prev | older))
        row = pred
    assert all(row[j]!=row[j+1] for j in range(top+3*r+1,high))
    assert row[top+3*r] != row[top+3*r+1]


def main():
    assert len(positive)==24
    words = {i | (((i>>9)&1)<<10) for i in range(1024)}
    certificate = {}
    missing = []
    for word in sorted(words-positive):
        for r in (1,2,3,4,5):
            for carry in range(1 << (2*r)):
                speed, _, witness = invert_window(word, carry, r)
                if not speed:
                    w = dict(ticks=r, L=witness["L"], source_low=witness["source_low"])
                    check_witness(word,w)
                    certificate[word]=w
                    break
            if word in certificate:
                break
        else:
            missing.append(word)
    assert set(certificate).isdisjoint(positive) and set(certificate) | set(missing) | positive == words
    data=(json.dumps(dict(witnesses=certificate,unresolved=missing),sort_keys=True,indent=2)+"\n").encode()
    (Path(os.environ['CAPPED_OUT'])/'exclusions.json').write_bytes(data)
    print('covered',len(certificate),'unresolved',missing)
    print('witness ticks',{r:sum(w['ticks']==r for w in certificate.values()) for r in range(1,6)})
    print('certificate sha256',hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
