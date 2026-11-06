# The class amplifier: what the pull became

*Local, L1578, 6 November 2026. The owner asked me to return to my L1573 pull while GPT works the bridge return state. Probes and predictions: [`tests/probes/swarm/sw02/amplifier/`](../tests/probes/swarm/sw02/amplifier/), with `prereg.txt` extended before each run. About 32 CPU seconds on the M5, by the time receipts. There is no unconditional Q01 conclusion. No new Lean.*

**GPT GC2711 carrying amendment:** Theorem C, Theorem S with the explicit width-K witnesses below, and Lemmas G/R under their stated map hypotheses are PROVED hand/two-party. The finite computations remain Local measurements; GPT read their source and evidence and rechecked the rate summaries. Padding arbitrary short rows, finite spatial edits, finite class births, independence and the registered bounded-gap prediction are narrowed below.

**Answer.** The pull as I wrote it is withdrawn, and a sharper question replaces it.

My sentence was: if immortal rows provably share futures with one orbit, a whole family of statistical routes closes outright. Both halves fail.

- **The consequence was already dead.** GC2702 showed that a finite-time bound N_m(W) = o(W) beats the floor. A linear q(W) closes nothing.
- **The hypothesis is not a shortcut.** By Theorem S below, a proof that immortal rows share one orbit would prove Q01 on at least 63 of 64 sectors of the positive naturals (62 for two classes). This particular one-orbit hypothesis therefore already proves many sectorwise Q01 statements; it is not a shortcut around them.

What survives is a family-by-family question, an exact count, and one measured fact: merging stops early and leaves thousands of apparent futures, of which only 64 can be proved apart.

| Result | Status |
|---|---|
| Theorem C: exact class count | PROVED hand/two-party, GC2711 |
| Theorem S and its corollary: sectors | PROVED hand/two-party with width-K construction, on kit theorems, GC2711 |
| Lemma R: block maps cannot raise the right-edge rate | PROVED hand/two-party under the stated Lipschitz/periodic-intertwining hypotheses, GC2711 |
| Rate census | COMPUTED, self-check |
| No stable phase effect detected in the finite W = 32 comparison | COMPUTED, Local; no independence theorem |
| Merge plateaus through W = 20 | COMPUTED. Known from AM-2, reproved here with longer caps |

## 1. Theorem C: the exact class count

On immortal rows write y ~ z when G^a y = G^b z for some a, b ≥ 0. This is an equivalence, and the width law makes a, b rigid: width y + 2a = width z + 2b. Let v_C be the least width in a class C, and o(W) the number of classes with v_C ≤ W.

**Theorem C.** q(W) = Σ over classes with v_C ≤ W of (⌊(W − v_C)/2⌋ + 1). Hence q(W) − q(W − 2) = o(W), taking q(V)=0 for V<0. Here o(W) denotes the class count, not Landau little-o.

*Proof.* For large k the survivors of width at most W are exactly the immortal rows I_W, because the population is finite. Rows y, z in I_W agree at some late tick iff y ~ z and they have equal width: agreement gives y ~ z, and the width law gives equal width; conversely equal width in one class forces a = b. For a fixed W, take one time after all mortal roots have failed and all coalescing equal-width immortal pairs have merged; finiteness permits this, without a uniform-in-W bound. A class occupies exactly the widths v_C, v_C + 2, …: parity follows from the merge width equation, and every listed width occurs by iterating a least-width representative. So late rows correspond to pairs (class, width ≤ W), which gives the sum. Each term rises by exactly 1 from W − 2 to W when v_C ≤ W, which gives the difference. ∎

So Theorem 1 of Block 5 is the one-class case. q(W)/W tends to infinity exactly when o(W) is unbounded, and if o is finite then q(W) = (o/2)W + O(1). The cited guarded twins, AM-3 partners, tock flips and guarded predecessors stay in their original class (AM-1 §3.2). They do not create new classes, though a lower-width representative can improve that class's finite-width contribution. **Superlinear amplification requires unboundedly many classes**; one extra class changes the linear slope. By `Rule30PrefixMerger.trace_tail_iff_row`, two rows are in different G-classes exactly when their full temporal column traces differ infinitely often after every pair of even time shifts. Finite edits of a temporal trace preserve its tail and cannot do this. Arbitrary finite spatial edits can change the class; all finite naturals differ by such edits.

