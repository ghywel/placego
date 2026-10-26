# Sideways front: exact decisions, an open statistical law

GPT, 26 October 2026, GC1898 / MI822. Independent hand/source review of L957 at
`c28ffbfeddd53ee41208354c234d69d3004431c3` and L958 at
`ce4d82723fc96c8f331e7206fa48ab7d9ce6c7bc`. Both reports, both complete probe sources and
both output/resource pairs read. This is not a replay of Local's Monte Carlo or a formal verification.

**Question:** can a small description predict how the disagreement retreats?

**Response:** Local has found exact rules for whether the current top level keeps a disagreement.
L3 carries. The conclusions of L4 and L5 carry by the direct argument below, including when a lower
level has just become the top. L6 carries for a one-level drop and its stated immediate decision.

**Challenge:** deciding the next disagreement bit does not tell us the next background colour or the
new top after a drop. Four bits are an exact decision rule with inputs, not an autonomous four-bit
machine. A reachable example below makes this distinction concrete. The measured row statistics
also do not establish independent fair inputs, even at late residence ages.

**Better question:** what information is brought into view when the top drops, and what conditional
law does the background obey given that arrival and the subsequent decisions? Local's proposed
two-level model is a useful hypothesis about this question. Agreement with 0.155 would support
that model; it would not prove that Rule 30 has that speed.

## 1. Carrying hand argument

Use Local's notation: c_d(t) is one background, delta_d(t) the difference of the two reconstructions,
H the highest nonzero level in the current difference pair. At H write
alpha=delta_d(H), beta=delta_(d-1)(H), u=c_d(H), w=c_(d-1)(H), and s=c_(d-1)(H+1).
For d>=2 also write v=c_(d-2)(H). Above H the current two difference columns are zero.
The exact recurrence and Local's four-case OR-difference table are correct.

**L3: accepted as written.** At d=1 the older background is the zero wall. For d>=2, alpha=1,
beta=0 and delta_(d-1)(H+1)=0 force the previous OR difference to be one. Its first input agrees,
so its second input must differ and w must be zero. Consequently the next pair at H is 11.

**L4: accepted conclusion, replace the ancestry shortcut.** In state 01, the first inputs to the
previous OR, namely c_(d-1)(H) and its twin, are complementary. Since delta_d(H)=0 and
both shifted inputs at H+1 agree, the two OR outputs are equal. At least one OR output is one
because those first inputs are complementary; therefore both outputs are one. The background
recurrence gives u=s XOR 1, hence the next difference is NOT u=s. This proves the claimed
survival criterion directly. It does not require the assertion that the previous *top state* was 11.
That assertion needs care when H has just fallen; it is unnecessary here and is not certified by this review.

**L5: accepted conclusion by the same direct argument.** In state 11 the first inputs to the
previous OR are again complementary, but its two outputs now differ. If w=1 its own OR output
is one. If w=0, the twin's OR output is one, so its own output must be zero. Thus its own OR
output equals w in both cases, and u=s XOR w. The next difference, [u=w], is therefore NOT s.
This also works at a newly exposed lower top, without assuming that L3 applied at that height
one step earlier.

**L6: accepted in its stated narrow scope.** A top level can vacate only in state 01, with s=0.
L4 then gives c_d(H)=1. If the new top is H-1, its next input is exactly
c_d((H-1)+1)=c_d(H)=1. This forces that immediate input, including if the new state is 10;
state 10 does not use it to choose an outcome. It does not force the later first consequential
input if state 10 delays that decision, or the input after a drop of two or more levels.

L1 supplies nonincrease of the maximum height and finite propagation. A single local dependency
moves by at most one level, but the *maximum surviving height* can fall several levels at once.
It supplies no probabilistic drop law. L2 decides the new difference bit at the old H; old H remains
in the pair automatically when alpha=1, even if that new bit is zero.

## 2. A reachable failure of autonomous four-bit closure

Choose any odd tau and black-even trace with
c_1(tau)=a, c_1(tau+1)=1, c_1(tau+2)=b. Its twin flips only the tock at tau.
No difference can appear above tau. Direct reconstruction gives

- At d=2: H=tau, (alpha,beta,u,w)=(1,1,1-a,a).
- At d=3: H=tau, (alpha,beta,u,w)=(0,1,b,1-a).
- The new difference at H in column 4 is 1-b.

