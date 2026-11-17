#!/usr/bin/env python3
"""sc8_water_level.py: spark SC8 (SPARKS.md). A water level and a warm hose end.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/sparks/sc8_water_level.py
COST:       instant.

Two arms of a hose level stand on a common low point; arm 1 holds a column of height h at temperature t1, arm 2 at
t2. Equal pressure at the bottom gives rho1 h1 = rho2 h2, so the surfaces differ by h1 (rho1 / rho2 - 1). Density of
air-free water from Tanaka and others (2001, Metrologia 38, 301), the CIPM formula.
Prediction (published in SPARKS.md before this ran): 1.5 +/- 0.3 mm for 1 m at 10 C against 20 C, roughly in
proportion to height and temperature gap. Fail: under 0.5 mm.
Control: the formula gives about 999.97 kg/m^3 at 4 C (its maximum) and about 998.21 at 20 C.
"""
A1, A2, A3, A4, A5 = -3.983035, 301.797, 522528.9, 69.34881, 999.974950


def rho(t):
    return A5 * (1 - (t + A1) ** 2 * (t + A2) / (A3 * (t + A4)))


def main():
    assert abs(rho(4.0) - 999.97) < 0.01 and abs(rho(20.0) - 998.21) < 0.01
    print(f"density: 4 C {rho(4):.3f}, 10 C {rho(10):.3f}, 20 C {rho(20):.3f}, 30 C {rho(30):.3f} kg/m^3")
    print(" column   cold  warm   difference")
    for h in (0.5, 1.0, 2.0):
        for t1, t2 in ((10, 20), (15, 25), (20, 30), (10, 40)):
            d = h * (rho(t1) / rho(t2) - 1) * 1000
            print(f"  {h:3.1f} m  {t1:3d} C {t2:3d} C   {d:5.2f} mm")
    d = 1.0 * (rho(10) / rho(20) - 1) * 1000
    print("PASS" if abs(d - 1.5) <= 0.3 else ("FAIL" if d < 0.5 else "PARTIAL"))


if __name__ == "__main__":
    main()