## 2. Theorem S: why "one orbit" is not a shortcut

Let L(v) = 4v ⊕ (2v ∨ v), the kit's map in `Rule30FourLeftSides`, and K = 87,867. For a nonzero natural Y and large t, let v_t(Y) be F^t Y read from its top cell through K cells. Then v_(t+1) = L(v_t) mod 2^K. By `odd_reaches_one_of_four`, `least_period_16` and `four_distinct` there is a unique strip σ(Y) among A0, A1, B0, B1 and a unique s(Y) mod 16 with v_t(Y) = L^(t+s(Y))(σ(Y)) for all large t. Define the **sector**

ι(Y) = (σ(Y), s(Y) − width Y mod 16).

**Theorem S.** (a) If F^a Y = F^b Y′ then ι(Y) = ι(Y′). (b) All 64 sectors occur among the naturals.

*Proof.* (a) σ(FY) = σ(Y), s(FY) = s(Y) + 1 and width FY = width Y + 1, so ι(FY) = ι(Y). Then ι(Y) = ι(F^a Y) = ι(F^b Y′) = ι(Y′). (b) For width(Y)≥K, let V_K(Y) be its highest K cells read inward. Directly from F(Y)=(Y>>1) XOR(Y OR(Y<<1)), V_K(FY)=L(V_K(Y)) mod 2^K: the new depth-j cell uses only old depths j−2,j−1,j. Width increases, so this remains autonomous forever. For each kit strip v in {A0,A1,B0,B1}, `rows_finite` gives v<2^K and bit0(v)=1. Choose X_v=reverse_K(v), a natural of width exactly K. Then V_K(X_v)=v and its shift is0. Every Y_m=2^m X_v, m≥0, has the same top K cells and shift0, but width K+m. Thus its sector is (v,−K−m mod16); m=0,…,15 realizes all sixteen phases of every strip. This proves64 sectors among positive naturals. It does not assert that padding an arbitrary short F-row preserves that row's strip/shift. ∎

**Corollary (the barrier).** If the immortal rows form at most k classes, they meet at most k sectors, so Q01 holds on at least 64 − k sectors. In particular one G-class gives Q01 on at least63 sectors; at most two G-classes, for example one per width parity, gives at least62. Each G-class lies in one F-sector because G=F^2. Zero is outside this positive-row sector partition.

For rows of width≥K, multiplying by2 rotates the sector, but it does not preserve immortality, so no symmetry I know moves the last sectors onto the others. If one existed, "one orbit" would imply Q01 outright.

**Computed support.** All 16 phases occur by width 12, with unequal shares (33 to 272 of 2048). At the tested depths K=32,…,400 the period is8; at the tested depths K=401,…,512 it is16. Depth400 includes wheels0–399; depth401 includes wheel400, which the kit proves has primitive period16. Smaller tested depths8 and12 have periods2 and4. Merges and orbits preserved the phase with no violation at width up to 13 and on rows below 2^11, and the raw shift without the width term fails, as it must. Strips fork only at wheels 53,208 and beyond, so strips were **not** censused. Every computed sector here is a shift sector.

**No stable phase effect detected in this finite comparison.** At W = 32, over the 8 phases of depth 64, pass rates at each check from t = 32 to 46 (N from 12,807 down to 95) give largest |z| = 2.5. One check of eight has χ²(7) = 16.7, which is about p = 0.02 alone and unremarkable over eight checks. These are descriptive binomial/chi-square comparisons for a finite deterministic population. They establish neither phase independence nor independence across repeated checks, and do not compare the four full strips.

## 3. Merging stops early (known, reproved, caps extended)

Let N_t(W) count distinct rows at tick t among rows of exact width W, and M(W) its limit. Applying Theorem C's argument to all rows under F, M(W) − M(W − 1) counts classes first born at width W.

| W | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N_4096 | 1 | 2 | 2 | 3 | 5 | 9 | 15 | 23 | 35 | 53 | 76 | 125 |
| ΔN_4096 | 1 | 1 | 0 | 1 | 2 | 4 | 6 | 8 | 12 | 18 | 23 | 49 |

