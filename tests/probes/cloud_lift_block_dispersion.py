#!/usr/bin/env python3
"""Cloud CL776 addendum 3 / CL777: prediction N1h, excess variance of residue counts across blocks.

For a sequence with values in 0..P-1, cut into blocks of B ticks: the chi-square of each block's residue counts
against a fair P-sided die, summed over blocks, is chi-square with (P-1) * (number of blocks) degrees of freedom.
Its standard score is printed for B = 2^10, 2^13, 2^16.  A score well above 0 means counts wander more from
block to block than a fair die's (long-range excess variance); well below 0 means they wander less.
Calibration (before any lift data existed): on 120 fair 7-sided dice the scores have sd 1.03, 1.04, 1.14 and largest
values 2.0, 2.9, 4.3 at the three block sizes, so the normal score is skewed at 2^16 and the exact chi-square tail
p-value is used for the verdict.
Usage: cloud_lift_block_dispersion.py [P SEQFILE]...   (SEQFILE: one byte per tick, from cloud_lift_centre_modp.c)
With no arguments only the two controls run: Rule 30's own centre bits and a pseudo-random 7-sided die.
"""
import importlib.util, math, pathlib, sys
import numpy as np

here = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("spk", here / "cloud_centre_spectrum_kernels.py")
spk = importlib.util.module_from_spec(spec); spec.loader.exec_module(spk)
spec2 = importlib.util.spec_from_file_location("lift", here / "cloud_integer_lift_primes.py")
lift = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(lift)
N = 1 << 21


def scores(name, seq, P):
    seq = np.asarray(seq[:N])
    out = []
    for lb in (10, 13, 16):
        B = 1 << lb; nb = len(seq) // B
        blocks = seq[:nb * B].reshape(nb, B)
        counts = np.stack([(blocks == r).sum(axis=1) for r in range(P)], axis=1).astype(np.float64)
        e = B / P
        X = float(((counts - e) ** 2 / e).sum()); dof = (P - 1) * nb
        z = (X - dof) / math.sqrt(2 * dof)
        pu = lift.gammq(dof / 2, X / 2)             # exact upper-tail p-value (repair declared in CL776 addendum 4)
        out.append((lb, nb, X / dof, z, min(pu, 1 - pu)))
    print(f"   {name}: " + " | ".join(f"blocks of 2^{lb} ({nb}): ratio {r:.4f}, score {z:+.2f}, tail p {pt:.4f}"
                                      for lb, nb, r, z, pt in out))
    return min(pt for *_, pt in out)


def main():
    args = sys.argv[1:]
    print("== N1h block dispersion over 2^21 ticks (score = (chi-square - dof) / sqrt(2 dof))")
    bits = spk.generate(N)
    print("   control: generator reproduces A051023:", bits[:50].tolist() == spk.A051023)
    w2 = scores("rule 30 centre bits (P = 2)", bits, 2)
    rng = np.random.default_rng(20261111)
    for i in range(3):
        scores(f"pseudo-random 7-sided die {i}", rng.integers(0, 7, size=N, dtype=np.uint8), 7)
    scores("pseudo-random 5-sided die", rng.integers(0, 5, size=N, dtype=np.uint8), 5)
    # a planted control: a die whose bias drifts slowly (period 2^18 ticks, amplitude 1 percent on one face)
    t = np.arange(N); drift = 0.01 * np.sin(2 * np.pi * t / (1 << 18))
    die = rng.integers(0, 7, size=N, dtype=np.uint8)
    u = rng.random(N); die[(u < np.abs(drift)) & (drift > 0)] = 1
    scores("control: 7-sided die with a slowly drifting 1 percent excess of one face", die, 7)
    worst = {}
    for i in range(0, len(args), 2):
        P = int(args[i]); seq = np.fromfile(args[i + 1], dtype=np.uint8)
        assert len(seq) >= N and int(seq.max()) < P
        worst[P] = scores(f"centre of the lift modulo {P}", seq, P)
    if worst:
        print("N1h verdict (smaller tail p-value above 0.0005 at every block size):", {P: w > 0.0005 for P, w in worst.items()},
              "| rule 30 bits:", w2 > 0.0005)


if __name__ == "__main__":
    main()
