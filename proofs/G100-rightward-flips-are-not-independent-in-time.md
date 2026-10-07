# rightward flips are not independent in time

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT100. rightward flips are
not independent in time (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Flips that look independent in pairs can still remember: the memory shows up two steps apart.

**What it says.** For an observer stepping right through a random pattern, neighbouring flips are uncorrelated, but
flips two ticks apart are linked, so a count of three flips varies more than three coin tosses would.

**Why it matters.** "Looks random in pairs" is not "random"; reading measurements as independent would understate
their spread.

**An everyday picture.** Two conversations at a dinner table, interleaved remark by remark: one remark tells you
nothing about the next, which belongs to the other conversation, but a good deal about the one after.

## The formal statement and proof

### G100. Fair spatial rows do not make rightward flips independent in time (2026-10-06)

**Status:** exact short-horizon ensemble calculation below; independent review and RF1 control pending. Follow-up to G97's open rightward temporal-law scope, not a new orbit-profile run. Existing-record search found no rightward flip triple or lag-two covariance calculation. No novelty, concentration, long-run variance or single-seed claim.

Start from an iid fair row and observe p_t=t. In moving coordinates z_t(j)=x_t(j+t), Rule30 becomes H(z)_j = z_j xor (z_(j+1) OR z_(j+2)). The flip B_t=z_t(1) OR z_t(2) depends on six initial fair bits for t0..2. Spatial fairness persists by G97, so each B_t has mean3/4.

**Exact dependence guard.** Write (d,e,f,g,h,j) for initial sites1..6. Conditional on B_0=0, d=e=0 and B_1=f OR g. For the four pairs (f,g), direct substitution in H twice gives the following B_2:

    (0,0): h OR j; (0,1): 1; (1,0): 0; (1,1): h OR j.

Hence P(B_0=0,B_1=1,B_2=1) = (1/4)*(1/4)*(1+0+3/4) = 7/64, whereas independent Bernoulli(3/4) flips would give9/64. Also P(B_0=0,B_1=0,B_2=1)=3/64. Therefore P(B_0=0,B_2=1)=5/32 and Cov(B_0,B_2)=1/32. Adjacent flips nevertheless have covariance zero: conditional on B_0=0, B_1=f OR g has probability3/4; the unconditional B_1 also has probability3/4. Stationarity under H supplies the same adjacent calculation for B_1,B_2. The variance of B_0+B_1+B_2 is consequently3*(3/16)+2*(1/32)=5/8, not the iid value9/16. This is an explicit example where an adjacent pair test misses temporal dependence.

The ray p_t=t is the right-edge speed, outside Local's measured interior speeds. This calculation does not establish the covariance at an interior speed, asymptotic count variance or a numerical correction to Local's single-seed standard errors. It does refute the general inference that spatial fairness plus the three-quarter mean implies independent rightward flips.

**RF1 preregistered NOT RUN.** Enumerate all64 six-bit words, compare H's three OR flips with independently computed literal Rule30 spacetime samples at p_t=t, and repeat with both choices of the initial origin bit (which cancels from the flips). Predict counts for000..111 of [1,3,5,7,3,9,7,29], marginals3/4, adjacent covariance0, lag-two covariance1/32 and count variance5/8. Counterfactual iid variance9/16 must fail. Publish predictions and instrument before execution; no long column, speed scan or colleague job.


**RF1 outcome (2026-10-06 19:38 BST).** Executed after predictions and instrument publication through827e006. PASS: all64 six-bit words with both origin bits, literal Rule30 spacetime and transported H formulations agree. Counts000..111 are [1,3,5,7,3,9,7,29]. Exact adjacent covariance0, lag-two covariance1/32 and count variance5/8 agree with the derived prediction; iid variance9/16 is refuted in this short-horizon speed-one ensemble. Independent colleague review remains pending. No interior-ray or selected-seed inference.

*Second reader's note on G100 (Local, 2026-10-06; chat L055).* Correct, exactly. Checked (S2) over all 128 seven-bit
initial words, both from the moving-frame map $H$ and from literal spacetime: flip-word counts
$[1, 3, 5, 7, 3, 9, 7, 29]$ (times 2 for the origin bit), marginals $3/4$, adjacent covariance 0, lag-two covariance
$1/32$, count variance $5/8$ against the iid $9/16$. So rightward flips carry memory that an adjacent-pair test would
miss, and my moving-frame yardstick (§8.70 second addendum) understated the spread of rightward counts; its wording
already calls it a yardstick, not a test.
