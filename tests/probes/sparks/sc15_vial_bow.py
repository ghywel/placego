#!/usr/bin/env python3
"""sc15_vial_bow.py: spark SC15 (SPARKS.md). The bow you cannot see.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/sparks/sc15_vial_bow.py
COST:       instant.

A bubble moves the vial's radius times the tilt, so a vial whose bubble moves one 2 mm graduation for a tilt of
theta radians has radius 2 mm / theta, and over a length L its curve rises L^2 / (8 R) above the chord (the
sagitta). The published figures below were looked up after the prediction was pushed; their sources are named in
SPARKS.md. Prediction: builders' vials 5' to 30' per graduation, a bow of 0.2 to 1.4 mm over 5 cm; machinists'
levels a radius of at least 20 m and a bow under 0.02 mm. Fail: builders' vials finer than 2' or coarser than 60'.
Control: the sagitta formula is checked against the exact chord geometry, R - sqrt(R^2 - (L/2)^2).
"""
import math

GRAD, L = 2.0, 50.0  # mm
ARCMIN = math.pi / (180 * 60)
LEVELS = [  # (name, tilt in radians that moves the bubble one 2 mm graduation)
    ("builders' level, Hultafors HV and RS (vial radius 200 mm, '10 mm/m')", 0.010),
    ("US federal specification's coarsest vial (45 minutes)", 45 * ARCMIN),
    ("surveyor's level (0.005 degree, Wikipedia)", math.radians(0.005)),
    ("machinist's level, 0.04 mm/m per division (Wikipedia)", 0.04e-3),
    ("machinist's level, 0.02 mm/m per division (a maker's listing)", 0.02e-3),
]


def main():
    for name, th in LEVELS:
        r = GRAD / th
        bow = L * L / (8 * r)
        exact = r - math.sqrt(r * r - (L / 2) ** 2)
        assert abs(bow - exact) / exact < 0.01, (bow, exact)
        print(f"{name}:\n  {th / ARCMIN:9.3f}' per graduation, radius {r / 1000:9.3f} m, bow over 5 cm "
              f"{bow:.4f} mm")


if __name__ == "__main__":
    main()
