#!/usr/bin/env python3
"""rule30_word_jen_census.py: WC, which periodic column words the one-sided Jen route excludes (L497, L498 generalized).
Local, chat L499; predictions pushed before the run.

RUN-ON:     cpu (Python 3); minutes
COMMAND:    python3 tests/probes/lexicon/rule30_word_jen_census.py [WIDTH=8] [PMIN=7] [PMAX=14]

For every primitive binary necklace w of period p (least rotation), with column 0 reading w periodically:
  - k-cell one-sided relaxation (free outside bit), the stable set of the macro (one period of w), then column +1 is
    determined if x1 takes one value at every tick from the stable set (rule30_white_end_jen.py's definitions,
    bitmask implementation as in rule30_one_hole_widths.py's `jen` mode);
  - a determined word is excluded as an eventual column of any finite nonzero seed by Theorem A (PROOFS.md entry 5),
    since columns 0 and +1 are then both eventually periodic with period p.
Record searched: 'Theorem A|Jen' with 'periodic word|column word|every word|primitive' and 'exclu' -> only RG's
strip-graph docstring (a two-sided test, which failed for periods <= 6 to radius 9); no census of this route exists.

PREDICTIONS (Local's, published before the run):
  WC-C1 (control): agreement with L497 and L498. The white-end words 0^q 1 (the necklace form of 1 0^q) are determined
        at p = 11 .. 14. The black-end words 0 1^(p-1) are undetermined at every p <= 14 (L497: from p = 15).
  WC-P1 (blind, confidence 0.6): at width 8 at least 5 percent of the primitive words of period 7 .. 14 are determined.
  WC-P2 (blind, confidence 0.5): every determined word contains a run (of 0s or of 1s) of length at least 6.
  WC-D1 (descriptive): counts by period, the determined words of period <= 10, and the shortest determined period.
"""
import sys


def necklaces(p):
    out = []
    for n in range(1 << p):
        s = format(n, '0%db' % p)
        rots = [s[i:] + s[:i] for i in range(p)]
        if s == min(rots) and len(set(rots)) == p:
            out.append(s)
    return out


def determined(k, word):
    n = 1 << k
    mask = n - 1

    def stp(x, w, u):
        return ((((x << 1) | w) & mask) ^ (x | ((x >> 1) | (u << (k - 1))))) & mask

    def img(S, w):
        return {stp(x, w, u) for x in S for u in (0, 1)}
    wall = [int(c) for c in word]
    S = set(range(n))
    for _ in range(300):
        T = S
        for w in wall:
            T = img(T, w)
        if T == S:
            break
        S = T
    ticks, T = [], S
    for w in wall:
        ticks.append({x & 1 for x in T})
        T = img(T, w)
    return all(len(v) == 1 for v in ticks)


def longest_run(w):
    s = w + w
    best = cur = 1
    for i in range(1, len(s)):
        cur = cur + 1 if s[i] == s[i - 1] else 1
        best = max(best, min(cur, len(w)))
    return best


def main():
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    pmin = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    pmax = int(sys.argv[3]) if len(sys.argv) > 3 else 14
    det, tot = {}, 0
    for p in range(pmin, pmax + 1):
        ws = necklaces(p)
        d = [w for w in ws if determined(k, w)]
        det[p] = d
        tot += len(ws)
        print('p = %2d: %d of %d primitive words determined%s' % (p, len(d), len(ws),
              (': ' + ' '.join(d)) if p <= 10 and d else ''), flush=True)
    c1 = all(('0' * (p - 1) + '1') in det.get(p, []) for p in range(11, 15) if pmin <= p <= pmax)
    c1 &= all(('0' + '1' * (p - 1)) not in det.get(p, []) for p in range(pmin, min(pmax, 14) + 1))
    print('WC-C1', 'PASS' if c1 else 'FAIL')
    nd = sum(len(v) for v in det.values())
    print('WC-P1', 'HELD' if nd >= 0.05 * tot else 'REFUTED', '(%d of %d, %.1f%%)' % (nd, tot, 100.0 * nd / tot))
    short = [w for v in det.values() for w in v if longest_run(w) < 6]
    print('WC-P2', 'HELD' if not short else 'REFUTED (e.g. %s)' % short[:6])
    first = min((p for p in det if det[p]), default=None)
    print('shortest determined period:', first)
    print('COMPLETE')


if __name__ == '__main__':
    main()