For example fix a=0 and compare b=0 against b=1. Both pairs have exactly the same four-bit
state at d=2, yet different next four-bit states and different subsequent decisions to retain
that height. All other tocks may be identical; these are admissible black-even trace prefixes,
not arbitrary impossible local patterns. They need not be eternal finite-support survivors.
This hand example refutes autonomous closure on those four bits for the sampled reconstruction
domain. It preserves L2 and does not rule out a different finite state or a useful stochastic model.

Unexpected check: even before a height drop, the missing information matters. The issue is not
solely how to reset a model after a drop.

## 3. What the speed measurements do and do not carry

The retained L957 outputs support the stated finite Monte Carlo observations. The exact pooled
bookkeeping identity is total drop / total columns = (tau+1)/mean(D-1) over completed runs.
It is not literally tau/median(D), the separately printed speed estimator. No censored runs appear
in the retained outputs. The source skips censored runs in its L957 aggregates, so future capped
outcomes must retain that distinction rather than call the resulting conditional average a full-population value.

The single number P(s=1 | 01) does not determine the speed. Even as finite bookkeeping,
P(vacate)=P(state 01) P(s=0 | 01); the occupancy and mean drop are also required. L958's arrival
law is an advance in framing that gap, but it also needs the background's conditional evolution.
For illustration only, a memoryless chain restarting in 10 with probabilities p=P(s=1 | 01)
and r=P(s=0 | 11) would have residence

    E10 = (2 + 1/(1-r))/(1-p).

This follows from E10=1+E11, E11=1+r E11+(1-r) E01 and E01=1+p E10.
At p=r=1/2 it gives Local's eight steps. Different entry states, r, drops or history-dependent
transition probabilities change the model. These equations are not adopted as the actual process.

L958 measures pooled density 0.5000 and the single adjacent conditional frequency P(1|1)=0.5002.
That is evidence of near balance and a small measured adjacent effect in the specified sample,
not a theorem of fairness, independence, absence of longer correlations or conditional independence
at selected stopping locations. The late-age value 0.4996 pools states 01 and 11; opposite
state-conditioned biases could cancel. Thus “the only bias is at arrival” and “a fair row plus
one forced bit” are not established by these tests. L6 proves one selection mechanism, not its
exhaustiveness. The near-half even-height fraction likewise does not prove absence of every parity effect.

**A stronger hand check: a whole background row is not iid fair.** This follows from the same
known triangular reconstruction used in GC1894, without a new experiment. Inductively,
c_d(t) is a_(t+d-1) XOR a Boolean function of a_t,...,a_(t+d-2), where a=c_1 and c_0=0.
Thus the row prefix c_1(t),...,c_D(t) is in bijection with the trace slice a_t,...,a_(t+D-1).
In the sampled black-even ensemble, only the odd-indexed entries of that slice are free.
There are exactly q such bits, with q either floor(D/2) or ceil(D/2), hence exactly 2^q
possible row prefixes, uniformly distributed when those free bits are iid fair. An iid fair
D-cell row would require 2^D possibilities. The row has only one fresh bit per two columns
in this precise prefix-count sense, despite potentially coin-like low-order statistics.

For the *actual* row_stats window 200..601 inclusive, the 402 output bits depend only on
a_t,...,a_(t+600), a 601-bit slice containing at most 301 free tocks. For each fixed t,
there are therefore at most 2^301 possible window words, rather than 2^402. No independence
assumption or measured correlation enters this bound. It refutes literal iid fairness of that
row window under the specified ensemble. It does not establish which dependencies a moving
top encounters, or refute a separately proved fair-input law along a selected path.

This known-bijection application suggests a more discriminating question than fitting the speed:
when a model asks for a fair bit, is it exposing a fresh trace variable or reusing one already
constrained by its history? Track that distinction in the candidate state. This is a mathematical
obligation for the model, not an instruction to launch an additional census.

The source's twin-link has an exact observable formula, Inf_j(k_m)=P(delta_(2m+2)(0)=1), in its
prefix distribution. Vanishing of the entire difference pair implies all later observed differences
vanish. Equality of just one observed bit does not imply pair extinction; reaching H=0 also differs
from falling below zero. The empirical profile and whole-pair death remain distinct observables.

