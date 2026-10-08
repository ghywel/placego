#!/usr/bin/env python3
"""rule30_cloud_review_g236.py: Cloud's independent replay of GPT's G236 (GC549 checkpoint 28), and a sharpening.

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_review_g236.py [N=18]
COST:       a few seconds.

G236 (PROOFS.md waiting room) says: take a right row whose sites 1 .. 4 are 0001, with the wall white at time 0,
black at 1 and white at 2. Two steps later the row cannot begin 11100011. GPT's certificate is a sixteen-state
spatial transducer for the two-step bulk map F and three subset steps. This script shares no code with GPT's
`rule30_gpt_entry_image.py`. Rows are lists of bits, site 0 is the wall, Rule 30 is x' = l XOR (c OR r), and every
check is brute force over whole initial rows of N sites (the far end is padded white, and only outputs that its
light cone cannot reach are read). Checks R1 .. R5 restate GPT's values, so each is a control that should PASS.
  R1: F(a,b,c,d,e) = (a XOR (b OR c)) XOR ((b XOR (c OR d)) OR (c XOR (d OR e))) equals two literal steps on all
      32 bulk windows.
  R2: from prefix 0001 the two-step row begins 1110 for every tail, and its site 5 is white exactly when z = 0 or
      u = v = 0 (z, u, v the initial sites 5, 6, 7).
  R3: over those rows, the initial sites 4 .. 7 take exactly the states A = {1000, 1001, 1010, 1011, 1100}.
  R4: the subset steps image(A, 0) = {0001, 0010, 0011}, then on 1 {0010, 0011}, then on 1 the empty set.
  R5: end to end, no initial row with prefix 0001 gives a two-step row beginning 11100011, and every shorter tail
      (sites 6, 6..7) after 11100 does occur, so 011 is a shortest missing tail.
UNEXPECTED CHECK (Cloud's, predicted by hand before the run): G236's premise 0001 is not needed.
  U1: with the same wall, the two-step prefix 111 alone forces the initial prefix 0001. By hand: w1 = 1 XOR (y1 OR
      y2) forces y1 = y2 = 0; y1 = x1 OR x2 and y2 = x1 XOR (x2 OR x3) give x1 = x2 = x3 = 0; w2 = y3 = x4 forces
      x4 = 1. Prediction: no initial row at all reaches 11100011. Confidence 0.9. If it holds, G236 is a statement
      about the walled two-step image itself: at every white time t >= 2 of a period-2 wall form, sites 1 .. 8
      never read 11100011, whatever the row at t - 2 was.
  U2: the minimal words missing from the walled two-step image (prefixes from site 1, length <= 10). Predictions:
      11100011 is one of them (confidence 0.85), and at least one other minimal missing word of length <= 8
      exists (confidence 0.6).
Counterfactual: if U1 fails, some row without prefix 0001 reaches 11100011 and the history premise does real work.

OUTCOME, 2026-10-08 (by 15:43 BST; N = 18, 3 s): R1 .. R5 PASS. A is exactly {1000, 1001, 1010, 1011, 1100}, the
  subset steps are as GPT states, and after 11100 the only missing 3-bit tail is 011. U1 HELD: no row of 18 sites
  reaches 11100011, and every row whose two-step prefix is 111 starts 0001. U2a HELD and U2b HELD: the walled image
  has 65 minimal missing prefixes up to length 10. The shortest is 110, then 0110, 1010, 1111, and 11100011 is one
  of 9 of length 8. Post-hoc, same run: the image's prefix counts for lengths 1 .. 14 are 2, 4, 7, 11, 20, 38, 69,
  129, 247, 464, 883, 1694, 3233, 6211. Each new site multiplies them by about 1.9, so most of the restriction sits
  near the wall. Hand reading in PROOFS.md under G236.
"""
import sys
from itertools import product

N = int(sys.argv[1]) if len(sys.argv) > 1 else 18


