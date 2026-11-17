#!/usr/bin/env python3
"""ether_front_potential_certificate.py: every finite ingredient of the front-comparison proof of
    M(k) = floor(2k/3) + 4 - [k = 0 or 2 (mod 6)]   for every k >= 1,
in one self-contained file (Python 3, no dependencies). Each check is complete for what it quantifies over; the
reasons why the finite checks cover every k are stated beside them. Hand proof: reports/inquisition-20261031.md,
round 5 ("The front-potential proof").

RUN-ON:     cpu (Python 3), under a second
COMMAND:    python3 tests/probes/ether_front_potential_certificate.py

Provenance (L1259): written by a sub-agent of Local in the round-5 proof workflow (route "mismatch comparison") and
read in full by Local, line by line against the hand argument, before it entered the record. Same worker: GPT's
carrying read of the hand steps is still required. The method (a front state and a potential certified on local
patterns) is prior art: the kit's Rule30EtherThreeErosion (R30-20261024-1fc962, Luis Perez Morales and Claude)
for the period-three ether.

Notation. Two-sided edge frame: X_j(t) = 0 for j < 0, X_0(t) = 1, PR69's rule for j >= 1. Reference wave
E_j(t) = e(t + 2j + c), e = (1,1,0,1,0,1,0,0), any j in Z. Mismatch D = X xor E on all of Z. Front R(t) = max{j :
D_j(t) = 1}. Front phase psi(t) = t + 2R(t) + 2 + c (mod 8) (the phase of cell R+1). Potential
Phi(t) = R(t) + g(psi(t)) - (3/2) t, g = (-3/2, 0, 3/2, -1, 1/2, -2, -1/2, 1). (Doubled to integers below.)
"""
E8 = (1, 1, 0, 1, 0, 1, 0, 0)
WORDS = (43, 202, 178, 172)
G2 = (-3, 0, 3, -2, 1, -4, -1, 2)            # 2 g


def e(p):
    return E8[p % 8]


def check(cond, msg):
    if not cond:
        raise SystemExit("CERTIFICATE FAILURE: " + msg)


def part1_reference():
    # ether(i,t) = bit t of W[i] = e(t + 2i); so E_j(t) = ether(i + j - k, t + q) is the wave with c = q + 2i - 2k.
    for i in range(4):
        for t in range(8):
            check(((WORDS[i] >> t) & 1) == e(t + 2 * i), "ether words vs e")
    # the wave obeys the two-sided recurrence at every phase: e(p+1) = e(p) xor (e(p-2) or e(p-4))
    for p in range(8):
        check(e(p + 1) == e(p) ^ (e(p - 2) | e(p - 4)), "wave recurrence")
    # the edge configuration is a two-sided solution: j<0: 0 = 0 xor (0 or 0); j=0: 1 = 1 xor (0 or 0);
    # j=1: X_1(t+1) = X_1(t) xor (1 or 0) = not X_1(t)  (PR69); j=2: X_2 xor (X_1 or 1) = not X_2 (PR69's rule at j=2)
    for x1 in (0, 1):
        check((x1 ^ (1 | 0)) == 1 - x1, "depth 1")
        for x2 in (0, 1):
            check((x2 ^ (x1 | 1)) == 1 - x2, "depth 2")
    print("1. reference wave = PR69 ether; wave and black-edge row both obey X_j(t+1) = X_j(t) xor (X_{j-1} or X_{j-2}) "
          "for every integer j: PASS")


def F(phi, a, b):
    """Mismatch increment at a cell of phase phi: (X_{j-1} or X_{j-2}) xor (E_{j-1} or E_{j-2})."""
    E1, E2 = e(phi - 2), e(phi - 4)
    return ((E1 ^ a) | (E2 ^ b)) ^ (E1 | E2)


