#!/usr/bin/env python3
"""rule30_SL_mixed_budget.py: does GC1148/GC1151's record budget extend from pure S and pure L residences to mixed S/L
residences? Loop check 2 (L700) drew door 6, the finite-support record route; this is Local's block there as the maths
lead (AGENTS.md item 19), on the item GC1151 left open: "Mixed words still need a separate record bound."

Background. GC1149 and GC1151 give an exact full-time lift for every completed white-time S/L word: each S gap (1001)
lifts to 110100 and each L gap (100001) to 1101000100, with no startup loss. Beside the clock (wall white at the anchor
a), the forced left row at time a at depths 0 .. N-1 is fixed by the first N full-time samples (depth k uses samples
0 .. k). GC1148's argument then gives, for any S/L lift u: if every image of an N-tick S/L lift has white runs at most g
at depths >= k0, a zero band [d, d+L) forbids an S/L residence of N >= d + a + g + 1 ticks at any anchor a with
L >= 2a + g + 1 (the white triangle meets the image in g + 1 cells). Pure S has g = 5 (GC1148's 84-ring), pure L g = 6
(GC1151's 155-ring). If mixtures have a uniform g, the budget holds for every S/L residence, mixed or not.

RUN-ON:     cpu, numpy; seconds to minutes.
COMMAND:    python3 tests/probes/lexicon/rule30_SL_mixed_budget.py

Record searched (record_find, 2026-10-13 23:47 BST): 'residence' -> 34 hits in 17 files (GC1102, GC1126, GC1148,
GC1151; pure-letter budgets only); 'record-conditioned|record conditioned' -> 13 hits in 8 files (GC1148 .. GC1151);
'largest cyclic.*white|cyclic spatial white gap' -> 4 hits in 2 files (the 84- and 155-ring gaps 5 and 6);
'mixed S/L|mixed word|mixed SL' -> 30 hits in 11 files (GC704/705's all-S results, the board; no mixed budget);
'S/L.*image|image.*S/L' -> 16 hits in 5 files (none an image bound); 'separate record bound' -> 1 hit (GC1151). GC1148,
GC1149 and GC1151 read.

PREDICTIONS (written 2026-10-13 23:49 BST and committed in 777abed9 at 23:50:29, first labelled 23:55, ahead of the
  clock; M1's two ring values and the scalar check on one word were seen in a sizing pre-check before that commit).
  AMENDED (2026-10-14 00:01 BST, before any census output was seen): 777abed9's run reached N = 180, 6.7 million lifts
  (about 10 GB); it was stopped for memory with its output unread (piped through tail). The scope below is cut to
  N = 150 (468,304 lifts); the thresholds are unchanged.
  M1 must hold (instrument): the pure S lift's image has longest white run 5 and the pure L lift's 6, at depths >= 12
     with N = 180, matching the rings of GC1148 and GC1151; and every image's depths 0 .. 5 depend only on the first
     block (locality, depth k uses samples 0 .. k).
  M2 blind (0.7): over every S/L lift of N ticks (all block orders, the last block truncated), the longest white run at
     depths >= 12 grows with N, by at least 3 from N = 60 to N = 150: no uniform mixed budget at these sizes.
     Counterfactual: a plateau of at most 8 from N = 90 to 150, a candidate constant g_SL for an all-depth mixed budget
     (GC1151's open item).
  M3 (reported, no prediction): a coin control (uniform random full-time column-1 words, the same count and length)
     and the S/L maximum against log2 of the number of words.
  M4 blind (0.6, the second fixture): 10,000 random S/L lifts of 600 ticks reach, at some depth > 150, a white run
     longer than the exhaustive N = 150 maximum.
  Unexpected check: the run lengths are also computed by a slow scalar loop on 50 words, compared with the vector code.

OUTCOME (2026-10-14 00:02 BST, M5, about 10 minutes; machine output quoted): M1 HELD, M2 HELD, M4 HELD; the
  unexpected check passed (scalar loop = vector code on 50 words).
  N= 60:    159 S/L lifts, longest white run  9 (log2 W =  7.3); coin control 14
  N= 90:   2307 S/L lifts, longest white run 13 (log2 W = 11.2); coin control 15
  N=120:  32820 S/L lifts, longest white run 17 (log2 W = 15.0); coin control 18
  N=150: 468304 S/L lifts, longest white run 19 (log2 W = 18.8); coin control 22
  M4: random 600-tick lifts reach 20 at depths > 150 (exhaustive N = 150 maximum 19).
  Reading: no constant mixed budget. The longest white run tracks log2 of the number of lifts (the coin law), so a
  mixed S/L residence's image allows white runs of about 0.125 per tick. Scope: these are all S/L block orders (the
  free shift, 0.256 bits per visible bit, above the channel bound 0.1236), not the real S/L sublanguage.

ADDENDUM PREDICTION (2026-10-14 00:03 BST, before the run; the second fixture of the loop-check rule's step 4).
  M5 blind (0.65): restricted to lifts whose blocks' visible bits (100 for S, 10000 for L) avoid the certified phase-0
     list (mfw44all plus cuts40) throughout, the longest white run at depths >= 12 still grows by at least 3 from
     N = 60 to N = 150, and the restricted count still grows. Counterfactual: a plateau of at most 8, a candidate
     constant budget for real S/L residences. The visible word from a white anchor is a phase-0 word of the
     configuration at that time, so the restriction removes no real residence.
  M5 HELD (2026-10-14 00:03 BST, seconds): cut-avoiding lifts 139, 613, 2809, 12186 at N = 60, 90, 120, 150, longest
     white runs 9, 10, 13, 15 (log2 W = 7.1, 9.3, 11.5, 13.6). Still the coin law, at 0.146 bits per visible bit.
     Scope: the 44-bit list and cuts40 only. CL340's typed-path bound (466 ticks, with the 114-, 117- and 178-bit cuts)
     is beyond this N; whether S/L lifts are typed paths there is put to GPT (L700).
  GPT's GC1214 read: S/L lifts are not CL340 typed paths (the 84- and 155-rings are eternal S and L words). M2, M4 and
     M5 refute small constants only, and 20 bounds every observation, so a uniform mixed budget remains open. The
     zero-entropy reading in L700 is withdrawn. lifts_cut's counts are a subset (whole last blocks are tested before
     truncation), not an exhaustive count of cut-avoiding residences.

ADDENDUM PREDICTION (2026-10-14 00:15 BST, before the run; the second door-6 block, on GC1214's advice to keep realness
  rather than entropy). The visible word from a white anchor (the lift's even samples, 75 of them at N = 150) must lie
  in the phase-0 visible language for the residence to occur in any real configuration at any time. RLK's membership
  query (in_language_phase, kissat) decides that for each word.
  M6 blind (0.55): among the 200 S/L lifts with the longest image white runs at N = 150 (runs from 19 down), fewer than
     half have a real visible word, and the longest run among the real ones is below 19. Counterfactual: the run-19
     lifts are real, so real S/L residences already show runs of 19 within depth 150.
  M6 HELD (2026-10-14 00:16 BST, about a minute): runs 19 .. 15 in the top 200; real visible words 0 of 200 (the seven
     run-19 lifts included). Post hoc instrument controls, run after the outcome: (100)^25 real True, (10000)^15 real
     True, the alternating (100 10000)^9 100 real False, a word starting 11 False.

ADDENDUM PREDICTIONS (2026-10-14 00:17 BST, before the run): enumerate the real S/L lifts directly. A depth-first search
  adds S or L blocks and keeps a prefix only if its visible word is in the phase-0 language (membership is
  prefix-closed). N = 60, 90, 120, 150; cap of 20,000 membership calls.
  M7 blind (0.5): the number of real S/L lifts grows at most polynomially in N (bounded or slowly growing switching
     between S and L), at most 4 times from N = 90 to N = 150. Counterfactual: exponential growth like M5's.
  M8 blind (0.5): the longest image white run over real S/L lifts at N = 150 (depths >= 12) is at most 8, close to
     the pure rings' 5 and 6. Counterfactual: 12 or more, so realness does not bring the runs near the rings.
"""
import os, sys
import numpy as np

