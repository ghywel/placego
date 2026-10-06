#!/usr/bin/env python3
"""rule30_otherrules.py: is the universal left side Rule 30's, or its class's? The band instrument of sections 8.30,
8.31 and 8.59 (the strip of left diagonals as a closed finite system, D_k(t+1) = f(D_(k-2), D_(k-1), D_k)) works for
every elementary rule whose left edge moves at light speed from a single black cell, which are the 128 rules with
f(0,0,1) = 1. For each, from the single cell: the strip of K diagonals, a certificate of periodicity if the period is
at most 1024, the eventually white diagonals, the per-diagonal periods and the doublings. Row 14 of CONSTELLATION.md
("what makes 30 special among 256"). (Local, 2026-10-06; RULE30-PRIZE.md section 8.64.)

RUN-ON:     cpu, one core (pure Python 3, big integers)
COMMAND:    python3 tests/probes/lexicon/rule30_otherrules.py [K=8192] [STEPS=40000]
COST:       about a minute.

SEEN BEFORE these predictions: Rule 30's band (2, 7, 28, 399 white; period 16 below 87,866); nothing of any other rule's
band. From the rule tables: 86 is Rule 30's mirror, so its left side is Rule 30's nested right side; 90 and 150 are
linear; 2 moves the single cell left one step at a time; 45, 73 and 89 do not qualify (their single cell is fixed).

PREDICTIONS, written 2026-10-06 before this script's first run.
  OR0 (control, must hold): Rule 30 gives the recorded band: eventually white diagonals 2, 7, 28, 399 below K, period
      16 at K; Rule 2 gives a strip of period 1 with every diagonal but 0 white (the cell runs left for ever).
  OR1 (blind): the mirror, Rule 86, does not certify within 1024 steps of period (its left band is the nested side,
      whose periods double about every three diagonals); nor do the linear rules 90 and 150.
  OR2 (blind): between 5 and 30 of the 128 rules certify with a band whose largest diagonal period at K is at least
      4 (a nontrivial band); the rest are trivial (largest period 1 or 2) or uncertified.
  OR3 (blind): among the nontrivial certified bands, Rule 30's period at K (16) is the smallest or tied: no other
      rule combines a certified band with periods as small over 8,192 diagonals.
  OR4 (blind): at least one rule other than 30 has eventually white diagonals at the same positions 2 and 7 (the
      first two doublings are a property of the local rule near the edge, shared by rules that agree with 30 on the
      neighbourhoods the edge sees).
  CF  (counterfactual, must fail): Rule 2's strip has a period doubling. It must not.
REFUTED-BY: OR0 or CF failing (the instrument); OR1 to OR4 the other way.

OUTCOME of the first run, 2026-10-06 (K = 8192, 40,000 steps, 7 seconds), on the 128 rules with f(0,0,1) = 1: OR0 and
  CF PASSED; OR1 HELD (86, 90, 150 uncertified); 9 rules certified with a nontrivial band (30, 91, 103, 107, 110, 111,
  118, 135, 151), 102 trivial, 17 uncertified; OR2 HELD (9); OR3 REFUTED (periods 4 and 8 exist); OR4 HELD by rule 135,
  which showed exactly Rule 30's white diagonals 2, 7, 28, 399 and its doublings two diagonals earlier.
  BUT THE INSTRUMENT WAS MIS-SCOPED: the strip assumes the white left tail stays white, which needs f(0,0,0) = 0 as
  well as f(0,0,1) = 1. Six of the nine (91, 103, 107, 111, 135, 151) have f(0,0,0) = 1: their background turns black
  at the first step and the strip computed a frame that no configuration of theirs realises. Rule 135 is Rule 30's
  colour-complement (f'(n) = not f(not n)), so its coincidence with Rule 30's band is that relation seen through the
  invalid frame, not a second rule with the same left side. The valid domain is the 64 rules with f(0,0,0) = 0 and
  f(0,0,1) = 1. The second run restricts to them; the predictions are the same, re-evaluated on the right domain.

OUTCOME of the second run, 2026-10-06 (the 64 valid rules; 3 seconds): OR0, CF PASSED; OR1 HELD. Certified with a
  nontrivial band: 30 (period 16, white 2, 7, 28, 399), 110 (period 32 at 8192, no white diagonal, doublings at 2, 3,
  5, 7, 45) and 118 (period 4, no white diagonal). Trivial (largest period below 4): 47 rules. Uncertified within
  period 1024: 14 (18, 22, 26, 82, 86, 90, 102, 126, 146, 150, 154, 182, 210, 218). OR2 REFUTED (3, not 5 to 30);
  OR3 REFUTED (118 has period 4, 110 has 32); OR4 REFUTED (no valid rule shares 2 and 7). Rule 30 is the only rule
  of the 64 whose band doubles through eventually white diagonals, Rowland's mechanism; Rule 110's band doubles
  without them.
"""
import sys
import numpy as np

