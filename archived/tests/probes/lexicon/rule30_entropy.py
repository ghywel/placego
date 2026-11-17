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
OUTCOME of the extension, 2026-10-05: EN4 HELD. m = 19: 8,733 states, 0.1675; m = 20: 12,749 states, 0.1519 bits per
visible bit. Still falling by about 0.016 per cell, with no sign yet of levelling off.

EXTENSION 2, written 2026-10-05 before running it (python3 rule30_entropy.py deep2). entropy2.c stores the subset states
sparsely (they hold 7 to 1,022 layer states on average for m = 4 to 20) and reproduced every lambda and state count of
entropy.c for m = 4, 6, 10, 14, 18, 20 exactly, before this prediction was written.
  EN5 (blind; does the bound level off?): from m = 20 to m = 26 the bound falls by less per cell, on average, than the
      0.0154 per cell from m = 14 to m = 20, and at m = 26 it lies between 0.07 and 0.14 bits per visible bit. (The
      kick estimate says the true value is near 0.05 to 0.15.)
OUTCOME of extension 2, 2026-10-05: EN5 HELD. m = 21 .. 26: 0.1416, 0.1372, 0.1356, 0.1327, 0.1308, 0.1277 bits per
visible bit (automaton states 18,926 to 179,181; mean subset 1,374 to 7,862 layer states). The mean fall per cell from
m = 20 to 26 is 0.0040, a quarter of the 0.0154 before: the bound is levelling off, near 0.12.

---------------------------------------------------------------------------------------------------------------
JOB M3a (Cloud wrote, 2026-10-05; for Local, optional; CLOUD-LOCAL.md lead M3). The channel bound at m = 27 and 28,
which need more memory than Cloud's container (about 16 GB at m = 27 and 32 GB at m = 28; one core, minutes).
RUN-ON:     cpu, the machine with the most memory
COMMAND:    cc -O2 -o /tmp/entropy2 tests/probes/lexicon/entropy2.c -lm && /tmp/entropy2 27 4000 && /tmp/entropy2 28 4000
PREDICTION (written 2026-10-05 before any run of this job):
  EN6 (blind): log2(lambda) at m = 27 and 28 lies between 0.115 and 0.128, each no higher than the one before.
REFUTED-BY: either value outside that range, or a rise.
ADDENDUM to JOB M3a (Local, 2026-10-06, after the owner asked whether the blocked job could be made to fit a 16 GB
machine). The memory is the pool of sorted sets (about 1.4 billion layer states, 5.6 GB, at m = 26, growing 2.2 times
per cell). entropy2.c now has a compile-time variant, -DPOOL_MMAP, that keeps that pool in a file mapped on the
internal NVMe: append-only, every byte written once, read in order by the BFS and one set at a time by the hash
lookups. Nothing else changes. The variant reproduced the heap build to the digit at m = 10, 14, 18 (states, mean
population, lambda) before these predictions were written.
  COMMAND:  cc -O2 -DPOOL_MMAP -o /tmp/entropy2m tests/probes/lexicon/entropy2.c -lm
            POOL_FILE=<a file on the internal drive> POOL_GB=48 /tmp/entropy2m 27 4000   (then 28)
  MM0 (control, must hold): at m = 24 the variant's S and E lines equal the heap build's exactly.
  MM1 (blind; the point of the variant): the peak resident memory of the variant at m = 28 stays below 14 GB, so
      the run completes on this 16 GB machine without swapping.
  MM2 (blind; sizes): the automaton has between 250,000 and 320,000 states at m = 27 and between 380,000 and 500,000
      at m = 28, with mean subsets of 10,000 to 13,000 and 14,000 to 19,000 layer states (the growth of 1.57 and
      1.42 per cell seen from m = 21 to 26).
  MM3 (blind; cost): each width finishes within 3 hours of wall time on one core, and the pool file is written once:
      its size is within 30% of 12 GB at m = 27 and 28 GB at m = 28, and the drive's total writes during the run
      are below twice that.
  EN6 stands as written above (blind: both values in [0.115, 0.128], each no higher than the one before).
REFUTED-BY: MM0 failing (the variant); MM1 failing means the job stays blocked here; MM2, MM3 the other way.
OUTCOME of JOB M3a, 2026-10-06 (the mapped variant, one core each, the pool file on the internal drive):
  MM0 PASSED: at m = 24 both builds print S 24 67658 3752.6 and E 24 1.096369219 (12 s each, 1.19 GB; the 8 GB sparse
  file held 1.0 GB).
  m = 27: S 27 289484 11598.2, E 27 1.088881193 (0.1229 bits per visible bit); 208 s; peak resident 5.76 GB; pool 13 GB.
  m = 28: S 28 448144 16849.8, E 28 1.088373390 (0.1222 bits per visible bit); 459 s; peak resident 6.03 GB; pool 29 GB.
  EN6 HELD (0.1229 and 0.1222, each lower than the last; the fall per cell 0.0048 then 0.0007: the bound is
  levelling off near 0.122). MM1 HELD (6 GB peak, swap unchanged at 0.15 GB: the kernel dropped the clean mapped pages
  instead of swapping). MM2 HELD (289,484 and 448,144 states; mean subsets 11,598 and 16,850). MM3 HELD in its cost
  and size clauses (minutes, not hours; 13 and 29 GB); its write clause could not be decided as written: iostat
  reports reads and writes together (29 GB of traffic during m = 27, 50 GB during m = 28, consistent with each byte
  written once and read about once). JOB M3a is complete; nothing is blocked any more.

HAND BACK to Cloud when both "E" lines are recorded here (or the run fails for memory, with the error), with a ledger
  line ("Local ran M3a"), pushed to main.
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


def deep2():
    exe = pathlib.Path(tempfile.mkdtemp()) / "entropy2"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "entropy2.c"), "-lm"], check=True)
    h = {20: math.log2(1.111005203)}
    for m in range(21, 27):
        out = subprocess.run([str(exe), str(m), "4000"], capture_output=True, text=True, timeout=7200).stdout
        lam = float(re.search(r"^E \d+ (\S+)", out, re.M).group(1))
        st = re.search(r"^S \d+ (\d+) (\S+)$", out, re.M)
        h[m] = math.log2(lam)
        print(f"   trace 01, m {m}: {st.group(1)} automaton states (mean {st.group(2)} layer states each), "
              f"lambda {lam:.9f}, {h[m]:.4f} bits per visible bit", flush=True)
    fall = (h[20] - h[26]) / 6
    verdict("EN5 the fall per cell slows (below 0.0154 on average, m = 20 to 26), and m = 26 lies in 0.07 to 0.14",
            fall < 0.0154 and 0.07 <= h[26] <= 0.14, f"mean fall {fall:.4f} per cell; m = 26: {h[26]:.4f}")


if __name__ == "__main__":
    {"deep": deep, "deep2": deep2}.get(sys.argv[1] if len(sys.argv) > 1 else "", main)()
