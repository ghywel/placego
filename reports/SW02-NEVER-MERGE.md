# When two rows can never merge

*Local, L1579, 6 November 2026. The owner asked me to catch up on Cloud's and GPT's reviews and to try for a proof that two rows never merge, if the target still stood. It did. Probes and predictions: [`tests/probes/swarm/sw02/amplifier/`](../tests/probes/swarm/sw02/amplifier/). About 390 CPU seconds on the M5, by the time receipts. There is no statement about Q01 here, and no new Lean.*

**Answer: proved in part, and the part that fails now has a measured reason.**

- **Proved.** Every nonzero row carries one 2-adic number ν, constant on merge classes at any lag. Rows with different ν never merge. There are infinitely many futures, and M(W) ≥ Π(W). In [L1578](SW02-CLASS-AMPLIFIER.md) I wrote that M(W) could be bounded for all I could prove. That is now false.
- **Exact values.** M(1), …, M(6) = 1, 2, 2, 3, 5, 9. Every future at these widths is proved distinct, with no plateau assumption.
- **Measured.** Every class tested has an exact integer clock, and ν is that clock mod 32. If the lock is permanent, M(7) = 15.
- **Not proved, and not reachable this way.** Most rows share a clock. Through W = 14 the clocks number 148 against 312 apparent classes, and the ratio is falling. So the left side cannot decide most pairs, whatever depth it is read to. A general certificate has to look below the front.

| Result | Status |
|---|---|
| Theorem N: the invariant ν, M(W) ≥ Π(W), M unbounded | PROOF-SKETCH, hand, awaiting a read |
| M(1..6) exact | On Theorem N; finite computation in C and in Python |
| Certified lower bounds for W = 7 to 14 | On Theorem N; COMPUTED, C only |
| Integer clock, no drift, ν = clock mod 32 | COMPUTED, self-check |
| Lock conjecture | CONJECTURE |
| Left-side tree | KNOWN, reproved: Gravner–Griffeath 2012 §8, kit four sides, CL738 sixteen sides in Lean |
| Clock lock, in kind | KNOWN in kind: CL746 and Berzai Prop 6.3. New here: the width term, the merge invariance, ν as its residue |

## 1. Theorem N

Let L(v) = 4v ⊕ (2v ∨ v), and L_K = L mod 2^K on odd residues. Let V_K(Y) be the top K cells of a row of width at least K, read inward. GPT's identity, which I carried (§5), gives V_K(FY) = L_K(V_K(Y)). So for any nonzero Y the sequence V_K(F^t Y) enters a cycle of L_K, and L_K permutes its periodic points Per_K. For large t define

ν_K(Y) = L_K^−(t + width Y) (V_K(F^t Y)).

**Theorem N.** (a) ν_K does not depend on t, and ν_K(FY) = ν_K(Y). (b) ν_K reduces to ν_K′ for K′ ≤ K, so ν(Y) = lim ν_K(Y) is one odd 2-adic number. (c) If F^a Y = F^b Y′ then ν(Y) = ν(Y′). (d) Every point of Per_W is ν_W of a row of exact width W. Hence M(W) ≥ Π(W) = |Per_W|. (e) Π(W) → ∞, so M(W) → ∞.

*Proof.* (a) V_K(F^t(FY)) = V_K(F^(t+1) Y) and the width rises by 1, so the exponent and the point both advance by one. (b) Reduction commutes with L and sends periodic points to periodic points. (c) follows from (a). (d) For p in Per_W put v = L_W^W(p) and X = reverse_W(v). Since v is odd, X has width exactly W, V_W(X) = v, and so ν_W(X) = p. Rows of one width with different ν_W have different futures. (e) Reduction Per_(K+1) → Per_K is onto: over a cycle of length P, L^P maps the two-point fibre into itself, and a self-map of a finite set has a periodic point. Kit `D_least_period_unbounded` gives, for each Q, a wheel j of the seed with no eventual period ≤ Q, so the seed's cycle mod 2^(j+1) has length above Q. ∎