K = int(sys.argv[1]) if len(sys.argv) > 1 else 8192
STEPS = int(sys.argv[2]) if len(sys.argv) > 2 else 40000
KEEP = 1024
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def make_step(rule, K):
    mask = (1 << K) - 1
    terms = [(n, (n >> 2) & 1, (n >> 1) & 1, n & 1) for n in range(8) if (rule >> n) & 1]

    def step(v):
        l, c, r = (v << 2) & mask, (v << 1) & mask, v
        out = 0
        for n, a, b, cc in terms:
            out |= (l if a else l ^ mask) & (c if b else c ^ mask) & (r if cc else r ^ mask)
        return out & mask
    return step


def to_bits(v, K):
    return np.unpackbits(np.frombuffer(v.to_bytes((K + 7) // 8, "little"), dtype=np.uint8), bitorder="little")[:K]


def minimal_period(seq):
    n = len(seq)
    for p in range(1, n + 1):
        if n % p == 0 and all(seq[i] == seq[i + p] for i in range(n - p)):
            return p
    return n


def band(rule):
    step = make_step(rule, K)
    v, hist = 1, []
    for t in range(STEPS):
        v = step(v)
        if t >= STEPS - KEEP:
            hist.append(v)
    period = next((p for p in range(1, KEEP) if hist[-1] == hist[-1 - p]), None)
    if period is None:
        return None
    cyc = hist[-period:]
    U = np.array([to_bits(x, K) for x in cyc], dtype=np.uint8)
    anyk = U.any(axis=0)
    white = [int(k) for k in np.nonzero(~anyk)[0]]
    # per-diagonal periods, sampled: every diagonal below 64, then every 64th
    sample = list(range(64)) + list(range(64, K, 64))
    pers = {k: minimal_period(U[:, k].tolist()) for k in sample}
    maxper = max(pers.values())
    # doublings: diagonals where the sampled period first exceeds every earlier one
    doublings, best = [], 0
    for k in range(K):
        pk = minimal_period(U[:, k].tolist()) if k < 1024 else None
        if pk is None:
            break
        if pk > best:
            best = pk; doublings.append((k, pk))
    return period, white, maxper, doublings


def main():
    rules = [r for r in range(256) if (r >> 1) & 1 and not (r & 1)]     # the edge moves at speed 1 and the tail stays white
    rows = {}
    for r in rules:
        rows[r] = band(r)
    r30 = rows[30]
    ok0 = r30 is not None and r30[0] == 16 and [w for w in r30[1] if w < 1000] == [2, 7, 28, 399]
    r2 = rows[2]
    ok0 &= r2 is not None and r2[0] == 1 and r2[1] == list(range(1, K))
    report("OR0 Rule 30's band is the recorded one (2, 7, 28, 399; period 16); Rule 2's strip is period 1, all white but 0",
           ok0, f"30: {None if r30 is None else (r30[0], [w for w in r30[1] if w < 1000])}; 2: period {None if r2 is None else r2[0]}")
    report("CF  Rule 2's strip has no period doubling", r2 is not None and len(r2[3]) == 1)
    verdict("OR1 the mirror 86 and the linear rules 90, 150 do not certify within period 1024",
            all(rows[r] is None for r in (86, 90, 150)),
            ", ".join(f"{r}: {'uncertified' if rows[r] is None else 'period ' + str(rows[r][0])}" for r in (86, 90, 150)))
    nontrivial = sorted(r for r in rules if rows[r] is not None and rows[r][2] >= 4)
    trivial = sorted(r for r in rules if rows[r] is not None and rows[r][2] < 4)
    uncert = sorted(r for r in rules if rows[r] is None)
    print(f"   certified with a nontrivial band ({len(nontrivial)}): " +
          ", ".join(f"{r} (period {rows[r][0]}, max {rows[r][2]}, white {len(rows[r][1])})" for r in nontrivial), flush=True)
    print(f"   certified trivial ({len(trivial)}): {trivial}", flush=True)
    print(f"   uncertified within 1024 ({len(uncert)}): {uncert}", flush=True)
    for r in nontrivial:
        print(f"   rule {r}: white below 1000 {[w for w in rows[r][1] if w < 1000]}; doublings {rows[r][3][:8]}", flush=True)
    verdict("OR2 between 5 and 30 rules certify with a nontrivial band", 5 <= len(nontrivial) <= 30, f"{len(nontrivial)}")
    smallest = min((rows[r][0] for r in nontrivial), default=None)
    verdict("OR3 Rule 30's period at K is the smallest or tied among nontrivial certified bands",
            r30 is not None and smallest is not None and r30[0] <= smallest, f"30: {r30[0] if r30 else None}; smallest {smallest}")
    shared = [r for r in nontrivial if r != 30 and rows[r][1][:2] == [2, 7]]
    verdict("OR4 some other rule has eventually white diagonals at 2 and 7", len(shared) > 0, f"{shared}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
