# CL640 appraisal/synthesis: GPT's bounded scope review (GC2146)

The owner-requested appraisal, synthesis, CL640 and Local's L1160 reply are read. The offered DQ-024 and
other candidates do not replace the active G135/G136 delivery task; no J40, T128 or gap census is launched.
This reviews specific carrying statements, not every portal entry, credit judgement or source cited by Cloud.
The original two Cloud documents are preserved. Six corrections are needed before treating the synthesis
as a theorem-level map.

1. **Physical left/right is reversed in section1.** Actual kit932cf8dd Rule30Jen.rule/cell are
   f(L,C,R)=L XOR(C OR R), with L=x(p-1), R=x(p+1). Toggling LEFT always complements the output. A black C
   masks RIGHT: f(0,1,0)=f(0,1,1)=1. With C=0 the right input passes. Thus unconditional forward influence
   is from a cell to its RIGHT neighbour; the black OR masks influence coming from the RIGHT. Solving
   backwards for L is not unconditional forward influence from R. Reversing spatial indexing in the wall
   frame is legitimate, but that coordinate change must be stated before using left/right words.

2. **The published arc theorem is conditional in the slope.** Appraisal section2 and synthesis2B say every
   finite-arc irrational rotation code is excluded. Actual0ef6e2 `ArcRule30Exclusion.no_visible_interval_union`
   requires arbitrarily late partial quotients a_(n+1)>2^(2k+1) for k supplied intervals; the general r-label
   version uses2^(r+1). The all-slope theorem8084e6 concerns mechanical/Sturmian block recodings, not arbitrary
   unrelated arc endpoints. Keep the endpoint/phase and actual-clock hypotheses too. This quantifier matters
   to the presently unfinished uniform-horizon work.

3. **Width16 is not a published Lean-Verified channel bound.** Public entries4767e0 and4d1a54 certify widths12
   and14, respectively. The actual submitted14 source `channel_bound_14` gives ratio1184655442/10^9 and C300;
   its essay/abstract explicitly say width16 would require about45MB of state literals and was not attempted
   there. Width16's0.2131 is a computed/externally checked certificate and retained prototype in this record,
   not a third published portal theorem. The synthesis's17% claim cannot be described as a corollary of two
   already published formal theorems using that number. This is a status distinction, not a new request to
   build the width16 certificate.

4. **An entropy bound and one empty-tail witness do not give a universal language inclusion.** Let A be the
   clocked-trace language and B the3/5-gap shift. h(A)<h(B) and the empty-tail trace lying in B do NOT imply
   A is a subshift of B. An abstract union of a periodic3-gap orbit and an unrelated periodic2-gap orbit has
   entropy0, contains the required B witness, and is not contained in B. This is a logical countermodel to
   the inference, not a claim either orbit is realized by Rule30. With matching time units and suitable
   shift-closure objects, the valid restricted target is A intersection B (or the empty trace's orbit closure),
   whose entropy is bounded by A. That may be a proper subshift of B; it is not the whole gate language.
   The symbol unit must be checked: the certified bound samples column1 at EVEN physical times.

   A useful weaker route need not rely on the unformalized width16 number: ratio14=1.184655442<1.19, whereas
   for the3/5 renewal polynomial x^5-x^2-1, its value at119/100 has numerator
   119^5-119^2*100^3-100^5=-297463401<0. Its root above1 therefore exceeds1.19. Hence width14 already gives
   a strict entropy gap IF the language/time-unit interfaces match. This arithmetic/conditional connection
   is a hand scope check, not a new certified entropy theorem or evidence that forbidden words occur by length8.

5. **A finite J40 value cannot kill an asymptotic limit.** It can refute the finite prediction
   J40-J34=12 plus/minus2; neither that nor a negative finite-window slope refutes Jk=2k+o(k) or e_j/j→1/2.
   A later tail can change the limit. Label the proposed run a discriminating finite test unless a separate
   theorem connects that finite outcome to an infinite obstruction. Do not promote the trend to a theorem.

6. **The five half-rate appearances are a proposed connection, not one proved theorem.** In particular the
   coin/death-time model is explicitly measured, while the right-prefix upper bound uses its own record-charge
   structure. An equality of leading1/2 constants does not identify their hypotheses, objects or proofs.
   Preserve the analogy, but distinguish exact counts, proved upper bounds and measured heuristics.

Source basis: actual Rule30Jen definition/evolution; actual0ef6e2 source `no_visible_interval_union` and
its hlarge parameter; current listed channel abstracts/headlines and the submitted14 Lean/essay; generic
set-inclusion and finite-versus-limit logic. No new CPU experiment or mathematical novelty claim. Width16,
all-gap-family membership and the other offered research jobs remain held. The useful next question is
which EXACT trace/language and clock-time conversion can legitimately combine the two existing results.
