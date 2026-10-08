# Proposition 19 (hand proof, second-read): no finite Rule 210 seed keeps the full 0101 clock

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "32. Proposition 19 (hand proof,
second-read): no finite Rule 210 seed keeps the full 0101 clock"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** second-read.

## In plain words

No finite starting row of Rule 210 can make the centre alternate white and black forever.

**What it says.** For any finite left side, the only possible alternating-centre realization is the parity background already identified in G65, and that realization needs infinitely many black cells on the right. A first change from it sends a clearing front through pairs of diagonals and eventually meets a black background gate, where the centre clock fails.

**Why it matters.** This replaces the radius-six bound of entry31 with a hand proof for every finite radius, and proves Local's conjectured2w life law. It is an auxiliary Rule210 theorem; Rule30 still needs its own argument. Local supplied the conjecture and independent orbit evidence, GPT supplied the proof, and Local verified it by hand.

**An everyday picture.** A travelling reset can pass a finite run of open gates, but reaches a closed gate eventually. Arbitrary choices farther along cannot repair the failure.

## The formal statement and proof

*Where:* RULE30-GPT.md GC478; independent Local hand reading L285, published at60865af; actual-orbit FR controls.
*Bears on:* Rule210 question B; entries29 and31, whose finite-radius statements are special cases.
*Credit:* The conjectured2w life law and PL/SB3/FV/FR evidence are Local's (L282); the clearing-front proof is GPT's (GC478). Local independently verified every hand step, including the left-row scope and tau0/w0.
*Status:* second-read. Auxiliary Rule210 result, not Rule30 and not a prize claim.

**Statement and dependencies.** With centre clock x_t(0)=t mod2, every finite initial-left row admits at most one full realization. Odd-supported rows have exactly G65's parity-sparse realization, whose right seed is infinite; rows containing an even left site are excluded by G27.3. Hence no finite global initial seed realizes this clock. Use diagonal D_c(s)=x_s(c-s). For a first positive right difference e from the G65 background, GC472 excludes odd e. For even e its diagonal is1 until the preceding odd background diagonal b first becomes black at tau, and0 thereafter, with tau<=e-1. GC476 gives the background gate transport and finite first-black gate. The quantified proof below is copied from GC478; it uses those independently reviewed lemmas, not a finite graph or census.

**Pair variables.** Write candidate diagonal pairs as P_j(s)=D_(e+2j)(x,s), Q_j(s)=D_(e+2j+1)(x,s). For j>=1 their updates, with U=P_(j-1), B=Q_(j-1), are

    P_j(s+1)=U(s) XOR ((1-B(s))*P_j(s)),
    Q_j(s+1)=B(s) XOR ((1-P_j(s))*Q_j(s)).

Define the marker M_j=(1-P_j)*Q_j, which means the pair is01. Direct binary algebra gives the key identity

    M_j(s+1)=(1-U(s))*(B(s) XOR M_j(s))
              =M_(j-1)(s) XOR ((1-P_(j-1)(s))*M_j(s)).

If U=1, the next marker is zero. If the input pair is01 and the current marker is zero, the output pair is01: Pnext=0, Mnext=1. This is a clearing pulse followed by a front, not a statement about the candidate's literal first black cell.

**Clearing-front propagation lemma.** Suppose an input pair has a time t with Pprev(t)=1, has Mprev(s)=0 for t<=s<T, and is01 at time T>t. Then the output pair has some clearing witness t' in{t,t+1}, has P(t')=1 and M(s)=0 for t'<=s<T+1, and is01 at T+1.

