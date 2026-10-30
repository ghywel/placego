#!/usr/bin/env python3
"""GC2273: fixed CL666 witnesses and their designated four-cell ablations.

No seed/width search or adjustable horizon. Literal unbounded-set dynamics and
packed dynamics must agree at every row. Published observations are compared,
not used as oracle assertions. All artifacts go to CAPPED_OUT.
"""
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import time

HORIZON = 24
OFFSET = 64
SITES = (0, 7, 14, 17)
WORDS = ("0010000", "0111000", "1100100", "1011111")
START_CPU = time.process_time()


def budget():
    if time.process_time() - START_CPU > 25:
        raise RuntimeError("cooperative payload CPU guard: 25 seconds")


def literal(row):
    if not row:
        return set()
    return {i for i in range(min(row)-1, max(row)+2)
            if ((i-1 in row) != ((i in row) or (i+1 in row)))}


def evolve(seed):
    row = {i for i in range(seed.bit_length()) if seed >> i & 1}
    packed = seed << OFFSET
    rows = []
    for t in range(HORIZON+1):
        budget()
        decoded = {i-OFFSET for i in range(packed.bit_length()) if packed >> i & 1}
        assert row == decoded, (seed, t, "independent oracle disagreement")
        rows.append(row)
        if t < HORIZON:
            row = literal(row)
            packed = (packed << 1) ^ (packed | (packed >> 1))
    return rows


def window(row, p, radius=3):
    return "".join(str(int(i in row)) for i in range(p-radius, p+radius+1))


def first(values):
    return next((i for i, v in enumerate(values) if v), None)


def describe(seed, p, rows):
    trace = [int(p in row) for row in rows]
    return {"seed": hex(seed), "p": p,
            "black_sites": sorted(rows[0]), "trace": "".join(map(str, trace)),
            "first_clock_mismatch": first(v != (trace[0] ^ (t & 1)) for t, v in enumerate(trace)),
            "windows": [window(row, p) for row in rows],
            "exterior_inputs": [[int(p-4 in row), int(p+4 in row)] for row in rows],
            "rows": [sorted(row) for row in rows]}


def main():
    out = Path(os.environ["CAPPED_OUT"])
    assert HORIZON < OFFSET
    # Rule 30's standard truth table, ordered 111 down to 000.
    truth = "00011110"
    for n in range(8):
        a, b, c = (n >> 2 & 1, n >> 1 & 1, n & 1)
        assert (a ^ (b | c)) == int(truth[7-n])
    assert all(not row for row in evolve(0))
    one = evolve(1)
    assert one[1] == {-1, 0, 1}
    for shift in SITES:
        assert evolve(1 << shift) == [{i+shift for i in row} for row in one]
    assert literal({0, 1}) == {-1, 0, 2}

    supplied = [
        (1, 1, 0, "0010000 0111000 1100100 1011110 0010001 1111011 1000010 1100111".split()),
        (0x3b5b, 9, 3, "0010000 0111000 1100100 1011110 0010000 0111001 1100111 1011100 1010011 1011110 0010001 1111011 0000010 1000111".split()),
        (0x24081, 8, 0, list(WORDS)*3 + "1100101 1011101 1010001 1011011 0010010 1111110 0000000 1000001".split()),
    ]
    witnesses = []
    for seed, p, start, quoted in supplied:
        rows = evolve(seed)
        d = describe(seed, p, rows)
        d["quoted_windows"] = {"start": start, "values": quoted}
        d["quotation_mismatches"] = [
            {"t": start+i, "quoted": w, "actual": d["windows"][start+i]}
            for i, w in enumerate(quoted) if w != d["windows"][start+i]]
        witnesses.append(d)

    full = evolve(0x24081)
    ablations = []
    for mask in range(16):
        seed = sum(1 << p for i, p in enumerate(SITES) if mask >> i & 1)
        rows = evolve(seed)
        d = describe(seed, 8, rows)
        d["subset_mask"] = mask
        d["first_center_difference_from_full"] = first((8 in r) != (8 in f) for r, f in zip(rows, full))
        d["first_window_difference_from_full"] = first(window(r, 8) != window(f, 8) for r, f in zip(rows, full))
        d["difference_windows"] = [window(r ^ f, 8) for r, f in zip(rows, full)]
        d["four_phase_core_prefix"] = first(window(r, 8) != WORDS[t % 4] for t, r in enumerate(rows))
        ablations.append(d)

    # All 16 exterior choices on the specified four local phases.
    guards = []
    for phase, word in enumerate(WORDS):
        for left, right in itertools.product(range(2), repeat=2):
            row = [left] + list(map(int, word)) + [right]
            nxt = "".join(str(row[i-1] ^ (row[i] | row[i+1])) for i in range(1, 8))
            guards.append({"phase": phase, "left": left, "right": right,
                           "next": nxt, "closes": nxt == WORDS[(phase+1) % 4]})
    # Independent shrinking literal evolution of the nine-cell cylinders.
    for g in guards:
        row = [g["left"]] + list(map(int, WORDS[g["phase"]])) + [g["right"]]
        result = literal({i for i, v in enumerate(row) if v})
        assert "".join(str(int(i in result)) for i in range(1, 8)) == g["next"]
    assert {g["next"][1:-1] for g in guards if g["phase"] == 3} == {"01000"}

    singles = [evolve(1 << p) for p in SITES]
    xor_rows = []
    for t in range(HORIZON+1):
        row = set()
        for series in singles:
            row ^= series[t]
        xor_rows.append(row)
    superposition = {"first_row_failure": first(a != b for a, b in zip(xor_rows, full)),
                     "first_center_failure": first((8 in a) != (8 in b) for a, b in zip(xor_rows, full)),
                     "xor_trace": "".join(str(int(8 in r)) for r in xor_rows)}
    payload = {"status": "PASS", "horizon": HORIZON, "witnesses": witnesses,
               "ablations": ablations, "guards": guards, "xor_superposition": superposition,
               "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "payload_cpu_seconds": time.process_time()-START_CPU,
               "payload_maxrss_raw": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               "cpu_guard": "25s cooperative single payload; no child processes or threads created"}
    (out / "audit.json").write_text(json.dumps(payload, indent=2)+"\n")
    print("PASS: independent oracles and local controls")
    for w in witnesses:
        print(w["seed"], "p", w["p"], "L", w["first_clock_mismatch"],
              "quoted mismatches", w["quotation_mismatches"])
    print("subset mask / black sites / L / first center delta / first window delta / four-phase prefix")
    for a in ablations:
        print(a["subset_mask"], a["black_sites"], a["first_clock_mismatch"],
              a["first_center_difference_from_full"], a["first_window_difference_from_full"], a["four_phase_core_prefix"])
    print("closing guards", [(g["phase"], g["left"], g["right"]) for g in guards if g["closes"]])
    print("XOR control", superposition)


if __name__ == "__main__":
    main()
