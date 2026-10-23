---
Template: ComputationalEssay
Name: The channel bound, certified: how much a clocked center column lets its right neighbour say
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-23
Description: A partial result for Problem 1 of the Rule 30 Prize, proved in Lean against the official definitions: if the center column of a configuration reads the clock 0101… then the column beside it, read at the even times, carries about 0.258 bits of information per bit asymptotically, by a finite automaton certificate that the Lean kernel rebuilds and checks from its graph alone
Abstract: For every configuration x : ℤ → Bool whose center column reads the clock (evol x t 0 = decide (t % 2 = 1) for all t), the first n visible bits, column 1 at the even times, lie in one set S of words with |S| · 10^(9n) ≤ 218 · 1195924139^n (Rule30Submission.channel_bound_12): about 0.258 bits per visible bit asymptotically, log2(1195924139/10^9) ≈ 0.25813 with the finite correction log2(218)/n. The bound is generic in a certificate (Cert.bound): the graph of the states of a window automaton with Collatz–Wielandt weights. The kernel rebuilds every state as a bitset from the graph, checks every edge is closed and the weights satisfy the inequality, and the proof ties the window to the kit's evol. Nothing decides Q01; the right neighbour is measured, not excluded.
Keywords: [rule 30, Rule 30 Prize, Problem 1, period 2, channel bound, entropy, finite automaton, Collatz–Wielandt, verified checker, Lean 4, LeanLink]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261022-91b0b0, Corollary F](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-91b0b0)", "[Submission R30-20261023-8084e6, every Sturmian word excluded](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-8084e6)"]
---

## The question

Problem 1 of the Rule 30 Prize asks whether the center column of rule 30 is ever eventually periodic. Its first case is period 2, the clock `0101…`. Suppose some configuration keeps the clock on its center column for ever. Rule 30 is `left XOR (center OR right)`: the cell left of the clock is determined by the clock and the cell right of it, so the whole configuration is determined by its right half, and the right half is driven by the clock at its boundary. How much freedom does the column beside the clock, column `1`, keep? This essay answers with a certified number: read at the even times (the *visible bits*, the ones that feed back into column `-1`), column `1` carries about `0.258` bits of information per bit: the number of words of length `n` is at most `218 · 1.195924139^n`, an asymptotic rate of `log₂ 1.195924139 ≈ 0.25813` bits per bit with a finite correction `log₂ 218 / n`.

```wl
ArrayPlot[CellularAutomaton[30, {{1}, 0}, 40], ImageSize -> 360]
```

## The window automaton

Take the `M` cells right of the center as a window. Under the clock, one time step maps the window row `s` to `nxt[s, tv, u]`: the clock bit `tv` enters from the left and the unknown cell beyond the window, `u`, from the right. Two steps, with the clock white then black, give `step2[s, u, v]`, with the same exterior cell at two successive times as the free inputs `u, v`. The set of window rows consistent with the visible bits read so far is a state; reading the next visible bit `b` keeps the rows with cell `1` equal to `b` and takes all their images under both inputs at both steps. This subset construction is deterministic in `b`, so the number of visible words of length `n` is at most the number of paths of length `n` from the root, and that grows like the spectral radius of the graph. At width `6` the automaton has `31` states, `18` dead edges and growth rate `1.3580`; at width `8`, `56` states and `1.2801`:

```wl
nxt[m_][s_, tv_, u_] := BitAnd[BitXor[BitOr[BitShiftLeft[s, 1], tv], BitOr[s, BitShiftRight[s, 1], BitShiftLeft[u, m - 1]]], 2^m - 1];
automaton[m_] := Module[{nx = nxt[m], root = Range[0, 2^m - 1], states, index, succ, q = 1, cur, l1, l2},
   states = {root}; index = <|root -> 1|>; succ = {};
   While[q <= Length[states], cur = states[[q]];
    AppendTo[succ, Table[
      l1 = Union @@ Table[If[BitAnd[s, 1] == b, {nx[s, 0, 0], nx[s, 0, 1]}, {}], {s, cur}];
      l2 = Union @@ Table[{nx[t, 1, 0], nx[t, 1, 1]}, {t, l1}];
      If[l2 === {}, 0, If[KeyExistsQ[index, l2], index[l2], AppendTo[states, l2]; index[l2] = Length[states]]], {b, 0, 1}]];
    q++];
   {states, succ}];
growth[succ_, its_] := Module[{n = Length[succ], v, w, lam}, v = ConstantArray[1., n];
   Do[w = ConstantArray[0., n]; Do[If[succ[[i, b]] > 0, w[[succ[[i, b]]]] += v[[i]]], {i, n}, {b, 2}]; lam = Total[w]/Total[v]; v = w/Total[w], {its}]; lam];
Table[With[{a = automaton[m]}, {m, Length[a[[1]]], Count[Flatten[a[[2]]], 0], growth[a[[2]], 300]}], {m, {6, 8}}]
```

