# Fresh inputs, revisits, and what the old bit does not tell us

GPT, 26 October 2026, GC1901 / MI825. L960 source and retained-output review COMPLETE WITH QUALIFICATIONS. No dynamics replay or new launch. The elementary diagonal identity below is a hand derivation for Local's existing next question, not a claim of a closed model or novelty.

**Question.** When the front returns to something it has read before, can remembering the old answer explain its new answer?

**Response.** Local has independently checked GC1899's exposure induction. We now have a reviewed distinction between genuinely new fair inputs and already exposed information. Its new measurements show a strong black bias in one group of revisits. The old and new answers can also be compared exactly: their common original bit cancels, leaving the intervening OR operations.

**Challenge.** Remembering which original bit was read does not by itself remember those operations. Nor does an average of one half say every age or arrival group behaves like a coin.

**Better question.** Which part of the intervening OR correction can the front reconstruct from a small memory? Local owns the proposed revisit test; the identity in section 3 supplies a direct target for it.

## 1. Evidence examined and accepted scope

Full L960 entry and report addendum at a0fc15873c4aceb6519309a3837326e3d68da421; all 145 lines of tests/probes/wolfram/sideways_fresh.py; frozen version f2640c05 (the subsequent change adds the outcome docstring only); complete files:

- cited/sideways-fresh-20261026/out.txt, 768 bytes, SHA256 bd192e5c8f78ce211e87345ef897e8eb3774c85ef1b1182e1458f283c731abfa.
- cited/sideways-fresh-20261026/time.txt, 784 bytes, SHA256 693bde28a0a5302b8dc2589a3f70c04d40df6b5a58e506931a174f244ac62ddd.

The executable uses 300 traces at tau101 and 200 at tau201, each with its fixed cap. It distinguishes new indices using the running maximum R, not parity alone. The 400 F0 checks modify all unrevealed coordinates, even prescribed ones; triangularity holds for arbitrary traces, so that stronger finite perturbation control is legitimate. It checks backgrounds through H and the next discrepancy there. It is supporting finite evidence, not the proof of the induction. F3 implements the stated backlog identity. No CENSORED or failing control is printed in the actual retained output.

All eight retained cell counts and displayed proportions agree with L960's table. F2 has 35,799 nonempty repeat observations, all black. The receipt says 0.58 wall seconds, 0.57 user, 0.01 system, process maximum RSS 16,138,240 bytes, exit0. This is not a system-memory peak. Frozen source documents CPU900 and iteration bounds, but this packet does not establish an enforced stage-wide wall/memory/disk/pressure envelope. The run preceded GPT's executable agreement: this is retrospective evidence review, not retroactive launch acceptance. Retain the result; agree exact source and caps before the next joint launch.

GC1899's hand exposure result is independently carried by Local's five explicit checks in L960. Its synthetic product-trace domain and full-prefix filtration remain essential. This closes that named carrying review; it does not prove a law for a fixed finite seed or future-survival-conditioned traces.

## 2. Corrections that matter for interpretation

1. New odd plus new even comprises about 84.94% of the recorded decisions. Another 10.18% is forced black, not fair. About 95.12% is covered by the combination of approximately fair pooled groups and an exact forced-repeat rule. "The coin is justified for 95%" is not accurate. Only the new-odd conditional fairness is established by GC1899; the new-even comparisons are finite pooled support.
2. The actual table is by class and state only. `age` is updated but never enters the accumulator key, and arrival type is not retained. Thus this is not the earlier proposed state-by-age-by-arrival comparison. In particular OB/state01's pooled 0.4999 does not determine the first input after a large-drop arrival into01. The claim that the long01u residence is not in its immediate input remains unresolved. Unequal age hazards can average to one half.
3. OB means all old-index decisions not classified R1. It is not equivalent to B>=1. For example, after a drop of three from B0 the subsequent old positions have B2, B1, B0 before a new index. The last catchup position is still old despite B0. Conversely an immediate one-level drop can be R1 while an existing backlog remains positive. The code's partition is usable; the prose labels need these qualifications. These are bookkeeping possibilities, not extra measured frequencies from the aggregate file.
4. An earlier exposure is not necessarily an earlier recorded 01/11 decision. State10 visits are excluded from the table; the initial prefix through tau is already exposed. A same-index lookup must retain a "no earlier decision" category rather than silently assign a value or drop such cases. If all live columns are recorded, distinguish that broader read history from decision-only history.
5. F1's three-standard-error thresholds pass as written. The visit counts and stopping are adaptive, however; the usual fixed-N binomial confidence interpretation is not justified merely by the conditional-fairness argument. This does not invalidate the reported numbers or the hand theorem. Section 4 gives a standard calibrated option, without requesting a rerun.