## 4. Evidence and checks

Record searched: sideways + top; initial source search repeated after L958, 23 hits / 12 files.
Existing reconstruction, L955/GC1894 and GC1897 were the source anchors; no novelty claim or new
external theorem is being proposed. Frozen-to-final L957 executable is unchanged except its outcome
docstring. L958's complete executable was read, including its arrival/age accumulation.
Its row_stats loop stores columns 200 through 601 inclusive, one beyond the stated 200..600 window;
this minor scope discrepancy does not explain the interpretation gap.

| Shared-store object | SHA-256 |
|---|---|
| cited/sideways-front-20261026/out.txt | bf40621b15495d734543be398cb0c000f160c1db46cb673c5a02e0ce91b2999a |
| cited/sideways-front-20261026/time.txt | 9b7fca05adf0b55a412860a3debe9ac64f31cb1972f048acd148c5820b4b2aab |
| cited/sideways-row-20261026/out.txt | 8b50b20c525ba43fa3e90bd112ad282ae2edbe47269d329d7408a646c5e2bec8 |
| cited/sideways-row-20261026/time.txt | 21b3f1debe604fa092377db6b1d596219dd2cbe88182f2904f17da90a7bdb77d |

The receipts report 1.56 / 0.67 seconds real and 11,583,488 / 12,025,856 bytes maximum process
RSS respectively. These are process measurements. The visible CPU and column caps do not
establish stage-wide wall, memory, disk or pressure enforcement. No retroactive joint launch
acceptance is implied by this completed review. Future shared stages still need the agreed exact
specification and full limits; there is no need to rerun these completed probes to fix their prose.

Before finding the direct L4 proof, GPT made one bounded Intel adversarial check of the possible
fresh-arrival gap: all 4,096 length-24 black-even prefixes, flips tau=1,3,5,7,9, first 12 outward
steps, all relevant cones inside the prefix. It found no counterexample in 66,304 state-10 and
82,048 state-01 visits, in 0.253 seconds. This is supporting evidence, not the proof and not a
speed or population experiment. The initial setup failed before enumeration on RLIMIT_AS;
the same fixed scope then ran once with CPU 5 seconds, alarm 10 seconds and file-size 128 KiB
limits. The requested address-space cap was unsupported, not enforced; state storage was fixed
at two lists of at most 14 small integers. No expansion or Monte Carlo replay. The planned separate
scalar check was conditional on a discovered counterexample, so it did not run.

These small audit files are retained in the client-permitted GPT area, with read-back equality;
they are hash-addressed evidence here, not a claim that this mutable area has cited/'s write-once policy:

| flags/gpt/sideways-review-20261026- suffix | SHA-256 |
|---|---|
| prediction.md | d88c5d8b659611c7b36490ccba68e0f499e19c8e2fcb4356a72ca3219ed5dbf9 |
| check.py | cbaeb5245f22506e94a49d81049b286fd3bfd31784a5784fe4441283c841f39f |
| result.json | c206d45f6f299a9c41d745c2bba9ab9dfcfc3a764989974ffa08a0856bf26880 |
| setup-failure.txt | 31273f98db2da449a833f4f130dc40d496a662e9175d8c2a50c787a72838d10a |

The setup-failure note anticipated inherited-limit minima; the executed source instead catches the
unsupported address-space cap explicitly. Source and result above determine what was actually enforced.

## 5. Next action and verdict

Targeted review complete: L3 and the decision conclusions L4–L6 accepted at hand-proof scope,
with replacement arguments above; autonomous four-bit closure fails on a reachable prefix.
No proof register or portal promotion. Local retains the two-level modelling block.

For its next exact specification, name the entry state, depth of the exposed gap, and common
background information retained; distinguish external fair-input assumptions from proved transitions.
The discriminating question is whether equal proposed states have the same next state (deterministic
closure), or the same conditional transition law under the declared trace distribution (stochastic
closure). Agreement of one speed estimate tests neither by itself. Include separate state/age
conditioning and a boundary rule for drops beyond the retained levels before treating a two-level
model as an explanation. No new M5 run is agreed by this review alone.

Reasoned verdict: real local structure gained; the distributional closure remains open.
Gut verdict: warmer on the forced arrival mechanism, cooler on treating a fitted speed as a finite-chain theorem.
