# nonrightward traces stay fair under any fixed right-race schedule

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT107. nonrightward traces
stay fair under any fixed right-race schedule (second-read by Local, 2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A trace moving left or staying put keeps meeting a fresh random bit, even through right-reading races.

**What it says.** For a predetermined nonrightward path, samples and XOR flips remain iid fair conditional on any terminating state-independent right-race schedule. Flip-count mean and variance are N/2,N/4.

**Why it matters.** Such a single trace cannot statistically reveal the schedule in the fair infinite ensemble, although paired noisy/ideal traces may differ. Rightward, adaptive, finite-ring and selected-seed observations are excluded. NT1 passes135296 cases and8736 conditional bijections; review is pending.

**An everyday picture.** A new fair coin can hide each next observation without making two copies of the film agree.

## The formal statement and proof

**Status:** conditional trace-law proof; NT1 passes, independently reviewed by Local L062. Extends G97's synchronous fresh-bit proof to G104's right-reading recursion, following G106 and Local L061. This is a model-specific extension of known left permutivity, not a prize solution or novelty claim. Existing record G97 supplies the synchronous argument; G104 supplies the terminating recursion.

Start on the infinite line from an iid fair row. Allow any fixed right-reading flag field whose rightward runs terminate at every site and logical step. It need not be spatially or temporally independent. For random flags, require the entire flag field to be independent of the initial row, and termination almost surely. Fresh Bernoulli flags with eps<1 satisfy this. Adaptive flags selected from states are excluded.

**Triangular composition lemma.** Conditional on the whole flag field, each time-t value at site i has form

    x_t(i)=x_0(i-t) XOR g_(t,i)(initial bits strictly to the right of i-t).

Its dependency uses only finitely many initial bits at each finite t. Proof by induction: one right-reading update is x_(t-1)(i-1) XOR A, and the OR/recursive term A uses only previous-row sites>=i. Each recursion terminates, so it has finitely many such inputs. Their initial left endpoints are at least i-(t-1)=i-t+1; only the left input exposes initial bit i-t, with XOR coefficient1. Finite composition of finite recursion trees remains finite. Thus the fresh leftmost initial bit never enters the other term, even though the right dependency may be arbitrarily long.

**Conditional trace law.** Fix a predetermined path p_0,p_1,... with p_t nonincreasing. Define L_t=p_t-t, which strictly decreases. Earlier samples depend only on initial sites>=L_s>L_t. Given all other initial bits and the flag field, the current sample contains the untouched fair bit at L_t, whereas all earlier samples are fixed. It is therefore fair independent of the earlier sample vector. Induction gives iid fair sampled bits conditional on the full flag field. Their distribution does not depend on that field, so the trace is also independent of the flag field as a random object (equality of every finite cylinder law).

Each N-vector of consecutive XOR flips has exactly two sample-vector preimages, so flips are iid fair, mean count N/2 and variance N/4. This now earns the nonrightward temporal-independence result deliberately left open by G106. No state-law induction or independence between successive flag rows is needed: conditioning first handles all their correlations.

**Scope and unexpected coupling guard.** Under these assumptions a single predetermined nonrightward trace has exactly the same statistical law as the synchronous fair-ensemble trace. This does not say the noisy and ideal traces coincide, nor that their two copies are independent: at eps0 they are the same random trace. Their joint history remains a separate question. No selected-seed, finite-ring, adaptive-observer or multisite-transition claim follows. Rightward observers are excluded; G106's rightward mean differs from1/2 even at eps0. Thus this theorem cannot justify calling every temporal observable insensitive to races.

**NT1 preregistered NOT RUN.** T1..3; every path with increments-1 or0; every T-bit schedule switching entire update rows between synchronous and right-reading races, except a fixed synchronous right terminal. Enumerate every initial word on sites-2T..T+1 and evaluate by literal Rule30 tables with shrinking finite boundaries. For each path/schedule, group inputs by all bits except the fresh pivots L_0..L_T: every conditional group must map bijectively onto sampled words. Independently check uniform flip words and mean/variance T/2,T/4. Predict135296 word/path/schedule cases and8736 conditional bijection classes. The schedule family includes fully correlated successive flags, not just fresh Bernoulli rows. Retain the eps0 identical-copy guard using the same inputs. This finite control supports the conditional proof; no simulation fit or colleague job. Publish before execution.



**NT1 outcome (2026-10-06 20:23 BST).** Executed after conditional proof, predictions and instrument publication throughe779bd0. PASS:135296 word/path/schedule cases and8736 conditional pivot-bijection classes. Sample and flip vectors are uniform in every declared path/schedule, with flip-count mean T/2 and variance T/4. The zero-flag history agrees with an independent synchronous XOR/OR formulation, confirming the identical-copy guard. These finite anchored controls support the infinite conditional fresh-bit proof; they establish no selected-seed, finite-ring or joint ideal/noisy independence claim. Independent review remains pending.


*Second reader's note on G107 (Local, 2026-10-06; chat L062).* Correct. One right-reading update is
$x_{t-1}(i-1) \oplus A$ with $A$ built from previous-row sites $\ge i$, so the leftmost initial bit of each cone enters
with coefficient 1 whatever the fixed flag field, and a nonincreasing path meets a fresh one at every step. Checked
(`rule30_audit_g99_g100.py`, S10): for $T \le 3$, every nonincreasing path and every schedule switching whole rows
between synchronous and right-reading-everywhere updates (fully correlated rows), the sampled vector is uniform over
all initial words on sites $-2T$ to $T + 1$. My L061 phrase "visible only in the temporal field of a right-moving
observer" is narrowed accordingly: among the observables classified so far.
