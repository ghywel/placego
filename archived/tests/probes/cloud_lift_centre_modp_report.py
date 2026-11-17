#!/usr/bin/env python3
"""Cloud CL776/CL777: chi-squares from the raw counts printed by cloud_lift_centre_modp.c.

Usage: cloud_lift_centre_modp_report.py P RAWFILE [RAWFILE ...]
The 2^21 raw file was produced before the C code printed a pair table per segment; it has the pair table of the
fresh ticks 2^18..2^21 only.  The 2^18 raw file comes from the later code and has both.
"""
import math, sys, importlib.util, pathlib
import numpy as np

here = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("lift", here / "cloud_integer_lift_primes.py")
lift = importlib.util.module_from_spec(spec); spec.loader.exec_module(lift)


def residues(name, cnt, P):
    n = sum(cnt); e = n / P; sd = math.sqrt(n * (P - 1) / P / P)
    x, dof, pv = lift.chi2_p(cnt, [e] * P)
    print(f"  {name}: {n} ticks, chi2 {x:.2f} on {dof} dof, p-value {pv:.4f} | z per residue {[round((c - e) / sd, 2) for c in cnt]}")


def pairs(name, tab, P):
    t = np.array(tab).reshape(P, P)
    x, dof, pv = lift.chi2_p(t, [t.sum() / P / P] * (P * P))
    xi, dofi, pvi = lift.indep_p(t)
    print(f"  {name}: pairs against uniform chi2 {x:.1f} on {dof} dof, p-value {pv:.4f} | dependence alone chi2 {xi:.1f} on {dofi} dof, p-value {pvi:.4f}")


def main():
    P = int(sys.argv[1])
    for path in sys.argv[2:]:
        print(pathlib.Path(path).name)
        segs = []
        for line in open(path):
            w = line.split()
            if not w:
                continue
            if w[0] == "segment":
                segs.append((int(w[1]), int(w[2]), [int(v) for v in w[4:]]))
                residues(f"ticks {w[1]}..{w[2]}", segs[-1][2], P)
            elif w[0] == "segpairs":
                pairs(f"ticks {w[1]}..{w[2]}", [int(v) for v in w[4:]], P)
            elif w[0] == "pairs":
                pairs(f"ticks {w[1]}..{w[2]}", [int(v) for v in w[4:]], P)
            elif w[0] == "exit":
                print("  " + line.strip())
        tot = lambda a, b: [sum(c[i] for lo, hi, c in segs if lo >= a and hi <= b) for i in range(P)]
        last = segs[-1][1]
        if last > (1 << 18):
            residues("first 2^18 (run 2 had chi2 20.5 here)", tot(0, 1 << 18), P)
            residues("FRESH ticks 2^18.. end (prediction N1g)", tot(1 << 18, last), P)
        residues("whole run", tot(0, last), P)


if __name__ == "__main__":
    main()
