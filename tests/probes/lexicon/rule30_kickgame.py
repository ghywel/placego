#!/usr/bin/env python3
"""rule30_kickgame.py: the kick game. Can a wheel kicked only at its arrival phases hold the left half at zero?

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_kickgame.py
COST:       several minutes on one core.

Background (RULE30-PRIZE.md sections 8.8, 8.12 to 8.14, 8.43). After the wheel forms, a finite configuration's
column 1 next to column 0 = 0101... is the wheel U, an exact coding of the rotation by 17/56, at one of its 28 even
phases. It is kicked by domain walls that arrive only at three phases of the wheel's 56-step cycle (classes 32, 52,
and rarely 42). Each kick moves the angle by whole notches of 1/28 turn: class 32 by +2 .. +6, class 42 by +1 .. +3,
class 52 by -1 .. -6. Column 1 departs from the old phase at the arrival and follows the new one from then on.
section 8.43 found the kicks' sizes come from the interior, which the adversary of this game may choose freely.
The ladder of section 8.12 gave its adversary any input to a layer of width m, and the runs still grew with depth
(section 8.14; at m = 12: 8, 11, 10, 13, 16, 14, 16, 16, 20 at depths 41, 49, .., 105; real right halves up to 12
cells: 6, 9, 10, 10, 8, 8, 9, 9, 10). The kick game is narrower. Column 1 is a kicked wheel from time 0 (the
wheel's formation is left out), and a kick may come only at an arrival phase, by a size from its class's alphabet,
and only if column 1 departs from the old phase at that moment. R_K(s) is the longest zero run of the forced left
half from depth s over every starting phase and every schedule of kicks. G_K(s) is the number of distinct visible
column-1 words before depth s.

PREDICTIONS, written 2026-10-05 before this script's first run (depths s = 41, 49, .., 105):
  KG0 (control, must hold): with kicks disabled the game is the pure wheel. Its run from each depth, for each of the
      28 phases, equals the run computed independently, cell by cell, by the left-parent rule.
  KG1 (blind; the wheel's rigidity): the kick game is no easier for the adversary than the ladder's width-12 layer:
      R_K(s) <= R(12, s) at every depth listed.
  KG2 (blind; the coin law): R_K(s) / log2 G_K(s) lies between 0.75 and 1.35 at every depth listed, as for the
      ladder (BL1).
  KG3 (random-chaos: does the timing matter?): with kicks allowed at every even time (sizes +-1 .. +-6, still
      departing), the run from depth 41 is at least 3 longer than the kick game's. (Depth 41, because with that much
      freedom the search approaches a free column 1 and its states grow like the forced walks' own.)
REFUTED-BY: KG0 failing (the instrument); KG1 to KG3 failing.

OUTCOME, 2026-10-05 (the first run, several minutes):
  KG0 PASSED: with kicks disabled every phase's run equals the cell-by-cell computation (longest run 8).
  Kick game, s = 41, 49, .., 105: R_K = 8, 9, 12, 13, 15, 23, 16, 18, 21; log2 G_K = 8.7, 10.2, 11.6, 13.1, 14.5, 15.9,
  17.4, 18.8, 20.2 (about 0.18 bits per step).
  KG1 REFUTED: the kick game is no harder for the adversary than the width-12 ladder. It beats it at 57 (12 against
     10), 81 (23 against 14), 97 (18 against 16) and 105 (21 against 20). So a width-12 layer cannot produce every
     schedule the game allows.
  KG2 REFUTED at depth 81 alone (ratio 1.44); at the other eight depths R_K / log2 G_K is 0.88 to 1.04. The coin law
     holds: the run is about log2 of the number of distinct column-1 histories.
  KG3 HELD: kicks allowed at every even time give a run of 23 from depth 41, against the game's 8. The arrival
     phases are a real constraint, worth about two thirds of the run at that depth, but the game's runs still grow
     with depth.
"""
import math, sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_wheel_left as wl                         # noqa: E402
sys.argv = _argv
U = [int(c) for c in wl.U]
P = 56
DEPTHS = list(range(41, 106, 8))
LADDER12 = dict(zip(DEPTHS, [8, 11, 10, 13, 16, 14, 16, 16, 20]))
ALPHA = {32: (2, 3, 4, 5, 6), 42: (1, 2, 3), 52: (-1, -2, -3, -4, -5, -6)}
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def diag(P_, Q, c, k):
    X = (P_ << 1) | (Q << 2) | (c << 1)
    X = (X & ~1) | (k & 1)
    s = 1
    while s <= k:
        X ^= X << s
        s <<= 1
    return X & ((2 << k) - 1)


def canon(P_, Q):
    return P_, Q & ~(P_ >> 1)


def new_phase(d, s):
    """The phase after a kick of s notches (an angle change of -17 delta / 56 turns; 33 = 17^-1 mod 56)."""
    return (d - 2 * s * 33) % P