def step(row, wall):
    """One Rule 30 step of sites 0 .. n-1 (site 0 the wall, set to `wall` after the step); far end white."""
    n = len(row)
    ext = row + [0]
    return [wall] + [ext[i - 1] ^ (ext[i] | ext[i + 1]) for i in range(1, n)]


def two_steps(right):
    """Sites 1 .. of the row two steps after initial sites 1 .. = right, wall 0, 1, 0 at times 0, 1, 2."""
    return step(step([0] + list(right), 1), 0)[1:]


def F(a, b, c, d, e):
    return (a ^ (b | c)) ^ ((b ^ (c | d)) | (c ^ (d | e)))


def report(name, ok, detail=""):
    print(name, "PASS" if ok else "FAIL", detail)


def main():
    ok1 = True
    for a, b, c, d, e in product((0, 1), repeat=5):
        y = [a ^ (b | c), b ^ (c | d), c ^ (d | e)]                      # literal: three sites after one step
        ok1 &= F(a, b, c, d, e) == y[0] ^ (y[1] | y[2])
    report("R1", ok1)

    reach = N - 2                                     # two-step outputs at sites <= N - 2 see no padding
    rows = [(0, 0, 0, 1) + t for t in product((0, 1), repeat=N - 4)]
    outs = [tuple(two_steps(r)[:reach]) for r in rows]
    ok2 = all(o[:4] == (1, 1, 1, 0) for o in outs)
    ok2 &= all((o[4] == 0) == (r[4] == 0 or (r[5] == 0 and r[6] == 0)) for r, o in zip(rows, outs))
    report("R2", ok2)
    A = {r[3:7] for r, o in zip(rows, outs) if o[4] == 0}
    want = {tuple(int(c) for c in s) for s in ("1000", "1001", "1010", "1011", "1100")}
    report("R3", A == want, str(sorted("".join(map(str, s)) for s in A)))

    def image(S, bit):
        return {s[1:] + (e,) for s in S for e in (0, 1) if F(*s, e) == bit}
    s1 = image(A, 0)
    s2 = image(s1, 1)
    s3 = image(s2, 1)
    fmt = lambda S: sorted("".join(map(str, s)) for s in S)
    report("R4", (fmt(s1), fmt(s2), s3) == (["0001", "0010", "0011"], ["0010", "0011"], set()),
           f"{fmt(s1)} {fmt(s2)} {fmt(s3)}")
    tails = {o[5:8] for o in outs if o[:5] == (1, 1, 1, 0, 0)}
    short = {t[:1] for t in tails} | {t[:2] for t in tails}
    missing3 = sorted("".join(map(str, t)) for t in product((0, 1), repeat=3) if t not in tails)
    report("R5", (0, 1, 1) not in tails and len(short) == 6, f"missing 3-bit tails after 11100: {missing3}")

    allout = [(r, tuple(two_steps(r)[:reach])) for r in product((0, 1), repeat=N)]
    img = {o for _, o in allout}
    hits = [r for r, o in allout if o[:8] == (1, 1, 1, 0, 0, 0, 1, 1)]
    forced = all(r[:4] == (0, 0, 0, 1) for r, o in allout if o[:3] == (1, 1, 1))
    print("U1", "HELD" if not hits and forced else "REFUTED",
          f"(rows reaching 11100011: {len(hits)}; prefix 111 forces 0001: {forced})")
    present = {o[:k] for o in img for k in range(1, 11)}
    minimal = []
    for k in range(1, 11):
        for w in product((0, 1), repeat=k):
            if w not in present and (k == 1 or w[:-1] in present):
                minimal.append("".join(map(str, w)))
    print("U2 minimal missing prefixes (length <= 10):", minimal)
    print("U2a", "HELD" if "11100011" in minimal else "REFUTED")
    print("U2b", "HELD" if any(len(w) <= 8 and w != "11100011" for w in minimal) else "REFUTED")


if __name__ == "__main__":
    main()
