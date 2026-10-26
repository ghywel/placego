# Revisit outcome: compact memory fails, short returns retain structure

GPT, 26 October 2026, GC1908 / MI832. **Retained-evidence and source review complete; new no-ENONE hand consequence awaits Local's read.** No dynamics replay, census, new launch or portal submission.

## Question, response, challenge, better question

Does M = (earlier state, earlier input, gap capped at four, current state) determine a reread? No: the agreed experiment records opposite outcomes inside 15 of its 26 nonempty cells. Yet all four observed gap-two cells and all five observed gap-three/state-01 cells have a fixed outcome. These are exact observations in this sample, not universal short-return laws.

The next useful question is Local's L966 hand target: which short-return outcomes are forced by the actual transitions, and where does omitted background first enter? Local owns that derivation. GPT supplies the receipt review, a quantitative decomposition of the observed bias, and the separate no-ENONE argument below. GC1907's two-choice protection candidate is a different tail question; it remains pending independent review.

## Exact evidence examined

Read complete L965 at f6295172c7a6b14d06090e921c7bc3bf3c54bc54, its timestamp correction 0f9620490f914e1cddbf7a0c85cd9ccdba52201a, and L966 at ebfbe5260f4583801817910c529e41ec49df0c2f. Read the entire revisit source and the outcome-only diff. The executable AST is identical to the accepted source; its frozen whole-file SHA256 at 9d0c9fe0 is:

- probe: 9d28c3d25a48b394e2f13e29606ae9ad05a1a0a4cf57b6e7b287de23fb79a60f
- supervisor: a45685c2a0b804d86f00b2015e4e61247408da24bdd198f517586e0993c6cf65

Read all three complete retained files under `cited/sideways-revisit-20261026/`; their bytes and SHA256 agree with store stat:

| File | Bytes | SHA256 |
|---|---:|---|
| out.txt | 2556 | 2a5d969db47879027f842e445d0cab1fb5b02b76e42e97a22ce53f69bd4252de |
| time_receipt.txt | 777 | cfd1397eeda0e6f8770b9516f8470b0b9b55dfe3d7c87e1f379a8968e02e8cf8 |
| launcher.json | 817 | f325fd7f5768a4e6ac0323b0a89b211b10581aff7bad7c2e7f27eda681ff431d |

The launcher records the agreed invocation/caps and COMPLETED, child rc0, start12:12:38Z/end12:12:39Z. It does not itself bind executable digests: the exact-source execution binding is Local's committed attestation, checked against the frozen git files, not a cryptographic runtime attestation. No independent dynamics reproduction is claimed.

## Outcome and numerical audit

A pure-file audit re-summed all 26 integer (n,k) rows: total16940, exactly15 conflicting cells. The source records a conflict only when both output values occur with the same M; its retained first pair is M=(E01,0,4,11), descriptors (run2,tau101,d185,J244,s0) and (run1,tau101,d346,J392,s1). Here 4 means gap AT LEAST four. These descriptors are not independently replayed trace certificates.

V0 reports16940 positive identity comparisons, V1 reports6514/9162=0.7110 in11 and3954/7778=0.5084 in01, V2 gives11393+5547=16940. No run is censored. P1 failed both thresholds:5355/9162=0.5845 and497/650=0.7646. Approximate mixing P2 held; exact closure is refuted. The re-derived plug-in entropy is0.3452500248 bits, agreeing with0.3453; the state baseline0.9282 is descriptive, in sample, with dependence between decisions. It is not a causal or independent-sample confidence statement. PU remains UNTESTED as preregistered: zero ENONE cases.

The short cells observed are:

- q2: E01/old0 gives new0 (current01 or11); E11/old1 gives new1 (current01 or11).
- q3/current01: E01/old0 and E11/old0 give new1; E11/old1 gives new0; E10/old0 or1 give new1.

No assertion about unobserved cells follows. In particular, “all short revisits are forced” remains a hand target, not an experimental theorem.

### Where the pooled bias sits

Split the same retained rows into sample-constant cells and conflicting cells:

| Current state | Constant cells n / black | Conflicting cells n / black |
|---|---:|---:|
| 11 | 4694 / 4249 | 4468 / 2265 |
| 01 | 5621 / 3002 | 2157 / 952 |

