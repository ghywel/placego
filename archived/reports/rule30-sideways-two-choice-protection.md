# A surviving tail must eventually protect both next choices

GPT, 26 October 2026, GC1907 / MI831. **PROVED in its stated almost-sure product-trace scope: Local L968 independently carried the argument at b3227b65; adopted GC1909.** Continues the carried GC1902/GC1904 budget and hazard arguments and L964's diagonal formula, carried in GC1906. No experiment, change to the accepted revisit stage, or portal candidate.

**Question.** We distinguished protection along the chosen path from protection for both possible next choices. Can a lasting disagreement keep relying on choosing the good branch?

**Response.** It can do so finitely often. But if opportunities to take a dangerous branch keep recurring, each offers a fresh, uniformly positive chance of retreat. The proof below shows that an infinite live path almost surely eventually avoids those situations too.

**Challenge.** “Eventually protects both choices” is a probabilistic tail conclusion, not a property of every individual surviving finite history. And protection for two rounds does not establish protection forever.

**Better question.** Can actual selected fronts sustain the concrete two-choice parity conditions below? This gives Local's consecutive-protection question a precise necessary condition without inventing a universal contradiction.

## 1. Two consecutive protecting rounds

At a live column d with fresh odd leading index J, before exposing its bit, write the top state as (alpha,beta), current input x and prescribed next input y=C XOR(A AND x). A current round is protecting exactly when

    alpha=1, C=0, A=beta.

This is GC1904's (11,copy) or (10,zero). Under either protecting combination, both possible values of x keep the same top height through two updates, and the state at d+2 is

    (alpha_next,beta_next) = (1, 1 XOR (beta AND x)).

Both counterfactual successors are genuine continuations of the current black-even trace prefix: x is a bijection of its next free bit; the pre-bit state is the same; the protecting table gives no drop in either branch. No claim about the lower discrepancy being unchanged is needed.

At column d+2 let the next input pair have response coefficients A_next(x), C_next(x). These coefficients depend on the prefix only through J+1. Before exposing the current bit, each is therefore a known function of the one Boolean variable x. Write

    A_next(x) = K XOR (B AND x),
    C_next(x) = U XOR (V AND x).

There is no exposure of the next random bit at J+2 here. To define these coefficients one uses the known next even bit at J+3 and the two formal values of the J+2 input; its coefficient/intercept are determined by the earlier prefix, exactly as in GC1904. In either current x branch, J+2 is fresh when its actual decision arrives.

Define a current history to have **two-choice protection** when it is currently protecting and BOTH successors at d+2 are protecting. Equivalently its predictable coefficients satisfy

    alpha=1, C=0, A=beta,
    K=1, B=beta, U=0, V=0.

This is a finite-cone condition on a specified history, not a finite-state autonomous description. It includes the intercept requirements; parity of A alone is insufficient.

## 2. Five-update hazard outside that condition

Conditional on the pre-bit history at any fresh odd input which lacks two-choice protection, the probability of a top drop or extinction within the next FIVE updates is at least1/8.

- If the current round is not protecting, GC1904 already gives probability at least1/4 within three updates.
- Otherwise at least one of x0 and x1 has a nonprotecting successor. Choose such a branch using only the pre-bit history. The fresh x takes it with probability at least1/2. Both current updates keep the top fixed. At d+2 that branch has a genuinely fresh odd input and the nonprotecting three-update hazard is at least1/4. Successive conditioning gives at least(1/2)(1/4)=1/8. No independence of the maps or states is assumed.

The five updates are those starting at d,d+1,d+2,d+3,d+4. The last decision can use the new odd bit at J+4 on a branch with no earlier drop. As before, an earlier drop is already success; no lower top is passed through an old-height formula.

**Almost-sure tail conclusion.** For each fixed finite starting flip tau, under the specified product law, almost surely every infinite live path eventually has two-choice protection at every fresh odd column.

Proof: fix a deterministic column m, select the first later fresh odd history failing the condition, and after an unsuccessful trial wait at least five updates before selecting another. Stop if a drop occurs. The condition and start selection are measurable before the current bit. Iterated conditioning, retaining the existence of each selected start, bounds the probability that n selected trials exist and all fail by(7/8)^n. Thus no-drop histories with infinitely many such trial opportunities after m have probability zero. GC1902 gives finitely many drops and old visits on any infinite live history, so choose m after them. A countable union over deterministic m proves the conclusion without conditioning the coins on eventual survival.

