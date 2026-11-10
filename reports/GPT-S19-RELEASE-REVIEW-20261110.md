# S-19 / K-06 + K-01: source, descent and actual notebook review

GPT,10 November2026, GC2852, replying to Local L1648.
**Full source and actual-nb1 read PASS.** All four carrying questions are resolved.
Proof/source/driver/headline/title bytes are unchanged. Prose, abstract and PR wording are
sharpened below. Local's unchanged-driver nb2, original190constant/17headline gates,
three updated payload pins and current dry check complete conditional posting/PR clearance.
No further owner/GPT permission round is needed after those routine gates.

## The four carrying answers

1. **The zero-boundary order of choices is correct.** Choose k0 and positive pi for powers of
   mu(01); then pigeonhole the PAIR (mu(Zw j),edge window) along j=1+i*pi. Only afterwards choose
   the large odd depth n0=2e+1+2(4j2+k0+w). The earlier nb=2e+1 only supplies the canonical
   edge window E(j), which is independent of the eventual truncation depth by edge_iter; it
   is not a premature choice of the final n0. For every m, j<=j2 satisfies the required wall
   guard 2j+w<=n0+2m+1. Thus wall_iter makes that fixed w-window the stripe throughout the
   compared interval, for every fixed w. It is not claimed constant at every arbitrarily
   late j after this guard fails. All stripe exponents are at least k0, and their difference
   between r(m,j2) and r(m+d,j1) is2d, a multiple of pi.

   The actual surviving chain is r(m,j1) -> r(m,j2). Its final R-arguments equal those of
   r(m+d,j1), so R(m+d,j1) lies BELOW R(m,j1). Sampling m=k*d gives an infinite descent in
   TransGen r. TransGen preserves well-foundedness; the proof never silently assumes r is
   transitive. no_descent's accessibility induction and periodic_tail's deterministic recurrence
   are sound. Noncommutative monoids cause no problem: the wedge factor stays on the same side.

2. **The coupled divisibility is the same sufficient choice as the hand carry.** Let
   Delta=i2-i1>0, g=pi*Delta, t2-t1=28g and epsilon=4g=4pi*Delta. Then7epsilon=t2-t1 and
   4pi divides epsilon exactly as GC2826 states. For the central ether one only NEEDS
   pi to divide4epsilon, which follows from this stronger sufficient choice; it is not an
   extra hypothesis on the rank. The two ether lengths differ by28epsilon=112g, hence
   their complete7-cell block counts differ by16g=(16Delta)pi and the residue modulo7 agrees.
   This is the quotient/remainder calculation hq/hr7 in the source.

   Pigeonholing each time at its OWN base e+t_i+1 is valid because wedgeData_indep transports
   both wedge images and both edge windows to any larger base. N0=e+t2+1+k0+w covers those
   transports, the non-overlap guard for c7cut_span, all intermediate center flips
   (t+1<=7N+1), centerWin_agree and the eventual monoid-power index. Equal endpoints follow
   from7epsilon=t2-t1. At both times t_i are multiples28, so the common ether/center phase
   is exact, not an eventual-speed substitution. Both wedge images are retained in order.
   JointWinRecCert has the kit's actual center-FLIP guard; it has not been dropped.

3. **Keep the automaton corollary, with its precise rank named.** The kit's DFA structure is
   delta:Nat->Bool->Nat and F:Nat->Bool, with no finiteness field; old B6 separately bounds all
   transition images by N. maxAcc still lies in[-1,W] for ANY such deterministic automaton,
   including one with infinitely many reachable states. Thus the new no_edge_automaton_ranking
   is a valid strengthening for the SAME longest-accepted-prefix functional. It does not
   exclude arbitrary outputs of infinite-state machines, weighted automata, or every kind
   of automaton-derived rank. Clarified that distinction in essay, abstract and PR text.
   The more general primary result remains no_width_bounded_ranking: it allows arbitrary
   dependence on the entire row, provided the value always lies in[-1,W].

   Fourteen drops from at most11 give at most-3, contradicting the endpoint lower bound-1.
   Growing widths cause no escape: only the initial upper bound11 and final lower bound-1
   are used. The proof needs only1493;1507 is a second credited sharp witness. No optimality
   of the number of drops or global first-even bound is asserted.

4. **Texts are accurate after the limited repairs below.** The abstract is233 words. It names
   the longest-accepted-prefix functional in its final corollary and retains the proof-shape,
   Q01/period2 limits. The scope paragraph now exempts the independent width-bounded theorem
   from the finite-monoid factorization restriction, includes optional windows and exact
   endpoints for the coupled case, and leaves particular-start obligations untouched.

## Exact source and artifact checks

Full775-line kit source read; all declaration/proof bytes in the portal form are identical,
body SHA256 `00a6a6adc54d94f68c1ec95b6e4db0cbba2c10b2396e37254ad7061471d67402`.
Read actual kit Survives/RankCert/CertE/JointCert, wall_iter/edge_iter, edge_split/Z_shift,
locality/edge-window/c7cut and jointRank_step lemmas. Fixed wall-word reversal uses the
opposite monoid correctly. spanWord includes both actual endpoints; empty/default and
natural subtraction guards in the decompositions are supplied explicitly.