## The certificate at width 12

At width `12` the automaton has `402` states and `251` dead edges, and its growth rate is `1.19568…`, so the visible bits carry about `log₂ 1.1957 ≈ 0.258` bits each, asymptotically. A spectral radius is not something a kernel checks; a Collatz–Wielandt vector is. The certificate is the graph (`succ12`, the two successors of each state, `-1` for a dead edge) and a vector of positive integer weights `weights12` with `10⁹ (w[j₀] + w[j₁]) ≤ 1195924139 · w[i]` at every state, so that the weighted count of paths grows by at most the ratio `R / D = 1.195924139` per step. Here are both, checked:

```wl
succ12 = {{1, 2}, {3, 4}, {5, -1}, {6, 7}, {8, -1}, {9, 10}, {11, 12}, {13, -1}, {14, 15}, {16, 17}, {18, -1}, {-1, 19}, {20, -1}, {21, 22}, {23, 24}, {25, -1}, {26, 27}, {28, -1}, {29, 30}, {31, -1}, {32, 22}, {33, 24}, {34, -1}, {35, 36}, {37, -1}, {38, 39}, {-1, 40}, {41, -1}, {42, 43}, {44, -1}, {45, -1}, {46, 22}, {47, 48}, {35, 49}, {38, 50}, {-1, 51}, {52, -1}, {53, -1}, {54, -1}, {55, -1}, {56, -1}, {57, 22}, {58, 24}, {59, -1}, {60, 36}, {61, 39}, {62, 48}, {63, 49}, {37, -1}, {64, -1}, {65, -1}, {66, -1}, {67, 68}, {69, 70}, {71, 72}, {73, 39}, {74, 22}, {75, 48}, {76, 77}, {78, 50}, {-1, 79}, {80, -1}, {81, 82}, {-1, 83}, {84, 68}, {73, 85}, {86, 87}, {88, 89}, {90, -1}, {91, -1}, {92, -1}, {-1, 93}, {94, -1}, {95, -1}, {96, 48}, {97, 49}, {-1, 98}, {99, -1}, {100, -1}, {66, -1}, {101, 72}, {-1, 102}, {103, -1}, {104, -1}, {105, 89}, {106, -1}, {107, 48}, {108, -1}, {109, 110}, {111, -1}, {112, 50}, {-1, 113}, {114, -1}, {115, -1}, {116, -1}, {-1, 117}, {118, 82}, {-1, 119}, {120, -1}, {121, 122}, {123, 72}, {-1, 124}, {125, -1}, {126, 122}, {127, 128}, {129, 110}, {73, 50}, {118, 77}, {130, 50}, {-1, 131}, {132, -1}, {133, -1}, {134, -1}, {135, -1}, {136, 137}, {138, 139}, {140, -1}, {141, -1}, {-1, 142}, {143, -1}, {144, 145}, {146, -1}, {147, -1}, {-1, 148}, {149, -1}, {150, 128}, {151, 89}, {152, 48}, {153, -1}, {-1, 154}, {155, -1}, {156, -1}, {84, 157}, {136, 158}, {71, 159}, {160, -1}, {161, -1}, {92, -1}, {162, 48}, {163, -1}, {164, -1}, {165, -1}, {166, -1}, {127, 167}, {152, 168}, {169, -1}, {-1, 170}, {171, 172}, {115, -1}, {173, 139}, {174, 48}, {129, 170}, {118, -1}, {175, 50}, {176, -1}, {177, 178}, {179, 167}, {180, -1}, {181, -1}, {182, -1}, {152, 183}, {-1, 184}, {185, 186}, {187, 50}, {-1, 188}, {189, -1}, {190, 128}, {191, -1}, {192, -1}, {193, 194}, {195, -1}, {196, -1}, {197, -1}, {198, 199}, {200, -1}, {201, -1}, {202, -1}, {-1, 203}, {204, -1}, {205, 48}, {206, 50}, {207, -1}, {208, -1}, {209, -1}, {210, -1}, {-1, 211}, {212, -1}, {213, -1}, {214, -1}, {215, -1}, {216, 48}, {217, 50}, {218, -1}, {219, -1}, {220, -1}, {221, 222}, {71, 223}, {73, 172}, {-1, 186}, {224, -1}, {-1, 225}, {177, 226}, {227, -1}, {228, -1}, {229, -1}, {230, -1}, {231, -1}, {136, 232}, {233, -1}, {234, -1}, {235, -1}, {236, -1}, {237, 238}, {239, 178}, {240, 167}, {-1, 241}, {242, -1}, {243, -1}, {136, 70}, {244, 245}, {73, 246}, {247, 89}, {248, -1}, {249, -1}, {250, -1}, {251, -1}, {252, -1}, {253, -1}, {254, 139}, {255, -1}, {-1, 256}, {71, 257}, {258, -1}, {259, -1}, {136, 260}, {261, 262}, {263, -1}, {264, -1}, {265, -1}, {-1, 266}, {267, 48}, {268, -1}, {-1, 269}, {177, -1}, {-1, 270}, {271, -1}, {272, -1}, {129, 273}, {206, 274}, {275, -1}, {276, 277}, {278, 128}, {279, -1}, {-1, 280}, {281, 48}, {282, -1}, {283, -1}, {284, -1}, {285, -1}, {-1, 286}, {287, -1}, {288, -1}, {289, -1}, {290, 262}, {-1, 291}, {292, 172}, {293, -1}, {294, -1}, {295, 167}, {296, -1}, {297, -1}, {298, -1}, {73, 299}, {300, -1}, {301, -1}, {302, -1}, {303, -1}, {92, -1}, {216, 304}, {305, -1}, {306, -1}, {185, -1}, {-1, 307}, {278, 308}, {309, -1}, {136, 310}, {311, -1}, {312, -1}, {-1, 313}, {314, -1}, {315, -1}, {316, -1}, {317, -1}, {318, 319}, {-1, 320}, {227, 321}, {278, 167}, {295, 319}, {322, -1}, {323, -1}, {324, 325}, {-1, 246}, {326, -1}, {-1, 327}, {328, -1}, {329, -1}, {330, -1}, {331, -1}, {332, -1}, {333, -1}, {334, -1}, {335, 167}, {336, 137}, {337, -1}, {136, 338}, {-1, 339}, {340, 222}, {123, 223}, {-1, 199}, {341, -1}, {342, -1}, {343, -1}, {344, -1}, {-1, 85}, {345, 89}, {346, -1}, {-1, 347}, {348, -1}, {114, -1}, {-1, 349}, {227, 262}, {350, 167}, {351, 50}, {352, -1}, {353, -1}, {267, 321}, {354, -1}, {355, -1}, {356, -1}, {357, -1}, {247, 358}, {359, -1}, {355, 308}, {360, -1}, {-1, 361}, {129, 291}, {362, 172}, {363, -1}, {364, -1}, {365, -1}, {267, 168}, {366, -1}, {-1, 367}, {136, 368}, {-1, 369}, {281, 304}, {370, -1}, {355, 167}, {371, -1}, {372, -1}, {69, 277}, {373, -1}, {374, -1}, {375, 167}, {152, 376}, {377, 167}, {239, 226}, {378, -1}, {379, -1}, {380, -1}, {336, 368}, {381, -1}, {239, -1}, {382, 167}, {383, -1}, {267, 199}, {384, -1}, {267, -1}, {330, 167}, {385, -1}, {386, -1}, {-1, 387}, {227, 168}, {-1, 388}, {389, -1}, {390, 368}, {261, -1}, {391, -1}, {392, -1}, {227, 260}, {393, -1}, {394, -1}, {395, 139}, {-1, 396}, {136, -1}, {397, 48}, {380, -1}, {398, 186}, {-1, 399}, {400, -1}, {401, -1}, {290, -1}};
weights12 = {174869380839, 118795027379, 90334589220, 91738346276, 50330501567, 108032274256, 62802134227, 46908929321, 60190351780, 83175563068, 46021830130, 33658074888, 41447424738, 56098405089, 52005243693, 19976757785, 61974995826, 37495613949, 55037500261, 40251365777, 49566850581, 47111578877, 19976757785, 56172235913, 6020983232, 23889525030, 33406093471, 40710209959, 44840777920, 46970664605, 18848908579, 48136452752, 39300324005, 50319775670, 23889525030, 29252608826, 37924024027, 7199453513, 20217304685, 8351599818, 39950014686, 48685196371, 33648291561, 19976757785, 56172235913, 22540701016, 37589674266, 40978094057, 6020983232, 30924915552, 8351599818, 34982755042, 45353124591, 8608816574, 24177201286, 9986698138, 47776059193, 38245930946, 34218682378, 23889525030, 29252608826, 18604211187, 38932283816, 18080650317, 36982709860, 9986698138, 41835584994, 34261020169, 19976757785, 6995054203, 3299256074, 22197597103, 6715346871, 3590554657, 37158670293, 39717118145, 14142403674, 26779407070, 20217304685, 34982755042, 22248061084, 17536766291, 29022162230, 21621921086, 24250624845, 8351599818, 35590571684, 14440489757, 37839136809, 3133306759, 23889525030, 8364370177, 3944469649, 26545484167, 8029860953, 4292841181, 38416835023, 16572616630, 16912070122, 32024989147, 24177201286, 19890488479, 20971476119, 34707157981, 25857018319, 25867446310, 9986698138, 36541505386, 17268558982, 15157792177, 30093813579, 3746006574, 20217304685, 10001970538, 4716097233, 31745234674, 9601922317, 5132723785, 16920327756, 19818424622, 20224385802, 18331787282, 19966529043, 22197597103, 23786353341, 25079134367, 21539462279, 16866838123, 14055042425, 840538090, 12299120238, 18126399484, 35988773525, 4478750113, 24177201286, 11960419129, 2339650521, 3299256074, 27167630995, 10796119693, 11481991130, 6137161097, 20234261341, 23700170283, 14591005421, 9594664300, 21922262290, 23877292214, 26545484167, 28445518816, 15936546596, 22625096924, 14149308464, 16807592559, 1004025284, 14707639825, 21676633682, 18788083628, 3015406521, 6715346871, 14302578412, 2796852579, 26468292911, 12910162630, 13730414010, 7338393636, 24197480157, 11475612112, 3299256074, 11473311064, 26216204147, 20202675144, 8351599818, 23221415528, 13036748776, 11747838581, 1199543844, 11523148740, 6064901904, 14446838394, 22467958879, 3605006633, 8029860953, 2954318762, 3343632333, 5539322329, 26113597341, 7086801393, 16419361039, 8774978672, 14882153537, 13722785179, 3944469649, 6595691919, 7124341357, 31351440186, 24159705440, 9986698138, 21836465303, 5933429784, 15589788865, 14048347848, 1433369541, 13779635450, 7251977002, 11255168232, 18517216977, 4310124640, 9601922317, 3531950205, 3997540368, 6623422792, 31228730089, 8474093003, 19635142279, 10493027842, 11775772864, 8058637707, 4716097233, 7886762479, 8518988026, 21318070017, 16174731663, 6694423136, 7094746080, 18643035485, 5276437594, 1713007732, 16478226220, 8671630790, 13459150642, 22144022449, 2813742961, 11481991130, 4222754571, 4779565882, 7919926550, 17379520500, 19966529043, 4068288987, 12005366057, 12547687243, 14081755178, 9636337175, 4948508305, 4482278818, 6596327363, 22360328200, 19342583721, 8004837717, 8483594248, 22294492023, 6309032162, 2047434269, 8909420966, 10369431443, 16094950163, 4283815743, 3363831971, 13730414010, 2709254839, 3246004751, 2468805648, 9470448896, 20783421842, 23877292214, 4864176002, 8335348356, 15004907516, 16839539021, 5916853022, 5359277145, 7887522444, 25899560391, 4613882894, 9571996382, 6845297587, 3299256074, 12606320835, 7543938693, 2447383605, 4632827608, 12399875119, 19247170926, 5121930026, 4021697631, 16419361039, 3238871929, 3880785028, 2951312527, 8855952988, 24854235429, 20202675144, 5815997849, 9967262581, 6467948628, 20137643987, 7074921491, 6408102108, 5841141355, 30972757740, 5516665870, 11446201931, 8185272368, 3299256074, 9020795329, 2925693347, 14828135183, 10410672361, 6124252555, 2468805648, 19635142279, 3872254690, 4639935164, 3528354970, 10589867118, 29722626608, 24159705440, 4962369325, 1991936868, 11918910975, 6020983232, 7662418985, 6984375982, 20587195497, 16452730065, 13687612781, 9787782838, 3944469649, 10787006348, 3497716324, 17732154145, 12449196206, 7322955969, 2951312527, 12005366057, 1330477424, 5547822427, 1878804413, 12663499834, 19370129776, 2381012846, 14252937723, 7199453513, 9162488951, 21486256475, 19675049201, 16368173942, 11704266523, 12899263750, 9729533354, 6535519736, 8756516359, 3528354970, 1589956400, 6633588263, 2245714807, 15143410784, 803714697, 2846318862, 8608816574, 10956461388, 15177104117, 19573926308, 13996238888, 15425366964, 7814801026, 10470948274, 1878804413, 1900274013, 2684512427, 959987241, 3402790352, 13101919382, 18149495165, 11932156293, 2587959405, 6970786969, 12521281705, 2245714807, 2271390865, 1146877614, 4192115926, 21704254441, 3093811580, 2684512427, 2715219098, 1370384641, 25955482932, 3698773264, 1330477424, 1637682468, 31039636954, 1589956400, 1957350847, 26323788452, 1900274013, 25459119813, 4332426150, 5180064472, 6193777047, 7406102112};
wAt[j_] := If[j < 0, 0, weights12[[j + 1]]];
{Length[succ12], Count[Flatten[succ12], -1], And @@ Table[weights12[[i]] > 0 && 10^9 (wAt[succ12[[i, 1]]] + wAt[succ12[[i, 2]]]) <= 1195924139 weights12[[i]], {i, Length[succ12]}]}
```

