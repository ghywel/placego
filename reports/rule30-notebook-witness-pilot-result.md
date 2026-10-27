# The witness pilot: simulation resolves 25 of 31 words at age 100, including GC1979's timeout

Local, 27 October 2026, L1030. One run of GPT's frozen pilot (GC1981) on the M5, as the owner directed.
- *Source:* `tests/probes/wolfram/notebook_witness_pilot.py`, SHA256 e25dd2cf…. Its literal evaluator, supervisor and
  MFW list hashes were checked against the freeze before launch.
- *Supervisor:* `run_capped.py` with GPT's caps: 600 CPU s, 750 wall s, 512 MiB RSS, 64 MiB disk.
- *Outcome:* COMPLETED, rc 0.

## Result

- **Controls passed (P_A).**
  - The fast simulator matches the literal evaluator cell by cell on all 4,096 tiny cones.
  - The retained q00002 row replays to `00001000` at visible age 100.
  - No EXCLUDED word appeared at or above its bound, and no window outside the initial language appeared at any age.
  - Every retained witness, both at age 100 and at each word's latest age, was replayed with the literal evaluator.
- **Sampling.** All 200,000 draws ran; the stop reason is N_MAX. Wall and CPU were 10.5 s each. Peak RSS was 15.1 MB
  by time -l; the supervisor's own samples are in the launcher receipt.
- **Verdicts over the 36 words of L8:**

| Verdict | Count | Words |
|---|---:|---|
| EXCLUDED (offset rule, from the 32 and 34 deaths) | 5 | 00010001, 00100010, 01000101, 10001010, 10010001 |
| WITNESSED_100 (a replayed row shows the word at age 100) | 25 | the other 25 targets, including **00001001** |
| UNRESOLVED | 6 | 00010101 (latest sampled age 98), 00101010 (99), 01010100 (99), 10001001 (16), 10010100 (0), 10010101 (0) |

- **GC1979's timeout is resolved by an explicit witness.** `00001001` at visible age 100 has a replayed row. That
  single query had stopped the previous stage after 30 s of SAT search.
- **P_B was refuted.** I predicted fewer than 10 of the 19 targets with a 1-distance outside {3, 5} would be
  witnessed. 13 were (the counterfactual held). All 12 targets with distances in {3, 5} were witnessed.
  - Rows showing an off-rhythm word at age 100: 18,857 of 200,000.
  - The five most common age-100 words, `01000010`, `10000100`, `00100001`, `00010000` and `00001000`, account for
    about 74% of the rows.
  - Only 25 distinct words appear at age 100 at all.
  - As GC1981 says, coverage and frequency are separate measures, and none of this concerns trap entry.

**The gate E_34^8 = E_100^8 is not yet complete.** No death is inferred from the six unresolved words. They fall into
two kinds.
- **Near 100** (latest sampled ages 98 and 99): 00010101, 00101010, 01010100. Likely rare survivors.
- **Early** (latest sampled ages 0 to 16): 10001001, 10010100, 10010101. Candidates for early exclusions that the
  offset rule did not catch, as GC1980 foresaw. That is unproved.

## The next step it suggests (for GPT; nothing has run)

- **Early words.** SAT at the first unwitnessed age (17, 1 and 1) uses tiny CNFs. UNSAT there would move these words
  to EXCLUDED, with new early deaths at most 34, and so out of the gate's way.
- **Near-100 words.** Search locally from their retained rows: flip deep cells of the age-98 and age-99 witness rows
  and resimulate. A row reaching age 100 is a replayable witness. Alternatively, SAT at 100 with a longer, frozen
  timeout.
- If all six resolve, the gate closes and the n = 20..24 stage can be redesigned the simulate-first way.

## Evidence

- *Store:* `cited/l1030-witness-pilot/` (10 files, read back byte-exact), manifest SHA256
  `2095839827018bd0daa4ed352c1bb1d5e27696dbdf0194a5479cefee0a886a77`.
- *Privacy:* `launcher.json` held private local paths. The uploaded `launcher-sanitized.json` replaces them; the
  original's hash is in the manifest.
