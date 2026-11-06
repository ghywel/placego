# The bridge return automaton

GPT GC2705, 6 November 2026. Owner-requested continuation of
[GC2698](GPT-BLOCK4-BRIDGE-HISTORY-20261106.md). GPT owns construction and checking;
Local's submission work and both paused schedules are unchanged.

## Question and test, before execution

Let A=25 and E=33535555. Starting after a complete E in the retained X gap
DFA, retain the state after each word A^n E. Compute each state's exact unary
A orbit, including its preperiod and cycle, so every exponent n>=0 is covered.
Minimize by equality of **all future sequences of exponents**, not just equality
of the next allowed exponents. Preserve the rejecting state and distinguish
total resets from synchronizing only the histories that survive a word.

Prediction: this gives a small return graph which explains the forbidden
successions 4,4 and 4,6, and sufficiently long separations synchronize its
surviving states. Counterfactual: a larger graph or persistent long-separation
memory. Both outcomes are useful. The next question is which of its states has
a meaning in an actual shared boundary history; a finite-language quotient alone
does not settle that question.

Inputs are the existing X DFAs at widths 38,39,40,41, from Local's digest-bound
bridge archive. No new windows, seeds, SAT queries or horizons. Exact finite
quotients, distinguishing suffixes, return-cycle costs and reset tests are the
whole computation. Controls: tiny known return machines; raw-vs-quotient
commutation for every transition type; distinct classes have separating future
words; GC2698 counterwords reproduced; width39–41 return languages compared;
an independent literal-word replay checks all exponent representatives and their
first repeated cycle. A corrupted transition must fail this replay.

The generic construction and any hand consequences remain PROOF-SKETCH until
Local carries them. Computational claims are conditional on the supplied DFA
tables: their earlier subset-hash/original-graph-completeness caveat remains.
The exact language under review is E(A*E)*, not all partially parsed gap words.

Record searched: GC2698/GC2699, L1569 and the retained scripts/packets;
record_find return-automaton search finds only this existing queue. The current
kit/portal/PR refresh and relevant primary-source check are recorded below at
closeout. No claim to invent return automata or finite-state minimization.

## Resource freeze

One serial Python worker on Intel, one thread, nice10. Stage ceiling120 aggregate
CPU seconds/300 wall seconds, worker stop105, individual worker100CPU/240wall;
reserve15CPU for supervision. Tree RSS8192MiB, launch headroom4096MiB,
running floor1024MiB, swap-growth4096MiB, at most6 processes including wrappers
and monitors. At most16MiB/file and128MiB/stage. Use run_capped.py plus the
existing serial stage driver, with real aggregate worker accounting. All source,
input and plan digests are frozen before launch. A pressure, thermal, monitor or
control failure stops the stage; no dependent retry or size enlargement.

## Outcome

Pending the frozen run.

Frozen source/input digests:

| File | SHA256 |
|---|---|
| return_automaton.py | aa3d06aa249f4efc3bbaaafc3000c62dfe0af1d570cbb0f46a8dcdc006c5cdb8 |
| intel_worker.py | 2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94 |
| stage.py | ba9696782abbee65ffcd3433e78848f1de82647a4f8033ab1e6a5c6cbdaaa09a |
| run_capped.py | 26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b |
| dfa_xx_W38_c0.txt | 465c2cfd8b303db816c439d237c760c1a28f6766fdda10e56a8df37cbcde68e4 |
| dfa_xx_W39_c0.txt | 7972a731983ef9baa397a9107283f5e34b4b6429e091bf24c08e673c7f089aaf |
| dfa_xx_W40_c0.txt | 0323f4a3bb60717f97c432c378e61cd85feacd1a9097ce667396de58d196167a |
| dfa_xx_W41_c0.txt | 0d0231db4179ab4ac79eb9409933beefe313d9c4a1473cffcbe7ee6bd0b9593c |
| gc2705-plan.json | 068cad1c98a269d85fbb5bf4eabb7c5fa223e9ed4d26f4d259d44372c84bda11 |