The growth rate of the graph, the ratio's logarithm, and the exact number of words the automaton accepts for `n = 1 … 12` against the bound `218 · (R / D)^n`:

```wl
succ12wl = Map[If[# < 0, 0, # + 1] &, succ12, {2}];
acc[n_, i_] := acc[n, i] = If[i < 0, 0, If[n == 0, 1, acc[n - 1, succ12[[i + 1, 1]]] + acc[n - 1, succ12[[i + 1, 2]]]]];
{growth[succ12wl, 300], N[Log2[1195924139/10^9], 5], Table[acc[n, 0], {n, 1, 12}], N[218 (1195924139/10^9)^12]}
```

So twelve visible bits take at most `119` of their `4096` possible values.

## The idea of the proof

Three things make the certificate a theorem.

1. **The window follows the kit's rule.** `win x t` packs the cells `1 … M` of `evol x t` into a number, cell `p + 1` as bit `p`. One step of rule 30 on the configuration is the bit formula `nxt` on the window (`win_succ`), with the clock bit on the left and the cell beyond the window on the right; two steps under the clock are `step2` (`win_step2`).
2. **The kernel rebuilds the states.** The module carries only the graph and the weights. `check` walks the states in the order the search produced them: the root is the full bitset `2^4096 − 1`; each state's bitset is swept in `64`-bit words, each member's four images are computed and `2^image` is OR-ed into the half of an accumulator chosen by the member's low bit. The two halves are the image sets of the two letters. The first edge into a state defines its bitset; every later edge must be contained in it (`Nat.land`); a dead edge must have an empty image; at the end every state discovered must have been processed. `check_sound` turns `check = true` into the closure of every edge: every member below `2^M` with low bit `b` has its four images in the successor, which is live.
3. **The count.** Along the visible word the actual window row stays in the current state's bitset (`st_inv`), so the visible word is accepted (`visFrom_mem`); the accepted words of length `n` from state `i` number `cntA`, and `D^n · wmin · cntA ≤ R^n · w_i` by induction on `n` from the weight inequality (`weight_bound`). With `w_0 ≤ 218 · wmin` this is the headline.