def part2_lemmaA_B():
    # literal one-step update of a window whose top mismatch is R (cells above R clean); psi = phase of cell R+1
    table = {}
    for psi in range(8):
        for dm2 in (0, 1):
            for dm1 in (0, 1):
                D = {-2: dm2, -1: dm1, 0: 1}
                D.update({j: 0 for j in range(1, 9)})
                Et = {j: e(psi + 2 * (j - 1)) for j in range(-2, 9)}
                Et1 = {j: e(psi + 2 * (j - 1) + 1) for j in range(-2, 9)}
                X = {j: Et[j] ^ D[j] for j in D}
                new = {j: (X[j] ^ (X[j - 1] | X[j - 2])) ^ Et1[j] for j in range(0, 9)}
                for j in range(0, 9):          # same as the mismatch rule with F
                    check(new[j] == D[j] ^ F(psi + 2 * (j - 1), D[j - 1], D[j - 2]), "F rule")
                check(all(new[j] == 0 for j in range(3, 9)), "A1: nothing beyond R+2")
                top = [j for j in (0, 1, 2) if new[j]]
                if not top:
                    check(psi == 1 and dm1 == 1 and dm2 == 1, "A3: retreat only at psi=1 with D_{R-1}=D_{R-2}=1")
                    table[(psi, dm2, dm1)] = None
                    continue
                dR = max(top)
                psin = (psi + 1 + 2 * dR) % 8
                check(2 * dR + G2[psin] - G2[psi] - 3 == 0, "A2: Phi invariant without retreat")
                table[(psi, dm2, dm1)] = dR
                if psi == 4:
                    check(dR == 2 and new[1] == 0 and psin == 1, "B: psi=4 -> front +2, cell below it clean, psi'=1")
    # A4: the table
    for (psi, dm2, dm1), dR in table.items():
        want = {0: 1, 2: 2, 4: 2, 6: 2, 7: 2,
                1: (None if (dm1 and dm2) else 0),
                3: (1 if dm1 == 0 else 0),
                5: (1 if dm1 == 1 else 0)}[psi]
        check(dR == want, f"A4 table at psi={psi}")
    # B: psi(t) = psi(t-1) + 1 + 2 dR, odd step, so after a retreat (from psi = 1) psi is even; among the
    # non-retreat moves only psi = 4 leads to psi = 1.
    preds = {psi for (psi, a, b), dR in table.items() if dR is not None and (psi + 1 + 2 * dR) % 8 == 1}
    check(preds == {4}, "B: the only predecessor of psi = 1")
    check(all((1 + 1 + 2 * (-d)) % 2 == 0 for d in range(1, 50)), "B: retreats land on even psi")
    print("2. Lemma A (all 32 local configurations, literal update): moves +2 at psi in {2,4,6,7}, +1 at psi=0,")
    print("   0 at psi=1 (retreat iff D_{R-1}=D_{R-2}=1), psi=3: +1 iff D_{R-1}=0 else 0, psi=5: +1 iff D_{R-1}=1 else 0;")
    print("   Phi unchanged by every non-retreat move.  Lemma B: psi=1 is entered only from psi=4 by a +2 move that")
    print("   leaves D_{R-1} = 0, so no retreat ever happens at t >= 1: PASS")
    return table


def value2(c, t, R):
    return 2 * R + G2[(t + 2 * R + 2 + c) % 8] - 3 * t


def Rmin(c, t, P2):
    R = (P2 + 3 * t) // 2 - 4
    check(value2(c, t, R) < P2, "Rmin start")
    while value2(c, t, R) < P2:
        R += 1
    return R


def part3_potential_floor():
    # value2(c,t,R) is non-decreasing in R (steps 0 or 8) and invariant under (t,R) -> (t+4,R+6): residues suffice
    for c in range(8):
        for t in range(8):
            for R in range(-8, 8):
                check(value2(c, t, R + 1) - value2(c, t, R) in (0, 8), "monotone in R")
                check(value2(c, t + 4, R + 6) == value2(c, t, R), "(4,6) invariance")
    PHI2 = {}
    lines = []
    for c in range(8):
        D1 = {j: (e(1 + 2 * j + c) if j < 0 else 1 - e(1 + c)) for j in range(-8, 1)}   # fixed cells at t = 1
        r = max(j for j in D1 if D1[j])
        # the unique D(0) with D_j(1) = 0 for all j >= 1: D_j(0) = F(phase 2j+c; D_{j-1}(0), D_{j-2}(0))
        D = {0: 1 - e(c), -1: e(c - 2)}
        seen, j, dies = set(), 1, False
        while True:
            st = (D[j - 1], D[j - 2], j % 4)
            if st[:2] == (0, 0):
                dies = True
                break
            if st in seen:
                break                       # cycles through nonzero states: infinitely many mismatches
            seen.add(st)
            D[j] = F(2 * j + c, D[j - 1], D[j - 2])
            j += 1
        P = value2(c, 1, r)
        if not dies:                         # finite-support rows cannot have R(1) = r_c
            P = max(P, value2(c, 1, 1))
        if c == 7:
            check(dies and all(D.get(i, 0) == 0 for i in range(1, 30)), "c=7: the healing row is the witness")
            check(r == -4 and value2(7, 1, -4) == -8 and value2(7, 1, 1) == 0 and D1[0] == 0, "c=7 dichotomy")
            P = 0                            # non-witness rows: R(1) >= 1, Phi(1) >= 0
        PHI2[c] = P
        lines.append(f"   c={c}: fixed cells give r_c={r:+d}; healing row {'finite' if dies else 'infinite'}; "
                     f"Phi(1) >= {P / 2:+.1f}" + ("  (non-witness rows; the witness has Phi = -4)" if c == 7 else ""))
    print("3. potential floor at t = 1 (Phi(1) = h_c(R(1)) is non-decreasing in R(1) >= r_c):")
    print("\n".join(lines))
    return PHI2


