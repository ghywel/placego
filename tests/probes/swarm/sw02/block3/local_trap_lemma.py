#!/usr/bin/env python3
"""local_trap_lemma.py (Local, 9 November 2026): the trap lemma (GC2775, carried CL758) replayed a third time with
Local's own code, the trap's whole gap language, and the data for a kit module.

Usage: python3 local_trap_lemma.py KIT_DIR [--layers OUT]
  KIT_DIR  a checkout of the Rule 30 Prize kit; the trap is read from
           lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean
  OUT      write the exact path-set layers of the word 3353 as Lean `List Nat` definitions

Conventions (the kit's `Rule30Certificates.GateTrap`): a window is columns 1..16 of the right half driven by the
alternating column at an odd time, coded with bit i = column i + 1. From an odd time column 0 is white, then black,
and `step2 w x1 x2` applies the two steps with x1, x2 the two values of column 17. `u R s` is column 1 at time 2s + 1,
the window's bit 0. A gap word g1 g2 ... gk means black cells of `u` at s, s + g1, s + g1 + g2, ..., white between.

PREDICTION, written before the first run (18:40 UTC):
 P1. The 829 codes are closed under all 3,316 double steps (both values of column 17), and the path sets of the
     15-sample word 1 001 001 00001 001 (gap word 3353) inside the trap have sizes 188, 191, 186, 68, 68, 69, 17, 21,
     21, 18, 21, 29, 40, 41, 0, as GC2775 and CL758 report. E = 33535555 and A's opening gap 2 die too.
     Counterfactual: any other size, which would mean a convention mismatch to be found before anything is written.
 P2. The trap's gap language over {3, 5} has 3353 as its shortest forbidden word, together with a few longer minimal
     forbidden words (at most six gaps), and keeps positive entropy: 33 and 55 both recur. Counterfactual: a shorter
     forbidden word (333, 353, 553, ...), in which case the lemma to submit is that one and 3353 is its corollary; or
     a long list of minimal forbidden words, in which case only 3353 goes into Lean and the language is described.
 P3. Non-vacuity: 335 and 3355 have paths in the trap, and the empty right half's u, which is in the trap from step
     146 (the kit's entry_empty), shows 335 within its first 2,000 steps after 146, never 3353.
     Counterfactual: no 335 in u of the empty half, in which case the non-vacuity control is the graph path alone.
 First run (18:40 UTC): P1 HELD to the digit. P2's counterfactual happened: the shortest forbidden gap word is 333;
 the minimal forbidden words up to 14 gaps are 333, 3353, 3533, 3553, 5533, with 17 distinct path sets. P3 HELD.
 P4, written after that run, before the second (18:41 UTC): (a) the trap's gap language equals the shift of finite
     type over {3, 5} with exactly those five forbidden words: a product of the 17-path-set automaton with the
     three-gap-memory automaton of the five words, explored over all reachable pairs, never disagrees; (b) from any
     trap window, column 1 is black within five double steps (a white run of at most 4). Counterfactual: (a) a pair
     where one side accepts and the other does not (a longer minimal forbidden word, or a word allowed by the list
     that the trap kills); (b) a longer white run, in which case the eventual form of the statement needs a longer
     delay after entry.

Record searched: record_find 3353 (GC2724, GC2734, GC2766, GC2775, CL758; SW02-BLOCK3-BRIDGES: X = 25, E = 33535555);
known_find trap with gap (kit 8d8e157c, portal 18:34:47Z, 14 open PRs): the kit's `Rule30GateTrap.gaps_of_entry`
(gaps 3 or 5 only, Bosdure, R30-20261027-230bc7), `Rule30SidewaysLocks.lock5_win_trap` (ours), and
`Rule30PeriodTwoWidth13.lang_GE2` (nine-pair gap language for every right half: its pairs include 33, 35, 53, 55,
so it allows 3353). No source states a gap word forbidden inside the trap.
"""
import re
import sys
from pathlib import Path

KIT = Path(sys.argv[1])
OUT = None
if '--layers' in sys.argv:
    OUT = Path(sys.argv[sys.argv.index('--layers') + 1])
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()


def codes(name):
    m = re.search(r'def ' + name + r' : List Nat := \[(.*?)\]', src, re.S)
    return [int(x) for x in m.group(1).replace('\n', ' ').split(',')]


