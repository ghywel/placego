# first nonlinear pair

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT62. first nonlinear pair
(second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

In Rule 210, the first pair of black squares next to the wall can appear only at a sparse list of even times: 0, 6,
30, 126, ...

**What it says.** Adding column 2's own update to G61, a black pair in columns 1 and 2 can occur only at even times,
and only where the visible signal switches off. For the signal of the initially empty left half those times are 0,
6, 30, 126, and so on.

**Why it matters.** It restricts where Rule 210's non-linear term can act near the wall to a very thin set.

**An everyday picture.** A request-stop bus allowed to stop only at the minutes 0, 6, 30, 126 and so on: the gaps
keep growing, so the stops get ever rarer.

## The formal statement and proof

### G62. Column2's update restricts the first nonlinear pair (2026-10-06)

Continue G61 by imposing column2's even-to-odd update, rather than assuming its freely chosen temporal pair evolves. Retain s_n,d_n,b_n,c_n from G61 and let q_n=x(3,2n). Rule210 gives

    c_n=s_n XOR ((1-b_n)*q_n).

If d_n=1, G61 forces s_n=0,b_n=1. The new equation then forces c_n=0. Thus x(1,2n+1)*x(2,2n+1)=d_n*c_n=0 at every odd time in any full0101 wall orbit. If s_n*b_n=1 at even time, then s_n=b_n=1, so d_n=0 and c_n=1. G61's odd-to-even equation forces s_(n+1)=0. Therefore

    x(1,2n)*x(2,2n)=1 implies (s_n,s_(n+1))=(1,0).

The temporal support of this particular nonlinear gate is confined to effective1-to0 transitions, and its odd-time support is empty. This is necessary for full orbits; it is not a sufficiency statement for a whole right half. In contrast, G61's wall gate tau*x(1) can occur only at odd-time0-to1 transitions. The two neighboring nonlinear sources therefore have distinct allowed timing.

For G26's empty-left stream,1-to0 transitions are n=4^r-1, r>=0, including the special n=0. Hence the pair in columns1-2 can activate only at even times2*(4^r-1)=0,6,30,126,... . The wall's allowed gate times remain4^(r+1)-1=3,15,63,... . These are possible times, not a claim that every such gate fires. G60's fully parity-sparse realization fires neither.

**Unexpected guard.** G61's local tuple(s,d,s_next,b,c)=(1,0,0,1,1) remains compatible with column2's added even update, for either q. Thus deeper compatibility sharpens the support but does not eliminate nonlinear activity at the allowed down-transition gates. No timing restriction on pairs at sites2 or farther right is obtained here, so neither logarithmic gate count nor G59 implies a finite-seed exclusion. This direct Boolean derivation uses the existing rule and G61, with no novelty claim and no new computational experiment.

**Next bounded control, preregistered NOT RUN.** NG1: enumerate all32 initial positive patches(s,b,q,h,z)=x(1..5,2n), evaluate scalar Rule210 updates of columns1-3 at two steps under the imposed wall values0 then1, and check both implications. This is a local Dirichlet-layer check, not a claim that the imposed wall evolves from the patch alone. Compare resulting s,d,b,c with G61; retain the allowed tuple above as a realizable local guard. NG2: compare down-transition positions through4096 effective indices with n=4^r-1 including0. CF: the columns1-2 pair can be black at an odd time under the clock; must fail. A local two-step patch is not an infinite full clock or a finite witness. Independent Local reading requested; next complete these controls before extending farther right.


### G62 controls outcome (2026-10-06)

NG1 passes all32 positive five-cell Dirichlet patches through the two specified updates. All8 patches with an even columns1-2 black pair force the next effective bit0; all32 have no odd pair. The allowed even-pair guard survives in8 patches. NG2 passes4096 indices, with down-transition positions0,3,15,63,255,1023,4095. The odd-pair counterfactual is refuted. Probe: `tests/probes/lexicon/rule30_gpt_pair_support.py`, Python on GPT's Intel host, under1 s.

These are local compatibility controls under the imposed wall, not a full-clock construction or a finite-seed search. No control failed. G62 remains awaiting an independent reader. The pair-specific block is complete; next seek a statement controlling a whole right strip during a constant effective run, rather than extrapolating the first pair's support to all depths.

*Second reader's note on G60, G61 and G62 (Local, 2026-10-06; chat L035).* All three correct. G60: in Rule 90 the
centre at time $2n+1$ is $\bigoplus_j \binom{2n+1}{n-j} v_j$ with coefficient 1 on the newest site, so the recursion is
triangular and defines the full odd-supported seed; the left half is G58's because it depends only on the left cells
and column 0; finite support would contradict G59 for a nonzero periodic wall; the site-1 scope check gives
$a_n = \binom{2n+1}{n} \bmod 2$. G61: the two column-1 updates are $d_n = (1 - s_n)b_n$ and
$s_{n+1} = 1 \oplus (1 - d_n)c_n$, and G26's up-transitions fall at $n = 2^{2r+1} - 1$, odd times $3, 15, 63, \ldots$.
G62: column 2's update $c_n = s_n \oplus (1 - b_n)q_n$ makes every odd columns-1-2 pair impossible and forces
$s_{n+1} = 0$ after an even pair; G26's down-transitions fall at $n = 4^r - 1$ (with $n = 0$). Checked independently
(`rule30_audit_g60_g66.py`): full Rule 210 evolved from the recursion's seed reproduces the wall for 12 periodic
inputs over 120 steps; the G61 and G62 truth tables exhaustively; the transition positions to 5,000.
