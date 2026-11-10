Rule30RecognizableBarrier: no ranking through a recognizable statistic, and two rows that defeat every width-bounded rank (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30RecognizableBarrier.lean`, with its `public import` line in `lean/Ruliology.lean` after `Rule30FourFrontsBase` and a row in *Added in the kit*. It imports only `Rule30ZeroBoundaryBarriers`.

**What it proves.** A recognizable statistic of a row is its image under a morphism from Boolean words into a fixed finite monoid (`FinMonoid`, `FinMonoid.eval`).
- `no_recognizable_ranking`, `no_recognizable_ranking_nat`, `no_wall_recognizable_ranking`: no rank of the width and the image of the row, read from its edge or from the wall, falls at every surviving double step of every finitely supported row. The ranks may take values in any well-founded order.
- `no_windowed_recognizable_ranking`: the same with the kit's wall and edge windows added. Its one-element-monoid case is `no_local_ranking` (`no_local_ranking_of_recognizable`).
- `no_joint_recognizable_ranking`, `no_joint_recognizable_ranking_nat`, `no_joint_windowed_recognizable_ranking`: the coupled frame of `JointCert`, with the image of the whole configuration between its ends. `no_joint_local_ranking_of_recognizable` recovers `no_joint_local_ranking`.
- `no_width_bounded_ranking`: the rows `1493` and `1507`, of width `11`, survive fourteen double steps (`sharp_rows_check`, `sharp_rows_width`, `sharp_rows_survive`, `sharp_rows_fourteen`). So no integer rank between `-1` and the width falls at every surviving double step. `no_edge_automaton_ranking`: hence `no_edge_dfa_ranking` without its bound on the number of states.

**Method.** The kit's witnesses:
- the truncated stripes, whose rows after `j` double steps read from the edge are a word independent of the depth followed by a run of `01` pairs (`edge_decomp`, from `edge_split` and `Z_shift`);
- the truncations `c7cut N`, whose rows at times divisible by `28` are two wedges around an ether word (`c7cut_span`).

Pigeonholing the monoid images along these families gives two rows with equal rank arguments, one reachable from the other by surviving steps. The certificate's strict decrease then gives an infinite descent.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30RecognizableBarrier`: no warnings, about 3 s.
- The kit's own `Check.lean --claim partial` passes all 17 headlines, with 190 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`.
- The compiler rejected all seven mutations tested:
  - the rows odd for sixteen iterates;
  - width `12`;
  - fifteen surviving double steps;
  - one more `01` pair in the decomposition;
  - a longer ether word;
  - the rank relation without well-foundedness;
  - the width bound loosened by two.
- The worked numbers agree in Python and Wolfram Language: the first even iterates of the two rows, the largest first-even index by bit length up to `12`, and the decomposition for every odd depth up to `41`.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The barriers, the certificates and the witnesses are those of `Rule30ZeroBoundaryBarriers`, which this extends. Recognizable statistics are the classical finite-monoid recognizers of regular languages. The sharpness of `1493` and `1507` for the bound bit length plus four was observed in R30-20261108-a0fd36.

**What it does not do.** It says nothing about ranks whose values do not factor through a finite monoid and the width, or about obligations restricted to particular starts. Nothing here decides `Q01` or period 2.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