TRAP = codes('trapCodes')
ENTRY = int(re.search(r'def entryCode : Nat := (\d+)', src).group(1))
assert len(TRAP) == 829 == len(set(TRAP)), len(TRAP)
TS = set(TRAP)
M16 = (1 << 16) - 1


def step(s, c, x):
    """One Rule 30 step of columns 1..16: column 0 is c, column 17 is x."""
    e = s | (x << 16)
    return (((e << 1) | c) ^ (e | (e >> 1))) & M16


def step2(s, x1, x2):
    return step(step(s, 0, x1), 1, x2)


# scalar cross-check of the packed step: cell by cell
def step_scalar(s, c, x):
    col = [c] + [(s >> i) & 1 for i in range(16)] + [x]          # columns 0..17
    new = [col[j - 1] ^ (col[j] | col[j + 1]) for j in range(1, 17)]
    return sum(b << i for i, b in enumerate(new))


print('kit trap: 829 codes, entry', ENTRY, 'in trap', ENTRY in TS)
closed = sum(1 for w in TRAP for x1 in (0, 1) for x2 in (0, 1) if step2(w, x1, x2) in TS)
scal = all(step_scalar(step_scalar(w, 0, a), 1, b) == step2(w, a, b) for w in TRAP for a in (0, 1) for b in (0, 1))
print('P1 closure', closed, 'of', 4 * 829, '; scalar step agrees', scal)

# the empty right half: window at time 293 (row white at time 0, column 0 black at even times)
row = [0] * 400                                                      # columns 1..400
for t in range(293):
    c = 1 if t % 2 == 0 else 0
    col = [c] + row + [0]
    row = [col[j - 1] ^ (col[j] | col[j + 1]) for j in range(1, len(col) - 1)]
w293 = sum(b << i for i, b in enumerate(row[:16]))
print('empty right half: window at 293 =', w293, '(kit entryCode', ENTRY, ')')


def bits_of_gaps(gaps):
    b = [1]
    for g in gaps:
        b += [0] * (g - 1) + [1]
    return b


def layers(word, start=None):
    """Path sets inside the trap: windows after reading each sample of `word` (bit 0 = u)."""
    S = {w for w in (TRAP if start is None else start) if (w & 1) == word[0]}
    out = [S]
    for y in word[1:]:
        S = {v for w in S for a in (0, 1) for b in (0, 1) for v in [step2(w, a, b)] if (v & 1) == y}
        assert S <= TS
        out.append(S)
    return out


W3353 = bits_of_gaps([3, 3, 5, 3])
L = layers(W3353)
print('P1 3353 samples', ''.join(map(str, W3353)), 'layer sizes', [len(x) for x in L])
print('P1 E = 33535555 layer sizes', [len(x) for x in layers(bits_of_gaps([3, 3, 5, 3, 5, 5, 5, 5]))])
print('P1 A opening (gap 2) layer sizes', [len(x) for x in layers(bits_of_gaps([2]))])

# the gap language: path sets on gap words, from every black window of the trap
BLACK = frozenset(w for w in TRAP if w & 1)


def after_gap(S, g):
    for k in range(g):
        y = 1 if k == g - 1 else 0
        S = {v for w in S for a in (0, 1) for b in (0, 1) for v in [step2(w, a, b)] if (v & 1) == y}
    return frozenset(S)


# the only gaps are 3 and 5 (gaps_of_entry): check 1, 2, 4, 6, 7 die from every black window
print('gaps from black windows:', {g: len(after_gap(BLACK, g)) for g in range(1, 8)},
      '(nonzero only for 3 and 5 expected; 6, 7 can be nonzero through an intermediate black: not a gap)')
NMAX = 14
allowed = {(): BLACK}
frontier = [()]
forbidden = []
for n in range(1, NMAX + 1):
    nxt = []
    for w in frontier:
        for g in (3, 5):
            v = w + (g,)
            S = after_gap(allowed[w], g)
            if S:
                allowed[v] = S; nxt.append(v)
            else:
                forbidden.append(v)
    frontier = nxt
minimal = [v for v in forbidden if v[1:] in allowed]
print('P2 allowed gap words by length:', [sum(1 for v in allowed if len(v) == n) for n in range(NMAX + 1)])
print('P2 minimal forbidden gap words up to', NMAX, 'gaps:', [''.join(map(str, v)) for v in minimal])
cnt = [sum(1 for v in allowed if len(v) == n) for n in range(NMAX + 1)]
print('P2 growth ratios', [round(cnt[n + 1] / cnt[n], 4) for n in range(6, NMAX)])
# the language as a graph on reachable window sets is finite: count distinct path sets
print('P2 distinct path sets', len(set(allowed.values())))