| W | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|
| N_4096 | 193 | 312 | 487 | 750 | 1143 | 1784 | 2795 | 4266 |
| ΔN_4096 | 68 | 119 | 175 | 263 | 393 | 641 | 1011 | 1471 |

The displayed differences are finite-time count differences, not certified new-class births; only the true limits M(W) have the class interpretation.

**Prior art.** AM-2 §6 already has this plateau: 23, 125, 750, 4266 at W = 8, 12, 16, 20, last merges 63, 196, 219, 305, and last merge plus W constant on runs of W by orbit inheritance. What this run adds is reach and labels: flat through t = 32,768 at W = 10, 12, 13, 14 and through t = 4,096 to W = 20, last merge by tick 312 throughout, all 16 phases present at each plateau, and no two-phase merge.

**The strong form of the pull has no support, and is not refuted.** The strong form says rows of equal width and sector always merge, which would leave finitely many master orbits. The counts sit far above 64 by W = 14 (312). In the 296 unmerged same-phase pairs at W = 14, the damage reaches 0.232 to 0.2552 of the tick, median 0.2535, so it is growing and not fading. The median is above the central estimate0.246 but within its quoted ±0.01 interval (§8.66); these numbers do not establish a discrepancy. But **N_t only bounds M(W) from above**. A plateau is evidence, not proof, that two rows never merge. Beyond the 64 sectors, I know no proof that any two rows have different futures. M(W) could in principle be bounded for all I can prove.

## 4. Candidate H: what moved and what did not

AM-5's Candidate H is the right bounded form of the pull: a one-sided block map on column words with A(N) ⊂ N and width cost w is 0 or F^j. Write c = r + w. Candidate H remains **open for all radii**.

**AM-5's obstacle applies to the seed-only form.** AM-5 feared that "A(1) = 0 forces A = 0" needs col(1) to contain every word. H quantifies over all naturals, and every word is a prefix of some natural's column, so a proof can pick its test rows. I found no implication from H to a statement about col(1). That is a negative search, not a theorem. It answers backlog item AM-5 (line 129) only that far.

**Lemma G (gap transfer).** If u in Z_2 is white on [a, b), then A(u) is white on [a + w, b − r). *Proof.* u mod 2^a is natural of width at most a, so its image has width at most a + w, and it agrees with A(u) below b − r. ∎ This restates the hypothesis, with b = ∞ the natural case. It is the useful form, because it holds inside any row.

**Lemma R (rate).** Let e_d(x) be log2 of the T-period of x mod 2^d, and let b_n = B_n(x), periodic with 2-power period Q (AM-5 §7). Whenever Per_d(x) ≥ Q, every value b of b_n has e_d(b) ≤ e_d(x). *Proof.* Ψ(T^k x) = T^k b_(r+k), and Ψ(u) mod 2^d depends only on u mod 2^d. Take k′ = k + Per_d(x). Both periods are powers of two, so Q divides Per_d(x). Then k′ ≡ k mod Q and T^k′ x ≡ T^k x; the 1-Lipschitz property gives T^k′ b ≡ T^k b mod 2^d. Cancel T^k using its permutation action modulo2^d. Thus Per_d(b) divides Per_d(x), proving the exponent bound. Choose k in each phase modulo Q to cover every value b; no transitivity of the orbit of x is needed. ∎

My registered form had a spare +1, which the sharp form removes. **Census (COMPUTED):** for the impulse of a single cell at c = 9, Q ≤ 2^6, valid from depth 10. Of the 512 odd values below 2^10, 469 fail by depth 62 and 43 survive. This holds for every radius with r + w ≤ 9 and uses nothing about col(1). It adds no coverage past AM-5's radius-12 box, and the survivors are many T-orbits with stable offsets, so the rate alone will not classify the impulse.

**What failed.** My first idea was that T is transitive on residue classes, so that one impulse fixes Ψ on a clopen set. It is not: e_44(1) = 18, where transitivity needs 42, and GC2157 had said so. O_1 is thin, so hardly any natural rows lie in it, and the transfer test was not run.

## 5. Predictions

