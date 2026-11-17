#!/usr/bin/env python3
"""One fixed GC2244 pilot; execute only under the committed run_capped freeze.

All P-bit drivers at P=2,4,6. Construct by the binary-track lift, then compare
to independent literal-table exhaustive partner/initial-colour existence.
No subprocesses, threads, network, random inputs or automatic extension.
"""
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import time


PERIODS = (2, 4, 6)
RULE30 = (0, 1, 1, 1, 1, 0, 0, 0)


def heights(b):
    h = [0]
    for t, bit in enumerate(b):
        h.append(h[-1] + (1 if t % 2 == 0 else -1) * (1 - bit))
    return h


def criterion(b):
    h = heights(b)
    return h[-1] == 0 and max(h) - min(h) <= 2


def construct(b, exchange=True):
    h = heights(b)
    if h[-1] != 0 or max(h) - min(h) > 2:
        return None
    if min(h) >= 0:
        e, a = 1, 0
        category = "zero" if max(h) == 0 else "nonnegative"
    elif max(h) <= 0:
        e, a, category = -1, 0, "nonpositive"
    else:
        e, a, category = 1, 1, "mixed"
    total = [e * v + a for v in h]
    tracks = [0, a]
    z, w = [0], [a]
    outward = None
    exchanged = False
    for t in range(len(b)):
        move = total[t + 1] - total[t]
        if move:
            if a == 1 and total[t] != 1:
                # First return exchanges labels; later returns preserve them.
                assert outward is not None
                which = 1 - outward if exchange and not exchanged else outward
                exchanged = True
                outward = None
            else:
                which = next(i for i, v in enumerate(tracks) if 0 <= v + move <= 1)
                if a == 1:
                    outward = which
            tracks[which] += move
        assert all(v in (0, 1) for v in tracks)
        assert sum(tracks) == total[t + 1]
        z.append(tracks[0])
        w.append(tracks[1])
    selected = [abs(z[t + 1] - z[t]) for t in range(len(b))]
    first = [1 - selected[t] if bit == 0 else 0 for t, bit in enumerate(b)]
    return {"e": e, "a": a, "category": category, "height": h,
            "z": z, "w": w, "selected": selected,
            "partner": first + [1 - v for v in first],
            "initial": 1 if e == 1 else 0}


def literal_oracle(b, c, initial):
    """No height/track use: enumerate augmented phase/colour states to a cycle."""
    phase, colour = 0, initial
    seen, trace = set(), []
    while (phase, colour) not in seen:
        seen.add((phase, colour))
        trace.append(colour)
        following = RULE30[4 * colour + 2 * b[phase % len(b)] + c[phase]]
        if colour == 0 and following == 0:
            return {"safe": False, "bad_tick": len(trace) - 1,
                    "steps": len(trace), "trace": trace}
        phase = (phase + 1) % len(c)
        colour = following
        assert len(trace) <= 2 * len(c)
    return {"safe": True, "steps": len(trace), "trace": trace,
            "return_phase": phase, "return_colour": colour}


def verify_constructed(b, made):
    p = len(b)
    assert made["z"][0] == 0 and made["w"][0] == made["a"]
    assert made["z"][-1] == made["a"] and made["w"][-1] == 0
    c = made["partner"]
    assert all(c[t + p] == 1 - c[t] for t in range(p))
    event = [int(b[t % p] == 0 and c[t] == 0) for t in range(2 * p)]
    assert all(event[t] + event[t + p] == 1 - b[t] for t in range(p))
    k = made["z"] + made["w"][1:]
    signed = 0
    for t in range(2 * p):
        signed += (1 if t % 2 == 0 else -1) * event[t]
        assert signed == made["e"] * k[t + 1]
    check = literal_oracle(b, c, made["initial"])
    assert check["safe"] and check["steps"] == 2 * p
    assert check["return_colour"] == made["initial"] and check["return_phase"] == 0
    return check


