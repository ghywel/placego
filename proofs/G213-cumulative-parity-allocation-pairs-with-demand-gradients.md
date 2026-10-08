# cumulative parity allocation pairs with demand gradients

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT213. cumulative parity
allocation pairs with demand gradients (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Cumulative parity imbalance interacts with changes in future survival demand.

**What it says.** The exact count increment can be rewritten using cumulative odd-minus-even counts and neighbouring differences of the demand weights. Centering those cumulative counts gives an upper bound from their range times the full variation of the demand.

**Why it matters.** It offers another way to study the actual allocation without assuming a bell-shaped demand law. Both boundary jumps must be counted. The bound can be worse than the earlier absolute sum, and a useful asymptotic estimate still needs control of the actual allocation.

**An everyday picture.** Instead of counting surpluses separately in every bin, keep a running surplus and pair it with how the price changes between bins. The endpoint price changes matter too.

## The formal statement and proof

**Where:** RULE30-GPT.md GC416 at58bf849; identity and proof copied verbatim below. Local L250 at3a54850 checked the summation, both boundary jumps, centered bound and guards. This is ordinary Abel summation applied to G74, not a new general theorem or a uniform count estimate.

At fixed t and final T, write I_a=I_w(t,a) and d_a=Delta_t(a), extending both by zero outside their finite support. Set B_a=sum_(b<=a) I_b; include its zero left tail and constant right tail. Then the exact increment is

    H_(t+1)-H_t = (1/2)*sum_a B_a*(d_a-d_(a+1)).

Proof: substitute I_a=B_a-B_(a-1) in G74 and shift the second finite sum. The lower support jump must be retained. The gradient coefficients sum to0, so one may subtract any constant from B. Choosing the midpoint of its maximum and minimum gives

    abs(H_(t+1)-H_t) <= osc(B)*TV(d)/4,
    osc(B)=max_a B_a-min_a B_a,
    TV(d)=sum_a abs(d_a-d_(a+1)).

Telescoping yields the sufficient bound abs(C_w(T)-Q_w(T)) <= sum_(t=m)^(T-1) osc(B_t)*TV(Delta_t)/4. No unimodality or log-concavity is needed; full demand variation includes every interior reversal and both endpoint jumps. Actual signed cancellation may be retained in the identity rather than bounded by the oscillation. A uniform ratio would still require this sum to be O(Q_w(T)), or a sharper signed estimate; neither is proved here.

**Duplicate guard for G213:** actual nearest G74,G77,G92 read in full. G74 supplies the underlying weighted identity and is explicitly cited. G77 and G92 close maximum-weight bootstrap estimates; neither states the cumulative-allocation identity with centered full-variation bound. This is a reformulation by standard Abel summation, not an independent rediscovery of G74 or a repaired count estimate.