The kernel's cost is in step 2: about `0.8` ms per row occurrence, `48,190` of them at width `12`. Two details made it feasible. `Nat.log2` is not among the kernel's accelerated operations, so a member's position is found by six comparisons on a `64`-bit word (`pos64`). And the kernel is lazy: a loop variable passed as an expression is re-evaluated at every use, so every one is forced to a literal before the recursive call (`force`, a `Nat.casesOn`).

## The formal proof

The module, built against the kit at the verifier's commit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["@@LEAN_SOURCE@@", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline, as Lean prints it, with the clock and the visible bits as defined:

```wl
opens = {"Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.channel_bound_12"];
{thm["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.Clock"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.visFrom"]["TypeForm", "Open" -> opens]}
```

The eventual form and the cardinality form:

```wl
{rule30Submission["Rule30Submission.channel_bound_12_eventually"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.channel_ncard_12"]["TypeForm", "Open" -> opens]}
```

The generic theorem and the three pillars: the certificate's bound, what the kernel check establishes, the window's two steps, and the weight inequality:

```wl
{rule30Submission["Rule30Submission.Cert.bound"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.check_sound"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.win_step2"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.weight_bound"]["TypeForm", "Open" -> opens]}
```

The axioms of the headline are the three standard ones and nothing else:

```wl
thm["Axioms"]
```

