#!/usr/bin/env python3
"""sc7_just_chord.py: spark SC7 (SPARKS.md). Why a just chord rings.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/sparks/sc7_just_chord.py
COST:       instant.

Three voices on C4 = 261.63 Hz, each with harmonics 1 to 16 at amplitude 1/k; spectral lines below 4 kHz, partials
within 0.01 Hz merged into one line (amplitudes added). Just tuning puts E and G at 5/4 and 3/2 of the root; equal
temperament at 2^(4/12) and 2^(7/12).
Predictions (published in SPARKS.md before this ran): the just chord has at least 25 per cent fewer distinct lines;
every just partial is a whole multiple of root/4 = 65.41 Hz; the equal-tempered chord has at least three
near-coincident pairs among harmonics 1 to 8 beating between 1 and 15 Hz.
Control: a single voice has 15 lines below 4 kHz (harmonics 1 to 15 of 261.63 Hz), in either tuning.
"""
ROOT, TOP, MERGE = 261.63, 4000.0, 0.01


def lines(ratios, harmonics=16):
    parts = sorted((ROOT * r * k, 1.0 / k, (i, k)) for i, r in enumerate(ratios) for k in range(1, harmonics + 1)
                   if ROOT * r * k < TOP)
    merged = []
    for f, a, tag in parts:
        if merged and f - merged[-1][0] < MERGE:
            merged[-1][1] += a
            merged[-1][2].append(tag)
        else:
            merged.append([f, a, [tag]])
    return parts, merged


def main():
    assert len(lines([1.0])[1]) == 15
    just = [1.0, 5 / 4, 3 / 2]
    equal = [1.0, 2 ** (4 / 12), 2 ** (7 / 12)]
    pj, mj = lines(just)
    pe, me = lines(equal)
    fewer = 1 - len(mj) / len(me)
    print(f"partials below 4 kHz: {len(pj)} in each tuning")
    print(f"distinct lines: just {len(mj)}, equal {len(me)}  ({fewer:.0%} fewer in just)")
    base = ROOT / 4
    on_grid = all(abs(f / base - round(f / base)) < 1e-9 for f, _, _ in pj)
    print(f"every just partial a whole multiple of {base:.2f} Hz: {on_grid}")
    top = sorted(mj, key=lambda x: -x[1])[:5]
    print("strongest just lines: " + ", ".join(f"{f:.1f} Hz ({len(t)} voices, amp {a:.2f})" for f, a, t in top))
    print("near-coincident equal-tempered pairs among harmonics 1 to 8 (different voices, under 20 Hz apart):")
    low = [(f, a, tag) for f, a, tag in pe if tag[1] <= 8]
    beats = []
    for i in range(len(low)):
        for j in range(i + 1, len(low)):
            (f1, a1, t1), (f2, a2, t2) = low[i], low[j]
            if t1[0] != t2[0] and abs(f1 - f2) < 20:
                beats.append((abs(f1 - f2), f1, f2, a1 * a2, t1, t2))
    names = "CEG"
    for d, f1, f2, w, t1, t2 in sorted(beats, key=lambda x: -x[3]):
        print(f"  {names[t1[0]]}{t1[1]} {f1:7.2f} Hz and {names[t2[0]]}{t2[1]} {f2:7.2f} Hz: beat {d:5.2f} Hz,"
              f" weight {w:.3f}")
    n_beat = sum(1 for b in beats if 1 <= b[0] <= 15)
    ok = fewer >= 0.25 and on_grid and n_beat >= 3
    print(f"pairs beating between 1 and 15 Hz: {n_beat}")
    print("PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
