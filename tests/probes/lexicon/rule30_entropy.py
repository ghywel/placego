#!/usr/bin/env python3
"""rule30_entropy.py: exact upper bounds on how much information column 1 can carry next to a periodic column 0.

RUN-ON:     cpu (C99 via cc, driven from Python 3 with the standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_entropy.py
COST:       a few minutes on one core (the widest layer dominates).

entropy.c builds the deterministic automaton of a width-m layer's visible language (ladder.c's model: cells 1..m, any
input in column m + 1, column 0 clamped to a periodic word) and finds its growth rate by power iteration. Every real
right half, finite or infinite, makes a column 1 inside every layer's language, so log2(lambda_m) / k (k = visible
bits per period) bounds the entropy of column 1 per visible bit, for every m. Wider layers can only lower it.

PREDICTIONS, written 2026-10-05 before this script's first run. Seen before writing: for 01, the values for m = 1 to
14 (0.694 down to 0.244 bits per visible bit) and the free-column counterfactual at m = 6 (exactly 1 bit).
  EN0 (controls): m = 1 gives the golden ratio (Lemma 3's Fibonacci count); lambda_m matches the ladder's measured
      growth of start groups (rule30_ladder_deep.py: 3.40, 2.68, 2.40 per 8 depths at m = 6, 8, 10) within 0.5%;
      lambda never rises with m (a theorem: a wider layer is a narrower one with a constrained input); the free
      column gives exactly 1 bit; and the constant trace 0 gives 0 bits (column 1 can switch on only once; its words
      grow only linearly, so power iteration reaches 0 slowly: below 0.01 counts).
  EN1 (blind): for 01 the bound keeps falling beyond m = 14 but stays clear of zero: at m = 18 it lies between 0.15
      and 0.235 bits per visible bit.
  EN2 (blind; the census, with the random-chaos step): among the traces 001, 011, 0001, 0011, 0111 and six seeded
      random primitive words of length 5 or 6, the trace 01 has the lowest bound at m = 10. The wheel, which only 01
      turns (section 8.8), is the most order a column 0 can impose.
  EN3 (blind): every trace except the constant 0 has a bound above 0.1 bits per visible bit at m = 10.
REFUTED-BY: EN0 failing (the instrument); EN1, EN2 or EN3 failing.

OUTCOME of the first run, 2026-10-05: EN0 passed (lambda_1 = golden ratio to 9 digits; the ladder's ratios matched
within 0.05%; monotone; free column 1.000000 bit; trace 0 0.00036, the slow linear count). Bits per visible bit for
01, m = 1 .. 18: 0.694, 0.694, 0.694, 0.617, 0.509, 0.442, 0.377, 0.356, 0.322, 0.316, 0.285, 0.258, 0.255, 0.244,
0.230, 0.212, 0.195, 0.185 (automaton states 2 to 5,901).
  EN1 HELD: 0.1846 at m = 18 (0.092 bits per step).
  EN2 REFUTED: at m = 10, 01 gives 0.316, but 0001 gives 0.159, 001 0.190, 11000 0.211, 10000 and 00010 0.230,
      001011 0.248 and 0011 0.260 bits per visible bit. Per step the traces range from 0.092 (110111) to 0.184
      (10000); 01 gives 0.158. The wheel does not make column 1 unusually poor.
  EN3 HELD: every trace above 0.1 bits per visible bit (the lowest, 0001, at 0.159).

EXTENSION, written 2026-10-05 after the first run and before running it (python3 rule30_entropy.py deep):
  EN4 (blind): for 01 the bound keeps falling at m = 19 and 20, by less than 0.02 per cell, and at m = 20 lies between
      0.15 and 0.18 bits per visible bit.
"""
import math, pathlib, random, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def primitive(w):
    n = len(w)
    return all(w != w[k:] + w[:k] for k in range(1, n) if n % k == 0) and "0" in w and "1" in w