def Rw(t):
    n, r = divmod(t, 4)
    return (6 * n - 4, 6 * n - 4, 6 * n - 2, 6 * n)[r]


def part4_front_comparison(PHI2, table):
    # witness front: R(1) = -4, psi(1) = 2; every move on its cycle 2 -> 7 -> 4 -> 1 -> 2 is forced (no retreat at t>=1)
    R, psi = -4, (1 + 2 * (-4) + 2 + 7) % 8
    check(psi == 2, "witness psi(1)")
    for t in range(1, 41):
        check(R == Rw(t), f"witness front at t={t}")
        moves = {table[(psi, a, b)] for a in (0, 1) for b in (0, 1)} - {None}
        if psi == 1:
            moves = {0}                      # Lemma B
        check(len(moves) == 1, "witness move forced")
        dR = moves.pop()
        R, psi = R + dR, (psi + 1 + 2 * dR) % 8
    check(all(Rw(t + 4) == Rw(t) + 6 for t in range(1, 100)), "R_w period")
    # front comparison on t = 1..4 (then for all t >= 1 by the (4,6) invariance of value2 and of R_w)
    rows = []
    for c in range(8):
        mins = [Rmin(c, t, PHI2[c]) for t in (1, 2, 3, 4)]
        margin = 3 if c == 7 else 0
        check(all(mins[i] >= Rw(i + 1) + margin for i in range(4)), f"front comparison c={c}")
        for t in range(1, 60):
            check(Rmin(c, t + 4, PHI2[c]) == Rmin(c, t, PHI2[c]) + 6, "Rmin period")
        rows.append(f"   c={c}: Rmin(t=1..4) = {mins}" + ("  >= R_w + 3" if c == 7 else ""))
    print(f"4. witness front forced: R_w(t) = 6n-4, 6n-4, 6n-2, 6n at t = 4n..4n+3 (t >= 1), so R_w(t=1..4) = "
          f"{[Rw(t) for t in (1, 2, 3, 4)]};")
    print("   front comparison R(t) >= Rmin(c,t,Phi_c) >= R_w(t) for every t >= 1, every row, every phase:")
    print("\n".join(rows))


def part5_episode():
    # L_w(k) = min{t >= 1 : R_w(t) >= k} lands on k or k+1; closed form by k mod 6 (n >= 0): checked symbolically
    # through the six residues, and numerically for k < 2000
    for k in range(1, 2000):
        tw = next(t for t in range(1, 4000) if Rw(t) >= k)
        check(Rw(tw) in (k, k + 1), "landing")
        m = (2 * k) // 3
        check(tw == m + 4 - (1 if k % 6 in (0, 2) else 0), "closed form")
    print("5. witness episode L_w(k) = min{t >= 1 : R_w(t) >= k} = floor(2k/3) + 4 - [k = 0,2 mod 6], front landing on k or")
    print("   k+1 (k < 2000; the six residue identities are linear in n): PASS")
    print("   => every row and phase: at t = L_w(k) the clean-topped modified row has a mismatch at depth >= k, so")
    print("      M(k) <= L_w(k); the witness attains it; at phase 7 every other prefix has episode <= L_w(k) - 1.")


def main():
    part1_reference()
    table = part2_lemmaA_B()
    PHI2 = part3_potential_floor()
    part4_front_comparison(PHI2, table)
    part5_episode()
    print("MISMATCH_FRONT_CERTIFICATE_PASS")


if __name__ == '__main__':
    main()
