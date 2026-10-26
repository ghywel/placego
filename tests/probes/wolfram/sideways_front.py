#!/usr/bin/env python3
"""sideways_front.py: does the reconstruction's forgetting front have a small exact state, and where does its speed come from?
(Local, 2026-10-26, L957; frozen before its first run.)

RUN-ON:   cpu, pure Python 3 (big integers as bitsets), one process.  python3 sideways_front.py > out.txt
COST:     a minute or two; under 200 MB.  CAPS: ulimit -t 900; column cap 14*tau + 400; nothing else is enlarged.
QUESTION: GPT's GC1894 question, taken up by L956: "what exact local state determines the sideways discrepancy transition? Can two
          equal candidate states have different next outcomes?" L955 measured a forgetting front advancing about 0.15 tock per tock
          (finite fits; GC1894's qualifications apply).
If this holds, it changes DQ-009 (the referee's memory) from a fitted slope to a decomposed mechanism; no prize or proof status.

THE SIDEWAYS VIEW (hand derivation, L957). The outward reconstruction x(t,d+1) = x(t+1,d) XOR (x(t,d) OR x(t,d-1)) treats column d as
time and trace time t >= 0 as space, with c_0 = 0 and c_1 = the trace. Two traces differing at one tock tau = 2j+1 give a difference
delta_d(t) = x(t,d) XOR x'(t,d). Exactly, with u = x(t,d), w = x(t,d-1), alpha = delta_d(t), beta = delta_(d-1)(t):
    delta_(d+1)(t) = delta_d(t+1) XOR o(alpha, beta, u, w),
    o = 0 if alpha = beta = 0;  NOT w if (1,0);  NOT u if (0,1);  [u = w] if (1,1)        (the same with x' in place of x).
Consequences, proved by inspection of the formula:
  L1 (one-way): levels >= t evolve as a closed system given the background at levels >= t; nothing below can affect them. A difference
     never rises; it can stay at its level or move down one, and it falls off at t = 0.
  L2 (the top closes): at the top H of supp(delta_d) U supp(delta_(d-1)), delta_d(H+1) = 0, so delta_(d+1)(H) = o(alpha, beta, u, w):
     whether the top level survives one column is decided exactly by those four local bits. No two equal states (alpha, beta, u, w)
     can have different outcomes: GPT's kill test cannot fail for this state; it is a theorem, checked below as a control.
  So the transition closes on four bits. What history can still carry is the BACKGROUND (u, w) as the top sees it. The front's speed
  then decomposes exactly, as section 8.66 decomposed the forward leftward speed 0.246 = 1 - P(heal) E[jump]:
     v = P(the top level vacates in a column) * E[levels dropped | vacate]                       (an identity over a whole run).
  With fair independent background bits, the top pair runs a three-state chain {10, 01, 11} to absorption: from 10 to 11 or 01;
  from 11 to 11 or 01; from 01 to 10 or vacate; each with probability 1/2. The expected columns to vacate from 10 is 6 (hand).

THE TWIN LINK: tock j's influence on k_m is P(delta_(2m+2)(0) = 1); it is near 1/2 while the top is above 0 and 0 once the whole
difference has fallen off. So "tock j is forgotten by step m" is "the top from tau = 2j+1 reaches 0 by column 2m+2", and the front
slope j/m is the top's fall speed v in levels per column.

Record searched (record_find.py, 2026-10-26): "sideways" 271 hits/75 files; "damage spreading" 0; "Lyapunov" 32/15; "0.246" 72/30;
"disturbance" 13/10. Read: RULE30-PRIZE.md 8.30 and 8.66 (the forward leftward speed and its heal/jump identity; GC295's scope).

PREDICTIONS, written 2026-10-26 before the first run.
Controls (must hold):
  S0  the sideways columns reproduce forward evolution: for 50 random 40-bit black-tick traces the start F_d = c_d(0) evolved forward
      gives back the trace at every t < 40.
  S1  L2 at every column of every real run: the top level's survival equals o(alpha, beta, u, w).
  S2  the identity v = P(vacate) * E[drop] holds within 0.005 for each tau (pooled over its runs).
  S3  Monte Carlo of tock j's influence on k_24 (delta_50(0), 20,000 random traces) reproduces tock_twins.c: j = 0 gives 0.0025 and
      j = 2 gives 0.1666, each within 3 standard errors.
Blind:
  PS1 real fall speed v_tau = tau / median(death column) lies in [0.12, 0.18] for tau = 101, 201, 401, and the three differ by <= 0.03
      (a linear front, if it holds, is finite evidence only).
  PS2 the coin model's v lies in [0.12, 0.25] (hand bracket: about one level per six columns if each vacate drops one level).
  PS3 (the door) coin v at tau = 401 is within 15% of real v. Counterfactual: more than 25% apart, so the background as the top sees
      it is not a fair coin and history acts through it (as in 8.66, where P(heal) was 0.41, not 1/2).
  PS4 the real background at the top, conditioned on the top state, is coin-like: P(w = 0 | 10), P(u = 0 | 01) and P(u = w | 11) each in
      [0.45, 0.55] (pooled, tau >= 101).
  PU  (unexpected check: the ticks sit at even trace times) the top spends a fraction in [0.45, 0.55] of its columns on even levels.

OUTCOME, 2026-10-26 (single run 10:32 GMT, 1.6 s, 12 MB max RSS; frozen sha256 f35079c5..., commit 99be4a30; raw out.txt sha256
bf40621b..., cited/sideways-front-20261026/). Added after the run. S0-S3 PASS (S3: 0.0027 and 0.1694). PS1 HELD (v = 0.1537, 0.1542,
0.1556 at tau = 101, 201, 401; 0.1555 at 51). PS2 HELD (coin 0.2207). PS3 FAILED, counterfactual MET (gap 0.418). PS4 FAILED: P(w=0|10)
= 1.0000 exactly (160,230 cases), which is a lemma, proved by hand in reports/rule30-sideways-front.md (L3: state 10 always
survives); P(u=0|01) = 0.6154, the conditional density of black just above the top (L4); P(u=w|11) = 0.4824. PU HELD (0.5003).
"""
import random, statistics, sys

