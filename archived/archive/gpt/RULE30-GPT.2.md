# RULE30-GPT, volume 2: G96 to G189 (2026-10-06 to 2026-10-07)

*A frozen volume of [RULE30-GPT.md](../../RULE30-GPT.md), rotated out of it unchanged on 2026-10-22 in the documentation spring clean. New entries go in the live file; the list of volumes is at its top.*

## G96. Fixed-cell change and moving-frame change are different observables (2026-10-06)

Follow the owner's temporal-instrument origin and Local's §8.70. For a binary history x_t(i), define Qx_t(i) = x_t(i+1), time shift Sx_t(i) = x_(t+1)(i), and, for fixed integer v,

    D_v = 1 + S*Q^v over GF(2),
    (D_v x)_t(i) = x_(t+1)(i+v) xor x_t(i).

D_0 is the fixed-cell XOR change. For x_t(i) = w(i-v*t), D_v x is zero everywhere, regardless of w; D_0 need not be zero. This is a generic exact-translation history, not a claimed Rule 30 solution. The dyadic identity is

    D_v^(2^k) = 1 + S^(2^k)*Q^(v*2^k),

by repeated squaring of the single linear operator S*Q^v in characteristic two. It compares cells along the same constant-speed worldline. No real-valued acceleration, physical unit, feature identity or noise model is asserted.

For an actual Rule 30 orbit with global map F, pull back to z_t(j) = x_t(j+v*t). Translation covariance gives

    z_(t+1) = Q^v*F(z_t),
    z_(t+1) xor z_t = Q^v*F(z_t) xor z_t.

Proof: at site j, x_(t+1)(j+v*(t+1)) equals F(x_t) at that site; replacing x_t(i) by z_t(i-v*t) gives F(z_t)(j+v). This is a change of coordinates, without treating the update rule as linear. At v = 0, §8.70 supplies F(x) xor x = R210(x).

**Unexpected derivative-dynamics guard.** Write u_t = F(x_t) xor x_t = R210(x_t). Its next value is R210(F(x_t)), not in general R210(u_t). For a single black cell at site 0, x_1 has black sites {-1,0,1}, so u_0 has {-1,1}. The next Rule 30 row has {-2,-1,2}, giving u_1 = {-2,0,1,2}. But applying Rule 210 to u_0 gives {-2,2}. The shortcut that the velocity field itself evolves by Rule 210 fails at sites 0 and 1. This clarifies the scope of the correct identity in §8.70; that section is not being accused of claiming the shortcut.

**Transport-versus-acceleration guard.** In the generic translating pulse x_t(i) = 1 exactly when i = t, the tracked position p_t = t has numerical velocity 1 and acceleration and jerk zero. At fixed site 0 the first three samples are 1,0,0: its second real finite difference is 1, and its second GF(2) difference is also 1. Along i = t every sample is 1, with zero differences. Thus fixed-cell second differences can reflect passage of a constant-speed pattern, not acceleration of that pattern. The example is a scope guard, not Rule 30 data or a PIV validation.

**MC1-MC2 preregistered NOT RUN.** MC1: every binary ring of widths 3 to 8, integer frames v = -1,0,1, compare literal Rule30 truth-table updates with both the transported update and moving-difference identities; separately require the v = 0 Rule210 identity. MC2: independently evolve the finite single-black-cell guard using padded direct truth tables, and verify the fixed/tracked pulse differences and dyadic worldline identity through lag 8. Counterfactual that u evolves by Rule210 must fail at the stated sites. No centre-column rerun, shader edit or Local complexity job. Existing-record search found §8.70's fixed-cell identity but no moving-frame audit or claimed autonomous derivative law. Elementary shift algebra and the recorded truth tables; no novelty or prize claim. The next question is which coherent structures and phase coordinates justify a tracked observable in actual Rule30 dynamics.

Probe: `tests/probes/rule30_gpt_moving_frame.py`. Independent Local reading requested.


**MC1-MC2 outcome (2026-10-06 19:16 BST).** Executed only after preregistration was published at e2c6a02. MC1 PASS: 504 ring rows and 1512 moving-frame cases. MC2 PASS: the padded derivative-dynamics guard and 168 dyadic worldline checks. The autonomous Rule210-change-field counterfactual fails at sites 0 and 1, as predicted; the tracked pulse has zero acceleration while its fixed-cell second difference is one. Finite controls support the implementation and examples, not an orbit-distribution or prize claim. Independent review remains pending.

### G97. The moving-frame flip prediction under a fair spatial ensemble (2026-10-06)

**Status:** proved below for iid fair initial rows; independent review and finite controls pending. Not a theorem about the single-black-cell orbit. Reply to Local L050 and G086. Existing record: C.5 and RULE30-PRIZE.md §8.68 already use invariance of the uniform spatial measure; Local supplies the right-step OR identity in §8.70. No novelty claim.

**Proposition.** Start Rule30 on an iid fair bi-infinite row. For any deterministic observer positions p_t with increments in {-1,0,1}, the expected number of XOR flips in N steps is N/2 + N_right/4, where N_right counts increments +1. No temporal independence is assumed.

**Spatial-law proof.** For any output block of k cells, its k+2 input cells are fair. Fix the two rightmost input bits. Given the output block, solve the other k input bits uniquely from right to left using y_i = x_(i-1) xor (x_i OR x_(i+1)). Every output block has exactly four preimages and hence probability 2^(-k). Every finite output block is therefore iid fair. Induction gives that spatial law at each time. This is a direct counting proof of the previously used invariance.

**Flip proof.** At observer site i, abbreviate a=x_(i-2), b=x_(i-1), c=x_i, d=x_(i+1), e=x_(i+2). The next sampled value XOR the current c is:

    right step: d OR e;
    stay: b xor (c OR d) xor c;
    left step: a xor (b AND NOT c).

The right expression has probability 3/4 under the fair spatial law. Each other expression includes a fair bit independent of the remaining expression, giving probability 1/2. Linearity of expectation then proves the claim, without any assertion that successive flips are independent. For p_t=floor(v*t), 0<=v<=1, N_right=floor(v*N), so the expected flip fraction is 1/2 + floor(v*N)/(4*N). For -1<=v<=0 it is exactly 1/2.

**Unexpected scope guard.** From the deterministic all-zero row every observed flip is zero, including every right step; from the all-one row the first right flip is one. Thus the exact right-step identity alone does not force a three-quarter probability. Nor does the ensemble expectation establish a variance, concentration, almost-sure time frequency or the distribution of the selected single-seed orbit. Those require separate arguments. In particular it does not validate an iid standard-error estimate for Local's temporal samples. The observer here is predetermined, not adaptively tracking features from the random row.

**SC1-SC2 preregistered NOT RUN.** SC1: enumerate all 2^(k+2) input words for k=1..8 using the literal Rule30 truth table; require exactly four preimages of each k-bit output word. SC2: enumerate all 32 five-bit neighbourhoods with literal updates at observer increments -1,0,+1; require 16,16,24 flips respectively, and independently require the three Boolean identities above. Retain the all-zero/all-one guards. These are tiny local controls, not a rerun of Local's 41 rays. Predictions must be published before execution.


**SC1-SC2 outcome (2026-10-06 19:20 BST).** Executed after predictions and instrument were published at a233f59. SC1 PASS: 2040 input words over widths 1..8, exactly four preimages per output word. SC2 PASS: all 32 five-bit neighbourhoods; left/stay/right flip counts 16,16,24. The constant-row scope guards pass. These local controls do not establish any single-seed frequency or temporal variance. Independent review remains pending.

**Corollary: temporal independence in the non-rightward fair-ensemble case.** If the observer is deterministic and p_(t+1)<=p_t for every t, its sampled values s_t=x_t(p_t) are iid fair, and its successive XOR flips are iid fair as well. In particular this applies to floor(v*t) for -1<=v<=0. It remains a statement about the random initial-row ensemble.

**Proof.** The t-step output x_t(p_t) is left-permutive in the leftmost initial input at L_t=p_t-t: it has form x_0(L_t) xor g_t of the other initial inputs. Induct on t in the Rule30 update: only the left child contains that leftmost input, and its coefficient remains one. Every earlier sampled value has a cone whose left endpoint L_s is strictly greater than L_t, because p_t<=p_s and t>s. Thus no earlier sample uses x_0(L_t). Conditional on all initial bits other than this fresh fair bit, the current sample is fair and the earlier samples are fixed. This proves independence from the entire earlier sample vector. Induction proves iid sampled values. Any N prescribed consecutive flip values have exactly two preimages among the 2^(N+1) equally likely sample vectors (choose s_0 and reconstruct); hence flip vectors are uniform and independent, with count variance N/4. No analogous independence is asserted for rightward frames.

**SC3 preregistered NOT RUN.** For all observer increment words over {-1,0} of lengths 1..4, enumerate every initial word on the union of their finite cones and evolve by a padded literal Rule30 truth table, using only cells with their complete cone present. Require each sampled word to have equal multiplicity and each flip word twice that multiplicity. Compare the exact flip-count first and second moments to N/2 and variance N/4. Unexpected guard: with increments +1 for one step, flip probability must instead be 3/4, refuting unrestricted fair-flip independence. No Local profile rerun. Publish this added prediction before execution.


**SC3 outcome (2026-10-06 19:27 BST).** Ran only after the added prediction and instrument were published at 5bb1aac. PASS: 30 left/stay observer paths, 9360 initial words, uniform sampled and flip vectors, and exact mean N/2 and variance N/4 on every path. The unexpected right-step guard gives 3/4 rather than 1/2, as predicted. These finite controls support G97's corollary; the proof uses the fresh initial left bit and does not transfer to the single-seed history. G98's DC1-DC2 remain NOT RUN.

### G98. Clock reparametrization, lattice diamonds and background-dependent fronts (2026-10-06)

**Status:** elementary scope proofs and counterexamples; independent review pending. Reply to Local L051 and CONSTELLATION rows 18/19. No physical time-dilation, Lorentz-invariance or prize claim. Prior-art check recorded in PRIOR-ART.md; no external theorem imported.

**Global-clock proposition.** For a synchronous deterministic map F with states x_n=F^n(x_0), choose any strictly increasing, unbounded tick-completion times T_n. Between completions hold the state at x_n. Every observable depending only on the ordered states is unchanged by the choice of T_n. Proof: neither the recurrence nor its ordered state sequence contains T_n. Durations can affect an observer given an additional physical clock or time-dependent inputs; they are invisible only to the stated state-sequence observables. This makes a precise version of the unequal-tick idea, without identifying elapsed time with computational complexity. A scalar cone simulation uses order n cells per row, but that implementation cost does not prove a lower bound for all ways of computing the nth centre bit.

**Continuum-diamond proposition.** Let a,b>0 be assumed constant left/right cone speeds. Between events (0,0) and (T,X), with -a*T<=X<=b*T, the continuum diamond has area

    A = (b*T-X)*(X+a*T)/(a+b).

Proof: put u=b*s-y and w=y+a*s. The diamond is the rectangle 0<=u<=b*T-X, 0<=w<=X+a*T. The absolute Jacobian of (s,y) to (u,w) is a+b. For a=b=1 this gives (T²-X²)/2. At fixed T the largest area occurs at X/T=(b-a)/2. Setting a=0.246, b=1 therefore gives 0.377, but only inside this assumed geometric model; it is not an established preferred frame of Rule30. A square root of normalized area is a constructed proxy, not a derived physical clock.

**Unexpected discrete-count guard.** On the ordinary integer event grid with speed-one edges, the inclusive diamond count is exactly

    sum over s=0..T of max(0, min(s,X+T-s)-max(-s,X-T+s)+1).

At T=2,X=0 the row counts are 1,3,1, total 5; continuum area is 2. Thus CONSTELLATION row18's exact number-of-events wording needs correction. Boundary conventions and event density must be specified before comparing counts with continuum volumes. For a fixed positive-speed cone, lattice counts have a boundary-order correction, not exact equality with area.

**Background guard.** Compare Rule30 started with a single black cell at zero against the all-zero orbit. The black support's leftmost site is -t at every t: the cell just left of the previous leftmost black has input100, hence becomes black; no cell farther left can turn black because input000 remains zero. Thus a disturbance propagates left at speed1 on this background. The measured approximately0.246 front speed on another background is not a universal causal bound. The symmetric radius-one dependency graph and a measured state-dependent damage front are different objects. Substituting the latter into a causal diamond requires a separate effective-cone model and validation.

**Unequal local-clock guard.** Individual in-place Rule30 updates need not commute. Start with one black cell at site1 and all others zero. Update site0 then site1: the final black set is {0}. Reverse those two updates: the final black set is {0,1}. Both orders update each selected site exactly once; the difference is not a change in global tick duration. This counterexample concerns raw in-place updates, not impossibility of asynchronous simulations with extra state or buffering.

**DC1-DC2 preregistered NOT RUN.** DC1: for integer T=0..12 and |X|<=T, count diamond grid points independently by path reachability and by the row-interval formula; retain T2,X0's five-versus-two guard. DC2: direct truth-table single-seed evolution through12 ticks must have leftmost support -t; two explicit local-update orders must give the sets above. These are bounded guards, not a new damage-speed measurement or asynchronous statistical job. Publish predictions before execution.


**DC1-DC2 outcome (2026-10-06 19:31 BST).** Ran after the predictions at5bb1aac and instrument publication through806cfec. DC1 PASS: 169 integer diamonds, with independent path reachability matching the row-interval formula. The five-versus-two count/area guard passes. DC2 PASS: seed left edge -t through12 and the two update orders giving {0} versus {0,1}. Local's L052 review independently checks larger finite ranges. These controls validate the recorded guards, not an effective physical metric.

### G99. Versioned dependency evaluation preserves logical time (2026-10-06)

**Status:** elementary finite-dependency proof; independent review and controls pending. Follow-up to G98, Local L052 and CONSTELLATION row19. The asynchronous-simulation prior art in PRIOR-ART.md uses additional state; this is a direct scheduling statement, not a new simulator or universality result.

**Proposition.** To compute x_N(0), keep immutable values indexed by (i,k) for 0<=k<=N and |i|<=N-k. Initially store x_0(i) for -N<=i<=N. A noninitial node (i,k) becomes ready only when its three parents (i-1,k-1), (i,k-1), (i+1,k-1) are stored. Evaluate it using the original local rule. Every schedule that eventually evaluates all these nodes and only evaluates ready nodes produces exactly the synchronous values, whatever the physical delays or order of independent ready nodes.

**Proof.** All parents of a node lie in the stated triangle. Generation0 is identical to the original data. By induction on k, every parent of a generation-k node has its synchronous value, so evaluating the deterministic rule produces x_k(i). This holds whenever that node is evaluated, independently of intervening work elsewhere. The finite graph is acyclic because each dependency lowers k; every complete topological order is therefore valid. Unbounded physical delays or lack of eventual completion are excluded explicitly.

There are (N+1)² stored nodes in this full cone, including initial nodes, and a longest chain of N update nodes. Those are costs/depths of this explicit one-step dependency graph, not lower bounds against every algorithm for the centre bit. Generation labels are logical time. The theorem supplies no physical time dilation, uniform physical signal speed, memory-optimal implementation or sublinear prize algorithm.

**Unexpected mixed-generation guard.** Start with a black cell at1. After computing only node(0,1), project the latest stored value at each site while retaining generation0 elsewhere. This projection has black set {0,1}, whereas the complete synchronous generation1 has {0,1,2}. Thus correct individual versioned nodes do not make an arbitrary mixed-generation projection a synchronous frame. An observable must specify its logical generation; buffering and labels are part of the assumptions, not optional bookkeeping. G98's raw in-place order guard separately shows what can go wrong if the parents are overwritten or read from the wrong generation.

**VP1 preregistered NOT RUN.** For N1..4 and every initial word on [-N,N], compare two complete ready-node schedules (increasing generation/site order and a ready-node schedule prioritizing the largest site) with a separately computed synchronous truth-table triangle. Require all stored node values and the centre output to agree. Retain the mixed-generation guard above; the unrestricted claim that every intermediate projection is a synchronous frame must fail. No asynchronous random-cell profile, Local job or speed benchmark. Publish the instrument and predictions before execution.


**VP1 outcome (2026-10-06 19:38 BST).** Executed after predictions and instrument publication through827e006. PASS: 680 initial words at N1..4, both ready-node schedules agree with every synchronous node. Mixed-generation guard passes: {0,1} differs from the complete frame {0,1,2}. These are bounded controls for the stated finite graph, not a new bounded-state simulator or speedup.

### G100. Fair spatial rows do not make rightward flips independent in time (2026-10-06)

**Status:** exact short-horizon ensemble calculation below; independent review and RF1 control pending. Follow-up to G97's open rightward temporal-law scope, not a new orbit-profile run. Existing-record search found no rightward flip triple or lag-two covariance calculation. No novelty, concentration, long-run variance or single-seed claim.

Start from an iid fair row and observe p_t=t. In moving coordinates z_t(j)=x_t(j+t), Rule30 becomes H(z)_j = z_j xor (z_(j+1) OR z_(j+2)). The flip B_t=z_t(1) OR z_t(2) depends on six initial fair bits for t0..2. Spatial fairness persists by G97, so each B_t has mean3/4.

**Exact dependence guard.** Write (d,e,f,g,h,j) for initial sites1..6. Conditional on B_0=0, d=e=0 and B_1=f OR g. For the four pairs (f,g), direct substitution in H twice gives the following B_2:

    (0,0): h OR j; (0,1): 1; (1,0): 0; (1,1): h OR j.

Hence P(B_0=0,B_1=1,B_2=1) = (1/4)*(1/4)*(1+0+3/4) = 7/64, whereas independent Bernoulli(3/4) flips would give9/64. Also P(B_0=0,B_1=0,B_2=1)=3/64. Therefore P(B_0=0,B_2=1)=5/32 and Cov(B_0,B_2)=1/32. Adjacent flips nevertheless have covariance zero: conditional on B_0=0, B_1=f OR g has probability3/4; the unconditional B_1 also has probability3/4. Stationarity under H supplies the same adjacent calculation for B_1,B_2. The variance of B_0+B_1+B_2 is consequently3*(3/16)+2*(1/32)=5/8, not the iid value9/16. This is an explicit example where an adjacent pair test misses temporal dependence.

The ray p_t=t is the right-edge speed, outside Local's measured interior speeds. This calculation does not establish the covariance at an interior speed, asymptotic count variance or a numerical correction to Local's single-seed standard errors. It does refute the general inference that spatial fairness plus the three-quarter mean implies independent rightward flips.

**RF1 preregistered NOT RUN.** Enumerate all64 six-bit words, compare H's three OR flips with independently computed literal Rule30 spacetime samples at p_t=t, and repeat with both choices of the initial origin bit (which cancels from the flips). Predict counts for000..111 of [1,3,5,7,3,9,7,29], marginals3/4, adjacent covariance0, lag-two covariance1/32 and count variance5/8. Counterfactual iid variance9/16 must fail. Publish predictions and instrument before execution; no long column, speed scan or colleague job.


**RF1 outcome (2026-10-06 19:38 BST).** Executed after predictions and instrument publication through827e006. PASS: all64 six-bit words with both origin bits, literal Rule30 spacetime and transported H formulations agree. Counts000..111 are [1,3,5,7,3,9,7,29]. Exact adjacent covariance0, lag-two covariance1/32 and count variance5/8 agree with the derived prediction; iid variance9/16 is refuted in this short-horizon speed-one ensemble. Independent colleague review remains pending. No interior-ray or selected-seed inference.

### G101. An interior speed-three-quarter observer retains temporal memory (2026-10-06)

**Status:** exact four-step fair-ensemble deduction from G97/G100; IF1 and independent review pending. Not a repeated long-ray measurement or selected-seed law.

Let p_t=floor(3*t/4). Its observer increments repeat (0,1,1,1). For any aligned block starting at t=4k, the spatial row at that time is iid fair by G97. Translate the starting site to0. The first flip B_0 (a stay step) equals a fair initial bit at site-1 XOR a function of sites0,1. The next three flips depend only on initial sites0..7: their update cones after cancelling the sampled value exclude site-1. Thus B_0 is independent of the entire subsequent triple. Those three steps are all right steps and, starting from the fair spatial row one tick later, have exactly the G100 triple law.

Consequently this four-step flip block has means (1/2,3/4,3/4,3/4), covariance1/32 between its second and fourth flips, and zero covariance for every other pair in the block. Its count mean is11/4 and variance1/4+5/8=7/8. Independent flips with those means would instead have variance1/4+3*(3/16)=13/16. Independence of the stay flip from the entire triple follows by conditioning on all initial bits except the unused fair site-1 bit. This is stronger than just zero pair covariance.

This law recurs at every aligned four-tick block under the random initial-row ensemble, by spatial-law invariance and translation. It supplies an interior-ray counterexample to temporal flip independence. It does not say distinct blocks are independent, compute a long-run variance coefficient, or prove the measured single-seed ray has this law. The speed3/4 occurs in Local's ray set, but the result is for the ensemble, not that measured orbit. Existing record: G97 supplies the invariant spatial measure and G100 the triple law; no novelty claim.

**IF1 preregistered NOT RUN.** Enumerate all512 initial words at sites-1..7, using literal Rule30 truth tables and observer sites0,0,1,2,3. Predict the four-bit flip histogram is4*[1,3,5,7,3,9,7,29] for each of the two first-flip values. Require all six covariances, count mean11/4 and variance7/8. Independent control: factor the predicted law into a fair first flip and G100's algebraic triple law. Unexpected counterfactual that the interior observer has independent flips with variance13/16 must fail. Publish predictions and instrument before execution. No Local computational run duplicated.


**IF1 outcome (2026-10-06 19:44 BST).** Ran after prediction and instrument publication through7773c41. PASS: all512 initial words at sites-1..7. Four-flip histogram0000..1111 is [4,12,20,28,12,36,28,116,4,12,20,28,12,36,28,116], matching the independently factored prediction. Mean11/4, variance7/8, second/fourth covariance1/32 and all other pair covariances zero agree. Independent review remains pending. No selected-seed, cross-block independence or asymptotic variance claim.

### G102. Isolated and chained race injection differ on a fair initial row (2026-10-06)

**Status:** first-row open-boundary recurrence proof; CI1 and independent review pending. Reply Local L054 and G092. Existing-record search found the isolated injection argument but no chain correction. The asynchronous prior-art pointers remain background, not a source of this probability. No novelty, later-row fairness, noisy-history survival or effective-cone theorem claim.

Model a forced race at site0 on an iid fair initial row. Neighbour flags are independent Bernoulli(eps). In right-to-left processing a flagged site reads its right neighbour's already-computed value, which may itself have raced. Truncate after D neighbour flags at sites1..D and compute site D+1 synchronously; all old inputs remain independent fair. The target's isolated case is D0. This is the local first-row mechanism of races.c, with an open terminal rather than its cyclic boundary.

**Right recurrence.** If the target's old bit is c and its right neighbour's old bit r, its error is (NOT c) AND (new_right XOR r). When c=0, new_right=r OR V, where V is either the next old bit or its updated value depending on that neighbour's race flag. Thus error requires c=r=0 and V=1. Conditional on a zero old bit to the left, let Q_D be the probability this effective right input is1. A nonrace gives a fair old bit. A race gives old_bit OR next_effective_input; conditional on old_bit0, the same zero-left condition recurs. Therefore

    Q_0=1/2; Q_D=(1-eps)/2 + eps*(1/2 + Q_(D-1)/2)
       =1/2 + (eps/2)*Q_(D-1); q_right,D=Q_D/4.

The limit for 0<=eps<=1 is q_right=1/[4*(2-eps)] =1/(8-4*eps). The exact remainder is q_right-q_right,D=(eps/2)^(D+1)/[4*(2-eps)]. The value at eps0 denotes the forced-target isolated limit, not conditioning on a zero-probability natural target event. For eps>0 it is the injection probability conditional on the target race in the stated model. It differs from1/8 for nonzero eps; relative correction is eps/(2-eps), small in the rare-race regime. This is a bulk limit, not an exact formula for every site of the finite cyclic implementation.

**Left contrast.** For a forced left race, target error is new_left XOR old_left. For any fixed finite flag pattern, expanding the consecutive left-race chain exposes a fresh far-left old bit with XOR coefficient1; all OR terms involve sites to its right. That bit is independent fair, so the conditional error probability is exactly1/2 at every finite depth, and in the limit for eps<1 where the chain terminates almost surely. No infinite unanchored left-to-right schedule at eps1 is asserted.

**Unexpected chaining guard.** Set old sites0..3 to0,0,0,1. With site1 synchronous, its new value is0 and a right race at0 injects no error. If site1 also races, site2's synchronous new value1 makes new_site1=1, so the race at0 injects an error. The isolated three-bit velocity formula does not cover this chain. This qualifies the exact isolated probability in L054; it does not refute the measured rare-race scaling or establish a survival law. Noisy later rows need their own joint-law analysis.

**CI1 preregistered NOT RUN.** For D0..5, enumerate every old word and every D-bit neighbour flag word in both directions; use literal Rule30 tables, a forced target race and a synchronous terminal. Apply exact flag weights at eps0,1/4,1/2,1. Predict the right recurrence and remainder, and left injection1/2; retain the explicit chain guard. Independent control is the conditioned algebra above versus full old-word/flag enumeration. No stochastic simulation, eps-scaling fit or colleague job. Publish predictions and instrument before execution.


**CI1 outcome (2026-10-06 19:50 BST).** Executed after predictions and instrument publication through84d09c9. PASS: 43680 old-word/flag combinations and48 exact rational weighted checks. Right finite-depth recurrence and remainder agree at all declared depths and eps; left conditional injection1/2 agrees. The explicit adjacent-race guard gives isolated injection0 and chained injection1. Independent colleague review remains pending. These controls cover the first-row open-terminal model, not the exact cyclic mean, later noisy rows or survival law.

### G103. A clean dependency cone gives a law-free disagreement bound (2026-10-06)

**Status:** coupling/union-bound proof; CP1 and independent review pending. Follow-up to Local L054 and G102. Existing-record search found the effective-cone fit but no clean-dependency-cone bound. This uses elementary deterministic dependencies and Bernoulli/union bounds, not a new concentration theorem.

Couple an ideal radius-one synchronous history and a raced history from the same arbitrary initial row. Assume every unflagged update reads its three parents from the raced history's previous logical row and applies the original rule; flagged updates may read already-computed neighbours as in races.c. For target(i,t), take all ancestor update nodes (j,s), 1<=s<=t, |j-i|<=t-s. There are t² distinct nodes on the line. On a W-cell ring, deduplication gives M=sum over s1..t of min(W,2*(t-s)+1)<=t².

**Clean-cone lemma.** If no ancestor node is flagged, target(i,t) equals the ideal value, regardless of flags outside the cone. Proof: induction from the common initial row through the cone's generations. Each cone update is unflagged and its three parents lie in the preceding cone layer. All those parents therefore agree, and applying the same deterministic rule preserves equality. New-value propagation outside the cone cannot enter via an unflagged node. Snapshot reads at unflagged nodes are an explicit assumption, not a claim about arbitrary in-place updating.

With independent Bernoulli(eps) flags, the clean event has probability(1-eps)^M. Consequently

    P(target differs)<=1-(1-eps)^M<=1-(1-eps)^(t²).

Without independence, if every flag has marginal probability at most eps, the union bound still gives P(target differs)<=min(1,eps*t²). Neither bound assumes fair states, injected-error independence, a measured speed0.246, damage irreversibility or a half-differing interior. Averaging cell indicators gives the same bound for the expected disagreement fraction D_t on a finite ring; spatial independence is unnecessary. Markov's bound also gives P(D_t>=delta)<=min(1,[1-(1-eps)^(t²)]/delta).

For 0<eps,delta<1, mean disagreement at least delta requires

    t>=sqrt(log(1-delta)/log(1-eps))

under independent flags, and t>=sqrt(delta/eps) under the marginal-only bound. Thus the necessary timescale is at least order eps^(-1/2) as eps tends to0, for any fixed mean threshold. This is a lower constraint on the onset of mean decoherence, not a matching upper estimate, exact survival law, realised hitting-time bound or exponent fit. It does not turn Local's measured coefficient0.623 into a theorem. Local's fractions concern finite realised runs.

**Unexpected final-tick guard.** On a five-cell ring started from a black cell at2, allow a right race only at site0 on step1, then no races on step2. Site1 on step2 differs from the ideal history despite its own final update being unflagged. Its ancestor at(step1,site0) was flagged. Checking just the final target is insufficient.

**CP1 preregistered NOT RUN.** For W3..5,T1..2, enumerate all initial rows and flag histories in both sequential race directions with races.c's boundary convention. Require agreement at every site with a clean cone. Use exact weights at eps0,1/4,1/2,1 and require every site disagreement probability to obey both bounds. Independently construct ancestor sets, and retain the final-tick guard. This is77440 short row/flag cases, no stochastic simulation or eps-scaling rerun. Publish predictions and instrument before execution.


**CP1 outcome (2026-10-06 19:56 BST).** Ran after prediction and instrument publication through43095bf. PASS: 77440 initial-row/flag histories and192 exact weighted site bounds. Every clean-cone site agrees, both independent-flag and marginal-only bounds hold, and the final-unflagged/earlier-ancestor guard differs as predicted. These finite controls support the coupling proof; they provide no matching rate, effective cone or realised hitting-time claim. Independent colleague review remains pending.

### G104. Right-reading races preserve fair spatial law; left-reading races change pairs (2026-10-06)

**Status:** bulk spatial-law proof; OM1-OM2 pass, independently reviewed by Local L059. Follow-up G102/G103 and Local L054. Prior-art abstract checks are recorded in PRIOR-ART.md; no imported theorem or novelty claim. This is the sequential snapshot/raced-neighbour model, not a general asynchronous cellular automaton.

On the infinite line, take old row x iid fair and a fixed flag pattern r independent of x. For right-reading updates, assume every rightward consecutive flag run terminates, so the recursion

    y_i=x_(i-1) xor (x_i OR [y_(i+1) if r_i=1 else x_(i+1)])

is well-defined by a finite recursion at every site. This condition holds almost surely for independent Bernoulli(eps) flags with eps<1.

**Right-law proposition.** Conditional on any such fixed flag pattern, y is iid fair. Proof: for output block[a,b], fix all old bits at sites>=b. This fixes y_(b+1), whose recursion uses only those tail bits. Given any prescribed y_a..y_b, solve right-to-left:

    x_(i-1)=y_i xor (x_i OR [y_(i+1) if r_i=1 else x_(i+1)]).

There is exactly one preimage among the b-a+1 old bits at[a-1,b-1]. They were independent fair even conditional on the tail, so every output block has probability2^(-(b-a+1)). This proves the product law for every finite block. Adaptive flags depending on x are excluded. Independent new flag fields at each logical step therefore preserve the fair spatial law at every step, although the temporal history need not match the ideal orbit.

**Earned extension of G102.** In this infinite right-reading model, the current noisy row remains iid fair and is independent of the next fresh flags. Thus G102's bulk conditional injection rate1/(8-4eps) applies at each step relative to F(current noisy row), for eps>0. It is not the disagreement rate relative to the original ideal history, and does not supply a survival law. This is no exact finite-ring invariant-measure claim.

**Left contrast and unexpected density guard.** For left-reading updates, assume each leftward flag chain terminates, and use

    y_i=[y_(i-1) if r_i=1 else x_(i-1)] xor (x_i OR x_(i+1)).

Expanding the chain ending at i exposes a fresh far-left old bit with XOR coefficient1, independent of all old bits at sites>=i. Therefore y_i is fair and independent of those higher old bits, conditional on the fixed flags. If r_(i+1)=0, y_(i+1) depends on x_i,x_(i+1),x_(i+2), so P(y_i differs from y_(i+1))=1/2. If r_(i+1)=1, their XOR is x_(i+1) OR x_(i+2), so that probability is3/4. Independent Bernoulli flags with0<=eps<1 give first-row adjacent disagreement1/2+eps/4 despite both densities remaining1/2. Thus the left map does not preserve the iid fair row law for eps>0.

This separates unchanged density from unchanged pair law. The left formula is for a fair input row and is not asserted at later noisy steps. Local's finite-ring later-time descriptive statistics are not being relabelled refuted; the theorem is about explicit infinite-bulk law and first-step scope. No selected-seed conclusion follows.

**OM1-OM2 preregistered NOT RUN.** OM1: widths1..4, every right flag pattern, every fixed three-bit synchronous terminal tail and every old block; require a bijection to output blocks and recovery by the independent XOR inverse. OM2: anchored left depths0..3, all old rows and flag patterns; require density1/2, pair disagreement1/2 or3/4 according to the right cell's flag. Exact weights at eps0,1/4,1/2,1 must give pair law1/2+eps/4. Counterfactual that unchanged density forces fair pairs must fail. No noisy long-run measurement or Local job. Publish predictions and instruments before execution.


**OM1-OM2 outcome (2026-10-06 20:07 BST).** Executed after predictions and instrument publication through8753ab0. OM1 PASS: 2720 right input cases, every fixed-tail/flag block map bijective and independently inverted. OM2 PASS: 10880 left input cases and48 exact rational weighted moments. Both densities are1/2, but left adjacent disagreement is1/2+eps/4 as predicted. The eps1 checks are finite anchored endpoint controls; the infinite terminating-chain theorem excludes eps1. These controls support the spatial-law proof, not ideal/noisy history survival or exact cyclic invariance. Independent colleague review remains pending.


### G105. Cyclic closure changes zero-row mass in the actual race model (2026-10-06)

**Status:** finite-ring preimage proof; ZR1 passes, independently reviewed by Local L060. Follow-up G104 and Local L054. This is a scope audit of the finite cyclic snapshot/sequential model in races.c, not a new damage-speed or prize theorem. Existing-record checks found fair infinite-row invariance and healing in structured backgrounds; these do not establish finite cyclic uniform invariance.

Take W>=3 cells with indices modulo W, old row x uniformly distributed over all 2^W words, and a fixed state-independent flag word. Sequential right-reading updates process W-1 down to0; an effective race at i<W-1 uses already-computed y_(i+1), otherwise old x_(i+1). Left-reading updates process0 up toW-1; an effective race at i>0 uses y_(i-1), otherwise old x_(i-1). The first processed cell always uses the old cyclic neighbour, so its flag is ineffective.

**Right zero-row preimages.** If the entire new row is zero, every update requires

    x_(i-1)=x_i OR [0 if the right race is effective else x_(i+1)].

If any x_i=1, this equation forces x_(i-1)=1, then repeats around the ring to force all old cells1. Conversely both the all-zero and all-one old rows produce the all-zero new row for every right flag pattern: induction in the scan order, using centre1 to keep the OR1 in the all-one case. These are the only two preimages. Thus conditional on any flags,

    P(new row is all zero)=2^(1-W).

The uniform ring law assigns that row probability2^(-W), so it is not invariant under any fixed right flag pattern or any state-independent mixture of them. G104's infinite-line fair product theorem is intact; closing the inverse around a cycle removes its independent tail. This mass discrepancy is exponentially small as W grows and does not refute Local's large-ring approximate statistics.

**Left zero-row preimages.** Any old1 at an effectively raced site would give new1 because its new left input is0. Therefore an old1 must sit at a nonraced site, where a zero output forces its old left neighbour1. Repeating this implication around the ring either encounters an effective race (a contradiction) or forces the whole old row1 with no effective flags. The all-zero old row always maps to zero. The all-one row does so exactly when no effective left flags are present. Consequently the zero row has one preimage when any effective left flag is present, and two otherwise. With independent Bernoulli(eps) flags,

    P(new row is all zero)=[1+(1-eps)^(W-1)]*2^(-W).

For0<=eps<1 this too differs from the uniform ring law. At eps1 the zero-row mass alone does not decide invariance; no claim is made from this one cylinder.

**No universal decoherence upper bound.** From the common all-zero initial row, ideal and raced histories remain identically zero for all logical times, every flag sequence and either scan direction. Thus no positive mean threshold can have a finite state-uniform onset bound, even with independent positive-rate flags. A matching upper side to G103 needs initial-state or activity assumptions. Fair marginal rows by themselves also cannot specify a coupling: equal copies have disagreement0, while independent fair copies have disagreement1/2, and synchronous Rule30 preserves both constructions' marginals. Those example couplings are not the common-initial-state race process; they only refute inference from marginals alone.

**Unexpected boundary/healing guard.** On a ring, distinct all-zero and all-one rows merge to the same all-zero row in one synchronous tick. Left permutivity therefore supplies no blanket finite-ring noncoalescence theorem. Infinite-line rightmost-damage propagation requires a rightmost discrepancy; these two infinite constant rows would have none. Local's background-dependent healing is preserved, not contradicted.

**ZR1 preregistered NOT RUN.** For W3..7, enumerate every old row and every flag word in both scan directions using the literal Rule30 truth table. Count zero-output preimages for every flag word: right always2; left1 or2 according to whether any effective flag is present. Independently apply exact Bernoulli weights at eps0,1/4,1/2,1 and compare the two formulas. Predict43648 row/flag/direction cases and40 weighted probability checks. Retain zero-row closure and the synchronous two-preimage healing guard. Counterfactual that G104 gives exact finite-ring uniform invariance must fail. This is a short exact enumeration, no long-run or Local scaling job. Publish before execution.


**ZR1 outcome (2026-10-06 20:13 BST).** Ran after proof, predictions and instrument publication throughf0f3a1b. PASS:43648 row/flag/direction cases and40 exact rational weighted probabilities. Right zero-row preimages are exactly zero and one for every flag pattern; left has only zero whenever any effective flag is present. Absorbing-zero and synchronous cyclic-coalescence guards pass. This confirms the finite preimage formulas; it supplies no long-run invariant measure, matching decoherence rate or selected-seed result. Independent review remains pending.


### G106. Spatial fairness survives right races, but moving-frame temporal activity changes (2026-10-06)

**Status:** infinite-bulk one-step flip-law proof; TF1 passes, independently reviewed by Local L061. Follow-up G97/G102/G104. Existing record separates spatial invariance from temporal independence; this derives a changed temporal mean in the specific right-reading race model. No general probabilistic-CA theorem, novelty or selected-seed claim is imported.

Use G104's infinite right-reading recursion with fair iid old row x and fresh independent Bernoulli(eps) flags,0<=eps<1. Let y be the next noisy row. For an observer moving by delta in{-1,0,1}, its flip is x_i XOR y_(i+delta). All flag chains terminate almost surely. The fresh flag field is independent of the current old row at each step.

**Nonrightward mean.** For delta0, y_i has form x_(i-1) XOR A, where A involves only old bits at sites>=i, even through raced-neighbour recursion. The bit x_(i-1) is fresh fair and independent of x_i and A, so the flip is fair. For delta-1, y_(i-1) similarly exposes fresh old x_(i-2). Thus both flip probabilities are1/2, conditional on any terminating fixed flag pattern. This is a marginal statement, not temporal independence of successive flips.

**Rightward mean.** Write

    A_j=x_j OR [y_(j+1) if r_j=1 else x_(j+1)].

The rightward observer's flip is x_i XOR y_(i+1)=A_(i+1). If r_j=0, A_j is the OR of two fair bits, hence has mean3/4. If r_j=1, y_(j+1)=x_j XOR A_(j+1), so

    A_j=x_j OR (x_j XOR A_(j+1))=x_j OR A_(j+1).

Here x_j is independent fair relative to A_(j+1), which depends only on higher old sites and flags. Let U be the translation-invariant mean of A_j. Conditioning on r_j gives

    U=(1-eps)*3/4+eps*(1/2+U/2)=(3-eps)/(4-2eps).

Hence U=3/4+eps/(8-4eps). The additive change is the total right-race injection rate from G102; this equality concerns a one-step temporal observable, not ideal/noisy disagreement accumulated over time. G104 preserves the fair spatial row law and independence from each next fresh flag field, so these flip means hold at every logical step in this ensemble.

**Predetermined moving path.** For N observer increments in{-1,0,1}, with N_right rightward increments, linearity of expectation gives mean flip count

    N/2+N_right/(4-2eps).

This extends G97's synchronous mean. It supplies no independence, covariance, variance, concentration or claim about an adaptively chosen observer. The infinite model excludes eps1; the finite anchored limit as eps tends to1 is a separate endpoint control.

**Finite anchored prediction.** With D potentially raced sites before a synchronous right terminal, define U_0=3/4 and U_D=3/4-eps/4+(eps/2)*U_(D-1). Then

    U-U_D=[eps/(8-4eps)]*(eps/2)^D.

For finite D these are polynomial probabilities also defined at eps1. At eps1, U_D=1-2^(-D-2); this does not define a nonterminating infinite update.

**Unexpected temporal guard.** With eps1/2, the infinite rightward flip mean is5/6, not3/4, although every noisy spatial row remains iid fair. Equal spatial measures need not give equal transition measures. This directly addresses the owner's temporal-field motivation without claiming physical acceleration or a prize result.

**TF1 preregistered NOT RUN.** D0..4, enumerate all old words on sites-2..D+2 and every flag pattern on sites-1..D, with siteD+1 a synchronous terminal. Use the literal Rule30 truth table to compute the next block, then count observer flips for delta-1,0,1. Exact flag weights at eps0,1/4,1/2,1 must give1/2,1/2,U_D. Independent control is the conditioned OR recurrence, including its exact remainder, against full word/flag enumeration. Predict43648 cases and60 weighted flip checks; this count happens to match ZR1 but the objects differ. Counterfactual that unchanged spatial law forces unchanged rightward flip mean must fail. Publish predictions and instrument before execution; no long-ray or colleague race-statistics rerun.


**TF1 outcome (2026-10-06 20:18 BST).** Executed after proof, predictions and instrument publication throughd05bb6b. PASS:43648 old-word/flag cases and60 exact rational weighted flip means. Left/stay means1/2 hold for every finite flag pattern; right U_D and its bulk remainder agree at every declared depth and eps. Finite eps1 checks remain anchored endpoint controls. The infinite eps1/2 rightward mean5/6 follows the proved recurrence, not a long-run empirical fit. No temporal independence, variance or ideal/noisy survival result follows. Independent review remains pending.


### G107. Nonrightward traces stay iid fair conditional on a state-independent right-race schedule (2026-10-06)

**Status:** conditional trace-law proof; NT1 passes, independently reviewed by Local L062. Extends G97's synchronous fresh-bit proof to G104's right-reading recursion, following G106 and Local L061. This is a model-specific extension of known left permutivity, not a prize solution or novelty claim. Existing record G97 supplies the synchronous argument; G104 supplies the terminating recursion.

Start on the infinite line from an iid fair row. Allow any fixed right-reading flag field whose rightward runs terminate at every site and logical step. It need not be spatially or temporally independent. For random flags, require the entire flag field to be independent of the initial row, and termination almost surely. Fresh Bernoulli flags with eps<1 satisfy this. Adaptive flags selected from states are excluded.

**Triangular composition lemma.** Conditional on the whole flag field, each time-t value at site i has form

    x_t(i)=x_0(i-t) XOR g_(t,i)(initial bits strictly to the right of i-t).

Its dependency uses only finitely many initial bits at each finite t. Proof by induction: one right-reading update is x_(t-1)(i-1) XOR A, and the OR/recursive term A uses only previous-row sites>=i. Each recursion terminates, so it has finitely many such inputs. Their initial left endpoints are at least i-(t-1)=i-t+1; only the left input exposes initial bit i-t, with XOR coefficient1. Finite composition of finite recursion trees remains finite. Thus the fresh leftmost initial bit never enters the other term, even though the right dependency may be arbitrarily long.

**Conditional trace law.** Fix a predetermined path p_0,p_1,... with p_t nonincreasing. Define L_t=p_t-t, which strictly decreases. Earlier samples depend only on initial sites>=L_s>L_t. Given all other initial bits and the flag field, the current sample contains the untouched fair bit at L_t, whereas all earlier samples are fixed. It is therefore fair independent of the earlier sample vector. Induction gives iid fair sampled bits conditional on the full flag field. Their distribution does not depend on that field, so the trace is also independent of the flag field as a random object (equality of every finite cylinder law).

Each N-vector of consecutive XOR flips has exactly two sample-vector preimages, so flips are iid fair, mean count N/2 and variance N/4. This now earns the nonrightward temporal-independence result deliberately left open by G106. No state-law induction or independence between successive flag rows is needed: conditioning first handles all their correlations.

**Scope and unexpected coupling guard.** Under these assumptions a single predetermined nonrightward trace has exactly the same statistical law as the synchronous fair-ensemble trace. This does not say the noisy and ideal traces coincide, nor that their two copies are independent: at eps0 they are the same random trace. Their joint history remains a separate question. No selected-seed, finite-ring, adaptive-observer or multisite-transition claim follows. Rightward observers are excluded; G106's rightward mean differs from1/2 even at eps0. Thus this theorem cannot justify calling every temporal observable insensitive to races.

**NT1 preregistered NOT RUN.** T1..3; every path with increments-1 or0; every T-bit schedule switching entire update rows between synchronous and right-reading races, except a fixed synchronous right terminal. Enumerate every initial word on sites-2T..T+1 and evaluate by literal Rule30 tables with shrinking finite boundaries. For each path/schedule, group inputs by all bits except the fresh pivots L_0..L_T: every conditional group must map bijectively onto sampled words. Independently check uniform flip words and mean/variance T/2,T/4. Predict135296 word/path/schedule cases and8736 conditional bijection classes. The schedule family includes fully correlated successive flags, not just fresh Bernoulli rows. Retain the eps0 identical-copy guard using the same inputs. This finite control supports the conditional proof; no simulation fit or colleague job. Publish before execution.


**NT1 outcome (2026-10-06 20:23 BST).** Executed after conditional proof, predictions and instrument publication throughe779bd0. PASS:135296 word/path/schedule cases and8736 conditional pivot-bijection classes. Sample and flip vectors are uniform in every declared path/schedule, with flip-count mean T/2 and variance T/4. The zero-flag history agrees with an independent synchronous XOR/OR formulation, confirming the identical-copy guard. These finite anchored controls support the infinite conditional fresh-bit proof; they establish no selected-seed, finite-ring or joint ideal/noisy independence claim. Independent review remains pending.


### G108. Shared initial bits give a causal invertible coupling of ideal and noisy traces (2026-10-06)

**Status:** conditional finite-horizon coupling proof; CT1 passes, independently reviewed by Local L063. Follow-up G97/G102/G107. Existing-record search found the fresh-bit marginal trace law but no paired causal-mask representation. This uses elementary triangular bijections and entropy counting, not a new general coding theorem or prize solution.

Fix a horizon N, a predetermined nonrightward path, and a terminating right-reading race field independent of the fair initial row as in G107. Couple the ideal synchronous and noisy histories from that same row. Write I_t and J_t for their sampled bits, t0..N. Their distinct fresh initial pivots are L_t=p_t-t. Let R contain all initial bits outside these N+1 pivots, and fix R and the entire flag field. The remaining pivot bits xi_t=x_0(L_t) are independent fair.

**Triangular pair representation.** G97 and G107 give

    I_t=xi_t XOR a_t(xi_0,...,xi_(t-1);R),
    J_t=xi_t XOR b_t(xi_0,...,xi_(t-1);R,flags).

Neither expression uses later pivots, which lie strictly to the left of its dependency boundary. Both expose the same current pivot with coefficient1. Inverting the first expression recursively recovers xi_<t from I_<t and R. Cancelling xi_t therefore yields

    J_t=I_t XOR e_t(I_0,...,I_(t-1);R,flags),   e_0=0.

This is causal: the time-t mask needs no current or future ideal sample. The map from I_0..I_N to J_0..J_N is itself a triangular bijection, recoverable successively from either trace when R and flags are known. Each trace separately is uniform conditional on this environment, yet their conditional joint law has only2^(N+1) equally likely pairs, rather than2^(2N+2).

In bits, conditional entropy of each trace and of their pair isN+1; conditional mutual information between the traces isN+1. These are statements conditional on R and flags. They do not make the unconditional coupling invertible, give its unconditional mutual information, or let an observer recover a hidden schedule from one trace. G107's independence of the single trace from the flag field is compatible with this conditional relation.

**Predictable-mask qualification.** Conditional on R and flags, e_t is determined by the past ideal samples. The current ideal sample is fresh fair independent of that past, so it is independent of the current mask under that conditioning. The masks need not be independent over time or independent of past samples. Their law remains the missing joint-history object, not something spatial invariance determines.

**First-tick state dependence.** For a stationary target i, let E_1=I_1 XOR J_1. On the common fair initial row, a right race can change its OR term only if x_0(i)=0. If x_0(i)=1, both OR values are1 and E_1=0. With fresh iid Bernoulli flags of rate0<=eps<1, G102's total injection probability gives

    P(E_1=1 | I_0=1)=0,
    P(E_1=1 | I_0=0)=eps/(4-2eps),
    Cov(E_1,I_0)=-eps/(16-8eps).

The latter follows because I_0 is fair, E_1*I_0 is always0, and E[E_1]=eps/(8-4eps). Thus even the first error is not state-blind or independent of the past observed bit for eps>0. This does not contradict iid marginal samples; it concerns the pairing of the two copies.

**Unexpected causal-mask guard.** Fix old sites1,2 to0,1, let only target0 read its updated right neighbour, and update site1 synchronously. Vary the two fresh pivots old0 and old-1 fairly. Then I_1=old-1 XOR I_0 while J_1=old-1 XOR1, so E_1=1-I_0. Each two-sample trace is uniform, but its partner is a deterministic bijective scramble given this environment. A state-independent fair error bit would be the wrong coupling. No selected-seed, finite cyclic survival or matching upper decoherence rate follows.

**CT1 preregistered NOT RUN.** Reuse NT1's literal right-reading history evaluator and an independent synchronous XOR/OR evaluator. For T1..3, all left/stay paths, all global-row switch schedules and all initial words on-2T..T+1, group by nonpivot initial bits. Require both trace projections bijective within each group, paired support size2^(T+1), and each time-t XOR mask constant for a fixed ideal prefix of length t. Predict135296 paired cases and8736 conditional classes. Independently check the four-pivot-input causal-mask guard above. This is a paired-law audit, not a repeat of NT1's marginal statistic; the existing first-tick weighted G102 control supplies the rate formula. Publish before execution.


**CT1 outcome (2026-10-06 20:29 BST).** Ran after paired proof, predictions and instrument publication through85f0972. PASS:135296 paired cases and8736 conditional triangular-coupling classes. Both projections are bijective, every time-t mask is determined by the ideal prefix of length t, and the four-input guard gives E_1=1-I_0. These controls support the conditional causal representation and its support/entropy count, not an unconditional independence, information value or survival rate. Independent review remains pending.


### G109. An isolated right-race source error heals once and returns one tick later (2026-10-06)

**Status:** local damage-echo proof; EH1-EH2 pass, independently reviewed by Local L064. Follows G102/G108 and Local L063. Existing record discusses background-dependent healing and state-dependent injection but not this source-site echo. This is a local Boolean mechanism, not a new global damage law, Markov closure or prize solution.

**Single-flip kernel.** Take any line background z and a second row differing only by a flipped bit at site0. Let delta_s(i) be their XOR disagreement after s synchronous Rule30 steps. At s0 the error is only at0. At s1,

    delta_1(-1)=1-z(-1), delta_1(0)=1-z(1), delta_1(1)=1.

These follow respectively from sensitivity of the OR's right input, sensitivity of its centre input, and the permutive left input. Let b=F(z). For the second synchronous step, delta_2(0)=z(1) OR z(2).

To prove this last identity, split on z(1). If z(1)=1, delta_1(0)=0 and b(0)=1-z(-1). Hence delta_2(0)=(1-z(-1)) XOR (1-b(0))=1. If z(1)=0, both centre and right inputs are flipped at s1. Toggling both OR inputs changes its value by1 XOR b(0) XOR b(1). Here b(0)=z(-1) XOR z(0) and b(1)=z(0) XOR z(2). Adding the left disagreement1-z(-1) cancels the z(-1) terms and leaves z(2). Both cases give the OR formula. This is an arbitrary-background identity, requiring no state probabilities.

**Isolated right-race injection.** Start ideal and raced copies from the same arbitrary old row x. On logical tick1, only site0 has an effective right-reading race; site1 is synchronous and already computed. All other sites read the old snapshot. Then the only possible first-row discrepancy is at0, and

    E_1=(1-x(0))*(1-x(1))*x(2).

Indeed an old black target masks the changed right value; with x(0)=0 the updated right neighbour is x(1) OR x(2), so disagreement requires old pattern001 at sites0..2. If no injection occurs, the two rows agree and continue to agree while subsequent ticks are synchronous.

If an injection occurs, the ideal first row z=F(x) has z(1)=1. Apply the single-flip kernel to these first rows. At the original source, disagreement over ticks1,2,3 is exactly

    1, 0, 1.

The second tick heals the source because the ideal right neighbour is black, while the error propagates to site1. The third-tick return follows from delta_2(0)=z(1) OR z(2)=1. There is no new injection in this experiment. Local source healing therefore does not imply the histories have coalesced or that the source will remain healed.

**Fair-input finite law.** On an iid fair initial row the injection probability is1/8 (G102's isolated event). Conditional on injection, second-tick disagreement is always present at site1, absent at0, and present at-1 precisely when x(-2)=x(-1). Thus the second-tick damage set is{1} or{-1,1}, each with probability1/2, and its mean size is3/2. These are conditioned short-time laws; they do not describe dense repeated races, chained injections, finite-ring wraparound or a global survival rate.

**Unexpected echo guard.** The event E_1=1,E_2=0,E_3=1 is forced for every injected isolated right race. It refutes the counterfactual that “healed at a source” means “permanently healed,” and explains why state-blind permanent-defect accumulation is not an exact coupling. It does not refute Local's finite empirical survival fit.

**EH1-EH2 preregistered NOT RUN.** EH1: enumerate all32 backgrounds on-2..2, flip site0 and run two synchronous ticks with shrinking boundaries; require source signature1,1-z(1),z(1) OR z(2). EH2: enumerate all128 old words on-3..3, apply one isolated target right race on tick1, then two synchronous ticks. Predict16 injections, all source signatures101; the other112 give000. Second-tick damage sets{1} and{-1,1} must occur8 times each. Independently verify synchronous propagation with the XOR difference-of-OR equation, rather than the truth-table implementation. These160 exact cases replace no Local long-run job. Publish predictions and instrument before execution.


**EH1-EH2 outcome (2026-10-06 20:34 BST).** Ran after proof, predictions and instrument publication throughf9aa008. EH1 PASS:32 arbitrary backgrounds and the source kernel1,1-z(1),z(1) OR z(2). EH2 PASS:128 initial words; exactly16 injections, all source signatures101, while112 noninjections give000. Second-tick masks{1} and{-1,1} occur8 times each. The independent XOR difference-of-OR propagation agrees throughout. This verifies the local echo, not repeated-race memory closure or a survival rate. Independent review remains pending.


### G110. The isolated-pulse paired trace is not first-order Markov despite iid marginals (2026-10-06)

**Status:** exact projected-memory counterexample; PM1 passes, independently reviewed by Local L065. Follow-up G108/G109 and Local L063's transition-table offer. Existing record provides causal masks and the source echo; this audits a concrete compressed state. It is not a general non-Markov theorem for repeated iid races or a new theory of hidden-state processes.

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


**PM1 outcome (2026-10-06 20:41 BST).** Executed after proof, predictions and instrument publication throughf922142. PASS:128 initial words. In each current ideal-bit bin, previous-error1/next-error1 count is8 and previous-error0/next-error0 count56; both opposite transitions have count0. Both marginal four-sample histograms contain16 words8 times each. The independent001 indicator and fresh-bit complement pairing agree. First-order Markov equality for the paired state is refuted in both bins of this isolated-pulse ensemble, not asserted refuted for repeated iid races. Independent review remains pending.


### G111. A nonzero finite-rate memory split extends to generic rates, but a zero at one rate does not (2026-10-06)

**Status:** finite Bernoulli-polynomial certificate proof; PC1-PC3 pass; independently reviewed by Local L067. Complements Local's requested W5,T3 memory table without enumerating that job. Existing record has exact rational weighting and pulse memory; this derives a parameter-scope certificate. It uses elementary polynomial counting, not a general closure theorem or prize solution.

Let A be a positive-count current-state bin at tick2, B a refined past/current bin contained in A, and S the next-error event E3=1. With a fixed finite initial distribution independent of the flags, use m independent Bernoulli(eps) flags before the current tick and n independent flags for its next step. All probabilities below are finite sums of eps^k*(1-eps)^(M-k) terms with nonnegative fixed weights. Past-only probabilities P(A),P(B) have degree at most m; success probabilities P(S and A),P(S and B) have degree at most m+n.

Define the conditional-split determinant

    D(eps)=P(S and B)*P(A)-P(S and A)*P(B).

When both bins are positive, D differs from0 exactly when P(S|B) differs from P(S|A). Its degree is at most2m+n. Any bin with positive count at an interior rate has positive probability at every eps in(0,1), because each compatible finite flag history has positive weight there. Hence a nonzero D at one interior rate proves D is not the zero polynomial and the split holds at every interior rate except finitely many roots.

**Application conditional on Local finding a split.** W5,T3 has m8 effective flags before tick2 and n4 on tick3, so degree is at most20. At eps0 both copies are identical, making the success event impossible and D(0)=0. If an exact eps1/2 table finds a nonzero witness, that same witness can fail at no more than19 interior rates. In particular it holds for all sufficiently small positive eps, since a nonzero polynomial has only finitely many roots. This gives no numerical rare-rate threshold or magnitude without coefficients, no infinite-ring conclusion and no long-time survival law. This generic implication was prepared before receiving Local's table; the support application below uses its subsequently published certificate.

At eps1/2 every one of the131072 paired histories has equal weight, so the integer witness is

    n_(S,B)*n_A-n_(S,A)*n_B,

and its nonzero status is exactly D(1/2)'s nonzero status. To reconstruct D, retain each event count by total number of active flags k: h_k. The scaled probability polynomial is sum h_k*eps^k*(1-eps)^(12-k); divide by32 for the uniform initial-row probabilities. Polynomial expansion and multiplication use integer coefficients; the determinant's common positive scale does not affect its roots. Past degrees reduce to8 when the future flags are summed out.

**Unexpected held-rate guard.** For two independent flag bits X,Y, take A always, B={X=1}, S={X XOR Y=1}. Then

    D(eps)=eps*(1-eps)*(1-2eps).

Conditional-rate equality holds at eps1/2 while failing at eps1/4, where D=3/32. Thus a held table at one noise rate cannot certify even a single witness polynomial identically zero. Nor does an identically zero determinant for one refinement prove full Markov closure.

**PC1-PC3 preregistered NOT RUN.** A four-count-histogram polynomial tool will be checked on three independent two-flag toy predicates: PC1 S=X, predicted D=eps*(1-eps); PC2 S=Y, predicted D identically0; PC3 S=X XOR Y, predicted D=eps*(1-eps)*(1-2eps). All use A always and B={X=1}. Expand active-count histograms, compare to declared coefficient vectors, and independently enumerate the four flag histories with rational weights at eps0,1/4,1/2,1 (12 determinant checks). The unexpected PC3 half-rate equality must coexist with quarter-rate failure. This validates certificate arithmetic, not Local's production table. Publish before execution.


**Application to Local L066's complete table: a support witness needs no rate exceptions.** During this block Local published the exact enumeration with controls, preregistered at9de993f. GPT audited the script's complete32-row/4096-effective-flag-history coverage and right-reading model, but did not repeat the computational lane. Take A={I2=1,E2=0} and B={I1=1,I2=1,E1=0,E2=0}. Local reports n_A=52736,n_(S,A)=9216,n_B=25600,n_(S,B)=0. Thus D(1/2)=-225/16384, an exact nonzero split. More strongly, the zero count means S and B has no compatible history, whereas B and S and A each have positive counts. All finite histories retain positive weight for every0<eps<1. Therefore P(S|B)=0 while P(S|A)>0 throughout that interval: the finite W5 paired state is not first-order Markov for any interior rate, without exceptional roots. This support argument is a finite-ring result; it supplies no infinite-bulk or higher-order conclusion. The general polynomial method remains useful for nonextremal witnesses. Independent review of this extension remains pending.


**PC1-PC3 outcome (2026-10-06 20:54 BST).** Executed after predictions and instrument publication through d8d67d1. PASS: coefficient vectors [0,1,-1], [0] and [0,1,-3,2], with12 independent exact rational determinant checks. The unexpected XOR toy has equality at eps1/2 and a nonzero determinant3/32 at eps1/4. This checks the polynomial arithmetic only; Local's production enumeration was not repeated. Independent review of G111 remains pending.

### G112. Two shared black observations shield the next tick and obstruct bulk first-order memory closure (2026-10-06)

**Status:** local proof and infinite-ensemble counterexample; WH1-WH3 pass, independently reviewed by Local L069. This explains Local L066's deterministic bin without repeating its production enumeration. It extends G109-G111 by a local argument, not by taking a ring limit. The general issue of projected Markov processes is established lumpability theory; the claim here is only this Rule30 coupling identity.

Let z_t be synchronous Rule30 and y_t its right-reading raced copy, with common initial row x. At each site the raced update reads the old left and centre and either the old or updated right neighbour. Write I_t=z_t(0), E_t=z_t(0) XOR y_t(0), K_t=(I_t,E_t). Flags may be arbitrary provided right recursions terminate. For the probabilistic conclusion use iid fair initial bits and fresh independent Bernoulli(eps) flags,0<eps<1, on the infinite line; these recursions terminate almost surely at every site and finite tick.

**First-step white agreement lemma.** If z_1(j+1)=y_1(j+1)=0, then z_1(j)=y_1(j). If x(j)=1, its old centre masks both right-read alternatives. If x(j)=0, the ideal right output0 equals x(j) XOR (x(j+1) OR x(j+2)), forcing x(j+1)=0. Both the old and updated raced right alternatives are then0, so the target updates agree. The lemma uses common initial input; it is not asserted for arbitrary later unequal rows.

**Two-black shielding.** Suppose z_1(0)=y_1(0)=z_2(0)=y_2(0)=1. The black old centre at site0 shields its tick2 right read. Output1 therefore forces z_1(-1)=y_1(-1)=0. Applying the white agreement lemma at j=-2 gives z_1(-2)=y_1(-2). When site-1 updates on tick2, its centre is0 but its old and updated right alternatives are both1. Its output is consequently the shared old left value XOR1, so z_2(-1)=y_2(-1). Site0's black old centre again shields tick3, yielding z_3(0)=y_3(0). Thus the refined bin

    B={I1=1,I2=1,E1=0,E2=0}

has next error E3=0 for every compatible shared-input history. This is a deterministic three-tick statement, independent of the rate and outside flag patterns.

**Positive finite cylinders, not an infinite clean event.** Define the nine update nodes C: tick1 sites-2..2, tick2 sites-1..1 and tick3 site0. Their ordinary ancestors are initial sites-3..3.

For initial word0110000 on-3..3 and all nine flags in C zero, both source traces have I1=I2=1, so B occurs. This cylinder has probability(1-eps)^9/128>0.

For initial word0000010 on-3..3, set only site0's tick1 flag in C to1 and all other eight to0. Its updated right neighbour at tick1 is an unflagged node of C, so no extra outside recursion enters. The ideal source trace at ticks0..3 is0011 and the raced trace0110: I2=1,E2=0,E3=1. The cylinder has probability eps*(1-eps)^8/128>0. Outside initial bits and flags are unrestricted in both constructions.

Take A={I2=1,E2=0} and S={E3=1}. The cylinders prove P(B)>0 and P(S and A)>0. The shielding identity proves P(S|B)=0, whereas P(S|A)>0. Since B further specifies past K1 within A, this violates the first-order Markov property of the single-site paired observable at tick2, even allowing time-dependent kernels. This proves neither failure of every finite memory order nor a long-time survival law. Each separate trace can remain iid fair as in G107; coupling memory is a different question. This is not a single-seed or prize claim.

**WH1-WH3 preregistered NOT RUN.** WH1: all initial rows and effective right-flag patterns on rings W3..5 (672 effective cases, equivalently1344 full flag assignments), test the first-step white agreement implication at every site. It must hold; this small one-step control is not Local's three-tick production table. WH2: implement the two explicit finite cylinders with shrinking boundaries and literal Rule30 table, independently compare the declared four-bit traces and synchronous XOR/OR updates; predict B and A intersect S respectively. WH3, unexpected orientation guard: on a W5 left-reading scan, initial00001 and only site1 flagged yield ideal/raced shared white output at site2 but different output at site1. The counterfactual that white agreement works for either scan direction must fail. Publish these predictions and instrument before execution; no production sweep or random trial.


**WH1-WH3 outcome (2026-10-06 20:59 BST).** Executed after proof, predictions and instrument publication through38eda50. WH1 PASS:672 effective one-step right-ring cases (equivalently1344 full flag assignments), with the white-agreement implication checked at every site. WH2 PASS:both explicit finite cylinders and independent literal-table/XOR-OR controls; pulse traces0011/0110 and the clean two-black bin agree with predictions. WH3 PASS:the left-reading00001 guard has shared white output at site2 and different output at site1, refuting orientation independence. These finite controls support the written local identity and cylinder construction; they do not themselves prove an infinite limit. The infinite conclusion rests on that argument and remains pending independent review.


### G113. A bounded audit of one-lag closure in the isolated-pulse paired trace (2026-10-06)

**Status:** LM1-LM3 preregistered NOT RUN. Existing G110 refutes first-order closure in the pulse model; G112 addresses fresh-race bulk first-order failure. Neither decides whether the enlarged state (K_(t-1),K_t) is sufficient. This block stays in the pulse model to seek an exact, inspectable history witness without duplicating Local's repeated-race jobs. General projected-memory theory is prior art, recorded with G112.

Start from an infinite iid fair row; only source0 reads its updated right neighbour on tick1, and all remaining reads are synchronous. Keep the pulse phase fixed and known. Source samples through tick6 depend only on initial sites-6..6. Uniform enumeration of those8192 words therefore gives exact finite-horizon probabilities in this infinite ensemble, without a ring limit. LM1 must reproduce the001 injection predicate and E1,E2,E3=indicator,0,indicator with independent literal-table/XOR-OR updates.

**Blind LM2 prediction:** at tick5, conditioning the next error E6 on K4,K5 differs from conditioning on K3,K4,K5 in at least one positive bin. Compare integer cross products for every child and parent. If no split occurs, retain the held finite result; that cannot establish two-step closure at all times. A nonzero split would refute order-two Markov at this tick for this pulse ensemble, not for fresh repeated Bernoulli flags. It would not refute every finite order.

**Unexpected LM3 control:** both separate seven-sample marginal histograms must still contain128 words64 times each, even if paired closure fails. The counterfactual that tick2 healing prevents tick3 return must fail by LM1. Run only after predictions and instrument are published. GPT owns this bounded history audit; no rate sweep, long run or Local spectrum repetition.

#### G113 result: one lag does not close the isolated-pulse paired trace at tick5 (2026-10-06)

**Status:** exact finite-cone enumeration counterexample; independently reviewed by Local L070. Predictions and instrument published through2589f4f before execution. This is the pulse ensemble of G110, not the fresh Bernoulli-race model of G112 and not an all-orders impossibility claim.

Let K_t=(I_t,E_t) for the source of two common-input Rule30 copies. Start with an infinite iid fair row; only the noisy source0 reads its updated right neighbour on tick1, and all other reads and future ticks are synchronous. Keep the pulse schedule fixed and known. The seven source samples at ticks0..6 depend only on the13 initial bits at sites-6..6; the pulse's extra same-tick right read needs initial sites0..2 and stays inside that domain. Thus8192 equally weighted words give exact probabilities for this infinite ensemble. Literal Rule30 table updates were independently checked against XOR/OR updates throughout the shrinking cone.

Take A={K4=(0,0),K5=(0,0)} and its refinement B=A intersect {K3=(0,0)}. LM2 counts n_A=1872,n_(E6=1,A)=40,n_B=896,n_(E6=1,B)=0. Therefore

    P(E6=1 | A)=40/1872=5/234,
    P(E6=1 | B)=0.

Both bins have positive probability. Their next-error probabilities differ despite identical last two observed paired states; this violates second-order Markov at tick5, even with a time-dependent kernel and the known pulse phase.

The zero child also has an analytic explanation: G109 gives E3=E1, so B's E3=0 means no initial injection. With no future races the two configurations then agree forever. The positive parent-success count is the enumerated existence certificate, checked with both update formulations; it is not an extrapolation or a fitted probability. All count claims can be reproduced by tests/probes/rule30_gpt_lagged_memory.py. Independent reading remains required.

**LM1-LM3 outcomes (2026-10-06 21:05 BST).** LM1 PASS:8192 cone words,001 injection predicate and E1,E2,E3=indicator,0,indicator. LM2's blind split prediction HELD:8 unequal child-parent refinements among16 parents and36 positive children. A second child K3=(0,1),K4=K5=(0,0) has20 successes in40 histories, versus the parent's40 in1872; the rate difference is56/117. LM3, the unexpected marginal check, PASS:both separate seven-sample histograms have128 words64 times each. The permanent-healing counterfactual is refuted by the source echo. Uniform marginals coexist with failure of order-two paired closure. No result about third-order closure, every finite order, repeated fresh flags or long-time survival follows.


**LM4 addendum preregistered NOT RUN (2026-10-06 21:09 BST).** Extract the lexicographically first13-bit word in each of B and {K3=(0,1),K4=K5=(0,0),E6=1}; previous counts896 and20 guarantee existence. Print its full source traces. Independently pad each word with both values on each outer initial site and run literal-table synchronous updates with the isolated pulse: all eight padded histories must preserve both source traces. This unexpected boundary check certifies finite cylinders with arbitrary exterior bits, rather than an implicitly zero exterior. Each specified13-bit cylinder has probability1/8192 in the infinite fair ensemble. Publish before execution.


**LM4 outcome and explicit positive cylinder (2026-10-06 21:09 BST).** Predictions and instrument published through832c0d3 before execution. PASS:the lexicographically first success word on sites-6..6 is0011110010000, with ideal source trace0110000 and noisy trace0011001 at ticks0..6. It has K3=(0,1),K4=K5=(0,0),E6=1. The zero-child witness is0000000000000 with both traces0000000. These specify only13 initial bits, not the whole infinite row; each cylinder has probability1/8192. All eight independently implemented padded-boundary histories preserve the predicted traces. Arbitrary exterior independence follows from the explicit finite ancestor cone, not from extrapolating those eight tests.

Consequently the proof's positive parent-success event can be checked by forwarding this single finite word, without trusting a total-count census. The zero child follows analytically from E3=E1 and no future injections, while this cylinder gives P(E6=1 and A)>0 and hence P(E6=1|A)>0. The exact5/234 rate remains the independently controlled enumeration result; the order-two counterexample itself now needs only the identity and a finite positive cylinder. This strengthens inspectability without changing the pulse-model scope or claiming every finite memory order.


### G114. A healed white source can hide cancellation of two incoming errors (2026-10-06)

**Status:** local algebraic identity and pulse mechanism; DP0-DP2 pass, independently reviewed by Local L071. This unpacks G113's explicit witness. G109 already gives the difference-of-OR propagation law; this is its Boolean expansion and a causal explanation, not new general damage-spreading theory.

For a synchronous tick, let a,b,c be ideal left, centre and right bits and p,q,r their respective XOR errors. Expanding OR over binary arithmetic gives

    delta_next = p XOR ((1-c)*q) XOR ((1-b)*r) XOR (q*r).

This follows by subtracting (in XOR) the two Rule30 outputs and using OR(b,c)=b XOR c XOR(b*c). If the source is currently healed, q=0, the update reduces to

    delta_next = p XOR ((1-b)*r).

At a shared black centre only the left error matters. At a shared white centre the two incoming errors cancel when equal, including when both are1. Thus zero observed source error is not evidence that either incoming channel is clean. The nonlinear q*r term also prevents treating the full damage process as autonomous Rule90. This identity applies to synchronous propagation after the isolated pulse; it is not the rule for a newly raced update.

**Hand derivation for G113's finite cylinder.** Initial sites-6..6 are0011110010000; only source0 races right on tick1. In the shrinking source cone, predicted ideal/noisy rows are:

| Tick | Sites | Ideal | Noisy |
|---|---|---|---|
| 3 | -3..3 | 1010101 | 1111011 |
| 4 | -2..2 | 01010 | 00001 |
| 5 | -1..1 | 101 | 001 |

At tick4 the white source has no error, but both immediate neighbours have errors1. These cancel, producing another healed source at tick5. At tick5 the source is still white and only its left neighbour has error1, so the source error returns on tick6. The observed two-tick recovery was parity cancellation, not elimination of the surrounding discrepancy. Rows in this table are restricted to the shrinking cone, not claims about the entire damage set.

**DP0-DP2 preregistered NOT RUN.** DP0:all64 ideal-neighbourhood/error triples must satisfy the expanded identity, independently compared with the literal Rule30 truth table. DP1:forward the specified cylinder through tick6 and require the three hand-derived rows above; check the expanded difference identity at every synchronous update, and require incoming source errors(1,1) at tick4 and(1,0) at tick5. DP2, unexpected guard:shared black centre with p=q=0,r=1 has next error0, whereas autonomous Rule90 would give1; the autonomous-damage counterfactual must fail. Publish before execution. No new production table or repeated-race job.


**DP0-DP2 outcome (2026-10-06 21:16 BST).** Ran after proof, predictions and instrument publication through9e09890. DP0 PASS:all64 local ideal/error triples satisfy the expanded Boolean difference identity. DP1 PASS:all three hand-derived cone rows agree; at tick4 the white source receives errors(1,1), cancelling to0, and at tick5 it receives(1,0), returning error1. The identity also matches literal-table differences at every synchronous node. DP2 PASS:the shared-black guard blocks right error, refuting autonomous Rule90 damage evolution. The result explains this pulse witness; it supplies no stochastic closure or survival rate. Independent review pending.


### G115. Audit an injection-indicator state against the full observed pulse history (2026-10-06)

**Status:** IS0-IS2 preregistered NOT RUN. Responds to Local L070's proposed injection-history state. In the isolated-pulse ensemble of G113, define F=E1, the actual injection indicator, not merely the occurrence of a raced read. If F=1 its injection time is always tick1, so at fixed tick5 its age is already known. Test the more generous candidate X5=(F,K4,K5), retaining both recent paired observations.

Enumerate the same8192 initial cone words and use the independently checked update formulations. IS0 must recover F=E3 and the001 predicate, all bin totals, and the known unaugmented zero-child0/896 versus parent40/1872 witness. IS1's blind prediction is that at least one positive refinement by the entire observed prefix K0..K5 has a different E6 rate from its X5 parent. Integer cross products decide equality exactly. A failure would refute this specified candidate in this pulse ensemble; a held finite table would not prove closure at all times.

**Unexpected IS2 prediction:** the shallower comparison using only K3 may hold after conditioning on F, even if the full-prefix comparison splits. This tests whether a diagnostic can miss deeper observed information. Retain either outcome. The counterfactual that omitting F closes the one-lag state must fail by IS0. No repeated-race injection definition is imported, no Local production job is repeated, and no all-orders conclusion is predicted. Publish instrument and predictions before execution.

#### G115 result: injection memory plus one lag still misses deeper observed pulse history (2026-10-06)

**Status:** exact finite-cone candidate-state counterexample; independently reviewed by Local L072. IS0-IS2 predictions and instrument published through114a83c before execution. This tests Local L070's injection-history repair in the isolated-pulse ensemble, not repeated random races.

Use the same8192 fair initial cone words as G113. Define F=E1, the actual injection indicator, and candidate X5=(F,K4,K5). Every positive injection happens at the fixed pulse time1, so adding its time or age at tick5 adds no further information. Refine each candidate bin by the full observed history H=(K0,...,K5). The instrument uses two independently checked update formulations and exact integer cross products.

The parent A={F=1,K4=(0,0),K5=(0,0)} has80 compatible words and40 next errors, so P(E6=1|A)=1/2. Its full-history child

    H=((0,0),(0,1),(0,0),(0,1),(0,0),(0,0))

has20 compatible words and no next error, so P(E6=1|H)=0. Both bins have positive probability in the infinite fair ensemble because only13 initial bits are needed. Thus the next-error law retains observed-past information not supplied by injection occurrence/time and one lag. The specified state is not sufficient at tick5, even allowing the known pulse phase.

A concrete word in the zero child is0101100010000 on-6..6. G113's independently checked positive cylinder0011110010000 lies in the same candidate parent and produces next error1. The zero conditional rate for the entire full-history child is certified by exhaustive enumeration, not inferred from the single zero word. Independent review remains required; no repeated-race or all-finite-orders conclusion follows.

**IS0-IS2 outcomes (2026-10-06 21:19 BST).** IS0 PASS:all8192 words, F=E3=001 indicator, bin totals and unaugmented0/896 versus40/1872 witness. IS1's blind split prediction HELD:24 unequal full-prefix refinements among18 candidate parents and112 full histories. A second witness has parent(F,K4,K5)=(1,(0,0),(0,1)), next-error24/48, while its zero-success full-history child has0/12. IS2's unexpected shallow-equality prediction HELD:zero unequal refinements when only K3 is added to X5. This is a controlled false reassurance: the K3-only diagnostic holds at this horizon while the complete observed past splits. No held finite diagnostic is promoted to closure. The unaugmented one-lag closure counterfactual remains refuted.

### G116. The fourth pulse error is gated parity of three earlier ideal samples (2026-10-06)

**Status:** local algebraic proof; PE0-PE2 pass, independently reviewed by Local L072. Follows G109's echo, G114's Boolean damage equation and G115's shallow/full-history distinction. This is the fixed isolated-pulse model, not a law for repeated races or a physical jerk measurement.

Write F=E1 for actual injection and I_t for ideal source0. With common initial input and only a source right race on tick1, followed by synchronous ticks,

    E4=F*(I1 XOR I2 XOR I3).

If F=0 there is no changed cell and all later errors vanish. If F=1, initial sites0..2 are001. Ideal first-tick sites1 and2 are therefore both1. At tick2 the ideal right sites1,2 have values1 XOR I1 and0 respectively; the ideal source is I2=1 XOR z1(-1). G109's second-tick errors are delta2(-1)=I2,delta2(0)=0,delta2(1)=1, with no error outside sites-1..1.

Using G114's synchronous damage equation on tick3:delta3(-1)=(1-I2)*I2=0; delta3(0)=I2 XOR(1-I2)=1; delta3(1)=1 because ideal tick2 site2 is0. Independently the ideal tick3 site1 is I2 XOR(1 XOR I1). Thus at the fourth source update, old errors(left,centre,right) are(0,1,1), and ideal(centre,right) are(I3,I2 XOR1 XOR I1). Flipping both OR inputs changes their OR by1 XOR centre XOR right. Substitution gives E4=I1 XOR I2 XOR I3, proving the gated identity.

**Conditional fair law.** Under F=1, the initial negative bits remain independent fair. The ideal samples I1,I2,I3 successively contain fresh initial bits-1,-2,-3 as XOR pivots. Conditioning on injection therefore leaves those three samples iid fair. Consequently P(E4=1|F=1,I2,I3)=1/2, but further specifying I1 makes E4 deterministic. Unconditionally P(E4=1)=1/16. This gives an exact example of older observed information disappearing under a shallow average; it does not by itself prove the later G115 candidate failure, which has its own complete-history certificate.

**PE0-PE2 preregistered NOT RUN.** Enumerate512 initial words on-4..4 through four ticks, with independent literal-table/XOR-OR updates. PE0 must reproduce F=001 and E1,E2,E3=F,0,F. PE1 must verify E4=F*(I1 XOR I2 XOR I3),64 injected words and448 noninjections, and32 fourth errors. PE2, the unexpected shallow-average guard, requires eight ideal triples(I1,I2,I3), each appearing8 times among injections. For each fixed I2,I3 there must be8 fourth errors among16 histories, whereas each I1 refinement is deterministic. The counterfactual that F and the last two ideal samples determine E4 must fail in every such bin. These are512 local cone controls, not a rerun of the8192-word production-history audit. Publish before execution.


**PE0-PE2 outcome (2026-10-06 21:25 BST).** Executed after proof, predictions and instrument publication through241fb49. PASS:all512 initial cone words;64 injections and448 noninjections;source echo and the gated parity E4=F*(I1 XOR I2 XOR I3). Exactly32 fourth errors. Among injections every one of the eight ideal triples appears8 times. Each fixed I2,I3 bin has8 errors among16 histories, while adding I1 gives deterministic parity. The unexpected shallow-average guard refutes last-two-ideal-sample sufficiency in all four such bins. Independent review pending;no repeated-race or physical-derivative law follows.

### G117. A hidden right-tail bit first enters the fifth pulse-error law (2026-10-06)

**Status:** local algebraic kernel and fair-ensemble law; FT0-FT2 pass, independently reviewed by Local L073. Continues G116 in the fixed isolated-pulse model. There are no further races after tick1; conditional uncertainty here comes from initial bits outside the observed source history, not fresh noise.

Condition on injection F=1, so old sites0..2 are001. Put D=x(3)*(x(4) OR x(5)), for the common initial row x. Write a=I1,b=I2,c=I3,d=I4 and define

    H=a XOR b XOR c,
    L=1 XOR ((1-b)*(d XOR (c OR (1 XOR a XOR b)))),
    R=b XOR D,
    C=c XOR ((1 XOR a XOR b) OR (1 XOR a XOR D)).

Then the fifth source error is

    E5=L XOR ((1-C)*H) XOR ((1-d)*R) XOR (H*R).

**Derivation.** G116 gives source delta4=H and ideal tick3 site1=1 XOR a XOR b. Direct ideal updates give z2(3)=D and z3(2)=1 XOR a XOR D: when x3=0 the relevant OR is1, and when x3=1 its complement is x4 OR x5. Hence ideal tick4 site1 is C. Tick3 right errors at sites1,2 are both1, so G114 gives delta4(1)=z3(1) XOR z3(2)=R. On the left delta3(-1)=0,delta3(0)=1 and delta3(-2)=(1-z2(-2))*b. If b=1, z3(-1)=1 XOR z2(-2), so delta4(-1)=1; if b=0 it is1 XOR z3(-1). Since z3(-1)=d XOR(c OR (1 XOR a XOR b)), these cases give L. Substituting the tick4 errors(L,H,R) and ideal centre/right(d,C) in G114's damage law proves the formula. For F=0 the copies remain identical, so E5=0.

**Exact fair conditional kernel.** After fixing F=1, D has probability3/8 of being1. Given the entire nonnegative initial tail, a,b,c,d each contain a successive independent fair negative pivot; their joint distribution is uniform on16 words independent of that tail. Thus D is independent of the ideal prefix. The paired observed history through tick4 contains no further tail information: I0=0, E1,E2,E3=1,0,1 and E4=H are fixed by that prefix.

Let g(a,b,c,d,D) denote the displayed formula. Then the exact next-error probability given the full paired observed past is (5/8)*g(a,b,c,d,0)+(3/8)*g(a,b,c,d,1). Algebra gives8 contexts that depend on D,6 deterministic-error contexts and2 deterministic-zero contexts. Of the8 mixed contexts,6 have rate3/8 and2 have rate5/8. Therefore

    P(E5=1)=19/256,
    H(E5 | K0,...,K4)=h2(3/8)/16,

where h2 is binary entropy in bits. For a=b, D affects the error exactly when d=c; for a differs from b, exactly when d=0, giving the eight mixed contexts. The unconditional entropy weights each injected prefix by1/128 and all noninjected histories by0. This is an exact short-horizon conditional uncertainty, not an entropy rate or a Markov-order theorem.

**FT0-FT2 preregistered NOT RUN.** Enumerate2048 initial words on-5..5 through tick5. Independently compare literal-table and XOR/OR updates; FT0 must recover F,0,F and G116's fourth parity. FT1 must verify the fifth-error formula,256 injections,1792 noninjections and152 fifth errors. Each injected ideal quadruple must occur16 times with D=1 in6 and D=0 in10. The16 conditional error counts must have histogram{0:2,16:6,6:6,10:2}. FT2, unexpected no-fresh-noise guard:prefix a=b=c=d=0 has E5=D, hence6 errors in16 otherwise identical observed histories. Print one initial word for each D value and verify identical paired histories through4 with different E5. The counterfactual that the full observed past determines the next error after racing stops must fail. Publish before execution; no repeated-race production job.


**FT0-FT2 outcome (2026-10-06 21:30 BST).** Executed after proof, predictions and instrument publication through6c4792e. PASS:2048 initial cone words,256 injections and152 fifth errors. All16 injected ideal prefixes occur16 times each, with D=1 in6 histories and D=0 in10. The conditional error-count histogram is exactly{0:2,16:6,6:6,10:2}, verifying the displayed kernel and entropy weighting. Independent literal-table/XOR-OR updates agree. The unexpected guard gives initial words00110001000 (D0,E5=0) and00110001101 (D1,E5=1) on-5..5, both with identical paired history((0,0),(0,1),(0,0),(0,1),(0,0)) through tick4. No fresh flags are present after the pulse. Independent review pending;these controls do not turn the conditional entropy into an entropy rate.

### G118. Exact unconditional mutual information of the first six pulse samples (2026-10-06)

**Status:** short-horizon entropy proof; JI0-JI2 pass, independently reviewed by Local L074. Complements G108's conditional coupling law using G116-G117. It is a pulse ensemble calculation, not an entropy rate, prize result or repeated-race law.

Let A=(I0,...,I5),B=(J0,...,J5) be ideal and noisy source traces in the fair initial-row isolated-pulse model. Both are iid fair by G97/G107, so H(A)=H(B)=6 bits. XOR-error history E is in bijection with B once A is given. Write h2(p) for binary entropy, with0*log2(0)=0. Then

    H(A,B)=6+h2(1/4)/2+h2(3/8)/16,
    MI(A;B)=6-h2(1/4)/2-h2(3/8)/16.

**Proof.** F=E1 is the001 injection indicator. Given I0=1, F=0; given I0=0, F is Bernoulli1/4. Fixing the nonnegative initial tail leaves the ideal samples I1..I5 successively triangular in five fresh negative initial bits, hence jointly uniform. Thus conditioning on those ideal samples adds no information about F or the hidden D of G117 beyond I0. In particular H(F|A)=h2(1/4)/2, not h2(1/8).

If F=0 the whole error history is zero. If F=1, its first five entries are0,1,0,1,I1 XOR I2 XOR I3. Only E5 remains to be specified. G117's independent D has rate3/8 even when the fifth ideal sample is observed: the fifth fresh negative pivot preserves the uniform conditional likelihood of the ideal prefix for every fixed right tail. Eight of the16 ideal quadruples have a D-dependent E5, each with entropy h2(3/8). Since P(F=1)=1/8, H(E5|F,A)=h2(3/8)/16. The first error identifies F, so entropy chain rule gives H(E|A)=H(F|A)+H(E5|F,A). Add H(A)=6 and subtract from H(A)+H(B)=12 to prove the formulas.

This gives unconditional MI strictly below6 bits, whereas G108 gives6 bits conditional on the nonpivot environment for the same horizon. In that conditional model the environment fixes the hidden inputs and the two traces are causally bijective. This is a statement about these two information quantities in this model, not a general monotonicity rule for conditional mutual information.

**Exact joint-count predictions.** On the2048 equally weighted11-bit initial words, each of64 ideal traces has32 preimages. For the32 traces with I0=1 all32 give one paired trace. For I0=0,24 are noninjections. For16 of those ideal traces the eight injected words give one deterministic-error trace; for the other16 they split5 and3 according to D. Thus the joint-support count histogram is{32:32,24:32,8:16,5:16,3:16}, with112 distinct pairs.

**JI0-JI2 preregistered NOT RUN.** JI0 checks all2048 words with independent literal-table/XOR-OR updates; both marginal histograms must contain64 traces32 times each and the joint histogram must match the prediction above. JI1 compares entropy from the integer count spectrum with the displayed binary-entropy expression and MI identity, tolerance1e-12 only for floating logarithms. JI2, unexpected conditioning guard:each ideal trace beginning0 must have8 injections among32, each beginning1 none; replacing H(F|A) by unconditional h2(1/8) must overestimate joint entropy. Publish before execution. No production job or asymptotic inference.


**JI0-JI2 outcome (2026-10-06 21:36 BST).** Executed after proof, predictions and instrument publication through8ced884. PASS:2048 words;both marginal histograms have64 traces32 times each. The112 joint pairs have exactly the predicted count histogram{32:32,24:32,8:16,5:16,3:16}. Entropy from those counts agrees with the closed expression within1e-12:joint6.465291187412 bits,mutual information5.534708812588 bits. The unexpected conditioning guard passes:every ideal trace starting0 has8 injections in32 histories;those starting1 have none. Substituting unconditional h2(1/8) overestimates joint entropy,refuting injection-independence. Independent review pending;no entropy-rate or repeated-race conclusion.

### G119. Shared fresh pivots turn error uncertainty into mutual-information increments (2026-10-06)

**Status:** general right-reading fair-ensemble identity; GF0-GF2 pass, reviewed by Local L075. Uses G107-G108's fresh-pivot property and ordinary entropy chain rule, not a new general information theorem.

Start ideal and right-reading noisy Rule30 copies from the same infinite iid fair row. The entire terminating right-reading flag field is independent of the initial row; temporal flag dependence is allowed. Observe both on a predetermined nonrightward path p_t. Put K_t=(I_t,J_t),E_t=I_t XOR J_t and M_t=MI(I0..It;J0..Jt), with empty-prefix M_-1=0. Then

    M_t-M_(t-1)=1-H(E_t | K0,...,K_(t-1)),
    M_T=(T+1)-sum_(t=0..T) H(E_t | paired past).

Each increment is between0 and1 bit;M_0=1 since the initial copies agree. No limit or entropy rate is asserted.

**Proof of the required conditional freshness.** The initial pivot index L_t=p_t-t strictly decreases. By G107-G108, both samples have form X_(L_t) XOR u_t and X_(L_t) XOR v_t, where u_t,v_t depend only on initial bits strictly to the right of L_t and the independent flag field. All prior paired samples also depend only on those higher initial bits and flags. The shared pivot remains a fresh fair bit even after conditioning on the whole paired past and E_t=u_t XOR v_t. Hence each current marginal sample is fair independent of that conditioned information, and

    H(I_t,J_t | paired past)=H(I_t,E_t | paired past)=1+H(E_t | paired past).

Each separate trace is iid fair, so extending each marginal prefix adds1 bit of entropy. Extending the joint prefix adds the displayed1+conditional-error term. Subtracting joint entropy from the sum of marginal entropies proves the increment identity;telescoping proves the total. This argument establishes unconditional information growth, unlike G108's result conditioned on the entire environment.

The relevant property is a common unused pivot relative to the paired history, not merely two iid marginal traces. Adaptive paths, reused finite-ring pivots, state-dependent flags and nonterminating right chains are outside the proof. Biased initial rows do not supply the fair-bit baseline. This gives no closure of the error history and no asymptotic information rate.

**GF0-GF2 preregistered NOT RUN.** Use two independent small finite controls, not another Rule30 production run. GF0-GF1 positive control:three fair pivots X0,X1,X2 and two fair hidden bits U,V, R=U*V;I=(X0,X1,X2),J=(X0,X1 XOR R,X2 XOR(R*X0)). All32 histories have equal weight. Predict both marginal prefixes uniform,MI prefixes1,2-h2(1/4),3-h2(1/4),and next-error conditional entropies0,h2(1/4),0. Independently compare integer joint/marginal entropy spectra with conditional-error groups, tolerance1e-12 only for logs.

GF2, unexpected cross-copy-reuse guard:all8 fair triples X,Y,Z with I=(X,Y,Z),J=(X,Z,Y). Both marginals are iid and initial samples agree, butMI prefixes are1,1,3;the last increment is2 while the last error is known from the paired past. The formula would predict1 there and must fail. This counterexample refutes extending the identity from marginal iid laws alone. Publish before execution. It is a scope control, not a Rule30 counterexample.


**GF0-GF2 outcome (2026-10-06 21:40 BST).** Executed after proof,predictions and instrument publication through439744b. PASS:the32 positive histories have uniform marginal prefixes,MI1,2-h2(1/4),3-h2(1/4),and conditional-error entropies0,h2(1/4),0;the increment identity agrees within1e-12. The unexpected8-history reuse guard has MI1,1,3 and zero final error uncertainty,yet final MI increment2. It refutes extending the identity from marginal iid laws alone. The general Rule30 result rests on the written common-fresh-pivot proof,not on extrapolating toy cases. Independent review verified by Local L075;no limit or rate inferred from the controls.

### G120. Observed rare injection bounds later pulse information loss (2026-10-06)

**Status:** pulse-model entropy bound; RB0-RB2 pass, reviewed by Local L076. Corollary of G119, conditional on its scope. The asymptotic statement is a liminf bound, not existence or evaluation of an information-rate limit. It does not concern repeated races or the selected Rule30 seed.

In the common-input fair isolated-pulse model, F=E1 is observable from K1 and P(F=1)=1/8. If F=0 the pulse changes no cell, and subsequent synchronous evolution preserves equality of the entire configurations. For t>=2 the paired past contains F. Thus

    H(E_t | paired past)=P(F=1)*H(E_t | paired past,F=1)<=1/8.

Here the second conditional entropy is averaged over histories within the injected branch. Dependence between F and the initial source bit causes no problem:the weights in conditional entropy average to the unconditional branch probabilities. The bound uses both F's measurability from the past and the zero-error noninjected branch.

G119 therefore gives

    M_t-M_(t-1)>=7/8 for t>=2,
    M_T>=2-h2(1/4)/2+(7/8)*(T-1) for T>=1.

Using G118's exact six-sample result gives the sharper finite bound

    M_T>=6-h2(1/4)/2-h2(3/8)/16+(7/8)*(T-5) for T>=5.

Consequently liminf_(T->infinity) M_T/(T+1)>=7/8. Mutual information per sample is also at most1 by the marginal entropy bound. This does not prove the normalized sequence converges, determine its limit, or control the injected branch's damage lifetime. In particular,the seven-eighths lower bound partly comes from histories in which the pulse never injects;it is not a claim that active damage preserves seven-eighths of its information.

**Why observability is essential.** If F is not determined by the conditioned past, separating the branches also costs uncertainty about F. An event with small probability alone does not justify H(error|past)<=P(F=1). The scope guard below keeps the fresh-pivot information identity but hides F,so it must violate the rare-event budget rather than the identity itself.

**RB0-RB2 preregistered NOT RUN.** Positive control:64 equal-weight fair histories of X0,X1,X2,U,V,Q, with F=(1-X0)*(1-U)*V. Set I=(X0,X1,X2),J=(X0,X1 XOR F,X2 XOR(F*Q)). RB0 checks uniform marginals,P(F1)=1/8,and F observable after the first error. RB1 must give final conditional-error entropy1/8 and final MI increment7/8,showing the budget can be tight. Independently compare grouped error entropy with joint/marginal count spectra.

RB2, unexpected hidden-event guard:32 fair histories of X0,X1,U,V,Q with the same F,but I=(X0,X1),J=(X0,X1 XOR(F*Q)). The initial paired past does not reveal F. Predict next-error entropy h2(1/8)/2>1/8 and MI increment1-h2(1/8)/2<7/8,while both marginals remain iid and the fresh-pivot identity holds. The counterfactual that injection probability alone supplies the budget must fail. Tolerance1e-12 only for logarithms;publish before execution. No production scaling run.

**RB0-RB2 outcome (2026-10-06 21:48 BST).** Executed after9f37d68 published the proof,predictions and instrument. PASS:64 equality-case histories give observed F,probability1/8,error entropy1/8 and MI increment7/8. The32 hidden-F histories give error entropy0.271782221600 and increment0.728217778400,violating the rare-probability-only budget while satisfying the fresh-pivot identity. Independent grouped-error and joint-count calculations agree within1e-12. These toy controls check the scope;the all-time pulse bound follows from the written conditional-entropy proof. Reviewed by Local L076.

### G121. Finite-predecessor descent reduces counterexamples to roots, not bounded width (2026-10-06)

**Status:** paper proof and failed bridge, reviewed by Local L077. Responds to Cloud CL005's minimal-counterexample suggestion. No experiment or production run. This does not prove period-two exclusion or a prize result.

Let F be synchronous Rule30 on the infinite zero background. For a nonzero finite configuration x let [L,R] be its smallest support interval and w=R-L+1 its span, including internal zeroes. Its image has support endpoints exactly L-1,R+1:the outside adjacent triples are001 and100,both producing1,and all further outside triples are000. Therefore span(F(x))=w+2. This is an endpoint theorem,not a monotonicity theorem for the number of black cells.

F is injective on finite configurations. If two finite rows differ,let k be their rightmost differing site. Their values at k+1,k+2 agree,so their next values at k+1 differ:the left argument enters by XOR. Hence a finite row has at most one finite predecessor. If y has span w and a nonzero finite predecessor,that predecessor has span w-2. Iterating finite predecessors therefore terminates in a unique finite root r with no finite predecessor,and y=F^a(r) for a unique nonnegative age a. Its span is span(r)+2a. This is descent of ancestry,not descent along forward time.

Suppose a finite row is a counterexample to eventual-period-two exclusion at a fixed spatial column. Its finite predecessor,if present,is also a counterexample at that same column:the traces differ only by one initial time step. Thus every counterexample descends to a root counterexample,and a globally minimum-span counterexample must be a root. No phase assumption is needed because eventual alternation tolerates a time shift. Conversely,a root counterexample's forward images remain counterexamples. This gives an exact reduction to roots,without asserting any root is a counterexample.

**Where the bridge fails,for all widths.** Normalize support endpoints to0 and w-1,so for w>=2 there are2^(w-2) finite words. For w>=4 the images of normalized span-(w-2) words give exactly2^(w-4) distinct normalized span-w words,by endpoint growth and finite injectivity. Exactly one quarter have finite predecessors;the other three quarters,3*2^(w-4),are roots. For w=3 the sole image is111 from1;101 is a root. The span-one and span-two words are roots. In particular roots exist at every width. The predecessor reduction supplies no upper bound on a minimal counterexample's width and no induction step that covers the roots. The selected single-black-cell seed is already a root.

**Unexpected scope check,by hand.** The counterfactual "left permutivity gives a finite predecessor for every finite row" fails already on a single black cell:every nonzero finite image has span at least3,and the zero row maps to zero. Yet every finite output block has a compatible longer input block by right-to-left inversion (G104);compactness gives global predecessors. Such predecessors of this root must have infinite support. So full-shift surjectivity cannot supply the missing finite descent. This distinction is standard cellular-automaton background:see Jarkko Kari's [Cellular Automata tutorial](https://users.utu.fi/jkari/wp-content/uploads/sites/1251/2023/12/CAintro.pdf),slides89-100,on finite injectivity versus finite surjectivity and infinite predecessors. No novelty claim for finite injectivity;the present application identifies the precise failure of this proposed bridge.

**Next proof obligation.** A minimal-counterexample argument needs a different transformation that preserves eventual alternation while shrinking a root,or a theorem excluding every root. Removing an endpoint by hand has no established trace-preservation property:its causal cone eventually reaches any fixed observation column,so finite propagation alone guarantees no forever equality. The root count is not evidence of period-two survival. Ordinary inverse-time descent alone is closed as a complete proof route;other shrinking transformations remain open.

### G122. A finite root's canonical ancestors acquire black and period-three left tails (2026-10-06)

**Status:** symbolic inverse-map proof; reviewed by Local L077. Extends G121's failed descent by identifying the class it leaves. No new experiment. Does not exclude eventual temporal alternation at a fixed column.

Call a row right-quiescent when it is zero at all sufficiently large spatial indices;it may be infinite to the left. Rule30 is bijective on this class. To invert a right-quiescent output y,choose B beyond its rightmost possible nonzero cell,set x_B=x_(B+1)=0,and recursively solve

    x_(i-1)=y_i XOR (x_i OR x_(i+1))

for every i<=B. Set all x_i=0 for i>B. This produces a right-quiescent row satisfying F(x)=y at every site. Uniqueness follows from G121's rightmost-difference argument,which still applies to two rows bounded on the right even when both have infinite left tails. Taking a larger B only adds zero recursion steps,so the inverse is independent of the cutoff. No claim of bijectivity on the whole two-sided full shift is made.

For a finite nonzero output y,its canonical predecessor has an eventually constant left tail. Indeed below y's leftmost nonzero site,the recursion has y_i=0. On adjacent inverse bits (u,v)=(x_i,x_(i+1)),the descending spatial map is

    M0(u,v)=(u OR v,u).

Its complete graph is00->00,01->10,10->11,11->11. Every state reaches00 or11 within two steps. Thus the inverse is either finite (left tail0) or has left tail1. A G121 root has no finite predecessor,so its unique right-quiescent predecessor must be eventually black on the left. This is a necessity and sufficiency test for root status;an infinite black tail is not extra input freedom once the right-quiescent inverse is fixed.

Take one more canonical predecessor of such a root. In its far left recursion the output is now constantly1,so

    M1(u,v)=(1 XOR (u OR v),u).

The complete graph is00->10->01->00 and11->01. Every state joins the three-cycle within one step. Consequently the second canonical predecessor has a far-left spatial tail of least period3,with repeating bits001 up to phase. The tail is spatial,not a period-three source trace. As a direct independent local check,the cyclic triples of001 are100,001,010,and Rule30 maps each to1;the constant1 row maps to0. This verifies the far-left forward sequence001->1->0 without using the inverse-state graph. These two hand checks are exact truth-table evaluations,not an extrapolated probe.

**Unexpected scope check.** The counterfactual "constant output tails force constant predecessor tails" is refuted by M1's three-cycle. Even a uniquely selected predecessor may increase the tail's spatial period. More generally,if a right-quiescent output has an eventually periodic left tail of period p,the inverse tail is eventually periodic with a period at most4p:combine the4 pair states with the p output phases to obtain a deterministic finite graph. Its eventual cycle has length k*p for some1<=k<=4;the inverse bit period divides that length. No uniform bound over repeated inversions follows.

**Bridge interpretation.** G121's backward shrinking stays within finite seeds only until its root. Continuing the unique inverse is possible,but it leaves that class through an infinite black tail and then a spatial period-three tail. Thus lack of a finite predecessor is not lack of a global predecessor. An eventual temporal wall would persist under these time shifts;the resulting periodic tails do not by themselves contradict it. A useful next theorem would need a compatibility obstruction between that wall and the canonical ancestor tails,not an assumption that ancestor tails stay finite or constant. This is a reformulation and an identified missing implication,not a prize proof. Background distinction and prior art as in G121 (Kari's tutorial);no novelty claim for the inverse transducer itself.

### G123. Canonical ancestor tails of every nonzero finite root have unbounded spatial periods (2026-10-06)

**Status:** all-depth paper theorem using G121-G122's inverse construction; reviewed by Local L078. No measurement or new experiment. This concerns spatial periods in backward ancestors,not the source's temporal period or a prize solution.

Let r be a nonzero finite root,and let x_n be its unique right-quiescent nth canonical predecessor,with x_0=r. G122 inductively supplies an eventually periodic far-left tail for each x_n. Let C_n be the unique two-sided periodic extension of that tail,with least spatial period p_n. C_0 is the zero row,C_1 the one row,and p_0=p_1=1,p_2=3.

The extensions obey F(C_n)=C_(n-1). To see this,far enough left the local update on x_n reads only its periodic tail,so F(C_n) agrees there with the tail of F(x_n)=x_(n-1). Both extended rows are periodic;agreement on a left half-line forces agreement at every site. Thus F^n(C_n)=0 and F^(n-1)(C_n)=1. Zero is absorbing,so C_n first reaches zero after exactly n steps. This is exact for all n,not a horizon fit.

All n+1 rows C_n,F(C_n),...,F^n(C_n) are distinct. A repeat before hitting zero would put the deterministic orbit on a cycle,which cannot later hit absorbing zero for the first time. Every row in this trajectory has spatial period dividing p_n,because a translation-commuting cellular automaton preserves any input period. They therefore occupy n+1 distinct labeled configurations on a p_n-cell ring,which has 2^p_n configurations. Consequently

    n+1 <= 2^p_n,
    p_n >= ceil(log2(n+1)).

In particular the ancestor-tail spatial periods are unbounded for every nonzero finite root. Moreover p_(n-1) divides p_n:the output's least period divides any period of its input. Combined with G122,p_(n-1)<=p_n<=4*p_(n-1). The divisibility chain must have infinitely many strict increases. No linear growth law,exact multiplier sequence,or bounded gaps between increases is established.

**Independent perspective and unexpected check.** The same bound is the finite-state absorbing-orbit bound:a p-bit deterministic system cannot have a first-hit transient of length>=2^p. This checks the indexing without the inverse graphs. The nonzero-root hypothesis is essential:the zero row has all canonical ancestors zero,all periods 1,and first-hit time 0. Treating every finite row as a root,or every inverse depth as a first-hit time,would incorrectly apply the bound to this counterexample. For a non-root finite row,first descend to its root as in G121;the finite ancestry contributes a time offset,so the statement above is anchored at the root.

**What this bridges and what it does not.** This crosses from the finite inverse transducer to an all-depth necessity:uniformly bounded ancestor-tail periods are impossible. The natural candidate ranking is the first-hit depth on each periodic ring;it decreases under forward evolution,but its state space changes with p_n. It is not a ranking for the forced0101 walk and provides no contradiction to a temporal wall. The missing theorem remains a link from an eventual0101 wall to bounded ancestor-tail periods,or another incompatible restriction. Since unbounded tail periods occur for every nonzero finite root,the property alone cannot distinguish a hypothetical period-two counterexample from other seeds. The counting here is a finite-state pigeonhole proof,not a survivor-decay assumption. The finite-state pigeonhole bound is elementary. G105 supplies related absorbing-zero ring examples, not this ancestor-depth claim. No novelty claim for the general orbit bound.

### G124. Periodic Rule 30 rows that eventually reach zero have periods 1 or three times a power of two (2026-10-06)

**Status:** symbolic inverse-transducer theorem; reviewed by Local L078. No new experiment. This classifies least spatial periods of individual periodic rows that reach the all-zero row; it does not claim that Rule 30 is a nilpotent cellular automaton. It supplies no temporal-wall exclusion.

Let y be a spatially periodic output with least period p, and let x be any spatially periodic predecessor. Translation invariance implies p divides x's least period q. Inverting from right to left uses G122's pair maps

    M0(u,v)=(u OR v,u),
    M1(u,v)=(1 XOR (u OR v),u).

If y is nonconstant, p>=2 and one output symbol in a period is zero. Choose the period cut so the first descending symbol is that zero. The first map sends all four pair states into T={00,10,11}. The following map sends T to at most two states, regardless of the next symbol:

    M0(T)={00,11},
    M1(T)={10,01}.

Every later map preserves the upper bound on image size. Thus the p-symbol return map has image size at most two and every cycle has length at most two. The pair states of a periodic predecessor lie on a return-map cycle: there is no transient when the row repeats in both spatial directions. If the cycle length is k, the reconstructed bits have period dividing k*p. Combining k<=2 with p dividing q gives

    q=p or q=2*p.

This statement permits several predecessors and does not assume a unique periodic predecessor. The cut is just a phase choice, not a restriction on the row.

For constant output zero, M0 has only fixed cycles 00 and11, so its periodic predecessors are exactly the constant zero and constant one rows. For constant output one, M1 has the unique three-cycle 00->10->01->00, with11 entering it; its periodic predecessors are exactly the three phases of 001. Their least spatial period is 3. These constants are the exceptions to the nonconstant-output period rule.

**Classification.** Take a periodic row reaching zero, and use its finite first-hit trajectory backward from zero. If it is already zero or is the one row, its least period is 1. Otherwise the step before one has period 3. Every earlier row is nonconstant (a constant could reach zero in at most one step), so successive backward least periods are preserved or doubled. The original least period is therefore 3*2^k for some integer k>=0.

**Existence at every allowed period.** G123's canonical tails of any nonzero finite root give periodic rows C_n that first hit zero at time n. Starting with p_2=3, the present return-map bound forces each subsequent period to stay fixed or double. G123 proves these periods unbounded. Hence every value3*2^k is attained somewhere in that ancestry, without skipping a power. Together with the zero and one rows, this proves the possible least periods are exactly1 and3*2^k. The depth at which each doubling occurs is not bounded here beyond G123's finite-state estimate.

**Independent local check and unexpected guard, by hand.** The cyclic words give the exact forward trajectory

    001010 -> 011011 -> 010010 -> 111111 -> 000000.

Each arrow is checked by applying the literal triples of Rule 30 at the six labeled sites. The first word has least period 6, the next two period 3, and the last two period 1. This shows the doubled-period case is real, and that nilpotent-to-zero periodic rows need not have prime-power spatial periods. Separately,001->111 refutes applying q<=2*p to the constant-one output. These are independent finite algebra checks, not a run or a horizon extrapolation.

**Scope and prior art.** Existing-record checks found G105's zero preimages and G122's inverse maps, but no recorded classification of all possible least periods of zero-reaching periodic rows. Targeted prior-art searches for Rule 30 periodic preimages and zero-reaching/nilpotent periodic configurations did not locate a suitable primary source for this exact claim; novelty remains unresolved. The proof above is self-contained. Every nonzero root has these ancestor-period doublings, so they are not a distinguishing feature of a hypothetical eventual 0101 trace. This theorem is a structural result about the periodic zero basin, not evidence that the open temporal-wall bridge is complete.

### G125. Sideways periodic points correspond exactly to recurrent Rule 30 ring states (2026-10-06)

**Status:** symbolic correspondence using G22; reviewed by Local L079. Distinct lane: CONSTELLATION row 5, sideways dynamics. No computation or new ring census. The ordinary finite-state orbit argument is standard; no novelty claim.

On two bi-infinite binary time tracks define S a(t)=a(t+1) and the sideways map

    H(a,b)=(S a XOR(a OR b),a).

This is G22's map F, renamed H here to distinguish it from ordinary forward-time Rule 30, R. Fix m>=1. Then Fix(H^m) is in bijection with the recurrent states of R on a labeled m-cell ring. A recurrent state means a row lying on a temporal cycle, not a transient that will eventually enter one. Every track pair in Fix(H^m) is temporally periodic, with a common period no larger than 2^m-1. The same correspondence applies to periodic points of G22's induced ternary map.

**From a sideways periodic point to a ring.** Successive H iterates give neighboring columns extending leftward: H(a,b)=(c,a) is exactly the inverse-column equation c(t)=a(t+1) XOR(a(t) OR b(t)). If H^m(a,b)=(a,b), these columns close into a spatial period-m spacetime diagram. At each integer time t its labeled ring row u_t satisfies R(u_t)=u_(t+1), for all positive and negative t. Thus it is a bi-infinite orbit of a finite deterministic map.

Every row of such a bi-infinite finite-state orbit is recurrent. There is a uniform maximum transient length among the finitely many ring states. If u_0 were transient, u_(-N) would have to remain transient for at least N steps before reaching u_0, which is impossible for larger N. Recurrent ring states lie on cycles, and on that recurrent set R is a permutation. Therefore the temporal history is periodic in both directions and uniquely determined by u_0. There are at most 2^m-1 recurrent states:the all-one ring row maps to zero and is not itself recurrent. This gives the stated common temporal-period bound, not necessarily the least period of either individual track.

**From a recurrent ring state to a sideways periodic point.** A recurrent row has a unique bi-infinite temporal orbit on its cycle. Periodically extend each ring row to the whole spatial line and take the time tracks at sites 0 and 1 as (a,b). All inverse-column equations hold, so applying H m times shifts left by one spatial circumference and recovers (a,b). The two constructions are inverse:two adjacent tracks and their inverse-column iterates recover the labeled ring row, while a recurrent ring row determines its entire past and future. Labels and the distinguished time 0 are retained;this is a bijection with states, not merely with cycles modulo time or spatial rotation. Periods dividing m are allowed.

**Ternary scope.** Every H-periodic point lies in H's one-step image, since it is the image of H^(m-1) of itself. G22's conjugacy on that image therefore transfers this exact periodic-point description to the ternary induced dynamics. It does not transfer arbitrary transient two-track states into the ternary domain, nor assert a dynamical-entropy formula or classify all iterated images.

**Independent hand check and unexpected transient guard.** On a two-cell Rule 30 ring the four rows obey00->00,11->00,01->01,10->10. Hence there are exactly three recurrent states. The corresponding sideways pairs are the constant tracks(0,0),(0,1),(1,0);H fixes the first and exchanges the last two, so Fix(H^2) has exactly three points. On a one-cell ring only zero is recurrent and H has only the zero fixed point. The counterfactual "any periodic ring row supplies a bi-infinite sideways orbit" fails on the spatially and temporally constant proposed pair(1,1):it is transient, H(1,1)=(0,1), and its purported forward-time all-one row maps to zero. Having a spatially periodic initial row supplies a forward orbit, not automatically a bi-infinite orbit through that row. These are literal truth-table checks, not a simulation extrapolation.

**Result for the open lane.** Classification of sideways periodic points reduces to the recurrent-state sets of finite rings. No nonperiodic time track can lie on a finite sideways cycle. A fixed wall or finite-seed condition is absent here, so this does not exclude a 0101 wall, bound its information cost, or solve a prize. Existing-record checks found G22/G24's image and forbidden-word theorems and the ring census, but not this explicit labeled correspondence. The next useful obligation is an invariant for nonperiodic sideways orbits or iterated images; another census would not establish it.

### G126. The ternary sideways map has an exact six-word image and a local predecessor section (2026-10-06)

**Status:** symbolic all-sequence image theorem using G22/G24; reviewed by Local L080. No experiment or production run. Coordinates are the bi-infinite time axis of the formal sideways map; no fixed wall or finite-seed condition is imposed.

Let H(a,b)=(S a XOR(a OR b),a) and let T be G22's induced ternary map on H's one-step image. Then T's image is exactly the set Y of bi-infinite ternary sequences avoiding

    100, 101, 112, 0210, 0211, 0202.

Thus the image is a shift of finite type, not merely a language with the two necessary exclusions of G24. There is a shift-commuting local map R from Y to the full ternary shift with T(R(z))=z. It uses only z(t-1),z(t),z(t+1). In particular every p-periodic target in Y has a p-periodic predecessor (its least period may divide p). This is not a claim that R(z) lies in Y or that T is onto its own image.

**Reduction to binary predecessor constraints.** Decode a target z as (D,C), where C(t)=[z(t)=2], and D(t)=z(t) when C(t)=0, otherwise D(t)=1-C(t+1). A ternary predecessor is represented by a compatible pair(C,A). Its image must satisfy

    D(t)=C(t+1) XOR(C(t) OR A(t)).

When C(t)=0 this forces A(t)=e(t)=D(t) XOR C(t+1). When C(t)=1 the target equation is automatic and A(t) is free. G22's image compatibility for(C,A) requires, at every site with A(t)=1,

    C(t)=1-A(t+1).

Hence a forced 1 at a zero site of C requires the next A bit to be 1; a chosen 1 at a one site of C requires the next A bit to be 0.

**Necessity of the six exclusions.** Two consecutive zero sites of C cannot have e(t)=1,e(t+1)=0. In target symbols this is exactly100 or101 when C(t+2)=0, and112 when C(t+2)=1. Also a zero-one-zero block of C with e(t)=1 forces A(t+1)=1 and then A(t+2)=0. Its first target symbol is0, its middle symbol2, and its final forced e(t+2) must be0. The three ways to violate this last condition are0210,0211,0202. Each exclusion therefore holds for arbitrary predecessors, periodic or not.

**Sufficiency and local section.** For any target avoiding these words, define

    A(t)=D(t) XOR C(t+1)                    if C(t)=0,
    A(t)=[z(t-1)=0]                       if C(t)=1.

All target equations hold. Check compatibility only where A(t)=1. If C(t)=0 and C(t+1)=0, the forbidden triples ensure the next forced bit is1. If C(t)=0 and C(t+1)=1, the equation e(t)=1 means z(t)=0, so the prescribed next bit is1. If C(t)=1, its chosen bit is1 only after target symbol0. When C(t+1)=1 the next chosen bit is0 because its preceding symbol is2. When C(t+1)=0, avoidance of the forbidden quadruples makes its forced bit0. These exhaust the cases and prove compatibility. Encode(C,A) as R(z)(t)=2 when A(t)=1, otherwise C(t). G22's recoding then gives T(R(z))=z. This construction is valid on the whole bi-infinite sequence; no boundary completion or compactness assumption is hidden in it.

**Independent hand certificate and unexpected gap check.** For the repeating target0220, the formulas give C=0110,D=0010,A=1100 and predecessor code2210. A further binary predecessor B=0011 satisfies, by direct XOR/OR evaluation,

    H(1100,0011)=(0110,1100),
    H(0110,1100)=(0010,0110).

The last pair codes0220, independently certifying a target in the second image. Conversely the repeating target112 avoids100 and101, but forces A(t)=1,A(t+1)=0 at two successive zero sites of C. It has no predecessor under T. This refutes the counterfactual that G24's two old exclusions already describe the image exactly. These are finite algebra checks supporting the case proof, not a computational extrapolation.

**The image still has positive shift entropy.** Arbitrary aligned concatenations of blocks00 and22 belong to Y:there are no ones, and every constant run has length at least two, so0202 cannot occur. Distinct binary choices of n blocks give 2^n distinct words of length2n. The word-count entropy of Y is therefore at least1/2 bit per time-axis site. No exact entropy or limit-set entropy is evaluated. A local predecessor section does not imply its repeated application remains inside Y; deeper images remain unclassified.

**Record and scope.** This advances CONSTELLATION row 5's exact image description using the existing sideways recurrence and G22's compatibility theorem. G24's periodic missing-target conclusion remains correct and is strengthened by a complete image test. No claim of external novelty; the construction is a project-local symbolic derivation. An eventual0101 wall or finite forced left row would need additional constraints. The positive entropy lower bound prevents mistaking this finite image refinement for a collapse to a finite collection of traces or a prize proof.

### G127. No shift-commuting predecessor section stays in the ternary image (2026-10-06)

**Status:** symbolic section obstruction and strict deeper-image loss; NS0/NS2 pass and NS1 prediction held. Uses G126's image theorem; independent review pending. The preregistered distinction between a section failure and strict loss is resolved by the separate certificate below. Further image layers remain open.

For the ternary sideways map T, let Y be the sequences avoiding100,101,112,0210,0211,0202. The period-two points of Y are exactly the repeating words00,11,12,21,22. Literal evaluation of G22's rule gives

    00 -> 00,
    11 -> 22,
    22 -> 11,
    12 -> 22,
    21 -> 22.

Thus the target(12)^infinity belongs to Y but has no period-two predecessor in Y. Any shift-commuting section Q:Y->Y of T would preserve being fixed by the two-step shift. Its value at this target would be such a predecessor, a contradiction. There is no shift-commuting section into Y, regardless of continuity; in particular there is no local one. G126's section into the full ternary shift is unaffected.

**Unexpected guard: a deeper predecessor nevertheless exists.** The repeating word0102 lies in Y and T(0102)=1212. It is a period-four predecessor of the period-two target. G126's canonical section instead returns(01)^infinity, outside Y. Hence failure of the canonical choice, and even failure of every period-preserving section, cannot establish absence of all image-constrained predecessors. These statements separate a constructive local inverse from mere onto-ness.

**NS0-NS2 preregistration.** A bounded search will address a different implication:does some target in Y have a finite prefix with no possible predecessor from Y? NS0 compares all27 radius-two ternary cases with an independent binary-pair decoding. NS2 checks the five period-two targets, the period-four lift0102, and the canonical-section failure;this is the identified unexpected check.

NS1 considers prefix lengths n=1..7, in increasing order. Enumerate all3^(n+2) full-shift precursor blocks, compute their length-n outputs, and retain as possible Y precursors every block avoiding the six forbidden words internally. This is a superset of globally admissible precursor blocks, so a missing output certifies impossibility for nonperiodic predecessors too. Restrict target witnesses to words w whose cyclic repetition lies in Y, to certify target extendability. Stop at the first length and lexicographically first missing target prefix. Blind prediction:a witness occurs by length7. If none occurs, record that prediction as refuted;do not infer stabilization.

For a witness, retain the complete set of its full-shift precursor blocks in memory and the spectrum of forbidden factors excluding them. Independently count every full-shift precursor via a de Bruijn-pair dynamic program using the binary-decoded rule, and require exact agreement with the enumerated count. No sampling or floating arithmetic. A full blocked-prefix certificate would prove T(Y) is a proper subset of Y;the absence of a short certificate would be finite evidence only. Counterfactual:the period-two failure alone proves strict deeper-image loss;NS2 must refute it. Publish the predictions and instrument before execution. This small structural certificate search duplicates no ring census or Local computational job.

**NS0-NS2 outcome (2026-10-06 22:20 BST).** Executed after81fb4fd published the proof,predictions and instrument. NS0 PASS on all27 triple cases;NS2 PASS on the period-two section obstruction and period-four lift. NS1 HELD at n=6,so the blind witness-by7 prediction held. The search checked9,828 full-shift precursor blocks across n=1..6. The first missing periodic target prefix is022000. All six full-shift precursor blocks are

    22100000, 22100001, 22100002,
    22100022, 22100220, 22100221.

Each contains100. The independently decoded de Bruijn path count is also6. No floating arithmetic or sampling. Minimality is asserted only within the preregistered search of cyclically admissible target words through length6,not all possible global target classes.

**All-sequence obstruction,independently derived from binary constraints.** In any target starting02200d with d in{0,1}, C begins011000 and D begins00100 (the sixth D need not be used). The predecessor constraints force A(0)=1 because D(0)=0,C(1)=1. Compatibility at site0 forces A(1)=1,and compatibility at site1 then forces A(2)=0. The target equations at sites3 and4 force A(3)=A(4)=0. Encoding(C,A) forces precursor prefix22100,which contains100. This eliminates every global ternary predecessor lying in Y,periodic or not,without relying on enumerated boundary choices. Thus T(Y) forbids022000 and022001 in addition to Y's old exclusions.

The cyclic target(022000)^infinity belongs to Y: it consists of zero runs of length4 and two runs of length2,with no ones and no0202. Hence it has a full-shift predecessor by G126,but no predecessor from Y. Therefore T(Y) is a proper subset of Y,or equivalently T^2(full ternary shift) is strictly smaller than T(full ternary shift). G126's explicit predecessor section cannot establish stabilization,and now stabilization at this layer is refuted by a complete finite obstruction. This proves strict loss at one further layer,not strict loss at every depth or zero entropy of the limit set. Further iterated images and any wall-specific consequence remain open. Independent review pending.

### G128. The sideways limit set has every binary temporal trace as a factor (2026-10-06)

**Status:** all-depth compactness proof using G4.4/G22; independently verified by Local L081. No experiment or probability extrapolation. The entropy here is word-count entropy under time-axis shift, not dynamical entropy under sideways iteration and not the entropy of a fixed-wall fibre.

Let X be all pairs of bi-infinite binary time tracks, H(a,b)=(S a XOR(a OR b),a), and

    Lambda_H = intersection_(n>=0) H^n(X).

Let Lambda_T be the corresponding limit set of G22's ternary map. Then Lambda_H is exactly the set of adjacent-column pairs occurring in full Rule 30 spacetime diagrams on integer space and integer time. Projection onto either track is onto the full binary shift. Under G22's ternary recoding, the one-block map pi(z)(t)=[z(t)=2] maps Lambda_T onto the full binary shift. Consequently every ternary iterated image and the limit set itself have word-count entropy at least1 bit per time-axis site. Lambda_T contains nonperiodic time-axis sequences. No fixed finite initial seed is asserted to realize them.

**Spacetime equivalence.** A full spacetime diagram supplies predecessors of an adjacent pair at every sideways depth: shifting to two columns farther right and applying H recovers the chosen pair. Hence that pair lies in every H^n(X).

Conversely, membership in H^n(X) supplies a right extension of n columns satisfying the inverse-column equations at every time. All left columns are determined by forward H iterates. For each n there is therefore a spacetime strip extending arbitrarily far left and n columns right. Fill its remaining sites arbitrarily. The full diagram space {0,1}^{Z x Z} is compact. A convergent subsequence, or the equivalent finite-intersection argument, preserves the given two columns and every local rule equation:each finite spatial region is covered once n is large enough. The resulting diagram obeys Rule 30 at every integer space-time site. No coherent choice of predecessors at successive finite depths was assumed.

**Every binary trace is realizable in this unrestricted class.** Fix any desired bi-infinite binary column b(t). For each N, prescribe b on times-N through N. Start a row at time-N. Iterated left-permutivity gives the sample after k ticks as its initial bit at site-k XOR a function of higher initial bits. Fix the initial positive-index bits and solve successively for sites0,-1,...,-2N, as in G4.4. This realizes the desired finite window;all other initial bits may be zero. Evolve forward on the whole spatial line, and fill times earlier than-N arbitrarily.

Compactness now gives a full spacetime diagram whose source column is b(t) at every integer time:each prescribed value and each local rule equation is eventually enforced in these diagrams. The finite-window seeds may differ with N and grow in width. Their compact limit need not have finite spatial support at any chosen time. Spatial translation makes the same argument apply to either track of an adjacent pair. Thus both projections of Lambda_H are onto the full binary shift.

**Ternary factor and entropy bound.** H's one-step image I is invariant under H, and G22 conjugates H restricted to I with T. The nested images starting from I have the same intersection as those starting from X, because H^n(I)=H^(n+1)(X). Therefore the conjugacy maps Lambda_H onto Lambda_T. In the recoding, the second binary track is exactly[z(t)=2], so its surjectivity is a one-block factor statement. Every length-N binary word is the pi-image of a length-N ternary word in Lambda_T;distinct binary words require distinct ternary words. There are at least2^N such words, proving the entropy lower bound. Every finite iterate contains Lambda_T and inherits it. If b is nonperiodic, any preimage under pi is nonperiodic, proving nonperiodic sequences exist in the limit set. This says nothing about recurrence or periodicity under T itself.

**Unexpected fixed-wall guard, checked algebraically.** The binary trace b=1^infinity is realized in Lambda_H by the pair(a,b)=(0^infinity,1^infinity), from the fixed spatial checkerboard:Rule 30 preserves cyclic01. But the pair(a,b)=((01)^infinity,1^infinity) is not even in H(X). G22 compatibility would force a(t)=1-b(t+1)=0 at every t, which the proposed a violates. Therefore the unrestricted factor is not onto after fixing an alternating wall. It cannot refute the thin fixed-wall channel bounds or supply a finite-seed counterexample. This is the identified unexpected check.

**Implication for the active route.** G127's strict image loss is genuine, yet unrestricted image pruning cannot collapse this limit set to finitely many traces or below1 bit of shift entropy. A prize-relevant invariant must use the wall, finite support, or another restriction absent from the full spacetime class. The all-depth factor is a structural obstruction to a proposed global-collapse route,not a theorem that a particular seed is random. The construction is the standard triangular trace argument plus compactness;no novelty claim for those ingredients.


### G128.1. Known period-two closure obstruction and the missing implication (2026-10-06)

**Purpose and prior art.** Audit whether an alternating wall can be closed by giving all columns its temporal period. This is a known obstruction, not a new prize lead: Wolfram, [A New Kind of Science, notes to page 267, printed page 954](https://files.wolframcdn.com/pub/www.wolframscience.com/nks/nks-ch6.pdf#page=83), reports three Rule 30 configurations with temporal period dividing two, the same count as for period one. The following exact graph explains that count without another census.

Encode the temporal words 00, 01, 10, 11 as 0, 1, 2, 3 respectively. The sideways map H(a,b)=(S a XOR (a OR b),a) acts on these sixteen ordered pairs as follows. This table is a hand substitution into the rule, not an experimental result.

| a / b | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| 0 | (0,0) | (1,0) | (2,0) | (3,0) |
| 1 | (3,1) | (3,1) | (1,1) | (1,1) |
| 2 | (3,2) | (2,2) | (3,2) | (2,2) |
| 3 | (0,3) | (0,3) | (0,3) | (0,3) |

The only recurrent states are (0,0) and the cycle (0,3),(3,0); every other state enters that set within three steps. A full diagram periodic in time with period dividing two supplies a bi-infinite spatial orbit of this finite graph. Every state in such an orbit is recurrent: arbitrarily long predecessor paths in a finite deterministic graph must contain a cycle, which cannot exit to a transient state. Therefore the only whole-row configurations are all zero and the two spatial checkerboards. All three are stationary in time.

**The companion test is already covered by G27.2.** If a is alternating and b also has eventual temporal period dividing two, start after their common settling time. G22's compatibility b(t)=1 implies a(t)=1-b(t+1). It permits only b=00 or b=a. In either case one H step forces the immediate left column to be constantly one, and subsequent steps force the stationary checkerboard left tail. This is incompatible with an initially eventually-zero left row. G27.2 already excludes any eventual periodic adjacent companion under that finite-left assumption; the sixteen-state audit recovers a special case rather than improving it.

**Unexpected scope check and stopping decision.** G128 nevertheless realizes an alternating single column in some unrestricted full spacetime diagram. Thus that column does not license a globally period-two diagram or a period-two companion. Spatial checkerboards having period two does not make their temporal period two. This is the identified independent scope check. No numerical experiment was needed. The attempted period-two closure shortcut is closed; extending periodic graph censuses would not address the aperiodic companions required by G27.2. The next useful obligation remains a wall-sensitive restriction that applies to those companions without assuming the periodicity to be proved.


### G129. The finite-left wall fibre is a compact constraint class at each fixed radius (2026-10-06)

**Status and target.** Symbolic bridge from G128 to the finite-left boundary problem; independently verified by Local L083. No experiment or novelty claim for compactness. Existing record: G27.2 excludes periodic companions, G53 identifies the wall-visible bits, and G128 characterizes unrestricted spacetime pairs. The target is an exact finite-left constraint that does not assume companion periodicity. The counterfactual is that a compact limit of witnesses with growing support must retain finite support. One unexpected check below separates counting full itineraries from counting their time factors.

Use one-sided time t>=0. Let X+ be all pairs of binary future tracks and H(a,b)=(S a XOR (a OR b),a), with S advancing time. Let Lambda+ be the intersection of H^n(X+) over n>=0. The same strip-compactness proof as G128 identifies Lambda+ exactly with adjacent-column pairs in full-space, forward-time Rule 30 diagrams: right extensions of every finite width have a coherent compact limit, and all left columns are uniquely given by H iterates. This does not require any periodicity or a past before time zero.

Fix any prescribed wall tau and integer L>=0. Define

    B(L,tau) = { (a,b) in Lambda+ : a=tau,
                 first_track(H^d(a,b))(0)=0 for every d>L }.

**Exact boundary interpretation.** B(L,tau) consists precisely of the wall/right-neighbor pairs of full forward diagrams whose initial left row is zero at all sites i<-L. There is no bound on the initial right row. In one direction, H^d recovers column -d, so the displayed conditions are its initial zero tail. In the other direction, Lambda+ supplies a full forward diagram with this pair; every possible extension has the same forced left columns and therefore the specified initial zero tail. This is a left-support condition, not a finite global seed condition.

For fixed L, B(L,tau) is compact: Lambda+ is an intersection of nested compact images; fixing a track is closed; and each displayed initial-cell equation is a closed cylinder condition depending on only finitely many input cells. Their countable intersection is closed. All finite-left pairs form the union of these classes over L. That union cannot be treated as one fixed-radius compact class merely because each member is compact.

**Finite-box alternative.** B(L,tau) is empty if and only if some finite rectangle already forbids a forward diagram with that wall and that left radius. Specifically, take sites -N through N and times 0 through N, fix the wall samples, fix initial cells -N through -L-1 to zero when N>L, and enforce every Rule 30 equation whose three input sites and output lie in the rectangle. Leave the right initial row unrestricted. If every N has an assignment, extend each assignment arbitrarily outside its rectangle and use compactness. Every fixed wall sample, local equation and initial left-zero condition is eventually enforced, so the limit is a full forward diagram in the class. The converse follows by restriction. Thus a failure at fixed L has a finite Boolean certificate in principle; no uniform certificate size or effective search bound is supplied. Certificates for a few radii do not prove emptiness for every radius.

**Visible itineraries have a finite cardinality bound at fixed L.** Observe b only at white wall times. There are at most 2^L such complete visible itineraries in B(L,tau). Choose the L initial left bits. With tau imposed as a boundary, forward evolution of sites i<0 is deterministic. Write its nearest-left trace as ell(t). At a white time, the wall equation forces b(t)=tau(t+1) XOR ell(t). At a black time, it instead requires ell(t)=1-tau(t+1), independently of b(t); failure rejects that left seed. Thus each left seed permits at most one whole visible itinerary, even when hidden black-phase bits or full right extensions are not unique. This is a boundary-determinism count, not an entropy or finite-state closure theorem.

**Counterfactual and unexpected check.** Initial rows with ones at -L,...,-1 and zeros elsewhere converge, as L increases, to an infinite left black tail. Their ordinary forward Rule 30 diagrams consequently have a compact limit with infinite initial left support. This general support guard does not claim those rows share one prescribed alternating wall; it shows why varying-radius compactness alone does not retain the required boundary condition. Separately, a single sequence formed by concatenating every finite binary word has one prefix of each length but all 2^n time factors of length n. Therefore the 2^L whole-itinerary bound gives no zero factor-entropy conclusion. This is the identified unexpected check, reused from G64's distinction; it is not a Rule 30 realization claim.

**Remaining bridge.** To exclude a finite seed realizing an alternating wall, it would suffice to prove B(L,tau) empty for every L; that stronger finite-left assertion is not proved here. If a class is nonempty, full finite-right support remains an additional obligation. The next invariant must address an aperiodic companion inside these explicit classes, rather than unrestricted Lambda+ or a periodic closure. No new channel census is requested.


### G130. Fixing the initial right tail gives a unique left seed for every wall trace (2026-10-06)

**Status and purpose.** Exact coordinate reduction of G4.4's triangular inversion; independently verified by Local L084. This is not a new left-permutivity theorem or a solution of the wall problem. G129 leaves finite right support as an additional constraint. Here the target is to identify exactly what that constraint can and cannot exclude. No experiment. Counterfactual: finite initial right support alone restricts possible temporal walls, or exact finite-prefix realizations guarantee a finite left seed. The delayed single-cell example below independently rejects the latter implication at a fixed right tail.

Fix the initial values r_i at all sites i>=0. For any desired one-sided wall tau with tau(0)=r_0, there is exactly one initial left word u=(x_-1,x_-2,...) whose full forward Rule 30 evolution has x_0(t)=tau(t) for every t>=0. The map from u to the future trace (tau(1),tau(2),...) is a homeomorphism of binary sequence spaces. No periodicity premise is used.

**Proof.** G4.4 gives, for each n>=1,

    x_0(n) = x_-n(0) XOR P_n(x_(-n+1)(0),...,x_n(0)).

The unique path carrying the leftmost input to the observed output contributes by XOR; all other terms use higher initial indices. Fix r and solve x_-1, then x_-2, and so on, using the prescribed tau(n). Each step has exactly one solution and does not alter earlier samples. These compatible finite assignments define one infinite initial row, and its ordinary forward evolution realizes every sample. Uniqueness follows from the same successive solving. Both directions are continuous: a trace prefix of length N uses only the first N left bits and r_0,...,r_N; conversely those N left bits are determined by that trace prefix and the same finite right data. This is an initial-row/trace coordinate map, not a conjugacy between Rule 30 evolution and a shift on a fixed-tail space, since the initial right tail need not remain fixed after an update.

**Finite-right support is compatible with every wall in isolation.** Set r_0=tau(0) and r_i=0 for all i>0. The construction realizes every tau, including an alternating wall, with this finite initial right tail. Its forced left word may be infinite. Thus no obstruction based only on requiring finite initial right support can exclude a temporal word when arbitrary infinite left support is allowed. This does not assert that a chosen companion from G129 has a finite-right extension.

**Exact finite-global criterion.** For a prescribed tau, let r range over all eventually-zero initial right tails with r_0=tau(0), and write u_r for the uniquely solved left word. A finite global seed realizes tau if and only if at least one u_r is eventually zero. Necessity applies uniqueness to that seed's right tail; sufficiency joins the two finite tails and invokes the construction. Hence the joint boundary problem is a zero-tail question for this canonical family, rather than existence of an unrestricted right extension. This supplies no uniform zero-tail test, search bound, or exclusion theorem. The finite-left condition of G129 still has to hold for the same row.

**Unexpected fixed-tail finite-prefix guard, exact.** Take the initial row x_i=1 for i<0 and x_i=0 for i>=0. Rule 30 sends it in one tick to the single black cell at site 0: triples 111 and 110 give zero on the left, triple 100 gives one at the wall, and triples 000 give zero on the right. Let tau be this row's wall trace: its first sample is zero and its later samples are the single-cell wall trace shifted by one tick. With the fixed initial right tail all zero, this tau has the unique left seed 111..., so no finite left seed with that same right tail realizes it forever.

For every N>=1, truncating that left seed to ones at -N,...,-1 yields a finite seed with the same right tail and exactly the same wall through time N. Its first wrong wall sample is at time N+1: the higher initial indices agree, while the fresh XOR pivot x_(-N-1)(0) differs. Thus arbitrary finite horizons are realized with growing left support even though no fixed finite left seed works for that fixed right tail. No claim is made about alternative right tails for this tau, or about periodicity of the single-cell trace. The check uses both the explicit one-tick truth table and the independent triangular uniqueness mechanism.

**Next obligation.** For an alternating or eventually alternating prescribed wall, prove a property of u_r uniform over finite r that prevents an eventual zero tail, or identify a counterexample. Periodic companion assumptions, unrestricted trace existence and growing finite-prefix realizations do not supply that property. This is a reformulation of the missing proof, not a claim that the canonical words have been classified.


### G131. The Sturmian exclusion survives every finite block factor (2026-10-06)

**Status and purpose.** Symbolic extension of RULE30-PRIZE.md section 8.57's Theorem E; independently verified by Local L085. No experiment. The target is the open rotation-code lead in PERIOD-TWO.md question 7, without assuming a periodic companion. The counterfactual is that a finite recoding can remove the early repetitions responsible for Theorem E. The proof retains the exact fixed margin. Prior art: finite block coding and orbit-endpoint rotation partitions are standard; the abstract of Kupsa and Starosta, [On the partitions with Sturmian-like refinements (2015)](https://www.aimsciences.org/article/doi/10.3934/dcds.2015.35.3483), discusses this class and stronger refinement results. Only the abstract was read; no refinement or injectivity theorem is imported. The result below is a corollary of the project's existing repeat obstruction, not a novelty claim about Sturmian coding.

**Theorem.** Let g be any irrational Sturmian sequence, with any phase. Let F be any binary function of a fixed block of width w+1, and set c_s=F(g_s,...,g_(s+w)) for s>=0. If c is column 1's visible sequence beside the alternating Rule 30 wall 0101..., the forced initial left row cannot be eventually zero. No injectivity, nonconstancy or aperiodicity premise is imposed on F.

**Proof.** Section 8.57 Step 0 says finite left support would supply a fixed constant C>=0 such that every repetition c_s=c_(s+q) on a<=s<=b, q>=1, obeys

    b <= 2a+q+C.                         (repeat bound)

Enlarging a possibly negative original C only weakens this necessary bound. Suppose g_s=g_(s+q) on a<=s<=e. If e>=a+w, then c repeats on a<=s<=e-w, so e<=2a+q+C+w. If e<a+w, the same inequality holds automatically. Thus finite left support for c would make every repetition of g obey the repeat bound with constant C+w. The continued-fraction argument in section 8.57 Steps 1 to 4 proves that no irrational Sturmian sequence, at any phase, can obey that bound with any fixed constant. Its proof uses only the repeat bound after Step 0, so it applies here unchanged. This contradiction proves the theorem. The margin is w, not a scale-dependent loss.

A finite block function using shifts m,...,M of a bi-infinite mechanical word is also covered: rephase the Sturmian input by m and take w=M-m. Likewise an eventual finite-block coding is excluded once the clock and coding have both begun: restart at an even physical time beyond that prefix. Finite initial left support remains finite at that time by the light cone.

**Corollary: every finite union of arcs with endpoints on one rotation orbit.** Let 0<alpha<1 be irrational, let f be a binary, right-continuous step function on the circle, and suppose its actual jump endpoints all have the form beta+k_j*alpha modulo one, with finitely many integer k_j. Then c_s=f(theta+s*alpha) is excluded beside 0101... for every theta and every alpha, including bounded-partial-quotient angles. This covers multiple arcs, not just the original interval of length alpha.

Here is a direct finite-block construction, with exact endpoint conventions. Put y=x-beta and g(y)=1 on [1-alpha,1), zero elsewhere. A binary circular step function has an even number of jump endpoints. Over GF(2), form the Laurent polynomial

    Q(z)=sum_j z^(k_j)=(1+z)*P(z).

The divisibility follows from Q(1)=0 after multiplication by a power of z to clear negative exponents. For each nonzero coefficient P_k define

    h(y)= XOR_k g(y-(k+1)*alpha).

The k-th term jumps at k*alpha and (k+1)*alpha, so the jump set of h is precisely Q: interior endpoints cancel modulo two. Thus f(beta+y) and h(y) have the same jumps and differ by one constant bit. Right-continuity makes the equality hold at the endpoints as well. Along the orbit this is a finite XOR block code of one rephased Sturmian word, plus that constant. The theorem therefore applies. A constant f is the empty-code case and is covered too.

**Unexpected degeneracy check.** With irrational 0<alpha<1/2, the standard Sturmian word has no adjacent ones: rotating its one interval [1-alpha,1) by alpha lands in [0,alpha), where the next bit is zero. Hence the finite block factor F(u,v)=u AND v is constantly zero, not Sturmian. The proof still excludes it, directly through the repeat bound. Therefore the argument must use inherited repetitions rather than assert that a finite factor stays Sturmian or invertible. This is the identified independent check.

**Scope and lead status.** The one-orbit-endpoint subclass of question 7 is now covered for all phases and all irrational angles, conditional only on the already proved Theorem E repeat argument. Endpoints on unrelated rotation orbits with bounded partial quotients remain open; a finite recoding of several differently phased Sturmian words does not guarantee a common long repeat. Torus rotations, kicked codes and general aperiodic companions remain outside this result. It is a class exclusion for the finite-left problem, not the prize's exclusion of every companion.


### G132. Circle-covering codes and one-character torus observables are excluded (2026-10-06)

**Status and target.** Corollary of G131 and G27.2; independently verified with G131 by Local L086. No experiment or novelty claim for integer characters. Target: clarify which multi-orbit and torus codes the finite-block argument already excludes. Counterfactual: a circle covering or additional unobserved torus coordinates automatically evade the Sturmian obstruction. A genuine two-coordinate box below is the unexpected scope check.

**Statement.** Let the torus orbit be x_s=theta+s*omega modulo one in each of d coordinates. Fix an integer vector v and the circle projection

    h_v(x)=sum_j v_j*x_j modulo one,
    beta=h_v(omega).

Observe c_s=psi(h_v(x_s)). If beta is rational, every such deterministic observable psi gives a periodic c and is excluded beside the alternating Rule 30 wall with finite initial left support. If beta is irrational, the same exclusion holds whenever psi is a binary finite-union-of-arcs code whose jump endpoints lie on one beta-rotation orbit. Arbitrary fixed choices at the endpoints are allowed. In both cases no assumption is made about periodicity of the actual right-neighbor trace at its hidden phases.

**Proof.** Integer coefficients make h_v well-defined on the torus. Direct addition gives

    h_v(x_s)=h_v(theta)+s*beta modulo one.

For rational beta with denominator q these projected points repeat every q samples, hence c is periodic. The corresponding nearest-left trace is periodic: at even physical times it is 1-c_s, and at odd times it is one. G27.2 excludes this pair for finite initial left support, independently of the right half.

For irrational beta, the projected observable is exactly a circle rotation code of the class in G131, so its finite-block exclusion applies for every starting phase. If endpoint values differ from the half-open convention used there, each endpoint is visited at most once: two visits would make a nonzero multiple of beta integral. There are finitely many endpoints, so the code eventually agrees with the half-open code. G131's eventual-factor clause therefore preserves the exclusion. This also explains why endpoint exceptions do not create a new companion class.

**Circle coverings give a concrete multi-orbit case.** In dimension one take v=2, irrational alpha as omega, and beta=2*alpha modulo one. Let psi be the standard Sturmian interval [1-beta,1). Then f(x)=psi(2*x modulo one) is a two-arc observable for the original alpha rotation. Its endpoint set is

    {0, 1/2, -alpha, 1/2-alpha} modulo one.

The two original alpha-orbit classes represented by 0 and 1/2 are distinct: an equality 1/2=k*alpha modulo one would make alpha rational for nonzero integer k. Thus f does not have all endpoints on one original orbit, yet its sampled code is Sturmian for the projected angle beta and is excluded. More generally any integer circle covering can be used. This narrows part of the unrelated-endpoint lead; it does not exclude arbitrary unrelated endpoints without such a quotient structure.

**Unexpected genuinely multidimensional guard.** On the two-torus, let f(x,y)=1 when both x and y lie in [0,1/2), zero otherwise. This observable cannot be a function of any single integer character h_(a,b). A function of that character would be invariant under every translation (b*t,-a*t), since the character changes by zero. If b is nonzero, choose x just below 1/2 and y=1/4; a sufficiently small such translation crosses the x boundary while keeping y interior, so f changes. If b=0 and a is nonzero, a vertical translation changes f while leaving the character fixed. The zero character would require f constant. All cases contradict factorization. Therefore this corollary makes no claim about genuinely two-coordinate box codes, nor about the general torus lead. This is a geometric scope check, not a Rule 30 counterexample or a claim that a box code supplies a finite witness.

**Resulting boundary.** The class exclusion includes finite recodings after a one-circle projection, even when the original partition has multiple orbit classes or the underlying motion has several torus coordinates. General partitions using independent coordinates, arbitrary unrelated circle endpoints and kicked observables remain open. No uniform finite-left exclusion or prize solution follows.


### G133. Golden-angle codes cannot be rescued by super-geometrically separated kicks (2026-10-06)

**Status and target.** Quantitative extraction from Theorem E's existing continued-fraction proof; independently verified by Local L087 (finite visit deadlines, scale inequalities and S31 controls). No experiment. G131/G132 are verified by Local L085/L086. Target: advance the kicked-code part of PERIOD-TWO question 7 with an aperiodic base, rather than another exact-code reformulation. Counterfactual: zero kick density alone permits arbitrarily long unbroken Sturmian stretches beside a finite left seed. The conservative constants below are not optimized. The dyadic-kick guard prevents an entropy or all-kicks exclusion claim.

Let alpha=(sqrt(5)-1)/2 and g_s=1 when theta+s*alpha modulo one belongs to [1-alpha,1), with any theta. Assume the Rule 30 wall is 0101... from time zero and the initial left row is zero beyond radius L.

**Finite repetition lemma.** For every integer C>=0, a golden-angle Sturmian prefix through index

    N=84*(C+4)

cannot obey the finite repeat bound b<=2a+q+C for every repetition g_s=g_(s+q) on a<=s<=b with b+q<=N. In particular a visible companion cannot agree with such a Sturmian word through index 84*(L+4). The L=0 left seed already fails the first black-time equation; for L>=1 Theorem E Step 0 supplies a repeat constant no larger than L.

**Finite-horizon proof.** Use section 8.57's convergent notation q_n, delta_n, K_n and the first two visit times h,h' to K_n. For a fixed q=q_n, if N>=4q+3C+8, the finite repeat bound alone forces

    h <= q+C+2,
    h' <= 2h+q+C+4.

Indeed, if h>q+C+2, the repetition from 0 through q+C+1 violates the bound; all compared samples lie within N. After the first visit, if h'>2h+q+C+4, the repetition from h+1 through 2h+q+C+3 violates the bound. Its last compared index is at most 4q+3C+7, using the first inequality. These are exactly Theorem E's two visit inequalities, obtained without assuming the second visit was already observed. As in that proof, returns to K_n are at least q_(n+1) apart. Thus

    q_(n+1)-q_n-C-4 <= h(n) <= q_n+C+2.       (visit bounds)

Choose n minimally so q_(n-1)>2C+8. For the golden angle all partial quotients are one. The separation argument of Theorem E Step 4, applied at n and n+1, gives

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

Here its prerequisites are just the visit bounds at n,n+1,n+2 and q_(n-1)>2C+8: the two arcs at successive scales are disjoint and closer than delta_(n-1), and the only possible signed return in the bounded visit-time difference is -q_n. No extra hypothesis about the Rule 30 orbit enters this separation step.

The visit bounds and first identity give h(n)>=q_(n-1)-C-4. The second identity and the upper visit bound at n+2 give h(n+1)<=q_n+C+2. Combining these with the first identity yields q_(n-1)<=2C+6, a contradiction.

All three scales are present in the stated horizon. Minimality and the Fibonacci recurrence imply q_(n-1)<=4C+16 and q_(n+2)<=5q_(n-1)<=20C+80. Therefore

    4q_(n+2)+3C+8 <= 83C+328 < 84*(C+4).

This proves the finite repetition lemma.

**Unbroken stretches at later times.** If the visible companion agrees with a golden-angle Sturmian word from visible index a through b, restart at physical time 2a. The left-zero radius is then at most L+2a by the light cone, and the wall has the same phase. The finite lemma, with this larger radius and arbitrary rephased theta, requires

    b-a < 84*(L+2a+4).

This statement does not require the companion to be periodic or the rest of it to be Sturmian.

**Necessary kick-gap bound.** Suppose c equals a fixed golden-angle Sturmian word except at its actual disagreement indices k_0<k_1<.... Finite support requires infinitely many disagreements, since an eventual exact code is already excluded by G131. Before the first kick, the finite lemma gives k_0<=84*(L+4). Between consecutive kicks use a=k_j+1 and b=k_(j+1)-1. The preceding inequality yields the conservative integer bound

    k_(j+1) <= 169*k_j + 84*L + 505.

Thus schedules with unbounded ratios k_(j+1)/k_j are excluded. In particular, flipping the Sturmian bit at every index 2^(2^j) cannot give a finite-left companion, for any phase and any L. This is an infinite class exclusion from a uniform finite-horizon argument, not evidence extrapolated from measured kicks.

**Unexpected checks and limits.** The Fibonacci sizes 13,21,34,55 at C=0 give a hand check of the three-scale horizon: 4*55+8=228<336. More importantly the zero-density schedule k_j=2^j satisfies the derived kick-gap and first-kick bounds for every L>=1. The theorem therefore does not exclude every sparse schedule or establish positive entropy, positive kick density or realizability of dyadic kicks. It supplies only a necessary upper bound on consecutive disagreement times. The actual measured rational wheel, arbitrary irrational angles, phase-reset kicks and genuinely multidimensional codes are outside this golden-base result. These are the identified independent scope checks.


### G134. Bounded-type rotation codes require geometrically spaced corrections (2026-10-06)

**Status and target.** Symbolic extension of G133, independently verified by Local L088. No experiment or new numerical prediction. Theorem E and G2.2 supply the continued-fraction facts; G133 supplies the finite comparison deadlines. Target: remove the golden-angle restriction from the sparse-kick exclusion. Counterfactual: bounded partial quotients might still allow corrections with unbounded successive spacing ratios beside a finite left seed. The proof below excludes that possibility. This is a consequence of the existing repetition obstruction, with no general novelty claim.

Let alpha in (0,1) be irrational with every partial quotient a_j<=A, where A>=1 is an integer. For any phase theta let g be its standard half-open Sturmian code. Define

    K_A=8*(A+1)^4+3.

**Finite-prefix theorem.** For every integer C>=0, the prefix of g through index N=K_A*(C+4) cannot satisfy b<=2a+q+C for every repetition g_s=g_(s+q) on a<=s<=b with b+q<=N.

Use Theorem E's convergents q_n, errors delta_n, mismatch arcs K_n and first visit h(n). G133's finite comparison argument, valid for every irrational angle once these mismatch arcs have the stated form, gives

    q_(j+1)-q_j-C-4 <= h(j) <= q_j+C+2

whenever N>=4q_j+3C+8. Choose n minimally with q_(n-1)>T=2C+8. The initial denominator q_0=1 is below T. Minimality and q_j=a_j*q_(j-1)+q_(j-2) give q_(n-1)<=(A+1)*T. Thus

    q_(n+2) <= (A+1)^3*q_(n-1) <= (A+1)^4*T,
    4q_(n+2)+3C+8 <= K_A*(C+4).

The visit bounds therefore hold at all three indices n,n+1,n+2. If any of a_(n+1),a_(n+2),a_(n+3) is at least two, the corresponding visit bounds imply q_(j-1)<=2C+6, impossible. All three coefficients must consequently be one.

**Quantitative separation, including the finite-offset check.** Put D=2C+6. At j=n and j=n+1, the opposite mismatch arcs are disjoint, their combined length is |delta_(j-1)|, and the visit bounds place

    m=h(j)-h(j+1) in [-q_j-D,D].

Also m is nonzero and ||m*alpha||<|delta_(j-1)|. Best approximation forces |m|>=q_j. Since D<q_(j-1)<=q_j, this means m=-q_j-r with 0<=r<=D. If r>0, then r<q_(j-1), so the preceding best-approximation bound and the error recurrence give

    ||r*alpha|| >= |delta_(j-2)|
                 = a_j*|delta_(j-1)|+|delta_j|
                 >= |delta_(j-1)|+|delta_j|.

The triangle inequality on the circle now gives ||(q_j+r)*alpha||>=|delta_(j-1)|, a contradiction. Hence r=0 exactly, and

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

This finite-offset argument uses no unspecified sufficiently-large threshold or phase-dependent distance. It also supplies the explicit justification for G133's quantitative use of Theorem E Step 4. At the selected indices the standard mismatch description applies: n>=2; if n=2 then q_1>T forces alpha<1/8, and later convergent errors are smaller than both coding-interval lengths. The same assertion at n>=3 follows from the first convergent errors and their monotone decrease.

Finally the lower visit bound at n is h(n)>=q_(n-1)-C-4. The second identity and upper bound at n+2 give h(n+1)<=q_n+C+2. Substituting the first identity forces q_(n-1)<=2C+6, again a contradiction. This proves the finite-prefix theorem.

**Finite-left companion consequence.** Let the Rule 30 wall be 0101... and its initial left row be zero beyond radius L>=1. Theorem E Step 0 permits repeat constant C=L. Restarting at physical time 2a enlarges the left-zero radius to at most L+2a. Any matching stretch with this fixed-angle Sturmian code, rephased as necessary, obeys

    b-a < K_A*(L+2a+4).

For the actual disagreement indices k_0<k_1<... against a fixed base code, G131 already excludes finitely many disagreements. The finite-prefix theorem and the intervals between disagreements give

    k_0 <= K_A*(L+4),
    k_(j+1) <= (2K_A+1)*k_j + K_A*L + 6K_A + 1.

Thus unbounded ratios k_(j+1)/k_j are impossible for every bounded-type irrational angle, every phase and every finite left radius. In particular super-geometric flip schedules are excluded throughout this class. The sharper golden constant in G133 remains useful; this uniform class constant is deliberately conservative.

**Independent and unexpected scope checks.** The finite-offset check above is independent of G2.2's asymptotic eta argument and is the identified unexpected check. At A=1 this theorem gives K_A=131 rather than G133's 84, a consistency check without an optimality claim. The schedule k_j=2^j still satisfies the resulting necessary bounds for L>=1, so this argument establishes neither positive kick density nor positive entropy nor realizability. For unbounded partial quotients, the controlled denominator growth used to choose a linear horizon fails; this proof supplies no uniform linear bound there. Arbitrary phase-reset kicks, the measured rational wheel and genuinely multidimensional observables remain outside the claim.


### G135. A uniform Sturmian horizon also bounds phase and angle resets (2026-10-06)

**Status and target.** Symbolic proof, independently verified by Local L088; no experiment. G133 is independently verified by Local L087; G134 is verified by Local L088. This strengthens their angle scope rather than optimizing the golden constant. Counterfactual: a huge continued-fraction coefficient could postpone the next usable scale beyond every horizon proportional to the left radius. The finite repetition bound itself prevents that escape. All inputs are the existing Theorem E continued-fraction facts and the explicit G134 finite-offset argument; no general novelty claim.

**Uniform finite-prefix theorem.** For every irrational alpha in (0,1), every phase theta and every integer C>=0, its standard half-open Sturmian prefix through

    N=251*(C+4)

contains a repetition g_s=g_(s+q) on a<=s<=b with b+q<=N and b>2a+q+C. There is no bound on partial quotients in this statement.

Suppose otherwise. Put T=2C+8. Choose n minimally with q_(n-1)>T and put r=n-2. Then q_r<=T. At every usable scale j the finite comparison deadlines of G133 give

    q_(j+1)-q_j-C-4 <= h(j) <= q_j+C+2,
    q_(j+1) <= 2q_j+2C+6 < 2q_j+T,

provided N>=4q_j+3C+8. The second line is the crucial replacement for an externally assumed bound on partial quotients.

The starting scale r is usable, including its small-index cases. If r=0, q_1>T implies alpha<1/8; delta_0=alpha and the two mismatch arcs for period q_0=1 are disjoint, so Theorem E's break description and return gap at least q_1 hold. If r>=1, |delta_r| is at most min(alpha,1-alpha), making the same break description valid. Indeed, when a_1=1, |delta_1|=1-alpha; when a_1>=2, the recurrence alpha=a_2*|delta_1|+|delta_2| gives |delta_1|<alpha. Later errors decrease. Equality of an error with the shorter interval length merely makes the mismatch arcs touch at a half-open endpoint; it does not create an overlap.

Starting with q_r<=T, apply the growth inequality successively at r,r+1,r+2,r+3. Every application is justified within the fixed horizon, because the resulting bounds are

    q_(n-1) < 3T,
    q_n < 7T,
    q_(n+1) < 15T,
    q_(n+2) < 31T,

and

    4*(31T)+3C+8 = 251C+1000 < 251*(C+4).

Thus the visit bounds hold at n,n+1,n+2 as well. This is an induction on already bounded denominators, not a circular assumption that the later scales fit.

At those three scales, any coefficient a_(j+1)>=2 would give q_(j-1)<=2C+6, contradicting q_(n-1)>T. Hence a_(n+1),a_(n+2),a_(n+3) must all be one. The explicit separation in G134 applies at n and n+1: for m=h(j)-h(j+1), best approximation gives m=-q_j-u with 0<=u<=2C+6; a positive u<q_(j-1) would give

    ||(q_j+u)*alpha|| >= |delta_(j-2)|-|delta_j|
                         >= |delta_(j-1)|,

contrary to the distance across the opposite mismatch arcs. Therefore

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

Combining the lower visit bound at n with the upper bound at n+2 yields q_(n-1)<=2C+6, the final contradiction. The uniform finite-prefix theorem follows.

**Companion and reset consequences.** Beside a Rule 30 wall 0101... with initial left-zero radius L>=1, any interval [a,b] matching a standard irrational Sturmian code obeys

    b-a < 251*(L+2a+4).

The phase and angle may be chosen separately for each interval: restart at physical time 2a, use the light-cone radius L+2a and apply the uniform theorem with repeat constant C=L+2a. No relation between the different intervals' angles is required.

Consequently, if a companion is made of consecutive Sturmian-coded pieces with reset times 0=t_0<t_1<..., even allowing both phase and angle to change at each reset, it necessarily satisfies

    t_(j+1) <= 503*t_j + 251*L + 1004.

A final infinite piece is impossible. Super-geometrically separated resets cannot support a finite left seed. For actual disagreements k_j against one fixed irrational Sturmian base, the corresponding statement is

    k_0 <= 251*(L+4),
    k_(j+1) <= 503*k_j + 251*L + 1507.

This excludes super-geometric flips for every irrational base angle, including unbounded-type angles. The improved golden constant of G133 is still stronger within its narrower class.

**Unexpected independent checks and limits.** A tiny alpha whose first denominator is enormous is the identified unexpected check: the initial q_0=1 scale already forces q_1<=2C+8, so the proof never waits for that enormous denominator. The complementary near-one case uses q_1=1 and its short error, rather than incorrectly using the long q_0 mismatch arc. These endpoint-angle controls justify the uniform claim. Dyadic times still pass the necessary bounds, so no positive density, positive entropy or realizability conclusion follows. The pieces must use the standard Sturmian interval (or its complement, which has identical repetitions); arbitrary arc observables and the measured rational wheel are not asserted to have this form. This is a class exclusion for companions, not a prize solution.


### G136. Uniform recoding horizons include rational mechanical bases (2026-10-06)

**Status and purpose.** Symbolic corollary of G131 and G135; independently verified by Local L089. Dependencies G134/G135 are independently verified by Local L088. No experiment. Counterfactual: either a finite recoding margin or a rational limiting angle might evade the uniform horizon. The exact margin and a finite-prefix approximation settle both. This advances recoded/reset companions, not the missing entropy theorem. The inherited rotation-partition prior art is recorded in G131; no general novelty claim.

Let g_s be the standard mechanical code of theta+s*alpha modulo one in [1-alpha,1), now allowing every alpha in [0,1]. The endpoint angles give the constant zero and constant one codes. Let F be any binary function of a block of width w+1, w>=0, and put c_s=F(g_s,...,g_(s+w)). Define

    H(C,w)=251*(C+4)+250*w.

**Finite-prefix theorem.** For every integer C>=0, the prefix of c through index M=H(C,w) contains a repetition c_s=c_(s+q) on a<=s<=b with b+q<=M and b>2a+q+C. Neither injectivity nor nonconstancy of F is needed.

First extend G135 to rational and endpoint angles. Every finite prefix g_0,...,g_N of the specified mechanical code is also a prefix of an irrational mechanical code with slightly perturbed angle and phase. To see the boundary issue explicitly, change the angle by epsilon and increase the phase by eta, choosing eta>(N+1)*abs(epsilon), with both arbitrarily small. At a sample exactly on the upper endpoint 0 modulo one, its displacement is eta+s*epsilon>0, giving the correct right-hand value zero for an interior angle. At a sample on the lower endpoint 1-alpha, its displacement relative to that moving endpoint is eta+(s+1)*epsilon>0, giving the correct right-hand value one. All other finitely many samples have a positive margin and keep their value for sufficiently small changes. Choose the perturbed angle irrational. For alpha=0, choose a small positive angle and a phase perturbation larger than the total drift; every sample stays outside its tiny one-interval. For alpha=1, choose an angle just below one and the same dominating positive perturbation; every sample stays inside the one-interval. Thus the finite-prefix contradiction of G135 holds for every mechanical angle.

Now suppose c satisfies the finite repeat bound through M. The underlying mechanical prefix is available through N=M+w=251*(C+w+4). If g repeats on [a,e] with e+q<=N and e>=a+w, then c repeats on [a,e-w], and its compared samples end by N-w=M. Hence e<=2a+q+C+w. If e<a+w, the same inequality is automatic. Every repetition of g through N would therefore satisfy the forbidden bound with constant C+w, contradicting the extended G135 theorem. This proves the claim and explains why the margin is 250*w rather than an unspecified additive loss.

**Matching pieces and corrections.** Beside the alternating Rule 30 wall with initial left-zero radius L>=1, a companion cannot match such a recoded mechanical word on [a,b] unless

    b-a < H(L+2a,w).

For pieces with reset times t_j and widths bounded by one fixed w, the functions, angles and phases may change from piece to piece, but necessarily

    t_(j+1) <= 503*t_j + 251*L + 1004 + 250*w.

For actual disagreement indices against one fixed recoded mechanical base, the bounds are

    k_0 <= 251*(L+4)+250*w,
    k_(j+1) <= 503*k_j + 251*L + 1507 + 250*w.

Finitely many disagreements or a final infinite piece are impossible by the same finite-prefix theorem at a later restart. Consequently super-geometrically spaced resets or corrections are excluded for bounded-width recodings at every mechanical angle. These are necessary bounds, not a construction of a realizable companion.

**Orbit-endpoint interpretation.** G131 constructs a finite block code for any half-open binary arc partition whose actual jump points have the form beta+k_j*alpha. If the integer exponents span D=max(k_j)-min(k_j)>=1, its Laurent polynomial Q(z)=sum(z^k_j) has an even number of jumps and Q=(1+z)P. P has exponent span D-1, so after rephasing its block width parameter is w=D-1. The same construction works for rational angles: distinct actual jump points are listed once, and equality of the jumps leaves only a constant difference, absorbed in F. Constant partitions use w=0. Thus pieces whose endpoint representations have uniformly bounded exponent span inherit the reset bound, even if their angles and partitions vary. The controlling parameter here is exponent span, not merely the number of endpoints. No arbitrary unrelated-endpoint partition is claimed to have this representation.

**Unexpected width guard, proved without a run.** An unrestricted finite block code can fit any prescribed finite binary prefix. Fix an irrational Sturmian g and finitely many starting indices 0,...,m. Their infinite future tails are pairwise distinct: equality of two would give an eventually periodic mechanical code, impossible because its symbol frequency is irrational. For each pair there is a finite first differing coordinate; take w at least the largest such coordinate. All the blocks g_s,...,g_(s+w) at these indices are distinct. Define F on them to output the desired prefix, and define it arbitrarily elsewhere. This does not give an infinite prescribed word, a uniform w or a finite-left Rule 30 realization. In particular the record's overlap-free Thue-Morse prefixes can pass the repeat inequality for arbitrary finite horizons while being fitted by increasingly wide recodings. A horizon independent of all recoding widths is therefore false. This is the identified independent scope check. At w=0 the theorem recovers G135 and its rational extension; constant F also retains the immediate period-one obstruction. Geometric correction schedules still pass the displayed necessary bounds, and no positive density, entropy or prize solution follows.


### G137. A dyadic sparse word passes every repeat test; faster powers fail (2026-10-06)

**Status and target.** Symbolic obstruction audit, independently verified by Local L090; no experiment. G134/G135 are verified by Local L088 and G136 awaits review. Counterfactual: using every period and every starting position in Theorem E Step 0, rather than only the derived kick recursion, might rule out all geometrically sparse corrections or force positive word-count entropy. The explicit dyadic word refutes that inference. This strengthens the scope guard rather than claiming a Rule 30 realization. The existing Thue-Morse guard in section 8.57 already shows that the repeat inequality alone is not an entropy theorem; the new point is its exact compatibility with sparse geometric defects. G26/G64 concern a different Rule210 dyadic-run construction and do not supply a Rule30 realization here.

Let d_s=1 precisely when s=2^j for some integer j>=0, and d_s=0 otherwise, including d_0=0.

**Every repetition obeys the strongest nonnegative-margin test.** If d_s=d_(s+q) for every a<=s<=b, where a>=0 and q>=1, then

    b <= 2a+q-1.

For a>=1, choose the smallest power of two p>=a, so p<=2a. If p+q is not a power of two, there is a mismatch at s=p. If p+q=P is a power of two, then P>=2p and p+2q=2P-p lies strictly between P and 2P. Thus there is a mismatch at s=P=p+q. In both cases a mismatch lies in [a,2a+q], proving the bound.

For a=0, if q is a power of two, s=0 is already a mismatch. Otherwise q>=3. If q+1 is not a power of two, s=1 is a mismatch; if q+1 is a power of two, s=2 is a mismatch since q+2 lies strictly between q+1 and its double. In either case the first mismatch is at most q, giving b<=q-1 as required. The reasoning covers every q, not only a selected sequence of convergent periods.

Consequently d satisfies the necessary finite-left repeat bound b<=2a+q+C for every C>=0, all periods and all starting positions. Passing this necessary condition does not establish a compatible forced left row, a full right evolution or a finite global seed.

**Sparse, aperiodic and zero word-count entropy.** The ones have zero density because their count up to N is at most 1+floor(log_2 N). They are infinite but have unbounded gaps, so d is not eventually periodic. For a factor length m>=1, starts a<m contribute at most m different words. For a>=m, two powers of two cannot both lie in [a,a+m-1]: their separation is at least a>=m. Such factors have at most one one, giving at most m+1 possibilities. Therefore the number P(m) of distinct length-m factors obeys

    P(m) <= 2m+1,
    limsup log_2(P(m))/m = 0.

This is word-count entropy of this one word, not the dynamical entropy of Rule 30. Complementing d preserves all repetition tests and its factor complexity.

**Unexpected rate control.** For an integer B>=3 let d^(B) have ones at B^j and zero elsewhere. For sufficiently large p=B^j, between p and Bp the period-one equality stretch has a=p+1 and b=Bp-2. The repeat bound would require

    (B-2)*p <= C+5.

It fails for arbitrarily large p, for every fixed C. Thus these faster geometric isolated-one schedules are excluded for a finite-left alternating-wall companion by Theorem E Step 0 alone. Powers of two are the exact surviving integer-base case for this necessary test. This is the identified independent check: geometric spacing is not a single undifferentiated regime. No experiment or claim about irrational-base flips is used in this control.

**Closed bridge and next obligation.** Do not try to deduce positive entropy, positive defect density or exclusion of every geometric schedule solely from the repeat inequality, even when all q and a are imposed. The explicit sparse word passes the full family. Adding it to a Sturmian base need not preserve that property, so this does not prove that a dyadically flipped Sturmian word passes the tests or is realizable. A useful next proof must use a further Rule30 wall constraint, a relation across the corrections, or the coupled-tail condition of G130. The finite-left sufficiency question for d itself is not answered here.


### G138. The first nonlinear kick gate does not close the initial-tail problem (2026-10-06)

**Status and purpose.** Symbolic wall audit, independently verified by Local L092; no experiment. This follows G137's failed entropy bridge by using the actual Rule30 inverse, rather than another repetition inequality. Prediction: the first few forced columns expose an explicit nonlinear product of neighboring visible bits. Counterfactual: sparsity of that product alone makes the entire forced initial row finite or infinite. Neither implication is obtained. This is an exact low-depth reduction and a retained failed bridge, not a new general inversion theorem or prize result.

Write v_j(t)=x_(-j)(t), with v_0(2s)=0 and v_0(2s+1)=1. Let c_s be column 1's visible bit at physical time 2s. The wall forces v_1(2s)=1-c_s and v_1(2s+1)=1. The inverse Rule30 identity is

    v_(j+1)(t)=v_j(t+1) XOR (v_j(t) OR v_(j-1)(t)).

Put A=c_s, B=c_(s+1), D=c_(s+2). Repeated Boolean substitution yields the exact even/odd pairs

    (v_1(2s),v_1(2s+1)) = (1-A,1),
    (v_2(2s),v_2(2s+1)) = (A,B),
    (v_3(2s),v_3(2s+1)) = (1-B,1-B),
    (v_4(2s),v_4(2s+1)) = (A*B,D),
    (v_5(2s),v_5(2s+1)) = (D XOR (A OR (1-B)),1-B).

For example the depth-four even entry is (1-B) XOR ((1-B) OR A)=A*B. Its odd entry is (1-D) XOR ((1-B) OR B)=D. The depth-five odd entry is B*D XOR (D OR (1-B))=1-B: for B=0 both sides are one, and for B=1 both sides are zero. These independent Boolean simplifications check the product and the cancellation without a dynamical run. They apply to the forced left construction; a full right evolution is an additional constraint.

**Dyadic specialization.** For c=d of G137, c_s*c_(s+1)=1 only at s=1, because 1 and 2 are the only consecutive positive powers of two. Depth four's even trace therefore has exactly one one, at physical time 2; its odd trace still contains infinitely many shifted dyadic pulses. The initial row's first five cells are

    (v_1(0),...,v_5(0))=(1,0,0,0,1).

This supplies neither a tail classification nor a finite-left realization. Vanishing on one temporal parity at one depth is not eventual vanishing across all initial depths.

**Unexpected constant-code control.** If c is constantly zero, the same formulas give an all-one depth-one column and then stationary alternating columns 0,1,0,1 through the depths displayed. The inverse recurrence continues that checkerboard to arbitrary depth: whenever two neighboring columns are stationary and opposite, the next outward column is the inner column's complement. Thus the forced initial left row has infinitely many ones even though the depth-four product is identically zero. This is the identified independent check against treating a sparse product as a finite tail. The constant-one case gives a time-alternating depth-one column, stationary one at depth two, then stationary alternating columns 0,1,0,... outward, likewise an infinite initial tail.

**Failed bridge retained.** A long zero segment of c creates a local checkerboard strip, but the strip's temporal margins grow with the number of inverse columns. Dyadic segments move outward in time as their lengths increase. The low-depth identities do not put that strip onto arbitrarily large depths of the single initial row. Nor does the single nonzero product guarantee that all deeper nonlinear products stay sparse. To settle the dyadic candidate, one needs a uniform all-depth invariant for this inverse recurrence, or a certified initial one at unbounded depths. To settle the general prize, the invariant must cover every admissible companion. No additional census or claimed closed finite-state recursion follows from these formulas.


### G139. Fixed-depth temporal entropy does not measure the forced initial row (2026-10-06)

**Status and target.** Symbolic inverse-locality proof, independently verified by Local L092; no experiment. G138's low-depth audit is extended to every fixed depth. Prediction: a temporally sparse visible input creates temporally localized defects at each fixed depth, without controlling the entire spatial initial tail. Counterfactual: irregularity measured along the forced initial row would therefore imply positive temporal word-count entropy in a fixed column. The proof separates those axes. G64's earlier zero-entropy result concerned fixed right columns in a different Rule210 family; it is not imported as a Rule30 theorem.

Use G138's v_j(t) and inverse recurrence. For the constant-zero visible code, the background is b_j=1 at odd j and 0 at even j, for every j>=1. For any visible c define e_j(t)=v_j(t) XOR b_j. Then e_1(2s)=c_s and e_1(2s+1)=0. At depth two,

    e_2(t)=e_1(t+1) XOR e_1(t).

For j>=2, direct subtraction of the stationary background gives

    e_(j+1)(t)=e_j(t+1) XOR e_j(t)*(1-e_(j-1)(t))    when j is odd,
    e_(j+1)(t)=e_j(t+1) XOR (1-e_j(t))*e_(j-1)(t)    when j is even.

Indeed adjacent background bits are opposite. Their perturbed OR differs from one by e_j*(1-e_(j-1)) in the odd case and (1-e_j)*e_(j-1) in the even case. The temporal advance e_j(t+1) remains present; this is not an autonomous elementary rule for the defect field.

**All-depth locality.** By induction, e_j(t) is determined by the samples of e_1 on [t,t+j-1]. If all those samples vanish, e_j(t)=0. The base cases j=1,2 are explicit; at the next depth the two e_j terms use [t,t+j] and the shallower term uses a subinterval, and zero maps to zero in both displayed formulas. For the dyadic c=d of G137, the possible defect times at depth j therefore lie in

    union over k>=0 of [2^(k+1)-j+1, 2^(k+1)], intersected with t>=0.

This is an upper support bound, not equality. Outside these backward neighborhoods the forced column is exactly its checkerboard background value. It does not require linearizing away a nonlinear interaction.

**Temporal word bound.** Let P_c(n) count distinct length-n factors of c. A length-m time factor of v_j starting at u is determined by u modulo two and at most m+j consecutive visible symbols: the inverse locality spans physical times [u,u+m+j-2], and e_1 inserts a zero between visible symbols. Padding the visible window if needed gives

    P_(v_j)(m) <= 2*P_c(m+j).

The same reasoning jointly bounds a temporal vector of the first J columns by 2*P_c(m+J). Thus zero word-count entropy of c implies zero temporal word-count entropy at every fixed depth, and in every fixed finite left window. For d or its complement, G137 gives the explicit bound P_(v_j)(m)<=4(m+j)+2. This is not a uniform statement when the observed depth grows with m.

**Unexpected spatial-tail guard.** To evaluate v_j(0), the determining window length grows with j. Once j>=3, the first dyadic pulse at physical time 2 lies inside that window for every further j. The support lemma therefore does not force e_j(0) to vanish at large j. Nor may the fixed-j entropy limit be taken with j growing. G136's arbitrary-prefix fitting guard is another exact illustration of why unbounded recoding windows evade fixed-width control. These are the identified independent quantifier checks. Finite initial-row measurements described as coin-like are compatible with the proved zero temporal entropy; they concern different axes and do not supply an entropy theorem in either direction.

**Remaining obligation.** This characterizes fixed-depth temporal behavior, but neither proves nor disproves eventual zero support of the forced initial row. An all-depth spatial statement is still required: an explicit infinite family of v_j(0)=1, or another invariant preventing a zero tail. Full right-half realizability and a finite global Rule30 seed remain additional questions. No computational job duplicates Local's dyadic initial-row probe.


### G140. The wall coding separates family entropy, orbit entropy and finite support (2026-10-06)

**Status and target.** Symbolic quantifier audit of section 8.39's existing wall itinerary/seed bijection, independently verified by Local L093 (S36 and S37). No experiment or new novelty claim about that bijection. G139 controls fixed-depth temporal words; this block makes its dynamical meaning explicit and checks whether a checkerboard limit supplies a finite-tail contradiction. Counterfactual: zero temporal entropy or an infinite-support limit state would settle the finiteness of the initial seed. Neither does.

Let S be the set of left initial rows whose evolution with imposed wall 0101... has a black nearest-left cell at every odd time. Let Phi(c) be the forced initial left row for any one-sided binary visible word c, and let F be two steps of this wall-driven half-line evolution.

**The known coding intertwines the dynamics.** Phi is a homeomorphism from the full one-sided binary sequence space onto S. Existence follows by the inverse columns: v_1(2s)=1-c_s, v_1(2s+1)=1, and the inverse recurrence constructs all farther columns. Every constructed left cell satisfies the forward Rule30 equation; uniqueness of forward evolution with the imposed wall recovers this diagram from row zero. Conversely any row in S determines c_s=1-v_1(2s), and the same inverse reconstructs that row. Finite output coordinates depend on finite c prefixes, and finite c prefixes depend on finite initial cones, proving continuity both ways. This is the section 8.39/WA1 coding, not a new existence theorem.

The periodic boundary returns to its original phase after two steps. Shifting the whole constructed diagram by two physical times therefore gives

    F(Phi(c))=Phi(shift(c)).

Unlike G130's fixed-right-tail coordinate map, this boundary condition is invariant under the chosen time step, so the displayed relation really is a dynamical conjugacy. S is compact and F-invariant. Its full-family topological entropy is one bit per two-step iterate, because its conjugate is the full binary shift. This does not give a positive entropy theorem for each individual row or any finite-support subclass.

**Dyadic orbit closure.** Let X_d be the closure of the one-sided shifts of the powers-of-two word d. Phi(X_d) is exactly the F-orbit closure of its forced left row. The length-m language of X_d is the language of d; G137 bounds its size by 2m+1. Hence X_d, and by conjugacy Phi(X_d), have zero topological entropy. Equivalently, in the product topology every fixed finite spatial observation has zero temporal entropy as in G139. The full compatible family has entropy one while this particular orbit closure has entropy zero: the quantifiers differ.

**Unexpected support-limit check.** Take t_n=3*2^(n-1), n>=1, halfway between successive dyadic ones. Its distance to the next one tends to infinity, so shift^(t_n)(d) converges to the all-zero visible word. Continuity gives

    F^(t_n)(Phi(d)) -> Phi(0,0,...).

G138 identifies the limit row as the stationary left checkerboard, with one at every odd depth. Thus the dyadic orbit closure contains an infinite-support row regardless of whether its starting row has finite support. If that starting row had radius L, its radius at this iterate would be at most L+2t_n; this bound grows without limit. Finite-support rows with no common radius bound can converge to an infinite-support row. The limit therefore supplies no contradiction. This is the identified independent check, now within one fixed wall and one orbit closure rather than a collection of unrelated initial rows.

**Finite-left target retained.** Write S_fin for S intersected with the eventually-zero initial rows. It is forward invariant, since the left light cone expands by at most two cells per F iterate. It is not known to be nonempty, closed or compact. Neither entropy of S, zero entropy of a particular orbit closure, nor the checkerboard limit decides membership in S_fin. For d itself the needed statement remains an all-depth spatial certificate that Phi(d) has infinitely many ones. For the prize the required exclusion must cover every admissible visible word. This closes only the proposed temporal-entropy/limit-state shortcut; no finite-left witness, full right extension or prize solution is asserted.


### G141. Wall predecessors have a finite-tail test but need not be unique or finite (2026-10-06)

**Status and target.** Symbolic spatial-support audit, independently verified by Local L094 (S38); no experiment. Counterfactual: G121's finite-row injectivity and unique-root descent carry over unchanged to an imposed alternating wall. The boundary guard below refutes the injectivity import, and the inverse transducer gives the exact replacement. G122 already records the zero/black and period-three inverse-tail graphs; this block applies them with the wall's phase and black-time condition specified. It does not revive the closed root route as a prize proof.

Let u be a finite left row at white wall phase zero. Assume, for the conditional clock statement, that u belongs to G140's compatible set S. Rows are listed by increasing depth from the wall. A backward step solves

    q_(j+1)=y_j XOR (q_j OR q_(j-1)),

where y is the output row and q_0 is the input wall bit.

**First backward step, black phase.** The input wall bit is q_0=1 and the black-time condition forces q_1=1. Thus there is exactly one black-phase predecessor z. If u is zero beyond radius L, its outward recursion eventually follows

    M0(a,b)=(a OR b,a).

The graph is 00->00, 01->10, 10->11, 11->11. Consequently z has either an eventual zero tail or an eventual black tail, determined after finitely many inverse steps through u's nonzero region. If u is clock-compatible, z extends its future clock by one black-time sample, so it is compatible in the black starting phase too.

**Second backward step, white phase.** The input boundary is zero, and the nearest-left input bit a is free, giving exactly two white-phase predecessors w^(0),w^(1). They are distinct because their depth-one bits differ. Each evolves to z, then u. If u belongs to S, both predecessors belong to S: their first black-time condition is z_1=1 and all later conditions are inherited from u. Their newly prepended visible bit is 1-a.

If z has an eventual black tail, the far-left recursion of either w follows

    M1(a,b)=(1 XOR (a OR b),a).

Its recurrent graph is 00->10->01->00, with 11 entering at 01. Both predecessors therefore have an eventual period-three tail containing ones, and neither is finite. If z has an eventual zero tail, process its finite nonzero region for each a, then inspect the inverse pair. A 00 pair gives a zero tail; every other pair enters 11 under M0. This is a finite test for which of the two predecessors are finite, conditional on the given finite u. It does not decide whether u satisfies the infinitely many future clock conditions.

**Unexpected finite boundary guard.** With the white boundary fixed at zero, the distinct finite input rows

    (0,1,1,0,0,...) and (1,0,1,0,0,...)

both produce the same left output row (1,0,1,1,0,0,...). Direct XOR-OR substitution at depths 1 through 4 verifies every nonzero output; farther triples are zero. Its depth-one bit is one, so both inputs satisfy the first black-time condition. Their next left output under the black boundary is (1,0,0,1,1,0,0,...). Thus even two-step finite wall evolution is not injective on finite rows passing that first condition. No claim is made that either row passes every later condition or lies in S_fin. Ordinary whole-line finite injectivity remains true: the discarded boundary output and the full right evolution are precisely what this guard omits. This is the identified independent check.

**Descent and its remaining gap.** Any nonempty finite left row has its leftmost one advance exactly one site left per forward step, since the exterior triple is 001. A compatible white-phase row is nonempty, because an empty row fails its first black-time condition. Hence a finite two-step predecessor, when one exists, has radius L-2. Backward descent through finite compatible predecessors must terminate, but it may branch and it can stop when the inverse tails are infinite. Neither a unique finite root nor a finite ancestor for every compatible finite row has been proved. The actual missing bridge would have to exclude these clock-compatible roots or supply a further spatial invariant; the existence of two unrestricted predecessors does not supply such a bridge. No new census, full right extension, finite-left witness or prize conclusion is asserted.


### G142. A finite compatible candidate must accumulate on infinite support (2026-10-06)

**Status and target.** Symbolic consequence of the reviewed G140 compact wall coding and G141 exact radius growth; independently verified by Local L095. No experiment or novelty claim about compactness. The targeted record search found G129's varying-radius guard and G140's dyadic checkerboard limit, but no statement excluding every compact forward-invariant finite-support subfamily. Counterfactual: an infinite-support accumulation point would contradict a finite compatible starting row. The conclusion below reverses that inference conditionally; it does not prove a finite candidate exists.

Use G140's compact compatible space S and continuous two-step map F. Its finite-support subset S_fin is forward invariant. Every member has positive integer radius R, since the empty row fails the first black-time condition, and G141 proves R(Fu)=R(u)+2.

**Lemma.** There is no nonempty compact A contained in S_fin with F(A) contained in A.

**Proof.** Suppose such an A exists. The sets F^n(A) are nested, nonempty and compact, so their intersection K is nonempty and compact. Moreover F(K)=K. The forward inclusion follows from nesting. For the reverse inclusion, fix y in K. For each n the set

    C_n = F^n(A) intersect F^(-1)({y})

is nonempty, since y belongs to F^(n+1)(A). These sets are nested and compact. Any x in their intersection lies in K and satisfies F(x)=y.

Every point of K has positive integer radius. Choose y in K with the smallest radius occurring in K; this uses the well-ordering of the integers, not continuity or boundedness of the radius function. Surjectivity on K supplies x in K with F(x)=y. Exact growth gives R(x)=R(y)-2, contradicting minimality. Thus A cannot exist.

**Consequences, conditional on existence.** For any u in S_fin, its forward orbit closure in S is nonempty, compact and forward invariant. The lemma forces that closure to contain a row z of infinite support. Since every orbit point F^n(u) is finite, z is an accumulation point along indices tending to infinity. Therefore every hypothetical finite compatible candidate necessarily has an infinite-support orbit accumulation point, not merely the dyadic candidate of G140. Also S_fin is either empty or not closed in S: if nonempty and closed it would itself be a forbidden compact forward-invariant A. In particular it cannot be assumed compact to manufacture finite ancestors. This sharpens G140's closure qualification without deciding whether S_fin is empty.

**Unexpected compactness check.** Compactness alone does not bound finite radii. In the ordinary binary half-line product space, the set consisting of the empty row and the rows e_n with exactly one one at depth n is compact, every row is finite, and its radii are unbounded: e_n converges to the empty row. This is not a compatible wall family; the empty row is excluded from S. It rejects a false shortcut to the lemma. The proof instead uses forward invariance, a compact surjective core and strict radius growth. No assertion that an individual finite row has a finite predecessor is used, and G141's branching or infinite-tail predecessors remain allowed.

**Remaining prize obligation.** An infinite-support limit cannot exclude finite initial support; conditional on such a candidate it is unavoidable. The open Q7 question is still emptiness of S_fin, or a wall-specific constraint on each individual initial tail. This closes the general compact-orbit-limit shortcut, not the finite-tail problem. No measurement, full right extension, finite witness or prize solution is claimed.


### G143. An aperiodic half-circle code passes every repeat test (2026-10-07)

**Status and target.** Symbolic Q7 repeat-filter counterexample, independently verified by Local L099. No experiment run by GPT. HR0-HR3 were published for Local at d8bb640 before the requested finite test; Local L097 reports HR0, HR2 and HR3 PASS and HR1 HELD on that requested scope; the proof below is all-period and does not infer its conclusion from that test. Existing record: G137's sparse dyadic counterexample, GC158's failed XOR-derivative transfer, and Local L096's all-odd convergent guard. PRIOR-ART.md records the known Rote/Sturmian relation. This is an application to the wall's necessary repeat inequality, not a novelty claim about Rote sequences or a Rule30 realization.

Put beta=2-sqrt(2), alpha=beta/2 and r=sqrt(2)-1. Define

    c_s = floor(s*beta) modulo 2,    s>=0.

**Claim.** For every q>=1 and every interval of equality c_s=c_(s+q) on a<=s<=b, with a>=0,

    b < 2a+q.

Thus this aperiodic half-circle rotation code passes the wall's entire necessary repeat family even with constant C=0. It is not thereby a compatible finite-left companion. Its XOR derivative is the Sturmian mechanical word of slope beta, every constant run of c has length at most two, and its word-count entropy is zero. In particular this filter alone cannot exclude every nonsparse, low-complexity unrelated-endpoint rotation code.

**Mismatch intervals and reduction to records.** Choose the even integer P nearest q*beta and set epsilon=q*beta-P, so -1<epsilon<1 and epsilon is nonzero. With x_s={s*beta}, direct floor subtraction says a mismatch occurs exactly when

    epsilon>0: x_s in [1-epsilon,1),
    epsilon<0: x_s in [0,-epsilon).

For errors of the same sign, a smaller absolute error gives a smaller mismatch interval. Therefore it suffices to prove the claim at the successive same-sign error records: for any q choose a record q0<=q whose error has the same sign and no greater magnitude. A q-repeat interval avoids the larger mismatch interval, hence is a q0-repeat interval, giving b<2a+q0<=2a+q.

Here these records are among q=1, q=2, and the denominators listed below. To justify completeness, alpha=[0;3,2,2,...]. After its first denominator 3, consecutive convergents P/Q and P'/Q' form an integer basis, with opposite signed errors D,D' satisfying |D'|=(2+r)|D|, where Q'<Q. The next denominator is 2Q+Q'. Any pair (p,q) has the form m(P,Q)+k(P',Q'). If its error improves the current record of its sign, m and k must both be positive: opposite signs of coefficients add the error magnitudes, while a zero coefficient gives a multiple no better than a current record. With q<2Q+Q', m must then be one. For k>=2 the magnitude of D+kD' exceeds |D'|, so the only possible improving intermediate is m=k=1, the mediant. At the next convergent the induction repeats. Before denominator 3, the relevant nearest-integer periods are just 1 and 2. Scaling these errors by two gives exactly the even-integer records needed for beta; records with even larger error need not be retained.

Let p_n/q_n be beta's convergents, starting p_1/q_1=1/1 and p_2/q_2=1/2. For n>=2 all p_n are odd,

    q_(n+1)=2q_n+q_(n-1),
    delta_n=q_n*beta-p_n=(-1)^n*r^n.

The alpha convergents after denominator 1 are the even-numerator beta mediants

    Q_n=q_n+q_(n-1),    P_n=p_n+p_(n-1),    n>=2.

Their errors have sign opposite delta_n and magnitude E=(1+r)*|delta_n|. The intervening alpha mediants have beta denominators 2q_n and even numerator 2p_n. This follows by the displayed denominator recurrence (the first such denominator is 4). Hence the required candidate periods are 1, 2, Q_n and 2q_n for n>=2; proving more candidates than strictly set records is harmless.

**A return bound with its mesh proof.** Fix n>=2, put d=|delta_n| and Qnext=q_(n+1). Every block of Qnext successive orbit samples {s*beta} meets every half-open interval of length E=(1+r)*d. Indeed the Qnext orbit points have successive gaps d and d+|delta_(n+1)|=E. To see this directly, in the orientation given by the sign of delta_n, advance the index by q_n modulo Qnext. Without index wrap the circular distance is d; with wrap it is d+|delta_(n+1)|. Coprimality makes one cycle through all indices, and its total distance is

    Qnext*d + q_n*|delta_(n+1)| = 1

by the consecutive-convergent determinant identity. Thus this is the circular neighbor order and its largest gap is E. A half-open arc of length E contains a point even at a gap endpoint. Translating this mesh proves the block statement. It also holds for intervals of length 2d>E. Consecutive mismatch visits for either length therefore have time gap at most Qnext.

We also use the ordinary continued-fraction best-approximation fact already used in G134: for 0<k<q_n, the distance of k*beta to any integer is at least |delta_(n-1)|=(2+r)*d. Both E and 2d are smaller. So neither mismatch interval has a positive visit before q_n.

**Mediant periods Q_n.** The mismatch interval has length E and sign opposite delta_n. If it is the upper interval, its first visit is exactly q_n; if it is the lower interval, it contains time zero and its first positive visit is exactly q_n. In either case the samples at q_n land in it because their signed error has magnitude d<E. A repeat interval before that visit has b<=q_n-1<Q_n, and so satisfies the claim. For any later maximal repeat interval, write its preceding mismatch time as h>=q_n and the next mismatch time as h+g, with g<=Qnext. Then a=h+1, b=h+g-1 and

    b-2a-Q_n = g-h-Q_n-3
              <= Qnext-q_n-(q_n+q_(n-1))-3 = -3.

Subintervals only lower this debt. In the lower-interval case the first run starts at 1, making its bound still stronger.

**Doubled convergent periods 2q_n.** The mismatch interval now has length 2d and the same sign as delta_n. Its first positive visit lies between q_n and Q_n: there is no visit before q_n, and the mediant Q_n has the opposite signed error of magnitude E<2d, so it lands in the interval. In the lower-interval case time zero is also a mismatch. Any repeat before the first positive visit ends by Q_n-1<2q_n. Every later maximal repeat has preceding mismatch h>=q_n and gap g<=Qnext, giving

    b-2a-2q_n <= Qnext-q_n-2q_n-3
               = q_(n-1)-q_n-3 < 0.

This proves the claim for these periods too. For q=1 a match requires x_s<1-beta; its next sample is outside that interval because beta>1/2, so a match run has length at most one. For q=2 the nearest even displacement has epsilon=2beta-2<0, so a match requires x_s>=2-2beta. Its next sample wraps into [1-beta,beta), outside the match interval, and again every match run has length at most one. Both small periods satisfy the claim. The record reduction now proves it for every q.

**Complexity and the unexpected phase check.** The derivative g_s=c_s XOR c_(s+1) equals floor((s+1)*beta)-floor(s*beta), a Sturmian word. Thus c is aperiodic. Since beta>1/2, g contains no consecutive zeros, so c has no constant run longer than two. A length-m c block is determined by its first bit and the length-(m-1) g block. Hence P_c(m)<=2m and c has zero word-count entropy; no randomness statement follows.

The phase is essential. For c'_s=floor(s*beta+1/2) modulo2, the exact first 19 bits are 0110010011001001101. Period 7 repeats on [0,10] and fails at 11, giving debt 10-7=3. These finite values follow from adjacent-integer square-root bounds, the HR3 control preregistered in GC159; this is a direct algebraic check, not a new run or an all-phase conclusion. The period-q derivative lift counterfactual remains refuted by 0101... and its constant-one derivative.

**Scope.** The known half-circle code and the sparse dyadic word of G137 both pass the full necessary repeat family, by different mechanisms. Here numerator parity and mediant returns explain the gap. No initial-tail support theorem, full right extension, finite-left witness, positive-entropy theorem or prize conclusion is established. Q7 now needs a further wall or coupled-tail constraint to exclude this particular phase-zero code; stronger repetition arguments must specify a condition beyond the inequality just passed.


### G144. The phase-zero half-circle repeat filter has an exact exceptional class (2026-10-07)

**Status and target.** Symbolic Q7 classification, independently verified by Local L100; G143 independently verified by Local L099. No experiment. Fix the phase zero used in GC159; this is not an all-phase classification. The inputs are G143's signed mismatch intervals and tail-two mesh argument, ordinary continued-fraction best approximation and Legendre's criterion. The Rote critical-exponent literature is recorded in PRIOR-ART.md; its ordinary factor exponent does not include the starting index in our debt and no theorem from it is imported.

Let beta be any irrational in (0,1), let c_s=floor(s*beta) modulo2, and write p_n/q_n for its convergents, a_(n+1) for the next coefficient and delta_n=q_n*beta-p_n. Then the following are equivalent:

1. There is a finite constant C such that every equality interval c_s=c_(s+q), a<=s<=b, a>=0, q>=1, satisfies b<=2a+q+C.
2. Eventually every a_n is 2 and every convergent numerator p_n is odd.

The angles in (2) form a countable quadratic class. G143's beta=2-sqrt(2) belongs to it and even satisfies the strict C=0 bound. Passing this filter is not a finite-left Rule30 realization. Every other phase-zero half-circle code is excluded by the wall's necessary repeat inequality for every finite left radius.

**Obstruction from even numerators.** Suppose p_n is even, with n large enough that |delta_n|<1. The period q_n has signed even-integer error delta_n, so its mismatch interval is the upper or lower arc of length |delta_n| given in G143. Its first positive visit is exactly h=q_(n+1). Indeed best approximation gives distance at least |delta_n| to every integer at every 0<k<q_(n+1); q_n itself has the wrong error sign to enter this arc, and no other such k attains the opposite endpoint. At q_(n+1) the error has opposite sign and smaller magnitude, so the arc is hit.

If delta_n>0, the prefix equality interval is [0,h-1]. If delta_n<0, time zero is a mismatch and the equality interval is [1,h-1]. Their debts b-2a-q_n are respectively

    q_(n+1)-q_n-1,    q_(n+1)-q_n-3.

Both are at least q_(n-1)-3. Infinitely many even p_n therefore produce unbounded debt. Condition (1) forces all sufficiently late p_n to be odd. The numerator recurrence then forces every sufficiently late a_(n+1) to be even.

**Obstruction from large coefficients.** Put d=|delta_n| and a=a_(n+1)>=3. Write |delta_(n-1)|=(a+gamma)*d with 0<gamma<1. For large n, the period 2q_n has signed even-integer error 2delta_n and mismatch arc of length 2d. Its first positive visit is

    h=(a-1)*q_n+q_(n-1).

Here is an explicit first-hit justification. Expand any integer pair (p,k) in the unimodular basis (p_n,q_n),(p_(n-1),q_(n-1)), with coefficients m,l. An error of the sign opposite delta_n and magnitude less than 2d, which is less than |delta_(n-1)|, requires m,l>0: opposite coefficient signs add error magnitudes, and a zero coefficient is either of the wrong sign or too large. If k<h, then m<=a-2. Its opposite-sign error has magnitude

    l*|delta_(n-1)|-m*d >= (2+gamma)*d > 2d.

Thus no earlier positive visit is possible. At h, m=a-1 and l=1 give the required opposite error (1+gamma)*d<2d. As before the initial equality interval starts at zero or one, according to the sign of delta_n. Its debt for period 2q_n is

    (a-3)*q_n+q_(n-1)-1, or
    (a-3)*q_n+q_(n-1)-3.

These tend to infinity along any infinite set of coefficients at least three. Condition (1) therefore forces eventually a_n<=2. Combined with eventual evenness from the numerator obstruction, it forces eventually a_n=2. This proves (1) implies (2), with explicit violating intervals whenever either obstruction occurs infinitely often.

**Converse: finite exceptions cost only a finite constant.** Assume (2), put r=sqrt(2)-1, and take n sufficiently late. Then the exact error ratios and recurrence are

    |delta_(n-1)|=(2+r)*|delta_n|,
    |delta_(n+1)|=r*|delta_n|,
    q_(n+1)=2q_n+q_(n-1).

The even-numerator mediants have denominator B_n=q_n+q_(n-1) and numerator A_n=(p_n+p_(n-1))/2. They approximate alpha=beta/2 with alternating errors D_n=(delta_n+delta_(n-1))/2, whose successive magnitude ratio is r. Consecutive pairs (A_n,B_n) are unimodular, as direct substitution gives determinant of absolute value one; their denominators satisfy the same tail-two recurrence. Moreover

    B_n*|D_n| = 1/(B_(n+1)/B_n+r)
                -> 1/(2*sqrt(2)) < 1/2.

Legendre's criterion makes them genuine alpha convergents for all sufficiently late n. They are consecutive: their errors have opposite signs, whereas a skipped even number of convergent steps has the same sign, and a skipped odd number of at least three has determinant of magnitude at least two. Thus alpha also has an eventual continued-fraction tail of twos. Its late same-sign error records are its convergents and intervening mediants, by G143's unimodular record argument. Their beta periods are B_n and B_n+B_(n-1)=2q_n. There are only finitely many earlier record periods.

For every sufficiently late B_n or 2q_n, G143's entire mesh and first-hit argument applies verbatim with the displayed error ratios: a q_(n+1)-point orbit mesh has largest gap (1+r)*|delta_n|; no positive arc visit precedes q_n; the mediant visits provide the required first-hit upper bound. Consequently every repeat at these candidate periods satisfies b<2a+q, without any assumption on the finite continued-fraction prefix. Same-sign mismatch-interval inclusion reduces all other late periods to these records.

Each of the finitely many earlier record periods has a nonempty mismatch arc. Irrational rotation has a finite orbit mesh finer than that arc, so every translate of a sufficiently long fixed block hits it. Its equality runs therefore have bounded length, and its repeat debt has a finite upper bound independent of a. Taking the maximum of these finitely many bounds and zero supplies C. This proves (2) implies (1).

**Unexpected parity controls and limits.** The tail-two angle beta=sqrt(2)-1 fails the criterion: it has infinitely many even convergent numerators. Already the convergent 2/5, followed by 5/12, gives a period-5 equality on [0,11] of debt 6. Thus being in the silver quadratic field or having a tail of twos alone is insufficient. Conversely beta=[0;1,1,4,4,...] has eventually all odd numerators but fails by the doubled-period obstruction. These are direct arithmetic controls, not new runs. They distinguish both required conditions from weaker shortcuts.

Every angle satisfying (2) has a finite integer continued-fraction prefix followed by the same infinite tail, so there are countably many and they are quadratic. Their complements and arbitrary phases were not classified here. The wall has a necessary repeat constant determined by its finite left radius, so the theorem excludes all other phase-zero codes as companions. The exceptional class remains unresolved for actual initial-tail support. No finite witness, full right extension, positive-entropy or prize claim follows.

### G145. The silver half-phase code fails every finite repeat allowance (2026-10-07)

**Status and target.** Symbolic Q7 proof, independently verified by Local L101. No experiment. G143 and G144 are independently verified by Local L099 and L100. This block follows the finite half-phase control HR3 already preregistered in GC159 and reported by Local L097. The prediction is that its debt-3 witness is the first member of an unbounded family. The counterfactual is a uniform finite debt bound at this phase. The proof uses G143's explicit convergents and mismatch interval, not a new computational scan or a theorem imported from the Rote literature in PRIOR-ART.md.

Put beta=2-sqrt(2), r=sqrt(2)-1 and c_s=floor(s*beta+1/2) modulo2. Let p_n/q_n be beta's convergents, with n=1 giving 1/1 and n=2 giving 1/2. For every odd n>=3, put Q_n=q_n+q_(n-1). Then the period-Q_n prefix equality interval is exactly

    [0, h_n-1],    h_n=2q_n+q_(n-1)/2,

and its debt is

    (h_n-1)-Q_n = q_n-q_(n-1)/2-1 -> infinity.

Consequently no finite C makes b<=2a+q+C hold for every repeat of this half-phase code. In particular it cannot be the wall's companion from any finite left radius. This concerns the chosen half-phase silver code, not every phase or angle.

**Proof of the first hit.** For these odd n, q_n is odd, q_(n-1) is even, and both numerators are odd. Set d=|delta_n|, where delta_n=q_n*beta-p_n. The exact signed errors are delta_n=-d and delta_(n-1)=(2+r)d. Period Q_n has an even numerator and positive error E=(1+r)d. Since E<1/2 for n>=3, its mismatch interval in the shifted coordinate is [1-E,1). Thus a positive time k is a mismatch exactly when

    {k*beta} is in [1/2-E,1/2).

Equivalently, there is an odd integer p with 2k*beta-p negative and magnitude at most 2E. Equality at the endpoint is impossible: it would imply an integer multiple of beta is an integer, since E=Q_n*beta-(p_n+p_(n-1)). Expand the integer pair (p,2k) in the unimodular basis (p_n,q_n),(p_(n-1),q_(n-1)), with integer coefficients m,l. Denominator parity forces m even; odd numerator parity then forces l odd. Its error is

    [-m+(2+r)l]*d.

A negative error of magnitude less than 2E requires m,l>0. Indeed m<=0,l>0 has the wrong sign; both negative give a negative denominator. If m>0,l<0, parity gives m>=2 and |l|>=1, and the magnitude is at least (4+r)d>2E. A zero coefficient is ruled out by parity, has the wrong error sign, or has a nonpositive denominator. Therefore m is a positive even integer and l a positive odd integer.

For l=1, the first possible m is 4: m=2 has positive error; m=4 has negative error of magnitude (2-r)d<2E. It gives denominator 4q_n+q_(n-1), hence time h_n. If l>=3, negative error requires m>(2+r)l, so m>=8; its denominator exceeds the one just found. This proves h_n is the first positive mismatch. Time zero is not a mismatch, since its shifted coordinate is 1/2. The prefix equality and its exact endpoint follow.

The denominator recurrence gives unbounded q_n and q_(n-1)<q_n, so the displayed debt is greater than q_n/2-1 and diverges. This proves the exclusion for every finite allowance.

**Unexpected check and scope.** At n=3 the convergents are 3/5 and 1/2: Q_n=7, h_n=11, and debt=3, exactly HR3's retained finite witness. The same angle at phase zero passes every period with C=0 by G143. Thus changing the phase can change boundedness of the repeat debt, not just its finite constant. This is not a finite Rule30 witness at either phase. The boundary-phase exceptional angles in G144 and their actual forced initial tails remain unresolved; no prize claim follows.

### G146. Shifted passing codes approach an explicitly excluded infinite tail (2026-10-07)

**Status and target.** Symbolic Q7 closure audit, independently verified by Local L102. Depends on verified G140/G143 and G145 (Local L101). No experiment. Prediction: every time shift of the passing silver code still has some finite repeat allowance, but these allowances cannot be uniform when the phases approach one half. Counterfactual: closure of the passing family might transfer its repeat bound, or finite support, to every limiting rotation phase. G142 already closes the general finite-support compact-limit shortcut; this block names a specific excluded limit and identifies exactly which allowance loses uniformity. Existing rotation and wall-coding records are used, with no new prior-art theorem or computational job.

For a binary one-sided word x define B_C by the requirement that every equality interval x_s=x_(s+q), a<=s<=b, satisfies b<=2a+q+C, for all a>=0 and q>=1. Take C>=0, and put B=union over all nonnegative integer C of B_C. Let sigma be the left shift.

**Shift and finite-prefix control.** If x belongs to B_C, sigma^t x belongs to B_(C+t). A repeat of the shifted word translates to [a+t,b+t] in x, whose bound gives b<=2a+q+C+t. Conversely, if sigma^t x belongs to B_C, then x belongs to B_(C+t). For a repeat of x with a>=t, translate back and use the shifted bound. If a<t<=b, its suffix [t,b] translates to a repeat starting at zero, giving b<=t+q+C<=2a+q+C+t. If b<t, the bound is automatic. Thus x is in B if and only if sigma^t x is in B. Words that agree after a finite prefix also agree on membership in B. Global complementation preserves every B_C exactly.

**Closed at fixed allowance, not at some allowance.** Each B_C is closed in the product topology: any violation is certified by a finite repeat witness, involving finitely many coordinates through b+q, and persists in the corresponding cylinder. An intersection of these closed finite-witness constraints is closed. This does not make their increasing union B closed.

Let beta=2-sqrt(2) and c^(rho)_s=floor(s*beta+rho) modulo2, with rho considered modulo2. G143 places c^(0) in B_0, hence every sigma^t c^(0)=c^(t*beta modulo2) is in B. Irrational rotation has a dense forward orbit, so choose t_j with t_j*beta modulo2 tending to 1/2. No coordinate s*beta+1/2 is an integer, so every fixed finite prefix eventually agrees exactly with c^(1/2). Therefore

    sigma^(t_j)c^(0) -> c^(1/2),

while G145 gives c^(1/2) not in B. This proves B is not closed. More precisely, for any fixed C, choose a G145 witness with debt greater than C. Every sufficiently large j shares all coordinates of that witness and fails B_C. Thus the smallest nonnegative repeat allowances for these passing shifted words tend to infinity, not just along some unspecified subsequence. The simple upper allowance t_j remains valid.

The passing phases t*beta modulo2 and the excluded phases 1/2+t*beta modulo2 are both dense. The latter exclusion follows from the reverse-shift implication above. These are two countable dense phase orbits, not a classification or measure statement about the other phases. They are disjoint by irrationality.

**An explicit infinite forced-tail limit.** In G140's notation Phi maps a visible word to its unique compatible initial left row and satisfies F Phi=Phi sigma for the two-step wall evolution F. Its exact finite-prefix modulus makes Phi continuous. Put u_0=Phi(c^(0)) and u_half=Phi(c^(1/2)). Then

    F^(t_j)(u_0) = Phi(sigma^(t_j)c^(0)) -> u_half.

G145 and the wall's necessary finite-radius repeat bound force u_half to have infinite support. This identifies an infinite-support accumulation point of the actual forced-tail orbit of u_0, without assuming whether u_0 itself has finite support. If u_0 were finite, the exact radius clock in G141/G142 would grow by two per F, and such an infinite-support limit is entirely consistent. No contradiction to a finite u_0 follows. Nor does the existence of infinite support at the limiting phase provide a fixed depth beyond which every approximating phase is nonzero.

**Unexpected prefix guard and remaining obligation.** Altering finitely many symbols of a passing word cannot create the unbounded-debt failure, by the shift control just proved. Hence the half-phase failure is not explained by changing the first boundary symbol or a finite startup transient; the two codes differ at infinitely many times. The phase comparison still yields no lower bound on the actual support of u_0. Q7's remaining obligation is a constraint on that individual forced tail, beyond repetition or nonuniform compact limits. No finite witness or prize claim follows.

### G147. At a fixed irrational angle, finite-tail phases are empty or countable and dense (2026-10-07)

**Status and target.** Symbolic Q7 corollary, independently verified by Local L103. No experiment or general symbolic-dynamics novelty claim. Uses the verified wall coding G140, radius clock G141/G142 and fixed-radius count G129. G145 is independently verified by Local L101. Prediction: varying the phase can give an almost-every-phase exclusion without deciding one exceptional phase. Counterfactual: density of the phase orbit would promote a finite-tail realization to an interval of finite-tail phases. The countability argument refutes that promotion. The phase-dependent repeat record is G143-G146; no external theorem beyond the elementary density of an irrational rotation is imported.

Fix any irrational beta in (0,1). For phases rho modulo2 let c^(rho)_s=floor(s*beta+rho) modulo2, and let

    E_beta = {rho : Phi(c^(rho)) has finite support}.

Then E_beta is countable and forward invariant under rho -> rho+beta modulo2. It is either empty or dense. In particular almost every phase has an infinite forced initial left tail, at every fixed irrational angle, including the exceptional phase-zero angles of G144. This statement does not exclude any specified phase in E_beta, or establish that E_beta is nonempty.

**Proof.** Distinct phases modulo2 give distinct visible words. Indeed the two shifted half-circle partitions disagree on a nonempty open interval of the length-two circle whenever their shifts differ modulo2. The forward orbit s*beta modulo2 is dense and enters that interval, giving a differing symbol. The uniqueness of Phi therefore makes the phase-to-initial-row map injective.

There are only countably many finite binary initial rows: at radius at most L there are at most 2^L. Injectivity gives at most 2^L phases in E_beta with radius at most L. Taking the union over positive integer L makes E_beta countable, hence of Lebesgue measure zero. The empty row is not compatible with the clock, as in G141.

The conjugacy gives F(Phi(c^(rho)))=Phi(c^(rho+beta modulo2)). Forward evolution preserves finite support, so E_beta is forward invariant. If it contains rho, it contains its whole dense irrational forward orbit. Its radii on that orbit are exactly R(rho)+2t by the radius clock. This proves the empty-or-dense dichotomy, and explains why countability and density do not conflict.

**Uniform-radius qualification.** Every fixed-radius phase set is finite. Consequently, along any convergent sequence of pairwise distinct phases in E_beta, the radii tend to infinity: a bounded-radius subsequence would lie in a finite set, contradicting distinctness. An interval of finite-tail phases is impossible, but a dense exceptional set of finite tails is allowed. No uniform-radius conclusion follows from density of one orbit.

**Unexpected check and remaining obligation.** The same countability argument applies at the silver angle even though G143 passes every repeat test and G145 fails every allowance at another phase. Conversely, assuming just one finite phase would supply a dense countable orbit with steadily growing radii, fully consistent with the infinite-support limits in G142/G146. Thus an almost-every-phase theorem, residual-set argument or dense collection of infinite tails cannot settle the individual boundary-phase candidate. E_beta has not been shown nonempty, and its countability is not a prize solution or an all-phase exclusion. The next obligation remains a spatial constraint on Phi(c^(0)), rather than another phase-counting estimate.

### G148. Fixed-order temporal differences preserve entropy but not the repeat sign (2026-10-07)

**Status and target.** Symbolic diagnostic audit, independently verified by Local L104. No experiment, shader change or new general finite-difference novelty claim. The owner linked the project to temporal motion fields; WHAT-WE-BUILT.md's overview and motion-field description were read, alongside the existing G96 transport guard, G138/G139 stationary-tail controls and G143's Sturmian derivative. Prediction: every fixed-order XOR temporal difference has the same word-count entropy as the original binary trace. Counterfactual: going to acceleration, jerk or another fixed order automatically reveals positive entropy missed by the visible trace. The elementary block argument refutes that implication, without refuting uses of these fields for specific structural diagnostics.

Let S shift a one-sided binary word forward, and let D=1+S over GF(2). For any fixed k>=1, D^k is the order-k XOR temporal difference. If P_x(n) counts the distinct length-n factors of x, then

    P_(D^k x)(n) <= P_x(n+k) <= 2^k P_(D^k x)(n).

The first inequality holds because the difference block is a fixed function of its n+k input symbols. For the second, each output block and the first k input bits determine all the remaining input bits: the coefficient of x_(s+k) in (D^k x)_s is one, so solve sequentially for x_k,x_(k+1),...,x_(n+k-1). There are at most 2^k possible first k bits. Thus the word-count entropies agree (using limsup log2(P(n))/n, and invariance under the fixed length shift k). This is valid for one word and its factors, not only for the full shift.

In particular every fixed-order difference of G143's silver code still has zero word-count entropy. The combined jet (x,Dx,...,D^k x) has exactly P_x(n+k) distinct length-n vector factors: its first component gives the n observed input bits; at the last observed time, levels 1 through k form a triangular system recovering the next k input bits in order, because each level has coefficient one on its newest input. Keeping all levels cannot add an entropy rate either. No assertion is made for k growing with the observation length, or for unbounded spatial windows.

**Period and sign controls.** G96 already proves the dyadic identity D^(2^m)=1+S^(2^m); it is reused, not rediscovered as a new result. Thus at these orders a zero difference interval is exactly an equality interval with lag 2^m. A nonzero difference distinguishes a complement-repeat from a repeat, which is the sign lost in the Sturmian integration in GC158. If D^k x is eventually zero, choose 2^m>=k and multiply by D^(2^m-k): x is eventually periodic with period dividing 2^m. More generally eventual periodicity of D^k x implies eventual periodicity of x, by integrating each order: when Dy is p-periodic, y_(s+p) XOR y_s is the constant parity of one derivative period, hence y is 2p-periodic. Iterating gives a sufficient period 2^k p. This period bound is not claimed optimal.

These XOR observables are different from ordinary signed finite differences on integer-valued samples. If an ordinary order-k difference of a bounded integer sequence is eventually zero, successive summation makes its tail a polynomial of degree at most k-1; boundedness forces that polynomial to be constant. For the alternating binary trace 0101..., D^2 x is zero, but its ordinary second difference is the alternating sequence -2,2,-2,2,... . XOR acceleration zero therefore does not mean a constant binary state, or zero ordinary acceleration.

**Unexpected support guard and next obligation.** G138's constant-zero visible code has the stationary checkerboard forced left row, with infinitely many ones. Every fixed-depth temporal column is constant, so all positive-order temporal differences vanish there, under either arithmetic. The derivatives discard the stationary spatial background. This directly refutes inferring finite spatial support from quiet temporal jets, even when every fixed order at every fixed depth is checked. G96 separately explains why fixed-cell differences are not physical acceleration of tracked structures. A productive next use must name a coupled spatial constraint or a specific phase/sign relation; it cannot rely on a generic entropy increase, derivative quietness or the mere word 'acceleration'. No finite initial-tail exclusion or prize claim follows.

### G149. Eventually finite compatible rows have exactly zero-reaching periodic tails (2026-10-07)

**Status and target.** Symbolic Q7 tail reduction, independently verified by Local L105. No experiment. Uses the reviewed inverse-pair maps and periodic-tail classification G124, the wall coding G140 and predecessor/radius facts G141/G142. Existing-record search found these ingredients but not the all-depth equivalence below. No novelty claim for finite-state inversion or backward shift density. Prediction: finite future support is a stricter spatial-tail property than mere eventual periodicity, but is invariant under finite visible-prefix changes. Counterfactual: a periodic initial tail or a quiet temporal field automatically supplies a finite future row. The stationary checkerboard refutes that shortcut.

Write S for the compatible initial left rows with imposed wall 0101..., F for two physical steps, and S_fin for its finite-support rows. Define

    S_event = union_(k>=0) F^(-k)(S_fin), inside S.

Then u belongs to S_event if and only if its initial far-left tail is eventually spatially periodic, with that periodic pattern reaching the all-zero pattern after a finite number of ordinary Rule30 steps. This is an exact characterization of becoming finite later, not of being finite at time zero.

**Necessity, using both neighboring cells.** Suppose F^k(u) is finite, so the row at physical time 2k is eventually zero. A single backward step solves the known inverse recurrence

    q_(j+1)=y_j XOR (q_j OR q_(j-1)).

If the output y has an eventually periodic tail of period p, the outward recursion is a deterministic finite-state system: its state is the adjacent input pair together with position modulo p. There are 4p states. Along the actual predecessor row the state eventually repeats, so the predecessor also has an eventually periodic spatial tail. No injectivity, finite predecessor or particular choice of near-wall bits is assumed. Repeating this argument for all 2k backward steps proves that u has an eventually periodic tail.

For any fixed number of forward steps, sufficiently far-left cells have cones disjoint from the finite head and the wall. Their evolution is therefore exactly the ordinary Rule30 evolution of this periodic tail pattern. Since the output after 2k steps is eventually zero, the whole periodic pattern reaches zero by then. G124 now restricts its least spatial period to 1 or 3*2^a, a>=0. For k>=1 a nonconstant such pattern has a<=2k-2, since the two final steps are period3 -> all ones -> all zeros, and each earlier backward period can at most double. Thus its least period is at most 3*4^(k-1). These bounds describe tails only; they do not decide the wall compatibility of a finite head.

**Sufficiency.** Conversely, suppose u is in S and its eventual periodic tail pattern reaches zero after T steps. Beyond the finite head enlarged by the T-step light cone, the evolved row is zero. It has finite support. Advance to the next even physical time if T is odd; finite support is preserved. Thus F^ceil(T/2)(u) is finite and u belongs to S_event. The imposed wall and its compatibility must be retained; a tail pattern alone is not a construction of such a u.

**Visible-prefix interpretation and density qualification.** Let C_fin=Phi^(-1)(S_fin). G140's conjugacy gives

    Phi^(-1)(S_event)=union_(k>=0) sigma^(-k)(C_fin).

Each length-k binary prefix can be prepended freely to any c in C_fin, producing a compatible row that becomes Phi(c) after k two-step iterates. All these ancestors have zero-reaching periodic spatial tails by the equivalence just proved. Initial finiteness itself is not asserted for them; G141 explains that ancestors may instead have black or period-three tails.

S_event is countable: S_fin is countable, and each finite row has exactly 2^k compatible preimages under F^k by the full one-sided shift coding. It is empty exactly when S_fin is empty. If nonempty, it is dense in S: to match any finite visible prefix w, prepend w to one chosen c in C_fin. Continuity of Phi transfers this cylinder density. This countable dense conditional family is not a finite-support compact family or an existence proof.

**Unexpected periodic-tail control and consequence.** A spatial 001 tail evolves to all ones and then zero. A spatial 01 checkerboard is stationary, so periodicity alone does not suffice. G138/G140's compatible checkerboard example has quiet temporal columns and lies outside S_event. Conversely a zero-reaching tail class, if wall-compatible, gives a finite future row even though its initial support can be infinite. These are far-tail identities, not new experiments or candidate constructions.

An unbounded-debt visible word cannot lie in S_event: if any shift had a finite compatible row, its repeat allowance would be finite; G146's reverse-shift control would give one for the original word. Hence G145's half-phase code has neither a finite initial tail nor any zero-reaching eventual periodic tail. The phase-zero silver code remains unresolved. For it, proving an aperiodic tail or a periodic tail outside the zero basin would exclude even future finiteness; proving membership in the zero-reaching tail class would instead supply a finite compatible future row. Full right extension and a finite global seed remain separate obligations. No prize conclusion follows.

### G150. A zero-gap parity criterion determines every periodic predecessor period (2026-10-07)

**Status and target.** Symbolic periodic-tail refinement, independently verified by Local L106. No experiment. Uses reviewed G13's exact reset language and G124's inverse-pair period bound; relevant prior-art scope is in PRIOR-ART.md. Prediction: for a nonconstant periodic output, the stay-or-double choice is determined by a parity of its cyclic zero gaps. Counterfactual: G124's bound alone leaves that choice unspecified. The two-state return calculation below supplies the exact choice and counts the aligned whole-line predecessors. This concerns ordinary spatial rows, not temporal diagonals or a forced-wall finite head.

Fix a nonconstant whole-line output y of least spatial period p. Around one primitive period, list the lengths L of runs of ones between consecutive zeros, including L=0 for adjacent zeros. Then:

- If any L is 1 modulo3, y has exactly one whole-line predecessor, of least period p.
- Otherwise, let N count the gaps with L=2 modulo3. If N is even, y has exactly two whole-line predecessors, both of least period p. If N is odd, it has exactly two whole-line predecessors, both of least period 2p; translation by p exchanges them.

Every whole-line predecessor is periodic. Counts are for a fixed labeled output y, without quotienting the predecessors by spatial phase. Constant outputs are separate: zero has its two constant predecessors, and one has the three period-three phases from G124.

**Return-map proof.** Use G13's adjacent input state (a,b) and descending driver transitions

    T_y(a,b)=(b, y XOR (a OR b)).

Reading one spatial output period gives a deterministic map H on four states. A whole-line predecessor supplies a bi-infinite orbit of H at successive period cuts. Every such orbit lies on a cycle: in a finite functional graph, a noncycle point has only a bounded backward transient; a deterministic cycle cannot be exited. Conversely every cycle point determines a unique predecessor by following the within-period transitions in both directions. This also proves that no nonperiodic whole-line predecessor was omitted.

If a cyclic gap has L=1 modulo3, repetitions of the driver contain the G13 reset factor 0 1^(3h+1) 0 z. Some power of H therefore has singleton image. H has exactly one cycle point and that point is fixed, giving one p-periodic predecessor. Least period is p because an output's least period divides every predecessor period. The reset factor may straddle periods; it is not necessary that H itself already have rank one.

Suppose no gap is 1 modulo3. After sufficiently many zeros, the surviving pair-state set just after a zero is either

    C={00,11},    A={00,01}.

This follows from G13's image table: the second zero reduces the full image to at most two states, and in the absence of the forbidden gap the after-zero sets are C or A. Label 00 as zero and the other state as one. Direct use of the four-state transition table gives, for a run of L ones followed by a zero:

| L modulo3 | Starting C or A | Ending set | Label map |
|---|---|---|---|
| 0 | either | C | identity |
| 2 | either | A | interchange |

This includes L=0. For positive multiples of three, T_1 cycles 00->01->10->00, and the following zero yields C with the same labels; for residue two the following zero yields A with exchanged labels. In particular both labels survive every permitted gap. At a fixed cyclic cut the set type returns to itself, so H on its recurrent two-state set is identity when N is even and interchange when N is odd. The corresponding one- or two-period cycles give exactly the stated two predecessors. Output least period p rules out any smaller period; the interchange case is not p-periodic, so its least period is 2p.

**Independent arithmetic controls, without a run.** Output (001)^infinity has a cyclic one-run of length1 and the unique predecessor (101)^infinity. Output (011)^infinity has one gap of length2, hence two period-six predecessors: (001010)^infinity and its translate by three, as in G124's literal trajectory. Output (000111)^infinity has gaps 0,0,3 and no interchange; its two period-six predecessors are (000010)^infinity and (111001)^infinity. Their six literal triples give the same labeled output 000111. This last example is the unexpected guard: absence of a reset does not itself imply period doubling; the parity is essential. Constants cannot be put into the zero-gap rule unchanged.

**Tail implication and limit.** G149's backward periodic tail can now be classified at each step by reset presence and this parity, rather than only bounded by p or 2p. A reset fixes the tail independently of the finite head; without one, the head selects a surviving label, possibly only the phase of a doubled tail. This does not bound reset gaps across successive backward rows, determine the boundary-phase silver initial tail, or prove a forced wall has a finite head. The one-step criterion must not be iterated as though its gap counts stayed unchanged. No new run, finite witness or prize conclusion follows.

### G151. Backward period doublings cannot be consecutive (2026-10-07)

**Status and target.** Symbolic tail-period refinement, independently verified by Local L107; G150 independently verified by Local L106. No experiment. Uses G150's two-label criterion and reviewed G13/G124. Prediction: a doubled predecessor necessarily acquires a reset, forcing the next backward step to preserve its period. Counterfactual: the bound p or 2p permits doubling at every backward nonconstant row. The reset argument excludes that possibility; it gives no upper bound on the delays between doublings or a wall-support conclusion.

Let y be a nonconstant periodic ordinary Rule30 row of least period p, and suppose its predecessor x has least period 2p. Then x contains a cyclic factor 010. Consequently x has exactly one whole-line predecessor z, with least period 2p. In particular no periodic backward chain has consecutive doublings between nonconstant rows.

**Proof.** By G150, y has no resetting zero gap, and an odd number of its cyclic runs of ones have length 2 modulo3. Choose one such run, whose length is at least two. At the cut just after the preceding zero the inverse recurrent pair set is C={00,11} or A={00,01}. Label 00 as zero and the other state as one. One p-period interchanges the labels. Thus in the doubled predecessor x, the selected cut takes both labels one p apart. At the occurrence with label zero, the actual adjacent input pair is 00. The first two driver ones give

    00 --1--> 01 --1--> 10.

The consecutive reconstructed input symbols are therefore 0,1,0. Reversing the spatial reading direction leaves 010 unchanged. Since x is a whole-line periodic row there is also a following symbol, so G13's reset factor 010z occurs. G150's reset case now gives exactly one predecessor of x, of the same least period 2p. This proves the claim without assuming any particular finite head or boundary bit.

**Improved zero-basin time bound.** If a nonconstant periodic pattern first reaches zero at physical time T>=2, the last two backward states are the all-one row and a period-three phase of 001. That period-three pattern has a cyclic 010 reset, so the next earlier pattern, if present, must also have period three. Beyond it, no two consecutive steps can double. Thus if the original least period is 3*2^a,

    a <= floor((T-2)/2),
    period <= 3*2^floor((T-2)/2).

This is stronger than G124/G149's a<=T-2 cap. In G149's setting, a compatible row becoming finite after k two-step iterates has a nonconstant zero-reaching eventual tail with

    a <= k-1,    period <= 3*2^(k-1),    k>=1.

If its periodic tail reaches zero earlier, apply the first-hit statement with that earlier T<=2k. Constant tails retain least period one. The former 3*4^(k-1) bound remains true but is superseded by this stronger bound; no reviewed text is invalidated.

**Independent control and unexpected sharpness guard.** The literal six-site trajectory extends G124 as

    101011 -> 001010 -> 011011 -> 010010 -> 111111 -> 000000.

The first arrow is checked by its six ordinary left-to-right triples, which give 0,0,1,0,1,0. The first two words have least period six; 011011 and 010010 have least period three. Read backward, the 3-to-6 doubling is followed by a 6-to-6 preservation, exactly as proved. Moreover 101011 itself has cyclic factor 010 (at positions 1,2,3), so its predecessor again preserves period six. The control prevents claiming that the upper bound is automatically attained by doubling every other step. No such matching all-depth construction is supplied.

**Scope.** This sharpens the periodic spatial zero basin and the conditional ancestors of finite compatible rows in G149. G123's canonical periods still have unbounded growth, and this theorem does not bound the gaps between their increases. It does not prove that the phase-zero silver tail is periodic, zero-reaching, finite or infinite. A new multi-row invariant or an actual all-depth tail classification is still required. No new computation, full right extension or prize conclusion follows.

### G152. Rotation classes sharpen the periodic zero-basin first-hit bound (2026-10-07)

**Status and target.** Symbolic refinement, independently verified by Local L109. No experiment. Uses reviewed G123/G124. Prediction: quotienting translations sharpens the labeled-ring first-hit bound because a zero-reaching orbit cannot revisit a rotation class. Counterfactual: distinct labeled rows might require counting all their phases separately. An absorbing quotient argument removes those phases. Existing-record search found no necklace bound; necklace counting and cellular-automaton rotation quotients are established prior art, recorded in PRIOR-ART.md. No novelty claim for the method.

Let x be a nonconstant spatially periodic Rule30 row of least period p that first reaches zero at physical time T. By G124, p=3*2^a for some a>=0. Define L(q) to be the number of binary rotation classes of least period q. Then

    T+1 <= C_a := 2 + sum_(b=0)^a L(3*2^b),
    L(3)=2,
    L(q)=(2^q - 2^(q/2) - 2^(q/3) + 2^(q/6))/q  for q=3*2^b, b>=1.

In particular p=3 forces T<=3; p=6 forces T<=12. These are upper bounds, not assertions that each is attained.

**No repeated rotation class.** Write x_i=F^i(x), 0<=i<=T. Suppose x_j is a spatial translate of x_i for i<j<=T. On the p-cell ring the update commutes with rotations, so it induces a deterministic map on rotation classes. The class of x_i then lies on a cycle of length dividing j-i. It cannot subsequently enter the distinct absorbing class of zero. If the class already is zero, the first-hit property instead gives i>=T, impossible. Thus all T+1 classes are distinct. This uses no assumption that the cellular automaton is injective.

Every intermediate row reaches zero and has spatial period dividing p. G124 therefore permits only least period one or 3*2^b, 0<=b<=a. Period one contributes precisely the constant zero and constant one classes. Counting all binary classes of the remaining permitted periods gives C_a; some counted classes may lie outside the zero basin, so the inequality can be strict. A primitive word of length q has q distinct rotations even when repeated on a larger p-cell ring. There is no additional factor p/q in the class count.

**Counting derivation.** If A(q) counts labeled binary words of least period q, then 2^q=sum_(d|q) A(d). Divisor inversion gives A(q)=sum_(d|q) mu(d)*2^(q/d), where mu is the ordinary Moebius function. Dividing by q gives L(q). For q=3 the only squarefree divisors are 1,3. For q=3*2^b, b>=1, they are 1,2,3,6; their signs give the displayed formula. This is the standard primitive-necklace formula, not a new counting identity.

**Asymptotic consequence.** Along p=3*2^a tending to infinity, C_a=(1+o(1))*2^p/p. The largest term L(p) has that asymptotic by its explicit formula; all smaller terms together are at most a*2^(p/2), whose ratio to 2^p/p tends to zero. Hence along zero-reaching rows with T tending to infinity,

    p >= log2(T+1) + log2(log2(T+1)) - o(1).

Indeed log2(T+1)<=p-log2(p)+o(1), while the original labeled-ring count gives p>=log2(T+1); substituting that lower bound inside log2(p) yields the claim. G123's canonical ancestor tail C_n first reaches zero at time n, so the same bound applies to its p_n. This improves a generic counting floor; it gives no upper bound on doubling gaps or a temporal-wall exclusion.

**Independent arithmetic control and unexpected guard, by hand.** The two primitive period-three classes are represented by 001 and 011. The literal trajectory 011 -> 010 -> 111 -> 000 visits both classes (010 is a rotation of 001) and then the two constants; T=3 attains C_0-1. At period six the four-term formula gives (64-8-4+2)/6=9, so C_1=2+2+9=13. Counting labeled primitive words would instead give 54 and miss the rotation reduction. As the identified unexpected scope check, the stationary checkerboard has least period two and revisits its rotation class forever: the no-repeat argument requires eventual absorption at zero, not mere periodicity or finite ring size. None of these controls is a numerical run.

**Scope.** This is a necessary first-hit bound for periodic spatial tails and the reviewed canonical ancestry. It neither constructs a finite compatible wall head nor identifies the silver phase-zero forced tail. The all-depth wall-tail obligation remains open.

**G152 finite-control follow-up — six-cell quotient (GPT, 2026-10-07; independently confirmed by Local L109).** This is a literal finite transition-table proof candidate, not a new computational run or an asymptotic extension. Prediction: the necklace bound T<=12 is not attained at period six; the exact maximum is10. Counterfactual: all counted classes must lie on one longest absorbing path. The quotient branches and merges instead. The nine primitive rotation classes counted by L(6)=9 have these literal one-step images and canonical rotation representatives:

| Input representative | Literal Rule30 output | Output class representative |
|---|---|---|
| 000001 | 100011 | 000111 |
| 000011 | 100110 | 001101 |
| 000101 | 101101 | 011 (period3) |
| 000111 | 101100 | 001011 |
| 001011 | 111010 | 010111 |
| 001101 | 111001 | 001111 |
| 001111 | 111000 | 000111 |
| 010111 | 010100 | 000101 |
| 011111 | 010000 | 000001 |

The representatives are distinct modulo rotation, and their number equals L(6), so the list is complete. The two primitive period-three classes obey 011 -> 010 (class001) -> 111 -> 000. The constants obey1 -> 0 -> 0. The longest primitive-six class path starts at000011 and reaches zero after10 steps:

    000011 -> 001101 -> 001111 -> 000111 -> 001011 -> 010111
    -> 000101 -> 011 -> 001 -> 1 -> 0.

These arrows denote rotation classes, not literal labeled words; only the table's middle column gives literal images. Every displayed primitive-six class feeds this path. Together with G124, this predicts that exactly62 of the64 labeled six-cell rows reach zero; the remaining two are the stationary checkerboards of least period two. No longer-ring claim follows.

**Retained arithmetic failure and unexpected check.** My first hand draft wrongly gave the first output bit as1 for010111 and011111, overlooking that both center/right OR and left bit are1 there. That would have created a spurious nonzero quotient cycle. Correct XOR gives0 in both cases, as the table retains. Local's existing ring audit can independently check these transitions and the maximum without a new census. The separate stationary checkerboard is the scope guard: not all finite-ring rows belong to the zero basin.

**G152 instrument audit of Local L109's correction (GPT, 2026-10-07).** Read the changed predecessor enumerator and basin search; no rerun. For n>=3, every predecessor is fixed uniquely after choosing its first two bits: the descending equation fills every remaining cell, and the scalar forward check enforces both cyclic closing equations. Enumerating the four starting pairs therefore loses no predecessor. Sizes one and two are separately enumerated to handle aliased neighbors. Starting at zero, breadth-first search records minimum distances, which equal first-hit times because the forward map is deterministic. Exhausting the frontier proves predecessor closure, unlike a forward step cap. Any omitted zero-reaching state would have a first forward entry into the recorded set, contradicting that closure. Thus completeness rests on exhaustive predecessor enumeration and an empty frontier; the 1,500-step cross-check is a separate finite control, not the stopping certificate. The unexpected termination guard is zero's self-predecessor: marking it visited at initialization avoids re-enqueuing an absorbing self-loop. Local's original coverage claims and appended corrections are preserved. The corrected counts are Local's measurements, not an independently rerun GPT census.

### RSP — preregistered exact repeat-debt decision for Rudin–Shapiro (2026-10-07; NOT RUN)

**Lane and target.** GPT takes the existing Q7 Rudin–Shapiro row as a symbolic automaton-certificate block; no Local computation requested. The finite-ring bounds are independently reviewed and will not be enlarged. Existing-record search found the open lead but no recorded repeat-debt decision for it. Automatic-sequence first-order decision is standard prior art, not a new method. The target is the project's necessary repeat filter, not a finite-left construction.

Define r(n) as the parity of the overlapping occurrences of11 in the binary representation of n, with r(0)=0. Its four-state DFAO reads most-significant digits and stores (previous digit, accumulated parity); digit d sends (h,e) to (d,e XOR (h*d)), initially(0,0), output e. Leading zero padding leaves the value unchanged.

For nonnegative integers a,b,q,C define

    Rep(a,b,q) := q>=1 AND b>=a AND
                  FOR ALL s: (a<=s AND s<=b) IMPLIES r(s)=r(s+q).
    Safe(C) := FOR ALL a,b,q: Rep(a,b,q) IMPLIES b<=2*a+q+C.
    Bounded := THERE EXISTS C: Safe(C).

These use only addition, comparison, quantification and indexing an automatic sequence. The classical automatic-sequence logical decision theorem therefore applies. A verified FALSE answer to Bounded would exclude this companion at every finite left radius by the existing repeat obstruction. A verified TRUE answer only closes that obstruction route for this word; it would not establish wall compatibility or finite support. The inclusive endpoint b and the shifted compared index s+q must be retained.

**RSP0 controls, NOT RUN.** Check the four-state generator against the independent integer formula bit_count(n AND (n>>1)) modulo2 for n=0..4095 and selected 64-bit carry boundaries. Check the compiled Rep predicate against direct literal comparisons for all 0<=a<=b<=15 and 1<=q<=15. Check the logic on the constant-zero and alternating words: both Bounded answers must be FALSE. For the automatic powers-of-two indicator, G137 supplies Safe(0)=TRUE as a separate positive control. These controls are bounded instrument checks, not research evidence for r's all-length behavior.

**RSP1 blind prediction, NOT RUN.** Safe(0) for r is TRUE. This prediction is unobserved; if false, retain the least accepted violation and independently check every compared bit and the debt. **RSP2 fallback, NOT RUN.** If RSP1 fails, decide Bounded rather than guessing a finite constant from prefixes. If TRUE, obtain and verify a finite C; if FALSE, retain the exact quantified certificate and extract a parameterized family or witness procedure before claiming an all-radius exclusion.

**Limits and unexpected check.** First inspect available tooling; do not install a system runtime. Keep tools and bulk automaton artifacts outside Git, with small specifications and verification code in the record. Stop an individual formula at120 CPU seconds or1GB working memory, and stop custom construction at100,000 intermediate states; a limit hit is NOT RUN TO COMPLETION, not TRUE or FALSE. Record actual resource enforcement rather than assuming it. Export exact transitions and check certificates independently before elevating an answer to a theorem. The identified unexpected check is arbitrary leading-zero padding on synchronized integer inputs; compare at least three extra zeros and verify that projections admit unbounded padding. A finite bit-width or overflow cap would invalidate the all-length claim. No computation has run in this block.

### G153. Rudin–Shapiro passes the necessary repeat-debt filter (2026-10-07; computer-assisted theorem)

**Status.** Computer-assisted theorem, independently verified by Local L111 at 8f7841c. The direct RSP-S semantic reconstruction and debt-product argument have been audited and independently replayed; the Walnut compilation dependency is discharged. RSP preregistration was pushed at dd61eb5 before runs. No finite-left realization or prize claim. The raw universal decision is TRUE and an independently implemented graph-product check agrees, conditional on the compiled repeat predicate's semantics. The standard automatic-sequence logical decision theorem is the prior-art method, not a new technique.

Let r(n) be the parity of overlapping occurrences of11 in the binary representation of n, r(0)=0. Proposed statement: for every a,b>=0 and q>=1, if r(s)=r(s+q) for all a<=s<=b with b>=a, then

    b <= 2*a+q.

Thus Safe(0) and Bounded in the RSP plan hold. This is a necessary-filter pass, not a candidate construction. RSP2 was not run because a verified Safe(0) would already settle Bounded positively.

**Certificate chain.** The four-state output automaton remembers the last binary digit h and the parity e. Reading d updates (h,e) to (d,e XOR h*d); induction on digits proves the definition of r, including leading-zero padding. Pinned Walnut7.1.0 source commit67e69c248d07324b25de1d4a498e877ac504999a compiled the exact RSP predicate

    q>=1 AND b>=a AND FOR ALL s:
        (a<=s AND s<=b) IMPLIES r(s)=r(s+q)

into a deterministic78-state automaton over synchronized most-significant binary digits of (a,b,q). Its exported file SHA256 is1a0f3ac7b9222da522c2077b1dbeccb8098bc9df15a1200af6920a2243f309b6. Review artifacts rsp-repeat-dd61eb5.txt and rsp-product-dd61eb5.json are in the shared scratch; bulk outputs stay outside Git. The formula, driver and replay verifier are in tests/probes/prizes/rudin_shapiro_repeat.py.

The independent checker intersects that exported relation with a separately derived debt comparator. After a digit triple, the signed prefix debt d=b-2a-q updates to 2*d+b_bit-2*a_bit-q_bit. Values at most-1 stay negative under all later digits; values at least3 stay positive. Saturation to the five states -1,0,1,2,3 is therefore exact, with final d>0 accepting. Breadth-first traversal of the product has84 reachable states and no accepting state. Closed reachability proves emptiness for all finite digit strings, not a finite integer horizon. This product check alone does not establish the compiled relation's semantics. The separate RSP-S reconstruction, audited and replayed by Local L111, discharges that dependency for this exported relation. Walnut's separately compiled universal formula also returned TRUE.

**Controls and failures.** RSP0 passes: the supplied generator versus the integer bit-count formula at0..4095 and189 selected64-bit carry-boundary inputs;2040 admissible literal repeats through a,b<=15 and q<=15; constant-zero and alternating Bounded=FALSE controls; and G137's powers-of-two Safe(0)=TRUE control. An expanded4096-tuple replay includes q=0 and reversed ranges and checks three additional leading zeros. The debt comparator matches32768 independent integer comparisons through31. These finite controls check instruments, not the universal theorem. The identified unexpected padding check is supplemented by the initial all-zero-digit self-loop and unbounded finite-graph traversal; no fixed bit width is used.

The first RSP0 run failed because Walnut resolves command filenames inside its command directory; the absolute positional filename was invalid. That failed run is retained, lookup corrected, and RSP0 completed before RSP1. Python's toolchain metadata request also failed its certificate-store check; system curl succeeded without disabling TLS. A checksum-verified portable Java archive and isolated tool/dependency caches were used, with no system-runtime installation. Formula processes had120 CPU-second limits,768MiB Java heap bounds,1GiB sampled-RSS termination checks and an additional180-second wall limit. No limit was approached: successful formulas took about0.42 seconds wall each, with sampled peak RSS below50MiB. Resource samples are not exact peak-memory measurements. No Local computational job was duplicated.

**Scope and next obligation.** After independent review, the ordinary repeat-filter exclusion route is closed for this specific automatic word. Its forced initial tail and full right extension remain unresolved. Passing this necessary inequality is neither finite evidence for support nor a theorem that a compatible finite row exists.

### RSP-S. Independent semantic reconstruction plan (2026-10-07; not run)

G153 remains a candidate awaiting Local review. GPT will build a distinct least-significant-digit nondeterministic automaton for the existence of s in [a,b] with r(s) != r(s+q). Binary addition has one carry; comparisons are updated by each newly read more significant digit; parity of adjacent 11 pairs is unchanged by reversing binary digits. One implicit zero input digit completes a possible addition carry. Complement this mismatch language within q>=1 and b>=a and compare it with the reversed exported repeat automaton.

Prediction: the symmetric difference is empty. Counterfactual: a shortest distinguishing digit word, replayed as integer a,b,q and literal bits, exposes either an exported-relation error or an independent-construction error; do not silently repair or promote G153. Controls: hand anchors, all 4096 triples through15, and independently computed additions/comparisons. Unexpected check: mutate one accepting output in the exported relation and require a distinguishing witness. Stop at100,000 reachable comparison states,120 CPU seconds or1GiB working memory; a stopped traversal is incomplete. Tooling is Python only, with bulk results outside Git. No new Local job requested: GPT owns this construction; Local owns the proof audit.

**RSP-S result (2026-10-07, publication checkpoint).** The independently constructed LSD mismatch automaton and the reversed Walnut repeat export agree: the full comparison graph closes after17,033 reachable states with no distinguishing word. This is a complete finite-language equivalence traversal over all nonempty synchronized binary strings, not a prefix measurement. G153 remains a candidate for independent Local proof review.

For each LSD input digit triple, nondeterministically choose the corresponding digit of s; its sum with q and the carry determines the digit of s+q. The state retains the previous digits of s and s+q and the XOR of their adjacent-11 parities. Each newly read more significant digit overrides an unequal lower-digit comparison; equal digits preserve it. Thus the final comparisons enforce a<=s<=b. Such an s fits within the input width because s<=b; s+q needs at most one extra digit. One implicit zero input digit with s digit zero completes that carry and its last adjacent pair. Reversal preserves adjacent-11 parity, so this construction computes the same r without relying on Walnut's generator or formula compiler. Complementing existential mismatch inside q>=1,b>=a gives the intended repeat language. Reversing the exported MSD automaton exchanges initial and accepting states; simultaneous subset traversal tests equivalence exactly. The nonempty-input guard excludes the empty digit string.

All4,096 literal triples through15 and1,024 arithmetic/comparison controls pass. The unexpected accepting-output mutation is detected after9 reached states, with witness(a,b,q)=(0,0,0): the changed export incorrectly accepts the prohibited zero period. The initial attempt failed before any language comparison: the certificate argument was a string rather than a Path, and the wrapper's ps memory sample was denied by the sandbox. The failed console is retained, Path parsing corrected, and the wrapper rerun with authorized process inspection. No theorem is inferred from the failed attempt. The corrected run exits0 in1.689 wall seconds, sampled peak RSS55,704KiB, with the120-second CPU limit and sampled1GiB memory guard enforced; samples are not exact peak memory. No cap approached and no additional Walnut computation was run.

Verifier: tests/probes/prizes/rudin_shapiro_semantics.py, supplied with the same rsp-repeat-dd61eb5.txt certificate identified in G153. Only Python is required. This removes dependence on Walnut compilation for the exported predicate's semantics, conditional on correctness of the new construction and its replay; Local still needs to audit that argument and G153's debt-product argument. The actual forced initial spatial tail remains open.

**RSP review and portability follow-up (2026-10-07).** Local L111 verifies G153's carry completion, reversed-language equivalence and saturated debt argument, and independently checks 32^3 literal triples with its own generator and parser. Both certificate replays were reproduced. Its unfinished MSD reconstruction was stopped on receiving the lane announcement, and its failure is retained; that incomplete construction is not evidence for G153. The original NOT RUN/pending statements above are historical preregistration/checkpoints, not current status.

Local caught that int.bit_count requires Python3.10 while its default runtime is3.9. GPT replaced the finite-control bit counts in both scripts with exact bin(x).count('1') counts. Under a genuine Python3.9.6 runtime, the replay still has the same certificate hash,78 relation states,84 product states and4,096 passing literal/padding controls; the independent reconstruction still closes at17,033 states, its mutation is detected and1,024 arithmetic controls pass. No additional Walnut run or research experiment was needed. G154 remains independently unreviewed.

### G154. Finite-tail exceptions in a minimal trace family are empty or countable dense (2026-10-07)

**Status and target.** Symbolic scope audit, independently verified by Local L112; no computation. Uses reviewed G140's wall coding and radius clock, and generalizes G147's phase-counting argument to a minimal trace family. This is an elementary dynamical argument, not a novelty claim about substitution systems. Prediction: generic infinite support cannot exclude the original Rudin–Shapiro trace. Counterfactual: minimal recurrence plus a generic exclusion forces every individual trace to have an infinite tail. The conditional dense-exception argument below shows why that inference fails. G153 and its RSP-S certificate are not assumed in this proof.

Let X be a nonempty compact, forward-shift-invariant family of one-sided visible binary words in which every forward orbit is dense. Assume X is infinite. Under G140's bijection Phi from visible words to compatible white-phase initial rows, set

    E_X = {c in X : Phi(c) has finite left support}.

Then E_X is empty or countable dense in X. Its complement is residual and has full measure for every shift-invariant probability measure on X. For each fixed radius L, at most 2^L words of E_X have radius at most L. None of these statements excludes a specified word of X.

**Proof.** There are at most 2^L binary rows supported in the first L cells. Injectivity of Phi gives the same bound for words, so E_X is countable. The conjugacy F Phi = Phi shift and finite-support preservation show that E_X is forward invariant. If nonempty, it contains a dense forward orbit and hence is dense. On that orbit radii increase by exactly two at each shift.

An infinite minimal compact trace family has no eventually periodic points: such a point would yield a finite periodic orbit in X, whose dense orbit would force X to be finite. It also has no isolated points. If a cylinder isolates c, minimality supplies a positive return of c to that cylinder, forcing shift^n(c)=c. More explicitly, compactness gives a finite cover by inverse images of that cylinder; applying the cover to shift(c) supplies the positive return. The resulting periodic point contradicts infinitude. Thus each singleton is nowhere dense, and countability makes E_X meagre. For an invariant probability measure, an atom at c would give every distinct forward image mass at least that atom's mass, since the preimage of the image contains c. Infinitely many such images contradict total mass one. Hence every such measure is nonatomic and E_X is null. This argument does not require Phi to preserve a preferred measure.

**Rudin–Shapiro supplies such an X.** Write r(n) for adjacent-11 parity. Appending a binary digit gives r(2n)=r(n) and r(2n+1)=r(n) XOR (n modulo 2). The pair (r(n),n modulo 2) is the fixed word starting at a of the substitution

    a -> ab, b -> ad, c -> cd, d -> cb,
    a=(0,0), b=(0,1), c=(1,0), d=(1,1).

Its directed graph reaches a from every letter in at most three steps and reaches every letter from a in at most three; the a self-loop pads each composed path to exactly six. Thus every sixfold substituted letter contains every letter. Any factor of the fixed word occurs inside some substituted prefix of a; consequently every sufficiently large substituted letter contains it. The fixed word is tiled by equal-length such substituted letters, so every sufficiently long factor contains that chosen factor. Projecting to the first coordinate preserves this bounded-gap property. The binary shift closure X_r is therefore minimal: every factor of r occurs in every member with bounded gaps, so every forward orbit meets every cylinder of X_r.

For completeness r is not eventually periodic. For m<2^(k-1), the separated binary blocks give r(2^k+m)=r(m) and r(3*2^k+m)=1 XOR r(m). If r were eventually q-periodic, taking k arbitrarily large in the first identity transfers that periodicity to every initial m, making it purely q-periodic. Now choose k with 2^(k-1)>q. The first identity at m=0 through q-1 says translation by 2^k fixes the entire q-periodic word; translation by 3*2^k must then fix it too. The second identity at m=0 contradicts that, since r(0)=0 and r(3*2^k)=1. Thus X_r is infinite and the stated dichotomy applies.

**Unexpected periodic-family check.** If X is instead a finite periodic orbit, E_X is empty: a finite row corresponding to a p-periodic visible word would return after p applications of F, contradicting radius growth by 2p. The all-zero visible control gives the infinite checkerboard initial tail, not a finite row. This verifies why temporal simplicity is not a spatial-support certificate.

**Scope.** For Rudin–Shapiro, generic members of its binary shift closure have infinite forced initial tails, independently of the pending repeat-filter decision. If even one member has finite support, its dense shift orbit has growing finite radii and remains fully consistent with generic infinite support and infinite-support accumulation points. The original r is a specified member; this argument neither excludes it nor constructs an exception. The missing obligation remains a direct spatial-tail constraint on Phi(r), and full right extension is separate. No prize claim.

### G155. Trace factor complexity bounds the number of finite-tail exceptions (2026-10-07)

**Status and target.** Symbolic deduction, independently verified by Local L113; no computation. Uses reviewed G139 inverse locality, G140 coding/radius growth and G154 (Local L112). The record search found G147/G154's exponential fixed-radius count and G139's fixed-depth temporal factor bound, but not this growing-radius exception count. This is an elementary application of substitution factor counting, not a new general complexity theorem. Prediction: Rudin–Shapiro's exception count is at most linear in radius. Counterfactual: temporal zero entropy alone resolves whether there is even one finite-tail exception; the matching conditional lower bound shows the remaining gap.

For a forward-shift-invariant trace family X, let P_X(k) count its length-k factors and N_X(L) count c in X whose compatible initial row Phi(c) has radius at most L. For integers L>=1, put k=ceil(L/2). Then

    N_X(L) <= P_X(k).

**Proof.** G139's inverse recurrence determines the first L initial cells from the visible prefix c_0 through c_(k-1): the physical-time determining window at depth j is [0,j-1], containing exactly ceil(j/2) even samples. Thus two visible words sharing their first k bits have identical initial rows through depth L. If both rows are zero beyond L, the entire rows agree; injectivity of Phi makes the words identical. Hence the exceptional words inject into their length-k prefixes, a subset of X's factors. This also proves Local L112's sharper universal bound 2^k, without assuming that different arbitrary length-k prefixes necessarily produce different length-L rows.

**Rudin–Shapiro bound.** Use G154's four-letter length-two fixed substitution word. For k>=1 choose m minimal with h=2^m>=k; then h<2k. Any length-k factor fits inside two consecutive level-m substituted letters, with its start at one of h offsets in the first. There are at most sixteen ordered letter pairs. Projection to the binary word cannot increase this count, so

    P_(X_r)(k) <= 16*h < 32*k,
    N_(X_r)(L) < 32*ceil(L/2).

This is a deliberately coarse all-length bound, not a claim about the exact known factor complexity. If a finite-tail exception c of radius R exists, its time shifts have distinct radii R+2t. For L>=R this gives

    N_(X_r)(L) >= floor((L-R)/2)+1.

Consequently N_(X_r) is either identically zero or grows linearly in L, with matching upper and conditional lower orders. No existence has been supplied.

**Unexpected endpoint check.** Replacing ceil(L/2) by floor(L/2) is wrong. At depth three G138 gives v_3(0)=1-c_1: words with the same c_0 but different c_1 have different depth-three cells. At even depth four the determining prefix has two symbols, as v_4(0)=c_0*c_1. Thus the count uses the actual growing window, not a fixed-depth entropy limit or an omitted endpoint. The bound is compatible with a dense countable exceptional set and unbounded radii from G154.

**Scope.** This counts hypothetical finite-tail rows within the Rudin–Shapiro family. It excludes neither the original word nor any specified shift and gives no full right extension. The necessary count is linear, not positive entropy. A spatial invariant forcing N_(X_r) to be zero is still missing; another prefix census cannot establish that invariant. No prize conclusion.

### G156. Temporal rotation classes sharpen the fixed-period edge-history bound (2026-10-07)

**Status and target.** Symbolic edge-diagonal proof, independent review pending; no computation. Returns to Q7's open period-growth/settling lead, distinct from Local's G155 review. G7 already proves the absolute-profile tree bound K<=4^P-1. Prediction: counting temporal rotations gives a stronger bound of order 4^P/P. Counterfactual: rotation-equivalent pairs can occur at different edge depths despite the absorbing zero boundary. The first-hit argument excludes that. The small-period controls below are literal finite graph proofs, not a sampled census.

Let K count a compatible prefix w_0 through w_(K-1) of P-periodic diagonal profiles rooted at (w_(-1),w_0)=(0,1^P). On pairs define

    B(a,b)=(S b XOR (a OR b),a),

with cyclic time shift S. G7's diagonal equation gives B(w_(j-1),w_j)=(w_(j-2),w_(j-1)). The zero pair is fixed, and the root maps to it. Thus the pair at depth j has first zero-hit time j+1: an earlier zero would force the root to be zero after further applications. B commutes with temporal rotation, so rotation-equivalent pairs have the same first-hit time. Pairs at different depths are therefore inequivalent even after rotation. Including the zero class gives

    K+1 <= N_4(P),
    N_4(P) = (1/P) * sum over d dividing P of phi(d)*4^(P/d).

Here N_4(P) counts cyclic words of length P over the four-letter pair alphabet. For a rotation by h, a fixed pair word has gcd(P,h) freely chosen letters, hence 4^gcd(P,h) possibilities. Averaging fixed counts over the cyclic group and grouping equal gcd values gives the displayed standard necklace formula. All periods dividing P are included; using only primitive necklaces would undercount.

For P>=2 the nonidentity contribution is at most (P-1)*4^(P/2)/P. Consequently N_4(P)=(4^P/P)*(1+o(1)). Along prefixes with K tending to infinity this strengthens G7's lower period floor to

    P >= log_4(K)+log_4(log_4(K))-o(1).

It is a lower bound on period, not an upper bound or a waiting-time budget.

**Period-one control.** N_4(1)=4. The root path (0,1),(1,1),(1,0) contains three pairs; each maps backward to its predecessor and then zero. The last pair has no constant-profile child. Thus K=3 attains the bound.

**Unexpected nonabsorbing-class check, period two.** Encode two-bit temporal words with the least significant bit at time zero. S swaps1 and2, fixes0 and3. The pairs (1,2) and (2,1) form a B-cycle and are rotations of one another, so their single rotation class cannot lie on a rooted edge history. N_4(2)=(16+4)/2=10; excluding zero and this additional class gives K<=8. The eight-pair path

    (0,3),(3,3),(3,0),(0,1),(1,3),(3,1),(1,1),(1,0)

attains it. Substitution in B sends each pair to the preceding one and the first to zero. Hence the maximum common-period-two rooted prefix has K=8. This check both tests the quotient convention and prevents mistaking every necklace class for an absorbing class.

**Prior-art map distinction.** Re-read Nersissian's section4 through Theorem13: its backward map B is exactly G7's edge-diagonal map, and its absolute-profile first-hit argument is the same mechanism. The earlier vertical-wall audit remains correct: that inverse shifts the first coordinate rather than the second and is a different map. The paper's profile bound is not a new wall theorem; the rotation quotient here applies directly to the diagonal tree. Standard necklace counting was already recorded for G152. No novelty is claimed for that counting method.

**Scope.** This improves the necessary period lower bound for every compatible edge branch and certifies the two smallest controls. It supplies no sublinear upper period growth, no adaptive waiting bound below slope3, no finite-left exclusion and no prize result. Q7's all-branch settling obligation remains open. No period16 graph, new ring census or Local computational job is requested.

**G155 source-checked refinement (2026-10-07; application checked by Local L114).** Local L113 suggested P_r(k)=8k-8 from finite factors and explicitly requested a source check. Allouche and Shallit, [Complexité des suites de Rudin-Shapiro généralisées](https://www.numdam.org/item/JTNB_1993__5_2_283_0.pdf), section2, Theorem1 on printed page287, proves exactly this formula for k>=8. Read printed pages285-288, including Lemmas1-2, Propositions1-2 and the small-length table. The paper's substitution is a->ab, b->ab', a'->a'b', b'->a'b; renaming a'=c,b'=d gives G154's substitution exactly, with the same binary output coding and start at a. The introduction identifies d=1 with adjacent-11 parity. Thus the theorem applies to precisely the word used here, not a differently generalized Rudin–Shapiro sequence.

Combining the published theorem with reviewed G155 gives N_(X_r)(L)<=8*ceil(L/2)-8 for L>=15. For k=ceil(L/2) from1 through7, the paper's binary factor table gives respective upper bounds2,4,8,16,24,36,46; k=8 gives56. These are source values, not a new measured census. The conditional linear lower bound from G155 is unchanged.

**Identified unexpected check.** Do not extrapolate the affine formula below its threshold: k=7 has46 factors whereas8k-8=48; k=1 would give zero instead of2. The source proof derives the four-letter factor count, then uses injectivity of binary coding on length-eight factors and extends that property to longer factors. The reported length-eight base enumeration was read but not rerun here; this is reliance on a published theorem, not a claim to have independently re-proved it.

The extracted PDF text dropped comparison signs; rendered printed pages285-288 were inspected before applying the threshold. A guessed download URL failed; the official article PDF succeeded. No runtime installation, new Walnut run, extended prefix scan, full-tail construction or prize claim. G155's coarser bound remains independently verified; the tighter source-based application is offered for Local's check.


### G157. Odd factors do not enlarge the rooted edge-history tree (2026-10-07)

**Statement.** Let P>=1 and Q=2^v, where v is the exponent of two dividing P. The common-period-P rooted tree of G7 is isomorphic to the common-period-Q tree: repeat each Q-bit temporal word P/Q times. This preserves depth, the predecessor B, zero hits and temporal rotation classes. In particular its maximum prefix length K is identical, and G156 sharpens to

```math
K+1\le N_4(Q)=\frac1Q\sum_{d\mid Q}\varphi(d)4^{Q/d}.
```

Every odd P has exact maximum K=3; every P with v=1 has exact maximum K=8. These are finite-tree statements, not a bound on physical transient lengths.

**Proof.** A child c of the adjacent pair (a,b) obeys

```math
c(t+1)=a(t)\oplus\bigl(b(t)\vee c(t)\bigr).
```

Suppose a and b have a common dyadic period d. If b has a one, a reset at t0 fixes c(t0+1)=a(t0) XOR1 independently of c(t0). The same reset occurs at t0+d, so c agrees with its d-shift immediately after the reset and thereafter by the recurrence. For any integer t choose an earlier reset; hence the entire periodic word c has period d. If b is zero, summing d steps gives c(t+d)=c(t) XOR sigma, where sigma is the parity of one d-block of a; in particular c has period 2d. Starting from the constant root, induction makes every profile's least period a power of two. Each profile is also P-periodic, so its least period divides P and therefore divides Q.

Restrict every profile to its first Q letters. Since all have period Q, restriction commutes with shift, OR, XOR and B. Conversely repetition embeds any Q-periodic rooted history in the P-periodic tree. The two maps are inverse on every node and edge, and a rotation by t on either side depends only on t modulo Q. Thus the entire rooted trees and their rotation quotients agree. Apply G156 at Q. Its literal Q=1 and Q=2 controls supply the asserted exact maxima. Square.

**Controls and identified unexpected check (symbolic, no run).** Local L114's P=3,5,7 maxima3 and P=6 maximum8 follow exactly, rather than merely fitting a pattern. At P=6 the necklace upper bound drops from700 to10; excluding the known nonabsorbing class gives exact K=8. The rooted hypothesis is essential: the ambient period-three pair (0,100), with the cyclic word written in temporal order, has least pair period3 and cannot be reduced to Q=1. It is excluded by the rooted induction, not by an assertion that all periodic B-states are dyadic. This is the unexpected scope guard.

**Prior art and limits.** This is an explicit finite-tree corollary of the reset/integration mechanism in Nersissian, section4, Theorems10-12 (read directly); that source attributes dyadic diagonal periods to Jen. No novelty is claimed for period doubling or the reset proof. The source's initialized physical tails do not alone establish equality of our arbitrary-phase rooted trees, so the two-sided periodic argument above supplies that transfer. This does not identify maximum K at Q>=4, control actual settling times, establish an upper period-growth law, or solve a prize problem. No computational experiment was launched.

### G158. Only even-parity integration branches the temporal-rotation quotient (2026-10-07)

**Statement.** Quotient G7's common-period-P rooted tree by simultaneous temporal rotation of each adjacent pair. It remains a finite rooted tree. At a node represented by (a,b), its number of child classes is classified as follows:

- If b is nonzero, there is exactly one child class.
- If b=0, write q for the least period of a and sigma for the parity of one q-block. The two words cannot both be zero. For sigma=0 there are exactly two child classes, both of least word period q.
- For sigma=1 and 2q dividing P, there is exactly one child class: the two literal children, of least period2q, differ by a rotation through q.
- For sigma=1 and 2q not dividing P, there are no children.

By G157, q is dyadic and divides Q=2^v2(P), so the final case means q=Q. Thus genuine branching in the quotient occurs precisely at even-parity zero-driver nodes; leaves occur precisely when odd-parity integration would exceed the allowed dyadic period. In particular, if E counts the even-parity zero-driver node classes and L counts leaf classes, then L=E+1. Period doubling itself supplies no new branch choice after phase quotienting.

**Proof.** Rotation commutes with B. Every node orbit has a unique predecessor orbit. Distinct depths cannot coincide by G156's first-zero-hit argument; no reconvergence is possible because predecessors are unique. The root is rotation invariant. Hence the quotient is a finite rooted tree. To find its children, rotate any child so that its parent is a chosen representative. Two representative children give the same orbit exactly when a rotation preserving that parent exchanges them.

An active driver b resets the scalar recurrence, as in G157: one complete driver period determines the unique periodic solution c. It has period dividing a common period of a and b, hence divides P. There is one child, before as well as after quotienting.

For b=0 the equation is c(t+1) XOR c(t)=a(t). Choosing c(0) gives exactly two complementary solutions. Summing q steps gives c(t+q)=c(t) XOR sigma. If sigma=0, both solutions are q-periodic. Their least periods are exactly q: any period of c is a period of its difference a, so it must be divisible by q. If sigma=1, their least periods are exactly2q for the same reason, and their q-shifts are their complements. Such solutions close at period P if and only if2q divides P.

Finally the stabilizer of (a,0) consists precisely of shifts divisible by q. For sigma=0 those shifts fix each child and cannot exchange the complementary solutions; for sigma=1 a shift by q exchanges them. This proves the child-class counts. A finite rooted tree with outdegrees0,1,2 has L=E+1 by counting edges in two ways. Square.

**Symbolic controls and identified unexpected check.** At P=1, the three G156 nodes form one chain and the last node (1,0) is the excluded-doubling leaf. At P=2, a nonzero word of least period1 has odd block parity, and a binary word of least period2 is01 or10, also odd. There are therefore no even-parity branch nodes; the quotient is one chain, with its eight nodes given by G156. The apparent first doubling is two phase copies of one continuation.

The unexpected even-parity guard is a=0110, of least period4: with b=0 its solutions are c=0010 and1101. Their child pairs are not rotation equivalent, because any rotation fixing the parent a is a multiple of4. This is a local transition check, not a claim that this parent lies in the rooted tree. By contrast a=01 integrates to0011 and1100, exchanged by rotation through2. Confusing these two parity cases would erase actual possible quotient branching.

**Prior art and scope.** The scalar reset/integration classification is the existing mechanism of Nersissian section4, Theorems10-12, and G7. The additional statement here classifies child orbits using the parent stabilizer; the record's G152 spatial quotient is different and need not be a tree. G157 is a pending proof dependency for the dyadic leaf identification, while the child-orbit calculation above holds without that dependency whenever a is periodic. No novelty is claimed for reset, integration or elementary tree counting. No new computation, larger graph census, uniform bound on E, period-growth upper bound, physical settling bound or prize solution is asserted.

### G159. Genuine quotient branches are separated by at least seven depths (2026-10-07)

**Statement.** On any rooted periodic edge history, two consecutive even-parity zero-driver branch nodes of G158 have depth difference at least7. Consequently the number of temporal-rotation classes at depth n in the common-period-P tree is at most2^ceil(n/7). This is a branch-choice rate bound, not an upper bound on the height of the tree or on physical waiting times.

**Proof.** At an even-parity branch write the profiles starting at its zero driver as0,c,d,e,f,g,h. The previous profile a is nonzero and satisfies Delta c=a, so c is nonconstant. The equation for d is S d=c OR d. A one in the periodic c resets d to1; thereafter1 persists. Periodicity therefore forces d=1. Next S e=1 XOR c, so e is nonconstant. If f=0, its equation S f=1 XOR(e OR f) would force e=1, impossible. Thus profiles c,d,e,f are all nonzero.

If g=0 then its equation forces e=f. Substituting in the equation for f gives S e=1 XOR e, so e and c are alternating and a=Delta c=1. But the constant-one profile has least period1 and odd block parity; it cannot be the even-parity branch under consideration. Hence g is nonzero.

If h=0 then f=g, and the equation for g gives e=f XOR S f. The equation for f is S f=1 XOR(e OR f). At any time with f=0 these two identities imply S f=1 XOR S f, a contradiction. Thus f must be constant1; then its equation would give S f=0, another contradiction. Hence h is nonzero. No zero-driver node occurs in the next six depths, proving the spacing claim.

A path from the root to depth n crosses at mostceil(n/7) binary branch nodes. By G158 all other nodes have at most one child in the rotation quotient. The binary decision words for distinct depth-n nodes are prefix-free (a proper prefix would give the same path until one node already ended at depth n). A prefix-free collection with maximum word length m has at most2^m members, by extending its words to disjoint sets of m-bit strings. Take m=ceil(n/7). The case n=0 has the single root. Square.

**Controls and identified unexpected check (symbolic, no run).** The constant-one predecessor is essential: odd-parity integration gives an alternating c, and the resulting segment0,c,1,c,c,0 has zero drivers only5 depths apart. This is exactly the period-two control and rejects extending the seven-depth claim to all zero drivers. The even-parity local guard a=0110 from G158 is nonconstant and does not trigger that exception. No claim of attainment at distance7 is made. A tree consisting entirely of unary nodes can have arbitrary height while obeying the depth-n count1; this is the unexpected inference guard against converting a branch-rate bound into a settling bound.

**Prior art and dependencies.** The calculation uses G7's recurrence and the pending G158 quotient classification; the six-step exclusion is proved directly here. Existing reset/integration prior art and G156-G158 are the relevant records. No computation or literature novelty claim is made. The number and location of later branch nodes, dyadic-period record spacing and adaptive physical waiting budgets remain open.

**G158-G159 phase-cost audit (2026-10-07).** A word-only temporal-rotation quotient does not preserve G8's adaptive reset-front edge costs. This is a symbolic counterexample, not a new computational run. At common period2 the rooted prefix is (0,3),(3,3),(3,0). With initial arrival phase0 its first two increments are1,1 and the next zero-driver increment is0, so both children arrive at phase0. The children (0,1) and (0,2), using G156's least-significant-bit temporal convention, are word rotations of each other. But their next costs are delta(1,0)=1 and delta(2,0)=2. Thus their elapsed four-edge costs are3 and4. The period-doubling step that G158 collapses structurally can retain different future waiting costs. The example uses the full-line periodic-parent front of G8; no birth-clamped physical settling claim is imported.

The identified unexpected check is the co-rotated clock: rotating1 to2 and phase0 to1 gives delta(2,1)=1, matching delta(1,0). Rotating both the temporal words and the arrival phase is valid; discarding the relative phase is the failed shortcut. Constant-one and zero drivers retain the direct controls delta=1 and0, respectively.

For a pair of least common word period q dividing P, its word-rotation orbit has exactly q relative-phase classes in the phase-augmented quotient. Fix a representative pair; rotations preserving it are precisely shifts divisible by q, so arrival phases are identified modulo q. This elementary fiber count retains the clock rather than erasing it. Conditional on the pending G157 and G159 proofs, q<=Q=2^v2(P), so the number of phase-augmented classes at depth n is at most Q*2^ceil(n/7). That is a count, not a weighted-cost certificate. The two period-two children already give distinct relative-phase classes in one word orbit.

**Result and next obligation.** Word-only branching/width cannot alone supply the adaptive waiting budget. A proposed quotient potential must keep the relative-phase coordinate, or prove an independent bound uniform over its fibers. G8 already retains this coordinate in h(a,b,r); its finite-period potential certificates and open uniform size bound are preserved. No larger census or duplicate Local job is proposed. The record's earlier word-only versus phase-aware cycle distinction remains consistent with this rooted counterexample.

### G160. A closed arrival-phase gate removes only transient front states (2026-10-07)

**Statement.** Use G8's common-period-P full-line reset-front graph, excluding the zero word-pair. For a state (a,b,r), define the gate by

- if a is nonzero: a(r-1)=1;
- if a=0: (S b XOR b)(r-1)=1.

Indices are modulo P. The gate is forward invariant. Every nonzero compatible front path is in it after at most two edges. The rooted front starts at the exceptional pair (0,1) and enters the gate after one edge. Every compatible phase-augmented cycle lies entirely inside the gate.

**Proof.** An edge goes to (b,c,r'), with S c=a XOR(b OR c). If b is nonzero, r'=r+delta(b,r) is exactly one time past the first black b cell at or after arrival. Thus b(r'-1)=1 and the child is in the first part of the gate regardless of the parent's phase.

If b=0, delta=0 and r'=r. The child obeys S c XOR c=a. Since (a,b) is not the zero pair, a is nonzero and c is nonconstant. A gated parent has a(r-1)=1, so the child's second gate condition holds. This proves invariance. From any ungated state an active b enters immediately. If b=0, its child has nonconstant driver c, so the following edge enters immediately. No nonzero pair has the zero pair as a child, by the same recurrence. Hence two edges suffice. The root has constant-one driver and cost1, giving the gated child (1,1). On a cycle every state has at least two preceding edges on the same cycle; the two-edge entry assertion puts every state inside the gate. Square.

**Phase counts and certificate transfer.** For a fixed pair of common period P, the gate allows exactly the number of black bits in a when a is nonzero, or the number of transitions in b when a=0. On its relative-phase fiber of size q, use the corresponding counts in q letters. This is an exact local restriction, not a census of reachable states. If a phase-sensitive potential on the gated graph bounds interval debt at slope gamma>=0 by H, the whole nonzero graph has the bound H+2P: discard at most two initial edges, each of cost at most P, and apply the gated certificate to the rest. For the rooted front, the initial cost is1, giving H+1 instead. Intervals wholly inside the discarded part obey the same conservative bound. These are full-line front statements; birth clamps and sublinear period growth remain separate obligations.

**Controls and identified unexpected check (symbolic, no run).** The root (0,1) itself fails the second gate condition because a constant word has no transitions; its first child satisfies the first condition. The derivative condition at a=0 is essential, as the period-two integrated children have zero first coordinate yet valid arrival phases.

The two-step threshold is needed on the unrestricted graph. In temporal order take a=0101, b=0000, r=1 at period4. Integration gives c=0011. The parent fails a(0)=1, and the child (0,c,1) still fails Delta c(0)=1. Its active c then enters on the next edge. This checks a local compatible path, not root reachability. The identified unexpected cycle guard is that every cycle already lies in the gate: G8's compatible slope-2 obstruction survives unchanged. Gate pruning cannot improve cycle means or cure that obstruction; it removes transient arrival phases only.

**Record and scope.** This is a direct finite-graph consequence of G8's reviewed next-black arrival rule and G7's diagonal recurrence. It does not depend on the pending G157-G159 proofs. No computation or literature novelty claim is made. A uniform gated potential size bound remains unproved; the gate by itself gives neither a settling bound nor a prize result.

**Review checkpoint (Local L115, 2026-10-07).** G157-G159 independently checked and promoted. The source entries’ pending labels describe their original publication; the reviewed structural results now support the relative-phase fiber count. Local found no rooted genuine branch at Q<=8 (all common periods P<=15); its Q=16 build was stopped, not certified. G160 also independently checked by Local L116; G161 below remains pending.

### G161. One representative path decides the first genuine rooted branch (2026-10-07)

**Statement.** For a dyadic common-period cap Q, the existence of an even-parity zero-driver node anywhere in the rooted tree can be decided by one representative path, without enumerating its phase copies. Start at (a,b)=(0,1) with least common period q=1. Repeat:

1. If b is nonzero, construct the unique q-periodic child c by resetting at any black b cell and following the scalar recurrence. Replace (a,b) by (b,c); keep q.
2. If b=0 and one q-block of a has even parity, stop: this path is a rooted genuine-branch witness.
3. If b=0 and that parity is odd, then if q=Q stop: no rooted genuine branch exists at this cap. Otherwise integrate a with c(0)=0 over2q letters, repeat a and b to that length, replace the pair by (b,c), and double q.

The procedure terminates. It uses O(Q) working bits apart from a retained witness, and O(sum q_j) bit updates along its visited path; in particular O(QK) for K visited nodes. These are symbolic complexity bounds, not runtime measurements or a claim that K is small.

**Proof.** All rooted pair periods are dyadic by verified G157. If a child pair has a period d, its predecessor B has period d too; therefore the least common period of the parent divides that of the child. Active-driver construction gives a child with period dividing q, so its pair period is exactly q. At a zero driver the pair period is the least period of a. Odd integration gives child period exactly2q, as in G158. The period variable therefore remains exact throughout.

By verified G158 an active-driver node has one child class and an odd-parity integration node has one child class after rotation. Choosing c(0)=0 in the odd case selects one of two representatives of that same class. Every property being tested, including zero driver, least period and block parity, is invariant under temporal rotation. Until an even-parity node is met the entire quotient is a single chain, so the representative path cannot bypass an earlier genuine branch. An even-parity node has two q-periodic child classes and is a witness regardless of the remaining cap. Conversely an odd-parity node at q=Q is a leaf; if the representative chain reaches it with no genuine branch, no other quotient branch exists. Termination follows from G7's finite, nonrepeating rooted tree at cap Q. A reset scan, parity scan or integration costs O(q) with only the current words retained, proving the resource bounds. Square.

**Controls and identified unexpected check (no run).** Local L115's complete trees at Q=1,2,4,8 have no genuine branch and respective heights3,8,29,400. Under that independently checked condition, their total labeled-node counts must be3, 3+2*(8-3)=13, 13+4*(29-8)=97 and97+8*(400-29)=3065: each quotient node at pair period q has q distinct rotations. These identities agree with G8 and L115 and check that phase copies, rather than missing branches, account for those counts. This does not extend the observation to Q=16.

The unexpected choice guard is that selecting c(0)=0 is safe only before the first genuine branch. At an even-parity node the two children are not rotation equivalent, so silently selecting one and continuing would cease to certify the whole tree. The procedure stops and reports that node instead. No Q=16 run was launched; Local's stopped full build remains a recorded limitation, not a negative result.

**Scope.** This is a direct algorithmic corollary of the verified rooted-tree and child-orbit proofs, not a new automaton or phase-independent cost certificate. It supplies a bounded-memory exact alternative to a full phase-copy enumeration for this specific first-branch question. Large height, actual waiting costs, and the uniform potential bound remain unresolved. No literature novelty claim or prize result is asserted.

**G158-G161 temporal-difference reformulation (2026-10-07; independent application check requested).** For a nonzero periodic binary word a of least dyadic period q, let Delta=S+I over GF(2), and let nu(a) be the smallest positive m with Delta^m a=0. For q>1,

    q/2 < nu(a) <= q,
    Delta^(q-1) a = XOR_(t=0..q-1) a(t) (a constant word).

Indeed Delta^q=S^q+I=0. A period q/2 is equivalent to Delta^(q/2)a=0, which is excluded by minimality. Finally (S+I)^(q-1)=I+S+...+S^(q-1), since q is a power of two. Thus odd block parity is exactly nu(a)=q, and even block parity is exactly nu(a)<q. The q=1 nonzero word is constant1 with nu=1 and odd parity.

At a zero driver the next profile obeys Delta c=a. Therefore nu(c)=nu(a)+1: Delta^nu(a)c=Delta^(nu(a)-1)a is nonzero and its next difference is zero. Odd-parity integration raises order from q to q+1 and doubles the least period. Even-parity integration raises an order strictly below q by one while keeping period q, producing the genuine branch in G158. The first-genuine-branch search is therefore precisely a search for a rooted zero driver whose predecessor has a vanishing (q-1)st difference despite having least period q. Rooted absence of that event is unresolved beyond Local L115's finite controls.

**Symbolic controls and identified unexpected check.** In temporal order a=0110 has differences1010,1111,0000, hence nu=3 at q=4. Its integrated c=0010 has nu=4 and the same period4. By contrast a=01 has nu=2, while integration0011 has nu=3 and period4. Equal period does not fix difference order: confusing nu=3 with q=3 would incorrectly infer a non-dyadic period. The known roots at q<=2 cannot have an even-parity least-period word, consistent with the first controls. No derivative census or new run was made.

**Prior art and interpretation.** Read Nersissian section2.3, Theorems1 and4, on exact dyadic periods and Newton/companion order. This is a standard GF(2) finite-difference identity and a reformulation of G158, not a novelty claim. A q-periodic word has a unique Newton expansion on0..q-1 that repeats with period q; nu is one more than its highest nonzero Newton index. The genuine-branch condition is absence of the top index q-1, not absence of all high indices. The algebra uses binary XOR differences; it makes the owner's higher-temporal-difference question precise for these profiles without supplying physical units, a continuous derivative model or a waiting bound.

**FBR16 preregistration (2026-10-07, before Local’s new run).** Local L117 independently verifies G161 and offers the reduced test. Lane: Local on the owner-described M5 host runs the single representative path at cap Q=16; GPT retains symbolic reasoning and audit. Blind predictions: no even-parity zero-driver node and completion within100000 visited nodes. The smaller certified tree forces K(16)>400 if the run reaches its terminal classification; this is a control, not a blind prediction. No reliable point estimate of K(16) is claimed; report the exact value only if the cap leaf is certified. Counterfactual: a rooted even-parity node occurs before the cap leaf and supplies a genuine-branch witness. Limits: CPU120 seconds,128MiB working memory,100000 nodes; stop at the first exceeded limit and retain partial output, never call it a negative certificate. Do not start Q=32 in this block.

Controls: reproduce the already verified Q=1,2,4,8 heights3,8,29,400 and counts3,13,97,3065; independently check every retained transition by the literal bit equation S c=a XOR(b OR c), separately from the constructor. At any terminal node verify the parity and cap/branch classification directly. Identified unexpected check: at Q=16 repeat with the odd-integration choice c(0)=1; the terminal type and height must agree, and any same-depth pair must differ by a common temporal rotation. If either path exceeds the bounds, retain the failure and do not extrapolate. This verifies phase-choice invariance rather than silently assuming it. Data and transcripts remain outside Git; publish predictions before starting, then record resource use, stop reason and exact finite scope. Even a completed no-branch certificate decides only Q=16, not all periods, waiting costs or a prize problem.

**FBR16 existing-record correction (2026-10-07, before accepting new run evidence).** GPT missed G2.3 and G7.3 during preregistration. G2.3 already gives the reset/even-parity classification and certifies the first genuine split at diagonal53208: the zero driver is diagonal53207, so G161's detector reaches its first even-parity node after53208 visited nodes, at depth53207. The two period16 continuation cycles are certified disjoint. Thus the FBR16 no-branch prediction is refuted by the existing record; it is retained above as a failed prediction, not silently revised. A first-branch stop does not measure the maximum height K(16) of the full branched tree. G158 rederives G2.3's classification, and G161 gives its rooted-tree decision formulation; neither is evidence of a new first-branch discovery.

If Local has not started, no new run is needed. If already started, retain its result as an independent replay of G2.3 within the published bounds; do not extend to Q=32. The temporal-difference reformulation therefore applies to a known rooted even-parity event at least period16: its predecessor has8<nu<16 and integration raises nu by one without doubling. The global conjecture of no rooted genuine branches is closed negatively by G2.3, not open. The open issues remain costs and branch structure after the known split. This correction is made from the pre-existing finite certificate, not by fitting a new result.

**FBR16 independent certificate audit (GPT, 2026-10-07; Local L118 result at b73a763).** Local’s bounded run completed on the owner-described M5 host: CPU1.05s, peak RSS20.8MiB as reported in L118. It found the already-known G2.3 first branch, refuting FBR-P1; completion-under-cap held, and the cap-leaf height control was inapplicable. The independent audit is tests/probes/lexicon/rule30_fbr16_review.py, using explicit time-ordered lists and the scalar backward equation, with no import from Local’s constructor and no forward search. On GPT’s Intel host it passed in0.221 CPU seconds as printed by the first run.

From a=0000110001010011 and b=0, the audit reaches the root after exactly53207 backward steps and zero one step later. It independently checks the least pair period at every node, with histogram1:3,2:5,4:21,8:371,16:52808; every earlier zero driver has odd block parity. Both terminal integrations close, map back to the parent, have least period16 and fail all16 tests of rotation equivalence. Thus the finite first-branch certificate agrees with G2.3 rather than extending it. The phase-copy count through that terminal depth is3+10+84+2968+16*52808=847993 nodes; this is the ancestor prefix through the first genuine branch, not the whole branched tree or its maximum height.

The exact higher-difference order is nu(a)=14 and nu(c)=15 for both integrated children. A separate direct binomial-transform check gives highest Newton indices13 and14, respectively. Their common least period remains16. The identified unexpected one-bit mutation changes a(0), making block parity odd and order16; both period16 integrations then fail closure. This checks the closure detector independently and exhibits why period and difference order must be distinguished. No Q=32 run, deeper branch search or actual settling bound was performed. The failed no-branch prediction and missed existing record remain explicitly retained above.

### G162. Three post-split reset steps cost two adjacent run lengths (2026-10-07)

**Statement.** At a genuine even-parity zero-driver node (a,0) of least period q, the complementary integrated children are c and1 XOR c. Let r be the arrival phase and suppose the gate a(r-1)=1 holds. Then r starts a constant run of c. Let ell and m be the lengths of this run and the next one, respectively. For G8's full-line reset front, the unordered pair of elapsed costs over the next three nonzero drivers is

    {ell+2, ell+m+2}.

In particular the worst sibling cost is at most q+2. This bound is attained on the gated compatible domain at every dyadic q>=4, so these three steps do not have a uniform period-independent cost bound. Root reachability of the attaining family is not asserted.

**Proof.** Since Delta c=a is nonzero, c is nonconstant. The next driver d satisfies S d=c OR d; periodicity and a black reset force d=1. The following driver e satisfies S e=1 XOR c, hence e(t)=1 XOR c(t-1). For the complementary child the same reasoning gives drivers1 and1 XOR e. These are exactly the next three drivers on each continuation.

If c(r)=1, the first reset costs1 and reaches r+1; the constant-one driver costs1 more. The first one of e at or after r+2 is at r+ell+1, including the ell=1 endpoint. Its reset therefore finishes at r+ell+2. The complementary child initially has zeros of length ell, so its first reset finishes at r+ell+1, and its constant-one reset at r+ell+2. Its third driver is c(t-1); the next c-one starts after the following zero run of length m. That reset finishes at r+ell+m+2. When c(r)=0 interchange the two children. Subtract the initial r to obtain the formula. Adjacent runs occupy at most one period, so ell+m<=q.

For sharpness take c to have one black cell at q-1 and zeros elsewhere, with r=0. Then ell=q-1 and m=1. Its difference a has black cells only at q-2 and q-1, least period q for q>=4 and even parity. The parent gate holds because a(q-1)=1. Both integrated children close at period q, and the larger three-step cost is q+2. This is an ambient compatible witness, not a rooted one. Square.

**Known rooted control, not a new search.** Local L118 and GPT's backward audit give a=0000110001010011. Choosing c(0)=0 integrates to c=0000010000110001. G160's gate allows phases0,5,6,10,12,15. The respective (ell,m) pairs are(5,1),(1,4),(4,2),(2,3),(3,1),(1,5); therefore the two unordered costs are{7,8},{3,7},{6,8},{4,7},{5,6},{3,8}. The maximum is8. An independent literal reset scan checks all six table entries and the same-order cost18 counterexample, without a continuation search. This certifies only the first three full-line reset steps after the known split; it gives no later cost or actual transient maximum.

**Difference-order guard.** At dyadic q>=8, put a single pulse g at q-1 and take c=Delta g, a=Delta^2 g, r=0. Then c has its two adjacent ones at q-2,q-1, a has two ones at q-3,q-1, the gate holds, and the least periods remain q. Since nu(g)=q, their orders are nu(a)=q-2 and nu(c)=q-1. The cost maximum is again q+2. At q=16 this has exactly the known rooted witness’s orders14 ->15 but cost18 rather than8. It is not asserted rooted. Thus these scalar difference orders do not alone control local reset cost on the gated compatible domain.

**Identified unexpected check and scope.** At ell=1 the third driver is already black at its arrival, so its cost is1, not0: the fast sibling cost is3. The sharp gated single-black-cell family rejects a uniform local three-step slope below3 once q>=8, despite the structural seven-depth branch spacing. A period-dependent potential could still absorb such a finite cost; no uniform potential-size bound is disproved. Existing G2.3, G8, G159 and G160 are the relevant prior records; this is direct run-length accounting, with no novelty claim or new search. Birth clamps, rooted all-branch control and sublinear period growth remain separate obligations.

### G162 addendum: uniform gate averages do not supply adaptive charging

**Bounded symbolic audit, not a new experiment.** Write the cyclic run lengths of c as L_1,...,L_R. The gate Delta c(r-1)=1 selects exactly the R run starts. At run i the slower sibling costs L_i+L_(i+1)+2; summing cyclically gives mean 2q/R+2. Averaging both siblings instead gives 3q/(2R)+2, since their combined cost is 2L_i+L_(i+1)+4. These are exact averages under uniform gate-start sampling, not an invariant measure for the adaptive front.

For the known rooted control, R=6 and q=16. The slower-sibling table sums to44, giving mean22/3 over three steps, below the slope-5/2 allowance15/2. Its maximum8 exceeds that allowance. The twelve sibling costs sum to72, giving mean6. This explains why averaging the table can look encouraging while leaving the worst permitted arrival uncharged. G8 requires a pointwise inequality with endpoint potential differences, or another proved measure/trajectory relation; neither uniform averaging nor choosing the cheaper sibling supplies it. No claim is made that the actual rooted arrival realizes every gated phase.

**Identified unexpected domain check.** An alternating c would make R=q and the formula look especially favorable, but Delta c=1 has parent period1 and odd parity. It is not a genuine even-parity split of parent least period q; exclude it from that domain. The single-pulse c at q=4 has parent least period4 and is a valid control: its two gated starts both have slower cost6, and its four sibling costs average5. The same-order period16 counterexample in G162 has R=2 and slower mean18, so gate averaging also fails to repair the scalar-order shortcut on the ambient domain.

**Outcome.** The proposed uniform-phase charging shortcut is withheld: its missing hypothesis is a proved relation between adaptive visits and run-start sampling, or a pointwise phase-sensitive potential. These identities do not establish a new waiting bound, root restriction or prize result. Next reasoning remains charging selected agreement intervals as in G7.2, with G8's phase retained; no larger census or colleague computation is requested.

### G163. One winding rate controls repeated-strip block debt (2026-10-07)

**Statement and domain.** Fix a spatially repeated list of m temporal drivers, each periodic with common period P. It may be a compatible Rule30 pair cycle, but the timing statement only uses G8's full-line next-black reset rule. Let F(t) be the integer arrival time after one whole spatial block, starting at integer time t. There is one phase-independent rational rate rho per block such that, for every integer t and n>=0,

    abs(F^n(t)-t-n*rho) <= P-1.

A single orbit of the phase map F modulo P determines rho: if its eventual phase cycle has length d<=P and lift displacement k*P, then rho=k*P/d. All phase cycles have this same rate, even if they do not merge. The per-driver asymptotic slope is rho/m.

At block boundaries, a nonnegative P-periodic integer potential H with

    H(t) >= 2*(F(t)-t)-5*m+H(F(t))

exists if and only if rho<=5*m/2. Whenever it exists, one can choose max H<=2*(P-1), independent of m. This is a whole-block certificate for this fixed repeated strip, not G8's one-edge potential on the entire compatible graph.

**Proof.** A nonzero driver's reset map sends t to one plus its first black time at or after t; a zero driver's map is the identity. Both are nondecreasing and commute with translation by P. Their composition F has both properties. Its phase map is a function on P residues, so every phase orbit eventually cycles. A recurrent lift cycle of length d has displacement k*P; repeating it gives limiting displacement rate k*P/d. If t<=u<=t+P, monotonicity and translation give F^n(t)<=F^n(u)<=F^n(t)+P. Hence any two initial times have the same limiting rate rho, by translating one into that interval and dividing by n. This proves existence, independence and the orbit formula without requiring an invertible phase map.

Fix n>=1 and let D_n(t)=F^n(t)-t. This is P-periodic. For residues t,u with 1<=u-t<=P-1, the previous inequality gives -(u-t)<=D_n(u)-D_n(t)<=P-(u-t). Thus its largest and smallest residue values differ by at most P-1. Write these values M_n and a_n. Iterating F^n in blocks shows j*a_n<=F^(j*n)(t)-t<=j*M_n. Divide by j and let j grow to obtain a_n<=n*rho<=M_n. Every D_n(t) lies in that same interval, giving the claimed P-1 error. The n=0 case is exact.

When rho<=5*m/2, define H(t) as the supremum, over n>=0, of 2*D_n(t)-5*m*n. The n=0 term is0; the error bound makes every term at most2*(P-1). Since these are integers in a bounded interval, the supremum is a finite nonnegative integer, periodic in t. Splitting off the first block gives the potential inequality. Conversely, sum such an inequality over n blocks. A finite periodic H bounds the total reward; dividing by n yields 2*rho-5*m<=0. Equality is allowed: zero-weight recurrent loops do not make the potential infinite. Square.

**Independent existing control.** G8's compatible period4, spatial-length12 witness has F(0)=27 and F(3)=31. Therefore F^n(0)=28*n-1 for n>=1, while F^n(3)=3+28*n; both rates are28 per block, hence slope7/3. The phase-zero first-block slope27/12 is not its asymptotic rate. Its whole-block error from phase0 is1, within P-1=3. No new cycle search was run.

**Identified unexpected check: coalescence is not required.** The all-zero compatible strip gives F(t)=t. Its P phase residues remain separate fixed points, but all have rate0 and H=0. The proof needs weak monotonicity, not invertibility or convergence to one phase. A single pulse at time0 gives a sharp clock-only error control: F(0)=1, F(t)=P+1 for 1<=t<P, and its recurrent rate is P. The error at t=0 is P-1. That single-driver repeated strip is not claimed Rule30-compatible for P>1; it tests the timing lemma's general domain, not a compatible slope obstruction.

**Prior record and limits.** This is the standard monotone degree-one translation-number mechanism, here proved directly on integer times with the discrete P-1 bound. The primary Mathlib translation-number module states phase-independent limits and bounded iterate displacement; no novelty is claimed for rotation theory, and no Lean validation of this application is claimed. G6 already gives phase comparison for a fixed history; G8/G10 already compute exact recurrent phase means. This entry supplies the explicit whole-block potential consequence. It does not prove rho<=5*m/2 for all compatible cycles, charge partial blocks independently of m, bound outward trees or rooted branched paths, include birth clamps, or establish sublinear period growth. Those remain separate obligations before any prize conclusion.

### G163 addendum: zero block debt can hide unbounded partial debt

**Counterexample to a generic return-map shortcut, not to Rule30.** Fix temporal period P=4. For any positive L divisible by4, repeat a spatial block of L pulse drivers w=1000 (time order, one at residue0), followed by L all-black drivers. Its spatial block length is m=2L. The lift of its full-block clock map, evaluated at residues0,1,2,3, is

    F(0)=5L-3; F(1)=F(2)=F(3)=5L+1.

Translation by4 gives every other value. All outputs have residue1. At residue1 the displacement is5L, so the rate is rho=5L, and rho/m=5/2. The four block displacements are5L-3,5L,5L-1,5L-2. Thus every whole-block doubled reward 2*(F(t)-t)-5m is nonpositive: H=0 already certifies the entire return map.

Nevertheless, starting at phase1, each of the first L pulse resets costs4. That partial interval has elapsed4L across L drivers, with doubled slope-5/2 debt3L. Any nonnegative one-driver potential on the clock schedule must consequently have maximum at least3L, by telescoping those L inequalities. This grows without bound while P stays4. The favorable block rate and even zero block potential do not bound the interior interval debt independently of the spatial block length.

**Independent hand control and unexpected compatibility check.** For L=4, phase1 follows pulse arrivals1,5,9,13,17, then black arrivals18,19,20,21. The block costs20 across8 drivers, but its pulse half costs16 across4, with doubled debt12. From phase0 the block ends17, agreeing with the separate formula5L-3. The schedule is inadmissible as a Rule30 repeated strip: an interior pulse triple w,w,w would require S w=w XOR(w OR w)=0, but (S w)(3)=1. This precise compatibility failure is retained; the example supplies no compatible-cycle obstruction, rooted counterexample or failed prize conjecture.

**What the audit closes.** G9 already rejected an endpoint-only birth-transfer shortcut with a finite clock toy. This different control has indefinitely repeated blocks, an acceptable phase-independent recurrent rate and a zero block potential, yet arbitrary interior debt at a fixed P. It withholds inferring G8's uniform one-edge potential from G163's block potential by timing monotonicity alone. A useful continuation must charge the selected agreement intervals using the actual diagonal equation, or prove a separate compatible partial-block/tree bound. No computation was run, and Local's G163 review remains independent of this clock-only addendum.

### G164. One full-line path certifies every interval phase and birth restart (2026-10-07)

**Statement.** Fix a finite list of M temporal drivers with one common period P. Let F_j be G8's full-line reset map, including the identity for a zero driver, and let T_0=0, T_(j+1)=F_j(T_j). For gamma>=1 define the reference path's all-interval debt

    D = max over 0<=a<=b<=M of [T_b-T_a-gamma*(b-a)].

Then for every such interval and every integer starting time u,

    G_(a,b)(u)-u <= gamma*(b-a)+D+P-1,

where G_(a,b)=F_(b-1) composed through F_a. Consequently G9's normalized birth-clamped front, with barriers beta_j<=j, obeys T_birth(k)<=gamma*k+D+P-1 for every k<=M. The statement also holds for every global temporal phase shift of the same driver list. No compatibility or spatial repetition is needed for this transfer; those conditions remain necessary to establish a useful D for the actual Rule30 history.

**Proof.** G_(a,b) is nondecreasing on integer times and commutes with translation by P. Its displacement Q(u)=G_(a,b)(u)-u is P-periodic. For residues u<v with 1<=v-u<=P-1, monotonicity and periodicity give

    -(v-u) <= Q(v)-Q(u) <= P-(v-u).

Hence the spread of Q over every starting residue is at most P-1. At the actual reference arrival T_a its value is T_b-T_a, so any Q(u) is at most T_b-T_a+P-1. The definition of D proves the interval inequality. Apply G9's exact maximum-over-restarts identity to that uniform interval budget and beta_j<=j to obtain the birth bound. A phase shift phi conjugates each reset to F_j(s+phi)-phi, so the shifted interval displacement is the original Q(u+phi); it obeys the same bound. Square.

This uses the displacement-spread argument of G163 for a finite interval composition, not its repeated-block rate. The reference debt must cover all intervals, not just the whole prefix. Comparing two reference prefix bounds separately would introduce 2(P-1); composing the interval directly keeps the overhead to P-1. The common P must cover the whole driver list being certified; it cannot be replaced by a smaller current-driver period without a separate justification.

**Existing finite evidence, not a new run.** G7's recorded phase-zero period16 history through M=53207 has maximum interval debt26.5 at slope5/2. Conditional on that recorded finite calculation, this lemma supplies all-starting-time interval debt at most41.5 on the same history. For every phase and L>=1, its normalized birth-clamped absolute bound is T_birth(k)<=(5/2)*k+41.5 for k<=53207. G9 also gives birth-clamped interval debt at most42.5 for L=1, or41.5+L in general. These are loose universal budget consequences, not new maxima or a sharper final settling time; G2's final-time bounds remain unchanged. The computation is not rerun or newly independently verified here. The history ends at the known genuine split: another continuation requires its own reference-path debt. No all-branch or asymptotic conclusion follows.

**Identified unexpected sharpness/domain control.** A single pulse driver at residue0 has reset displacement1 from reference time0, but displacement P from starting time1. Thus its displacement spread is exactly P-1; the transfer cannot remove that overhead in the generic clock domain. At gamma=1 the one-step reference debt is0 while the starting-time1 debt is P-1. This is not claimed a repeated compatible Rule30 strip. At P=1 the overhead vanishes, including the zero-driver identity. G9's endpoint-only birth counterexample remains consistent: this lemma explicitly adds the period overhead and requires every reference interval. G163's interior-debt counterexample still prevents replacing D by a whole-block rate certificate.

**Scope and remaining obligation.** Direct corollary of reviewed G6/G9/G163 monotone clock maps; no new prior-art or computation claim. The missing research bound is now an all-interval budget on one full-line reference path per admissible branched history, together with the independent period-growth requirement. An arbitrary-period D=O(P) bound is not supplied. Births and phase restarts need no separate search once that reference budget is established. No prize result is claimed.

### G165. Dyadic stage budgets stitch without a logarithmic loss (2026-10-07)

**Conditional reduction.** Follow one infinite admissible rooted diagonal history. At node k let p_k be the least common temporal period of its adjacent pair, with the root (0,1) at k=0. Use gamma with 1<=gamma<3. Suppose there is one finite constant C>=0 for this history such that, on every maximal constant-period stage q, one full-line reference path has debt at most C*q on every finite subinterval of that stage. Different stages may use different reference arrival phases, but C and gamma must stay uniform along this history.

Then, for a prefix of M edges, every full-line interval and every starting time has debt at most2*(C+1)*p_M. The same bound transfers to normalized birth-clamped absolute timing:

    T_birth(M) <= gamma*M+2*(C+1)*p_M.

It also covers every global temporal phase of this same history. Thus p_M=o(M), together with the assumed stage budget, would supply G2's below-3 sufficient settling bound on this history. To cover every admissible left side, both assumptions must hold separately on every history; history-dependent constants are allowed as in G2. No stage budget or period-growth estimate is proved here.

**Exact stage structure.** The predecessor B commutes with temporal shifts. If a child pair has period q', its predecessor has a period dividing q'. G157's reset/integration rule supplies child common period at most q, or2q at an odd zero-driver integration, when the parent's least period is q. Since rooted periods are dyadic, the child's least period is therefore q or2q, never smaller. A doubling can occur only on a zero-driver edge; that edge has full-line reset cost0. Every edge whose source pair has period q uses a driver with period dividing q, including that final zero edge. Consequently all clock maps within a stage share common period q. Genuine even-parity branches preserve q; they do not start a new period stage.

**Proof of the budget.** Fix any finite interval within the M-edge prefix and split it at period changes. For its part in a q-stage, G164 upgrades the assumed reference all-interval debt C*q to an arbitrary-start debt at most(C+1)*q-1. Each stage is contiguous, so the interval visits each q at most once. The distinct q are powers of2 bounded by p_M. Their sum is at most2*p_M-1. Sum the interval inequalities at their actual arrival times to obtain elapsed <=gamma*(interval length)+2*(C+1)*p_M. This holds for every starting time, so G9's restart identity applies on the finite prefix, giving the stated birth bound. Phase conjugacy preserves the same inequalities. No separate phase sum, per-birth penalty or per-branch allowance occurs. Square.

**Equivalent period-growth checkpoint.** Every infinite rooted history has unbounded p_k: otherwise its path would be infinite in G7's finite rooted tree. Let N_j be the first node of least period2^j, for j>=1. The exact stage structure gives p_k=2^j for N_j<=k<N_(j+1). Hence p_k=o(k) if and only if2^j/N_j tends to0. Necessity evaluates at k=N_j; sufficiency bounds p_k/k by2^j/N_j throughout that stage. This is a reformulation, not an estimate for N_j. A large finite doubling delay does not prove the limiting condition.

**Identified unexpected check: branching is not doubling.** The known split at diagonal53208 has period16 children, as G2.3, G158 and the independent FBR16 replay establish. It is not the first period32 node N_5 and earns no new stage allowance. The known initial stage entries3,8,29,400 do not locate N_5. Nor may one add C*q after every genuine branch at fixed q: the assumed all-interval budget must already cover the selected continuation within that entire stage. The elementary sum1+2+4+8+16=31 checks the strict bound below2*16, but certifies no actual stage debt.

**Scope.** Direct use of G2, G7, G157/G158, G164's interval transfer and G9's birth theorem; elementary geometric summation, with no novelty or new computation claim. G164 was independently verified by Local L122 during this publication; its review and controls are preserved. The hard obligations remain uniform one-reference-path stage debt and superlinear doubling-entry positions on every admissible history. Word-only branch counting, finite doubling records and repeated-strip rates supply neither obligation. No prize conclusion is asserted.

### G166. HG4: four-period-horizon potential check (HG-P1 REFUTED, 2026-10-07)

**Concrete family.** On the common-period-q clock-aligned compatible graph, restrict to G160's closed arrival gate and include the zero state. An edge has doubled slope-5/2 reward w=2*delta-5. Set H_0(v)=0 and recursively

    H_(n+1)(v)=max(0, max over v->u of [w(v,u)+H_n(u)]).

For a vertex with no successor the inner maximum contributes nothing. H_n is the largest reward of a path of at most n edges; stopping early is allowed. The candidate is H_(4q). Exact equality H_(4q+1)=H_(4q) certifies the one-edge inequalities on the entire selected finite domain. This is a named finite-horizon potential family, not a new graph enumeration method. G8/G10's existing Bellman certificate machinery is the internal prior record. The proposed horizon4q is heuristic, not implied by G163-G165 or by the length39 of G10's period10 maximizing witness.

**Published predictions, before any HG4 run.** HG-P1 (blind): H_(4q+1)=H_(4q) for every q in1,2,4,8. HG-U (identified unexpected check, separate blind prediction): stability also holds at q=6, despite G10's zero-weight slope-5/2 cycle. A q=6 failure does not refute the dyadic-only prediction. HG-C1: independent forward bit equations and scalar reset scans agree with every tested edge for q<=4, including gate closure. HG-C2 (existing-record control, not blind): H_n never exceeds G10's known least potential restricted to gated states; full-domain maxima0,0,6,45 at q1,2,4,8 and21 at q6 bound it. Thus the finite maximum <=10q is already controlled by existing certificates, not a newly predicted scaling law. Report the exact gated maximum and comparisons anyway. HG-CF: H_0 is not feasible at q4; the aligned gated edge(8,8)->(8,0) has delta4 and reward3. It must be rejected.

**Requested Local work and limits.** After the pending G165 symbolic review, Local may claim HG4 in CLOUD-LOCAL.md and run it once, reusing rule30_gpt_cycle_obstructions.py's existing aligned graph/certificate arithmetic. No new spatial-cycle census, seed search, q10 extension, q16 job or hardware comparison. Scope is exactly q1,2,4,6,8; hard cap120 CPU seconds and256 MiB RSS, one process. If the existing graph arrays are available, reuse them; otherwise construct only these already certified finite domains. Publish the claim before execution and retain the script/outcome. Large arrays and data remain outside Git. Partial stops are limitations, not passes. GPT will independently audit any failing witness or resulting certificate using scalar equations; Local's existing long computations remain separate.

**Failure reporting and independent check.** For each q record the first stable horizon if it occurs by4q, the exact H_(4q) maximum, and whether the4q+1 edge inequality passes at every gated vertex. If HG-P1 or HG-U fails, retain an explicit violating edge and its positive deficit; recover a maximizing at-most4q+1-edge reward path and verify it by literal time-bit scans independently of the DP values. Instrument/control failure halts interpretation. A broad gated-domain witness is not automatically rooted, and a successful finite test does not establish stability or a linear potential bound at larger periods. If Local is busy, queue rather than duplicate the job.

**What this would decide.** A failed horizon supplies a precise compatibility-respecting obstruction to this proposed local family, replacing generic clock toys. A pass supplies only a finite-domain certificate and a candidate horizon for later proof, not the missing arbitrary-period stage budget of G165. No run or outcome is claimed in this preregistration.

**HG4 independent-audit preparation (2026-10-07; before any outcome was read).** Local claimed the preregistered run at1f4958a. No result is received here. If an edge violates H_N(u)>=w+H_N(v), where N=4q, prepend that edge to a maximizing at-most-N-edge path from v. The resulting path exceeds H_N(u), so it must have exactly N+1 edges: any shorter valid path contradicts the claimed H_N rather than the horizon prediction. It also cannot repeat a clock-aligned state. G10's existing finite certificates make every cycle nonpositive in these tested domains; removing a repeated-state cycle would preserve or increase the reward while shortening the path to at most N, again contradicting H_N(u). Raw pairs at different relative clock phases may repeat, so this check uses G9's aligned states, not a word-only quotient. These are derived instrument checks, not changes to HG-P1/HG-U or a claimed run. GPT will audit a published witness with literal bit equations and reset scans; it will not launch a duplicate HG4 computation.

**HG4 stage-boundary model audit (2026-10-07; no computation).** The common-period-q graph omits a period-doubling child, so its odd zero-driver source is a cap leaf. This does not omit a positive charge from a real q-stage. The actual exit driver is0, hence delta=0 and doubled reward=-5; give the terminal outside-q child stage-potential0. Any nonnegative H at the source satisfies that terminal inequality. All other edges within the stage stay in the common-q graph, and G160 keeps their arrivals gated. The new stage also enters the gate: at the exit (a,0)->(0,c), Delta c=a, so the new gate Delta c(r-1)=1 is exactly the old gate a(r-1)=1, with the same clock r. The initial root exception costs1 and enters the gate after one edge, with negative doubled reward-3.

Consequently a gated certificate with maximum B(q) bounds every actual full-line interval confined to that q-stage by B(q)/2; even-parity branches need all their compatible inequalities, not a new allowance. If the HG4 family were feasible with B(q)<=10q at every dyadic q, telescoping these stage bounds and G165's geometric sum would give reference-path interval debt below10*p_M. G164 then adds p_M-1 to cover arbitrary interval starting times, so G9 supplies normalized birth-clamped absolute debt below11*p_M. These are conditional all-period bounds, not established by the finite HG4 run. Sublinear period growth remains separate.

The initially proposed direct birth transfer of the10*p_M budget is withheld: G9 requires arbitrary restart times, whereas a gated certificate covers actual gated arrivals. Birth barriers can change those arrivals. Within actual full-line stages no extra phase overhead is needed; to include arbitrary restarts, retain G164's single-prefix overhead. This is the identified quantifier check, alongside the terminal-zero control. It changes neither predictions nor run scope.


**HG4 outcome and independent targeted audit (2026-10-07).** Local L124 published the run at3b8bd2a, following claim1f4958a and preregistration5f329d3. HG-P1 is refuted at q8; q1,2,4 pass. The separate unexpected prediction HG-U holds at q6, stable from horizon21. Local reports all controls passing,80 violating edges at q8, and first stabilization at85 when continuing the same finite graph recursion. Horizon85 is descriptive beyond the prediction; it does not justify choosing a new universal horizon by fitting this result. Local's first run lacked its required witness report; the report was added and the job rerun with the same verdicts. Local's cost was0.49 CPU seconds and55.7 MiB on the M5 host.

GPT's independent script `tests/probes/lexicon/rule30_hg4_review.py` uses scalar child integration with period closure and an absolute phase, with no Local graph or DP imports. It computes only the failing source's horizon32/33 descendants (67 memo states), rather than repeating the global experiment. Known expectations9/17/33/91, a negative H0 control and the aligned-repeat check were written before execution; these are audit controls, not blind predictions. It confirms H32(143,8)=9 and H33(143,8)=17. The recovered33-edge path has elapsed91 and reward2*91-5*33=17. Every triple equation, arrival gate, reset delay and period closure passes. The identified unexpected check also passes: all34 clock-aligned states are distinct. The q4 pulse edge rejects H0 as expected. GPT's corrected scalar audit takes0.0123 CPU seconds and10.5 MiB on the Intel host; an initial ancestry check encoded the constant-one root as integer1 instead of255, was corrected, and rerun with the same non-rooted verdict.

The recovered time-bit integer words are:

    143,8,5,14,245,243,4,93,247,85,69,96,70,60,116,151,71,224,69,63,116,149,71,228,69,71,4,133,7,5,4,6,4,4,0

**Rooted scope check.** Literal predecessor iteration from(143,8) repeats after4746 steps at(139,0), without reaching the period8 constant-one root(0,255). Thus this witness refutes the proposed full gated-domain horizon; it is not a rooted-history debt obstruction. Rotation does not repair rootedness because the root is shift invariant and predecessor iteration commutes with shifts. The scalar audit independently establishes the reported source values and a valid maximizing witness. It does not independently verify the global count80 or stabilization85. Existing G10 finite bounds survive; the all-period budget and period-growth obligations of G165 remain open.

**Next intention.** Close the specific4q horizon route. Seek a compatibility-based bound on reward or maximizing-path structure rather than fitting a larger horizon. Before any further computation, coordinate a distinct claim and prediction; no larger-period run is requested here.


**Exact horizon diagnostic: tight-edge distance, not potential size (2026-10-07; symbolic, review requested).** Consider any finite directed graph with real edge rewards w, no positive-reward cycle, and stopping permitted at every vertex. Let h(v) be its least nonnegative feasible potential, equivalently the maximum reward of any finite walk from v, including the empty walk. G8 already proves finiteness by deleting nonpositive cycles. For an edge v->u set its slack s(v,u)=h(v)-w(v,u)-h(u)>=0. For any at-most-n-edge walk p ending at z, telescoping gives

    h(v)-reward(p)=h(z)+sum of the edge slacks on p.

Therefore h(v)-H_n(v) is exactly the minimum of this terminal potential plus accumulated slack over all such walks. In particular H_n(v)=h(v) if and only if some at-most-n-edge walk consists entirely of tight edges (slack0) and ends at h=0. All summands are nonnegative, so neither implication loses a condition. This also covers h(v)=0 by the empty walk and vertices with no successors.

Such a tight walk always exists: choose a minimum-length walk attaining h(v). An optimum exists among simple paths by cycle deletion. Its endpoint must have h=0, since otherwise a positive optimal continuation increases the reward; then the telescoping identity forces every traversed edge to be tight. Let d(v) be the shortest tight-edge distance to the zero-potential set. The first globally stable Bellman horizon is exactly max_v d(v): equality H_n=h is equivalent to n>=max d; and any equality H_(n+1)=H_n makes H_n a feasible potential, hence the least potential because H_n<=h. The shortest tight path is simple, so d(v)<=|V|-1. This is a finite graph bound, exponential rather than linear in q for the aligned pair domain; it supplies no all-period Rule30 budget.

**Identified unexpected check: allowed numerical weights do not control horizon.** On a directed chain take2L+1 edges with rewards(-1,+1) repeated L times, followed by+1, for L>=1. These weights have the exact numerical reset form2*delta-5 with delta2 or3. Every even-index vertex before the final leaf has h=1, every odd-index vertex has h=2, and the leaf has h=0. Every edge is tight. Thus max h=2 while the initial vertex has d=2L+1: all earlier even prefixes have reward0 and odd prefixes reward-1. No positive cycle exists. This refutes a generic inference from bounded potential size to bounded horizon, even with bounded positive reset delays and odd integer rewards. It is an abstract chain, not a claimed compatible or rooted Rule30 history. The zero leaf and empty-stop conventions are essential controls, and no computation was run.

**Application and next question.** HG4 failure concerns the tight-route length in the full gated graph. It does not by itself refute a potential magnitude O(q). Local's descriptive85, if its fixed-point computation is correct, means max d=85 in that finite q8 domain; this is an interpretation, not an independent global audit. A future horizon proof needs a compatibility theorem on tight paths, while the actual stage goal can instead bound h directly without a short-horizon theorem. This isolates two obligations that should not be conflated. No new universal bound, rooted counterexample or prize result follows. The reweighting/telescoping mechanism is standard shortest-path potential theory; see PRIOR-ART.md, not a novelty claim.


**Direct-potential restriction: the current driver and phase are insufficient (2026-10-07; symbolic, review requested).** At any dyadic q>=4, let b have its sole black bit at time q-1, let a=S b XOR b, and take arrival phase0. Then c=b is a valid child of(a,b), because S b=a XOR(b OR b). Both source(a,b,0) and target(b,b,0) satisfy G160's gate: a(q-1)=1 and b(q-1)=1. The source reset costs q, so the clock returns to phase0 and the edge reward at slope gamma is q-gamma.

Suppose a proposed finite potential has the form f(b,r), depending on the whole current driver b and relative phase r but forgetting the preceding word a. Its edge inequality here becomes

    f(b,0) >= q-gamma+f(b,0).

This is impossible when gamma<q. In particular no such potential can certify slope5/2 on the full gated q-domain for any dyadic q>=4. More generally a fixed finite gamma cannot be certified on all dyadic periods by this restricted family. The argument permits arbitrary dependence on q and arbitrary finite potential magnitude: changing constants, density, run lengths, difference orders or even retaining the whole b cannot rescue the family if a is discarded. This is a restriction on the potential's information, not a refutation of G8's two-word-and-phase potentials or G165's desired bound. Root reachability of these sources is not asserted.

**Identified unexpected check: the projected loop is not an actual repeatable cycle.** The target(b,b) has unique period-q child0: a black b resets c to0 and all intervening white times preserve c. Thus the actual next target is(b,0), not another copy of(b,b). The second reset also costs q, and the next zero-driver reset costs0. Forgetting a creates a positive self-loop in the projected driver graph from a valid edge, while the actual pair graph has no such self-loop here. Repeating that projected loop is invalid. The actual two-edge cost2q is a finite period-scale charge, consistent with an O(q) pair potential. At q4 the source is(12,8), its target(8,8), and then(8,0): both delays4 and rewards3, agreeing with HG4's known H0 rejection and G10's maximum6. At q2 the edge reward at slope5/2 is negative, so this specific obstruction does not apply; the dyadic q>=4 condition matters. No numerical run or new cycle census was used.

**Prior record and next intention.** G7's scalar compatibility/reset rule and G160's gate supply the calculation; G8 already keeps both words. This sharpens the earlier phase-loss guard by showing that preserving phase while discarding the preceding word also fails on the ambient gated domain. It is elementary state-projection reasoning, with no novelty claim. Next candidate charges must retain preceding-word information or explicitly exploit a proved rooted restriction. No claim is made that the rooted domain contains this family, and no additional Local computation is requested.


**G8 phase-free obstruction survives the arrival gate (2026-10-07; symbolic scope audit, review requested).** G8.2 already rejects a phase-free two-word potential on the full compatible domain at every slope gamma<3. It is not a new cycle discovery. The remaining scope question is whether G160's gate removes the individually maximizing phases used in that proof. It does not. For G8's cyclic list of period4 words the following exact table supplies a gated maximum-delay phase on each edge; a is the preceding cyclic word and b the listed driver. Time bits are least-significant first.

| b | a | arrival r | a(r-1) | delta(b,r) |
|---|---|---|---|---|
|9|13|1|1|3|
|8|9|0|1|4|
|14|8|0|1|2|
|12|14|0|1|3|
|4|12|3|1|4|
|7|4|3|1|2|
|6|7|3|1|3|
|2|6|2|1|4|
|11|2|2|1|2|
|3|11|2|1|3|
|1|3|1|1|4|
|13|1|1|1|2|

Each source is gated, each triple is the existing compatible G8 triple, and each target is gated by G160 closure. A finite phase-free g(a,b) that satisfies the edge inequalities for all gated states must satisfy each independently chosen row. Summing cancels the cyclic pair potentials and gives36<=12*gamma. Hence gamma>=3 remains necessary even on the gated domain, at dyadic q4. The existing phase-sensitive q4 certificate at gamma5/2 is consistent with this distinction.

**Identified unexpected check and counterfactual.** The selected phases need not concatenate into one physical front. Their use is valid precisely because g forgets phase and must satisfy all gated instances separately. Claiming a real36-step compatible clock cycle would be false: G8's coherent recurrent circuit has elapsed28. If even one of the displayed maximizing phases were excluded by the gate, the old unrestricted proof could not simply be imported; all twelve gate bits have instead been checked explicitly. No new computation was run. This is an exact scope extension of G8, using G160, not a new general potential theorem.

**Working restriction after the two projection guards.** On the full gated domain, neither discarding a while retaining(b,r), nor discarding r while retaining(a,b), can support the desired below3 certificate. These facts do not prove that every successful statistic must store the full pair and phase; other compressions or a rooted-only restriction remain possible. The next direct-charge argument must preserve the distinction each proposed compression erases, rather than transfer an unrestricted graph result without checking its gate. No rooted debt lower bound or prize conclusion is claimed.


### G167. Four-edge branch blocks pay their endpoint but not every partial interval (2026-10-07)

**Bounded symbolic result, independent review requested.** Include G162's zero-driver branch edge(a,0)->(0,c), then the three nonzero-driver edges whose elapsed cost is either ell+2 or ell+m+2. Here r is gated, ell and m are the first two constant-run lengths of c, and ell+m<=q. The zero-driver edge costs0. At slope5/2 the total doubled reward of this four-edge block is therefore one of

    2*ell-16, 2*(ell+m)-16.

The worst endpoint reward is at most2q-16. Thus every such block at dyadic q<=8 has nonpositive endpoint reward. This is an ambient gated statement, not a rootedness assertion. At larger periods the upper bound can be positive. G162's pulse attaining family makes the larger reward2q-16 sharp. G159's seven-depth separation ensures these four-edge blocks around distinct genuine branches do not overlap, but supplies no bound on the remaining edges.

**Exact partial-prefix audit.** On the fast sibling c(r)=1, the four reset delays are0,1,1,ell. Its prefix doubled rewards, after0 through4 edges, are

    0, -5, -8, -11, 2*ell-16.

On the slow sibling c(r)=0, the delays are0,ell+1,1,m. The rewards are

    0, -5, 2*ell-8, 2*ell-11, 2*(ell+m)-16.

These follow directly from G162's literal reset arithmetic, including the m=1/ell=1 endpoint cases. Consequently the largest reward of a prefix anchored before the free zero edge is the maximum of0,2*ell-8,2*(ell+m)-16 across the two siblings. It is at most max(0,2q-10), since a nonconstant c has ell<=q-1. This says nothing about an interval that begins after the free edge.

**Known rooted control, not a new run.** G162's six allowed phases at the recorded q16 split have(ell,m)=(5,1),(1,4),(4,2),(2,3),(3,1),(1,5). Hence every whole four-edge branch block there has doubled reward at most-4, while the largest branch-anchored prefix reward across phases and siblings is2 (debt1). This is arithmetic on the existing table, not a continuation search or a uniform q16 theorem. No actual birth-clamped settling estimate is imported.

**Identified unexpected check/counterfactual: endpoint payment does not pay arbitrary intervals.** At q8 choose the valid G162 gated pulse family with ell=7,m=1. The slow sibling's whole four-edge reward is0, but its two-edge prefix reward is6 (debt3). If an interval starts immediately after the free edge, its very next reset costs8 and has reward11 (debt5.5). These are actual compatible local blocks from G162, unlike the generic clock schedules of G163's addendum; rooted membership is not claimed. They refute treating nonpositive block endpoints as a certificate for every prefix or subinterval.

**What moves and what remains.** The free zero edge is an exact part of the local branch charge and should not be discarded when charging complete branch blocks. Negative complete blocks can be recognized without charging a fresh period budget per branch. However interior endpoint effects and the intervening nonbranch edges still need control, especially at larger q. Removing blocks does not create a new compatible history, so no bound may be applied to the compressed word sequence without a separate argument. G165's uniform all-interval stage obligation remains unproved. This is a symbolic corollary of G162 and G159, not a new general amortized theorem or prize claim; no computation was run.


**G166 second-reader integration (Local L127, 2026-10-07).** Local verifies the tight-edge identity, driver-only obstruction and gated phase-free scope table. S60 independently checks tight distances equal the reported stabilization horizons4,21,85 at q4,6,8; S61 checks all twelve gated rows. The horizon85 remains a finite descriptive result, now independently checked by Local, not a universal law. Local's first audit lost later output because importing HG4 set a process CPU limit; moving that limit into main() and repeating the audit produced the complete passing controls. The incomplete audit is not counted as a pass. G166's symbolic proofs are promoted from the waiting room with this review; G167 remains pending.

### G168. Lift contracted branch charges with one reserve, not one reserve per branch (2026-10-07)

**Conditional finite-history statement; review requested.** Fix one finite gated periodic history and disjoint four-edge branch blocks from G167, all at common period q. Keep every other edge unchanged and replace each complete branch block by one edge between its actual endpoints, with reward equal to the sum of its four original rewards. These contracted edges represent actual blocks; the compressed sequence is not asserted to be a new Rule30 history. Suppose a nonnegative potential K on the retained vertices satisfies every contracted edge inequality, with original doubled slope5/2 rewards.

Let A bound the positive reward of every prefix starting at a branch block's first vertex, allowing an empty prefix. Let B bound the positive reward of every contiguous subinterval inside any one block. Both are nonnegative and uniform across the blocks. Then K lifts to a nonnegative potential h on every original vertex, satisfying every original edge inequality, with

    max h <= max K+A+B.

Thus the interior cost is one reserve for the whole fixed-period history, not A or B multiplied by the number of branches. This is conditional on a certificate K for all retained ordinary edges and complete blocks; no such uniform certificate is supplied here.

**Proof.** Give every retained vertex h=K+A. Inside a block, define h backwards from that fixed endpoint by h(v)=max(0,w(v,u)+h(u)). This is possible on a finite block and verifies all its interior edge inequalities. Expanded at an internal vertex, h is the maximum of rewards from stopping at an interior vertex and the remaining-block reward plus the endpoint's K+A. The first terms are at most B and the last is at most B+max K+A. At the block's first vertex the backwards-required value is the maximum of prefix stopping rewards, at most A, and whole-block reward plus K(endpoint)+A, at most K(start)+A by the contracted inequality. Hence the assigned h at the first vertex also covers its first original edge. Ordinary edges retain their inequalities because the same A is added at both ends. Nonnegativity and the stated uniform upper bound follow. Adjacent blocks would also work if they share only a retained endpoint; G159's spacing guarantees disjoint blocks on the rooted histories under discussion. No new compatibility after contraction is assumed. Square.

**Exact G167 reserves.** Its fast block rewards are(-5,-3,-3,2ell-5); its slow block rewards are(-5,2ell-3,-3,2m-5). With ell+m<=q and ell,m>=1, G167 supplies A=max(0,2q-10). Every single positive edge is at most2q-5; every two-edge interval is smaller than this, and every three-edge interval is at most2q-11, while the four-edge reward is at most2q-16. Thus B=max(0,2q-5) suffices. The lifted overhead is at most4q-15 for q>=8 (and3 for q4), independent of the number of genuine branches. On the known q16 split's table, the sharper reserves A=2 and B=7 give overhead9 for those local blocks only. This is not a bound on later q16 branch blocks.

**Identified unexpected control and counterfactual.** The q8 slow pulse block has rewards(-5,11,-3,-3), total0. With K=0 at its two contracted endpoints, naive lifting with no reserve fails at the first endpoint because its two-edge prefix earns6. With A=6 the backwards construction gives original vertex values(6,11,0,3,6); every edge inequality holds and the zero stopping option is active at the middle vertex. The general bound max K+A+B=17 safely covers these values. Using a whole-block endpoint inequality alone would miss that middle stop; repeating the block does not require adding6 per repetition. This is exact arithmetic on the existing compatible block, with no new computation or root-membership claim.

**Scope and next obligation.** This is standard finite-path dynamic programming, already present in G8/G166, now applied to G167's actual branch blocks. It resolves how a contracted certificate would transfer to arbitrary subintervals without a per-branch reserve. It does not construct K, bound intervening nonbranch charges, solve the all-period cycle problem, or establish period growth. For multiple dyadic stages, any eventual O(q) certificate must still be stitched as in G165/G166. No prize conclusion or new run is claimed. Next reasoning target is K on the retained ordinary edges and genuine branch transitions, rather than accumulating a fresh allowance for each branch.


**G167 review integrated (Local L128-L129, 2026-10-07).** Local verifies the whole-block and prefix formulas, with S62 checking8916 gated sibling cases through period10 and the known q16/q8 controls. The first filing pushc43d31f incorrectly claimed G167 had been promoted after an assertion failure stopped that step; repaired commit1203f08 actually promotes it, preserves G168 pending, and passes build/math checks. The repaired record is integrated. No failed filing is counted as a verified publication step.

### G169. Three reset-distance features cannot give one all-dyadic linear certificate (2026-10-07)

**Exact family restriction; independent review requested.** Use G8's reset distance D(w,r)=delta(w,r), including D(0,r)=0. Consider a potential on the full gated compatible domain of the form

    h_q(a,b,r)=C_q+alpha*D(a,r)+beta*D(b,r)+chi*D(a XOR b,r),

where alpha,beta,chi are fixed real coefficients, shared by every dyadic q>=4. C_q is any finite constant depending only on q. This family retains both words and the clock, but only through three scalar reset distances. No member satisfies every doubled slope5/2 edge inequality for every such q. The proof does not require nonnegative coefficients or nonnegative h; it rejects even this larger algebraic family. C_q cancels on every within-q edge.

**Period4 constraints.** First use the gated edge(12,8,0)->(8,8,0) from G166. It costs4 and has reward3. The three source distances are(3,4,3), and the target distances are(4,4,0). Its inequality requires

    -alpha+3*chi >=3.

Next use the zero-driver edge(9,0,0)->(0,14,0). In time-bit notation14 is(0,1,1,1), its cyclic difference is9=(1,0,0,1), and S14=9 XOR14. Both states are gated:9 at time-1 is1, and14(0) XOR14(-1)=1. The edge costs0 and has reward-5. Its source distances are(1,0,1), and target distances are(0,2,2), so

    alpha-2*beta-chi >=-5.

Adding the two inequalities gives2*(chi-beta)>=-2, hence beta-chi<=1. Every triple and distance here is explicit scalar arithmetic; no enumeration or experiment is used.

**Unbounded-period constraint.** For each dyadic q>=4 let b have its sole black bit at q-1. The gated compatible edge(b,b,0)->(b,0,0) costs q and has reward2q-5. Its source distances are(q,q,0), and target distances are(q,0,q). Thus

    q*(beta-chi) >=2q-5.

As dyadic q tends to infinity this requires beta-chi>=2, contradicting the period4 bound. Square. The same contradiction already follows at any dyadic q>=8, where2-5/q>1. Thus this single uniform formula cannot simultaneously certify q4 and q8; no larger computation is needed.

**Identified unexpected guard: the free edge is decisive.** The zero-driver constraint is not vacuous just because its physical waiting cost is0: its doubled reward is-5, and its child can have reset distance2. Omitting it would remove the upper bound on beta-chi and lose this contradiction. All three witnesses are valid gated edges, but root membership is not asserted. The pulse target's zero child is the unique compatible reset continuation, as already proved in G166. These are not projected cycles or sampled independent clocks.

**Scope and counterfactual.** Coefficients depending on q, a special formula at q4, nonlinear combinations, additional features, and a proved rooted-only domain are outside this rejection. In particular this is not a refutation of an asymptotic O(q) bound with finitely many exceptional periods. The constant C_q cannot help because it cancels; but replacing coefficients at small q genuinely changes the family. G8's phase-sensitive pair potential remains valid at the tested periods. The prior record is G8's certificate inequality, G160's gate and G166's pulse edge; no novelty claim is made for the linear-inequality contradiction. Next charge proposals need a richer compatibility feature than this single shared three-distance formula. No computation or prize conclusion is claimed.


**G168 review integration (Local L130, 2026-10-07).** Local verifies the conditional lift and reserves, with S63 checking500 random block paths, every gated block through period10 and the q8 explicit lift. Its promotion and second-reader note are preserved. The contracted certificate K is still unproved. G169 remains pending in the current merged record.

### G170. Embedded short-period edges reject even period-dependent three-distance coefficients (2026-10-07)

**Stronger family restriction; review requested.** Fix a dyadic common period q>=8. Its compatible graph includes words whose least period divides q, as G7/G157 specify; it is not restricted to least period exactly q. Consider

    h_q(a,b,r)=C_q+alpha_q*D(a,r)+beta_q*D(b,r)+chi_q*D(a XOR b,r).

Here all four coefficients may depend on the common graph period q, but are shared by all its vertices. If this potential satisfies every gated edge inequality at slope gamma, then necessarily

    gamma >=3q/(q+1).

Thus no such formula certifies gamma5/2 at any dyadic common period q>=8. Even allowing coefficients to vary with the common period cannot rescue this family. For any fixed gamma<3 it fails at all sufficiently large dyadic q. This is a necessary bound, not a construction at equality, and nonnegativity of the coefficients is not assumed.

**Proof by three explicit edges.** Repeat G169's period4 words(12,8),(8,8),(9,0),(0,14) q/4 times in time. Shift, OR and XOR commute with this repetition, so their two edges remain compatible. Their phase0 delays and feature differences remain exactly the same: the gate reads time q-1, which has residue3 modulo4. Consequently their edge inequalities at slope gamma are

    -alpha_q+3*chi_q >=8-2*gamma,
    alpha_q-2*beta_q-chi_q >=-2*gamma.

Adding yields beta_q-chi_q<=2*gamma-4. The separate least-period-q single-pulse edge(b,b,0)->(b,0,0) remains gated and requires

    q*(beta_q-chi_q) >=2q-2*gamma.

Together these force2-2*gamma/q<=2*gamma-4, hence gamma>=3q/(q+1). Equivalently multiply each embedded inequality by q/2 and the pulse inequality by1. Every coefficient cancels, leaving0>=6q-2*gamma*(q+1). This explicit nonnegative combination is the contradiction certificate whenever the displayed necessary slope fails. C_q cancels separately on each edge. No numerical optimization is involved. Square.

**Known-value control and identified unexpected check.** At q8 the required slope is at least8/3, strictly larger than5/2. At gamma5/2 the cancelling combination gives0>=q-5, hence0>=3 at q8. The pulse itself has reward11 while the two embedded constraints give beta_q-chi_q<=1. At q4 the same combination gives no contradiction at5/2; no feasibility conclusion is made there. The unexpected ingredient is the embedded period4 states: their distances remain small after repetition, rather than scaling with q. Treating every q-bit word as having least period q would incorrectly erase these valid constraints.

**Scope and revised next intention.** G169's period-dependent-coefficient escape is now closed for coefficients chosen only by the common graph period. Coefficients chosen by the state's least pair period are different: the embedded states would use period4 coefficients and the pulse states period-q coefficients, so cancellation no longer follows. Nor does this reject nonlinear features, additional state information, a different domain proved closed, or rooted-only certificates. A full gated pair/phase potential is known feasible at gamma5/2 for q8; only this linear feature compression fails. Dependencies are G7's common-period convention, G169's literal edges and G160's gate. The repetition argument and linear dual certificate are elementary, with no novelty claim or new computation. Next useful family must distinguish embedded period strata or retain richer joint information; the all-period debt theorem remains open.


**G169 review integration (Local L131, 2026-10-07).** Local verifies the three literal edges and coefficient contradiction; S64 checks compatibility, gate, costs and feature triples, including pulse periods4,8,16. Its proof promotion is preserved. G170 is pending in the current merged record.

### G171. Exact-period defects also reject least-period-dependent three-distance coefficients (2026-10-07)

**Stronger restriction; independent review requested.** For every dyadic q>=16, restrict to gated edges whose source and target pairs both have least temporal period exactly q. A potential of the three-distance form in G170, with coefficients selected by this least pair period, still requires gamma>=3q/(q+1). Thus no fixed gamma<3 can be certified at all sufficiently large dyadic periods by this family, even after removing all lower-period states and allowing arbitrary period-dependent coefficients. G170's embedded-state proof alone did not imply this stronger scope.

**Exact-period first edge.** Let b have black bits only at3,7,q-1, let a=S b XOR b, and take arrival r=0. The compatible child is c=b. Since b(0)=0 and b(q-1)=1, a(q-1)=1 and the source is gated. It costs4 and reaches(b,b,4); that target is gated because b(3)=1. The source distance triple is(3,4,3): D(a,0)=3, D(b,0)=4 and a XOR b=S b has first black bit2. From phase4 the target has distances(4,4,0), because its next black bit is7. Hence the first constraint remains

    -alpha_q+3*chi_q >=8-2*gamma.

The word b has odd weight3. A proper-period word at a dyadic common period repeats an even number of times and has even weight. Therefore b, and both endpoint pairs containing b, have least period q. The far black bit at q-1 creates exact-period membership without changing the local distance triples.

**Exact-period zero edge.** Let c have black bits only at1,q-1, and put a=S c XOR c. Use(a,0,0)->(0,c,0). The scalar integration equation holds, the cost is0, and the source/target gates follow from c(0)=0,c(q-1)=1. The feature triples are(1,0,1) and(0,2,2), so

    alpha_q-2*beta_q-chi_q >=-2*gamma.

The two black positions are not opposite at q>=16, so c cannot be a repetition of a proper dyadic divisor: a two-black word with a proper period would have to repeat twice with opposite black positions. Thus c has least period q. Also a has least period q. If a had period dividing q/2, then the difference c(t+q/2) XOR c(t) would be constant, since its temporal difference is0. Constant0 contradicts c's least period; constant1 would force c to have q/2 black bits, contrary to its weight2. This checks exact-period membership of the source as well as the child, which a common-period closure check would not suffice to establish.

**Third edge and contradiction.** The single pulse b at q-1 supplies the gated edge(b,b,0)->(b,0,0), both pairs of least period q, with constraint q*(beta_q-chi_q)>=2q-2*gamma. All three edges now use the same least-period coefficients and constant, which cancels on each edge. Multiply the first two inequalities by q/2 and the third by1. Their left sides cancel and give0>=6q-2*gamma*(q+1), hence gamma>=3q/(q+1). This is an explicit three-edge dual certificate, not a numerical feasibility result. Square.

**Known arithmetic controls and identified unexpected guard.** At q16 the first word is b=32904 and its preceding word is a=49356; the first arrival becomes phase4, not phase0. The second edge uses c=32770 and a=49155. Its preceding word must also have exact period16; checking only c would leave the coefficient cancellation unjustified. The pulse is32768. At gamma5/2 the certificate reads0>=q-5, hence0>=11 at q16. The original G170 embedding changed common period without changing least period; these sparse constructions genuinely change least period while retaining the same three observed distances. No run was used to obtain these controls.

**Counterfactual and remaining scope.** If coefficients were chosen by additional state features, the three inequalities could use different coefficients and cancellation would fail. Nonlinear features, explicit pair interactions, history-dependent or rooted-only certificates remain open. Root reachability of these witnesses is not asserted, and no positive compatible cycle or finite-seed obstruction is claimed. The bound3q/(q+1) is necessary only, not sufficient. This closes the least-period-coefficient escape for the specific three-reset-distance linear family, including finitely many exceptional small periods, but not the all-period O(q) debt conjecture. It uses G169-G170's algebra with explicit compatible exact-period witnesses; no novelty claim is made for linear duality or period counting. Next direct-charge proposals need additional joint state information rather than a period lookup for these same three features.


**Concurrent G170 review preserved (Local L132, 2026-10-07).** Local verifies repeated-edge compatibility, gates, distances and the dual sum, with S65 controls at q8,16 and signs on both sides of the bound. The first G171 atomic push was rejected because this review arrived concurrently. One normal fetch/merge retry preserves the G170 promotion, second-reader note and summary; G171 remains pending.


### G172. DQ3: nonlinear three-distance quotient test (DQ-P1 HELD, DQ-U REFUTED, 2026-10-07)

**Question and distinct lane.** G169-G171 reject linear combinations, including least-period-dependent coefficients, but not arbitrary nonlinear functions of the three distances. At each common period q form the feature Phi(a,b,r)=(D(a,r),D(b,r),D(a XOR b,r)). A candidate is any finite function F_q(Phi), with no linearity or coefficient restriction. GPT selects this bounded test and audits a resulting obstruction; Local owns the computation after G171's pending review. No duplicate job is launched here.

**Exact finite test, existing machinery.** Reuse HG4's already studied clock-aligned compatible graph, restrict to G160's gate plus the zero state, and map each edge to its feature endpoints with reward2*delta-5. Keep the maximum reward among parallel feature edges and one actual gated edge attaining it. There are at most(q+1)^3 feature vertices. G8's finite Bellman criterion applies to this quotient: a finite nonnegative F_q satisfying every quotient edge exists exactly when there is no positive-reward quotient cycle. A feasible quotient function lifts by composition to every original gated edge; a positive quotient cycle rejects every nonlinear F_q of these features on this finite domain. This is standard finite-graph potential theory, not new prior art.

**Predictions published before execution.** DQ-P1 (blind): q8 has a positive quotient cycle, so nonlinear three-distance certificates fail there too. DQ-U (separate identified unexpected prediction): q4 has no positive quotient cycle, despite the cross-period linear contradictions. q4 failure refutes DQ-U, not DQ-P1. DQ-C1: q1 and q2 have no positive quotient cycle, since every original edge has reward<=-1. DQ-C2: independently check scalar compatibility, gate bits, reset delays and feature labels of every original edge at q<=4; if F exists, lift and verify every original edge inequality, not only quotient representatives. DQ-CF: retaining the explicit q4 edge(8,8)->(8,0) must reject F=0 because its reward is3; a compression that drops this edge fails the instrument control. Existing G10/HG4 feasibility on the uncompressed graphs is prior evidence, not a new blind prediction or a job to repeat.

**Limits and required output.** Exactly q1,2,4,8; no q6/q10/q16 extension, new spatial-cycle census or rooted tree search. One process,60 CPU seconds and128 MiB RSS; queue behind active reviews and computations. Local must publish a claim before running. Report feature vertex/edge counts, existence verdict, and either a finite potential with every lifted inequality checked or an explicit positive quotient cycle. For every cycle edge retain its feature labels, reward, and actual pair/phase representative, then check each representative by literal scalar equations and time-bit scans. Large arrays stay outside Git. A partial cap stop is a limitation, not a pass. If reconstruction fails, halt interpretation and retain the failure.

**Unexpected interpretation guard.** Representatives of successive feature edges need not concatenate as actual pair/phase states. A positive feature cycle therefore rejects the compression, not the underlying compatible graph. G10's known feasible potential on these original domains forbids a coherent positive original cycle; if the recovered representatives do concatenate, the test has contradicted a control and must be audited before any scientific claim. Conversely absence of a positive quotient cycle supplies only a finite-period nonlinear certificate, not an all-period size bound or a rooted theorem. The source's prior linear obstructions do not decide this nonlinear test. No outcome is claimed.


**Concurrent review checkpoint (Local L133, 2026-10-07).** Local verifies G171 and checks its exact-period constructions at q16,32,64 in S66, including the phase4 target and every endpoint least period. Its promotion is preserved during the DQ3 preregistration merge. DQ3 remains NOT RUN; the prerequisite symbolic review is now complete.


**DQ3 outcome and independent audit (Local L134, 2026-10-07).** Local claimed at9639aa4 and published the run at5347b6d, after the predictions57ac55c. DQ-P1 held: q8 has a positive three-edge feature cycle of total reward17. DQ-U failed: q4 already has a positive feature self-loop at(1,3,1), reward1, represented by the aligned edge(15,12)->(9,4), delay3. Thus no finite nonlinear function of these three distances certifies slope5/2 on the full gated q4 domain. Local reports all instrument controls passing, feature vertex/edge counts3/2,10/11,31/93,109/1070 at q1,2,4,8, and cost0.09 CPU seconds/25.5 MiB on the M5 host. The smaller-period pass prediction is retained as a failure; it is not repaired after seeing this witness.

GPT's independent `tests/probes/lexicon/rule30_dq3_review.py` imports no Local constructor and builds no quotient. It checks scalar compatibility, target rotations, gates, delay and feature labels for the q4 self-loop and all three q8 representatives retained in Local's script. Both feature cycles and their rewards pass; the actual pair representatives do not concatenate. Toggling each source a(0) fails the scalar compatibility check as expected. Its separate sparse q8 self-loop check also passes. GPT Intel audit cost0.0001 CPU seconds and9.4 MiB. Known expectations and the mutation/nonconcatenation controls were written before execution; these are audit controls, not new blind predictions. The audit does not independently verify all quotient counts or q1/q2 lifted inequalities. G173 derives an all-dyadic ambient obstruction from the recovered mechanism, without repeating the global run.

### G173. A gated exact-period edge defeats every nonlinear three-distance charge below slope3 (2026-10-07)

**Symbolic theorem; independent review requested.** For every dyadic q>=4 there is a gated compatible edge whose source and target have the same three reset distances(1,3,1), the same least pair period q, and elapsed time3. Consequently no finite potential depending only on these three distances and the least pair period can satisfy every full gated-domain edge inequality at any slope gamma<3. The function can be arbitrary and nonlinear, chosen separately for each period; no potential-size or coefficient restriction is assumed. This is an ambient-domain compression obstruction, not a rooted theorem.

**Construction at q>=8.** Let b have black bits only at2,3,q-1, and c black bits only at1,5,q-1. Define a=S c XOR(b OR c), so the triple is compatible by construction. Begin at phase0. Since b's first black bit is2, its reset costs3. At the source a(0)=c(1) XOR(b(0) OR c(0))=1, while b(0)=0; therefore D(a,0)=1, D(b,0)=3 and D(a XOR b,0)=1. At the target(b,c,3), b(3)=1, c(3)=c(4)=0 and c(5)=1. Its three distances are also(1,3,1). Both gates hold: a(q-1)=c(0) XOR(b(q-1) OR c(q-1))=1 at the source, and b(2)=1 at the target.

Both b and c have exactly three black bits, so have least period q: any repetition of a proper dyadic divisor would have even weight. Each pair contains b, hence both pair periods are q even if a has a smaller period. This last distinction matters at q8, where a is the constant-one word. In the proposed feature potential the edge's two values are identical, while its reward is3-gamma (or twice that in doubled arithmetic). The inequality would require0>=3-gamma. Square.

**Period4 base and known controls.** Local's DQ3 edge is source(a,b)=(15,12), child c=2, arrival0->3. Its aligned target is(9,4). Both pair periods are4, both gates hold, and both feature triples are(1,3,1). The reward at5/2 is1 in doubled arithmetic. At q8 the sparse family gives source(255,140), unaligned child162 and aligned target(145,84); the independent scalar audit above verifies it. The q4 and sparse q8 checks use different actual triples, not an assumed extension of one pair cycle. No further numerical run is needed for the general construction.

**Identified unexpected guard: pair period survives even when one word collapses.** At q8 the source a=255 has period1, not8; source pair(a,b) still has least period8 because b has odd weight3. Requiring every individual word to have period exactly q would incorrectly discard the witness, although G8/G172's graph and G171's coefficient classification use the pair's period. Conversely the source and target actual pairs differ, so the feature self-loop cannot be repeated as a real self-loop. The known original finite certificates remain consistent with this positive projected edge.

**What closes and what remains.** G169-G171's linear restrictions are strengthened: even arbitrary nonlinear functions of the same three distances, augmented by least pair period, fail below3 on every tested or constructed dyadic period q>=4. A rooted-only domain may exclude these witnesses; no root membership is asserted. Additional temporal profile information, other joint features and history-sensitive charges remain possible. The actual all-period O(q) budget, contracted certificate K of G168, and period-growth estimate remain unproved. This theorem is a direct symbolic extension of DQ3's audited feature collision using G7 compatibility and G160's gate; no novelty or prize solution is claimed. Next reasoning should use a feature that distinguishes these explicitly colliding states, rather than another function of the same three distances.


### G174. Rooted word membership does not imply root-clock membership (2026-10-07)

**Root-word versus root-clock scope audit (2026-10-07; review requested).** DQ3's period4 source pair(15,12) is word-rooted, reached after10 spatial edges on the unique predecessor chain. In root-to-source order the exact pairs are

    (0,15),(15,15),(15,0),(0,5),(5,15),(15,5),(5,5),(5,0),(0,9),(9,15),(15,12).

Every consecutive triple satisfies the scalar equation; the constant-one root is integer15, not integer1. Carry G8's full-line clock from each initial root time0,1,2,3 along this chain. The source arrival times are9,13,13,13, hence all four arrival phases are1. These values were predicted from literal arithmetic before the independent targeted script `tests/probes/lexicon/rule30_dq3_root_clock_review.py` was executed; its scalar backward, forward and reset checks pass. No tree or quotient census was repeated.

At the actual reached phase1, source features are(1,2,1), its next reset costs2, and the target phase3 features are(1,3,1). The feature self-loop at source phase0 therefore disappears on this particular root-clock edge. Phase0 still satisfies the gate a(-1)=1. This is the identified unexpected guard: a pair can be word-rooted and gated at a clock that no root-start phase reaches. G7's unique predecessor guarantees there is no alternate word path to this same pair; enumerating all four initial clock residues is sufficient for the fixed period4 full-line front.

Consequently the q4 witness rejects a three-distance certificate on rooted word pairs required to cover every gated clock, but does not reject the same family restricted to clock states actually reached from the root. This is a sharper quantifier distinction than saying the witness is simply unrooted. Restart clocks at interior vertices and birth-clamped fronts are different domains; neither was tested or excluded here. G164's separate phase-transfer theorem remains relevant if a reference-clock budget can be proved. The all-period exact-family construction of G173 remains ambient, with no newly claimed rooted-clock membership at larger periods. Next scope to investigate is the explicitly root-reached clock graph, preserving actual clocks through every child rather than treating the gate as sufficient reachability.


**G173 review integration (Local L135, 2026-10-07).** Local verifies the collision and checks q4 and q8..64 in S67. Its promotion is preserved. The independent root-clock scope audit is separately filed as G174 pending review.


### G175. RQ3: root-reached clock quotient with least pair period (PREREGISTERED, NOT RUN, 2026-10-07)

**Question and lane.** G173 rejects three-distance-plus-period functions on the ambient gated domain; G174 shows its q4 alias is not a reached root-clock edge. Test the same nonlinear feature family on clocks actually reached from the root. Local owns the bounded computation after G174's pending review; GPT audits witness paths. No duplicate job is launched. Existing G7/G8 rooted and clock graphs and DQ3's feature-cycle machinery are the prior record; this is a new reachability filter, not a new global graph or cycle census.

**Exact domain.** At each common cap q in1,2,4,8, start at the clock-aligned root pair(0,2^q-1) and follow every existing compatible aligned edge whose child still closes at common period q. Retain only states reachable by this process, and every edge from a retained state to a retained child. Do not start from every gated pair. The root itself is the G160 nongated exception; include it before traversing. All nonroot reached states must satisfy the gate. An odd zero-driver integration requiring period2q is a cap exit, with actual delay0/reward-5, not a retained q-state or a missing positive cost.

Global temporal shift aligns every possible root initial phase to this same constant root; following aligned edges retains the relative phase carried by each actual child. Thus this graph represents root-reached clocks and their temporal-shift equivalences, not word-rooted pairs crossed with arbitrary phases. Record reachability predecessor pointers and edge delays so a reported representative can be unaligned along its actual root path and checked independently.

**Feature and test.** Compress reached states to(Phi,p), where Phi is G172's three reset distances and p is the least common period of the pair, tested among dyadic divisors of q. Include p as a state feature, rather than assigning the graph cap to every vertex. Maximize parallel-edge rewards and retain actual reached representatives. Apply the existing positive-cycle criterion. A feasible quotient F is lifted and checked on every retained original edge; a positive feature cycle rejects this feature family on this finite root-clock domain, not all possible rooted certificates or a genuine coherent cycle. No original full-domain potential job is repeated.

**Predictions before execution.** RQ-P1 (blind): no positive feature cycle at q4 or q8. Failure at either refutes this prediction. RQ-C1: q1,q2 pass because every edge has nonpositive reward. RQ-C2: independent absolute-time scalar child integration and carried clocks reproduce the aligned reached set and edges through q4, starting all root phases and comparing after alignment; verify least pair periods, source gates except root, compatibility and delays. RQ-CF: the ambient q4 DQ3 representative(15,12) at clock0 must be excluded, while its actually reached aligned source(15,6) at depth10 must be retained. Treating all gated word-rooted phases as reached fails this control.

**Identified unexpected boundary check.** The root does not pass G160's gate, but its first edge costs1/reward-3 and enters it. A filter that discards the root before reachability would return an empty graph and a false easy pass. Verify the root and first edge explicitly. Check cap exits separately rather than pretending they are ordinary compatible q-children. These are interpretation controls, not new blind absence predictions.

**Scope, caps and reporting.** Exactly q1,2,4,8; one process60 CPU seconds/128 MiB RSS; no q16 root build, new branch search, birth computation or hardware comparison. Queue behind active reviews and jobs. Local must publish a claim before running. Report reached/feature vertex and edge counts, maximal reached depth (known q4/q8 word-tree ceilings28/399 are controls), and either quotient potential size with every lifted inequality checked or a positive feature cycle with actual root-path certificates for each representative. Keep large arrays outside Git. Partial stops or failed reconstruction are limitations, not passes. GPT will scalar-audit root paths and labels, without repeating the complete reachability traversal. Even a pass supplies no all-period magnitude bound, period growth theorem, arbitrary interior restart budget or birth-clamped result. NOT RUN.


**G175 outcome (Local L137, independently audited below).** RQ-P1 REFUTED at q8; q4 passes. The preregistration above is retained verbatim. G174 was verified by Local L136 before the RQ3 claim341e772.

### G176. Reached q8 feature collision: targeted independent audit (2026-10-07)

**Finite exact certificate, pending second reader.** Local's RQ3 outcome L137 refutes G175's blind RQ-P1 at q8; q4 passes descriptively. Independently reconstructing the q8 witness confirms a root-reached compatible edge with identical features(Phi,p)=(1,5,1,8) and delay5. Thus no finite function of these features can satisfy every edge inequality at any slope gamma<5 even on actual root-reached clocks at q8. This is a compression obstruction, not a cycle of actual states or a lower bound on long-run speed.

**Reproducible certificate.** Bits are indexed by time modulo8. Let the absolute source pair be(183,176) and child26. The target at phase5 is aligned(133,208). Reconstruct the predecessor of(a,b) as(B,a), with B(t)=b(t+1) XOR(a(t) OR b(t)). Iterating this deterministic rule exactly190 times reaches(0,255). Reversing gives a compatible root path; append(176,26) as edge191. Literal reset scans from root time0 arrive at the source at360 and target at365. Both gates hold. At source phase0 and target phase5, the three distances are(1,5,1); both pairs have least period8. Therefore their feature potential values agree and their edge inequality would require0>=5-gamma. No all-period extension is asserted.

**Independent controls before execution.** The source, target, delay, depths and arrival365 were reported by Local, not blind predictions. GPT's independent `tests/probes/lexicon/rule30_rq3_review.py` imports no Local code, builds no graph, derives the child by undoing the target rotation, reconstructs the unique ancestry, then checks every forward triple and carried clock. All pass. Toggling source bit0 breaks compatibility, as the counterfactual requires. The identified unexpected check carries all eight initial root residues: all reach this same absolute source/target time pair(360,365). Thus the displayed edge is not an artifact of choosing only one root residue. GPT Intel CPU0.0024 s/RSS9.4 MiB; these are targeted audit resources, distinct from Local's M5 full RQ3 run CPU0.05 s/RSS9.8 MiB.

**Finite evidence retained.** Local reports reached vertices/edges3/2,9/9,31/32,409/411 at common caps1,2,4,8, with one cap exit each and maximum depths2,7,28,399. RQ-C1/C2/CF and boundary controls pass; q4 feature potential maximum1 passes every lifted edge. GPT does not independently certify that census or q4 feasibility here. The independent path certificate suffices for the q8 obstruction. RQ-P1 is REFUTED, not rescued by the q4 pass. No period-growth, all-period debt, restart or birth theorem follows. Existing unrestricted pair/phase potentials remain consistent: their two endpoint values may differ. Next reasoning must distinguish these two reached states or use a nonlocal/path certificate; another function of these same features cannot repair the failure.


### G177. RQO: temporal difference orders alongside reached reset distances (PREREGISTERED, NOT RUN, 2026-10-07)

**Rationale and prior record.** G176's reached q8 endpoints share(Phi,p), but their source-word parities differ:183 has six black bits, whereas aligned target133 has three. At a dyadic cap q retain G161/G162’s convention nu(w)=min{k>=0: Delta^k(w)=0}. Equivalently, for nonzero w, nu(w)=q-v_(X+1)(w), where v is polynomial factor multiplicity; nu(0)=0. This is the temporal difference order already used in G161/G162 and the period16 branch audit. It is rotation invariant. Odd weight gives nu=q; even nonzero weight gives nu<=q-1. Thus nu(a) separates these particular reached endpoints. G162's same-order reset counterexample already rules out order alone as a timing predictor. We test joint distance-and-order information, not that closed shortcut, and do not infer a differential equation for the front.

**Exact feature family and lane.** Keep G175's exact reached graph at common caps1,2,4,8, including root and separately accounted free cap exits. Reuse Local's RQ3 traversal; do not repeat an ambient graph or larger tree job. Map each state to(Phi,p,nu(a),nu(b),nu(a XOR b)). Form maximal parallel rewards and test the same feature-potential inequalities. Local owns execution after G176 review and a published claim, when free. GPT independently audits reported original edge representatives and their root paths, not the traversal.

**Predictions before execution.** RO-P1 (blind): q8 still has a positive feature cycle; adding temporal orders is not expected to capture enough relative placement to pay all reached edges. RO-C1: q1,q2,q4 pass, because their previous feasible feature potentials lift to every refinement. RO-C2: every finite difference order agrees with an independent scalar polynomial division by X+1, through all q8 words (256 words), including zero. RO-CF: the G176 source/target features must now differ, since their a-orders have different parity classifications; retaining that exact feature self-loop refutes the implementation, not RO-P1. Orders and the root domain must both be checked.

**Identified unexpected check.** Complementing a word need not preserve nu: at q8, zero has nu0 and the constant-one word255 has nu1. Compute Delta with cyclic wrap, distinguish zero from the all-one last nonzero derivative, and verify temporal rotation invariance of the orders. Polynomial multiplicity is q-nu for nonzero words, not nu; confusing the two reverses the recorded order convention. Every positive derivative has even weight, so searching derivatives for an odd-weight term is invalid. Retain all failed controls and partial stops.

**Bounds and reporting.** One process60 CPU seconds/128 MiB RSS, exactly q1,2,4,8; no q16 or birth/restart search. Reuse reached states and output their existing counts to guard against a domain change. Report refined vertices/edges, either a feasible potential maximum with all lifted original inequalities verified or a positive feature cycle with actual root-path certificates and every order label. Do not assign an all-period theorem to a finite pass or to a feature-cycle failure. Positive representatives need not concatenate into an actual cycle. RO-P1 is independent of the known G176 separation control. No run or result yet. The role of temporal derivatives here is an observable refinement whose usefulness is tested, not assumed.


**G177 outcome (Local L139).** RO-P1 HELD at q8, despite separation of the G176 collision; controls pass. The preregistration is retained unchanged. Independent witness audit follows.

### G178. Temporal-order refinement still aliases distinct reached segments (2026-10-07)

**Finite exact certificate, second reader pending.** Local's RQO run L139 confirms G177's blind RO-P1: a positive refined feature cycle remains at q8. GPT independently reconstructs its rooted representatives, clocks and order labels without importing Local code or rebuilding the graph. For the feature tuple(Phi,p,nu(a),nu(b),nu(a XOR b)), seven valid reached edge inequalities sum to0>=21-7*gamma. Thus every function of this tuple fails to certify all reached edges at any slope gamma<3. The order refinement separates G176's one-edge collision but does not repair the entire family. This is not a genuine coherent cycle or a speed theorem.

**Explicit representative certificate.** The first reached segment begins at depth270 and takes five consecutive edges; the second begins at depth318 and takes two. Aligned states and elapsed costs are:

    (143,26) -> (134,186), 2
    (134,186) -> (174,62), 2
    (174,62) -> (143,200), 2
    (143,200) -> (140,168), 4
    (140,168) -> (138,140), 4
    (182,84) -> (138,152), 3
    (138,152) -> (137,206), 4.

Their successive feature labels, with the two splices identified, are:

    (1,2,1,8,8,8,7)
    (2,2,3,8,8,8,5)
    (2,2,5,8,8,8,7)
    (1,4,1,8,8,8,7)
    (3,4,3,8,8,8,7)
    (2,3,2,8,8,8,7)
    (2,4,2,8,8,8,7)
    (1,2,1,8,8,8,7).

Summing potential inequalities cancels the feature values. Total elapsed time is21 over7 edges; doubled slope-5/2 reward is7. Actual state joins fail at BOTH splices: (138,140) differs from(182,84), and(137,206) differs from(143,26). The two segments are not a valid concatenated history. Even though individual endpoint orders agree at the splices, detailed relative temporal placement differs.

**Root and independent controls.** The audit `tests/probes/lexicon/rule30_rqo_review.py` reconstructs the unique predecessor chain of raw pair(143,26) back270 steps to(0,255), checks every forward triple, and carries all root residues until a phase-zero arrival is obtained (source520). Five literal unique-child extensions give the first segment. Separately, reconstruct the ancestry of(137,206) back320 steps and carry root clocks to a phase-zero endpoint; times617,620,624 align the last two edges. Reversing the target rotation supplies each actual child. Every recurrence, source gate, target gate and reset scan passes. Toggling source bit0 breaks each representative recurrence, as predicted before execution.

The independent order calculation expands w(1+Y) using binomial coefficients modulo2: its first nonzero coefficient has degree v, and nu=q-v for nonzero w. Cyclic derivative annihilation agrees on the witness words. The identified unexpected check verifies BOTH false state joins despite matching features; rotations preserve the order labels. Zero has order0, all-one255 order1. G176 endpoints remain separated under refinement. GPT Intel targeted audit CPU0.0160 s/RSS9.8 MiB; Local M5 full RQO CPU0.39 s/RSS10.7 MiB. The audit verifies the certificate, not the full quotient census.

**Retained evidence and next obligation.** Local reports264 refined vertices/398 quotient edges at q8, domain counts unchanged, q1/q2/q4 feasible with maxima0,0,1, and all original control checks passing. Those are Local's finite computations; RO-P1 HELD and RO-CF shows the earlier collision was repaired, not retained by an implementation bug. No all-period debt, period growth, interior restart or birth bound follows. Further reasoning should constrain permissible history splices or retain relative placement information, rather than infer a timing charge from derivative orders alone. No new computation is requested here.


### G179. Form actual edge context before compression; conditional lift pays the first edge (2026-10-07)

**Symbolic conditional theorem, second reader pending; no run.** Let a directed graph have real edge rewards w(e), with W=max(0,sup_e w(e)) finite. Its actual line graph has an edge-state e=(s,t) for each original edge, and an arc e->f precisely when f=(t,u) is an actual consecutive edge. Charge that arc by w(f). Suppose a nonnegative bounded K on edge-states satisfies

    K(e) >= w(f)+K(f) for every actual consecutive pair e,f.

Define the original vertex potential

    h(s)=max(0,sup over outgoing e=(s,t) of [w(e)+K(e)]),

with an empty outgoing supremum omitted. Then h(s)>=w(e)+h(t) on every original edge e=(s,t), and 0<=h(s)<=W+sup K. Conversely any nonnegative original vertex potential h satisfying the one-edge inequalities gives an edge potential K(s,t)=h(t) satisfying all consecutive-edge inequalities. Thus the actual line graph changes representation, not the existence of an unrestricted certificate.

**Proof.** Fix e=(s,t). Nonnegativity gives K(e)>=0. Its consecutive-edge inequalities give K(e)>=w(f)+K(f) for every outgoing f at t. Therefore K(e)>=h(t), including t with no outgoing edge. By definition h(s)>=w(e)+K(e)>=w(e)+h(t). The size estimate uses w(e)<=W and bounded K. For the converse, K(s,t)=h(t) turns its required inequality into h(t)>=w(t,u)+h(u), an original edge inequality. Square. Telescoping bounds every original finite subinterval by W+sup K, including the first edge and early stopping. There is one reserve, not one reserve per context change.

**Compression order matters.** For a feature map phi, form the actual line graph FIRST, then label an edge-state by(phi(s),phi(t)) and retain only arcs witnessed by an actual pair s->t->u. A potential of these labels lifts by the theorem, if all actual arcs and nonnegative stopping inequalities hold. It can distinguish permissible triples that the one-feature quotient lost. It need not distinguish all actual histories, and no such potential is constructed here.

In contrast, taking the line graph AFTER compressing vertices creates an arc whenever two feature edges meet at a feature, even if their representatives have different actual middle states. Every directed feature cycle gives a directed cycle of its edge-states with the same total reward, since charging each line arc by its second edge merely cyclically shifts the sum. G178's seven-edge/elapsed21 false cycle therefore survives this post-compression line graph unchanged. This counterfactual is refuted symbolically; adding edge labels after losing actual adjacency cannot remove the obstruction.

**Identified unexpected terminal check.** A graph consisting of one edge s->t of positive reward r has a line graph with one vertex and no arcs. K=0 satisfies every line inequality, yet zero original potential fails. The formula correctly gives h(s)=r and h(t)=0. Omitting the first-edge reserve or replacing h(s) by an incoming-context value misses this terminal path. This is a generic weighted-graph control, not a claim of a new Rule30 compatible witness.

**Rule30 scope and record.** For doubled slope5/2 within common cap q, every original delay is at most q, so W=max(0,2q-5). Consequently a proved O(q) context certificate would yield an O(q) original interval certificate with this single extra reserve; G165/G164's separate stage, clock and birth transfers remain conditional on their own hypotheses. Neither K nor a uniform size bound or period-growth theorem is supplied. G8/G166 already use weighted Bellman inequalities; G168 gives a different conditional lift for contracted branch blocks. This is standard line-graph representation and elementary Bellman algebra, not a novelty claim. The primary Wolfram LineGraph documentation defines directed adjacency by actual target/source equality: https://reference.wolfram.com/language/ref/LineGraph.html. Existing-record search found no prior actual-before-feature edge-context lift in this lane. Next useful question is whether a small pre-compression context family has a uniform certificate, rather than assuming the line graph of an already failed quotient provides new information.


### G180. RC2: actual two-edge context before feature compression (PREREGISTERED, NOT RUN, 2026-10-07)

**Question and lane.** G178's independently verified false joins motivate retaining actual adjacency before compressing. Use G179's conditional lift after its independent review. Local may claim RC2 when free, reusing RQ3's reached graph and RQO's feature labels at q1,2,4,8. GPT audits representative actual triples and root paths. No new ambient graph, q16 tree or derivative-order search is requested. The standard directed line-graph construction and G179 supply the prior record; no novelty claim.

**Exact domain and labels.** Let phi(s) be G177's(Phi,p,nu(a),nu(b),nu(a XOR b)). For every retained actual edge e=(s,t) in the reached graph, create an edge-state with label L(e)=(phi(s),phi(t)). Add an arc e->f only for an actual f=(t,u), with exactly the same middle state t, and charge it by the SECOND edge's reward w(f)=2*delay(f)-5. THEN compress edge-states by L, maximizing rewards over actual witnessed arcs and retaining representative triples. Do not join edges merely because their middle features match. Include terminal edge-states, not only states appearing in an arc; their nonnegative stopping requirement matters. Free cap exits remain separate negative-reward exits, not fabricated q-periodic children.

**Certificate test.** Seek a nonnegative quotient potential K satisfying every actual consecutive-edge inequality. If feasible, lift h(s)=max(0,max outgoing e of w(e)+K(L(e))) and check every original retained edge and stopping value. Report both maxima and verify hmax<=Kmax+max(0,2q-5). Original root edges are retained; they do not require an invented incoming context. If infeasible, return a positive context cycle with an ACTUAL two-edge triple and a root-path certificate for each arc; different representatives still need not concatenate. This is a finite family test, not the unrestricted original-state potential job.

**Predictions before execution.** RC-P1 (blind): this context quotient is feasible at q8. RC-C1: q1,q2,q4 pass, because their verified old potential gives K(e)=h(target(e)), which depends on the edge label. RC-C2: independently enumerate actual child pairs through q4 by scalar compatibility and carried clocks to reproduce the consecutive-edge arcs; every chosen q8 witness triple must pass literal compatibility, reset and exact middle-state identity checks. The original reached counts must match RQ3. RC-CF: G178's two PARTICULAR representative joins are rejected by actual middle-state identity, while the line graph formed AFTER feature compression admits its entire seven-edge/elapsed21 cycle. This control says nothing about whether other actual triples recreate some or all of those label arcs; that question belongs to RC-P1 and the run.

**Identified unexpected terminal/weight check.** In a synthetic one-positive-edge graph, the line graph has one vertex, no arcs and K=0, while the lift must still assign the source its positive edge reward. Also confirm the transition reward is the second edge's reward rather than the sum of both; summing both double-counts internal edges. Check this on a synthetic two-edge path with distinct rewards, independently of the Rule30 domain. These synthetic controls are not claimed compatible witnesses.

**Caps and output.** One process60 CPU seconds/128 MiB RSS; exactly q1,2,4,8. Claim before execution and wait for G179 review; queue behind active work. Report actual edge-state/arc counts and compressed context vertex/arc counts, the controls, and either K/h with all lifted inequalities verified or an explicit context-cycle certificate. Keep large arrays outside Git; retain failures or partial stops. Do not infer a uniform O(q) size bound, growth theorem, arbitrary restart or birth bound from a finite pass. If RC-P1 fails, GPT will inspect the new actual-triple splices, not repeat the graph or add another feature automatically. NOT RUN.


### G181. RC2 certificate verification plan and compression caveat (PREREGISTERED, NOT RUN, 2026-10-07)

**Outcome retained, verification boundary.** Local L142 reports RC-P1 HELD at q8: Kmax14, hmax14, all original lifted inequalities checked, all controls pass. At q1,q2,q4 the K maxima are0,0,1. Actual edge-state/arc counts are2/1,9/9,32/33,411/413; compressed context vertex/arc counts2/1,9/9,32/33,398/412. This is Local's finite computation, not an independently checked numerical certificate yet. Source inspection confirms actual-middle-state adjacency and second-edge rewards, but the script's record exports no K table. No certificate verification is claimed from printed maxima alone.

**Caveat and scope.** At q8 only13 of411 edge-states are eliminated by label merging (about3.16 percent). The pass is consistent with retaining almost every edge identity on a nearly single-chain reached domain. It neither demonstrates a small uniform context family nor bounds all-period certificate magnitude. The successful finite representation and G179's symbolic lift are separate facts. Do not promote hmax14 into an all-period estimate or interpret the context quotient as necessarily minimal.

**Requested static artifact, Local lane.** Export the existing RC2 certificates at q1,2,4,8 into one `rc2-certificate.json` artifact in the shared scratch, keeping numerical data outside Git. For each q supply root index; vertices with state(a,b) and one parent edge index (root null); edges with source/target vertex indices and integer delay; and all context label/value K rows, including labels with no outgoing arcs. A label is the ordered pair of RQO endpoint feature tuples. Record the artifact checksum and producing Git commit in the ledger. This is bounded certificate export from the existing computation, not a new research experiment or larger-period run; retain any export failure. If regeneration is needed because arrays were not retained, report that explicitly and keep the original RC2 caps, with no other exploration.

**GPT checker, predictions before execution.** Once that artifact is available, GPT will verify it without Local imports, potential optimization or quotient-cycle search. CV-C1 (known outcome expectation): reproduce Kmax14 and hmax14 at q8, and verify every nonnegative K value, actual consecutive-edge inequality, G179 lift and original one-edge inequality. Recompute labels with literal reset scans and binomial-substitution difference orders. CV-C2: validate each supplied parent edge and parent chain to the root, all compatibility equations, exact rotations and delays; check closedness at each supplied state by scalar enumeration of the256 possible q8 child words (smaller caps similarly), comparing the provided edge list. Parent reachability plus successor closedness certifies the entire finite reached domain; this is static certificate checking, not another graph construction or search. Odd zero-driver cap exits must be the explicitly negative free exits, not missing positive edges.

**Counterfactual and identified unexpected check.** Replacing every K value by zero must fail the known positive actual line arc from G178's contiguous segment. Removing one known actual edge must fail successor closedness. Require a K row for every edge label, even when it has no outgoing context arc; silently omitting terminal labels would invalidate the stopping argument. The reported hmax14 can be less than Kmax+11; the checker must compute the lift rather than force equality with that upper bound.

**Limits and reporting.** One GPT verification process,120 CPU seconds/128 MiB RSS, q<=8 only, no Bellman iteration, global graph search, q16 build or Local duplicate experiment. State coverage, static closedness and numerical inequalities must each be reported separately; any missing artifact, cap stop or failed check is not a pass. No new proof claim is filed until the artifact is checked. Local's successful controls and the held blind prediction remain retained even while independent verification is pending. Next progress should address compression or a mathematical size bound, not automatically enlarge the period after a barely compressed pass. NOT RUN.


**G181 outcome.** Artifact checksum, parent coverage, successor closedness and all context/lifted inequalities PASS at q1,2,4,8; corruption controls rejected. CV-C1/C2 held. Static verification completed; G182 records its exact finite conclusion.

### G182. RC2 finite reached-domain certificate independently verified (2026-10-07)

**Finite certificate theorem, second reader pending.** On the clock-aligned root-reached graphs at common caps q1,2,4,8, the exported RC2 certificate supplies nonnegative original vertex potentials h satisfying h(s)>=2*delay(s,t)-5+h(t) on every retained edge, with maxima0,0,1,14 respectively. Therefore every finite path segment remaining in the corresponding reached domain has doubled slope-5/2 reward at most that maximum, by telescoping. The q8 upper budget is14, or7 in undoubled arithmetic. This proves neither minimality nor any uniform all-period bound. A cap exit has reward-5 but the ensuing larger-period stage is outside this certificate.

**Artifact and provenance.** The static artifact `rc2-certificate.json` has56,232 bytes and SHA-256 f8d57126f5601ec41295db803ba13271ac54523e4b39a6c5a749b3f30e76a2a7. Local produced it with exporter commit c5d24a0, after regenerating the arrays because the original RC2 run retained none; L143 records that limitation and matching counts/maxima. The numerical data remains outside Git in the shared scratch. Git holds the producing source, checksum, independent checker and this conclusion. No claimed provenance relies on a flag's note.

**Independent verification of coverage and values.** GPT's `tests/probes/lexicon/rule30_rc2_certificate_check.py` imports no Local code and performs no Bellman iteration, potential search or graph-generation traversal. For each supplied vertex it validates the supplied parent chain to the constant root, and every supplied edge by literal compatibility, rotation and reset scans. It enumerates scalar candidate child words at each supplied state to verify successor closedness against the edge list; reachability plus closedness certifies the exact finite reached graph. A no-child state must be a zero driver with odd source parity, whose cap exit costs0/reward-5. Features use scalar resets, least pair period and independent binomial substitution at X=1 for temporal difference order.

Every K row is nonnegative, every actual consecutive-edge inequality holds, and every edge label is represented, terminal labels included. The G179 lift is computed explicitly and every original edge inequality checked. Confirmed counts (vertices/edges/context labels/actual arcs) are3/2/2/1,9/9/9/9,31/32/32/33,409/411/398/413. Confirmed K and h maxima are0,0,1,14 at the four caps. The checker verifies the artifact's summary against these computed values, not merely its printed assertions.

**Controls retained from G181.** Zero K fails a known positive actual context arc; deleting the known(143,26)->(134,186) edge fails successor closedness. Terminal labels are present. The identified unexpected strict-bound guard passes: q8 hmax14 is strictly below Kmax+11, so the checker does not mistake the reserve bound for an equality. Parent coverage, successor closedness and numerical inequalities all pass separately. GPT Intel static audit CPU0.1287 s/RSS14.4 MiB; Local's regeneration CPU0.01 s/RSS12.2 MiB is a separate run. CV-C1/C2 expectations hold; no failed check or partial stop is counted as a pass.

**Scope and closure of this block.** RC-P1's finite success is now independently verified, while its398/411-label caveat remains unchanged. This does not establish a small context family, bounded degree-independent memory, linear certificate magnitude at unbounded periods, period growth, arbitrary interior clocks or birth-clamped bounds. The gap-1 candidate-refinement loop stops here following CL011's coordination steer. Next GPT work is a reasoning synthesis of the compression failures, then the open period-growth obligation of G165; no new candidate family or larger-period job is launched.


### G183. Compression fails exactly at positive feature-balanced edge collections (2026-10-07)

**Symbolic synthesis, second reader pending; no run or new candidate family.** Let G be a finite directed graph of actual states and edges, with elapsed costs delta(e), and let phi map states to any finite set of retained labels. Fix slope gamma and reward w(e)=delta(e)-gamma. A finite potential F on labels satisfying

    F(phi(s))-F(phi(t)) >= w(s,t) for every actual edge s->t

exists if and only if there is NO finite multiset of actual edges with positive total reward and equal incoming/outgoing edge multiplicity at each LABEL. Balance is required at phi(s), not at the actual state s. Consequently a collection can obstruct this feature family even when its edges cannot concatenate into an actual history. This is the exact information-loss mechanism common to the recorded failures; it names a criterion on a chosen compression, not a universal theorem against every compression.

**Proof of obstruction and converse.** For a label-balanced multiset, sum its edge inequalities with their nonnegative integer multiplicities. Each label's potential cancels, giving0>=sum w, which contradicts positive reward. Conversely form the label multigraph with one arc phi(s)->phi(t) for each actual edge, retaining its reward. Any label-balanced edge multiset decomposes into directed label cycles by repeatedly following an unused outgoing edge until a vertex repeats and removing that cycle. Thus if its total reward is positive, at least one cycle has positive reward. A positive label cycle itself supplies a balanced multiset of actual representative edges. These equivalences do not assume actual-state joins.

If there is no positive label cycle, set H(x) to the maximum total reward of any finite label walk starting at x, allowing the empty walk. Every cycle has nonpositive reward; deleting cycles never decreases a walk's reward, so a maximum occurs on a simple path and is finite. Prepending an arc x->y gives H(x)>=w(x,y)+H(y), so H is a nonnegative feasible potential. Any other nonnegative feasible F bounds every starting walk by telescoping and F(end)>=0, hence F(x)>=H(x). H is the least nonnegative feature potential. Square. Arbitrary real finite potentials add no feasibility advantage: on this finite label set a constant shift makes them nonnegative without changing inequalities.

**What the records actually close.** G166 supplies a driver-only label loop and a phase-free balanced collection; G173 supplies exact-period same-label edges on every dyadic ambient cap q>=4, requiring slope>=3. G176's actually reached q8 edge requires slope>=5 for the three-distance-plus-period labels. G178 supplies a seven-edge collection balanced in distance-plus-order labels, elapsed21 over7 edges, requiring slope>=3. Its two false joins explain why the balance is not an actual cycle. G179 shows that a line graph formed after compression preserves the same balanced collection. RC2 avoids those known collections at q<=8 by retaining actual adjacency before compression, but G182's398/411 labels give no small uniform representation theorem. These are distinct domain and feature restrictions; none may be promoted to a claim that every lost observable is indispensable.

**Budget magnitude is a separate obligation.** Even if every q-level quotient has no positive cycles, an O(q) feature budget requires the maximum reward of ALL quotient walks to be O(q), by the least-potential characterization above. Existence alone gives no such estimate; walks may use joins impossible in the actual graph. On the uncompressed graph, uniform bounded debt B over every finite path is equivalent to a nonnegative vertex potential bounded by B: define h(s)=sup of rewards of finite paths starting at s, including the empty path, and prepend edges as above. Conversely telescope a bounded potential. This statement also holds on an infinite graph if B is genuinely uniform. The definition is a restatement of the debt bound, not a method to prove it. A single C shared across all histories is stronger than G165's permitted history-dependent constants; this synthesis does not silently strengthen that quantifier.

**Identified unexpected check against overgeneralization.** A generic three-state path s->t->u with rewards+1,-1 admits the noninjective label map phi(s)=phi(u)=A, phi(t)=B. Its label cycle has total0, and F(A)=1,F(B)=0 pays both edges. States were forgotten and a false join introduced, yet a bounded feature certificate exists. This is a weighted-graph logical control, not a new Rule30 witness. It refutes inferring 'every noninjective compression fails' from the selected positive examples. Likewise taking an already proved h as a scalar feature trivially yields a sound budget, but merely encodes the answer; one scalar is not automatically one small piece of information.

**Prior record and next direction.** G8/G166 already use the standard difference-constraints/positive-cycle criterion; this statement consolidates its representative-edge and uniform-size quantifiers for CL011. Primary prior art: MIT's difference-constraints lecture explains the corresponding negative-cycle criterion after reversing reward signs (https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/a9e76885a78c729f2375e14830caebf2_MIT6_046JS12_lec07.pdf, section7.2.2). No novelty claim. The gap-1 refinement loop remains closed. The next reasoning block is G165's independent period-growth obligation2^j/N_j->0; no new family, larger graph or run is queued.


### G184. Period-growth gap is an exponentially weighted stage-length condition (2026-10-07)

**Symbolic checkpoint, second reader pending; no run.** Fix one infinite admissible rooted history, with N_j the first node of least pair period2^j as in G165. Let ell_j=N_(j+1)-N_j be its spatial stage length, lambda_j=ell_j/2^j and R_j=N_j/2^j. G165's required sublinear period growth is exactly R_j->infinity. The entry recurrence becomes

    R_(j+1)=(R_j+lambda_j)/2,
    R_j=2^(-(j-J))*R_J + sum from i=J to j-1 of 2^(-(j-i))*lambda_i.

Thus the missing growth estimate is divergence of this exponentially weighted moving sum of normalized stage lengths. It is not merely divergence of absolute stage lengths, a large observed entry depth, or a geometric delay lower bound.

**Proof and useful sufficient condition.** N_(j+1)=N_j+ell_j gives the first identity after division by2^(j+1); induction gives the second. G165 already proves p_k=o(k) iff2^j/N_j->0, which is R_j->infinity. If lambda_j->infinity, then R_(j+1)>=lambda_j/2->infinity. More generally, for any fixed positive m and j>=J+m,

    R_j >= 2^(-m) * sum from i=j-m to j-1 of lambda_i.

Hence divergence of an unweighted sum over any fixed recent window of normalized stage lengths is sufficient. These are conditions to prove from compatibility, not estimates supplied here. Their constants and eventual thresholds may depend on the history, as G165 allows.

**Counterfactual: geometric delay alone is insufficient.** For a synthetic stage schedule with lambda_j=C>0 after J (choose integer C so ell_j=C*2^j are positive integers), the recurrence gives R_j=C+2^(-(j-J))*(R_J-C). Thus R_j tends to C rather than infinity, despite exponentially increasing absolute stage lengths and arbitrarily large initial R_J. Its period/depth ratio tends to1/C rather than0. This is a logical stage-schedule control, not a compatible Rule30 counterexample. It shows that a proof of ell_j>=c*2^j with fixed c would not by itself settle the growth target.

**Identified unexpected check: individual normalized stage lengths need not diverge.** In a synthetic integer schedule let lambda_j=1 at even j and lambda_j=j at odd j (after any finite prefix). Then R_j->infinity: if j-1 is odd, R_j>=(j-1)/2; if j-1 is even, the preceding odd term gives R_j>=(j-2)/4. Yet lambda_j remains1 at every even index. Therefore lambda_j->infinity is sufficient, not necessary; refuting that stronger condition would not refute period growth. The two-step recent-window sufficient condition covers this example. Conversely any finite prefix's contribution decays as2^(-(j-J)), so no finite delay record alone can force the limit.

**What the recorded depths say.** The certified unbranched small-cap prefixes give N_1=3,N_2=8,N_3=29,N_4=400, hence R_1=1.5,R_2=2,R_3=29/8,R_4=25. Their normalized completed stage lengths are lambda_1=5/2,lambda_2=21/4,lambda_3=371/8. These are existing G161/G165 and Local L115 records, not new measurements. The known period16 genuine branch at depth53208 preserves period16; it is NOT N_5. Later period16 branch examples likewise supply no certified period32 entry. No N_5 value or asymptotic stage-length estimate is inferred.

**Scope and next proof obligation.** The recurrence is elementary weighted summation applied to G165's reviewed dyadic stage structure; no novelty claim or new experiment. All controls here are algebraic synthetic schedules and explicitly lack Rule30 compatibility. A sufficient next lemma would bound actual normalized stage lengths from below by a quantity tending to infinity, or establish divergence of their recent-window sum on each admissible history. Genuine branch spacing from G159 does not imply this bound: same-period branches do not end the stage. GPT next examines constraints at consecutive odd zero-driver doubling events, reasoning first; no new gap-1 family or larger-period run is queued.


**G182 checker repair and review integration (Local L144; GPT, 2026-10-07).** Local independently verifies the finite certificate in S72 and promotes G182. It also identifies two limitations in GPT's original checker: the negative controls were logical proxies, not mutated artifacts passed through the validator; and `bit_count()` was unavailable on Python3.9. The original known-edge deletion would first break a supplied parent certificate, not reach the successor-closedness assertion. These corrections do not alter the independently verified positive certificate or its budget.

The checker now uses portable binary-string parity and actually validates corrupted copies in memory, bypassing only the checksum comparison for those deliberate mutations. Zero K is rejected by a context inequality; deleting the known tree edge with the child's parent pointer left stale is rejected by the parent certificate; deleting a non-tree edge and reindexing all surviving parent pointers is rejected by successor closedness. The first repair attempt replaced the tree edge by a duplicate existing edge and failed earlier at duplicate detection, so it did NOT pass the intended parent-control check. That failed control design was retained here and corrected to actual deletion. Both final suites pass on GPT's Intel host: Python3.14.7 CPU0.2743s/RSS16.2MiB; Python3.9.6 CPU0.5873s/RSS11.5MiB. All genuine certificate values remain0,0,1,14.

Local additionally reports an attained reward14 along eight reached edges at depths273..281, making the bound sharp on the finite q8 domain. That lower witness is Local's independently recorded S72 result, not newly reconstructed by GPT here. Local's question whether costly structures stay localized at large periods remains open. Such a compression would require a proved criterion locating every costly region and a bound on the intervening intervals; the q8 clustering observation alone supplies neither. No new gap-1 family or run is launched. The period-growth reasoning checkpoint G184 remains pending review.

## G185 — Maximal difference order can return three edges after a doubling

**Symbolic counterlemma, second reader pending; no computation.** G161's temporal-difference addendum gives a useful stage-entry fact: odd zero-driver integration at least period q creates a profile of order q+1 and least period2q. That fact does not supply a slowly recovering order deficit. For every dyadic q>=4 there is an ambient gated compatible prefix whose new period2q stage reaches maximal difference order2q in three further spatial edges. One of those edges raises the maximum order of the pair by q-1. Rooted ancestry of this family is NOT established.

**Construction and entry.** Write temporal words in increasing time order, with S w(t)=w(t+1), Delta=I+S, and nu(w)=min{k>=0:Delta^k w=0}. Thus nu(0)=0 and nu(1)=1. On a2q-cycle take

    c = 0^(q-2) 1 0  1^(q-2) 0 1,
    a = Delta c,   e = 1 XOR S^(-1)c.

The second q-block of c complements the first, so a repeats every q letters. Its q-block has exactly three black cells, at q-3,q-2,q-1. Odd parity on a dyadic cap gives nu(a)=q and least period q: Delta^(q-1)a is constant1, whereas Delta^q a=0. Also Delta c=a gives nu(c)=q+1 and least period2q. These are the previously recorded integration identities, not a new stage-entry theorem. The compatible word prefix is

    a, 0, c, 1, e, f,

where f is the unique2q-periodic child of (1,e). Compatibility means S z=x XOR(y OR z) for three successive words x,y,z. The first triple is Delta c=a. For (0,c,1), constant1 satisfies the equation and c is a nonzero reset driver. For (c,1,e), S e=c XOR1. Finally f satisfies S f=1 XOR(e OR f), with a unique periodic solution because e has black reset cells. Choose arrival phase r=q-2 at the source (a,0); then a(r-1)=1. G160's gate is preserved along this prefix with the ordinary reset-clock updates. This certifies gated compatibility, without any root-start clock claim.

**Counting the last profile.** The cyclic white-run lengths of e are q-2,1,1, and its black-run lengths are the same. At a black e cell the recurrence forces the next f cell to0. Across a white e run of length ell, f alternates, starting at0, up to and including the next black e position. That disjoint interval contributes ceil(ell/2) black f cells. Hence one2q-block of f has weight

    (q-2)/2 + 1 + 1 = q/2 + 1.

For dyadic q>=4, q/2 is even, so this weight is odd. Consequently nu(f)=2q and f has least period2q. Shifts preserve nu, and adding the order-one constant to the order-(q+1) word cannot cancel its highest nonzero difference, so nu(e)=q+1. The successive pair maxima after the entry (0,c) are therefore

    q+1, q+1, q+1, 2q

at (0,c),(c,1),(1,e),(e,f). In particular the final edge raises that maximum by q-1, an unbounded jump as q grows. Rotating each pair to its actual arrival phase leaves these orders unchanged.

**Independent literal control, by substitution.** At q=4 the time-ordered words a,c,1,e,f on the cap8 are respectively01110111,00101101,11111111,01101001,01001010, or integer masks238,180,255,150,82 with time0 in the low bit. The q-block of a is0111. For the last triple e OR f=01101011 and S f=10010100, its complement, so the scalar equation holds. The orders are4,5,1,5,8, and f has three black cells. This is a hand substitution control independent of the general run-count argument; no census or measured run is reported. The q=2 case is excluded: its proposed q-2 run is empty and the evenness argument does not apply.

**Counterfactual and identified unexpected guard.** The assertion that every compatible edge raises the pair's difference order by at most one is false on the gated ambient domain. Only the zero-driver integration step has the recorded exact +1 relation. However, restoring maximal order does NOT end the stage: all three further pairs still have least period2q, their drivers are nonzero, and no next odd zero-driver event has been supplied. Thus this family neither realizes a short doubling-to-doubling stage nor refutes rooted period growth. It closes a blanket order-recovery shortcut, while leaving a root-specific restriction or a genuine bound on the distance to the next zero driver open.

**Existing record and next intention.** G161's difference addendum and G162 already separate order, period and reset cost; G178 retains order labels yet still loses actual adjacency. G184 identifies divergence of normalized stage delays as the missing growth statement. The present algebraic control adds no timing certificate, new experiment or prize claim. Next reasoning should use the actual zero-driver hitting condition along an admissible rooted history; an order deficit alone is insufficient on the larger compatible domain. Gap-1 refinement stays closed and Local's status-board contraction remains theirs.

**G185 continuation: zero-hit condition and a failed autonomous half-difference shortcut (2026-10-07; symbolic, no run).** The next child of (a,b) is0 exactly when a=b, by direct substitution in S c=a XOR(b OR c). The last five profiles before any nonzero zero-driver event are consequently

    u, Delta b, b, b, 0,    u=b AND NOT(S b).

Indeed the predecessor map B(a,b)=(S b XOR(a OR b),a) sends (b,0) to (b,b), then to (Delta b,b), then to (u,Delta b). The last identity uses S b XOR((Delta b) OR b)=b AND NOT(S b). This is an explicit form of the existing inverse/reset mechanism, not a new hitting-time bound. At an odd zero source of dyadic least period Q, b has nu(b)=Q and Delta b has nu=Q-1. The actual hitting condition is equality of adjacent words, not merely these orders. G166 already uses the equal-driver terminal pair; no rediscovery claim is made.

For period-growth reasoning let Q=2q, T=S^q and define the half-differences alpha=a XOR(T a), beta=b XOR(T b). In GF(2) notation pointwise multiplication is AND. The exact BACKWARD defect update under B is

    alpha_new = S beta + alpha + beta + a*beta + b*alpha + alpha*beta,
    beta_new = alpha.

This follows by expanding x OR y=x+y+xy on the two temporal halves. The terms a*beta and b*alpha retain background information: the half-differences alone need not determine their next backward values. At a doubling entry (0,c), T c=1+c, so (alpha,beta)=(0,1) and this update gives(0,0), exactly the preceding smaller-period pair. At an odd zero source (b,0), the first half-difference has odd parity on a q-block because that parity equals the parity of the full2q-block of b. For dyadic q>=2 it therefore has order q; it cannot be constant1, whose q-block parity is even. These two endpoint facts do not bound the distance between them.

**Identified unexpected control against dropping the background.** On cap4 choose a=0011 in increasing time order and compare b=0000 with b=1111. Both pairs have least period4, both have half-differences(1111,0000), and both satisfy G160's active-source gate at r=0 because a(3)=1. But B(a,0)=(a,a) has defects(1111,1111), while B(a,1)=(0,a) has defects(0000,1111). Thus even on the gated ambient domain the proposed autonomous backward evolution of these defects is false. Rootedness of these two sources is not asserted, so this does not exclude a root-specific closure lemma. Nor does a backward countercontrol establish anything about arbitrary forward defect evolution. The failed shortcut is retained; no new potential family, computation or status-board row is opened. Next useful obligation remains a rooted estimate for distances between actual odd zero-driver hits.

**Backward half-difference kernel check (2026-10-07; continuation, no run).** The same equation recovers the known period-halving mechanism without assuming rootedness. If both output half-differences vanish then beta_new=alpha forces alpha=0. The remaining equation is S beta=(1+a)*beta. If a has any black cell it resets beta to0, which then persists; periodicity forces beta=0 everywhere. Thus a genuinely non-q-periodic input can map to a q-periodic predecessor only when a=0. Then S beta=beta, so the nonzero beta is constant1: the second profile has complementary q-halves. Conversely a=0,beta=1 indeed gives zero output defects. This is G157-G158's existing integration/halving classification checked through the defect equation, not a new result. The identified quantifier guard is that recognizing a halving edge gives no estimate of how many intervening edges occur between successive halvings. No normalized-stage lower bound was obtained in this reasoning block; no computation is proposed on that basis.

**G184 continuation: no fixed recent window is necessary (2026-10-07; algebraic control, no run).** The fixed-window sufficient criterion must not become an additional obligation. Consider a synthetic integer stage schedule with lambda_j=1 except at j_k=2^k, where lambda_(j_k)=2^(2^(k+2)). All ell_j=lambda_j*2^j are positive integers. For j_k<j<=j_(k+1), the contribution of the most recent exceptional stage gives

    R_j >= 2^(-(j-j_k))*lambda_(j_k) >= 2^(3*2^k).

Hence R_j tends to infinity. But for every fixed positive m, at j=j_k+m+1 with k sufficiently large, the last m normalized lengths are all1 and their sum is m. No fixed recent-window sum diverges. This is a synthetic schedule, not a compatible Rule30 history, and it refutes only the logical necessity of the convenient sufficient condition. It does not refute G184's exact exponentially weighted criterion. The identified unexpected check is that even arbitrarily long intervals of bounded normalized lengths can coexist with sublinear period growth when preceding deposits are large enough; decay by repeated halving does not force a fixed-window test to be necessary. No estimate for actual stage lengths or new experiment follows.

**GPT scope clarification after L146 (2026-10-07; existing theorem, no run).** The unbounded-period premise on an infinite ROOTED history is already proved in G165's equivalent period-growth checkpoint, using G7/G156. For completeness, a pair at depth k has first backward zero-hit time k+1 under B; therefore two distinct depths cannot have the same pair. If all periods were bounded by a fixed dyadic Q, all pairs would lie in the finite set of4^Q Q-periodic binary pairs, contradicting this injectivity along an infinite history. Rotation classes strengthen the same argument but are not needed. Ambient B-cycles such as G156's period-two example do exist; they are excluded by rooted first-hit times, not by a global acyclicity assertion. Thus every infinite admissible rooted history has all dyadic entries N_j, and no additional bounded-period cyclic rooted case remains to classify. This settles the scope question, not the growth rate. From the shared period16 prefix, the conservative reviewed bound N_5>=53208 implies lambda_4>=(53208-400)/16=6601/2 and R_5>=53208/32=6651/4; neither is the unknown exact entry. These are finite lower bounds, not asymptotic estimates.

**GPT incorporation of L147 (2026-10-07).** Local S75 independently verifies the family for q4 through64 and locates the q4 member on the rooted history at depths28 through32, with arrival phases shifted by5 on the cap8 cycle. Thus the rooted period8 stage starts at depth29 with order5 and reaches order8 at depth32; the stage continues through its zero-driver exit at depth399. Rootedness for the larger members remains unproved here; the q8 member is not the rooted cap16 exit word, as Local observes. At q2, direct substitution gives c=1001, a=1010, e=0011, f=0100, with f of weight1/order4. So the order conclusion survives, although the three-run proof degenerates. The stated arrival choice r=q-2=0 fails its gate since a(3)=0. The theorem retains q>=4; the q2 exclusion is not an assertion that maximal order fails to return. Local's verified filing is preserved.

**G184 prior-art spacing checkpoint (2026-10-07; no run).** Rechecked Nersissian, Diagonal Periods and Newton Supports of Rules30,86,135, arXiv2609.25077v1, sections4.4 and7 (https://arxiv.org/html/2609.25077v1). Section7 leaves record spacing open. Section4.4's milestone polynomial is a formal model, not a physical-diagonal annihilator or justified derivative law. Its first indices4,9,30,401 match our shared entries3,8,29,400 after an offset; the later natural-orbit record87868 is not independently verified here or transferred to every rooted branch. The proposed2107985256 is explicitly unestablished. This is the unexpected indexing/quantifier guard, not new evidence for N5. No quantitative stage-length bound was found in this bounded primary-source check; reset/halving facts already credited in G156-G161 remain unchanged.

**G184 continuation: every-history growth does not automatically give a uniform minimum (2026-10-07; synthetic tree control, no run).** A sufficient strengthening would show inf_history N_j/2^j tends to infinity. It must not be mistaken for a necessary reformulation of G165's history-by-history condition. Consider a binary comb of synthetic dyadic-stage schedules. Its backbone has N_j=4^j for j>=1. At the distinct backbone depth4^k+1 allow a same-period fork into an offshoot indexed k>=1. The offshoot shares N_j=4^j through j=k, takes ell_j=8 for k<=j<2k, then takes ell_j=4^j for j>=2k. It never forks again. All changes of period are single doublings at stage boundaries; branch depths on the backbone are more than seven apart. These assignments define a locally finite acyclic tree with only the backbone and one eventual offshoot for each k as infinite paths; all bounded-period prefixes are finite. They do not assert Rule30 compatibility or literal reset profiles.

Every path separately has R_j=N_j/2^j tending to infinity. On the backbone R_j=2^j. On a fixed offshoot, for j>2k, N_j>=ell_(j-1)=4^(j-1), so R_j>=2^(j-2) eventually. Nevertheless at j=2k the kth offshoot has

    N_(2k)=4^k+8k,    R_(2k)=1+8k/4^k.

Thus the whole-tree minimum does not tend to infinity. The identified unexpected check is that local finiteness, absence of bounded-period infinite paths, and widely separated binary forks all hold in this control: those qualitative facts do not upgrade pointwise divergence to uniform divergence. This is a quantifier countercontrol, not a counterexample to Rule30 growth. A uniform lower-bound proof would still be sufficient and useful, but failing that stronger goal would not settle any individual history's asymptotic behavior. No new lead row, computation or prize claim follows.

**Finite-history control.** If the admissible family has only finitely many infinite histories and each satisfies R_j->infinity, then its minimum does tend to infinity: for any threshold A choose an eventual index for each history, then take the largest of finitely many indices. For example a rooted tree with a uniform finite bound on the number of binary decisions per path has finitely many infinite histories. The synthetic comb avoids this conclusion because its backbone passes infinitely many fork opportunities. This is a logical distinction, not a claim about the number of future genuine Rule30 branches. The necessary research target remains the original history-by-history condition; a uniform estimate is a sufficient strengthening.


## G186 — Arbitrarily good prefix depths suffice for the Thue–Morse reduction (2026-10-07)

**Conditional lemma, second-read by Local L151; reasoning only.** Fix one admissible rooted history and a fixed left-edge distance L. Let p(M) be its nondecreasing least common prefix period. Suppose its entire-prefix settling bound satisfies

    tau(M) <= gamma*M + A*p(M) + B,
    1 <= gamma < 3,  A >= 0,

with finite constants A,B along this history. Then liminf as M tends to infinity of p(M)/M equal to0 suffices for the unbounded Thue–Morse repeat contradiction of G2.4. A full limit p(M)/M ->0 is not required for this application. This supplies no actual growth or settling estimate for Rule30.

**Proof, including endpoint rounding.** Choose a fixed theta with 2<theta<6/gamma; then theta<6. Take integer depths n_s tending to infinity with p(n_s)/n_s ->0. Choose the largest nonnegative integer k_s for which M_s=ceil(theta*2^k_s)<=n_s, and put P_s=p(M_s). Such a k_s exists eventually and tends to infinity. Maximality gives

    n_s < ceil(2*theta*2^k_s) <= 2*theta*2^k_s + 1.

Monotonicity gives P_s<=p(n_s), hence P_s/2^k_s ->0. Also M_s=theta*2^k_s+O(1). The three G2.4 requirements now hold eventually: M_s<6*2^k_s because theta<6; tau(M_s)+P_s<=6*2^k_s because gamma*theta<6 and (A+1)*P_s+B+O(1)=o(2^k_s); and M_s>=L+2*2^k_s+2*P_s because theta-2>0. Substitution in G2.4's A⁗ inequality gives its one-cell contradiction at arbitrarily large scales. Every endpoint uses the settling bound and period from this SAME history. To exclude the code for every admissible left side, the assumptions must hold separately on every such history; constants may depend on the history.

**Stage-entry reformulation.** For the infinite rooted dyadic histories of G165, all entries N_j exist and p(M)=2^j for N_j<=M<N_(j+1). Write R_j=N_j/2^j as in G184. Then

    liminf_M p(M)/M = 0  if and only if  limsup_j R_j = infinity.

For the reverse implication, evaluate p(M)/M at entries N_j along an unbounded R_j subsequence. For the forward implication, a good depth n in stage j obeys N_(j+1)>n, so R_(j+1)>n/(2*p(n)); this is unbounded along the good-depth subsequence. Its stage indices tend to infinity because every fixed stage is finite. Thus, conditional on G165's uniform stage debt bound at slope gamma<3, unbounded R_j suffices for this Thue–Morse application: G165 supplies A=2*(C+1), with any fixed normalization offset absorbed in B. G165's stronger all-depth sublinear-period conclusion and G184's equivalence for a FULL limit remain unchanged.

**Independent margin control and counterfactual.** At gamma=5/2, theta=11/5 gives gamma*theta=11/2<6 and theta-2=1/5. Thus the time margin is half the dyadic scale and the endpoint margin is one fifth; both absorb any fixed B,L and vanishing relative period. If periods were not monotone, moving a good endpoint backwards could destroy its small period. The proof uses the reviewed predecessor-divisibility property, rather than assuming sparse depths align with repeat scales.

**Identified unexpected check: the weakened growth condition is strictly weaker.** This is an algebraic synthetic schedule, NOT a Rule30 history. Start N_1=2 and use the G184 recurrence R_(j+1)=(R_j+lambda_j)/2 with lambda_j=1 except at j_k=2^k, k>=1, where lambda_(j_k)=2^(2^(k-1)). Set each integer stage length to lambda_j*2^j. Immediately after a spike, R_(j_k+1)>=lambda_(j_k)/2, so limsup R_j=infinity. Before the next spike, at j=j_(k+1), the baseline contributes1 and the k earlier spikes contribute in total at most k*2^(-2^(k-1)): each contribution is bounded by 2^(3*j_h/2-j_(k+1))<=2^(-j_k/2). Hence R_(j_(k+1))->1. Consequently p(M)/M has liminf0 but does not tend to0, as evaluating at these latter entries shows. Unlike G184's previous oversized-deposit control, these deposits decay before the next spike.

**Prior record, scope and next intention.** G2.4 supplies the repeat criterion; G165 supplies conditional birth timing and monotone dyadic periods; G184 supplies the exact stage recurrence. This is an elementary subsequence application, with no literature novelty or computation claim. Neither the stage debt hypothesis nor even the weaker growth condition is proved on actual histories. No paperfolding claim or prize conclusion is added. Local: please second-read the endpoint selection, the equivalence and the strictness control; no run requested. GPT next seeks actual odd-zero hitting constraints strong enough to force unbounded R_j on each history.


**G186 continuation: the recorded paperfolding repeats also suffice (GPT, 2026-10-07; second reader pending, no run).** The initial G186 statement concerned only Thue–Morse. RULE30-PRIZE.md section8.59 also records paperfolding repeats with i=s, i'=3*s and ell=2*s-1 at dyadic scales s. Apply A⁗ to the same adjacent pair (-1,0) at distance L-1, with a=2*s, a'=6*s and n=2*ell=4*s-2. Its endpoint and one-cell contradiction requirements become

    M < 4*s,
    tau(M)+P <= 6*s,
    M >= L+2*s+2*P+2.

Indeed these give 4*s-2 <= L-1+6*s-M+2*P <= 4*s-3, impossible. The lost repeat symbol contributes the additional2 in the lower endpoint requirement; the later start contributes the stricter upper endpoint4*s, not6*s.

Under G186's SAME history-specific settling bound and liminf p(M)/M=0, choose theta with 2<theta<min(4,6/gamma). This interval is nonempty for 1<=gamma<3. The already proved endpoint selection gives M=ceil(theta*s), P/s->0 and arbitrarily large dyadic s. The strict positive margins 4-theta, 6-gamma*theta and theta-2 absorb all fixed offsets and the extra2. Thus the conditional sparse-depth criterion excludes the recorded paperfolding code as well as Thue–Morse. No new repeat theorem is proved here: the application uses exactly the recorded section8.59 repeats and A⁗, with the original timing/settled-band assumptions.

**Independent offset control and identified unexpected check.** Put L=1, s=8, P=1 and M=21, and assume tau(21)+1<=48. The upper endpoint is21<32, the lower threshold is1+16+2+2=21, and the A⁗ right side is1-1+48-21+2=29 whereas n=30, the desired one-cell contradiction. Reusing the Thue–Morse lower threshold would allow M=19, giving right side31 and NO contradiction. This literal arithmetic control retains the two-cell correction instead of treating the two repeat families as identical. No actual settling-time measurement is claimed by this assumed-timing control. The unresolved stage budget and actual unbounded stage-entry ratios remain necessary proof obligations for this route; no prize claim. Local: review the additional start-time and length offsets, no new job.


## G187 — A positive period/depth threshold suffices for both repeat reductions (2026-10-07)

**Conditional quantitative lemma, second-read by Local L152; no GPT run.** Fix a left-edge distance L and one admissible rooted history with nondecreasing common prefix period p(M). Suppose its entire-prefix settling bound is

    tau(M) <= gamma*M+A*p(M)+B,
    1 <= gamma < 3, A >= 0,

with finite constants A,B on that history. Define

    delta = (3-gamma)/(2*gamma+2*A+8).

Then liminf p(M)/M < delta suffices for G2.4's unbounded Thue–Morse repeat contradiction. For the recorded paperfolding repeats, the sufficient condition is liminf p(M)/M < min(delta,1/6). In G165's application A=2*(C+1)>=2, so delta<=1/7<1/6 and the SAME delta suffices for both codes. This complements G186: for a specified budget it weakens the sufficient growth condition. G186 remains useful when only existence of a finite budget constant is known. Neither lemma proves an actual budget or period estimate.

**Endpoint construction and proof.** Choose a number r strictly between the liminf and the relevant threshold. Along arbitrarily large integer depths n, let q=p(n)<=r*n. Put D=L for Thue–Morse and D=L+2 for paperfolding, and choose the largest dyadic s for which 2*s<=n-2*q-D. Such a scale exists eventually. Then

    s > (n-2*q-D)/4,
    M = 2*s+2*q+D <= n,
    P = p(M) <= q.

Thus s tends to infinity, and limsup along these chosen depths of q/s is at most 4*r/(1-2*r). Direct rearrangement shows

    r < delta  iff  4*r/(1-2*r) < (6-2*gamma)/(2*gamma+A+1).

Consequently

    tau(M)+P <= 2*gamma*s+(2*gamma+A+1)*q+gamma*D+B < 6*s

eventually, by a strict linear margin in s. For Thue–Morse, r<delta<=1/5<1/4 implies q/s<2 eventually, hence M<6*s. For paperfolding, r<1/6 implies q/s<1 eventually, hence M<4*s. All fixed D and B are absorbed by those strict margins.

For Thue–Morse, the G2.4 A⁗ right side is at most L-1+6*s-M+2*q=4*s-1, below its repeat-run length4*s. For paperfolding the same expression is4*s-3, below repeat-run length4*s-2. Both contradictions use exactly the repeats and timing hypotheses already recorded in G2.4 and G186's section8.59 continuation. To exclude either code for every admissible left side, this quantitative condition and the settling budget must hold separately on every such history, with history-dependent constants allowed.

**Exact dyadic stage interpretation.** In G165's rooted stage structure the last depth m_j=N_(j+1)-1 minimizes p(M)/M within stage j. Its value is

    p(m_j)/m_j = 1/(2*R_(j+1)-2^(-j)).

Every stage is finite and its index tends to infinity with depth. Thus taking the liminf of these stage minima gives the exact extended-real identity

    liminf_M p(M)/M = 1/(2*limsup_j R_j),

with 1/infinity=0 and 1/0=infinity. The vanishing subtraction2^(-j) does not affect the denominator's limsup; inversion exchanges positive limsup and liminf, including these limiting cases. Hence the displayed quantitative condition is equivalent to limsup R_j>1/(2*delta). The factor2 comes from using the END of a stage, just before the next doubling, rather than its entry. For G165 at gamma=5/2 and C=1, A=4 and delta=1/42. Entry ratios above21 by a fixed margin at arbitrarily large indices therefore suffice for BOTH repeat applications, conditional on that stage budget. No such actual asymptotic statement is established.

**Independent integer control.** Hypothetically take L=1, B=0, gamma=5/2, A=4, n=1000 and q=16. For paperfolding D=3; the selected s is256 and M=547. The assumed bound gives tau(M)+P<=1447.5<1536=6*s, and M<1024=4*s. The A⁗ right side is at most1021 against repeat-run length1022. The same endpoint also works for Thue–Morse, whose run length is1024. This verifies the arithmetic under the stated assumptions; it is NOT a settling measurement or a certified C=1 budget on a Rule30 history.

**Identified unexpected strictness/control check.** If q/s equals (6-2*gamma)/(2*gamma+A+1), the scale-dependent time margin vanishes. A positive gamma*D+B then prevents the required timing inequality: this argument cannot replace its strict threshold by a non-strict one. Moreover the synthetic schedule N_j=25*2^j has constant R_j=25 and integer stage lengths25*2^j; it satisfies the gamma=5/2,C=1 entry threshold while p(N_j)/N_j=1/25 never tends to0. Its stage-end ratios tend to1/50. At period16, the entry depth400 has ratio1/25 above1/42, but the last stage depth799 has ratio16/799 below1/42. Thus G186's unbounded-ratio condition is sufficient but not necessary for the conditional application. This schedule has no asserted Rule30 compatibility.

**Prior record and next intention.** This is a quantitative endpoint selection using reviewed G165 timing, G184 stage notation and the pending G186 repeat applications; no novelty or computation claim. A finite large entry such as the conservative N_5 lower bound does not establish arbitrarily many useful scales. The actual target can now be a history-specific positive period/depth threshold tied to its stage-debt constant, rather than unbounded R alone. Both linked obligations remain open. Local: please second-read the threshold algebra and scope, together with G186; no run requested. GPT next examines what actual odd-zero hitting constraints could maintain or recurrently recover such a threshold.


**G187 continuation: align the repeat scale with the dyadic period (GPT, 2026-10-07; second reader pending, no run).** The general sparse-depth threshold is sufficient but can lose room by treating periods as arbitrary integers. In G165's actual stage structure, let q=2^j and choose a FIXED power of two K with

    K > (2*gamma+A+1)/(6-2*gamma).

For the paperfolding application also require K>1. With G165's A=2*(C+1)>=2 and gamma>=1, the displayed fraction is at least5/4, so its smallest admissible dyadic K automatically meets this additional requirement. Then

    limsup_j R_j > K+1

suffices for both repeat contradictions, conditional on that same history's settling budget. At infinitely many stages the next entry obeys N_(j+1)>2*(K+1)*q+D, where D=L for Thue–Morse or L+2 for paperfolding, because the limsup inequality has a fixed positive margin and q tends to infinity. Set s=K*q (a valid dyadic repeat scale) and M=2*(K+1)*q+D. Since M<N_(j+1), its common prefix period P is at most q, whether M falls in the q-stage or an earlier stage. The settling bound gives

    tau(M)+P <= [2*gamma*(K+1)+A+1]*q+gamma*D+B < 6*K*q = 6*s

eventually. The strict coefficient gap is (6-2*gamma)*K-(2*gamma+A+1)>0. Also M<4*s eventually when K>1, hence the paperfolding upper endpoint holds; this also implies the Thue–Morse upper endpoint M<6*s. Both lower endpoints and the one-cell contradictions follow from the same M=2*s+2*q+D construction in G187. This proves the claim without assuming liminf period/depth zero, or measuring any new stage length.

**Independent coefficient control and identified unexpected comparison.** For the hypothetical gamma=5/2,C=1 budget, A=4 and the coefficient fraction is10. Choose K=16; the sufficient entry threshold is now17 rather than G187's general21. At q=16,L=1,B=0 the paperfolding endpoint is again M=547,s=256, and the timing margin is6*q-7.5=88.5, agreeing with the earlier literal control. A synthetic constant schedule N_j=18*2^j has R_j=18 and stage-end period/depth ratios tending to1/36. It passes this new threshold but fails the earlier sufficient condition liminf period/depth<1/42. Thus the improvement is strict as a reduction; no Rule30 compatibility or actual C=1 budget is asserted. Choosing K=8 instead would give a negative coefficient gap8-10=-2, so the next smaller dyadic scale is not licensed by this bound. If the fraction itself is a power of two, equality still leaves no positive margin for offsets: choose the next power. No optimality claim is made for other endpoint strategies or stronger timing information.

**Handoff.** This is a refinement of the same pending G187 proof, not a new growth estimate or a reopened gap-1 family. Local: include the dyadic scale choice and the earlier-stage prefix-period guard in the second read; no job requested. The remaining actual obligation is a recurrent entry-ratio margin linked to the history's uniform stage-debt constant. Finite large entries alone still supply no such recurrence.


**GPT incorporation of L151-L152 (2026-10-07; no new run).** Local independently verifies G186, its paperfolding offsets, G187 and its dyadic-scale refinement (S76-S79); the verified filings and second-reader notes are preserved in PROOFS.md. Adopt L152's wording: G187 complements G186, because its finite threshold is linked to a quantified budget constant. G186's unbounded normalized-stage-length route remains useful when only existence of some finite budget constant is proved.

The recorded R_4=25 and conservative R_5>=6651/4 clear the hypothetical C=1 thresholds on the growth side. The rooted finite q<=8 certificate is consistent with C=1 at slope5/2, whereas a corresponding period16 stage budget is not measured here. Thus these are two favorable finite growth ratios, not two verified joint asymptotic applications. The identified scope check is that replacing an unknown C by the small-cap value would silently strengthen the evidence. No actual large-period timing or growth estimate is added. Next reasoning keeps Local L151's unbounded normalized-stage-length target, or a quantitatively linked recurrent threshold; a numerical target17 alone is not justified without C control. No new gap-1 family or larger-period computation is requested.


## G188 — A doubled stage of period at least four cannot return to zero within eight steps (2026-10-07)

**Local zero-return lemma, second reader pending; symbolic, no run.** Consider an odd zero-driver integration that doubles period from q/2 to q>=4. Write its following compatible temporal profiles as

    0, c, 1, e, f, g, h, i, ...,

with S w(t)=w(t+1), Delta=I+S over binary XOR, and T=S^(q/2). Integration gives T c=1+c. Then none of profiles at positions1 through8 after the displayed initial zero can be identically zero. Thus the first subsequent zero is at position at least9. On a rooted history, every stage entered by doubling to q>=4 has length at least9. This is a CONSTANT bound; it gives no positive lower bound on normalized stage length as q grows.

**The first six positions.** The reset equations force the next profile to1 and S e=1+c, equivalently e=1+S^(-1)c. G159's direct six-position calculation applies because the pre-integration source Delta c has least period q/2>=2 and is nonconstant. Its only earlier-zero exception would require that source to be constant1. Therefore c,1,e,f,g,h are nonzero. This uses the already reviewed local proof, not its even-branch hypothesis: nonconstancy excludes the same exception here.

**Position7 cannot be zero.** If i=0, compatibility forces g=h. The equations for g and h then give S g=f+g and e=f*g (pointwise product). Since e is contained in f, the f equation reduces to S f=1+f. Thus f alternates, g integrates that alternating word, and g is a rotation of0011 repeated. The word e=f*g has exactly one black cell per four positions. Therefore c=1+S e has least period4 and three black cells per four positions. But an entry word c of least period q with complementary q/2 halves has exactly q/2 black cells. Here q must be4 and the required weight is2, contradicting3.

**Position8 cannot be zero.** Suppose the profile after i is0; then h=i. The equations for h and i give g=Delta h, and comparison with the h equation gives f=g*h. Since f is contained in g, the g equation gives e=Delta g=Delta^2 h. Put x=h(t), y=h(t+1), z=h(t+2). The f equation reads

    y*(1+z) = 1 + [(x+z) OR x*(1+y)].

Its allowed triples are001,010,011,100,101. No periodic or bi-infinite word satisfying these constraints can contain11: both110 and111 are forbidden. Hence011 is also absent, and h has no adjacent ones and no three consecutive zeros. The shifted word T h has the same two properties.

Now beta=h+T h obeys Delta^2 beta=1, because e+T e=1 follows from c+T c=1. Thus beta(t+2)=1+beta(t): beta is a rotation of0011 repeated. Choose a phase with five successive beta bits11001. At the second position, h and T h differ; absence of adjacent ones forces their common bit at the third position to0. At the fifth position they also differ, forcing their common fourth-position bit to0. Absence of000 now forces BOTH second-position bits to1, a contradiction. This excludes position8.

**Independent literal control and identified unexpected exception.** The seven-step compatible zero return

    a=0110, 0, c=1101, 1=1111, e=0001,
    f=0101, g=0011, h=0011, 0

uses increasing temporal order on cap4. Direct substitution gives Delta c=0110, S e=0010=1+c, S f=1010=1+(e OR f), S g=S h=0110, and the last equal pair produces0. It has an EVEN pre-integration source and no complementary halves in c, so it does not refute the lemma. Rootedness of this control is not asserted. The q=2 exception is essential: the compatible prefix0,01,11,01,01,0 returns to zero in five steps after constant-one integration, as already recorded in G159. The new assertion keeps q>=4. These literal checks independently guard against extending the result to all zero-driver events or to the smallest doubling.

**Prior record and scope.** G157-G159 supply reset, integration and the six-position guard; G185 shows difference order can recover rapidly without ending a stage. The present short-return exclusion uses actual compatibility and complementary temporal halves, rather than an autonomous order or half-difference model. Neither rooted reachability of the control nor attainment at position9 is claimed. The bound9/q tends to0: this result does NOT establish the unbounded normalized lengths of G186/L151, or the budget-linked recurrent thresholds of G187. No literature novelty, computation or prize claim. Local: please second-read the two return equations, especially the five-position beta contradiction; no job requested. Next useful task is whether longer return constraints yield a period-dependent obstruction, rather than extrapolating this constant bound.


**G188 continuation: positions9 and10 are also impossible (GPT, 2026-10-07; second reader pending, hand algebra only).** These two exclusions require only a nonzero initial c, which forces the following profile to1; they do not require complementary halves. Together with the initial G188 argument, a period-doubling entry of least period q>=4 has no subsequent zero in positions1..10, so its first return and its stage length are at least11. This remains a constant bound, not a normalized-stage estimate.

Define, for three consecutive bits x,y,z of a temporal word w,

    E(x,y,z) = x+y+z*(1+x)*(1+y),

where additions are XOR and products are AND. In the order000,001,010,011,100,101,110,111, its values are0,1,1,1,1,1,0,0. This function arises directly by eliminating the four profiles before a repeated pair (w,w): they are E(w), Delta^2 w, w*Delta w, Delta w, followed by w,w. Here E(w)(t)=E(w(t),w(t+1),w(t+2)). Indeed the closest equations first give Delta w, then w*Delta w, then Delta^2 w, and the next gives S(w*Delta w)+(Delta^2 w OR w*Delta w)=E(w).

**Return at position9.** In 0,c,1,e,f,g,h,i,j,0, the repeated pair i=j=w forces h=Delta w, g=w*Delta w, f=Delta^2 w and e=E(w). The remaining equation for f is

    S(Delta^2 w) = 1 + (E(w) OR Delta^2 w).

For x=w(t), y=w(t+1), z=w(t+2), v=w(t+3), this fixes v uniquely. The resulting triple-state transitions are

    000 -> 001 -> 010 -> 101 -> 010,
    011 -> 111 -> 110 -> 101,
    100 -> 000.

These lines include all eight states. The only cycle is010 <->101, so every periodic w satisfying the equation alternates. Then e=1 and c=1+S e=0, contradicting the nonzero entry. Merely finding a cycle of the necessary temporal map is insufficient: the entry condition must still be checked.

**Return at position10.** In 0,c,1,e,f,g,h,i,j,k,0, the repeated pair j=k=w instead forces i=Delta w, h=w*Delta w, g=Delta^2 w and f=E(w). With e=S g+(f OR g), the remaining f equation reduces to

    if E(x,y,z)=1: E(y,z,v)=0;
    if E(x,y,z)=0: E(y,z,v)=1+x+y+z+v.

Its ONLY allowed triple-state edges are

    011 -> 110 or111,  111 -> 110,  110 -> 100,  100 -> 000.

State000 has no outgoing edge; states001,010,101 likewise have none. This graph has no cycle, so no periodic temporal word can satisfy the return equation. In fact it has no infinite path, even without periodicity. This excludes position10.

**Independent substitution controls and identified unexpected fragment check.** At state000 the position9 equation forces v=1 because E=0 and Delta^2 w=0; at state111 it forces v=0 for the same reason, reproducing the two easily confused endpoints of the first table. At state011 the position10 equation admits both v values because E=1 while E(1,1,v)=0; at state000 it admits neither because it would require v=1+v. The finite fragment0111000 obeys four successive position10 constraints (edges011->111->110->100->000), yet cannot continue even one more bit. A short temporal window can therefore mimic the return condition without defining a compatible periodic profile. No finite fragment is counted as a return certificate. These are direct Boolean substitutions independent of the cycle inspection, not a computational job or a new measured census.

**Scope and handoff.** The argument uses the same backward pair equations as G7/G159, with all word products and shifts retained. It supplies two additional local exclusions; no attainment at11, period-dependent return bound, rooted control example or prize claim follows. Local: include these two tables and the nonzero-entry guard in G188's second read, no run requested. The normalized lower bound11/q still tends to0; whether longer constraints force a growing obstruction remains open.


**G188 continuation: return11 has an odd-period cycle, so cannot follow doubling (GPT, 2026-10-07; second reader pending, hand algebra only).** Retain E(x,y,z)=x+y+z*(1+x)*(1+y), and define H(x,y,z)=(x+y) OR (y+z), equal to0 exactly at000 and111. Four profiles before a repeated pair were eliminated in the previous continuation. One further backward step gives

    F(x,y,z,v)=y+v+H(x,y,z).

For a putative return0,c,1,e,f,g,h,i,j,k,l,0, the last equal pair k=l=w therefore forces j=Delta w, i=w*Delta w, h=Delta^2 w, g=E(w), f=F(w), and e=S E(w)+(F(w) OR E(w)). Its remaining f equation simplifies to

    S F(w) = 1 + (F(w) OR Delta E(w)).

For consecutive w bits x,y,z,v,u, it determines the next bit uniquely:

    u = z + H(y,z,v) + 1
        + [F(x,y,z,v) OR (E(x,y,z)+E(y,z,v))].

The resulting four-bit-state successors, in increasing binary order0000 through1111, are

    0001,0011,0100,0111,1000,1011,1100,1111,
    0000,0010,0100,0111,1001,1011,1100,1110.

Every state feeds the SINGLE cycle

    0000 -> 0001 -> 0011 -> 0111 -> 1111 -> 1110
         -> 1100 -> 1001 -> 0010 -> 0100 -> 1000 -> 0000.

Hence a periodic w satisfying the equation has least period11. The reconstructed preceding profiles are all11-periodic. In particular c cannot have the even least period created by odd integration: its period divides11. For a rooted dyadic stage, there is also the direct check that w cannot be both11-periodic with least period11 and q-periodic for a power of two q. No earlier zero occurs through position10 by the preceding exclusions, so reset uniqueness indeed keeps all these profiles within the entry period until this putative return. Thus position11 is excluded. Combined with G188's earlier parts, the first subsequent zero and the stage length after doubling to q>=4 are at least12. This is still a constant bound.

**Independent cycle-word control and identified unexpected ambient return.** Reading the cycle gives the cyclic temporal word w=00001111001. Its four-bit windows reproduce exactly the eleven cycle states above. It has five black cells and, since11 is prime and the word is nonconstant, least period11. At window0000 the formula has E=F=S E=0, so e=0; at window0111 it has E=F=1 and S E=0, so e=1. Therefore c=1+S e is nonconstant and of least period11. Backward reconstruction consequently DOES produce a compatible ambient return at position11 with a nonzero entry; its pre-integration source Delta c has even block parity. This guards against claiming that the return equation has no compatible solutions. What fails is period-doubling ancestry, not compatibility. Neither this odd-period ambient return nor its gate/root reachability is asserted to belong to the rooted tree. The table and these controls are Boolean proof calculations, not a computed census or a requested Local run.

**Next obligation.** This continuation identifies an actual domain countercontrol while extending only a fixed local exclusion. The lower bound12/q still vanishes. No rule for arbitrary return lengths, period-dependent obstruction, recurrence of large normalized stages, or prize conclusion is established. Local: include the successor list, single cycle and odd-period scope check in G188's second read; no new job.


## G189 — Odd zero returns require logarithmic delay in the entry period (2026-10-07)

**Odd-return period bound, second reader pending; symbolic, no run.** Let compatible periodic profiles start with0,c,1, where c is nonzero of least period q. Suppose the first subsequent identically zero profile occurs at an ODD position r=2k+3, counting the initial zero as position0. Then

    q <= 2^k; equivalently r >= 2*log2(q)+3.

This applies to a doubled dyadic stage when its first zero return is odd. It does not assert that first returns are always odd, or that logarithmic delay supplies the normalized growth required by G186/G187.

**Prediction and counterfactual before the hand checks.** The backward profile functions at even indices should be affine with coefficient1 in their newest temporal bit, so a constant-one condition determines that bit. At odd indices this coefficient can vanish. The counterfactual that every return constraint is deterministic should fail at G188's return10 branch. The controls below check these three claims without a census or computational job.

**Backward functions and their temporal support.** At the final zero the preceding two profiles must be equal; call them w,w. Define U0(w)=U1(w)=w and, for n>=0,

    U_(n+2)(w) = S U_n(w) + (U_(n+1)(w) OR U_n(w)).

Here S w(t)=w(t+1), addition is XOR, and OR is pointwise. This is exactly the compatibility equation solved for the preceding profile, not a model that drops its background. By induction, U_(2j) and U_(2j+1) depend only on bits w(t)..w(t+j). Moreover

    U_(2j)(w)(t) = w(t+j) + A_j(w(t),...,w(t+j-1))

for a Boolean function A_j (A0=0). For the induction step, S U_(2j) has the new bit w(t+j+1) with coefficient1; the OR term in U_(2j+2) depends only on bits through t+j and cannot cancel it. The odd function U_(2j+3) has support through t+j+1, because it is S U_(2j+1) plus an OR term on that same support. This proves both support and affine claims.

In a return of length r, the profile at position2 is U_(r-3)(w), and the entry at position1 is U_(r-2)(w). Thus odd r=2k+3 forces U_(2k)(w)=1. For k>=1 this fixes

    w(t+k) = 1 + A_k(w(t),...,w(t+k-1)).

The k consecutive bits are therefore a state of a deterministic shift map with2^k states. Because w is periodic, its state sequence is a directed cycle, of length P<=2^k. Its temporal word repeats with period P. Every reconstructed profile, including c=U_(r-2)(w), also repeats with P, since these functions commute with time shift. Hence the least period q of c divides P and q<=2^k. For k=0, U0(w)=1 gives w=1 and q=1, yielding the same bound directly. No root reachability assumption is needed for this necessary bound.

**Independent literal and formula controls.** The first functions are U2=Delta w, U3=w*Delta w and U4=Delta^2 w, where Delta=I+S. Thus the r=5 equation fixes w(t+1)=1+w(t), and the r=7 equation fixes w(t+2)=1+w(t), matching G188's alternating and0011 cycles. The literal first return0,01,11,01,01,0 has q2,r5 and meets the bound exactly. Direct forward substitution checks its four interior triples: the right-hand sides are11,10,10,00, respectively, equal to the shifted children. Its preceding source is constant1, so this also guards the essential q2 exception in G188. The ambient r7 control there has entry1101 of least period4 and also meets the bound exactly, but is not an odd-source doubling. G188's ambient r11 entry has period11<=16, consistent with the bound and inconsistent with a blanket dyadic claim for ambient histories.

**Identified unexpected check: even returns retain branching.** U3(x,y)=x*(1+y) is independent of y when x=0, so the even-index induction does not extend to all U_n. More directly, G188's actual r10 condition admits BOTH next bits from state011, even though its full graph has no periodic cycle. This prevents replacing the even return condition with a deterministic map on the same states. For a nondeterministic graph, a periodic word can revisit states before its least temporal period: even the full binary shift admits words0^(m-1)1 of arbitrary least period m on a fixed finite state graph. That abstract control is not a compatible Rule30 return. It only shows why counting states alone is insufficient for the even case.

**Existing record, scope and next obligation.** This generalizes the deterministic odd-return maps of G188 using the backward identity already present in G7/G159. Finite deterministic maps and their cycle bounds are standard; no literature novelty is claimed. The result is a parity-restricted necessary logarithmic delay, not a growing normalized delay: log2(q)/q tends to0. Even first returns, ancestry restrictions and recurrence of large normalized stage lengths remain open. Local: please second-read the support induction, r-3 indexing and least-period divisibility; no new job or larger cap requested. The saved return12 calculation remains unpublished rather than supplying another fixed-bound increment.


**GPT incorporation of L153 (2026-10-07).** Local independently verifies G188 and all its published continuations in S80/S81 and promotes the proof. The cap-11 ambient return and the nonzero-entry guards pass. Their separate first-return census is explicitly exploratory, not preregistered: earliest returns21,88,6343 at q4,8,16, with sixteen q16 walks censored at200000 steps. These are finite descriptive findings, not an asymptotic lower bound. The growing gap between those returns and12 reinforces stopping individual constant exclusions. G189 instead records a general but weak odd-return bound; the saved return12 calculation stays unpublished. No q32 sample is requested in this block.

**G189 follow-on work note: a balanced entry does not replace complementary halves (GPT, 2026-10-07; hand control, independent review pending).** The proposed even-return shortcut was to retain only weight(c)=q/2 from the doubling identity c+S^(q/2)c=1. Prediction: G188's return8 language should admit a genuinely compatible balanced entry that fails this stronger pointwise identity. Counterfactual: half the cells black is sufficient to identify a doubling entry. The following derivation and literal forward control refute that counterfactual; no census or computational job was run.

For a return0,c,1,e,f,g,h,i,0, put h=i=w. G188 gives g=Delta w, f=w*Delta w, e=Delta^2 w, c=1+S e. Its return language has no11 and no000. Therefore f=w, and

    c(t)=1+w(t+1)+w(t+3).

Let A count cyclic gaps between consecutive ones with one zero, and B gaps with two zeros. Then q=2A+3B, weight(w)=A+B, and the number of pairs w(t)=w(t+2)=1 is A. Counting XOR ones gives

    weight(c)=q-2B=2A+B.

Thus balance is equivalent to B=2A, and the represented block length is8A. This already shows why cap4 cannot provide such a balance control while cap8 can. It does not say balance implies complementary halves.

Choose w=10100100, with A1 and B2. In increasing temporal order on cap8 the literal compatible first return is

    a=10110100, 0, c=10010011, 1=11111111,
    e=00110110, f=10100100, g=11101101,
    h=10100100, i=10100100, 0.

Starting with triple(a,0,c), the shifted children are respectively00100111,11111111,01101100,01001001,11011011,01001001,01001001,00000000. Direct XOR/OR substitution in S child=left+(driver OR child) gives these same eight words, independently of the gap-count argument. Every displayed intermediate profile is nonzero, so the return is first at8. The entry c has weight4 and least period8: its four-bit halves1001 and0011 differ. But S^4 c=00111001 differs from1+c=01101100; indeed c(1)=c(5)=0. It is balanced without complementary halves.

**Identified unexpected ancestry check.** The source a=Delta c has weight4 and least period8, not4; its halves1011 and0100 differ. This is an EVEN-source integration preserving period8, not a doubling from4. Merely checking entry weight would misclassify the domain. Neither rooted reachability nor an odd-doubling return is claimed. This actual ambient countercontrol blocks the balance-only shortcut while leaving G188 intact. The next even-return argument must keep the two temporal halves pointwise, together with the background profiles, rather than replacing them with scalar counts. The return12 checkpoint remains unpublished; no larger run requested.


**GPT incorporation of L154 (2026-10-07).** Local S82 independently checks G189's support induction, newest-bit coefficient, r-3 indexing and least-period divisibility, then promotes it to the verified record. The statement is read as a delay bound: an odd first zero return after entry period q cannot occur before2log2(q)+3. Their rooted first-return sequence21,371,52808 has parity odd,odd,even, so the even case is directly relevant at period16. The separate balanced cap8 return8 control above remains pending independent review and is not part of the promoted theorem. Its source retains period8, guarding the doubling scope. No asymptotic growth or new run is claimed.

