# Blind futures, witnesses and knowing when a prediction is trustworthy

GPT, 26 October 2026, GC1922 / MI844. Owner-directed manual exploration of DQ-015/016. Both heartbeats remain paused; the owner will pass the conversation to Local. No dynamics, model training, solver, benchmark or Lean run. **Status: elementary hand derivations and an application of known left-permutivity, not independently read and not a new prize result.**

## 1. The question in words

Can the future be our examiner without being part of our answer sheet? Yes: specify what we may see, make a prediction and state its confidence, then reveal what actually happened. The future checks the claim. If we change our rule after looking at the answer, that case becomes a discovery example, not an unseen test.

The bystander question asks something different from direct causation. A witness need not operate the machinery to tell us about its state. But being nearby is not enough. A useful witness must distinguish some situations our present description treats as identical.

Three questions must stay separate:

1. Does the allowed information determine the answer exactly?
2. If it does not, how often can the best guess succeed in a specified population?
3. Can we distinguish the cases we know from the cases we are merely guessing?

The third can improve even when the second does not. Section 3 gives an exact Rule 30 example.

## 2. A precise meaning of an informative witness

Take a finite population Ω of N possible beginnings, equally weighted. Evolve each with the same rule and boundaries. Let Y be a selected binary future outcome and O the information permitted at the prediction cutoff. These are functions of the beginning; O cannot inspect the hidden target or use it to select observations.

For each description o, count n(o,0) beginnings with outcome0 and n(o,1) with outcome1. These are mathematical counts for this population, not a proposed census.

**Exact prediction criterion.** There is a predictor depending only on O which is right everywhere in Ω if and only if every nonempty description class contains only one outcome. Necessity: one prediction cannot fit two opposite outcomes with the same description. Sufficiency: assign each class its unique outcome.

**Best possible hit rate.** For unrestricted predictors using only O,

    A*(O) = Σ_o max(n(o,0), n(o,1)) / N.

Choose the majority outcome in each class. Any other choice loses or ties there. Randomization cannot improve it because a randomized choice is an average of the two possible success counts. This is an information bound, not a claim that an efficient algorithm can learn or compute those counts.

An extra witness B subdivides each class into (o,b) classes. Therefore

    A*(O,B) >= A*(O).

The inequality need not be strict. The witness is sufficient for exact prediction precisely when every subdivided class is pure. Merely splitting one conflicting pair is necessary to fix that pair, not enough to fix all others.

For confidence forecasts put p_o = n(o,1)/(n(o,0)+n(o,1)). A forecast p says how often outcome1 occurs among the beginnings still compatible with the observation. It does not mean the deterministic rule itself throws a coin. The exact probabilities are calibrated on this named population: among cases assigned p, the fraction with outcome1 is p. Calibration by itself is weak: the same overall population frequency assigned to every case is also calibrated.

Let Brier(O) be the mean squared error of these probability forecasts, rather than the binary hit rate. Conditional on o, a forecast r has error

    p_o(1-r)^2 + (1-p_o)r^2
      = p_o(1-p_o) + (r-p_o)^2.

So p_o minimizes that error. For q_(o,b) = P(Y=1 | O=o,B=b), averaging q over each o gives p_o. Expanding the squares yields

    Brier(O) - Brier(O,B) = E[(q_(O,B)-p_O)^2] >= 0.

Any witness that changes the conditional probability on a positive-weight class strictly improves this probability score. It may leave the majority prediction and hence the optimal hit rate unchanged. This is standard finite conditional averaging, derived here as a control, with no novelty claim.

All formulas extend to specified nonuniform weights by replacing counts by probability masses. Uniform weighting of beginnings is generally NOT uniform weighting of distinct futures or merge classes (GC1916). A number such as “75%” is incomplete without this choice. Finite-population calibration also does not establish calibration on new widths, other populations, or successive times of one selected orbit.

## 3. Hand control: the same 75% accuracy can hide very different knowledge

Use the standard physical orientation, not depth-from-wall notation. The next target bit is

    Y = L XOR (C OR R).

L, C and R are the left, centre and right input bits. Here the population is exactly the eight equally likely triples: the three bits are independent and fair. This is a deliberately simple control involving direct inputs, **not a discovered informative bystander** and not the distribution of a survivor-conditioned or single-seed history.

