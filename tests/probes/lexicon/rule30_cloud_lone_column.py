#!/usr/bin/env python3
"""rule30_cloud_lone_column.py: a two-colour, asymmetric automaton with exactly one eventually periodic column?

RUN-ON:     cpu (Python 3 standard library; big-integer rows)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_lone_column.py [T=4096]
COST:       expected a few minutes at T = 4096 (256 elementary rules and 98 linear rules).

Why. Math SE 4141181, "Periodic columns in asymmetrical 1D cellular automata?" (Trevor, 2021-05-16), asks for a
two-colour automaton of any range, with an asymmetric rule and a start such as 0^inf 1 0^inf, that has at least one
but not infinitely many eventually periodic columns, with aperiodic columns on both sides of one. Its motivation is
Rule 30: every known example (Rule 150, say) has a symmetric rule, whose symmetric start keeps the centre on the
mirror axis. The survey (CL085) could not read the one answer. The owner fetched it (2026-10-09): Johan Kopra
(2022-01-19, accepted) reduces three colours to two by marker words w0 = 0000011, w1 = 0000101, w2 = 0001001, which
never overlap, and simulates a three-colour solution by a two-colour automaton of larger range, run on the encoded
start (w0)^inf w1 (w0)^inf. The question has the same shape as the prize's: one column periodic among aperiodic
ones. Kopra's own barrier (§8.77) is Rule 90, symmetric. An asymmetric example would show that the barrier does not
rest on symmetry.

Reasoning before the run (Cloud, by hand; checked by the run).
  K1. The reduction keeps infinitely many constant columns. An overlap of length one between two marker words
      (last letter of one = first letter of the next) is forbidden, so every word's last letter differs from every
      word's first letter: in a binary non-overlapping code all words share their first letter, and all share their
      last letter. In the encoded configuration the first and last offsets of every block of seven are constant
      columns. Here offsets 0, 1, 2 and 6 agree in all three words, four constant columns per block, and the
      question excludes infinitely many periodic columns. Wherever the simulated column avoids symbol 2, the offsets
      where w0 and w1 agree (0, 1, 2, 3, 6) are constant too.
  K2. A literal answer, by symmetry in disguise. From a single cell Rule 90 never shows 011, 110 or 111 (black cells
      sit on one parity of i + t), so Rules 18, 26, 82, 90, 146, 154, 210 and 218 all give its orbit. Rules 26, 82,
      154 and 210 are asymmetric, and Rule 90's centre column is 1 then white for ever, with every other column
      aperiodic. The orbit is the symmetric Sierpinski triangle, so this meets the letter of the question, not its
      motivation.
  K3. An asymmetric linear rule with a lone white column: x_{t+1}(j) = x_t(j+1) xor x_t(j-3), the polynomial
      p = X^-1 + X^3, range 3. From one cell x_t(j) = C(t, k) mod 2 with 4k = t + j.
      Column 0 reads C(4s, s), which is odd iff s & 3s = 0 (Kummer): impossible for s > 0, since the lowest set bit
      of s is also set in 3s. So column 0 is 1 at t = 0 and white for ever after.
      Every column j != 0 has infinitely many black cells: k = 2^m for j > 0 (3k - j has bit m clear); for j = -v,
      3k + v = 2^M when v is not a multiple of 3, and 3k + v = 2^M + 2^N (M - N odd, 2^N > v / 3) when it is.
      Every column also has white runs of unbounded length: for t in [2^M, 2^M + 2^(M-3)), Lucas makes C(t, k) odd
      only for k <= t - 2^M or k >= 2^M, and k = (t + j) / 4 lies strictly between. So column j != 0 is not
      eventually periodic. Exactly one eventually periodic column, aperiodic columns on both sides, an asymmetric
      rule (its mirror is X^-3 + X), and a row that is not symmetric about column 0 (support [-t, 3t]).
      Caveat: p = X (X^-2 + X^2) is Rule 90 dilated by two and moving right one cell a step, so the orbit is mirror
      symmetric about the moving line j = t. Column 0 is not that axis; its whiteness is a carry fact (s & 3s != 0),
      not a reflection. A sceptic may still call the rule symmetric in a moving frame.

Method. Single-cell orbits to T rows. Column j is "eventually periodic (measured)" when rows T/2 .. T-1 repeat with
some period at most T/8. For linear rules (x_{t+1}(j) = xor of x_t(j - k), k in S, S a subset of -3..3 with a
negative and a positive element) eventual whiteness is also decided exactly. Columns are 2-automatic:
c_j(2t) = c_{j/2}(t) (0 for odd j) and c_j(2t+1) = sum of c_{(j-k)/2}(t) over k in S with j - k even, so the
combinations of columns reachable from c_j form a finite automaton read on t's binary digits from the low end, and
"eventually white" means it accepts only finitely many t. A rule "qualifies" when it has a periodic column with
aperiodic columns on both sides in -J .. J (J = 64), and no periodic column beyond |j| = J/2 (a proxy for finitely
many). Its orbit is "fully asymmetric" when it is not mirror symmetric about any axis, fixed or moving: for linear
rules, S is not a palindrome up to a shift; for elementary rules, row T - 1 trimmed of background is not a
palindrome.

PREDICTIONS, written 2026-10-09 17:46 BST, before any run of this script (T = 4096).
  LC-C0 (control, 0.97): the three marker words have no overlap at shifts 1 .. 6; the offsets common to all three
         are exactly {0, 1, 2, 6}; w0 and w1 agree exactly at {0, 1, 2, 3, 6}.
  LC-C1 (control, 0.97): Rules 18, 26, 82, 146, 154, 210 and 218 reproduce Rule 90's single-cell orbit for every
         row below T.
  LC-C2 (control, 0.95): the automaton's c_j(t) equals the simulation for every linear rule, |j| <= J, t < 256.
  LC-P1 (0.95): for X^-1 + X^3, column 0 is white for 1 <= t < T and exactly eventually white; every other column
         with |j| <= J is aperiodic (measured) and not eventually white (exact); Kummer's formula matches every cell
         of the simulation; the black cells K3 constructs are black.
  LC-P2 (0.5): at least one fully asymmetric linear rule qualifies.
  LC-P3 (0.35): at least one fully asymmetric elementary rule qualifies (single cell, T = 4096). Rules 30 and 86
         have no periodic column in the window (as the record expects), and at least four symmetric-orbit rules
         qualify, Rule 90 among them.
  LC-U, the unexpected check (0.5): among the primitive linear rules (gcd of S is 1, so no sublattice of
         identically white columns), every eventually white column (exact test, |j| <= J) lies in a rule whose
         exponents are all odd, the moving-frame dilation of K3.
  Counterfactual. If LC-P1 fails, K3's proof has an error and the example dies. If LC-P2 or LC-P3 holds, the question
  is answered in its spirit too, and the counter-model library (CL084) gains a barrier with no symmetry at all. If
  both fail, the honest answer is K3: asymmetric rule, asymmetric rows, symmetric only in a moving frame.
"""
import sys