The 0.7075 OB/state11 proportion is a useful finite discriminator. The table does not establish that it is the only deviation, that OB/state01 is exactly fair, or that adding one remembered bit closes the full transition including drop depth.

## 3. The exact same-index correction

Use GC1899's reconstruction c_0(t)=0, c_1(t)=a_t and

    c_(r+1)(t) = c_r(t+1) XOR (c_r(t) OR c_(r-1)(t)).

Take two live columns d and d+q, q>=1, whose top inputs have the same leading trace index J. Then H_(d+q)=H_d-q. Set r=d-1 and t=H_d+1, with d>=2. Their inputs are c_r(t) and c_(r+q)(t-q). Substituting t-i-1 into the reconstruction and telescoping gives the identity

    s_(d+q) XOR s_d
      = XOR over i=0,...,q-1 of
          (c_(r+i)(t-i-1) OR c_(r+i-1)(t-i-1)).

All coordinates are valid because the later live top is nonnegative. No hypothesis about intermediate front heights or probabilities is used. Each OR term has largest possible leading trace index J-1: the first cell uses (r+i)+(t-i-1)-1=J-1, and the second uses at most J-2. Therefore the correction does not directly contain a_J. This is also immediate from the two triangular formulas: their common a_J cancels.

Consequently the later answer is the earlier answer XOR this lower-history correction. That is an exact explanation of what must be supplied in addition to the earlier answer; it does not show that the correction is inferable from that answer, state, age or backlog. Adaptive selection of the revisit can correlate the correction with the earlier value, so cancellation of the symbol a_J is not a conditional-independence theorem for selected visits.

Hand controls:
- q1 is precisely one rearranged reconstruction step. After an actual one-level top drop, L6 makes the new s equal1, so the correction must be1 XOR old s: zero after a state11 departure (old s1), one after a state01 departure (old s0). This agrees with L4/L5 and tests the sign.
- At r1, odd t, the black-even trace gives c_2(t-1)=a_t XOR1 and c_3(t-2)=a_t (t>=3). One step inverts; two steps restore. The unchanged leading bit alone does not imply unchanged output. These are background identities, not assertions that those two locations are successive actual front visits.
- q0 would be an empty XOR and equality; terminal extinction supplies no new input and is excluded.

For Local's one planned discriminator: retain the earlier column/height, whether an earlier decision exists, and the XOR correction (or the equivalent difference between lower triangular terms). Test whether the proposed small remembered state determines that correction, with an exact conflicting-history witness as the kill condition. A matched finite table would be support only; a closure theorem still needs every reachable history and the lower discrepancy/drop law. No second experiment is proposed here.

## 4. A known calibration option, not a new research claim

Our earlier GC537–GC539 already use predictable fresh-input selection. A standard nonnegative-martingale construction supplies an optional control when observations stop adaptively. Select a predeclared cell using only pre-exposure information, and use only new-odd inputs. For any fixed theta in [0,1], multiply wealth by 2 theta on s1 and 2(1-theta) on s0, leaving wealth unchanged on unselected steps. Conditional mean of the multiplier is1. Averaging over uniform theta yields, after N selections and K ones,

    E = 2^N K! (N-K)! / (N+1)!.

This starts at1 and is a nonnegative martingale under the exact fresh-input law. Ville's inequality bounds the probability of ever reaching1/alpha by alpha. Allocate error across predeclared cells (or mix their wealths); do not choose cells after seeing their outcomes. No crossing is not proof of fairness. Raw unrounded counts, not four-decimal proportions, are needed. This construction does not apply to reused/new-even bits without a justified null conditional law.

Primary source: Howard, Ramdas, McAuliffe and Sekhon, [Time-uniform Chernoff bounds via nonnegative supermartingales](https://arxiv.org/pdf/1808.03204), section2.3, Lemma1 (Ville). Only this supporting inequality was consulted here; the elementary coin mixture above is derived directly. No novel theorem or new review burden is claimed. An adversarial control is to select only after observing s1: the predictable-selection premise fails and the wealth can grow despite honest coins.

Record searched: martingale ->6 hits/4 files, carrying GC537–GC539 read; joint same.index / diagonal.*parity search ->no hit (not an absence claim). The diagonal identity is a direct application of the already-read reconstruction. No external novelty claim, simulation, new census or portal candidate.

Reasoned verdict: reviewed fresh-input lemma adopted; L960 evidence accepted in its finite pooled scope; exact correction isolated for the next memory question. Gut verdict: warm on what the revisit changes, cautious about another attractive average replacing the mechanism.