| # | Prediction | Result |
|---|---|---|
| P1 (0.8) | Orbit of 1 mod 2^k has size 2^(k−2) | **REFUTED** (GC2157; e_44(1) = 18) |
| P2 (0.85) | Nontrivial b fails on every residue class | **NOT RUN**: premise gone with P1 |
| P3 (0.6) | No rational pattern in log_1(y) | **NOT RUN**: same |
| P4 (0.6) | Most odd b fail the rate, survivors close to {T^j 1} | **Half.** 453 of 512 fail in the registered form; survivors are not close to {T^j 1} |
| P5 (0.5) | Seed1 is slowest; registered form allows a bounded gap | Pointwise version **REFUTED**: e_36(817)=9 versus e_36(1)=13. The registered asymptotic bounded-gap claim is **UNRESOLVED** by finite data |
| P6 (0.7) | All 64 sectors occur at width ≤ 16 | **Checkable part HELD**: 16 phases by width 12, shares unequal. Strips not censused; 64 by hand, at large width |
| P7 (0.95) | Merges preserve the sector | **HELD**, no violation |
| P8 (0.7) | Survival independent of sector at W = 32 | Finite benchmark met, largest \|z\|2.5; independence unproved |
| P9 (0.75) | Plateau well above the sector count | **HELD** as a reading; not a proof of non-merging |
| P10 (0.6) | Last merges before t = 4096 | **HELD**, by tick 312 |
| P11 (0.7) | Plateau by t = 4096, exponent in [0.55, 0.65] | **HELD** |
| P12 (0.6) | M(W) monotone | **HELD** |
| P13 (0.5) | New classes at every W ≥ 2 | Finite differences vanish at W = 3 and are positive thereafter; true births unproved |

## 6. Limits and corrections

- Theorems C/S and Lemmas G/R are carried with the GC2711 guards above; the underlying all-radius classification is still open. Lemma R is conditional on its stated AM-5 structural hypotheses, not a carry of every AM-5 claim. Theorem C and part of §3 are vacuous under Q01 in the immortal case; the all-rows version is not.
- Theorem S rests on the kit's classification through wheel 87,866. If more left sides appear deeper, the sector count only rises.
- The census is finite, and Lemma R's threshold depends on Q, so each exclusion is stated for its c.
- The phase computations are mine alone, in one language, on the M5. No Wolfram result carries a status here.
- **Correction, in chat during this block:** I told the owner AM-2 read 4,266 as still falling, and that my run answered its open item. Both were wrong. AM-2 had the plateau, labelled as an upper bound. Its open item, a law for N_t(W) when t ≫ W, stays open.

## 7. What this changes

- **L1573-1 is answered as far as it can be.** The one-orbit hypothesis implies many sectorwise Q01 statements, so it is not pursued as a shortcut. Refute amplifiers one family at a time, as Candidate H does.
- **Statistical routes are untouched.** GC2702 stands, and Theorem C changes none of their hypotheses.
- **Three routes forward.** (1) Theorems 1 and 2 hold inside each sector, because a class sits in one sector. So a count law on one sector gives Q01 on that sector, a new kind of partial target. It is practical only for phases, since strips need depth 53,208. (2) Close Candidate H by proving memory flush: A(y + 2^M x) = A(y) + A(2^M x) for long gaps. Deriving a uniform finite spatial radius and a compatible whole-line extension from that identity would require further proofs before whole-line centralizer results apply. (3) Find an invariant finer than the sector, a certificate that two rows never merge. We can prove 64 futures apart and see thousands.

**Evidence:** `cited/local/class-amplifier-20261106.tar.gz`, 78,594 bytes, SHA256 `ab8e6f4d3f3eb04f6cc78970156c017ac624e4ab2b8e176ae31f184c02a987ed`.

**Record searched:** AM-1, AM-2 §6, AM-5, MM-1 reports; GC2702; GC2157; genealogy §§25, 29.1–29.2; `Rule30FourLeftSides`, `Rule30PrefixMerger` and the PROOFS L1514 entry. `record_find` on class amplifier, share futures, one orbit, CT4C, AM-1, MM-1, 3955, orbit floor, four left, odometer, unipotent, 4,266, 8,024, never merge, merge tick, eventual image, Lyapunov, damage front, front speed, side_unique. `known_find` on commut (71 hits) and merge (106 hits) were counted, not read one by one; Lyapunov, distinct rows and same future had none; left_side_classification hits are our own theorem. A web search gave no value for the left exponent of rule 30 that I could use. A clean keyword search is not novelty clearance.
