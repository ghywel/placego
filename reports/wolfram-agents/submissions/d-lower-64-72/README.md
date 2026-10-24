# Submission d-lower-64-72: death-time lower bounds at widths 64 to 72, witnesses from a complete GPU census (Local, 2026-10-24)

One module (tests/probes/wolfram/d5_lower_submission.py): for W in 64, 66, 68, 70, 72 a witness start (one census maximizer),
`wW_lt : wW < 2 ^ W` by `decide`, its packed orbit black at depth 1 at every even time below D by `decide +kernel`, white at D,
bridged to `zrow` by the kit's `run_toFun`; headline `widthW_lower` per width. D = 116, 120, 122, 124, 130.
- **Headlines:** `Rule30Submission.width64_lower`, `width66_lower`, `width68_lower`, `width70_lower`, `width72_lower`.
- **Local check (the pipeline's kit copy, cc1e0e0, v4.35.0), revision 2 module (49129053…):** `lake build Rule30Submission` 18.1 s wall, maximum
  resident set 3484532736 bytes (mostly the kit's imported environment); the kit's checker 3.9 s, 3610886144 bytes; (revision 1 module: 18.3 s, 4.4 s); verdict pass, newAxioms [],
  replay of 52 constants ok, 38 declared, all five headlines found, ok, type-matching, axioms propext and Quot.sound.
- **What is proved:** the five lower bounds only. Maximality and the maximizer counts (40, 112, 32, 156, 252) are numerical
  results of the GPU censuses (L865, L866, L868), stated as such in the essay.
- **Expected notebook outputs, written before the build:** the bit lengths {64, 65, 67, 70, 72}; the first even white times
  {116, 120, 122, 124, 130}; the orbit plot; True (the kit directory); the LeanEnvironment summary; `LeanEnvironment` (the head);
  the five headline statements (each with `W < k` and `t < D`); the five axiom lists, each within propext, Quot.sound,
  Classical.choice; the width-72 survival and death statements; the two bridge lemmas; `KernelCheck` Success.
- **Revision 2 (GC1782):** the census domain, the check scope, the wall's orientation and the kit pin stated exactly in the module comment and the essay; gate revision 3 (exact cells, counts bound to the checker JSON). Notebook 72790 bytes, sha256 6181671a9dc5c205286d9d7cbc40437c94c7eb362c72872786c231e7932297ee; gate PASS.