def o_bits(al, be, u, w, mask):
    nu, nw = ~u & mask, ~w & mask
    return ((al & ~be & nw) | (~al & be & nu) | (al & be & ~(u ^ w))) & mask

def trace(rng, L):
    a = 0
    for t in range(0, L, 2): a |= 1 << t
    for t in range(1, L, 2):
        if rng.getrandbits(1): a |= 1 << t
    return a

def forward_check(rng):
    for _ in range(50):
        L = 40; a = trace(rng, L)
        cm1, c, F = 0, a, [0] * (L + 2)
        F[1] = c & 1
        for d in range(1, L):
            cm1, c = c, (c >> 1) ^ (c | cm1); F[d + 1] = c & 1
        row = F[:] + [0] * (L + 4)
        for t in range(L):
            if row[1] != (a >> t) & 1: return False
            row = [0] + [row[d + 1] ^ (row[d] | row[d - 1]) for d in range(1, len(row) - 1)] + [0]
    return True

def real_run(rng, tau):
    cap = 14 * tau + 400; L = tau + cap + 8
    a = trace(rng, L); b = a ^ (1 << tau)
    mask = (1 << (tau + 2)) - 1
    cm1, c, dm1, dc = 0, a, 0, 0
    pm1, p = 0, b
    dc = (c ^ p) & mask; dm1 = 0
    stats = {"cols": 0, "vac": 0, "drop": 0, "s1": True, "st": {"10": [0, 0], "01": [0, 0], "11": [0, 0]}, "even": 0}
    H0 = tau
    for d in range(1, cap):
        un = dc | dm1
        if un == 0: return d, stats
        H = un.bit_length() - 1
        al, be = (dc >> H) & 1, (dm1 >> H) & 1
        u, w = (c >> H) & 1, (cm1 >> H) & 1
        cn = (c >> 1) ^ (c | cm1); pn = (p >> 1) ^ (p | pm1)
        dn = (cn ^ pn) & mask
        pred = (1 - w) if (al, be) == (1, 0) else (1 - u) if (al, be) == (0, 1) else int(u == w)
        if ((dn >> H) & 1) != pred: stats["s1"] = False
        key = f"{al}{be}"
        if key == "10": stats["st"][key][0] += 1; stats["st"][key][1] += (w == 0)
        elif key == "01": stats["st"][key][0] += 1; stats["st"][key][1] += (u == 0)
        else: stats["st"][key][0] += 1; stats["st"][key][1] += (u == w)
        stats["cols"] += 1; stats["even"] += (H % 2 == 0)
        un2 = dn | dc
        H2 = un2.bit_length() - 1 if un2 else -1
        if H2 < H: stats["vac"] += 1; stats["drop"] += H - H2
        cm1, c, pm1, p, dm1, dc = c, cn, p, pn, dc, dn
    return None, stats

def coin_run(rng, tau):
    cap = 14 * tau + 400; mask = (1 << (tau + 2)) - 1
    dm1, dc = 0, 1 << tau          # column 1 differs at tau, column 0 never
    wbg = 0                        # background of column 0 is white
    ubg = rng.getrandbits(tau + 2)
    for d in range(1, cap):
        if dc | dm1 == 0: return d
        on = o_bits(dc, dm1, ubg, wbg, mask)
        dn = ((dc >> 1) ^ on) & mask
        dm1, dc = dc, dn
        wbg, ubg = ubg, rng.getrandbits(tau + 2)
    return None

