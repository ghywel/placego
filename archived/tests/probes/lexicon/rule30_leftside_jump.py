#!/usr/bin/env python3
"""rule30_leftside_jump.py: the 13-tick jumps of the left horizon beside 0101 (RULE30-PRIZE.md 8.94, addendum).

H_L(W) jumps by exactly 13 at W = 11 (17 to 30) and at W = 31 (53 to 66). This lists every seed above the previous
width's horizon (leftside_dump.c, same survive() and encoding as the frozen leftside_horizon.c) and tests whether the
W = 31 champions are built from the W = 11 ones, and whether such a build repeats.

RUN-ON:     cpu, 10 threads (OpenMP; ompflags.py)
COMMAND:    python3 tests/probes/lexicon/rule30_leftside_jump.py
COST:       about a minute.

PREDICTIONS (stated in the session before the run, 2026-10-13 12:41 BST; written into this header after it; exploratory).
  J1 blind: at W = 31 fewer than 100 seeds a phase survive past H_L(30) = 53 (the jump is a small family).
  J2 blind: the W = 31 jump family shares its last 8 cells (the cells next to the wall).
  J3 blind: no W = 31 jump seed ends with the W = 11 champion 10111010101 (the jump is not the W = 11 one reused).
  J4 blind, stated after J3's outcome: the 20-cell prefix P20 = 10011100101110100100 that turns the W = 11 champions
     into W = 31 champions repeats: P20 P20 + champion (W = 51) survives at least 95 ticks.

OUTCOME (2026-10-13, M5): J1 HELD, J2 REFUTED, J3 REFUTED, J4 REFUTED.
  W = 11: two seeds above 17, both at 30 (10111010101 and 10111100011, phase 1). W = 31: 27 seeds above 53, the best
  at 66 (phase 1). W = 32: 34 seeds above 53, the best at 65 (phase 0). The W = 31 family has no common ending (J2).
  P20 followed by either W = 11 champion is a W = 31 champion (66 ticks): the W = 31 jump is the W = 11 jump carried
  through a 20-cell prefix that adds 36 ticks (J3 refuted, the finding). The prefix does not repeat: P20 twice or three
  times before a champion (W = 51, 71) survives 34 ticks in either phase (J4).
"""
import pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ompflags import OMP

def survive(seed, phase, T=200):
    """Independent pure-Python simulation of the left half beside the wall 01 (phase 0 white at t = 0)."""
    W = len(seed); x = {-(W - k): int(ch) for k, ch in enumerate(seed)}
    for t in range(T):
        tau = (phase + t) % 2
        if tau and x.get(-1, 0) != 1: return t
        new = {}
        for i in range(1, W + t + 3):
            left = x.get(-(i + 1), 0); me = x.get(-i, 0); right = x.get(-(i - 1), 0) if i > 1 else tau
            new[-i] = left ^ (me | right)
        x = new
    return T

def main():
    exe = pathlib.Path(tempfile.mkdtemp()) / "leftside_dump"
    arch = ["-mcpu=native"] if sys.platform == "darwin" else ["-march=native"]
    subprocess.run(["cc", "-O3", *arch, *OMP, "-o", str(exe), str(HERE / "leftside_dump.c")], check=True)
    def dump(W, th):
        rows = []
        for ph in (0, 1):
            out = subprocess.run([str(exe), "01", str(W), str(ph), str(th), "90", "10"],
                                 capture_output=True, text=True, check=True).stdout
            for line in out.split("\n"):
                if line.startswith("D "):
                    _, w, p, h, s = line.split(); s = int(s, 16)
                    rows.append((int(h), int(p), "".join(str((s >> k) & 1) for k in range(W - 1, -1, -1))))
        return sorted(rows, reverse=True)
    r11, r31, r32 = dump(11, 18), dump(31, 54), dump(32, 54)
    print("W=11 above 17:", r11)
    print(f"W=31 above 53: {len(r31)} seeds, best {r31[0]}")
    print(f"W=32 above 53: {len(r32)} seeds, best {r32[0]}")
    ok = {"J1": max(sum(1 for _, p, _ in r31 if p == ph) for ph in (0, 1)) < 100}
    common = r31[0][2]
    for _, _, s in r31:
        k = 0
        while k < min(len(s), len(common)) and s[-1 - k] == common[-1 - k]: k += 1
        common = common[len(common) - k:] if k else ""
    print(f"J2: longest common ending of the W=31 family: '{common}'")
    ok["J2"] = len(common) >= 8
    champs11 = [s for _, _, s in r11]
    reuse = [s for _, _, s in r31 if any(s.endswith(c) for c in champs11)]
    print("J3: W=31 jump seeds ending with a W=11 champion:", reuse)
    ok["J3"] = not reuse
    P20 = "10011100101110100100"
    j4 = []
    for c in champs11:
        assert survive(c, 1) == 30 and survive(P20 + c, 1) == 66      # independent replay of the two champions
        for k in (2, 3):
            s = P20 * k + c
            j4.append((len(s), max(survive(s, 0), survive(s, 1))))
    print("J4: P20 repeated before a W=11 champion (width, best survival):", j4)
    ok["J4"] = all(h >= 95 for W, h in j4 if W == 51)
    print("\n" + "  ".join(f"{k} {'HELD' if v else 'REFUTED'}" for k, v in ok.items()))

if __name__ == "__main__":
    main()
