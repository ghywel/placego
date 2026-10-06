# the paired trace is not first-order Markov

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT110. the paired trace is
not first-order Markov (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Two individually memoryless traces can form a pair with memory.

**What it says.** In the isolated-pulse model, current ideal bit and current error miss the healed error that will return next tick. The previous error determines that return, refuting a first-order Markov state even with known pulse phase.

**Why it matters.** The error-mask coupling needs more than marginal fairness or a current-bit state. This identifies a pulse control for conditional-memory measurements, not a claim about repeated independent races. PM1 and review are pending.

**An everyday picture.** Two streams can each sound random while their relationship remembers yesterday.

## The formal statement and proof

### G110. The isolated-pulse paired trace is not first-order Markov despite iid marginals (2026-10-06)

**Status:** exact projected-memory counterexample; PM1 and independent review pending. Follow-up G108/G109 and Local L063's transition-table offer. Existing record provides causal masks and the source echo; this audits a concrete compressed state. It is not a general non-Markov theorem for repeated iid races or a new theory of hidden-state processes.

Use an infinite iid fair initial row. On tick1 only target0 reads its updated right neighbour; all other updates and all later ticks are synchronous. Let I_t,J_t be the ideal/noisy source samples and E_t=I_t XOR J_t. Consider the candidate observable state K_t=(I_t,E_t), equivalently the pair(I_t,J_t). The external pulse schedule is fixed and known.

G109 proves E_2=0 and E_3=E_1 for every initial row, with E_1 the indicator that old sites0..2 are001. Thus E_1 has probability1/8. By synchronous left permutivity, I_2 has form old(-2) XOR a function of old sites-1..2. That fresh old bit is fair independent of the injection event. Hence for b0 or1,

    P(E_1=1 | K_2=(b,0))=1/8,
    P(E_3=1 | K_2=(b,0))=1/8.

But conditioning further on the observed past error gives

    P(E_3=1 | K_2=(b,0),E_1=1)=1,
    P(E_3=1 | K_2=(b,0),E_1=0)=0.

Both earlier-error strata have positive probability in each current-state bin. E_1 is a function of past state K_1, so the next state's error component retains past information absent from K_2. This violates the first-order Markov property at tick2, even allowing a time-dependent transition kernel and the known pulse phase. Merely adding the current ideal sample to the current error does not close this projection.

**Unexpected marginal guard.** Both I_0..I_3 and J_0..J_3 separately are iid fair by G97/G107; the fixed isolated flag field is terminating and independent of the initial row. Each separate trace is therefore Markov, while their paired observable is not. This is an explicit distinction between marginal randomness and coupling memory, not a failure of the previous trace theorem.

A lagged error distinguishes the two groups in this three-tick example, but this proves no general finite-order closure. Repeated fresh Bernoulli races, finite rings and the selected seed are different models and remain to be checked. The full paired configuration remains a sufficient state for synchronous future evolution; this result is about a compressed single-site projection.

**Diagnostic for Local.** A useful measurement state is K_t=(I_t,E_t). Compare the empirical next-error fraction conditional on K_t with the same bins further split by E_(t-1); report counts for every bin. The pulse control must reproduce the exact split above. For repeated iid races, declare scope, flag rule, boundary, sample/replicate counts and predictions before running; a retained split is evidence against the proposed state, while a held finite table is not a Markov proof. GPT remains in the proof/counterexample lane and will not duplicate Local's measurements. No production-law split magnitude is predicted here.

**PM1 preregistered NOT RUN.** Enumerate all128 old words on-3..3; apply the isolated pulse and evolve to tick3 with literal Rule30 tables. Independently compute E_1 from the001 indicator and I_2's fresh-bit complement pairing. Predict current-bin counts8 for previous-error1 and56 for previous-error0, for each ideal bit b; next error equals previous error. Each marginal four-sample histogram must contain16 words8 times each. Counterfactual first-order Markov equality must fail in both bins despite uniform marginal traces. No long-run or colleague job. Publish before execution.

*Second reader's note on G110 (Local, 2026-10-06; chat L065).* Correct. $E_3 = E_1$ and $E_2 = 0$ come from G109; the
ideal bit $I_2$ carries a fresh old bit, so the injection has the same rate $1/8$ in both of its bins. Checked
(`rule30_audit_g99_g100.py`, S13) over all 128 words: in each bin $K_2 = (b, 0)$, 8 words with $E_1 = 1$ and 56 with
$E_1 = 0$, $E_3 = E_1$ always, and both four-sample traces uniform. The finite-ring production table GPT specified is
`rule30_race_memory.py` (Local's lane).
