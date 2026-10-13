#!/usr/bin/env python3
"""Fixed controls of an absolute guard transported across a white triangle.

RUN-ON: cpu, Python standard library, no solver or census.
COMMAND: python3 tests/probes/lexicon/rule30_zero_triangle_guard_transport.py

Record searched: zero.band|zero.triangle|white.triangle|white.band with
guard|charge|boundary|diagonal ->40 hits13files; packet/triangle/guard
search adds no prior first-crossing packet. GC549 checkpoint25, GC592,
GC717, GC718, GC1167, GC1199 and GC1200 read. The triangle and frontier
identities are established; the target is their absolute guard transport.

PREDICTIONS before execution (2026-10-13):
 Z1: d in(2,5,8), a in(0,1,3), both phases and both offsets k=d+2a+e:
     with x(d-1)=1 and zeros d..k+1, the packet at crop a+1, depths
     n=k-a-1 and n+1, is (1,1-e). Use two fixed exterior tails:72 cases.
 Z2: the remaining GC717 formula E XOR H0 XOR P equals the direct
     nearest-left value at tick k in each case; no compatible clock
     before k or right-language membership is predicted.
 Independent control: packed Boolean updates versus literal Wolfram30.
 Counterfactual/unexpected controls: remove the final required zero,
     flip only initial k+1, and the packet's partner and final guard
     both flip (d5,a3, both phases/offsets). Thus farther data cannot be
     ignored outside the stated horizon. At d1,a0,p1 the even packet
     hits the clamped wall and is01, refuting extension to d1.
 No depth scan, record maximization, membership test or train refinement.

OUTCOME: Z1/Z2 held in72 fixed cases; four sharp final-cell controls and
the d1 wall-overwrite counter held. No instrument failure.

Z3 ADDENDUM before its execution: on those same cases, the final guard
equals E XOR(n mod2) XOR the parity of00 pairs (F_t,r_t). At a black
endpoint k, a passing guard requires that hole parity=(d+a-1) mod2;
its terminal hole is the demanded visible bit at white time k-1.
Record searched:00|empty.pair|white.pair|hole.parity with diagonal and
guard|charge|triangle ->23hits12files, no prior triangle-entry packet.
Z3 OUTCOME: held on the same72 cases, including the terminal demand.
This is the one-step rule summed along the retained path, not a claim
that the hole input has a closed scalar update. No new cases added.
"""


def packed(seed, phase, ticks, width):
    mask = (1 << width) - 1
    b = sum(v << (j - 1) for j, v in seed.items())
    rows = [{j: (b >> (j - 1)) & 1 for j in range(1, width + 1)}]
    for t in range(ticks):
        b = ((b >> 1) ^ (b | ((b << 1) | ((phase + t) % 2)))) & mask
        rows.append({j: (b >> (j - 1)) & 1 for j in range(1, width + 1)})
    return rows


def literal(seed, phase, ticks, width):
    rows = [{j: seed.get(j, 0) for j in range(1, width + 1)}]
    for t in range(ticks):
        old = rows[-1]
        new = {}
        for j in range(1, width + 1):
            l, c = old.get(j + 1, 0), old[j]
            r = old[j - 1] if j > 1 else (phase + t) % 2
            new[j] = (30 >> (4 * l + 2 * c + r)) & 1
        rows.append(new)
    return rows


def profiles(rows, phase, crop, n):
    def cell(t, j):
        return rows[crop + t][j] if j else (phase + crop + t) % 2
    h, parity, i = 0, 0, 0
    for t in range(n):
        r = cell(t, n - t - 1)
        h ^= i | r
        parity ^= 1 - r
        if t < n - 1:              # no profile beyond the clamped wall
            i ^= r | cell(t, n - t - 2)
    return h, parity


def seed_for(d, k, tail):
    seed = {j: (j * (j + 1) // 2) % 2 for j in range(1, d)}
    seed[d - 1] = 1
    seed[k + 2], seed[k + 4] = tail, 1 - tail
    return seed


def main():
    total = 0
    for d in (2, 5, 8):
        for a in (0, 1, 3):
            for phase in (0, 1):
                for e in (0, 1):
                    k, crop = d + 2 * a + e, a + 1
                    n = k - crop
                    for tail in (0, 1):
                        seed = seed_for(d, k, tail)
                        width = k + 4 + k
                        rows = packed(seed, phase, k, width)
                        assert rows == literal(seed, phase, k, width)
                        assert (rows[crop][n], rows[crop][n + 1]) == (1, 1 - e)
                        h, parity = profiles(rows, phase, crop, n)
                        assert rows[k][1] == ((1 - e) ^ h ^ parity)
                        holes = []
                        for t in range(n):
                            f = rows[crop + t][n - t]
                            j = n - t - 1
                            r = rows[crop + t][j] if j else (phase + crop + t) % 2
                            holes.append((1 - f) * (1 - r))
                        charge = sum(holes) % 2
                        assert rows[k][1] == ((1 - e) ^ (n % 2) ^ charge)
                        if (phase + k) % 2:
                            demanded = 1 ^ rows[k - 1][1]
                            assert holes[-1] == demanded
                            if rows[k][1] == 1:
                                assert charge == (d + a - 1) % 2
                                assert demanded == ((d + a - 1) % 2) ^ (sum(holes[:-1]) % 2)
                        total += 1
    sharp = 0
    for phase in (0, 1):
        for e in (0, 1):
            d, a = 5, 3
            k, crop = d + 2 * a + e, a + 1
            n = k - crop
            seed = seed_for(d, k, 0)
            first = packed(seed, phase, k, 2 * k + 4)
            seed[k + 1] = 1        # one cell outside the shortened band
            second = packed(seed, phase, k, 2 * k + 4)
            assert second == literal(seed, phase, k, 2 * k + 4)
            assert first[crop][n] == second[crop][n] == 1
            assert first[crop][n + 1] ^ second[crop][n + 1] == 1
            assert first[k][1] ^ second[k][1] == 1
            sharp += 1
    seed = {1: 0, 2: 0}
    rows = packed(seed, 1, 1, 4)
    assert (0, rows[1][1]) == (0, 1)  # wall at crop1, then actual depth1
    print('Z1/Z2 PASS:', total, 'fixed packets, guard identities and independent engines.')
    print('Z3 PASS: hole parity, terminal white demand and passing black-guard constraint in the same cases.')
    print('Sharp final-cell controls PASS:', sharp, '; d1 wall-overwrite counter PASS.')


if __name__ == '__main__':
    main()