This uses the sectors of L1578 at every depth at once, and it does not need the classification. **A certificate is a finite exact computation:** two rows reaching different ν_K are proved apart forever.

## 2. What the certificate reaches

Upper bounds are witnessed merges at a finite tick. Lower bounds are distinct ν at level 87,868.

| W | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| upper, N_4096 | 1 | 2 | 2 | 3 | 5 | 9 | 15 | 23 | 35 | 53 | 76 | 125 | 193 | 312 |
| **proved lower, ν** | 1 | 2 | 2 | 3 | 5 | 9 | 13 | 17 | 22 | 25 | 29 | 32 | 32 | 32 |
| clocks (needs the lock) | 1 | 2 | 2 | 3 | 5 | 9 | 15 | 21 | 30 | 44 | 60 | 87 | 114 | 148 |

The two bounds meet through W = 6, so **M(W) is exact there**. W = 6 needs the doubling at wheel 87,866: only 8 of its 9 classes are apart at level 401. Python big integers reproduce the W ≤ 6 row independently. At W ≤ 8 reading down to wheel 894,236 adds nothing.

**Why ν stops at 32.** The tree reproduces the kit exactly and explains its limit: wheel 87,866 is itself white. But all 854 classes through W = 14 stay on the seed's strip, with no fork taken. This is §21.11's "one common fate", and it sank my reasoning that fork bits act like coin flips. So ν only reads a phase, and the next doubling on that strip lies past wheel 40,000,000, beyond any row simulation.

## 3. The integer clock

For large g let τ_g(Y) be the least tick from which V_g(F^t Y) is on its cycle, and θ_g(Y) = τ_g(Y) + width Y. Then θ_g(FY) = θ_g(Y), and merged rows share θ_g once g is past their merge.

**COMPUTED.** θ_g(Y) − θ_g(1) is constant in g, to the tick, for all 854 classes through W = 14 at depths 79,000 to 99,900, and for all 60 classes through W = 8 out to 199,800. Call it the clock c(Y). There is no drift in any class. Rows along one orbit share θ exactly. Across all 854 classes, ν is a function of c mod 32.

**Lock conjecture.** Every nonzero row has an integer c(Y) with θ_g(Y) − θ_g(1) = c(Y) for all large g. Under it, c is a class invariant, equal-width rows with different clocks never merge, and M(7) = 15.

**Why it is not a theorem.** Agreement of the top g wheels at lag d is permanent, because wheels are autonomous, and `extend` pushes it deeper at each black parent. It can fail only if the strip front overtakes the pair front. That needs a parent word white across their whole gap in the transient region, and I cannot exclude that without a pseudo-randomness statement of the reset-gap kind. The measured gap is 99 to 804 wheels at t ≤ 60,000, growing. Merging at lag 0 would force such an unlocking, so never-merge for these pairs is exactly permanence of the lock.

## 4. Where the left side ends

Clocks range over −109 to 143 at W = 14, while the classes grow like 2^(0.6W). Distinct clocks over classes fall 1.0, 0.91, 0.86, 0.83, 0.79, 0.70, 0.59, 0.47 from W = 7 to 14. If the plateaus are real and the range stays small, exponentially many classes share a clock, and ν, being the clock's residue, cannot separate them at any depth. So P17 (ν is complete) is in serious doubt, though a plateau proves nothing by itself.

**A second front.** Same-clock pairs do not differ at the strip front. At (129,154) and (145,157) the fronts agree exactly, and the first difference lies 115 to 552 wheels deeper at t ≤ 60,000. Locked pairs at lag 96 and lag 32 look the same. So the row reads: strip, then a transient shared by same-clock rows, then a second front, then the part that differs. That second front is where a general certificate would have to work.

**Correction to L1578.** I read "damage top / t = 0.2535" as damage growing in a chaotic core. Most of those pairs have different clocks, so that number is largely the strip front itself.

## 5. The two carrying reads GPT asked for (GC2714)

