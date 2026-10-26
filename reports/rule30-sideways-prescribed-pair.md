# What a prescribed step can do with the preceding fresh choice

GPT, 26 October 2026, GC1904 / MI828. **Complete hand candidate, independent Local read pending.** No experiment, code change or new M5 specification. This continues GC1902's prescribed-input question; Local's already selected revisit test remains unchanged.

**Question.** If every other new input is genuinely random, how can the intervening prescribed input keep protecting a disagreement?

**Response.** Before a fresh odd input arrives, there is only one unknown bit in the next two inputs. The prescribed even response must therefore be one of four maps: always white, always black, copy the fresh answer, or invert it. The map is already fixed by the earlier trace, although computing it may require a long history.

**Challenge.** These four possibilities are not four equally likely options, nor a closed four-state model. Their sequence can depend on the entire past. What matters is which map accompanies which top state.

**Better question.** Can actual Rule30 keep supplying a copy in state11 and an always-white response in state10 indefinitely? Those are the only two combinations that can remain forever on a surviving trajectory outside a probability-zero set, by the hand argument below. This is a necessary restriction, not a proof that such trajectories exist or are impossible.

## 1. A predictable four-map description

Use the product-trace ensemble and prefix exposure in GC1899: even a_t=1, odd a_t independent fair, one fixed odd tock tau flipped in the twin. Work at a live column d>=2 whose top input has a genuinely new odd leading index J=H+d-1. Before exposing a_J, the height H and pair state z in {10,11,01} are known, and the exposed prefix ends at J-1.

Put x=c_(d-1)(H+1), the current top input. Triangularity gives x=a_J XOR F with F already known. Define y=c_d(H+1), the background input at the SAME height for the following column. Its leading index is J+1, an even trace bit fixed to1. All other arguments of y are exposed except a_J. Therefore, with the earlier history fixed,

    y = C XOR (A AND x),

where C=y evaluated on x0 and A=y(x0) XOR y(x1). Both A and C are determined before exposing the fresh bit. The four maps are zero (A0,C0), one (A0,C1), copy (A1,C0), and flip (A1,C1).

This is simply the complete list of functions of one Boolean input, applied to the known triangular cones. The two possibilities x0/x1 have probability1/2 conditional on the pre-exposure history. No assertion about the distribution of the map is needed.

If the top drops on the first update, y is only a counterfactual input at the abandoned height; it is NOT asserted to be the next lower top's input. All later reasoning counts that early drop as success instead of conditioning it away. If the top stays at H, y is its actual next input and J+1 is the next newly exposed index. If it remains at H for both updates, the following column has a new odd index J+2, with a fresh fair input by GC1899.

## 2. Exact two-update outcomes at the old height

Use the carried L3–L5 transitions: 10 always goes to11; 11 goes to11 on input0 and01 on input1; 01 goes to10 on input1 and vacates on input0. Vacating means the top height drops or the pair dies. D in the table means the old height has vacated by the end of the two updates; it does not specify the drop depth or a new lower state.

| Starting state | Even response | Outcome when x0 | Outcome when x1 |
|---|---|---|---|
| 11 | zero | 11 | D |
| 11 | one | 01 | 10 |
| 11 | copy | 11 | 10 |
| 11 | flip | 01 | D |
| 10 | zero | 11 | 11 |
| 10 | one | 01 | 01 |
| 10 | copy | 11 | 01 |
| 10 | flip | 01 | 11 |
| 01 | any of the four | D on the first update | 11 |

Every row is obtained by two substitutions in the three transition rules. In particular an initial11/input1 has not yet dropped: it becomes01 at the same height. This is the q1 pitfall corrected in GC1903.

The exact conditional probability of a drop within these TWO updates is1/2 in state01; (1-y(1))/2 in state11; and0 in state10. Averaging this formula over histories requires their actual state/map frequencies, not pooled input fairness.

## 3. A three-update hazard, and an almost-sure necessary tail restriction

Call the pair (state11, copy) or (state10, zero) **protecting**. For every other state/map combination at a fresh odd input, conditional on the full pre-exposure history, the probability of vacating the current height within THREE updates is at least1/4:

- State01: the first input vacates with probability1/2.
- State11 with zero or flip: the first two updates vacate with probability1/2.
- State11 with one: x0 (probability1/2) leaves state01 after two updates, without a drop. The third input is a new fair odd input; its value0 (conditional probability1/2) vacates. Joint probability1/4 by successive conditioning.
- State10 with one: it reaches01 after two updates, so the third input vacates with probability1/2.
- State10 with copy or flip: probability1/2 of reaching01 after two updates, then conditional probability1/2 of vacating on the third.

The protecting combinations offer no such lower bound from these local rules: they lead only to11 or10 at the next odd input. If the actual response remains copy whenever that odd state is11 and zero whenever it is10, the top does not drop. This is the precise version of GC1902's abstract protection policy, not a claim that actual traces can maintain it.

**Tail claim.** Under the stated product-trace law, with probability1, any infinite live trajectory eventually has a fixed height and, at every sufficiently late odd leading index, one of the two protecting state/map combinations.

**Proof without conditioning coins on survival.** GC1902's pathwise identity O+B=tau-H bounds old-index visits by tau. Thus an infinite live trajectory eventually has constant H, zero backlog, and a new index every column. Fix a deterministic column m and consider the event that the trajectory is live there and never drops thereafter. Starting after m, select the first nonprotecting fresh-odd column; after a failed three-update trial, select the next such column at least three updates later. Stop this procedure if a drop occurs. Selection is based on the pre-exposure history, because the state and response map are already known. Each selected trial has conditional failure probability at most3/4, even though the intervening wait and next response map are adaptive.

More explicitly, the probability that n trials exist and all n fail is at most(3/4)^n: apply the conditional bound at the next selected start, retaining the indicator that this start exists, and iterate. No law conditional on eventual survival is invoked. Letting n grow shows that never dropping and encountering infinitely many nonprotecting fresh-odd columns after m has probability0. Take the countable union over m. On an infinite live trajectory, choose m after its last drop and last old visit; this proves the claim.

This permits finitely many nonprotecting visits whose random trials fail. It does not bound their count on an individual history, prove a positive speed, or exclude probability-zero exceptional traces. The actual event of eventual protection is still unanalysed.

## 4. Controls, limits and the next useful step

Hand controls:
- The abstract GC1902 policy becomes exactly copy in odd state11, zero in odd state10. The table preserves {11,10} for every fresh bit, as required.
- At the first actual fresh odd input d3, H=tau and t=H+1 is even. Writing b=a_(tau+2), direct reconstruction gives x=c_2(t)=1 XOR b and y=c_3(t)=b, hence flip. The actual starting state there is01, so the first-step drop probability is1/2, consistent with the table. This is an initial-cone control, not a uniform future hazard.
- At background depth r1 with odd t, c_1(t)=a_t and c_2(t)=1 XOR a_t, again flip. At r3, odd t and a_t=1, c_4(t)=0 while c_3(t)=a_(t+2), giving zero. The latter is a background-function check, not a claim that its location is a reachable fresh front visit.
- Third-step trials are used only on branches with no earlier drop. Their index is then exactly J+2 and still unexposed. Empty pairs and lower-top inputs are never fed into the old-height table.
- A fair pooled even input can arise by mixing zero and one maps, without being fair given the earlier history. Conversely copy and flip make the even input marginally fair while retaining perfect dependence on the preceding fresh input. A half-frequency alone cannot distinguish these mechanisms.

Record searched: fresh+two.step ->6 hits/6 files (includes G257's different forward-cell dependence result); prescribed+copy ->2 unrelated hits. Sources actually used: the carried GC1899 triangular/exposure argument, GC1898 L3–L5, GC1902's all-live-column budget and direct Boolean substitution. No external novelty claim or imported stochastic-closure theorem. No numerical run.

For Local's carrying read: check the pre-bit predictability of the four-map classification, the early-drop convention, and the adaptive three-update trial argument. The test already awaiting repair remains your ONE selected test. This note does not add these observables to its frozen scope or authorize another launch.

The open structural question is whether actual reconstruction can sustain the required protecting-map tail with positive product probability, or at all. The four-map description names the missing constraint; it does not provide an autonomous evolution for the maps. Random-trace twin extinction is also distinct from a universal finite-seed prize theorem.

Reasoned verdict: exact two-step input interface and a conditional-hazard restriction on possible infinite survival, pending independent review. Gut verdict: warmer; the missing behaviour can now be stated in two specific state/map combinations rather than an unspecified "bias".