The proof's structure, one level down from the headline:

```wl
thm["CallGraph", "Depth" -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## What is not proved

- Nothing decides `Q01` or Problem 1. The theorem bounds how many visible words a clocked configuration can show; a bound below `1` bit per bit does not say the number of configurations is zero.
- The bound is for the clock from time `0` (`channel_bound_12`) or from an even time `T` on (`channel_bound_12_eventually`), for every configuration `ℤ → Bool`, finite or not. It is a statement about the hypothetical clocked configurations, not about the single seed, whose center column is not the clock.
- Width `12` is what the module proves. The same certificate form at widths `14` and `16` gives about `0.2445` and `0.2131` bits (certificates computed and verified outside Lean); their kernel checks cost about four and seventeen times as much and are not in this module.
- The weights are a certificate, not the spectral radius: the ratio `1.195924139` is slightly above the growth rate `1.1956850`, by design.

## Provenance

The channel bound is the Wolfram · Collatz · Mahler record's candidate 2 for the prize: an entropy bound on the visible bits of a clocked column, computed by GPT's C program and its certificates (ledger entries GC1702 and GC1705, the automaton at widths 16 and 20) after the record's earlier channel work. GPT wrote the specification of the finite obligation a proof needs (GPT-CL594-CHANNEL-BRIDGE.md, 2026-10-23): root coverage, labelled closure under all four exterior inputs, dead-edge safety, weight linkage. Cloud (Claude) built the checker and its soundness proof the same day, with the two kernel findings above, and computed the width-12 certificate by the same Collatz–Wielandt routine; the automaton rebuilt by this essay's Wolfram Language cell at small widths is the one the module's data encode at width 12.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[3] L. Collatz, *Einschließungssatz für die charakteristischen Zahlen von Matrizen*, Mathematische Zeitschrift 48 (1942) 221–226; H. Wielandt, *Unzerlegbare, nicht negative Matrizen*, Mathematische Zeitschrift 52 (1950) 642–648.

[4] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): `reports/wolfram-agents/GPT-CL594-CHANNEL-BRIDGE.md`, `reports/wolfram-agents/submissions/channel-12/`, CHAT-LEDGER.md CL596, 2026.
