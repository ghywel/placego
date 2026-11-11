#!/usr/bin/env python3
"""Cloud CL776 addendum 5 / CL778: prediction N1i, the block statistic of N1h on fresh ticks only.

N1h's control (the centre of the integer lift modulo 5, blocks of 2^16 ticks over the first 2^21 ticks) fell below
its declared threshold on the lower tail: its counts were more even from block to block than a fair die's.  The rule
written beforehand makes fresh data the judge.  This probe reads a longer sequence and computes the same statistic on
a range of ticks [2^LO, 2^HI) that the first run never saw.

Statistic: cut the range into blocks of B ticks; the chi-square of each block's residue counts against a fair P-sided
die, summed over the blocks, is referred to the chi-square law with (P - 1) * (number of blocks) degrees of freedom.
That reference is asymptotic (GPT's note, GC2931): the tail values are not exact multinomial probabilities.

Prediction N1i, pushed before the run existed (CL776 addendum 5): on the 32 fresh blocks of 2^16 ticks the lower-tail
value is above 0.01.  Chance given beforehand: 0.85.
Usage: cloud_lift_block_fresh.py P SEQFILE LO HI [OLDSEQFILE [SEC]]
       LO HI = 21 22 is N1i.  LO HI = 22 23 is N1j (CL778); SEC = 21 adds the secondary figures from 2^21 on.
"""
import hashlib, importlib.util, pathlib, sys
import numpy as np

here = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("lift", here / "cloud_integer_lift_primes.py")
lift = importlib.util.module_from_spec(spec); spec.loader.exec_module(lift)


def block_stat(seq, P, lb):
    B = 1 << lb; nb = len(seq) // B
    blocks = seq[:nb * B].reshape(nb, B)
    counts = np.stack([(blocks == r).sum(axis=1) for r in range(P)], axis=1).astype(np.float64)
    e = B / P
    per_block = ((counts - e) ** 2 / e).sum(axis=1)
    X = float(per_block.sum()); dof = (P - 1) * nb
    upper = lift.gammq(dof / 2, X / 2)
    return nb, X, dof, upper, per_block


def main():
    P = int(sys.argv[1]); path = sys.argv[2]; lo = int(sys.argv[3]); hi = int(sys.argv[4])
    seq = np.fromfile(path, dtype=np.uint8)
    assert len(seq) >= (1 << hi) and int(seq.max()) < P
    print(f"sequence: {len(seq)} ticks modulo {P}, SHA-256 {hashlib.sha256(seq.tobytes()).hexdigest()}")
    if len(sys.argv) > 5:
        old = np.fromfile(sys.argv[5], dtype=np.uint8)
        print(f"control: the first {len(old)} ticks equal the earlier run's sequence:", bool((seq[:len(old)] == old).all()))
    for name, part in (("old ticks [0, 2^%d)" % lo, seq[:1 << lo]), ("fresh ticks [2^%d, 2^%d)" % (lo, hi), seq[1 << lo:1 << hi])):
        counts = np.bincount(part, minlength=P)
        e = len(part) / P; x = float(((counts - e) ** 2 / e).sum())
        print(f"== {name}: residue counts {counts.tolist()}, chi-square {x:.2f} on {P - 1} dof, upper tail {lift.gammq((P - 1) / 2, x / 2):.4f}")
        for lb in (10, 13, 16):
            nb, X, dof, upper, per_block = block_stat(part, P, lb)
            print(f"   blocks of 2^{lb} ({nb}): sum {X:.2f} on {dof} dof, ratio {X / dof:.4f}, upper tail {upper:.6f}, lower tail {1 - upper:.6f}")
            if lb == 16:
                print("      per-block chi-squares:", " ".join(f"{v:.1f}" for v in per_block))
    nb, X, dof, upper, _ = block_stat(seq[1 << lo:1 << hi], P, 16)
    lower = 1 - upper
    if hi == 22:
        print(f"N1i: {nb} fresh blocks of 2^16 ticks, sum {X:.2f} on {dof} dof, lower tail {lower:.6f}, upper tail {upper:.6f}")
        print("N1i verdict (lower tail above 0.01):", lower > 0.01)
    else:
        # N1j (CL778): the 64 fresh blocks of [2^22, 2^23).  Closed above 0.05, real below 0.001, otherwise unresolved.
        print(f"N1j: {nb} fresh blocks of 2^16 ticks, sum {X:.2f} on {dof} dof, lower tail {lower:.6f}, upper tail {upper:.6f}")
        print("N1j verdict:", "closed (lower tail above 0.05)" if lower > 0.05 else "real (lower tail below 0.001)" if lower < 0.001 else "unresolved (between 0.001 and 0.05)")
        if len(sys.argv) > 6:                              # secondary, no verdict: all fresh blocks from 2^SEC on
            sec = int(sys.argv[6])
            for lb in (10, 13, 16):
                nb, X, dof, upper, _ = block_stat(seq[1 << sec:1 << hi], P, lb)
                print(f"   secondary, ticks [2^{sec}, 2^{hi}), blocks of 2^{lb} ({nb}): sum {X:.2f} on {dof} dof, ratio {X / dof:.4f}, lower tail {1 - upper:.6f}")
            nb, X, dof, upper, _ = block_stat(seq[:1 << hi], P, 16)
            print(f"   secondary, the whole run [0, 2^{hi}), blocks of 2^16 ({nb}): sum {X:.2f} on {dof} dof, ratio {X / dof:.4f}, lower tail {1 - upper:.6f}")


if __name__ == "__main__":
    main()