for gw in ([3, 3, 5], [3, 3, 5, 5], [3, 5, 3], [5, 3, 5, 3], [3, 3, 3], [5, 5, 5, 5]):
    print('P3 graph path for gap word', ''.join(map(str, gw)), ':', len(layers(bits_of_gaps(gw))[-1]) > 0)

# u of the empty right half from step 146 (time 293), its gap word, to step 146 + 2000
row = [0] * 4400
u = []
for t in range(293 + 2 * 2000 + 1):
    if t >= 293 and (t - 293) % 2 == 0:
        u.append(row[0])
    c = 1 if t % 2 == 0 else 0
    col = [c] + row + [0]
    row = [col[j - 1] ^ (col[j] | col[j + 1]) for j in range(1, len(col) - 1)]
blacks = [i for i, b in enumerate(u) if b]
gaps = [b - a for a, b in zip(blacks, blacks[1:])]
gs = ''.join(map(str, gaps))
print('P3 u(empty) from 146: black at 146', u[0] == 1, '; gaps in', sorted(set(gaps)), '; length', len(gaps))
print('P3 u(empty) gap word starts', gs[:60])
for sub in ('335', '3355', '3353', '553', '5553', '33333', '55555'):
    print('   ', sub, 'occurs at gap index', gs.find(sub))
mf = [''.join(map(str, v)) for v in minimal]
print('P3 u(empty) contains a minimal forbidden word:', any(m in gs for m in mf))

# P4 (a): product of the path-set automaton with the forbidden-word automaton (state: the last three gaps)
F = {(3, 3, 3), (3, 3, 5, 3), (3, 5, 3, 3), (3, 5, 5, 3), (5, 5, 3, 3)}


def sft_ok(hist, g):
    """hist: up to the last three gaps; is hist + g free of every word of F as a suffix?"""
    h = hist + (g,)
    return not any(h[-len(f):] == f for f in F if len(h) >= len(f))


seen = {(BLACK, ())}
todo = [(BLACK, ())]
disagree = []
while todo:
    S, h = todo.pop()
    for g in (3, 5):
        S2 = after_gap(S, g) if S else frozenset()
        ok = sft_ok(h, g)
        if bool(S2) != ok:
            disagree.append((h, g, len(S2), ok))
        if ok and S2:
            st = (S2, (h + (g,))[-3:])
            if st not in seen:
                seen.add(st); todo.append(st)
print('P4a product states', len(seen), '; disagreements', len(disagree), disagree[:5])

# P4 (b): the longest white run of column 1 from any trap window
cur = {w for w in TRAP if not (w & 1)}
run = 0
while cur:
    run += 1
    cur = {v for w in cur for a in (0, 1) for b in (0, 1) for v in [step2(w, a, b)] if not (v & 1)}
print('P4b longest white run from a white trap window:', run, '(windows white at that many consecutive odd times)')

WORDS = {'333': [3, 3, 3], '3353': [3, 3, 5, 3], '3533': [3, 5, 3, 3], '3553': [3, 5, 5, 3], '5533': [5, 5, 3, 3]}
for name, gw in WORDS.items():
    Ls = layers(bits_of_gaps(gw))
    print('   word', name, 'samples', ''.join(map(str, bits_of_gaps(gw))), 'layer sizes', [len(x) for x in Ls])

if OUT is not None:
    lines = []
    for name, gw in WORDS.items():
        Ls = layers(bits_of_gaps(gw))
        assert not Ls[-1]
        rows = []
        for S in Ls:
            codes_k = sorted(S)
            chunks = [', '.join(str(x) for x in codes_k[i:i + 16]) for i in range(0, len(codes_k), 16)]
            rows.append('[' + ',\n    '.join(chunks) + ']')
        sizes = ', '.join(str(len(S)) for S in Ls)
        lines.append(f'/-- The layers of the gap word `{name}`: the windows of the trap after each of its '
                     f'{len(Ls)} samples ({sizes}). -/\n'
                     f'def layers{name} : List (List Nat) := [\n  ' + ',\n  '.join(rows) + ']')
    OUT.write_text('\n\n'.join(lines) + '\n')
    print('wrote', OUT, len(lines), 'words')