S, L = '110100', '1101000100'
K0 = 12


def lifts(N):
    """Every S/L block sequence's full-time lift, truncated to N ticks (deduplicated)."""
    out = set()
    stack = ['']
    while stack:
        w = stack.pop()
        if len(w) >= N:
            out.add(w[:N])
            continue
        stack.append(w + S)
        stack.append(w + L)
    return sorted(out)


def images(words):
    """Forced left rows at the anchor, depths 0 .. N-1, for column-1 words beside the wall 0101 (white at time 0)."""
    W = np.array([[int(c) for c in w] for w in words], dtype=np.uint8)
    n, N = W.shape
    c0 = np.tile((np.arange(N) % 2).astype(np.uint8), (n, 1))
    rows = np.zeros((n, N), dtype=np.uint8)
    rows[:, 0] = 0                                       # depth 0 is the wall, white at time 0
    cur = c0[:, 1:] ^ (c0[:, :-1] | W[:, :-1])          # c_-1(t) = c0(t+1) XOR (c0(t) OR c1(t))
    rows[:, 1] = cur[:, 0]
    a, b = c0[:, :N - 1], cur                            # columns -(j-2) and -(j-1)
    for j in range(2, N):
        nxt = b[:, 1:] ^ (b[:, :-1] | a[:, :b.shape[1] - 1])
        rows[:, j] = nxt[:, 0]
        a, b = b, nxt
    return rows