T = int(sys.argv[1]) if len(sys.argv) > 1 else 4096
J = 64
PMAX = T // 8
W = ['0000011', '0000101', '0001001']


def markers():
    overlaps = [(a, b, s) for a in W for b in W for s in range(1, 7) if a[s:] == b[:7 - s]]
    constant = [i for i in range(7) if len({w[i] for w in W}) == 1]
    agree01 = [i for i in range(7) if W[0][i] == W[1][i]]
    return overlaps, constant, agree01


def eca_rows(rule):
    """Rows 0 .. T-1 from one black cell; bit off + i holds cell i. Cells beyond the array read white, so a rule
    with 000 -> 1 grows edge artefacts; the array is wide enough that they cannot reach row t's cone before row T."""
    off = 2 * T + J + 2
    mask = (1 << (2 * off + 1)) - 1
    x = 1 << off
    rows = [x]
    for _ in range(T - 1):
        l, r = (x << 1) & mask, x >> 1
        nl, nx, nr = ~l & mask, ~x & mask, ~r & mask
        y = 0
        for v in range(8):
            if rule >> v & 1:
                y |= (l if v & 4 else nl) & (x if v & 2 else nx) & (r if v & 1 else nr)
        x = y
        rows.append(x)
    return rows, off


def linear_rows(S):
    off = 3 * T + J + 8
    x = 1 << off
    rows = [x]
    for _ in range(T - 1):
        y = 0
        for k in S:
            y ^= (x << k) if k >= 0 else (x >> -k)
        x = y
        rows.append(x)
    return rows, off