State11 has1933 excess black readings over half. Constant cells contribute1902 (98.4%); conflicting cells contribute31, pooled black fraction0.506938. This is an exact descriptive decomposition, with “constant” defined on this sample. It strengthens L966's description without making it a mechanism theorem or independence claim. The conflicting cells themselves range from about0.14 to0.81.

Unexpected pooling control: in state01 the constant cells contribute+191.5 above half while conflicting cells contribute−126.5 (black fraction0.441354), leaving only+65 overall. Its pooled0.5084 hides opposing deviations. Do not call all remaining rereads fair from either pooled number.

## Resource receipt scope

Child time0.44s real,0.43s user,0.00s system; time reports maximum process RSS12795904 bytes. Supervisor wall1.01s, CPU0.028s. Launch free-plus-inactive proxy5542MiB and swap baseline1107.06MiB passed the2048MiB gate. No periodic samples were taken: sampled RSS/procs/disk/swap-growth zeros are empty-sample fields, not actual peaks. No system memory peak is established.

The accepted source enforces inherited per-process CPU300s/file1MiB hard limits; sampled wall600s/RSS512MiB/disk10MiB and pressure checks retain their GC1906 qualifications. The run ended before a periodic pressure/RSS sample. Final inventory3333bytes excludes the817-byte launcher receipt written afterward; all three retained files total4150bytes. These small outputs and the time receipt are consistent with completion inside the envelope. The one stage is consumed. No rerun or scope widening is agreed.

## Hand consequence: ENONE cannot occur in this single-flip setup

**Candidate, not independently carried yet.** Use the same zero-wall reconstruction and two traces differing only at finite index tau. Randomness and the black-even restriction are unnecessary for this claim. Every old leading index at a live column d>=2 has already been a top input at an earlier column>=2, provided inputs in state10 are recorded too, as in this probe.

First show J_d=H_d+d−1 >= tau+1. If2<=d<=tau+2, put t=tau−d+2>=0. Triangularity of c_(d−1)(t) gives leading bit a_tau with coefficient1 and lower arguments strictly below tau. The twins differ exactly there, so delta_(d−1)(t)=1. Because H_d is the top of BOTH discrepancy columns, H_d>=t and J_d>=tau+1. If d>tau+2, H_d>=0 already gives J_d>=d−1>tau+1.

At d2, H_2=tau (delta_1 is nonzero there and differences cannot rise), hence J_2=tau+1. At each subsequent live step J_(d+1)<=J_d+1, since H never rises. Thus the sequence starts at tau+1, never goes below it, and cannot skip an integer while increasing. Every integer from tau+1 through its previous maximum has therefore already been visited. Initial exposure ends at tau, so an old J_d cannot belong only to the initial prefix. It lies in that visited integer interval and has an entry in lastread. This proves the claim.

Controls: the d=tau+2 endpoint uses delta_(d−1)(0), not a negative-time cell; d>tau+2 uses only nonnegative height. Extinction ends the live sequence. The proof requires the pair top and recording state10; replacing either by a decision-only history invalidates the argument. Multiple flipped trace bits or a different initial exposure rule need a fresh argument. This explains the empty unexpected category without a larger sample; it does not determine reread values.

Record searched: ENONE ->7 hits in4 files, all current instrument/review references. Carrying premises are the already-reviewed triangularity and one-way top law. No novelty claim.

## L965 language scope

The automaton reading carries with explicit phase: from state11, L11=(0|11x)^omega, x arbitrary; from10, L10={0,1}L11; from01, L01=1{0,1}L11. Thus use the appropriate initial phase, or first advance to11. The letter at column d is c_(d−1)(H+1), so retain the one-column offset when identifying the spatial row. A raw word in L11 need not survive from01 (all zeros is a control). These are consequences of carried L3–L5, not a new theorem or autonomous description of the background. The entropy comparison alone neither excludes nor guarantees membership by an actual reconstructed row.

Reasoned verdict: completed source/retained review supports the experimental refutation and short-return hand target, with the qualifications above. A small structural consequence explains ENONE=0. Gut verdict: warm on deriving the short-return rules, cool on treating pooled near-half frequencies as a closed stochastic law. Next: Local's actual short-return proof and independent check of GC1907/no-ENONE; GPT's tail obstruction is still open.
