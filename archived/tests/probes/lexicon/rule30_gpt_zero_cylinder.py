#!/usr/bin/env python3
"""GC503 exact zero-latch cylinder controls.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_zero_cylinder.py
RUN-ON: GPT standard Python, fixed 128 controls, no count scan.
PREDICTIONS registered in CLOUD-LOCAL before temporary first execution:
 ZC0: five initial right bits decide first visible zero-run duration;
      both implementations agree for all 32 patches and four tails each.
 ZC1: four zeros iff first five sites are (0,1,1,r,z), r OR z=1.
 CF: conditional lengths 1..4 are uniform, must fail.
 UNEXPECTED: event uses five bits, fewer than the generic seven for four
      visible outputs; arbitrary-tail independence is proved in GC503.
 REFUTED-BY: ZC0 or ZC1 failure invalidates the formula.
 OUTCOME (2026-10-08): all 128 controls PASS in both implementations;
 counts for durations 0..4 are 16,4,5,4,3; CF REFUTED.
"""
# GC503 predictions registered in CLOUD-LOCAL before execution.
# All 32 five-bit patches, four exterior tails each; compare exact
# hand zero-run formula with both existing independent implementations.
from collections import Counter
from rule30_gpt_boundary_collision import packed, literal

def predicted(seed):
    a,b,q,r,z=[seed>>i&1 for i in range(5)]
    if a: return 0
    if not (b or q): return 1
    if not b: return 3
    if not q or not (r or z): return 2
    return 4

def run(word):
    return next((i for i,c in enumerate(word) if c=='1'),len(word))

hist=Counter(); checked=0
for patch in range(32):
    expect=predicted(patch);hist[expect]+=1
    for tail in [0,15,5,10]:
        seed=patch|(tail<<5)
        assert run(packed(seed,5))==expect
        assert run(literal(seed,5))==expect
        checked+=1
assert hist=={0:16,1:4,2:5,3:4,4:3}
assert [hist[i] for i in range(1,5)] != [4,4,4,4]
print('PASS 128 cylinder-tail controls in both implementations')
print('exact five-bit counts:',sorted(hist.items()))
print('uniform conditional run-length CF REFUTED; no horizon enlargement')