This does NOT say that every realised history already protects both branches. It permits finitely many unsafe branch points whose dangerous outcome was avoided. Probability-zero histories remain outside the conclusion. It supplies no lifetime bound or speed, and no universal finite-seed prize theorem.

## 3. A concrete new diagonal restriction

Use L964's indexing, k=0,...,d-2:

    e_k = c_(d-2-k)(H+1+k),
    P_k = c_(d-1-k)(H+1+k),
    Q_k = c_(d-k)(H+1+k).

Extend Q_(d-1)=1 and Q_d=0. Let w_k=1 XOR e_k, the indicator that e_k is white. L964 gives A=XOR_k w_k. From Q_k=Q_(k+1) XOR(P_k OR e_k) and the fact that each P_k has slope1 in x,

    slope_x(Q_k) = XOR_{j=k,...,d-2} w_j.

At the next odd column, its exposed diagonal is exactly this Q, including the two fixed endpoint cells. Its white parity is A_next(x). Taking the XOR of the slopes above, each w_j occurs j+1 times. Hence

    B = XOR_{even j} w_j.

Current protection requires A=beta; two-choice protection requires B=beta. Subtracting in Boolean arithmetic yields the explicit necessary condition

    XOR_{odd j} w_j = 0.

In words: an even number of the white cells occupy odd-indexed positions on this exposed diagonal. This condition must hold eventually along an infinite live path outside a null set. It follows from the hand theorem above, not from an assumption that diagonal cells are independent or fair.

There is also a direct hazard reading: at a currently protecting history with odd-index white parity1, B differs from beta. Therefore A_next(x) differs from the required1 XOR(beta AND x) on exactly one of the two x values, regardless of K. That successor cannot protect. The current history consequently has the five-update hazard at least1/8. This uses only the carried diagonal formula and current protecting table; it does not require computing C_next.

## 4. Controls and the boundary of the result

- **Index control:** for d3, e=(1,0), A1 but B0, since the only white has odd index1. This is consistent with the slope calculation. The actual initial map there is flip and the state is01, so it is NOT offered as a currently protecting reachable example.
- **Multiplicity control:** a white at position j0 contributes once to Q parity; j1 twice; j2 three times. Only even positions contribute to B. The fixed Q endpoints contribute no slope.
- **Branch control:** if one successor is nonprotecting, taking the other branch can still survive this trial. That is why the conclusion uses repeated conditional hazards, not a contradiction from one observed protected pair.
- **No hidden next coin:** current protection keeps H fixed through d+2 under both x values, so J+2 has not been consumed by a drop or revisit. The next-map coefficients are fixed before that bit, as required.
- **Unexpected relaxed-model control:** GC1902's abstract policy, choosing copy in11 and zero in10 at every odd round, protects both branches forever. The new probability argument cannot rule that policy out. Only actual reconstruction constraints, such as the exposed-diagonal conditions, can supply the missing obstruction.
- **No infinite quantifier interchange:** finite look-ahead protection does not imply an infinite all-choice safe tree. No stronger limit claim is used.

Record searched: protect+both ->146 hits/32 files; odd.index+parity ->2 hits/2 files; targeted current reports contain GC1906's branch distinction. GC526's earlier physical iid width-two confinement argument was read as a scope control: it concerns a different front/ensemble and is not imported. Carrying sources here are GC1902/GC1904 (independently read L963), L964's telescope (carried GC1906), and the same elementary iterated-conditioning argument. No external novelty claim, stochastic closure or numerical run.

For Local: one carrying extension of the existing hand line. Please check predictability of the two successor maps, the five-update trial selection, and the odd-index white-parity consequence. The accepted L962 revisit experiment retains priority and exactly its frozen scope. Next actual mathematical dependency: demonstrate repeated violations of the necessary conditions on selected fronts, or identify an actual mechanism sustaining them. Arbitrary background examples alone do neither.

Reasoned verdict: a stronger almost-sure necessary protection condition and an exact parity discriminator, hand candidate pending independent review. Gut verdict: the earlier branch caveat becomes useful mathematics, but the actual obstruction has still not been found.

## Independent review adoption, GC1909

L968 re-derived the successor states, predictable coefficients, disjoint five-update hazard trials and diagonal multiplicities. Adopted in the exact stated scope. Original requests above are historical; no extinction, speed or every-trace conclusion is added.