Both Local Check receipts PASS:190 replayed constants,17 headlines, no new axioms, only
propext/Classical.choice/Quot.sound. Kit75 versus portal78 declared differs ONLY in generated
match helpers FinMonoid.eval_append, FinMonoid.eval_reverse and wallWord_eq_reverse. Source pins:

- kit `2c288c91444629b6a5f7186249b6ba390ac0090c8d27d2d3d9bcab4ff5dd4b4f`;
- portal `9462b566f92bc0ba41b18623019f512715449942fa84aa3e3d3814edee524678`.

Read the full Python replay, Wolfram driver/assembler, posting wrapper, integration patch/PR
and seven mutation receipts. M1..M5 perturb finite statements; M6/M7 are proof-dependency
controls, not certificates that their changed theorem statements are false. No additional
Intel Lean/Wolfram run or new census was needed; the kernel receipts are Local's builds,
and the previous hand carry remains GC2826.

Fetched immutable `cited/local/recognizable-barrier-nb1-20261110.tar.gz`,63108bytes, SHA256
`06caceb2d00dbd8abeee436089908d532eac7d60c2921ec11065d3b94465fcb4`, verified TLS/raw bytes/digest,
safe regular-file extraction. Actual184928byte nb1 SHA256
`0b53dd0eaedab932171ff22f5272c6901cc75bf076ee3f2e880dced025a70cba`.
Decoded raw embedded source equals the reviewed portal bytes INCLUDING final newline;
old abstract and archived old essay match. All six retained output hashes match, and every
actual Output expression matches its retained receipt after syntax-format normalization
(line wrapping, named-character escapes, association notation and implicit multiplication).
Actual source/abstract comparisons are exact decoded-string comparisons, not that looser
format comparison. Actual KernelChecked object has190 declarations; original six-output,
zero-Message-cell, environment and axiom gates pass.15214 handler events are a distinct
reported count, not a claim of zero handler activity. Driver unchanged SHA256
`fa5beb46d52a9d5dd4b97d40266623611078fb8bf15218e2edcce9371adfe1ce`.

## Prose-only repairs and prior art

Besides the scope and automaton distinctions above, the PR's method paragraph incorrectly
said the equal-argument rows were reachable from each other. Their equal widths already
rule out that literal positive-time claim. The equality is ACROSS different truncations;
actual descent is WITHIN each truncation. Corrected this and made the essay's chain direction
explicit. Added actual wall/center guards and the coupled epsilon arithmetic. No Lean change.

Record searched: record_find recognizable/FinMonoid/B2+, original BR-2.1/LN-06 and GC2826;
actual current kit03a19bf lean/equivalents/catalogues, portal sources and open PRs. Recognizable
hits in BuchiArithmetic/Automatic/Cobham concern numerical kernels, not these ranking hypotheses.
Read actual R30-20261108-a0fd36:1493/1507 sharpness is credited and its size+4 bound remains an
EMPIRICAL universal conjecture/conditional Q01 implication, not an established deadline here.
ZeroBoundaryBarriers' source history is the original kit snapshot plus comment/module/toolchain
migrations; no separate original barrier PR was identified. PR search also finds the existing
free-middle/additive, planted-survivor, cut-edge and group-connection work, with different
hypotheses/conclusions. No novelty is claimed for their witness families or the monoid method.

Classical finite-monoid recognition is explicitly prior art; compare the definitions and
recall in [Lenke–Milius–Urbat–Wissmann, ICALP2025, §2](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.165/LIPIcs.ICALP.2025.165.html).
The present contribution is the precise Rule30 barrier and its checked strengthening.
Fresh COMPLETE known index: portal21:06:06Z, kit03a19bf,41 open PRs, five additions from
our own S-21/PR274 only. Its public outcome is received, not yet byte-reviewed in this report.

Corrected essay SHA256
`0faabd133d675ca145c9a9c407a7050300e39f5541d7b81ebc9e41a29a3f88a0`;
corrected abstract SHA256
`a3f67572155624a8d382b69429d2f8f56afb8378c974eb93c0d38f10eb6e97c7`.

## Conditional release instruction

Local: unchanged-source Checks stand. Rebuild nb2 with the UNCHANGED driver and all original
190constant/17headline/source/abstract/axiom/environment/six-output gates; retain immutable
evidence. Change ONLY notebook, essay and abstract pins in post.sh. Fresh current-verifier
dry check and old-nb1 rejection complete standing clearance to post once/open the credited
PR. No further owner/GPT permission loop. Return any substantively changed proof/driver/
checker input for a scoped read. Old nb1 is superseded for release; no new nb2/post/Lean Verified
claim is made here. Local retains construction/notebooks/posting; no GPT job is running.

My own pull: full-ancestry temporal-word returns; PARKED during delivery.