def columns(rows, off):
    lo, n = off - J, 2 * J + 1
    m = (1 << n) - 1
    fmt = '0%db' % n
    strs = [format((x >> lo) & m, fmt)[::-1] for x in rows]
    return [''.join(c) for c in zip(*strs)]          # cols[j + J][t]


def tail_period(s):
    tail = s[T // 2:]
    n = len(tail)
    key = tail[:64]
    pos = tail.find(key, 1)
    while pos != -1 and pos <= PMAX:
        if tail[pos:] == tail[:n - pos]:
            return pos
        pos = tail.find(key, pos + 1)
    return 0


def classify(cols):
    per = {j: tail_period(cols[j + J]) for j in range(-J, J + 1)}
    P = [j for j in per if per[j]]
    A = [j for j in per if not per[j]]
    ok = bool(P) and all(abs(j) <= J // 2 for j in P) and \
        any(any(a < c for a in A) and any(a > c for a in A) for c in P)
    return P, ok, per


def row_symmetric(x, off, t):
    lo = off - t - 1
    s = format((x >> lo) & ((1 << (2 * t + 3)) - 1), '0%db' % (2 * t + 3))
    s = s.strip(s[0])
    return s == s[::-1]


def gcd_all(S):
    from math import gcd
    g = 0
    for k in S:
        g = gcd(g, abs(k))
    return g


def palindromic(S):
    m = min(S) + max(S)
    return set(S) == {m - k for k in S}


def automaton(S):
    memo = {}

    def E(v):
        key = (0, v)
        if key not in memo:
            memo[key] = frozenset(j // 2 for j in v if j % 2 == 0)
        return memo[key]

    def O(v):
        key = (1, v)
        if key not in memo:
            out = set()
            for j in v:
                for k in S:
                    if (j - k) % 2 == 0:
                        out ^= {(j - k) // 2}
            memo[key] = frozenset(out)
        return memo[key]
    return E, O


def value(S, j, t, maps):
    E, O = maps
    v = frozenset([j])
    while t:
        v = O(v) if t & 1 else E(v)
        t >>= 1
    return 1 if 0 in v else 0


def eventually_white(S, j, maps):
    """Exact: True iff column j has only finitely many black cells."""
    E, O = maps
    start = frozenset([j])
    seen, stack, succ = {start}, [start], {}
    while stack:
        u = stack.pop()
        succ[u] = (E(u), O(u))
        for w in succ[u]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    good = {u for u in seen if 0 in succ[u][1]}       # an O-step (top bit 1) into a state holding column 0
    pred = {u: [] for u in seen}
    for u in seen:
        for w in succ[u]:
            pred[w].append(u)
    co, stack = set(good), list(good)
    while stack:
        w = stack.pop()
        for u in pred[w]:
            if u not in co:
                co.add(u)
                stack.append(u)
    # a state of co on a cycle gives infinitely many accepted t
    index, low, onstack, st, cyc, counter = {}, {}, set(), [], set(), [0]
    for root in seen:
        if root in index:
            continue
        work = [(root, 0)]
        while work:
            u, i = work.pop()
            if i == 0:
                index[u] = low[u] = counter[0]
                counter[0] += 1
                st.append(u)
                onstack.add(u)
            nxt = succ[u]
            if i < 2:
                w = nxt[i]
                work.append((u, i + 1))
                if w not in index:
                    work.append((w, 0))
                elif w in onstack:
                    low[u] = min(low[u], index[w])
                continue
            for w in nxt:
                if w in onstack:
                    low[u] = min(low[u], low[w])
            if low[u] == index[u]:
                comp = []
                while True:
                    w = st.pop()
                    onstack.discard(w)
                    comp.append(w)
                    if w == u:
                        break
                if len(comp) > 1 or u in nxt:
                    cyc.update(comp)
    return not (cyc & co)


def kummer_row(t, off):
    """Row t of X^-1 + X^3 from Lucas: C(t, k) is odd iff k is a submask of t; the cell is j = 4k - t."""
    x, k = 0, t
    while True:
        x |= 1 << (off + 4 * k - t)
        if k == 0:
            return x
        k = (k - 1) & t


def kummer(t, j):
    if (t + j) % 4:
        return 0
    k = (t + j) // 4
    return 1 if 0 <= k <= t and k & (t - k) == 0 else 0


def main():
    print('T = %d, J = %d, periods up to %d over rows %d .. %d' % (T, J, PMAX, T // 2, T - 1))
    ov, const, agree = markers()
    print('LC-C0: overlaps %s; offsets common to all words %s; w0 = w1 at %s' % (ov, const, agree))

    base, off90 = eca_rows(90)
    same = [r for r in (18, 26, 82, 146, 154, 210, 218) if eca_rows(r)[0] == base]
    print('LC-C1: rules reproducing Rule 90 from one cell: %s' % same)

    print('Elementary rules (single cell):')
    eca_ok = []
    for rule in range(256):
        rows, off = eca_rows(rule)
        P, ok, per = classify(columns(rows, off))
        sym = row_symmetric(rows[-1], off, T - 1)
        if ok or rule in (30, 86, 90):
            print('  rule %3d: periodic columns %s; qualifies %s; row %d symmetric %s'
                  % (rule, P if len(P) <= 12 else '%d columns' % len(P), ok, T - 1, sym))
        if ok:
            eca_ok.append((rule, sym))
    print('  qualifying: %d (%d fully asymmetric: %s)' % (len(eca_ok), sum(1 for r, s in eca_ok if not s),
                                                       [r for r, s in eca_ok if not s]))

    print('Linear rules x_{t+1}(j) = xor of x_t(j - k), k in S:')
    lin_ok, white_found, c2_bad, cross = [], [], 0, [0, 0]
    subsets = []
    for mask in range(1, 128):
        S = [k for k in range(-3, 4) if mask >> (k + 3) & 1]
        if min(S) < 0 < max(S):
            subsets.append(S)
    for S in subsets:
        rows, off = linear_rows(S)
        cols = columns(rows, off)
        P, ok, per = classify(cols)
        maps = automaton(S)
        for j in range(-J, J + 1):
            for t in range(256):
                if value(S, j, t, maps) != int(cols[j + J][t]):
                    c2_bad += 1
        white = [j for j in range(-J, J + 1) if eventually_white(S, j, maps)]
        for j in range(-J, J + 1):
            last = cols[j + J].rfind('1')
            if j in white and last >= T // 2:
                cross[0] += 1                        # exact says white, a black cell late in the tail
            if j not in white and last < T // 2:
                cross[1] += 1                        # exact says black again, none seen in the tail
        if white and gcd_all(S) == 1:
            white_found.append((S, white))
        if ok:
            lin_ok.append((S, palindromic(S), P, white))
            print('  S = %-16s palindromic %-5s periodic %s; eventually white (exact) %s'
                  % (S, palindromic(S), P, white))
    print('LC-C2: automaton/simulation disagreements %d (t < 256); exact-white columns black in the tail %d;'
          ' exact-not-white columns with no black cell in the tail %d' % (c2_bad, cross[0], cross[1]))
    print('  qualifying: %d (%d fully asymmetric)' % (len(lin_ok), sum(1 for x in lin_ok if not x[1])))
    print('LC-U: primitive rules with an eventually white column: %s'
          % [(S, w if len(w) <= 8 else '%d columns' % len(w)) for S, w in white_found])
    print('      all such rules have only odd exponents: %s' % all(all(k % 2 for k in S) for S, w in white_found))

    S = [-1, 3]
    rows, off = linear_rows(S)
    cols = columns(rows, off)
    P, ok, per = classify(cols)
    maps = automaton(S)
    col0_black = [t for t in range(1, T) if cols[J][t] == '1']
    white = [j for j in range(-J, J + 1) if eventually_white(S, j, maps)]
    bad = sum(1 for t, x in enumerate(rows) if x != kummer_row(t, off))
    built = 0
    for j in range(-J, J + 1):
        if j == 0:
            continue
        if j > 0:
            k = 1 << j.bit_length()
        else:
            v = -j
            M = v.bit_length() + 2
            if v % 3:
                while (1 << M) % 3 != v % 3:
                    M += 1
                k = ((1 << M) - v) // 3
            else:
                N = max(1, (v // 3).bit_length() + 1)
                M = N + 2 * v.bit_length() + 3
                if (M - N) % 2 == 0:
                    M += 1
                k = ((1 << M) + (1 << N) - v) // 3
        t = 4 * k - j
        built += kummer(t, j)
    print('LC-P1: X^-1 + X^3: column 0 black at t >= 1: %s; exact eventually white columns %s; periodic (measured) %s;'
          % (col0_black[:5], white, P))
    print('       rows differing from Lucas %d of %d; constructed black cells black %d of %d' % (bad, T, built, 2 * J))


if __name__ == '__main__':
    main()