def kicks(d, t, mode):
    """The phases column 1 may follow from time t: the old one, and each allowed kick that departs at t."""
    out = [d]
    if mode == "none":
        return out
    if mode == "game":
        a = (t - d) % P
        sizes = ALPHA.get(a, ())
    else:                                              # "any": every even time, any size from -6 to 6
        sizes = [s for s in range(-6, 7) if s] if t % 2 == 0 else ()
    for s in sizes:
        d2 = new_phase(d, s)
        if U[(t - d2) % P] != U[(t - d) % P]:
            out.append(d2)
    return out


def game(mode, depths, cap=200, count_words=True):
    """R_K(s) for each s in depths, and G_K(s): a merged search over (left state, wheel phase)."""
    front = {(canon(0, 0), d) for d in range(0, P, 2)}
    words = {(d, 1) for d in range(0, P, 2)} if count_words else set()   # visible words, as ints with a leading 1
    R, G = {}, {}
    k = 1
    while k <= max(depths):
        if k in depths:
            G[k] = len({w for _, w in words}) if count_words else None
            cur, run = set(front), 0
            kk = k
            while cur and run < cap:
                nxt = set()
                for ((P_, Q), d) in cur:
                    for d2 in kicks(d, kk - 1, mode):
                        c = U[(kk - 1 - d2) % P] if (kk - 1) % 2 == 0 else 0
                        A = diag(P_, Q, c, kk)
                        if not (A >> kk) & 1:
                            nxt.add((canon(A, P_), d2))
                if not nxt:
                    break
                cur, run, kk = nxt, run + 1, kk + 1
            R[k] = run
        t = k - 1
        nf = set()
        for ((P_, Q), d) in front:
            for d2 in kicks(d, t, mode):
                c = U[(t - d2) % P] if t % 2 == 0 else 0
                nf.add((canon(diag(P_, Q, c, k), P_), d2))
        front = nf
        nw = set()
        for d, w in words:
            for d2 in kicks(d, t, mode):
                nw.add((d2, (w << 1) | U[(t - d2) % P] if t % 2 == 0 else w))
        words = nw
        k += 1
    return R, G


def left_row0(col1, K):
    """Independent: row 0 of the forced left half, cell by cell, from column 0 = t mod 2 and column 1 (a list)."""
    T = K + 2
    right = [t % 2 for t in range(T + 1)]
    far = [col1[t] if t % 2 == 0 else 0 for t in range(T + 1)]
    row = []
    for _ in range(K):
        col = [right[t + 1] ^ (right[t] | far[t]) for t in range(len(right) - 1)]
        row.append(col[0])
        far, right = right, col
    return row


def main():
    ok0, worst = True, 0
    for d0 in range(0, P, 2):
        col1 = [U[(t - d0) % P] for t in range(400)]
        row = left_row0(col1, 330)
        front = {(canon(0, 0), d0)}
        k = 1
        while k <= max(DEPTHS):
            if k in DEPTHS:
                cur, run, kk = set(front), 0, k
                while cur:
                    nxt = set()
                    for ((P_, Q), d) in cur:
                        c = U[(kk - 1 - d) % P] if (kk - 1) % 2 == 0 else 0
                        A = diag(P_, Q, c, kk)
                        if not (A >> kk) & 1:
                            nxt.add((canon(A, P_), d))
                    if not nxt:
                        break
                    cur, run, kk = nxt, run + 1, kk + 1
                indep = next(j for j in range(330 - k) if row[k - 1 + j])
                ok0 &= run == indep
                worst = max(worst, run)
            t = k - 1
            front = {(canon(diag(P_, Q, U[(t - d) % P] if t % 2 == 0 else 0, k), P_), d) for ((P_, Q), d) in front}
            k += 1
    report("KG0 with kicks disabled, every phase's run equals the cell-by-cell computation", ok0,
           f"longest pure-wheel run from these depths: {worst}")
    R, G = game("game", DEPTHS)
    print("   kick game: R_K(s) " + ", ".join(f"{s}: {R[s]}" for s in DEPTHS), flush=True)
    print("              log2 G_K(s) " + ", ".join(f"{s}: {math.log2(G[s]):.1f}" for s in DEPTHS), flush=True)
    print("   ladder, width 12: " + ", ".join(f"{s}: {LADDER12[s]}" for s in DEPTHS), flush=True)
    verdict("KG1 R_K(s) <= R(12, s) at every depth", all(R[s] <= LADDER12[s] for s in DEPTHS),
            ", ".join(f"{s}: {R[s]} vs {LADDER12[s]}" for s in DEPTHS if R[s] > LADDER12[s]) or "all within")
    ratio = {s: R[s] / math.log2(G[s]) for s in DEPTHS}
    verdict("KG2 R_K / log2 G_K between 0.75 and 1.35", all(0.75 <= r <= 1.35 for r in ratio.values()),
            ", ".join(f"{s}: {r:.2f}" for s, r in ratio.items()))
    Ra, _ = game("any", [41], count_words=False)
    verdict("KG3 kicks at any even time make the run from 41 at least 3 longer", Ra[41] >= R[41] + 3,
            f"{Ra[41]} against {R[41]}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