def main():
    rng = random.Random(20261026)
    fails = 0
    s0 = forward_check(rng); print("S0 sideways columns reproduce forward evolution:", "PASS" if s0 else "FAIL"); fails += not s0
    # S3
    for j, want in ((0, 0.0025), (2, 0.1666)):
        N, hit = 20000, 0
        for _ in range(N):
            a = trace(rng, 50); b = a ^ (1 << (2 * j + 1))
            cm1, c, pm1, p = 0, a, 0, b
            for d in range(1, 50):
                cm1, c = c, (c >> 1) ^ (c | cm1); pm1, p = p, (p >> 1) ^ (p | pm1)
            hit += (c ^ p) & 1
        q = hit / N; se = (want * (1 - want) / N) ** 0.5; ok = abs(q - want) <= 3 * se
        print(f"S3 influence of tock {j} on k_24: {q:.4f} (want {want}, 3 SE {3*se:.4f}): {'PASS' if ok else 'FAIL'}"); fails += not ok
    real_v, coin_v, pooled = {}, {}, {"10": [0, 0], "01": [0, 0], "11": [0, 0]}
    even = cols = 0; s1 = True
    for tau, N in ((51, 400), (101, 300), (201, 200), (401, 100)):
        deaths, vac, drop, cl = [], 0, 0, 0
        for _ in range(N):
            D, st = real_run(rng, tau)
            if D is None: print(f"CENSORED real run at tau {tau}"); fails += 1; continue
            deaths.append(D); vac += st["vac"]; drop += st["drop"]; cl += st["cols"]; s1 &= st["s1"]
            if tau >= 101:
                for k in pooled: pooled[k][0] += st["st"][k][0]; pooled[k][1] += st["st"][k][1]
                even += st["even"]; cols += st["cols"]
        v = tau / statistics.median(deaths); real_v[tau] = v
        ident = (vac / cl) * (drop / vac); vrun = (tau + 1) / statistics.mean(deaths)
        ok2 = abs(ident - (tau + 1) / statistics.mean([dd - 1 for dd in deaths])) <= 0.005
        print(f"REAL tau={tau} N={len(deaths)} median death col {statistics.median(deaths)} v={v:.4f} | P(vacate)={vac/cl:.4f} "
              f"E[drop]={drop/vac:.4f} product={ident:.4f} vs (tau+1)/mean(D-1)={(tau+1)/statistics.mean([dd-1 for dd in deaths]):.4f}: S2 {'PASS' if ok2 else 'FAIL'}")
        fails += not ok2
        cd = [coin_run(rng, tau) for _ in range(N)]
        if any(x is None for x in cd): print(f"CENSORED coin run at tau {tau}"); fails += 1; cd = [x for x in cd if x]
        coin_v[tau] = tau / statistics.median(cd)
        print(f"COIN tau={tau} median death col {statistics.median(cd)} v={coin_v[tau]:.4f}")
    print("S1 top-level survival equals o(alpha,beta,u,w) at every column:", "PASS" if s1 else "FAIL"); fails += not s1
    vs = [real_v[t] for t in (101, 201, 401)]
    p1 = all(0.12 <= x <= 0.18 for x in vs) and max(vs) - min(vs) <= 0.03
    print(f"PS1 real v at 101/201/401 = {vs[0]:.4f} {vs[1]:.4f} {vs[2]:.4f}: {'HELD' if p1 else 'FAILED'}")
    p2 = 0.12 <= coin_v[401] <= 0.25
    print(f"PS2 coin v at 401 = {coin_v[401]:.4f} in [0.12,0.25]: {'HELD' if p2 else 'FAILED'}")
    rel = abs(coin_v[401] - real_v[401]) / real_v[401]
    print(f"PS3 coin vs real at 401: relative gap {rel:.3f} (<= 0.15): {'HELD' if rel <= 0.15 else 'FAILED'}; counterfactual (> 0.25): {'MET' if rel > 0.25 else 'not met'}")
    fr = {k: pooled[k][1] / pooled[k][0] for k in pooled}
    p4 = all(0.45 <= x <= 0.55 for x in fr.values())
    print(f"PS4 top background: P(w=0|10)={fr['10']:.4f} P(u=0|01)={fr['01']:.4f} P(u=w|11)={fr['11']:.4f} "
          f"(counts {pooled['10'][0]}, {pooled['01'][0]}, {pooled['11'][0]}): {'HELD' if p4 else 'FAILED'}")
    pe = even / cols
    print(f"PU top on even levels: {pe:.4f} in [0.45,0.55]: {'HELD' if 0.45 <= pe <= 0.55 else 'FAILED'}")
    print(f"CONTROLS: {'ALL PASS' if fails == 0 else 'FAIL'} ({fails} failures)")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