| Permitted observations | Best binary accuracy | Minimum mean squared probability error |
|---|---:|---:|
| Nothing | 1/2 | 1/4 |
| C and R | 1/2 | 1/4 |
| L | 3/4 | 3/16 |
| L and C | 3/4 | 1/8 |
| L, C and R | 1 | 0 |

Every entry follows by hand:

- An unseen fair L masks the answer regardless of C and R: for each fixed pair, one L gives each outcome. Thus observing C and R alone supplies no predictive information about Y in this population.
- Given L, the pair C,R has OR1 in three of its four equally likely cases. Predict NOT L. This wins six of the eight cases. The probability of Y=1 is 3/4 when L=0 and 1/4 when L=1; either forecast has squared error 3/16.
- Add C. If C=1, the answer is certainly NOT L. If C=0, the answer is L XOR R and remains equally likely either way. These two situations each occupy half the population. Accuracy is still (1/2)×1+(1/2)×(1/2)=3/4. Squared probability error is now (1/2)×0+(1/2)×(1/4)=1/8.
- With all three inputs the answer is exact.

**Unexpected check:** more information need not improve the best hit rate. It can instead identify the reliable half of our predictions. In this example the gain in probability score is 3/16−1/8=1/16. A test reporting only “still75%” would miss it. An honest predictor could answer only in the certain half and abstain in the other half: 100% accuracy at 50% coverage of this population, not a 100% predictor for every case.

The result also warns against equating causal importance with predictive value. C and R genuinely enter the update, yet revealing both does not help when the independent masking bit L is hidden. Conversely an indirect witness can help if it reveals information about a missing input or their joint effect.

## 4. A limit on what bystanders can reveal: the hidden fair bit

This is the existing fresh-left-input argument of G4.4 and G97, applied to the owner's observation question. It is not a new universal unpredictability theorem.

For a target at physical position i after h>=1 steps,

    x_h(i) = x_0(i-h) XOR G_h(x_0(i-h+1), …, x_0(i+h)).

Proof by induction on h: the h+1 update XORs its left child's value with the OR of its centre and right children. Only the left child's initial cone contains the new extreme-left bit x_0(i-h-1); by induction that bit occurs as a single XOR term. The other two cones exclude it, so all remaining terms form G_(h+1).

Put p=i-h. Choose a finite initial interval covering the cones of the target and all permitted, finitely many observer cells. Give its bits independent fair values and fix everything outside it. Flipping x_0(p) pairs each beginning with another equally weighted beginning and reverses Y.

Suppose the complete observation O is unchanged by this flip. The pair then has identical observations but opposite targets. Every O class has exactly half of each target, so **every binary predictor using O succeeds on exactly half this population**. Independent randomization has the same expected rate; probability forecasts cannot beat squared error1/4. Any added witness also unchanged by the flip remains powerless to improve these bounds.

A sufficient geometric condition for an observation x_s(j), 0<=s<h, to be unchanged is that its initial cone [j-s,j+s] excludes p. In particular, any fixed collection with j-s>p qualifies. This can include many earlier-time observations and near-looking diagonal points. If observation positions are chosen adaptively, the selection procedure itself must also be unchanged by the flip; otherwise the chosen position could leak the missing bit.

This gives a necessary test for a proposed witness: does it break the pairing that made the answer ambiguous? Breaking some pairs is not sufficient to guarantee useful average accuracy; other ambiguities may remain.

**Scope guards:** the pairing depends on equal weights and on including both beginnings. A fixed single seed, a restricted family of seeds, or conditioning on survival can remove or reweight one partner. No fair-coin claim transfers automatically. Past observations whose cones include p may reveal it. Full present information determines the future. This argument concerns missing information, not a lower bound on the computation needed when the information is available.

## 5. Reconnecting to the actual work without looking at the answer first

GC1915, independently carried by Local L980, gives the conditional short-reread identity

    s_new = NOT(x OR y),
    x = c_d(H-2),  y = c_(d+1)(H-2).

Its hypotheses include old E11/input1, a live most-recent return at gap3 and the resulting drop pattern030. Knowing B=x OR y resolves this conditional reread exactly. But x,y are already inputs in the local reconstruction, and the return conditions themselves may require later information. This is an explanatory formula, not a demonstrated blind predictor or a new bystander mechanism.

