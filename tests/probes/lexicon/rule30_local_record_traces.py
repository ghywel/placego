#!/usr/bin/env python3
"""rule30_local_record_traces.py: RT, the record witnesses' trace words for the finite-support record route (CL355).

RUN-ON:     cpu (Python 3 standard library; a few seconds)
COMMAND:    python3 tests/probes/lexicon/rule30_local_record_traces.py check   (anyone: re-verifies the text file)
            python3 tests/probes/lexicon/rule30_local_record_traces.py build   (Local: rebuilds it from the data)

WHAT. For every depth d = 20 .. 160 the best record witness Local holds (SP's sampled witnesses, the deep runs and the
CUT lifts; L = the exact R_real(d) where it is known), written as the objects of CL355's route: the column-1 trace
c_0 .. c_T beside the clamped wall (T = d + L - 1, column 0 = (t + phase) mod 2 for t <= T), its visible word (c at the
white-wall times t < T), and the LEFT row at time 0 at depths 1 .. T, which the trace determines leftward
(x_(i-1)(t) = x_i(t+1) XOR (x_i(t) OR x_(i+1)(t)); T + 1 samples fix depth T, GC1148's step). The band is white at
depths d .. d + L - 1 of that row. Status: 'exact' when L is the exact R_real(d) (20 .. 120 from RR2/RR3; 17 at 132,
139, 142), else '>=' with the certified upper bound where one exists (<= 17 at 121 .. 124, 140, 144).

FILE: rule30_local_record_traces.txt, one block a depth:
  'd=<d> L=<L> phase=<p> T=<T> status=<exact|>=|>=,<=17>'
  'trace=<c_0 .. c_T>'
  'visible=<c at white-wall times t < T>'
  'left=<depths 1 .. T at time 0>'
  'right=<sites 1 .. n at time 0: the witness's right half, so the whole configuration replays>'

CHECKS (`check`, standalone on the file, two methods): (1) the leftward relation from the wall and the trace gives the
stored left row, and its band d .. d + L - 1 is white; (2) the stored configuration (left row, wall cell, right half)
replays in rule30_witness_check.check (band white, clock through T), and a forward simulation of it gives the stored
trace and visible word. `build` also replays every source witness before choosing the best one a depth.

RESULT (L643, 2026-10-11): see the ledger entry; the file's header line carries the counts.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.join(HERE, 'rule30_local_record_traces.txt')
DATA = os.path.expanduser('~/np-scratch-int')
DMIN, DMAX = 20, 160
EXACT17 = {132: 17, 139: 17, 142: 17}
LE17 = {121, 122, 123, 124, 140, 144}


def trace_of(left, right, ph, T):
    """Column 1 at t = 0 .. T from the time-0 row (left = cells -T .. 0, right = sites 1 ..); clock asserted."""
    off = T + 4
    row = [0] * (off + len(right) + T + 4)
    for j, b in enumerate(left):
        row[off - T + j] = int(b)
    for j, b in enumerate(right):
        row[off + 1 + j] = int(b)
    c = []
    for t in range(T + 1):
        assert row[off] == (t + ph) % 2, 'clock'
        c.append(row[off + 1])
        row = [0] + [row[i - 1] ^ (row[i] | row[i + 1]) for i in range(1, len(row) - 1)] + [0]
    return c


def left_image(c, ph):
    """Depths 1 .. T at time 0 from the wall and the trace, by the leftward relation."""
    T = len(c) - 1
    col1, col0 = c, [(t + ph) % 2 for t in range(T + 1)]
    out = []
    for k in range(1, T + 1):
        nxt = [col0[t + 1] ^ (col0[t] | col1[t]) for t in range(T + 1 - k)]
        out.append(nxt[0])
        col1, col0 = col0, nxt
    return out


def blocks(path):
    txt = open(path).read()
    pat = (r'^d=(\d+) L=(\d+) phase=([01]) T=(\d+) status=(\S+)\ntrace=([01]+)\nvisible=([01]*)\nleft=([01]+)\n'
           r'right=([01]+)$')
    for m in re.finditer(pat, txt, re.M):
        yield (int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), m.group(5), m.group(6), m.group(7),
               m.group(8), m.group(9))


def check(path=OUT):
    from rule30_witness_check import check as wcheck
    n = 0
    for d, L, ph, T, status, tr, vis, left, right in blocks(path):
        c = [int(b) for b in tr]
        assert T == d + L - 1 and len(c) == T + 1 and len(left) == T, d
        img = left_image(c, ph)
        assert ''.join(map(str, img)) == left, ('leftward relation', d)
        assert all(img[k - 1] == 0 for k in range(d, d + L)), ('band', d)
        cells = left[::-1] + str(ph % 2)                    # cells -T .. 0, as the checker takes them
        band, clock, v = wcheck(d, L, ph, cells, right, vis)
        assert band and clock and v, ('replay', d)
        assert trace_of(cells, right, ph, T) == c, ('forward trace', d)
        n += 1
    print('RT check: %d blocks; leftward relation, white band, replay and forward trace hold' % n)
    return n


def exact_table():
    from rule30_rreal_sample import exact
    R = exact()
    R.update(EXACT17)
    return R


def sources():
    """(d, L, ph, left, right, source) from SP's witness files and the CUT lifts."""
    for f in sorted(glob.glob(os.path.join(DATA, 'rule30-sample', '*_w[01].txt'))):
        for line in open(f):
            p = line.split()
            if len(p) == 6 and p[0] == 'W':
                yield int(p[1]), int(p[2]), int(p[3]), p[4], p[5], os.path.basename(f)
    for f in sorted(glob.glob(os.path.join(DATA, 'rule30-rlk', 'lift_d*_L*_p*.txt'))):
        t = open(f).read()
        h = dict(z.split('=') for z in t.splitlines()[0].split())
        d, L, ph, T = int(h['d']), int(h['L']), int(h['phase']), int(h['T'])
        left = re.search(r'^left \(cells -?\d+ \.\. 0\)=([01]+)$', t, re.M).group(1)[-(T + 1):]
        right = re.search(r'^right \(sites 1 \.\. \d+\)=([01]+)$', t, re.M).group(1)
        yield d, L, ph, left, right, os.path.basename(f)