Proof: choose t'=t if P(t)=1, and t'=t+1 otherwise. In the latter case the first update has P(t+1)=1 because U(t)=1 and P(t)=0. In either case M(t')=0. Since U(t)=1, M(t+1)=0 independently of all prior values. From t+1 through T-1 the input marker vanishes, so Mnext=(1-U)*M preserves zero. Thus M(T)=0. At T the input pair is01, so the next output pair is01. The same argument proves every asserted intermediate zero; no unmentioned initial-tail restriction is used.

**Base front and induction.** Let e be a first even initial deviation from G65, and tau the preceding odd diagonal's first black time. GC472 gives P_0(s)=1 through tau and0 afterwards. At s=tau its own next odd update resets Q_0(tau+1)=b(tau)=1. Thus pair0 has a clearing witness t_0=tau, marker zero through tau, and is01 at T_0=tau+1. Iterating the propagation lemma yields, for every j, a witness t_j<=tau+j with P_j(t_j)=1, marker zero from t_j through T_j-1, and pair01 at

    T_j=tau+j+1.

This candidate front statement alone holds for arbitrary later suffixes; it does not yet identify their background errors.

**Identification with the parity background.** Let w be the first initially black odd background gate: A_j(0)=0 for j<w and A_w(0)=1, where A_j=D_(e+2j+1)(y). GC476 proves that A_j stays at its initial value through tau+j and flips at T_j. Hence A_j(T_j)=1 for j<w and A_w(T_w)=0. Every background even diagonal is white.

For j=0, after T_0 the candidate first even diagonal is zero, and candidate/background odd diagonals accumulate the same b. Their error is therefore constant, equal to A_0(0). Induct on j<=w. When j>0, the preceding pair is a passing gate and already equals the background from T_(j-1) onwards. At T_j the candidate pair is01. If j<w this agrees with the background pair01; thereafter both obey the same recurrence and remain equal, with P_j=0. If j=w the background pair is00, so the odd error is1. The preceding even input is zero forever; the current P_w stays zero and both odd tracks accumulate the same preceding odd input. The error remains1 forever. Thus, for every j<=w and every s>=T_j,

    P_j(s)=0,  Q_j(s) XOR A_j(s)=A_j(0).

This is stronger than the tested tau+1+2j settling bound. Its proof covers tau0, w0 and arbitrary later b histories.

**Clock consequence and finite-left exclusion.** Since tau<=e-1, T_j<=e+j<=e+2j+1, and for j>=1 also T_j<=e+2j. All earlier clocks agree by first-difference locality. The first even pulse passes its own clock; every later even clock up to e+2w is white, and every odd clock before e+2w+1 passes. At e+2w+1 the frozen error is1, so that clock fails, regardless of every subsequent initial bit. This proves the exact2w life law.

For any finite odd-supported initial-left row, G65's parity background has R_0 beyond its left radius, so GC476 proves w is finite for every even e. An alternative full0101 member has a first right difference. An odd first difference is impossible by GC472; an even first difference now fails at a later odd clock. Hence the G65 background is the unique full0101 realization of that left row. G27.3 proves that any full0101 left system has initial ones only at odd depths, so all finite initial-left rows are covered. G65's right seed is infinite beyond the left radius; therefore no finite global initial seed has a full0101 centre clock. No assumption of near-wall periodicity, fixed radius or tail truncation enters this conclusion.

**Predictions and controls.** Before running, predict the sharper front/settling times on GC477's abstract cases. The initial sharpened query found no failure. After deriving the clearing-marker identity and witnesses, check all16 input/output pair choices by literal decimal Rule210 and each constructed witness on all10880 abstract cases:40064 front witnesses pass, as do the sharper settling values. Unexpected: the first failing background gate also has the candidate01 front; it fails by its error, not by absence of a front. Omitting the clearing premise fails: input01 with target01 outputs00, not01. Reproduction: `tests/probes/lexicon/rule210_gpt_clearing_front.py`. These are proof controls, not a substitute for the quantified propagation lemma. GC477's earlier indexing failure remains retained.

*Independent reading (Local L285).* Pair updates, marker identity, clearing-witness interval, base and identification all checked by hand. G27.3 uses only the left wall equation, so arbitrary right continuations do not escape its odd-support premise. The separate FR instrument checks235892 actual-orbit tail cases, with sharp settling; these finite controls are evidence about the instrument, not replacements for the induction.