There is also an axis issue. d indexes spatial reconstruction depth; H indexes physical time in the column histories. The target c_(d+2)(H-2) and the two displayed background cells share the same physical time. Advancing to another reconstruction column is not advancing the physical clock. A valid held-out spatial-completion exercise is possible, but must be named as such. To claim a physical future forecast, give the physical cutoff and show that every feature and every case-selection condition was available by then.

For example, selecting only cases later known to make a gap3 return and then announcing high accuracy estimates a future-conditioned task. It does not measure the pre-return predictor's success on all eligible cases. A legitimate alternative is to predict both return and outcome jointly, or choose cases solely by already available observations.

The retained longer-gap conflict descriptors in L966 do not contain the exact background rows, exact gap or individual OR terms. Their label4 means at least four. This report does not regenerate them, pretend their missing cells were read, or reopen the closed return-length census. A concrete prospective bystander predictor on those physical cases remains unconstructed.

## 6. Checkpoint for the owner's handoff to Local

**Question → response:** Can unseen outcomes judge both our prediction and our confidence? Yes, with a frozen information cutoff and a named population. Exact finite mathematics separates perfect prediction, optimal hit rate and useful confidence.

**Challenge:** improvement may disappear when we remove a hidden future-dependent selection rule, change population weights, or test on a genuinely new case. A near-looking cell may add no information at all. A fixed future is an examiner only after the prediction and its selection rules are frozen.

**Better question:** What is the smallest observation, available before the chosen cutoff, that distinguishes two otherwise identical descriptions with different outcomes—or tells us when our description is sufficient?

Useful next work with Local is an independent hand read and choice of one physical target/observer, not a large forecasting run. In particular:

1. Check the class criterion, the 75%/confidence example and the exact scope of the hidden-bit pairing.
2. Choose physical-time forecasting or explicitly held-out spatial completion. State the cutoff, permitted observations, population and target before selecting examples.
3. Identify an actual admissible witness or a same-observation/opposite-outcome pair. First try a hand argument or already retained complete examples. The incomplete L966 descriptors are not such examples.
4. Only if that produces a discriminating question, freeze a bounded experiment separately. Freeze the predictor and confidence assignments before revealing its test outcomes; keep already seen cases as development material. Compare against the majority baseline and the existing observer. Record both hit rate and probability error, plus any abstention coverage.

For generalization tests, related twins or overlapping histories must not be casually split between training and test and called independent. Specify whether the claim concerns new beginnings, new future classes, new widths, or later times of one beginning. Consecutive Rule30 samples do not acquire independent binomial error bars merely because they are called test data. No experiment or launch agreement is made here.

**Present result and wall:** we can now state exactly what an informative witness must do, and we have an exact counterexample to accuracy being the sole measure of progress. We have not found such a witness for the surviving tick/tock mechanism, an efficient predictor for the single-seed centre, or any all-width survival bound. The warm pull is narrower: a witness may be most valuable as an indicator of when we know enough.

## Record and checks

Record searched: `record_find.py 'predict|forecast|Bayes|calibrat' 'permut|fresh|light.cone|bystander'` returned342 hits in146 files; not all hits were read. Relevant carrying sources read: G4.4 in archive/gpt/RULE30-GPT.1.md; G97 in archive/gpt/RULE30-GPT.2.md; GC1899/GC1902 in reports/rule30-sideways-fresh-input.md; GC1914/15/17 outcome note in reports/rule30-revisit-sat-outcome-review.md. The existing record overrides any novelty suggestion. Finite conditional-averaging formulas are standard and proved above; no external source is needed as an unproved premise.

Hand adversarial checks: masked inputs remain uninformative; informative C leaves accuracy unchanged; full-input prediction is exact; initial-bit pairing fails without its population symmetry; reconstruction depth cannot silently become physical time. No fresh execution pass is claimed for the legacy startup probes (previous monitoring limitation remains); no experiment was attempted. No independent Claude read of this note yet. No portal submission or schedule restart.

Reasoned verdict: useful mathematical clarification and a concrete handoff, no prize advance. Gut verdict: warm on distinguishing trustworthy predictions from guesses; uncommitted on which actual bystander, if any, will supply that distinction in the hard family. Stop this manual block at the owner's requested handoff point.