def scalar_image(w):
    """Slow reference: c_-j(t) = c_-(j-1)(t+1) XOR (c_-(j-1)(t) OR c_-(j-2)(t)), with c_0 the wall and c_1 = w."""
    N = len(w)
    col = {0: [t % 2 for t in range(N)], 1: [int(c) for c in w]}
    row = [0]
    for j in range(1, N):
        prev, prev2 = col[1 - j], col[2 - j]
        col[-j] = [prev[t + 1] ^ (prev[t] | prev2[t]) for t in range(len(prev) - 1)]
        row.append(col[-j][0])
    return row


def longest_white(rows, k0=K0):
    best = np.zeros(rows.shape[0], dtype=np.int32)
    run = np.zeros(rows.shape[0], dtype=np.int32)
    for k in range(k0, rows.shape[1]):
        run = np.where(rows[:, k] == 0, run + 1, 0)
        best = np.maximum(best, run)
    return best


def main():
    rng = np.random.default_rng(20261013)
    # M1
    pS = images([(S * 40)[:180]])
    pL = images([(L * 20)[:180]])
    m1 = int(longest_white(pS)[0]) == 5 and int(longest_white(pL)[0]) == 6
    ws = lifts(90)
    im = images(ws)
    loc = all(np.array_equal(im[i, :6], images([ws[i][:6] + '0' * 84])[0, :6]) for i in range(0, len(ws), max(1, len(ws) // 40)))
    sample = [ws[i] for i in rng.choice(len(ws), size=min(50, len(ws)), replace=False)]
    vec = images(sample)
    unexpected = all(list(vec[i]) == scalar_image(sample[i]) for i in range(len(sample)))
    print('M1 pure S run %d, pure L run %d; locality %s:' % (longest_white(pS)[0], longest_white(pL)[0], loc),
          'HELD' if m1 and loc else 'FAILED', flush=True)
    print('Unexpected check, scalar loop = vector code on 50 words:', unexpected, flush=True)
    table = {}
    for N in (60, 90, 120, 150):
        ws = lifts(N)
        best = longest_white(images(ws))
        coin = longest_white(images([''.join(map(str, rng.integers(0, 2, N))) for _ in range(len(ws))]))
        table[N] = int(best.max())
        print('N=%3d: %7d S/L lifts, longest white run %2d (log2 W = %.1f); coin control %2d' % (
            N, len(ws), best.max(), np.log2(len(ws)), coin.max()), flush=True)
    m2 = table[150] - table[60] >= 3
    plateau = max(table[N] for N in (90, 120, 150)) <= 8 and len({table[N] for N in (90, 120, 150)}) == 1
    print('M2 grows by >= 3 from N=60 to 150:', 'HELD' if m2 else 'REFUTED', '| counterfactual plateau <= 8:', plateau)
    deep = []
    for _ in range(10):
        words = []
        for _ in range(1000):
            w = ''
            while len(w) < 600:
                w += S if rng.random() < 0.5 else L
            words.append(w[:600])
        rows = images(words)
        deep.append(int(longest_white(rows, 151).max()))
    print('M4 random S/L lifts of 600 ticks, longest white run at depths > 150: %d (exhaustive N=150 max %d):' % (
        max(deep), table[150]), 'HELD' if max(deep) > table[150] else 'REFUTED')


def lifts_cut(N, ac):
    """Lifts whose visible bits avoid the certified list, checked block by block (a subset of the cut-avoiding set)."""
    vis = {S: '100', L: '10000'}
    out, stack = set(), [('', 0)]
    while stack:
        w, st = stack.pop()
        if len(w) >= N:
            out.add(w[:N])
            continue
        for b in (S, L):
            s2, ok = st, True
            for ch in vis[b]:
                s2 = int(ac.goto[s2][int(ch)])
                if ac.out[s2]:
                    ok = False
                    break
            if ok:
                stack.append((w + b, s2))
    return sorted(out)


def m5():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import rule30_relaxed_records_k as rlk
    from rule30_seed_prefix_tree import AhoCorasick
    ac = AhoCorasick(rlk.load_forbidden('44all') + rlk.load_cuts(0, 40))
    table, counts = {}, {}
    for N in (60, 90, 120, 150):
        ws = lifts_cut(N, ac)
        counts[N] = len(ws)
        table[N] = int(longest_white(images(ws)).max()) if ws else 0
        print('cut-avoiding N=%3d: %7d lifts, longest white run %2d (log2 W = %.1f)' % (
            N, len(ws), table[N], np.log2(max(1, len(ws)))), flush=True)
    grow = table[150] - table[60] >= 3 and counts[150] > counts[120] > counts[90]
    print('M5 cut-avoiding lifts: run grows by >= 3 and the count grows:', 'HELD' if grow else 'REFUTED')


def m6():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import rule30_relaxed_records_k as rlk
    ws = lifts(150)
    runs = longest_white(images(ws))
    order = np.argsort(-runs, kind='stable')[:200]
    real = []
    for i in order:
        vis = ws[i][0::2]
        ok = bool(rlk.in_language_phase(vis, 0))
        real.append((int(runs[i]), ok))
    nreal = sum(1 for r, ok in real if ok)
    best_real = max([r for r, ok in real if ok], default=0)
    print('top-200 runs %d .. %d; real visible words: %d of 200; longest real run %d; run-%d lifts real: %d of %d' % (
        real[0][0], real[-1][0], nreal, best_real, real[0][0], sum(1 for r, ok in real if ok and r == real[0][0]),
        sum(1 for r, ok in real if r == real[0][0])))
    print('M6 fewer than half real and longest real run below 19:', 'HELD' if nreal < 100 and best_real < 19 else 'REFUTED')


def m78():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import rule30_relaxed_records_k as rlk
    vis = {S: '100', L: '10000'}
    calls = [0]
    cache = {}

    def real(v):
        if v not in cache:
            calls[0] += 1
            cache[v] = bool(rlk.in_language_phase(v, 0))
        return cache[v]
    res = {}
    for N in (60, 90, 120, 150):
        out, stack = set(), [('', '')]
        while stack and calls[0] < 20000:
            w, v = stack.pop()
            if len(w) >= N:
                out.add(w[:N])
                continue
            for b in (S, L):
                v2 = v + vis[b]
                if real(v2):
                    stack.append((w + b, v2))
        ws = sorted(out)
        run = int(longest_white(images(ws)).max()) if ws else 0
        sw = max((sum(1 for i in range(1, len(x)) if x[i] != x[i - 1]) for x in
                  [[c for c in w.replace(L, 'L').replace(S, 'S') if c in 'SL'] for w in ws]), default=0)
        res[N] = (len(ws), run)
        print('real S/L lifts N=%3d: %6d lifts, longest white run %2d, membership calls so far %d%s' % (
            N, len(ws), run, calls[0], ' (CAP)' if calls[0] >= 20000 else ''), flush=True)
    print('M7 count grows at most 4x from N=90 to 150:', 'HELD' if res[150][0] <= 4 * res[90][0] else 'REFUTED')
    print('M8 longest real run at N=150 <= 8:', 'HELD' if res[150][1] <= 8 else 'REFUTED')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'm78':
        m78()
    elif len(sys.argv) > 1 and sys.argv[1] == 'm6':
        m6()
    elif len(sys.argv) > 1 and sys.argv[1] == 'm5':
        m5()
    else:
        main()
