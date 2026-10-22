# Submission 2a: 48 excluded column words of length 11–16, beyond the kit's table (Cloud, 2026-10-22)

PROOFS.md entry 41 (Local's `tests/probes/lean/JenRoute.lean`), restricted to the words the kit's
`Rule30StripCertificateTable` lacks and restated on the kit's `evol` and `cell`, with the bridge to `EventuallyWord`.
41 words at strip width 8 and 7 at width 10 (lengths 11: 1, 12: 1, 13: 2, 14: 9, 15: 15, 16: 20). Headlines:
`Rule30Submission.not_eventuallyWord_words` (for every listed word, the seed's center column is not eventually that
word) and `words_general` (every column of every configuration with a leftmost black cell). `check.json`: verdict
pass, replay of 235 constants, standard axioms only. Build 165 s, check 145 s here: too slow for the verifier's
four-minute automatic check as it stands (see CL572); a faster certificate is being built before this is submitted.
Generated from JenRoute.lean by the generator recorded in CL571–572; the eleven words of entry 41 that are already in
the kit's table are left out.