def sharp17():
    """Every distinct trace in the data folder that carries 17 at the exact depths 132, 139, 142 (GC1155's request),
    by phase: any witness whose band covers d .. d + 16, cut to T = d + 16 (its column-1 trace through T)."""
    from rule30_witness_check import check as wcheck
    seen = {}
    for d, L, ph, left, right, src in sources():
        for dd in sorted(EXACT17):
            T = dd + 16
            if d <= dd and d + L - 1 >= T:
                cells = left[-(T + 1):]
                band, clock, _ = wcheck(dd, 17, ph, cells, right)
                assert band and clock, ('sharp row fails the checker', dd, src)
                c = ''.join(map(str, trace_of(cells, right, ph, T)))
                seen.setdefault((dd, ph, c), (cells, right, []))[2].append('%s (d=%d L=%d)' % (src, d, L))
    absent = ', '.join('%d phase %d' % (dd, ph) for dd in sorted(EXACT17) for ph in (0, 1)
                       if not any(k[0] == dd and k[1] == ph for k in seen))
    out = ['', '## sharp 17 (GC1155): every distinct column-1 trace in the data carrying 17 at 132, 139, 142;',
           '## absent from the data: %s.' % absent]
    for (dd, ph, c), (cells, right, srcs) in sorted(seen.items()):
        T = dd + 16
        img = left_image([int(b) for b in c], ph)
        out += ['# sources: ' + '; '.join(srcs),
                'd=%d L=17 phase=%d T=%d status=exact' % (dd, ph, T), 'trace=' + c,
                'visible=' + ''.join(c[t] for t in range(T) if (t + ph) % 2 == 0), 'left=' + ''.join(map(str, img)),
                'right=' + (right.rstrip('0') or '0')]
    return out


def build():
    from rule30_witness_check import check as wcheck
    R = exact_table()
    best = {}
    for d, L, ph, left, right, src in sources():
        if not DMIN <= d <= DMAX:
            continue
        if d in best and best[d][0] >= L:
            continue
        band, clock, _ = wcheck(d, L, ph, left, right)
        assert band and clock, ('source witness fails the checker', d, L, src)
        best[d] = (L, ph, left, right, src)
    missing = [d for d in range(DMIN, DMAX + 1) if d not in best]
    lines, nexact, below = [], 0, []
    for d in sorted(best):
        L, ph, left, right, src = best[d]
        T = d + L - 1
        c = trace_of(left, right, ph, T)
        img = left_image(c, ph)
        assert ''.join(map(str, img)) == ''.join(reversed(left[:-1])), ('left image differs from the witness', d)
        if d in R:
            assert L <= R[d], ('witness above the exact value', d, L, R[d])
            status = 'exact' if L == R[d] else '>='
            nexact += L == R[d]
            if L < R[d]:
                below.append((d, L, R[d]))
        else:
            status = '>=,<=17' if d in LE17 else '>='
        tr = ''.join(map(str, c))
        lines += ['d=%d L=%d phase=%d T=%d status=%s' % (d, L, ph, T, status), 'trace=' + tr,
                  'visible=' + ''.join(tr[t] for t in range(T) if (t + ph) % 2 == 0), 'left=' + ''.join(map(str, img)),
                  'right=' + (right.rstrip('0') or '0')]
    head = ['# RT (rule30_local_record_traces.py): the best record witness Local holds at each depth %d .. %d, as its '
            'column-1 trace,' % (DMIN, DMAX),
            '# visible word and forced left row at time 0 (depths 1 .. T). %d depths; %d at the exact R_real(d); '
            'missing: %s.' % (len(best), nexact, ' '.join(map(str, missing)) or 'none'),
            '# Below the exact value (no witness at it in the data folder): %s.' % (
                ', '.join('%d (%d of %d)' % z for z in below) or 'none'),
            '# Phase p: column 0 = (t + p) mod 2 for t <= T. Every block replays (`check`).', '']
    lines += sharp17()
    open(OUT, 'w').write('\n'.join(head + lines) + '\n')
    print('\n'.join(head[:3]))
    check(OUT)


if __name__ == '__main__':
    {'build': build, 'check': check}[sys.argv[1] if len(sys.argv) > 1 else 'check']()