def main():
    exe = pathlib.Path(tempfile.mkdtemp()) / "entropy"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "entropy.c"), "-lm"], check=True)

    def H(m, word="01", free=False, it=4000):
        args = [str(exe), str(m), str(it), word] + (["free"] if free else [])
        out = subprocess.run(args, capture_output=True, text=True, timeout=7200).stdout
        e = re.search(r"^E \d+ (\S+) \S+ \S+ (\d+)$", out, re.M)
        lam, k = float(e.group(1)), int(e.group(2))
        states = int(re.search(r"^S \d+ (\d+)$", out, re.M).group(1))
        return lam, k, (math.log2(lam) / k if lam > 0 else 0.0), states

    lam = {}
    for m in range(1, 19):
        l, k, h, st = H(m)
        lam[m] = l
        print(f"   trace 01, m {m:2d}: {st:6d} automaton states, lambda {l:.9f}, {h:.4f} bits per visible bit", flush=True)
    phi = (1 + 5 ** 0.5) / 2
    ladder = {6: 3.40 ** 0.25, 8: 2.68 ** 0.25, 10: 2.40 ** 0.25}
    mono = all(lam[m + 1] <= lam[m] + 1e-9 for m in range(1, 18))
    lf, _, hf, _ = H(6, free=True)
    l0, _, h0, _ = H(6, word="0")
    ok0 = abs(lam[1] - phi) < 1e-8 and all(abs(lam[m] / v - 1) <= 0.005 for m, v in ladder.items()) and mono \
        and abs(hf - 1) < 1e-9 and h0 < 0.01
    report("EN0 golden ratio at m = 1, agreement with the ladder, monotone in m, free column 1 bit, trace 0 0 bits", ok0,
           f"lambda_1 {lam[1]:.9f}; ladder ratios " + ", ".join(f"m {m}: {lam[m] / v:.4f}" for m, v in ladder.items())
           + f"; monotone {mono}; free {hf:.6f}; trace 0 {h0:.6f}")
    h18 = math.log2(lam[18])
    verdict("EN1 at m = 18 the bound for 01 lies between 0.15 and 0.235", 0.15 <= h18 <= 0.235, f"{h18:.4f}")

    rng = random.Random(1990)
    rand = []
    while len(rand) < 6:
        n = rng.choice((5, 6))
        w = "".join(rng.choice("01") for _ in range(n))
        if primitive(w) and w not in rand:
            rand.append(w)
    census = {}
    for w in ["01", "001", "011", "0001", "0011", "0111"] + rand:
        l, k, h, st = H(10, word=w)
        census[w] = h
        print(f"   trace {w:>6}: m 10, {st:6d} states, {h:.4f} bits per visible bit ({k} visible per period of {len(w)}; "
              f"{math.log2(l) / len(w):.4f} bits per step)", flush=True)
    others = {w: h for w, h in census.items() if w != "01"}
    verdict("EN2 01 has the lowest bound at m = 10", all(census["01"] < h for h in others.values()),
            f"01: {census['01']:.4f}; lowest other: {min(others, key=others.get)} {min(others.values()):.4f}")
    verdict("EN3 every trace but constant 0 is above 0.1 bits per visible bit at m = 10",
            all(h > 0.1 for h in census.values()), ", ".join(f"{w}: {h:.3f}" for w, h in census.items()))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


def deep():
    exe = pathlib.Path(tempfile.mkdtemp()) / "entropy"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "entropy.c"), "-lm"], check=True)
    h = {18: math.log2(1.136477331)}
    for m in (19, 20):
        out = subprocess.run([str(exe), str(m), "4000"], capture_output=True, text=True, timeout=7200).stdout
        lam = float(re.search(r"^E \d+ (\S+)", out, re.M).group(1))
        st = int(re.search(r"^S \d+ (\d+)$", out, re.M).group(1))
        h[m] = math.log2(lam)
        print(f"   trace 01, m {m}: {st} automaton states, lambda {lam:.9f}, {h[m]:.4f} bits per visible bit", flush=True)
    falls = all(0 <= h[m - 1] - h[m] < 0.02 for m in (19, 20))
    verdict("EN4 still falling at m = 19, 20 by less than 0.02 per cell, and 0.15 to 0.18 at m = 20",
            falls and 0.15 <= h[20] <= 0.18, ", ".join(f"m {m}: {v:.4f}" for m, v in sorted(h.items())))


if __name__ == "__main__":
    deep() if sys.argv[1:] == ["deep"] else main()
