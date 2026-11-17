# rooted word membership does not imply root-clock membership

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT174. rooted word membership does not
imply root-clock membership (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A pattern can lie on the real history without every clock setting turning up there.

**What it says.** The bad period-4 step of G173 does occur on the real history, 10 steps from the seed's edge. But
there the clock always reaches it at one setting, while the bad step needs another, which the gate of G160 allows
but the real history never produces. So checking a budget on every gated clock setting asks more than the real
history needs.

**Why it matters.** A budget might still work on the clock states the history really reaches; the next test (RQ3)
was restricted to those.

**An everyday picture.** Your station is on the line, but the trains that actually call there all arrive on the
hour: a rule about trains arriving at twenty past need never be tested there, although the map of the line allows
it.

## The formal statement and proof

### GPT G174 — rooted word membership does not imply root-clock membership (RULE30-GPT.md G174; awaiting second reader, 2026-10-07)

**Root-word versus root-clock scope audit (2026-10-07; review requested).** DQ3's period4 source pair(15,12) is word-rooted, reached after10 spatial edges on the unique predecessor chain. In root-to-source order the exact pairs are

    (0,15),(15,15),(15,0),(0,5),(5,15),(15,5),(5,5),(5,0),(0,9),(9,15),(15,12).

Every consecutive triple satisfies the scalar equation; the constant-one root is integer15, not integer1. Carry G8's full-line clock from each initial root time0,1,2,3 along this chain. The source arrival times are9,13,13,13, hence all four arrival phases are1. These values were predicted from literal arithmetic before the independent targeted script `tests/probes/lexicon/rule30_dq3_root_clock_review.py` was executed; its scalar backward, forward and reset checks pass. No tree or quotient census was repeated.

At the actual reached phase1, source features are(1,2,1), its next reset costs2, and the target phase3 features are(1,3,1). The feature self-loop at source phase0 therefore disappears on this particular root-clock edge. Phase0 still satisfies the gate a(-1)=1. This is the identified unexpected guard: a pair can be word-rooted and gated at a clock that no root-start phase reaches. G7's unique predecessor guarantees there is no alternate word path to this same pair; enumerating all four initial clock residues is sufficient for the fixed period4 full-line front.

Consequently the q4 witness rejects a three-distance certificate on rooted word pairs required to cover every gated clock, but does not reject the same family restricted to clock states actually reached from the root. This is a sharper quantifier distinction than saying the witness is simply unrooted. Restart clocks at interior vertices and birth-clamped fronts are different domains; neither was tested or excluded here. G164's separate phase-transfer theorem remains relevant if a reference-clock budget can be proved. The all-period exact-family construction of G173 remains ambient, with no newly claimed rooted-clock membership at larger periods. Next scope to investigate is the explicitly root-reached clock graph, preserving actual clocks through every child rather than treating the gate as sufficient reachability.

*Second reader's note on G174 (Local, 2026-10-07; chat L136).* Correct. The ten-edge chain is compatible at every
triple. It is the unique predecessor chain from $(15, 12)$ back to the root $(0, 15)$, so with G7's unique predecessor,
the four root residues exhaust every root-reached clock. Carrying the full-line clock by literal reset scans from times
0, 1, 2, 3 reaches the source at times 9, 13, 13, 13, so always at phase 1. There its triple is $(1, 2, 1)$, the reset
of 12 costs 2, and the target at phase 3 has $(1, 3, 1)$, so DQ3's feature self-loop does not occur on a root-reached
clock. Phase 0 is gated but no root start reaches it. Checked (`rule30_audit_g99_g100.py`, S68) by my own scans, and
GPT's `rule30_dq3_root_clock_review.py` reproduces here with the same path and arrivals. The scope is as stated:
interior restarts, birth clamps and larger periods are not covered.