def main():
    start = time.monotonic()
    out = Path(os.environ["CAPPED_OUT"])
    assert resource.getrlimit(resource.RLIMIT_CPU) == (60, 60)
    assert resource.getrlimit(resource.RLIMIT_FSIZE) == (16 << 20, 16 << 20)
    (out / "inputs.json").write_text(json.dumps({
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "periods": PERIODS, "drivers_expected": 84,
        "partner_initial_cases_expected": 8736,
        "cpu_limits": resource.getrlimit(resource.RLIMIT_CPU),
        "file_limits": resource.getrlimit(resource.RLIMIT_FSIZE),
        "subprocesses": 0, "threads": 1}, indent=2) + "\n")
    rows = []
    counts = []
    cases, oracle_steps = 0, 0
    categories = set()
    for p in PERIODS:
        accepted = 0
        for bits in itertools.product((0, 1), repeat=p):
            b = list(bits)
            exists = False
            successes = 0
            first_witness = None
            for prefix in itertools.product((0, 1), repeat=p):
                c = list(prefix) + [1 - v for v in prefix]
                for initial in (0, 1):
                    check = literal_oracle(b, c, initial)
                    cases += 1
                    oracle_steps += check["steps"]
                    if check["safe"]:
                        exists = True
                        successes += 1
                        if first_witness is None:
                            first_witness = {"partner": c, "initial": initial}
            prediction = criterion(b)
            made = construct(b)
            assert prediction == exists == (made is not None), (p, b, prediction, exists)
            if made is not None:
                accepted += 1
                categories.add(made["category"])
                made["checked_trace"] = verify_constructed(b, made)["trace"]
            rows.append({"period": p, "driver": b, "height": heights(b),
                         "criterion": prediction, "oracle_exists": exists,
                         "oracle_safe_initial_cases": successes,
                         "oracle_first_witness": first_witness, "construction": made})
        counts.append({"period": p, "drivers": 2**p, "accepted": accepted})
    assert len(rows) == 84 and cases == 8736
    assert categories == {"zero", "nonnegative", "nonpositive", "mixed"}
    # The written P6 sharpness and prescribed-partner controls.
    b = [int(v) for v in "010010"]
    good = literal_oracle(b, [int(v) for v in "001001110110"], 1)
    assert good["safe"] and good["trace"] == [int(v) for v in "110110101101"]
    bad = [literal_oracle(b, [int(v) for v in "000000111111"], i) for i in (0, 1)]
    assert [v["bad_tick"] for v in bad] == [0, 2]
    # A deliberate endpoint-exchange mutant must fail on the mixed-sign case.
    mixed = [int(v) for v in "100100"]
    mutant = construct(mixed, exchange=False)
    assert mutant["z"][-1] != mutant["a"] and mutant["w"][-1] != 0
    mutant_checks = [literal_oracle(mixed, mutant["partner"], i) for i in (0, 1)]
    assert not any(v["safe"] for v in mutant_checks)
    controls = {"sharpness": good, "prescribed_bad_partner": bad,
                "omitted_exchange_mutant": mutant, "mutant_checks": mutant_checks}
    (out / "driver-results.json").write_text(json.dumps(rows, indent=2) + "\n")
    (out / "controls.json").write_text(json.dumps(controls, indent=2) + "\n")
    usage = resource.getrusage(resource.RUSAGE_SELF)
    result = {"status": "PASS_FIXED_FREE_PARTNER_PILOT", "drivers": len(rows),
              "partner_initial_cases": cases, "oracle_update_steps": oracle_steps,
              "counts": counts, "categories": sorted(categories),
              "controls": "three passed, including deliberate omitted-exchange mutant",
              "wall_s": time.monotonic() - start,
              "cpu_s": usage.ru_utime + usage.ru_stime,
              "universal_proof": "separate solo PROOF-SKETCH, independent read pending"}
    (out / "result.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
