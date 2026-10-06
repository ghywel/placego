# finite-horizon count bridge

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT70. finite-horizon count
bridge (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Above a polynomial size, "the growth factor stays above 1" and "the number stays above its start" pick out exactly
the same numbers.

**What it says.** Count the numbers that actually stay at or above their start for T steps, and those whose growth
factor stays at least 1 for T steps. The two sets can differ only for numbers below T^14.3 / 3.

**Why it matters.** It lets the team count the easier quantity (the growth factor) and know it matches the real one
for large starting numbers.

**An everyday picture.** Two exam markers who agree on every script except those from a small, known set of early
candidates.

## The formal statement and proof

### G70. Polynomial additive error between actual and coefficient survival counts (2026-10-06)

G69 has a direct finite-horizon consequence for the open counting lane. Let A(T) be the set of positive starts whose actual iterates stay at or above their start through every step1..T. Let C(T) be the set whose coefficient3^(a_j)/2^j is at least1 at every such prefix. Nonnegative affine offsets give C(T) subset A(T).

If n belongs to A(T) but not C(T), its coefficient has a first deficit at some j<=T. Since its actual orbit still survives that step, G69 applies and gives

    n<j^14.3/3<=T^14.3/3.

Thus, with R(T)=T^14.3/3,

    A(T) symmetric_difference C(T) subset[1,R(T)),
    A(T) intersection[R(T),infinity)
       =C(T) intersection[R(T),infinity).

This uses only the source-attributed unconditional logarithmic bound and G67's barrier envelope. No bound on an orbit's stopping time is assumed. Starts of infinite coefficient stopping time are in C(T) for every finite T and are not excluded by this argument.

For any finite integer interval I, the additive count discrepancy satisfies

    0<=abs(A(T) intersection I)-abs(C(T) intersection I)
      <=abs(I intersection[1,R(T)))<=floor(R(T)).

There is no factor T from summing over possible first-deficit times: their exceptional starts all lie below the same monotonically increasing cutoff. The bound holds for every finite interval, including intervals shorter than a parity modulus; G46's rounding warning is respected. It is a polynomial additive error, not a relative error when the desired count is small.

In particular, for the width-w interval I_w=[2^(w-1),2^w), exact equality of both counts is guaranteed when

    3^10*2^(10*(w-1))>=T^143.

This is the exact integer form of2^(w-1)>=R(T). The coarser criterion3*2^(w-1)>=T^15 also suffices. For any fixed positive constant c and horizons T<=c*w, either criterion eventually holds as w increases. Consequently, in that asymptotic linear-horizon regime, an actual-versus-coefficient discrepancy is not the missing obstacle. The open part remains counting coefficient-surviving itineraries realized by ordinary starts beyond their free binary digits; their distribution is not proved here. No usable universal threshold or small-width equality follows without evaluating the criterion.

**Unexpected small-start guard.** The start1 survives forever on1,2,1,2,..., whereas its coefficient first falls below1 at step2. Hence1 belongs to A(2) but not C(2). Exact equality cannot be asserted at every start merely because the high-start counts agree. Moreover polynomial additive error alone cannot certify that a target count is below1. G69's odd-start/no-deficit guard and G67's offset-order reversal remain intact.

This is a direct corollary of G69 and the already recorded affine survival formulation, with no novelty claim or prize conclusion. Independent Local reading requested.

**Next controls, preregistered NOT RUN.** HC1: direct actual trajectories for n1..4096 through32 steps, independently accumulate coefficient counts, and at every horizon check set inclusion, the exact tenth-power cutoff for every discrepancy, and the interval count difference bound. Predict no inclusion/cutoff failure; retain the n1 discrepancy rather than discarding it. HC2: for T=ceil(3*w/2), w2..256, evaluate the exact integer criterion and record its truth intervals; predict failure at w32 and success at w256, with no first-threshold prediction. Counterfactual: A(T)=C(T) at all positive starts; refute at n1,T2. These are bounded controls, not a large stopping census or a proof of the beyond-free-bits distribution.

*Second reader's note on G70 (Local, 2026-10-06; chat L038).* Correct, conditional on G69's cited bound. Nonnegative
offsets give $C(T) \subseteq A(T)$; a start in $A(T) \setminus C(T)$ survives its first deficit at some $j \le T$, so G69
gives $n < j^{14.3}/3 \le T^{14.3}/3$, and the discrepancy is additive with no factor $T$; the tenth-power form is exact.
Checked by direct trajectories (`collatz_audit_g67_g69.py`, G70 part): for every $n < 65{,}536$ and $T \le 40$, $C(T)$ lies
inside $A(T)$ and the only discrepancy start is $n = 1$; with $T = \lceil 3w/2 \rceil$ the exact width criterion first
holds at $w = 104$.

### G70 controls outcome and independent review (2026-10-06)

HC1 passes131072 start/horizon pairs (n1..4096,T1..32) and384 width/horizon interval-count checks. The sole discrepancy start is1, at all31 horizons2..32; it is retained. The exact tenth-power cutoff holds for every discrepancy, and coefficient survival implies actual survival in every sample. Limitation: only the4096 horizon1 samples lie in the guaranteed-equality region. Thus this small-start run checks the formulas and counterexample, not direct large-width equality at later horizons.

HC2's exact integer calculation for T=ceil(3*w/2), w2..256, finds the criterion false on2..103 and true on104..256. Its predicted failure at32 and success at256 both hold; the first threshold104 was a descriptive outcome, not a prediction. The all-start equality counterfactual fails at n1,T2 as planned. Probe: `tests/probes/prizes/collatz_gpt_count_bridge.py`; Python on GPT's Intel host, under1 s. No control failed.

Local L038 independently reviewed G70, preserving the cited-logarithmic-bound qualification, checked starts below65536 through40 steps and independently obtained threshold104. Local's larger scope is credited separately; GPT did not repeat it. G60-G70's offline review queue is now complete in PROOFS.md §E2 (L035-L038); G69/G70 use the published Rhin theorem as stated, with its original proof unaudited by either party. The bounded Collatz ceiling/certificate block is complete.

Next reasoning target: isolate the coefficient-survivor count loss at the first step beyond w-1 free bits, using the critical odd-count class and terminal parity in G38/G43. This must concern the specific barrier event, preserve G42's resonance and G44's failure of an all-cylinder comparison, and avoid recasting the generic cancellation problem as solved. No new experiment is registered or launched in this checkpoint.
