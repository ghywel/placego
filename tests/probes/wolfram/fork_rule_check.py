"""fork_rule_check.py: the branch law at a fork, checked (CL749). At the first fork j = 53,207 of the seed's strip A0, with
the configuration settled through the fork's child, a perturbation at tick T0 (a flip on wheel W in {53206, 53207, 53208})
blackens the fork wheel transiently or not at all. Law: if the fork wheel is black at some tick after T0, let tau* be the
last such tick; the configuration ends on A0 iff the A0 child word c = w_(53208) is white at tau* + 1. If the fork wheel
is never black, the child's complement persists and the configuration ends on the other branch. The script evolves the
seed to T0, flips the bit, follows the fork wheel for up to 64 ticks to find tau*, reads c(tau* + 1) from A0's cycle
(the seed is on A0 at phase 0, so the strip's row at tick t is cyc[t mod 32]), predicts the strip, and compares with
the observed outcomes of chink.py (chink_fork.out). The law as written assumes wheel j-1 aligned at tau*; the general
form d = not a_(j-1)(tau*) xor c(tau*+1) (CL749 addendum 1, a post-hoc refinement) reads a_(j-1)(tau*) off the run. Usage: python3 fork_rule_check.py ROWSDIR OBSERVED.out"""
import sys, re
ROWS = sys.argv[1]; OBS = sys.argv[2]
K = 165750; MASK = (1 << K) - 1; P = 32; J = 53207
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
A0 = int.from_bytes(open(f"{ROWS}/A0.bin", 'rb').read(), 'little') & MASK
cyc = [A0]
for _ in range(P): cyc.append(step(cyc[-1]))
assert cyc[P] == A0; cyc = cyc[:P]
def c_word(t): return (cyc[t % P] >> (J + 1)) & 1
def w_word(t): return (cyc[t % P] >> (J - 1)) & 1
assert all(((cyc[t] >> J) & 1) == 0 for t in range(P)), "the fork wheel is white on the strip"
assert all(((cyc[t] >> (J - 2)) & 1) == ((cyc[t] >> (J - 1)) & 1) for t in range(P)), "the two words below the fork are equal"
obs = {}
for b in re.split(r'(?=^chink on wheel)', open(OBS).read(), flags=re.M):
    m = re.match(r'chink on wheel (\d+) at tick (\d+)', b); s = re.search(r'settles on (\S+) at', b)
    if m and s: obs[(int(m.group(1)), int(m.group(2)))] = s.group(1)
x = 1; t = 0
T0s = sorted(set(t0 for _, t0 in obs))
while t < T0s[0]: x = step(x); t += 1
rows = {}
for t0 in T0s:
    while t < t0: x = step(x); t += 1
    rows[t0] = x
ok = 0; okg = 0; n = 0
print("W      T0     fork wheel black at ticks (after T0)   tau*    c(tau*+1)  predicted      observed")
for (W, t0) in sorted(obs):
    y = rows[t0] ^ (1 << W); blacks = []; lower = {}
    for k in range(0, 64):
        if (y >> J) & 1: blacks.append(t0 + k)
        lower[t0 + k] = (y >> (J - 1)) & 1          # the configuration's own wheel j-1, which may itself be an error
        y = step(y)
    if blacks:
        tau = blacks[-1]; cv = c_word(tau + 1); pred = "A0" if cv == 0 else "A0.53207"
        a1 = lower[tau]; gen = (1 - a1) ^ cv; pred_gen = "A0" if gen == 0 else "A0.53207"    # the general law: d = not a_(j-1)(tau*) xor c(tau*+1)
    else:
        tau = None; cv = None; pred = "A0.53207"; a1 = None; pred_gen = "A0.53207"
    n += 1; ok += (pred == obs[(W, t0)]); okg += (pred_gen == obs[(W, t0)])
    print(f"{W}  {t0}  {[b - t0 for b in blacks] if blacks else 'never'!s:36s}  {tau!s:6s}  {cv!s:9s}  {pred:13s}  {obs[(W, t0)]:9s}  {'ok' if pred == obs[(W, t0)] else 'MISS'}   a_(j-1)(tau*) {a1!s:4s} general {pred_gen:9s} {'ok' if pred_gen == obs[(W, t0)] else 'MISS'}")
print(f"the law as written (premise: wheel j-1 aligned at tau*) reproduces {ok} of {n}; the general law d = not a_(j-1)(tau*) xor c(tau*+1) reproduces {okg} of {n}")
print("the A0 child word c over one period: " + "".join(str(c_word(t)) for t in range(P)) + "; w: " + "".join(str(w_word(t)) for t in range(P)))