**S(b), width-K witnesses: CARRIED.** I derived V_K(FY) = L(V_K(Y)) from the bit formula. New bit j is Y_(W−j+1) ⊕ (Y_(W−j) ∨ Y_(W−j−1)), which is v_(j−2) ⊕ (v_(j−1) ∨ v_j), and W ≥ K keeps every index at or above 0. Kit `rows_finite` gives v < 2^K and v odd, so reverse_K(v) has width exactly K, and 2^m X_v has shift 0 and width K + m. This is cleaner than my padding argument. All 64 sectors stand, and one class leaves 63.

**Branch selector: CARRIED.** I re-derived every step in GPT's frame, not from its text: the corridor T1 = T2 = T3 = 0; gap 2 iff R2 = R3 = 0 and R4 ∨ R5 = 1; the image restriction that removes prefix 9; the case split at post-head positions 2, 3 and ≥ 6, including S = 0 1 ¬c 1 and F²(R) = 0 0 ¬c; gap 3 iff low5 = 23, with b = 0 forcing R5 = 0; and the seven-cell set {25, 49, 89} with R7 = d ∧ (e ∨ f). All correct.

GC2711's other corrections are accepted: one class leaves 63 sectors, the e_36 = 9 witness is 817, and the finite data do not settle bounded-gap P5.

## 6. Predictions

| # | Prediction | Result |
|---|---|---|
| P14 (0.9) | The tree reproduces the kit's wheels and thresholds | **HELD**, exactly |
| P15 (0.7) | 53 classes of width 10 give 28 to 45 values of ν | **FAILED**: 25. I had warned of this before the run |
| P16 (0.6) | All 23 classes of width 8 separate by K = 300,000 | **FAILED**: 17, none added past 87,868 |
| P17 (0.5) | ν is complete | Unresolved; serious doubt, §4 |
| P18 (0.65) | Fronts lock at a constant offset | **HELD**, no drift in 854 classes |
| P19 (0.5) | Most width 7, 8 collisions have different clocks | **HELD**: 7 of 9 pairs |
| P20 (0.7) | Distinct clocks over classes below 0.6 at W = 14 | **HELD**: 0.474 |
| P21 (0.6) | Same-clock damage within 2% of the strip front | **HELD** (0.8% to 1.8% in wheels at t = 60,000), but the gap grows, so it is a separate front |

## 7. Limits and errors kept

- Theorem N is my hand argument and stays PROOF-SKETCH until read. Part (e) rests on the kit's single-seed theorem.
- N_t only bounds M(W) from above. Rows 7 to 14 of §2 are bounds, not values.
- Only W ≤ 6 has a second-language replay. W = 7 to 14 lower bounds rest on `left_nu.c`, controlled against Python at K = 448.
- Distinct hashes prove distinct values. Equal hashes do not prove equal values, so the counts are safe as lower bounds.
- Clock offsets were read over bounded depths. "All large g" is the conjecture.
- `left_nu.c` first cleared one buffer only, and the Python control caught it before any result. One clock run was invalid: zsh did not split the depth list, and depths below 0.75K are unobservable. One pair in the first `pair_front` run used the wrong lag sign, and it is rerun. My K = 894,236 run stopped at its own 280-second cap at 69 rows.
- The next doubling on the seed's strip was not located: the tree stops at wheel 40,000,000 with no further event.

**Evidence:** `cited/local/never-merge-20261106.tar.gz`, 26,913 bytes, SHA256 `75a248a0d1f23310934218faf6b8a17c05082a1f3490b1e5f41ad403ef3158c4`.

**Record searched:** GC2711, GC2714, CL753, CL738, CL746, CL749, CL750, CL752; atlas §§21.5–21.11; `Rule30FourLeftSides`, `Rule30LeftUnbounded`, `Rule30LeftReset`; AM-2 §6; genealogy §25. `record_find` on 165,748, 183183, 229337, 894,23, sixteen left, 87,866 is white, and left side with merge (two hits, not read beyond their headings). `known_find` on left sides, sixteen, exactly four, merge. PR 145 only for left sides. No clean keyword search is novelty clearance.
