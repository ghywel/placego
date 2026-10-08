#!/usr/bin/env python3
"""GC549 fixed continuation audit, predictions before run, 2026-10-08.
Instrument repair: initial C1 failed on 11100 because the paired boundary used
a XOR b instead of a OR b at the first tick. Corrected before rerun; retained here.
Only target 1000010001001 from the canonical right prefix 11100 is tested.
C1: paired two-step map agrees with literal decimal Rule 30 on every visited prefix.
P1 blind: every surviving target source has sites 6..8 equal to 011.
CF: source 11100 has initial visible symbol 0; must fail.
Unexpected: report the earliest target prefix forcing that spatial tail, if any.
Cap: 100000 surviving sources at any stage; cap exhaustion is not a pass.
OUTCOME: first boundary control failed and was repaired as retained above.
Corrected C1 passes on all visited prefixes; CF refuted. The final target
has zero canonical sources, so P1 supplies no nonvacuous 011 mechanism.
Unexpected: sites 6..8 are instead forced to 001 at target length 10;
1280 sources survive there, 12000 at length 12, and zero at length 13.
The cap was not hit. An initial terminal assertion reported the empty
source result as an exception; reporting repaired without changing enumeration.
REFUTED-BY: C1 mismatch, a P1 survivor without 011, or no surviving source.
This is one conditional word audit, not a language census or RV3 death-time run.
"""
from itertools import product
from rule30_gpt_entry_image import bulk

TARGET = '1000010001001'

def literal_trace(source):
    row, trace, t = list(source), [], 0
    while row:
        if t % 2 == 0:
            trace.append(str(row[0]))
        wall = t % 2
        left = [wall] + row[:-1]
        row = [(30 >> (4*left[j]+2*row[j]+row[j+1])) & 1
               for j in range(len(row)-1)]
        t += 1
    return ''.join(trace)

def paired_trace(source):
    row, trace = list(source), []
    while row:
        trace.append(str(row[0]))
        if len(row) < 3:
            break
        # wall zero at even times, one at odd times.
        a, b, c = row[:3]
        beta, eta = a | b, a ^ (b | c)
        first = 1 ^ (beta | eta)
        extended = [0] + row
        row = [first] + [bulk(tuple(extended[j-1:j+4]))
                         for j in range(1, len(row)-2)]
    return ''.join(trace)

def main():
    assert literal_trace((1,1,1,0,0))[0] != '0'
    sources = [(1,1,1,0,0)]
    for n in range(3, len(TARGET)+1):
        if n > 3:
            sources = [s + e for s in sources for e in product((0,1), repeat=2)]
        for s in sources:
            assert paired_trace(s) == literal_trace(s), s
        sources = [s for s in sources if literal_trace(s) == TARGET[:n]]
        if len(sources) > 100000:
            print('CAPPED', n); return
        tails = sorted({''.join(map(str,s[5:8])) for s in sources if len(s)>=8})
        print('length',n,'survivors',len(sources),'sites6..8',tails)
    if not sources:
        print('P1 REFUTED as a nonvacuous mechanism: target has no canonical source')
        print('C1 PASS; CF REFUTED')
        return
    good = all(s[5:8] == (0,1,1) for s in sources)
    print('P1', 'HELD' if good else 'REFUTED')
    print('first witness', ''.join(map(str,sources[0])))
    print('C1 PASS; CF REFUTED')

if __name__ == '__main__':
    main()
