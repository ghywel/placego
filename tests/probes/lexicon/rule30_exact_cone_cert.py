#!/usr/bin/env python3
"""rule30_exact_cone_cert.py: the exact light-cone record query (RR's cnf, rule30_records_real_sat.py), one phase at a
time, with the phase's certified absent visible words added as redundant clauses on column 1, solved by CaDiCaL with
an LRAT proof checked by cake_lpr. The fallback agreed with GPT (L694, GC1209) for depths where RLK's relaxation keeps
returning non-real early origins (147 at L = 18, phase 0: two early-prefix artefacts, two new certified cuts).

Soundness. RR's cone CNF is exact: column 0 follows the wall through T = d + L - 1 and the band is white at time 0;
every configuration's cone is covered (RR's docstring). A certified absent word cannot occur in a real visible word, so
adding its clauses on the white-tick samples of column 1 removes no real configuration. UNSAT, VERIFIED by cake_lpr and
with every added word certified (the 44-bit lists and cuts40 by MFC/L590..L641; the 50- and 70-bit cuts by
rule30_cadical_certify.py K12 and K15), gives R_real(d) <= L - 1 in that phase. SAT gives a cone whose zero-padded
simulation (RR's check) keeps the clock and the band: a real witness, R_real(d) >= L.

RUN-ON:     cpu; CaDiCaL plus cake_lpr (one check at a time through the lock wrapper).
COMMAND:    python3 tests/probes/lexicon/rule30_exact_cone_cert.py D L PHASE [CAP=14400] [EXTRA_CUTS,comma-separated]
            python3 tests/probes/lexicon/rule30_exact_cone_cert.py controls

Record searched (record_find, 2026-10-13 22:31 BST): 'exact cone|cone CNF' -> 23 hits in 13 files (RR, RR3, GC937's
solver-free match of the cone CNF); 'RR3' -> 84 hits in 25 files. RR, RR3 (rule30_cloud_rr3.py) and TR's 13,321 s
UNKNOWNs at 140 .. 164 read.

PREDICTIONS (written 2026-10-13 22:31 BST, before any run; the main run is made only if certify K16 is SAT).
  X1 must hold (controls): d = 21: L = 16 in phase 0 is VERIFIED-UNSAT (RR's R_real(21) = 15 is the maximum over both
     phases), and L = 15 is SAT with a checking witness in at least one of the two phases.
  X2 blind (0.45): d = 147, L = 18, phase 0, with the 50- and 70-bit cuts, ends VERIFIED-UNSAT within a 4-hour cap, so
     R_real(147) <= 17 in phase 0 without any relaxation. REFUTED-BY: SAT (then a real witness, R_real(147) >= 18,
     checked by simulation), a cap, or CAKE-FAILED.

AMENDMENT (2026-10-13 22:35 BST, before the run): the first loop check (loop-check rule, L696) drew door 5, the
  exact-cone census at 147 .. 150, so X2 is run now, beside certify K16, not only if K16 is SAT. Both are sound and
  answer different questions (relaxed with cuts against exact with cuts). X2's prediction is unchanged.

OUTCOME (controls, 2026-10-13 22:31 BST, seconds; machine output quoted): X1 HELD.
  EXACT d=21 L=16 phase 0 (1156 words): VERIFIED-UNSAT; cnf sha256 03fe08b3e63be651bf8cc2babbbc2c0d7c136ac071180882c65fe59625f11ac0.
  EXACT d=21 L=15 phase 0 (1156 words): VERIFIED-UNSAT (so the phase-0 record at 21 is at most 14).
  EXACT d=21 L=15 phase 1 (1226 words): SAT-WITNESS, row 00000000000000001011110001111000011100000100000100111100111111111111111,
     checked by RR's zero-padded simulation: RR's R_real(21) = 15 is reached in phase 1.
  The first control run failed at import (RR's module parses sys.argv); shielded and rerun, retained in history.

OUTCOME X2 (2026-10-14 00:07 BST, M5; machine output quoted): X2 REFUTED by a real witness.
  EXACT d=147 L=18 phase 0 (1158 words): SAT-WITNESS; cnf sha256
     1f156ffca7e47c500ba4afe4ff9c75c897ffaf00584200f123cd4f404777476c; solve 5338 s; partial LRAT (29.9 GB) deleted.
  The witness row (cells -164 .. 164) passes RR's zero-padded check (band and clock) and the phase gate. An independent
  replay on an expanding zero background (L700 follow-up) confirms the band at depths 147 .. 164 and the clock for
  t = 0 .. 164 in phase 0. The support is -146 .. 101: a finite configuration whose left half is white beyond depth 146
  keeps the clock for 165 ticks (it fails at 165, past the cone). So R_real(147) >= 18 (phase 0). Its left row agrees
  with round 2's relaxed model (rule30_cadical_lift.py) on depths 164 .. 58; the two first differ at depth 57. The
  relaxed artefacts carried non-real codes over a left row that is nearly real.
  The witness row, cells -164 .. 164 at time 0 (329 bits, for replay; GC1214.1):
     0000000000000000001111011101101101110011000111001011111111100101001110000111000110000010001111111101
     1110001011011001011100000011101000111111100110001100001100100101001001010001101100011100110010100110
     0100011001010010001110001101000110011111000001000000100101011011010000000000000000000000000000000000
     00000000000000000000000000000
  With K14 (148 phase 0 <= 17) and the same-phase bound R_p(d) <= R_p(d + 1) + 1, R_real,0(147) = 18 exactly
  (GC1214.1).
  X4 WITHDRAWN (2026-10-14 00:14 BST, stopped before any output): its answer is implied UNSAT by that same bound.
OUTCOME X3 (2026-10-14 03:26 BST, M5): X3 REFUTED (UNSAT, predicted SAT at 0.35). EXACT d=149 L=18 phase 0 (1158
  words): VERIFIED-UNSAT; cnf sha256 0f643f65fed169685596ead70f8a5e4c3521a9217a93e0350ba9f0c7b126ed14; solve 9591 s,
  check 1881 s, lrat 42864.4 MB, deleted. So R_real,0(149) <= 17 (exact cone, no relaxation). Phase 1 is X6.
OUTCOME X5 (2026-10-14 04:23 BST, M5): X5 REFUTED (UNSAT, predicted SAT at 0.35). EXACT d=150 L=18 phase 0 (1158
  words): VERIFIED-UNSAT; cnf sha256 dd7fcb266c0491fdb4db361b9d4bb7df5940c3fe6c49f78cd4f8ea9202daa9a0; solve 8487 s,
  check 1544 s, lrat 43402.6 MB, deleted. So R_real,0(150) <= 17. Phase 1 is X7.
OUTCOME X6 (2026-10-14 04:49 BST, M5): X6 REFUTED (UNSAT, predicted SAT at 0.35). EXACT d=149 L=18 phase 1 (1226
  words): VERIFIED-UNSAT; cnf sha256 1e7a04442e3ec1980910d920fc4f5e6ff925aebaf827be6af09eb3236631b092; solve 8809 s,
  check 2699 s, lrat 44389.5 MB, deleted. With X3, R_real(149) <= 17 in both phases.

GPT witness-review predictions (2026-10-14 00:31 BST, before replay; GC1215):
  The committed 329-bit row must have centre0, initial support -146..101 and a white band at -164..-147;
  independent literal-table evolution must match the clock at0..164 and first fail at165, and RR's checker must
  agree on the specified finite query. Unexpected control: adding black cells at -166 and166 must preserve
  the entire observed clock through164 and the initial band (both are outside the determining cone).
  No solver or record search; the published row is a fixed verification fixture.
  OUTCOME: all checks PASS. Witness ASCII SHA256
  bd2e7ab1aa9cb7628d9348cb7f046fad4acbddf8d15b7d30c51d387b00d07517.
  Literal expanding evolution and RR's zero-padded check agree; outside-cone blacks preserve times0..164.

ADDENDUM PREDICTIONS (2026-10-14 00:12 BST, before the runs; the frontier after X2, both with the phase-0 lists plus the 50-
  and 70-bit cuts). Record searched: as above, plus 8.96's addendum (149, 150 sampled 15 .. 17; 148 phase 0 <= 17).
  X3 blind (0.35 for SAT): d = 149, L = 18, phase 0: SAT with a checking witness (R_real(149) >= 18). REFUTED-BY:
     VERIFIED-UNSAT (then phase 0 <= 17 at 149), a cap, or CAKE-FAILED.
  X4 blind (0.25 for SAT): d = 147, L = 19, phase 0: SAT with a checking witness (R_real(147) >= 19, a new high for the
     run). REFUTED-BY: VERIFIED-UNSAT (phase 0 at 147 is then exactly 18), a cap, or CAKE-FAILED.

ADDENDUM PREDICTIONS (2026-10-14 01:33 BST, before the runs; the frontier at 18 continued, on the cores the finished
  history census freed). Phase 0 runs use the 44-bit list, cuts40 and the 50- and 70-bit cuts; phase 1 uses 44allp1
  and cuts40 only (the two long cuts are phase-0 words).
  X5 blind (0.35 for SAT): d = 150, L = 18, phase 0: SAT with a checking witness. REFUTED-BY: VERIFIED-UNSAT, a cap,
     or CAKE-FAILED.
  X6 blind (0.35 for SAT): d = 149, L = 18, phase 1: SAT with a checking witness. REFUTED-BY: VERIFIED-UNSAT, a cap,
     or CAKE-FAILED. With X3 (phase 0) this decides 149 at 18 in both phases.

ADDENDUM PREDICTION (2026-10-14 02:04 BST, before the run; the last cell of the registered frontier 148 .. 150 at 18).
  X7 blind (0.35 for SAT): d = 150, L = 18, phase 1 (44allp1 and cuts40): SAT with a checking witness. REFUTED-BY:
     VERIFIED-UNSAT, a cap, or CAKE-FAILED. With X5 this decides 150 at 18 in both phases.

GPT review (GC1210.1, 2026-10-13): the inherited exact cone, phase unit and
white-sample cut placement are sound; no carrying defect found. Added only
metadata assertions for the mirrored RR variable map and a requested-phase
check in SAT replay. The CNF is unchanged. Pure construction controls at
(21,16,0),(21,15,1),(147,18,0) compare before/after clauses, row map and
variable bound identically; no solver, certificate or witness replay.
The current X2 run needs no restart; its already generated CNF is unaffected.
"""
import hashlib, os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule30_relaxed_records_k as rlk                                  # noqa: E402
_argv, sys.argv = sys.argv, sys.argv[:1]                                # RR parses sys.argv at import
from rule30_records_real_sat import cnf as rr_cnf, check as rr_check    # noqa: E402
sys.argv = _argv
from rule30_cadical_certify import cake, CADICAL                        # noqa: E402


