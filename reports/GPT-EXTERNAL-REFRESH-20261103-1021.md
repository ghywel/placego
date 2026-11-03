# Portal and kit refresh, with a prose/source mismatch — GC2499

GPT, 3 November 2026. Complete `known_find.py --new` succeeded at
**10:21:10Z**, portal updated10:21:00Z, kit main unchanged
`c42f6e5133f61a47e99289fd4b6e0536fd8a0453`,30 open PRs.
24 added index units,0 changed,0 gone since GPT's08:52 complete check.
Units include sources and metadata, not24 separate discoveries.

Read PR103–108 descriptions and available conversation (none in the
snapshot), and the relevant actual-head theorem types. This is a scope
read, not a new full proof audit, build, or review-summary/closed-PR
audit. No novelty/submission decision is made. The four new portal
entries are publicly Lean Verified/partial, with replay counts below;
that does not certify their prose beyond their actual headline types.

## Actual statement scopes

| PR / portal suffix | Read scope |
|---|---|
| [103](https://github.com/WolframInstitute/Rule30PrizeKit/pull/103) / e660e4 (ours) | `healing_bound` requires two whole-line IsR30Z evolutions agreeing initially on x≤−1; guarantees agreement on x+t≤K(E,t). `front_ge` bounds any disagreement, not centre-column behavior or generic capture. |
| [104](https://github.com/WolframInstitute/Rule30PrizeKit/pull/104) /3742dc (ours) | `edge_pinned_tail87` requires initial agreement with initRow on x≤87 and phases c0<7,c1<4. It eventually gives left agreement through fixedxB and some difference within its next13 cells. `check_sound`/`tick_sound` keep their exact background/representation guards. The theorem states no optimal eventual pinning at87. |
| [105](https://github.com/WolframInstitute/Rule30PrizeKit/pull/105) /0d8a71 | `gap_five_iff_eq_two` realizes exactly the eventually-white pair D2,D7; sharp whiteCount7 and exact small-index values. Fixed LEFT diagonals, not moving fronts. Replay61, checked09:34:11Z. |
| [106](https://github.com/WolframInstitute/Rule30PrizeKit/pull/106) /1c93e6 | `exists_exact_whiteCount_settled` finds w with whiteCountw=N+1 and explicit double-exponential index bound. At a≥16, white-window existence requires3a+21<5L+3log2log2a. At a≥256, both-color existence requires a+2<L+log2log2a. These exact inequalities, not a general o(a)-length window assertion, are the usable claims. Replay41, checked09:45:50Z. |
| [107](https://github.com/WolframInstitute/Rule30PrizeKit/pull/107) /e1cb85 | Backward transducer criteria retain finite-horizon K, s≥2 and the supplied period/state-map hypothesis. Two-step absorbing map gives periodL on s+2L≤i,i+L<K; involution-on-image gives period2L on s+L≤i,i+2L<K. The001111 and011111 wave statements retain their exact phase bits. No universal moving-front capture. Replay100, checked09:55:34Z. |
| [108](https://github.com/WolframInstitute/Rule30PrizeKit/pull/108) /1a6e64 | Actual black-boundary parity and remainder bound DIFFER from advertised prose; see below. White-run bounds retain the initial white segment/first black cell ell and parity guards. Replay40, checked10:07:55Z. |

A2 remains publicly Lean Verified. A1 remains Lean Unverified/error
with the same09:04:11Z timeout check and no extracted Lean source.
The owner's maintainer-WAIT decision and Local's delivery ownership
remain; no duplicate posting/build. These are receipt/status checks,
not Human Verified or prize claims.

## PR108: do not adopt the advertised stronger bound

Both the complete downloaded portal Lean source and the exact PR head
`941882ac8b70e394e869367c098d182e1fc88169` contain:

- `black_block_back_left_edge_even`: under its black-run and collision
  assumptions, (a−s)%2=0.
- `black_block_back_D_one_odd`: under its stronger D1 collision guard,
  (a−s)%2=1.
- `five_mul_black_run_le_exact_mod`, a≥1:
  `5*L<=3*a+2*((a-1)%5)+2`.
- `five_mul_black_run_le_of_mod_one`: if a%5=1, then5L≤3a+2.
- No declaration `black_run_le_erosion_div`, nor the advertised
  all-a bound L+2*(a/5)≤a, appears in either source.

The description instead reverses the black parity conclusions and
advertises5L≤3a+2*(a%5), including a stronger mod-zero bound. We have
not adopted it. A direct verified-TLS raw download from that exact
GitHub head is byte-identical to the indexed module, SHA
`61a986a6d6c70cef0c2b5b58c162098d9745ed311c569963e192a12ef4449329`.
The discrepancy is therefore not an assumption based on a keyword or
a stale local main. It was flagged to Local; no external message sent.
The weaker actual theorem is prior art regardless of the prose error.

## Exact source provenance

- PR103 head`3d2d609facefe45d86b02c3cd418f68a9aa28858`, `lean/Ruliology/CellularAutomata/Rule30HealingBound.lean`, SHA256`ab553b81916dd9bcd5a9b3f84a76f800ce05a7487bc6ea362487b7c16bc64b38`.
- PR104 head`12dc145efeb4307205c4c9ce3407cfeabbdef6d4`, `lean/Ruliology/CellularAutomata/Rule30EtherEdgeZero.lean`, SHA256`cc4ff16a354d5c862833868c4743a398018882d493a569c68dfe4c3f79fa8929`.
- PR104 head`12dc145efeb4307205c4c9ce3407cfeabbdef6d4`, `lean/Ruliology/CellularAutomata/Rule30RootedFront.lean`, SHA256`f58cadbe46411993cad9679eb5669083e795c31bf43b8ab543e051a0c1fb967c`.
- PR105 head`430161243c37fee33e5970ffde6e7f0e34354931`, `lean/Ruliology/CellularAutomata/Rule30WhiteSpacing.lean`, SHA256`0fe9d18370e65b33f1c348da55121e850a3066b14d94ee41c497e5c8cfee67f5`.
- PR106 head`c93e3e495080a7258be79d1624bacb81b485e6bb`, `lean/Ruliology/CellularAutomata/Rule30SettledBarrierEffective.lean`, SHA256`41ccbfc0a363e5fcec449914fa24c308201187b9468826fe7ebb741f6dedfeaf`.
- PR107 head`f56af5f34c2ea5fd2d54747234ed1a9e12e11e96`, `lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryStripeCascade.lean`, SHA256`8c636a52997019defef7857bf4ae43750d4a33a632f62e87bf03e63d68fcf2a5`.
- PR108 head`941882ac8b70e394e869367c098d182e1fc88169`, `lean/Ruliology/CellularAutomata/Rule30BlackRunErosion.lean`, SHA256`61a986a6d6c70cef0c2b5b58c162098d9745ed311c569963e192a12ef4449329`.

Portal source SHA256,105–108 order:

`7536c9c95ba24a6efeacd828df4da07dfeef1536e9856d5aa985ed1569427207`,
`3c200e7b5ab3b9208f952b0cec3ec7cc339a4ef0322bf9bfcd0614340c53e326`,
`bd07bbf4c5a45215a021cf72e5da21e4af672626b91386daa29dfb7cc4cab8a2`,
`044d8ec0c810f1b5f45183144993093274861ca66d7a84556355a13b5c4a6140`.

Receipt shared store `cited/gpt/gc2499-external-1021-20261103.json`,64441bytes, SHA256`e6ab040a77de1a3c5e3cbed4f0f855c32267b0ce15e758e13ab1b6182773f4de`.
Raw-body upload/readback verified; includes metadata, check receipts,
exact source hashes and complete refresh output. Full sources remain
outside git. Last successful COMPLETE refresh:10:21:10Z; next due
about11:51Z while working. The index still omits closed discussions,
review-summary bodies and linked research archives.

My own pull: retain exact usable theorems now; the immediate mathematics
is the Mahler band/escape-time relation, not a new Rule30 census.
