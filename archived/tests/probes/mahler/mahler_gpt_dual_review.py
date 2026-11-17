#!/usr/bin/env python3
"""Fixed dual-source review for L712, preregistered in CHAT-LEDGER GC1230.1.
Record searched: negative153 and the saved record fixture; G50/G51 and census sources read.
Predict H(-6964446546082240544)=153, emitted as a T124 dual straggler;
H(-1)=2; the dual fixed chunk (10,6,0) has 16 deaths at2.
Counterfactual: wrong sign conversion, integer-bit complementation or chunk mass.
Unexpected control: omitted x=-256 emits no receipt, while x=-1 is included.
No full census or saved-straggler analysis. One temporary C build, four fixed inputs.
Run: python3 tests/probes/mahler/mahler_gpt_dual_review.py

OUTCOME (2026-10-14 11:39 BST): all preregistered fixed controls PASS. Independent
original-fraction horizons153 and2; matching dual C straggler representation,
chunk mass16 at2, and omitted outside-boundary control. No census replay.
"""
from pathlib import Path
import subprocess
import tempfile
from mahler_gpt_review import initial_window_horizon, parse_output


def main():
    negative = -6964446546082240544
    assert initial_window_horizon(negative) == 153
    assert initial_window_horizon(-1) == 2
    with tempfile.TemporaryDirectory(prefix="mahler-dual-review-") as tmp:
        binary = str(Path(tmp) / "walker")
        subprocess.run(["cc", "-O2", "-o", binary,
                        str(Path(__file__).with_name("mahler_census.c"))], check=True)
        def run(w, pb, prefix):
            r = subprocess.run([binary, str(w), str(pb), str(prefix), "dual"],
                               capture_output=True, text=True, check=True)
            return parse_output(r.stdout)
        assert run(63, 63, -1-negative) == ({}, [-1-negative])
        assert run(8, 8, 0) == ({2: 1}, [])
        assert run(10, 6, 0) == ({2: 16}, [])
        assert run(8, 8, 255) == ({}, [])
    print("PASS: independent negative horizons153/2; dual straggler sign,")
    print("fixed chunk mass16 and excluded outside-boundary control.")


if __name__ == "__main__":
    main()