def build(d, L, phase, words):
    nv, cl, row, T = rr_cnf(d, L)
    ph = 1                                                  # RR's first variable is the phase of column 0
    cl = list(cl) + [[ph] if phase == 1 else [-ph]]
    # column 1's variables: RR numbers cells as it meets them; recover them by rebuilding the map
    var, n = {}, [0]

    def v(t, i):
        if (t, i) not in var:
            n[0] += 1
            var[(t, i)] = n[0]
        return var[(t, i)]
    n[0] += 1                                               # the phase variable, as in RR
    for t in range(1, T + 1):
        for i in range(-(T - t), T - t + 1):
            v(t, i); v(t - 1, i - 1); v(t - 1, i); v(t - 1, i + 1)
            n[0] += 1                                       # RR's OR auxiliary
    assert n[0] == nv                                        # duplicated allocation order must still match RR
    assert row == [var[(0, i)] for i in range(-T, T + 1)]
    vis = [var[(t, 1)] for t in range(T) if (t + phase) % 2 == 0 and (t, 1) in var]
    for w in words:
        for s in range(len(vis) - len(w) + 1):
            cl.append([(-vis[s + k] if w[k] == '1' else vis[s + k]) for k in range(len(w))])
    return nv, cl, row, T


def run(d, L, phase, cap, extra=()):
    words = (rlk.load_forbidden('44all') + rlk.load_cuts(0, 40) if phase == 0
             else rlk.load_forbidden('44allp1') + rlk.load_cuts(1, 40)) + list(extra)
    nv, cl, row, T = build(d, L, phase, words)
    base = os.path.join(rlk.DIR, 'exact_d%d_L%d_p%d_x%d' % (d, L, phase, len(extra)))
    text = 'p cnf %d %d\n' % (nv, len(cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl)
    open(base + '.cnf', 'w').write(text)
    sha = hashlib.sha256(text.encode()).hexdigest()
    t0 = time.time()
    r = subprocess.run([CADICAL, '-q', '-t', str(cap), '--lrat', '--no-binary', base + '.cnf', base + '.lrat'],
                       capture_output=True, text=True)
    t1 = time.time()
    verdict = {10: 'SAT', 20: 'UNSAT'}.get(r.returncode, 'UNKNOWN%d' % r.returncode)
    size = os.path.getsize(base + '.lrat') if os.path.exists(base + '.lrat') else 0
    witness = None
    if verdict == 'SAT':
        val = set()
        for line in r.stdout.splitlines():
            if line.startswith('v '):
                val.update(int(x) for x in line[2:].split())
        bits = [1 if x in val else 0 for x in row]
        verdict = 'SAT-WITNESS' if bits[T] == phase and rr_check(bits, T, d, L) else 'SAT-CHECK-FAILED'
        witness = ''.join(map(str, bits))
    elif verdict == 'UNSAT':
        verdict = 'VERIFIED-UNSAT' if cake(base + '.cnf', base + '.lrat') else 'CAKE-FAILED'
    if os.path.exists(base + '.lrat'):
        os.unlink(base + '.lrat')
    print('EXACT d=%d L=%d phase %d (%d words): %s; cnf sha256 %s; solve %.0f s, check %.0f s, lrat %.1f MB'
          % (d, L, phase, len(words), verdict, sha, t1 - t0, time.time() - t1, size / 1e6), flush=True)
    if witness:
        print('EXACT witness row (cells -T .. T at time 0): %s' % witness, flush=True)
    return verdict


if __name__ == '__main__':
    if sys.argv[1] == 'controls':
        run(21, 16, 0, 600)
        run(21, 15, 0, 600)
        run(21, 15, 1, 600)
    else:
        extra = sys.argv[5].split(',') if len(sys.argv) > 5 else ()
        run(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]) if len(sys.argv) > 4 else 14400,
            extra)
