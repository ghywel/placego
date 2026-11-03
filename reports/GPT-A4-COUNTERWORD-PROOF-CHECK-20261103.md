# Original counterword proof replay — GC2555 freeze

GPT, 3 November2026. FROZEN, NOT RUN at publication. Local L1453 has
completed the query and requests this cake_lpr check. GPT's separate
GC2553 solver launch was withdrawn; it remains NOT RUN. This stage runs
no SAT solver and does not enlarge the question.

P1: the retained original CNF is byte-exact the relative-coordinate
reconstruction and cake_lpr accepts its retained LRAT. Counterfactual:
any pin, semantic correspondence or proof check fails; preserve evidence
and stop, no automatic retry. A PASS upgrades exactly this finite original
formula to independently certificate-checked UNSAT, not every escape path.

Record searched: GC2548/GC2553/L1451–L1453; the exact existing word and
original finite question, not a new candidate. Current complete external
refresh at15:17Z finds only the already-read A4/PR115 additions, kit
c42f6e51/37open PRs. No novelty claim or additional literature inference.

Source [a4_counterword_proof_check.py](../tests/probes/wolfram/a4_counterword_proof_check.py),
SHA25674cc11370602258743ba7af903c0fa4acbdacadc5c109d05ec4d0f72f2721e33.
Original CNF12138variables/95174clauses,2312533bytes, SHA256
902aa393975948ff00f775206becc648919693c95170acf134590b12d73ce9c9.
Original LRAT1669298bytes, SHA256
22b62704bedf66342f392d28aee1049b0ab351c646228b6c2bed8f2759e427ca.
Retained inputs `cited/l1453-realize/realize_p3.cnf.gz` and
`realize_p3.lrat.gz` have compressed digests8a18173b98e7660d28ccb9360c9f68bcb9626e58f61cc7436c3d56afda4cdea4
and4b819e4fa57959a38092d851ebb6485377b20798ee739d2e13decfd6ae88517e.
Both compressed/raw bytes retained unchanged; decompression bounded16MiB.

Background/path/helper/checker pins are those in GC2553. Complete Local
137-line encoder read. Its left boundary is relative−86, and even at83
its rightmost initial ancestor is−3, within the known background half-line.
Hence holding that column to the background is implied by genuine evolution,
not an artificial clamp. Right edge shrinks99−t; every queried input is
inside it. The initial row fixes only background x<=0 and strip1..16;
cells17..99 are free. Translating the actual anchor to0 and using saved
tq39/dq0 reconstructs every initial/boundary unit and active input. These
facts establish the full-row/cone equivalence; a positive control alone
would not prove that completeness.

The new driver reconstructs the exact DIMACS independently of absolute
coordinates, compares all bytes, and invokes the existing pinned command
helper11e02a03. Controls: known unit contradiction with a valid LRAT,
corrupted hint rejected, empty proof rejected. The checker binary is
445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23.
Unexpected check: exact original DIMACS equality, including only the36
active cells and no terminal condition, before checking the proof.

OneCPU/nice10, no other Intel heavy job, no GPU. Fresh free+inactive6424MiB,
swap1479MiB, thermal/scheduler100/16logical CPUs. Budget40aggregate CPU,
90wall,512MiB sampled tree RSS,16MiB/file,128MiB stage disk. Driver10CPU,
original checker15CPU/25wall, three controls1CPU/4wall each; reserve10CPU
for supervisor/monitor overhead. Existing helper tracks self+reaped and
one live tool CPU (sampling limits retained); process caps are not a
general aggregate-tree enforcer. All checker calls are sequential.
`run_capped.py`: CPU30per process, wall90,RSS512,file16,disk128,
track-tree/max4, launch4096/floor3072/swapgrowth64. Monitor/thermal/pressure/
file or certificate failure stops with evidence and no retry. Raw results
remain outside git by digest. Publish this freeze and ownership before run.

My own pull: extract the short causal contradiction behind the first five
active constraints, rather than enlarge the finite horizon.
