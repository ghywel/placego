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
rule30Submission = LeanImportString["import Rule30PrizeKit
set_option linter.unusedSimpArgs false

/-!
# The channel bound, certified: how much a clocked center column lets its right neighbour say

**Partial result for Problem 1** (period 2, the kit's `Rule30ZeroBoundary.Q01` family). Suppose a
configuration `x : Int → Bool` has the clock on its center column, `evol x t 0 = decide (t % 2 = 1)`
for every `t` (`Clock`). Then the visible bits, column `1` at the even times, are constrained: for
every `n` the words `visFrom x 0 n = [evol x 0 1, evol x 2 1, …, evol x (2 (n - 1)) 1]` of all
clocked configurations lie in one set of at most `C (R / D) ^ n` words (`Cert.bound`,
`channel_bound_12`: `D = 10 ^ 9`, `R = 1195924139`, `C = 218` at width `12`), so they carry about
`log₂ (R / D) ≈ 0.258` bits of information per visible bit asymptotically, instead of `1`.

**The method.** The `M` cells right of the center form a window; under the clock, two time steps map
the window row `s` to `step2 s u v` with the unknown cell beyond the window at the two times as inputs `u, v`.
The set of rows consistent with the visible bits read so far is an automaton state; the certificate
is the finite graph of these states (`succ12`) with a Collatz–Wielandt weight vector (`weights12`).
The kernel rebuilds every state as a bitset of `2 ^ M` bits from the graph alone, with the bit
operations GMP evaluates, checks that every edge is closed (`check`) and that the weights satisfy
`D (w j0 + w j1) ≤ R w i` (`wcheck`); `check_sound` and `weight_bound` turn the two Boolean facts
into the bound, and `win_succ`, `win_step2` tie the window to the kit's `evol`.

What the catalog has: `Q01` reduced to the zero-boundary left half, kernel-checked up to width 52;
nothing about the right neighbour of a clocked column. Nothing here decides `Q01`: the bound says
how constrained the right neighbour is, not that no configuration keeps the clock.
-/
namespace Rule30Submission
open Ruliology.CellularAutomata Rule30Realization Rule30Jen

/-! ## 1. The kernel computation -/

/-- Force `n` to a literal before continuing (the kernel reduces the major premise of `casesOn`). -/
noncomputable def force {α : Sort u} (n : Nat) (k : Nat → α) : α :=
  Nat.casesOn (motive := fun _ => α) n (k 0) (fun m => k (Nat.succ m))

theorem force_eq {α : Sort u} (n : Nat) (k : Nat → α) : force n k = k n := by
  cases n <;> rfl

/-- One rule 30 step on an `M`-cell window `s` (cell `p + 1` is bit `p`), clock bit `tv` on the left,
input `u` on the right; `mask = 2 ^ M - 1`. -/
def nxt (M mask s tv u : Nat) : Nat :=
  Nat.land (Nat.xor (Nat.lor (Nat.shiftLeft s 1) tv)
    (Nat.lor s (Nat.lor (Nat.shiftRight s 1) (Nat.shiftLeft u (Nat.sub M 1))))) mask

/-- The same step with the right input already shifted into place (`ut = u <<< (M - 1)`). -/
def nxtT (mask s tv ut : Nat) : Nat :=
  Nat.land (Nat.xor (Nat.lor (Nat.shiftLeft s 1) tv) (Nat.lor s (Nat.lor (Nat.shiftRight s 1) ut))) mask

theorem nxtT_eq (M mask s tv u : Nat) : nxtT mask s tv (Nat.shiftLeft u (Nat.sub M 1)) = nxt M mask s tv u := rfl

/-- Two steps: the clock white, then black. -/
def step2 (M mask s u v : Nat) : Nat := nxt M mask (nxt M mask s 0 u) 1 v

/-- The bitset of the four two-step images of `s`, sharing the first step (`top = 1 <<< (M - 1)`). -/
def img4 (mask top s : Nat) : Nat :=
  let s0 := nxtT mask s 0 0
  let s1 := nxtT mask s 0 top
  Nat.lor (Nat.lor (Nat.shiftLeft 1 (nxtT mask s0 1 0)) (Nat.shiftLeft 1 (nxtT mask s0 1 top)))
    (Nat.lor (Nat.shiftLeft 1 (nxtT mask s1 1 0)) (Nat.shiftLeft 1 (nxtT mask s1 1 top)))

/-- `⌊log₂ w⌋` for `0 < w < 2 ^ 64`, by six comparisons. -/
def pos64 (w : Nat) : Nat :=
  let a := cond (Nat.ble 4294967296 w) 32 0
  let w := Nat.shiftRight w a
  let b := cond (Nat.ble 65536 w) 16 0
  let w := Nat.shiftRight w b
  let c := cond (Nat.ble 256 w) 8 0
  let w := Nat.shiftRight w c
  let d := cond (Nat.ble 16 w) 4 0
  let w := Nat.shiftRight w d
  let e := cond (Nat.ble 4 w) 2 0
  let w := Nat.shiftRight w e
  let f := cond (Nat.ble 2 w) 1 0
  Nat.add (Nat.add (Nat.add a b) (Nat.add c d)) (Nat.add e f)

/-- The members of the word `w` at base `base`, highest first: the images of each go into the
half of `acc` selected by its low bit (`H = 2 ^ M`). -/
noncomputable def wordLoop (M mask H top : Nat) (fuel : Nat) : Nat → Nat → Nat → Nat :=
  Nat.rec (motive := fun _ => Nat → Nat → Nat → Nat) (fun _ _ acc => acc)
    (fun _ ih w base acc =>
      cond (Nat.beq w 0) acc
        (force (pos64 w) fun p => force (Nat.add base p) fun s =>
          force (Nat.xor w (Nat.shiftLeft 1 p)) fun w' =>
            force (Nat.lor acc (Nat.shiftLeft (img4 mask top s) (Nat.mul (Nat.land s 1) H))) fun acc' =>
              ih w' base acc'))
    fuel

/-- Sweep the words `nwords - 1, …, 0` of the bitset `B`. -/
noncomputable def sweep (M mask H top : Nat) (nwords : Nat) : Nat → Nat → Nat :=
  Nat.rec (motive := fun _ => Nat → Nat → Nat) (fun _ acc => acc)
    (fun k ih B acc =>
      force (Nat.land (Nat.shiftRight B (Nat.mul 64 k)) 18446744073709551615) fun w =>
        cond (Nat.beq w 0) (ih B acc)
          (force (wordLoop M mask H top 64 w (Nat.mul 64 k) acc) fun acc' => ih B acc'))
    nwords

/-- The two image bitsets of `B`, packed: label `0` in the low `2 ^ M` bits, label `1` above. -/
noncomputable def imageSets (M mask H : Nat) (B : Nat) : Nat :=
  sweep M mask H (Nat.shiftRight H 1) (Nat.shiftRight H 6) B 0

def DEAD : Nat := 1000000

/-- The bitset of state `j` among `cnt` discovered ones, newest first. -/
def at_ (bits : List Nat) (cnt j : Nat) : Nat := List.getD bits (Nat.sub (Nat.sub cnt 1) j) 0

/-- One edge to `j` with image `T`: a dead edge needs `T = 0`; a new state is recorded; an old one
must contain `T`. -/
noncomputable def edge (j T : Nat) (bits : List Nat) (cnt : Nat) : Option (List Nat × Nat) :=
  force T fun T =>
  cond (Nat.beq j DEAD) (cond (Nat.beq T 0) (some (bits, cnt)) none)
    (cond (Nat.beq j cnt) (some (T :: bits, Nat.succ cnt))
      (cond (Nat.blt j cnt)
        (cond (Nat.beq (Nat.land T (at_ bits cnt j)) T) (some (bits, cnt)) none)
        none))

/-- Run over the successor list in state order; at the end every discovered state was processed. -/
noncomputable def run (M mask H ALL : Nat) : List (Nat × Nat) → Nat → List Nat → Nat → Bool :=
  List.rec (motive := fun _ => Nat → List Nat → Nat → Bool) (fun i _ cnt => Nat.beq i cnt)
    (fun p _ ih i bits cnt =>
      cond (Nat.blt i cnt)
        (force (at_ bits cnt i) fun B =>
         force (imageSets M mask H B) fun T =>
         match edge p.1 (Nat.land T ALL) bits cnt with
         | none => false
         | some (bits1, cnt1) =>
           match edge p.2 (Nat.shiftRight T H) bits1 cnt1 with
           | none => false
           | some (bits2, cnt2) => force cnt2 fun cnt2 => ih (Nat.succ i) bits2 cnt2)
        false)

/-- The closure check for width `M`. -/
noncomputable def check (M : Nat) (succ : List (Nat × Nat)) : Bool :=
  force (Nat.shiftLeft 1 M) fun H => force (Nat.sub H 1) fun mask => force (Nat.sub (Nat.shiftLeft 1 H) 1) fun ALL =>
    run M mask H ALL succ 0 [ALL] 1

/-- The weight check: `D (w j0 + w j1) ≤ R w i` with `w DEAD = 0`, every `w i > 0`. -/
def wcheck (D R : Nat) (succ : List (Nat × Nat)) (w : List Nat) : Bool :=
  (List.range succ.length).all fun i =>
    let p := succ.getD i (DEAD, DEAD)
    let wi := w.getD i 0
    Nat.blt 0 wi && Nat.ble (Nat.mul D (Nat.add (w.getD p.1 0) (w.getD p.2 0))) (Nat.mul R wi)


/-! ## 2. What the computation establishes -/

/-- `s` is a member of the bitset `B`. -/
def Mem (B s : Nat) : Prop := Nat.testBit B s = true

theorem lor_eq' (a b : Nat) : Nat.lor a b = a ||| b := rfl
theorem land_eq' (a b : Nat) : Nat.land a b = a &&& b := rfl
theorem xor_eq' (a b : Nat) : Nat.xor a b = a ^^^ b := rfl
theorem shiftLeft_eq' (a b : Nat) : Nat.shiftLeft a b = a <<< b := rfl
theorem shiftRight_eq' (a b : Nat) : Nat.shiftRight a b = a >>> b := rfl
theorem add_eq' (a b : Nat) : Nat.add a b = a + b := rfl
theorem sub_eq' (a b : Nat) : Nat.sub a b = a - b := rfl
theorem mul_eq' (a b : Nat) : Nat.mul a b = a * b := rfl

theorem beq_zero_false {w : Nat} (hw0 : w ≠ 0) : Nat.beq w 0 = false := by
  cases h : Nat.beq w 0
  · rfl
  · exact absurd (Nat.eq_of_beq_eq_true h) hw0

theorem cond_ble (c w k : Nat) : cond (Nat.ble c w) k 0 = if c ≤ w then k else 0 := by
  by_cases h : c ≤ w
  · simp [Nat.ble_eq_true_of_le h, h]
  · have : Nat.ble c w = false := by
      cases hb : Nat.ble c w
      · rfl
      · exact absurd (Nat.le_of_ble_eq_true hb) h
    simp [this, h]

/-- One halving step of `pos64`. -/
theorem pos_step (k c w : Nat) (hc : c = 2 ^ k) (hw : w < 2 ^ (2 * k)) :
    let a := if c ≤ w then k else 0
    let w' := w >>> a
    w' < 2 ^ k ∧ 2 ^ a * w' ≤ w ∧ w < 2 ^ a * (w' + 1) ∧ (0 < w → 0 < w') := by
  intro a w'
  subst hc
  simp only [a, w', Nat.shiftRight_eq_div_pow]
  by_cases h : 2 ^ k ≤ w
  · simp only [h, ite_true]
    have hpos : 0 < 2 ^ k := Nat.two_pow_pos k
    refine ⟨?_, ?_, ?_, ?_⟩
    · rw [Nat.div_lt_iff_lt_mul hpos, ← Nat.pow_add]
      rw [show k + k = 2 * k by omega]; exact hw
    · exact Nat.mul_div_le w (2 ^ k)
    · exact Nat.lt_mul_div_succ w hpos
    · intro _; exact Nat.div_pos h hpos
  · simp only [h, ite_false, Nat.pow_zero, Nat.div_one, Nat.one_mul]
    exact ⟨Nat.lt_of_not_le h, Nat.le_refl _, Nat.lt_succ_self _, fun h0 => h0⟩

theorem pos64_spec (w : Nat) (h0 : 0 < w) (h : w < 2 ^ 64) :
    2 ^ pos64 w ≤ w ∧ w < 2 ^ (pos64 w + 1) := by
  unfold pos64
  simp only [cond_ble, add_eq', shiftRight_eq']
  have s1 := pos_step 32 4294967296 w (by norm_num) (by simpa using h)
  obtain ⟨l1, le1, lt1, p1⟩ := s1
  set a := (if 4294967296 ≤ w then 32 else 0) with ha
  set w1 := w >>> a with hw1
  have s2 := pos_step 16 65536 w1 (by norm_num) (by simpa using l1)
  obtain ⟨l2, le2, lt2, p2⟩ := s2
  set b := (if 65536 ≤ w1 then 16 else 0) with hb
  set w2 := w1 >>> b with hw2
  have s3 := pos_step 8 256 w2 (by norm_num) (by simpa using l2)
  obtain ⟨l3, le3, lt3, p3⟩ := s3
  set c := (if 256 ≤ w2 then 8 else 0) with hc
  set w3 := w2 >>> c with hw3
  have s4 := pos_step 4 16 w3 (by norm_num) (by simpa using l3)
  obtain ⟨l4, le4, lt4, p4⟩ := s4
  set d := (if 16 ≤ w3 then 4 else 0) with hd
  set w4 := w3 >>> d with hw4
  have s5 := pos_step 2 4 w4 (by norm_num) (by simpa using l4)
  obtain ⟨l5, le5, lt5, p5⟩ := s5
  set e := (if 4 ≤ w4 then 2 else 0) with he
  set w5 := w4 >>> e with hw5
  have w5pos : 0 < w5 := p5 (p4 (p3 (p2 (p1 h0))))
  set f := (if 2 ≤ w5 then 1 else 0) with hf
  have hf1 : 2 ^ f ≤ w5 ∧ w5 < 2 ^ (f + 1) := by
    simp only [hf]; split_ifs with h2 <;> simp <;> omega
  -- combine: 2^(a+b+c+d+e+f) ≤ w < 2^(a+b+c+d+e+f+1)
  have key : ∀ (x y : Nat) (p q : Nat), 2 ^ p * y ≤ x → x < 2 ^ p * (y + 1) →
      2 ^ q ≤ y → y < 2 ^ (q + 1) → 2 ^ (p + q) ≤ x ∧ x < 2 ^ (p + q + 1) := by
    intro x y p q h1 h2 h3 h4
    constructor
    · calc 2 ^ (p + q) = 2 ^ p * 2 ^ q := Nat.pow_add 2 p q
        _ ≤ 2 ^ p * y := Nat.mul_le_mul_left _ h3
        _ ≤ x := h1
    · calc x < 2 ^ p * (y + 1) := h2
        _ ≤ 2 ^ p * 2 ^ (q + 1) := Nat.mul_le_mul_left _ h4
        _ = 2 ^ (p + q + 1) := by rw [← Nat.pow_add, Nat.add_assoc]
  have k5 := key w4 w5 e f le5 lt5 hf1.1 hf1.2
  have k4 := key w3 w4 d (e + f) le4 lt4 k5.1 k5.2
  have k3 := key w2 w3 c (d + (e + f)) le3 lt3 k4.1 k4.2
  have k2 := key w1 w2 b (c + (d + (e + f))) le2 lt2 k3.1 k3.2
  have k1 := key w w1 a (b + (c + (d + (e + f)))) le1 lt1 k2.1 k2.2
  have hex : a + b + (c + d) + (e + f) = a + (b + (c + (d + (e + f)))) := by omega
  rw [hex]; exact k1

theorem pos64_testBit (w : Nat) (h0 : 0 < w) (h : w < 2 ^ 64) : w.testBit (pos64 w) = true :=
  Nat.testBit_of_two_pow_le_and_two_pow_add_one_gt (pos64_spec w h0 h).1 (pos64_spec w h0 h).2

/-- Clearing the top bit leaves a number below `2 ^ pos64 w`. -/
theorem pos64_clear (w : Nat) (h0 : 0 < w) (h : w < 2 ^ 64) :
    w ^^^ (1 <<< pos64 w) < 2 ^ pos64 w := by
  rw [Nat.shiftLeft_eq, Nat.one_mul]
  apply Nat.lt_pow_two_of_testBit
  intro i hi
  rw [Nat.testBit_xor]
  rcases Nat.eq_or_lt_of_le hi with rfl | hlt
  · rw [pos64_testBit w h0 h, Nat.testBit_two_pow_self]; rfl
  · rw [Nat.testBit_two_pow_of_ne (Nat.ne_of_lt hlt)]
    have : w < 2 ^ i := lt_of_lt_of_le (pos64_spec w h0 h).2 (Nat.pow_le_pow_right (by norm_num) hlt)
    rw [Nat.testBit_lt_two_pow this]; rfl

theorem testBit_clear_of_ne (w p j : Nat) (hj : j ≠ p) :
    (w ^^^ (1 <<< p)).testBit j = w.testBit j := by
  rw [Nat.shiftLeft_eq, Nat.one_mul, Nat.testBit_xor, Nat.testBit_two_pow_of_ne (Ne.symm hj), Bool.xor_false]

/-- The four images of `s` are in `img4`. -/
theorem img4_mem (M mask top s u v : Nat) (htop : top = Nat.shiftLeft 1 (Nat.sub M 1)) (hu : u ≤ 1) (hv : v ≤ 1) :
    (img4 mask top s).testBit (step2 M mask s u v) = true := by
  unfold img4 step2
  rw [← nxtT_eq M mask s 0 u, ← nxtT_eq M mask _ 1 v]
  have h0 : Nat.shiftLeft 0 (Nat.sub M 1) = 0 := by simp [shiftLeft_eq']
  simp only [lor_eq', shiftLeft_eq', Nat.testBit_or, Nat.shiftLeft_eq, Nat.one_mul]
  rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hu with rfl | rfl <;>
  rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hv with rfl | rfl <;>
  simp [Nat.testBit_two_pow_self, htop, h0, shiftLeft_eq', Nat.shiftLeft_eq, Nat.one_mul]

theorem wordLoop_succ (M mask H top fuel w base acc : Nat) :
    wordLoop M mask H top (fuel + 1) w base acc =
      cond (Nat.beq w 0) acc
        (force (pos64 w) fun p => force (Nat.add base p) fun s =>
          force (Nat.xor w (Nat.shiftLeft 1 p)) fun w' =>
            force (Nat.lor acc (Nat.shiftLeft (img4 mask top s) (Nat.mul (Nat.land s 1) H))) fun acc' =>
              wordLoop M mask H top fuel w' base acc') := rfl

theorem wordLoop_zero (M mask H top w base acc : Nat) : wordLoop M mask H top 0 w base acc = acc := rfl

/-- Every member of the word gets its images into the right half; nothing is lost. -/
theorem wordLoop_spec (M mask H top : Nat) (htop : top = Nat.shiftLeft 1 (Nat.sub M 1)) :
    ∀ (fuel w base acc : Nat), w < 2 ^ fuel → w < 2 ^ 64 →
    (∀ t, acc.testBit t = true → (wordLoop M mask H top fuel w base acc).testBit t = true) ∧
    (∀ j, w.testBit j = true → ∀ u v, u ≤ 1 → v ≤ 1 →
      (wordLoop M mask H top fuel w base acc).testBit
        (step2 M mask (base + j) u v + (base + j) % 2 * H) = true) := by
  intro fuel
  induction fuel with
  | zero =>
    intro w base acc hw _
    have : w = 0 := by simpa using hw
    subst this
    refine ⟨fun t ht => by simpa [wordLoop_zero] using ht, fun j hj => ?_⟩
    simp at hj
  | succ n ih =>
    intro w base acc hw h64
    rw [wordLoop_succ]
    by_cases hw0 : w = 0
    · subst hw0
      rw [show Nat.beq 0 0 = true from rfl, cond_true]
      exact ⟨fun t ht => ht, fun j hj => by simp at hj⟩
    · have hbeq : Nat.beq w 0 = false := beq_zero_false hw0
      rw [hbeq]; simp only [cond_false, force_eq, lor_eq', land_eq', xor_eq', shiftLeft_eq', add_eq', mul_eq']
      have hpos : 0 < w := Nat.pos_of_ne_zero hw0
      have hp := pos64_spec w hpos h64
      have hpl : pos64 w ≤ n := by
        have : 2 ^ pos64 w < 2 ^ (n + 1) := lt_of_le_of_lt hp.1 hw
        exact Nat.lt_succ_iff.mp (Nat.pow_lt_pow_iff_right (by norm_num) |>.mp this)
      have hw' : w ^^^ (1 <<< pos64 w) < 2 ^ n :=
        lt_of_lt_of_le (pos64_clear w hpos h64) (Nat.pow_le_pow_right (by norm_num) hpl)
      have hp64 : pos64 w < 64 := by
        have := lt_of_le_of_lt hp.1 h64
        exact (Nat.pow_lt_pow_iff_right (by norm_num)).mp this
      have hw'64 : w ^^^ (1 <<< pos64 w) < 2 ^ 64 := Nat.xor_lt_two_pow h64 (by
        rw [Nat.shiftLeft_eq, Nat.one_mul]; exact Nat.pow_lt_pow_right (by norm_num) hp64)
      obtain ⟨mono, mem⟩ := ih (w ^^^ (1 <<< pos64 w)) base
        (acc ||| (img4 mask top (base + pos64 w) <<< (((base + pos64 w) &&& 1) * H))) hw' hw'64
      refine ⟨fun t ht => mono t (by rw [Nat.testBit_or, ht]; rfl), fun j hj u v hu hv => ?_⟩
      by_cases hjp : j = pos64 w
      · subst hjp
        apply mono
        rw [Nat.testBit_or, Nat.testBit_shiftLeft]
        have hland : (base + pos64 w) &&& 1 = (base + pos64 w) % 2 := Nat.and_one_is_mod _
        rw [hland]
        simp only [ge_iff_le, Nat.le_add_left, decide_true, Bool.true_and, Nat.add_sub_cancel]
        rw [img4_mem M mask top _ u v htop hu hv]; simp
      · exact mem j (by rw [testBit_clear_of_ne w (pos64 w) j hjp]; exact hj) u v hu hv

theorem sweep_succ (M mask H top k B acc : Nat) :
    sweep M mask H top (k + 1) B acc =
      force (Nat.land (Nat.shiftRight B (Nat.mul 64 k)) 18446744073709551615) fun w =>
        cond (Nat.beq w 0) (sweep M mask H top k B acc)
          (force (wordLoop M mask H top 64 w (Nat.mul 64 k) acc) fun acc' => sweep M mask H top k B acc') := rfl

theorem sweep_zero (M mask H top B acc : Nat) : sweep M mask H top 0 B acc = acc := rfl

theorem word_testBit (B k j : Nat) :
    ((B >>> (64 * k)) &&& 18446744073709551615).testBit j = (decide (j < 64) && B.testBit (64 * k + j)) := by
  rw [Nat.testBit_and, Nat.testBit_shiftRight]
  rw [show (18446744073709551615 : Nat) = 2 ^ 64 - 1 by norm_num, Nat.testBit_two_pow_sub_one]
  rw [Bool.and_comm]

theorem word_lt (B k : Nat) : (B >>> (64 * k)) &&& 18446744073709551615 < 2 ^ 64 :=
  Nat.and_lt_two_pow _ (by norm_num)

/-- Every member `s < 64 n` of `B` gets its images into the right half; nothing is lost. -/
theorem sweep_spec (M mask H top : Nat) (htop : top = Nat.shiftLeft 1 (Nat.sub M 1)) : ∀ (n B acc : Nat),
    (∀ t, acc.testBit t = true → (sweep M mask H top n B acc).testBit t = true) ∧
    (∀ s, s < 64 * n → B.testBit s = true → ∀ u v, u ≤ 1 → v ≤ 1 →
      (sweep M mask H top n B acc).testBit (step2 M mask s u v + s % 2 * H) = true) := by
  intro n
  induction n with
  | zero => intro B acc; exact ⟨fun t ht => by simpa [sweep_zero] using ht, fun s hs => by omega⟩
  | succ k ih =>
    intro B acc
    rw [sweep_succ, force_eq]
    simp only [land_eq', shiftRight_eq', mul_eq']
    set w := (B >>> (64 * k)) &&& 18446744073709551615 with hw
    by_cases hw0 : w = 0
    · rw [hw0, show Nat.beq 0 0 = true from rfl, cond_true]
      obtain ⟨mono, mem⟩ := ih B acc
      refine ⟨mono, fun s hs hB u v hu hv => ?_⟩
      by_cases hsk : s < 64 * k
      · exact mem s hsk hB u v hu hv
      · exfalso
        have hj : w.testBit (s - 64 * k) = true := by
          rw [hw, word_testBit]
          have : 64 * k + (s - 64 * k) = s := by omega
          rw [this, hB]; simp; omega
        rw [hw0] at hj; simp at hj
    · have hbeq : Nat.beq w 0 = false := beq_zero_false hw0
      rw [hbeq]; simp only [cond_false, force_eq]
      obtain ⟨wmono, wmem⟩ := wordLoop_spec M mask H top htop 64 w (64 * k) acc (hw ▸ word_lt B k) (hw ▸ word_lt B k)
      obtain ⟨mono, mem⟩ := ih B (wordLoop M mask H top 64 w (64 * k) acc)
      refine ⟨fun t ht => mono t (wmono t ht), fun s hs hB u v hu hv => ?_⟩
      by_cases hsk : s < 64 * k
      · exact mem s hsk hB u v hu hv
      · apply mono
        have hj : w.testBit (s - 64 * k) = true := by
          rw [hw, word_testBit]
          have : 64 * k + (s - 64 * k) = s := by omega
          rw [this, hB]; simp; omega
        have := wmem (s - 64 * k) hj u v hu hv
        have e : 64 * k + (s - 64 * k) = s := by omega
        rw [e] at this; exact this

/-- The packed image bitsets: label `b` members of `B` below `2 ^ M` send their images to half `b`. -/
theorem imageSets_spec (M mask H : Nat) (hM : 6 ≤ M) (hH : H = 2 ^ M) (B s u v : Nat)
    (hs : s < 2 ^ M) (hB : B.testBit s = true) (hu : u ≤ 1) (hv : v ≤ 1) :
    (imageSets M mask H B).testBit (step2 M mask s u v + s % 2 * H) = true := by
  unfold imageSets
  have htop : Nat.shiftRight H 1 = Nat.shiftLeft 1 (Nat.sub M 1) := by
    rw [hH, shiftRight_eq', shiftLeft_eq', sub_eq', Nat.shiftRight_eq_div_pow, Nat.shiftLeft_eq, Nat.one_mul]
    rw [Nat.pow_div (by omega) (by norm_num)]
  apply (sweep_spec M mask H _ htop (H >>> 6) B 0).2 s _ hB u v hu hv
  rw [hH, Nat.shiftRight_eq_div_pow]
  have : 2 ^ M = 64 * (2 ^ M / 2 ^ 6) := by
    rw [show (64 : Nat) = 2 ^ 6 by norm_num]
    rw [Nat.mul_div_cancel' (Nat.pow_dvd_pow 2 hM)]
  omega


/-! ### The run: every edge of the graph is closed -/

theorem nxt_lt (M mask s tv u : Nat) (hmask : mask = 2 ^ M - 1) : nxt M mask s tv u < 2 ^ M := by
  unfold nxt; simp only [land_eq']; rw [hmask]
  exact Nat.and_lt_two_pow _ (Nat.sub_lt (Nat.two_pow_pos M) Nat.one_pos)

theorem step2_lt (M mask s u v : Nat) (hmask : mask = 2 ^ M - 1) : step2 M mask s u v < 2 ^ M :=
  nxt_lt M mask _ 1 v hmask

/-- The successor of state `i` on letter `b` in the list `succ` (`DEAD` past the end). -/
def succAt (succ : List (Nat × Nat)) (i b : Nat) : Nat :=
  if b = 0 then (succ.getD i (DEAD, DEAD)).1 else (succ.getD i (DEAD, DEAD)).2

/-- Edge `(i, b) → j` is closed: every member of `Bset i` below `2 ^ M` with low bit `b` has its four
two-step images in `Bset j`, and `j` is a live state below `N`. -/
def EdgeOK (M mask : Nat) (Bset : Nat → Nat) (N i j b : Nat) : Prop :=
  ∀ s, s < 2 ^ M → (Bset i).testBit s = true → s % 2 = b →
    j < N ∧ ∀ u v, u ≤ 1 → v ≤ 1 → (Bset j).testBit (step2 M mask s u v) = true

theorem at_cons_lt (T : Nat) (bits : List Nat) (cnt k : Nat) (hk : k < cnt) :
    at_ (T :: bits) (cnt + 1) k = at_ bits cnt k := by
  unfold at_
  simp only [sub_eq']
  have : cnt + 1 - 1 - k = (cnt - 1 - k) + 1 := by omega
  rw [this, List.getD_cons_succ]

theorem at_cons_self (T : Nat) (bits : List Nat) (cnt : Nat) : at_ (T :: bits) (cnt + 1) cnt = T := by
  unfold at_; simp only [sub_eq']
  rw [show cnt + 1 - 1 - cnt = 0 by omega, List.getD_cons_zero]

theorem edge_sound (j T : Nat) (bits : List Nat) (cnt : Nat) (bits' : List Nat) (cnt' : Nat)
    (h : edge j T bits cnt = some (bits', cnt')) (hlen : cnt = bits.length) :
    cnt' = bits'.length ∧ cnt ≤ cnt' ∧ (∀ k, k < cnt → at_ bits' cnt' k = at_ bits cnt k) ∧
    (j = DEAD → T = 0) ∧
    (j ≠ DEAD → j < cnt' ∧ ∀ t, T.testBit t = true → (at_ bits' cnt' j).testBit t = true) := by
  unfold edge at h
  rw [force_eq] at h
  cases hjd : Nat.beq j DEAD with
  | true =>
    rw [hjd, cond_true] at h
    have hj : j = DEAD := Nat.eq_of_beq_eq_true hjd
    cases hT : Nat.beq T 0 with
    | true =>
      rw [hT, cond_true] at h
      have hT0 : T = 0 := Nat.eq_of_beq_eq_true hT
      simp only [Option.some.injEq, Prod.mk.injEq] at h
      obtain ⟨rfl, rfl⟩ := h
      exact ⟨hlen, Nat.le_refl _, fun _ _ => rfl, fun _ => hT0, fun hne => absurd hj hne⟩
    | false => rw [hT, cond_false] at h; cases h
  | false =>
    rw [hjd, cond_false] at h
    have hj : j ≠ DEAD := Nat.ne_of_beq_eq_false hjd
    cases hjc : Nat.beq j cnt with
    | true =>
      rw [hjc, cond_true] at h
      have hjc' : j = cnt := Nat.eq_of_beq_eq_true hjc
      simp only [Option.some.injEq, Prod.mk.injEq] at h
      obtain ⟨rfl, rfl⟩ := h
      refine ⟨by simp [hlen], Nat.le_succ _, fun k hk => at_cons_lt T bits cnt k hk, fun hd => absurd hd hj,
        fun _ => ⟨by omega, fun t ht => ?_⟩⟩
      rw [hjc', at_cons_self]; exact ht
    | false =>
      rw [hjc, cond_false] at h
      cases hlt : Nat.blt j cnt with
      | true =>
        rw [hlt, cond_true] at h
        have hjlt : j < cnt := Nat.le_of_ble_eq_true hlt
        cases hsub : Nat.beq (Nat.land T (at_ bits cnt j)) T with
        | true =>
          rw [hsub, cond_true] at h
          have hsub' : T &&& at_ bits cnt j = T := Nat.eq_of_beq_eq_true hsub
          simp only [Option.some.injEq, Prod.mk.injEq] at h
          obtain ⟨rfl, rfl⟩ := h
          refine ⟨hlen, Nat.le_refl _, fun _ _ => rfl, fun hd => absurd hd hj, fun _ => ⟨hjlt, fun t ht => ?_⟩⟩
          have := congrArg (fun x => x.testBit t) hsub'
          simp only [Nat.testBit_and, ht, Bool.true_and] at this
          exact this
        | false => rw [hsub, cond_false] at h; cases h
      | false => rw [hlt, cond_false] at h; cases h

theorem run_nil (M mask H ALL i : Nat) (bits : List Nat) (cnt : Nat) :
    run M mask H ALL [] i bits cnt = Nat.beq i cnt := rfl

theorem run_cons (M mask H ALL : Nat) (p : Nat × Nat) (l : List (Nat × Nat)) (i : Nat) (bits : List Nat) (cnt : Nat) :
    run M mask H ALL (p :: l) i bits cnt =
      cond (Nat.blt i cnt)
        (force (at_ bits cnt i) fun B =>
         force (imageSets M mask H B) fun T =>
         match edge p.1 (Nat.land T ALL) bits cnt with
         | none => false
         | some (bits1, cnt1) =>
           match edge p.2 (Nat.shiftRight T H) bits1 cnt1 with
           | none => false
           | some (bits2, cnt2) => force cnt2 fun cnt2 => run M mask H ALL l (Nat.succ i) bits2 cnt2)
        false := rfl

theorem succAt_cons_succ (p : Nat × Nat) (l : List (Nat × Nat)) (k b : Nat) :
    succAt (p :: l) (k + 1) b = succAt l k b := by
  unfold succAt; rw [List.getD_cons_succ]

theorem succAt_cons_zero (p : Nat × Nat) (l : List (Nat × Nat)) (b : Nat) :
    succAt (p :: l) 0 b = if b = 0 then p.1 else p.2 := by
  unfold succAt; rw [List.getD_cons_zero]

theorem run_sound (M mask H ALL : Nat) (hM : 6 ≤ M) (hmask : mask = 2 ^ M - 1) (hH : H = 2 ^ M)
    (hALL : ALL = 2 ^ H - 1) :
    ∀ (l : List (Nat × Nat)) (i : Nat) (bits : List Nat) (cnt : Nat),
      run M mask H ALL l i bits cnt = true → cnt = bits.length → i ≤ cnt →
      ∃ (bitsF : List Nat) (cntF : Nat), cntF = bitsF.length ∧ cnt ≤ cntF ∧
        (∀ k, k < cnt → at_ bitsF cntF k = at_ bits cnt k) ∧ cntF = i + l.length ∧
        ∀ k, k < l.length → ∀ b, b ≤ 1 →
          EdgeOK M mask (at_ bitsF cntF) cntF (i + k) (succAt l k b) b := by
  intro l
  induction l with
  | nil =>
    intro i bits cnt hrun hlen hi
    rw [run_nil] at hrun
    have := Nat.eq_of_beq_eq_true hrun
    exact ⟨bits, cnt, hlen, Nat.le_refl _, fun _ _ => rfl, by simp [this], fun k hk => by simp at hk⟩
  | cons p l ih =>
    intro i bits cnt hrun hlen hi
    rw [run_cons] at hrun
    cases hblt : Nat.blt i cnt with
    | false => rw [hblt, cond_false] at hrun; cases hrun
    | true =>
    rw [hblt, cond_true, force_eq, force_eq] at hrun
    have hilt : i < cnt := Nat.le_of_ble_eq_true hblt
    set B := at_ bits cnt i with hB
    set T := imageSets M mask H B with hT
    rcases h1 : edge p.1 (Nat.land T ALL) bits cnt with _ | ⟨bits1, cnt1⟩
    · rw [h1] at hrun; cases hrun
    rw [h1] at hrun; dsimp only at hrun
    rcases h2 : edge p.2 (Nat.shiftRight T H) bits1 cnt1 with _ | ⟨bits2, cnt2⟩
    · rw [h2] at hrun; cases hrun
    rw [h2] at hrun; dsimp only at hrun; rw [force_eq] at hrun
    obtain ⟨len1, le1, st1, dead1, live1⟩ := edge_sound _ _ _ _ _ _ h1 hlen
    obtain ⟨len2, le2, st2, dead2, live2⟩ := edge_sound _ _ _ _ _ _ h2 len1
    obtain ⟨bitsF, cntF, lenF, leF, stF, cntF_eq, edges⟩ := ih (Nat.succ i) bits2 cnt2 hrun len2 (by omega)
    refine ⟨bitsF, cntF, lenF, by omega, ?_, by simp [cntF_eq]; omega, ?_⟩
    · intro k hk
      rw [stF k (by omega), st2 k (by omega), st1 k hk]
    · intro k hk b hb
      cases k with
      | succ k' =>
        rw [succAt_cons_succ]
        have := edges k' (by simpa using hk) b hb
        rw [show i + (k' + 1) = Nat.succ i + k' by omega]
        exact this
      | zero =>
        rw [succAt_cons_zero]
        intro s hs hmem hsb
        rw [Nat.add_zero, stF i (by omega), st2 i (by omega), st1 i hilt] at hmem
        have himg := fun u v hu hv => imageSets_spec M mask H hM hH B s u v hs hmem hu hv
        have hst2 : ∀ u v, step2 M mask s u v < H := fun u v => hH ▸ step2_lt M mask s u v hmask
        rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hb with rfl | rfl
        · simp only [ite_true]
          have hT0 : ∀ u v, u ≤ 1 → v ≤ 1 → (Nat.land T ALL).testBit (step2 M mask s u v) = true := by
            intro u v hu hv
            rw [land_eq', Nat.testBit_and, hALL, Nat.testBit_two_pow_sub_one]
            have := himg u v hu hv
            rw [hsb, Nat.zero_mul, Nat.add_zero] at this
            rw [this]; simp [hst2 u v]
          by_cases hd : p.1 = DEAD
          · exfalso
            have := hT0 0 0 (Nat.le_refl _ |>.trans (Nat.zero_le 1)) (Nat.zero_le 1)
            rw [dead1 hd] at this; simp at this
          · obtain ⟨hj, hmemj⟩ := live1 hd
            refine ⟨by omega, fun u v hu hv => ?_⟩
            rw [stF _ (by omega), st2 _ (by omega)]
            exact hmemj _ (hT0 u v hu hv)
        · simp only [one_ne_zero, ite_false]
          have hT1 : ∀ u v, u ≤ 1 → v ≤ 1 → (Nat.shiftRight T H).testBit (step2 M mask s u v) = true := by
            intro u v hu hv
            rw [shiftRight_eq', Nat.testBit_shiftRight]
            have := himg u v hu hv
            rw [hsb, Nat.one_mul, Nat.add_comm] at this
            exact this
          by_cases hd : p.2 = DEAD
          · exfalso
            have := hT1 0 0 (Nat.zero_le 1) (Nat.zero_le 1)
            rw [dead2 hd] at this; simp at this
          · obtain ⟨hj, hmemj⟩ := live2 hd
            refine ⟨by omega, fun u v hu hv => ?_⟩
            rw [stF _ (by omega)]
            exact hmemj _ (hT1 u v hu hv)

/-- `check M succ = true` gives bitsets for the states, the root full, every edge closed. -/
theorem check_sound (M : Nat) (hM : 6 ≤ M) (succ : List (Nat × Nat)) (h : check M succ = true) :
    ∃ Bset : Nat → Nat, Bset 0 = 2 ^ (2 ^ M) - 1 ∧
      ∀ i, i < succ.length → ∀ b, b ≤ 1 →
        EdgeOK M (2 ^ M - 1) Bset succ.length i (succAt succ i b) b := by
  unfold check at h
  simp only [force_eq, shiftLeft_eq', sub_eq', Nat.shiftLeft_eq, Nat.one_mul] at h
  obtain ⟨bitsF, cntF, lenF, leF, stF, cntF_eq, edges⟩ :=
    run_sound M (2 ^ M - 1) (2 ^ M) (2 ^ 2 ^ M - 1) hM rfl rfl rfl succ 0 [2 ^ 2 ^ M - 1] 1 h rfl (Nat.zero_le 1)
  have hc : cntF = succ.length := by simpa using cntF_eq
  subst hc
  refine ⟨at_ bitsF succ.length, ?_, ?_⟩
  · rw [stF 0 Nat.one_pos]; rfl
  · intro i hi b hb
    have := edges i hi b hb
    rw [Nat.zero_add] at this
    exact this


/-! ## 3. The physical window -/

/-- The `M` cells right of the center at time `t`, cell `p + 1` as bit `p`. -/
def win (x : Int → Bool) (t : Nat) : Nat → Nat
  | 0 => 0
  | M + 1 => 2 ^ M * (evol x t ((M + 1 : Nat) : Int)).toNat + win x t M

theorem win_lt (x : Int → Bool) (t : Nat) : ∀ M, win x t M < 2 ^ M
  | 0 => by simp [win]
  | M + 1 => by
    unfold win
    have h1 := win_lt x t M
    have h2 : (evol x t ((M + 1 : Nat) : Int)).toNat ≤ 1 := Bool.toNat_le _
    calc 2 ^ M * (evol x t ((M + 1 : Nat) : Int)).toNat + win x t M
        ≤ 2 ^ M * 1 + win x t M := by gcongr
      _ < 2 ^ M * 1 + 2 ^ M := by omega
      _ = 2 ^ (M + 1) := by rw [Nat.pow_succ]; ring

theorem win_testBit (x : Int → Bool) (t : Nat) : ∀ M p,
    (win x t M).testBit p = (decide (p < M) && evol x t ((p + 1 : Nat) : Int))
  | 0, p => by simp [win]
  | M + 1, p => by
    unfold win
    rw [Nat.testBit_two_pow_mul_add _ (win_lt x t M)]
    by_cases hp : p < M
    · rw [if_pos hp, win_testBit x t M p]
      simp [hp, Nat.lt_succ_of_lt hp]
    · rw [if_neg hp, Nat.testBit_bool_toNat]
      by_cases hpm : p = M
      · subst hpm; simp
      · have : ¬ p < M + 1 := by omega
        have : p - M ≠ 0 := by omega
        simp [*]

theorem win_mod_two (x : Int → Bool) (t M : Nat) (hM : 0 < M) :
    win x t M % 2 = (evol x t 1).toNat := by
  have h := win_testBit x t M 0
  rw [Nat.testBit_eq_decide_div_mod_eq] at h
  simp only [Nat.pow_zero, Nat.div_one, hM, decide_true, Bool.true_and] at h
  have : (0 + 1 : Nat) = 1 := rfl
  rw [this] at h
  cases hc : evol x t ((1 : Nat) : Int)
  · rw [hc] at h; simp at h; simp [h]
  · rw [hc] at h; simp at h; simp [h]

/-- One step of the window is `nxt`. -/
theorem win_succ (x : Int → Bool) (t M : Nat) (hM : 1 ≤ M) :
    win x (t + 1) M = nxt M (2 ^ M - 1) (win x t M) (evol x t 0).toNat (evol x t ((M + 1 : Nat) : Int)).toNat := by
  apply Nat.eq_of_testBit_eq
  intro p
  unfold nxt
  simp only [land_eq', xor_eq', lor_eq', shiftLeft_eq', shiftRight_eq', sub_eq']
  rw [Nat.testBit_and, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_or, Nat.testBit_or,
    Nat.testBit_shiftLeft, Nat.testBit_shiftRight, Nat.testBit_shiftLeft, Nat.testBit_two_pow_sub_one,
    Nat.testBit_bool_toNat, Nat.testBit_bool_toNat, win_testBit, win_testBit, win_testBit, win_testBit]
  by_cases hp : p < M
  · simp only [hp, decide_true, Bool.true_and, Bool.and_true]
    rw [show evol x (t + 1) ((p + 1 : Nat) : Int) =
        rule (evol x t (((p + 1 : Nat) : Int) - 1)) (evol x t ((p + 1 : Nat) : Int)) (evol x t (((p + 1 : Nat) : Int) + 1)) from rfl]
    unfold rule
    have e1 : (((p + 1 : Nat) : Int) - 1) = ((p : Nat) : Int) := by push_cast; ring
    have e2 : (((p + 1 : Nat) : Int) + 1) = ((p + 2 : Nat) : Int) := by push_cast; ring
    rw [e1, e2]
    by_cases h0 : p = 0
    · subst h0
      simp only [ge_iff_le, Nat.zero_le, Nat.lt_irrefl, decide_false, Bool.false_and, Bool.false_or, Nat.sub_zero,
        Nat.zero_add, decide_true, Bool.true_and]
      have hM1 : ¬ (0 ≥ M - 1) ∨ (0 ≥ M - 1) := by tauto
      by_cases hm : M = 1
      · subst hm; simp
      · have : ¬ (0 ≥ M - 1) := by omega
        have : 0 + 1 < M := by omega
        simp [*]
    · have h1 : p ≥ 1 := Nat.pos_of_ne_zero h0
      simp only [h1, ge_iff_le, decide_true, Bool.true_and, h0, decide_false, Bool.false_and, Bool.or_false]
      have hpm : p - 1 < M := by omega
      simp only [hpm, decide_true, Bool.true_and]
      rw [show p - 1 + 1 = p by omega, show 1 + p = p + 1 by omega]
      by_cases hlast : p + 1 < M
      · have : ¬ (p ≥ M - 1) := by omega
        simp [hlast, this, show ((p : Int) + 1 + 1) = (p : Int) + 2 by ring]
      · have hpM : M = p + 1 := by omega
        subst hpM
        simp [show ((p : Int) + 1 + 1) = (p : Int) + 2 by ring]
  · simp [hp]

/-- The clock: column `0` reads `0, 1, 0, 1, …` from time `0`. -/
def Clock (x : Int → Bool) : Prop := ∀ t, evol x t 0 = decide (t % 2 = 1)

/-- Two steps under the clock are `step2`. -/
theorem win_step2 (x : Int → Bool) (hx : Clock x) (k M : Nat) (hM : 1 ≤ M) :
    win x (2 * k + 2) M = step2 M (2 ^ M - 1) (win x (2 * k) M)
      (evol x (2 * k) ((M + 1 : Nat) : Int)).toNat (evol x (2 * k + 1) ((M + 1 : Nat) : Int)).toNat := by
  unfold step2
  have h0 : (evol x (2 * k) 0).toNat = 0 := by rw [hx]; simp
  have h1 : (evol x (2 * k + 1) 0).toNat = 1 := by rw [hx]; simp
  rw [show 2 * k + 2 = (2 * k + 1) + 1 by omega, win_succ x (2 * k + 1) M hM, win_succ x (2 * k) M hM, h0, h1]

/-! ## 4. The walk and the count -/

/-- The automaton state after reading `k` visible bits. -/
def st (succ : List (Nat × Nat)) (x : Int → Bool) : Nat → Nat
  | 0 => 0
  | k + 1 => succAt succ (st succ x k) (evol x (2 * k) 1).toNat

theorem st_inv (M : Nat) (hM : 6 ≤ M) (succ : List (Nat × Nat)) (hN : 0 < succ.length)
    (Bset : Nat → Nat) (hB0 : Bset 0 = 2 ^ (2 ^ M) - 1)
    (hE : ∀ i, i < succ.length → ∀ b, b ≤ 1 → EdgeOK M (2 ^ M - 1) Bset succ.length i (succAt succ i b) b)
    (x : Int → Bool) (hx : Clock x) :
    ∀ k, st succ x k < succ.length ∧ (Bset (st succ x k)).testBit (win x (2 * k) M) = true := by
  intro k
  induction k with
  | zero =>
    refine ⟨hN, ?_⟩
    simp only [st, hB0, Nat.testBit_two_pow_sub_one]
    simp [win_lt x 0 M]
  | succ k ih =>
    obtain ⟨hlt, hmem⟩ := ih
    have hb : (evol x (2 * k) 1).toNat ≤ 1 := Bool.toNat_le _
    have := hE (st succ x k) hlt _ hb (win x (2 * k) M) (win_lt x _ M) hmem
      (win_mod_two x (2 * k) M (by omega))
    obtain ⟨hj, himg⟩ := this
    refine ⟨hj, ?_⟩
    show (Bset (succAt succ (st succ x k) (evol x (2 * k) 1).toNat)).testBit (win x (2 * (k + 1)) M) = true
    rw [show 2 * (k + 1) = 2 * k + 2 by ring, win_step2 x hx k M (by omega)]
    exact himg _ _ (Bool.toNat_le _) (Bool.toNat_le _)

/-- The accepted words of length `n` from state `i`. -/
def AccF (succ : List (Nat × Nat)) : Nat → Nat → Finset (List Bool)
  | 0, i => if i < succ.length then {[]} else ∅
  | n + 1, i => if i < succ.length then
      (AccF succ n (succAt succ i 0)).image (List.cons false) ∪ (AccF succ n (succAt succ i 1)).image (List.cons true)
    else ∅

/-- Their number, by the recursion of the automaton. -/
def cntA (succ : List (Nat × Nat)) : Nat → Nat → Nat
  | 0, i => if i < succ.length then 1 else 0
  | n + 1, i => if i < succ.length then cntA succ n (succAt succ i 0) + cntA succ n (succAt succ i 1) else 0

theorem card_AccF_le (succ : List (Nat × Nat)) : ∀ n i, (AccF succ n i).card ≤ cntA succ n i
  | 0, i => by unfold AccF cntA; split_ifs <;> simp
  | n + 1, i => by
    unfold AccF cntA
    split_ifs with h
    · calc _ ≤ ((AccF succ n (succAt succ i 0)).image (List.cons false)).card +
            ((AccF succ n (succAt succ i 1)).image (List.cons true)).card := Finset.card_union_le _ _
        _ ≤ (AccF succ n (succAt succ i 0)).card + (AccF succ n (succAt succ i 1)).card :=
            Nat.add_le_add Finset.card_image_le Finset.card_image_le
        _ ≤ _ := by have := card_AccF_le succ n (succAt succ i 0); have := card_AccF_le succ n (succAt succ i 1); omega
    · simp

/-- The visible bits from the `k`-th even time on, `n` of them. -/
def visFrom (x : Int → Bool) : Nat → Nat → List Bool
  | _, 0 => []
  | k, n + 1 => evol x (2 * k) 1 :: visFrom x (k + 1) n

theorem visFrom_mem (M : Nat) (hM : 6 ≤ M) (succ : List (Nat × Nat)) (hN : 0 < succ.length)
    (Bset : Nat → Nat) (hB0 : Bset 0 = 2 ^ (2 ^ M) - 1)
    (hE : ∀ i, i < succ.length → ∀ b, b ≤ 1 → EdgeOK M (2 ^ M - 1) Bset succ.length i (succAt succ i b) b)
    (x : Int → Bool) (hx : Clock x) : ∀ n k, visFrom x k n ∈ AccF succ n (st succ x k) := by
  intro n
  induction n with
  | zero => intro k; simp [visFrom, AccF, (st_inv M hM succ hN Bset hB0 hE x hx k).1]
  | succ n ih =>
    intro k
    have hlt := (st_inv M hM succ hN Bset hB0 hE x hx k).1
    simp only [visFrom, AccF, hlt, ite_true, Finset.mem_union, Finset.mem_image]
    have := ih (k + 1)
    simp only [st] at this
    cases hb : evol x (2 * k) 1
    · left; refine ⟨visFrom x (k + 1) n, ?_, rfl⟩; rw [hb] at this; simpa using this
    · right; refine ⟨visFrom x (k + 1) n, ?_, rfl⟩; rw [hb] at this; simpa using this

theorem wcheck_sound (D R : Nat) (succ : List (Nat × Nat)) (w : List Nat) (h : wcheck D R succ w = true) :
    ∀ i, i < succ.length → 0 < w.getD i 0 ∧
      D * (w.getD (succAt succ i 0) 0 + w.getD (succAt succ i 1) 0) ≤ R * w.getD i 0 := by
  intro i hi
  unfold wcheck at h
  rw [List.all_eq_true] at h
  have := h i (List.mem_range.mpr hi)
  simp only [Bool.and_eq_true] at this
  obtain ⟨h1, h2⟩ := this
  refine ⟨Nat.le_of_ble_eq_true h1, ?_⟩
  have := Nat.le_of_ble_eq_true h2
  simpa [succAt, mul_eq', add_eq'] using this

/-- The weight bound: `D ^ n · wmin · cntA n i ≤ R ^ n · w i`. -/
theorem weight_bound (D R : Nat) (succ : List (Nat × Nat)) (w : List Nat) (hw : wcheck D R succ w = true)
    (wmin : Nat) (hmin : ∀ i, i < succ.length → wmin ≤ w.getD i 0) :
    ∀ n i, D ^ n * wmin * cntA succ n i ≤ R ^ n * w.getD i 0 := by
  intro n
  induction n with
  | zero =>
    intro i; unfold cntA
    split_ifs with h
    · simpa using hmin i h
    · simp
  | succ n ih =>
    intro i; unfold cntA
    split_ifs with h
    · obtain ⟨_, hineq⟩ := wcheck_sound D R succ w hw i h
      have h0 := ih (succAt succ i 0)
      have h1 := ih (succAt succ i 1)
      calc D ^ (n + 1) * wmin * (cntA succ n (succAt succ i 0) + cntA succ n (succAt succ i 1))
          = D * (D ^ n * wmin * cntA succ n (succAt succ i 0)) + D * (D ^ n * wmin * cntA succ n (succAt succ i 1)) := by ring
        _ ≤ D * (R ^ n * w.getD (succAt succ i 0) 0) + D * (R ^ n * w.getD (succAt succ i 1) 0) := by gcongr
        _ = R ^ n * (D * (w.getD (succAt succ i 0) 0 + w.getD (succAt succ i 1) 0)) := by ring
        _ ≤ R ^ n * (R * w.getD i 0) := by gcongr
        _ = R ^ (n + 1) * w.getD i 0 := by ring
    · simp

/-! ## 5. The certificate and the bound -/

/-- A certificate: the width, the graph, the weights and the ratio `R / D`. -/
structure Cert where
  M : Nat
  succ : List (Nat × Nat)
  w : List Nat
  D : Nat
  R : Nat
  C : Nat
  wmin : Nat

/-- What the kernel checks of a certificate. -/
structure Cert.Valid (c : Cert) : Prop where
  hM : 6 ≤ c.M
  hcheck : check c.M c.succ = true
  hw : wcheck c.D c.R c.succ c.w = true
  hN : 0 < c.succ.length
  hlen : c.succ.length ≤ c.w.length
  hmin : c.w.all (fun v => Nat.ble c.wmin v) = true
  hmin0 : 0 < c.wmin
  hC : c.w.getD 0 0 ≤ c.C * c.wmin

/-- **The channel bound.** For a valid certificate and every `n`, a set of at most
`C (R / D) ^ n` words of length `n` contains the first `n` visible bits of every configuration
whose center column reads the clock from time `0`. -/
theorem Cert.bound (c : Cert) (hv : c.Valid) (n : Nat) :
    ∃ S : Finset (List Bool), (∀ x : Int → Bool, Clock x → visFrom x 0 n ∈ S) ∧
      S.card * c.D ^ n ≤ c.C * c.R ^ n := by
  obtain ⟨Bset, hB0, hE⟩ := check_sound c.M hv.hM c.succ hv.hcheck
  refine ⟨AccF c.succ n 0, fun x hx => visFrom_mem c.M hv.hM c.succ hv.hN Bset hB0 hE x hx n 0, ?_⟩
  have hmin : ∀ i, i < c.succ.length → c.wmin ≤ c.w.getD i 0 := by
    intro i hi
    have hl : i < c.w.length := lt_of_lt_of_le hi hv.hlen
    have hmem : c.w.getD i 0 ∈ c.w := by
      rw [List.getD_eq_getElem _ _ hl]; exact List.getElem_mem hl
    exact Nat.le_of_ble_eq_true (List.all_eq_true.mp hv.hmin _ hmem)
  have hwb := weight_bound c.D c.R c.succ c.w hv.hw c.wmin hmin n 0
  have hcard := card_AccF_le c.succ n 0
  have h1 : c.D ^ n * c.wmin * (AccF c.succ n 0).card ≤ c.R ^ n * (c.C * c.wmin) :=
    le_trans (Nat.mul_le_mul_left _ hcard) (le_trans hwb (Nat.mul_le_mul_left _ hv.hC))
  have h2 : c.wmin * ((AccF c.succ n 0).card * c.D ^ n) ≤ c.wmin * (c.C * c.R ^ n) := by
    calc c.wmin * ((AccF c.succ n 0).card * c.D ^ n) = c.D ^ n * c.wmin * (AccF c.succ n 0).card := by ring
      _ ≤ c.R ^ n * (c.C * c.wmin) := h1
      _ = c.wmin * (c.C * c.R ^ n) := by ring
  exact Nat.le_of_mul_le_mul_left h2 hv.hmin0


/-- The number of distinct words a set of visible prefixes can take, as a cardinality. -/
theorem Cert.ncard_bound (c : Cert) (hv : c.Valid) (n : Nat) :
    Set.ncard {w : List Bool | ∃ x : Int → Bool, Clock x ∧ visFrom x 0 n = w} * c.D ^ n ≤ c.C * c.R ^ n := by
  obtain ⟨S, hS, hcard⟩ := c.bound hv n
  have hsub : {w : List Bool | ∃ x : Int → Bool, Clock x ∧ visFrom x 0 n = w} ⊆ (S : Set (List Bool)) := by
    rintro w ⟨x, hx, rfl⟩; exact hS x hx
  have := Set.ncard_le_ncard hsub S.finite_toSet
  rw [Set.ncard_coe_finset] at this
  calc _ ≤ S.card * c.D ^ n := Nat.mul_le_mul_right _ this
    _ ≤ _ := hcard

/-- Shifting time: the evolution from time `T` on is the evolution of the row at time `T`. -/
theorem evol_add (x : Int → Bool) (T : Nat) : ∀ t p, evol x (T + t) p = evol (fun q => evol x T q) t p
  | 0, p => by simp [evol]
  | t + 1, p => by
    rw [show T + (t + 1) = (T + t) + 1 by omega]
    show rule (evol x (T + t) (p - 1)) (evol x (T + t) p) (evol x (T + t) (p + 1)) = _
    rw [evol_add x T t, evol_add x T t, evol_add x T t]; rfl

/-- **The eventual form.** If the center column reads the clock from an even time `T` on, the
visible bits from `T` on are bounded in the same way. -/
theorem Cert.bound_eventually (c : Cert) (hv : c.Valid) (n : Nat) :
    ∃ S : Finset (List Bool),
      (∀ (x : Int → Bool) (T : Nat), T % 2 = 0 → (∀ t, T ≤ t → evol x t 0 = decide (t % 2 = 1)) →
        visFrom (fun q => evol x T q) 0 n ∈ S) ∧
      S.card * c.D ^ n ≤ c.C * c.R ^ n := by
  obtain ⟨S, hS, hcard⟩ := c.bound hv n
  refine ⟨S, fun x T hT hx => hS _ ?_, hcard⟩
  intro t
  rw [← evol_add x T t 0, hx (T + t) (Nat.le_add_right T t)]
  have h2 : (T + t) % 2 = t % 2 := by omega
  rw [h2]

theorem visFrom_getD (x : Int → Bool) : ∀ n k m, m < n → (visFrom x k n).getD m false = evol x (2 * (k + m)) 1
  | 0, _, _, h => by omega
  | n + 1, k, 0, _ => by simp [visFrom]
  | n + 1, k, m + 1, h => by
    simp only [visFrom, List.getD_cons_succ]
    rw [visFrom_getD x n (k + 1) m (by omega)]
    congr 2; omega

/-! ## 6. Width 12 -/

def succ12 : List (Nat × Nat) := [(1,2),(3,4),(5,1000000),(6,7),(8,1000000),(9,10),(11,12),(13,1000000),(14,15),(16,17),(18,1000000),(1000000,19),(20,1000000),(21,22),(23,24),(25,1000000),(26,27),(28,1000000),(29,30),(31,1000000),(32,22),(33,24),(34,1000000),(35,36),(37,1000000),(38,39),(1000000,40),(41,1000000),(42,43),(44,1000000),(45,1000000),(46,22),(47,48),(35,49),(38,50),(1000000,51),(52,1000000),(53,1000000),(54,1000000),(55,1000000),(56,1000000),(57,22),(58,24),(59,1000000),(60,36),(61,39),(62,48),(63,49),(37,1000000),(64,1000000),(65,1000000),(66,1000000),(67,68),(69,70),(71,72),(73,39),(74,22),(75,48),(76,77),(78,50),(1000000,79),(80,1000000),(81,82),(1000000,83),(84,68),(73,85),(86,87),(88,89),(90,1000000),(91,1000000),(92,1000000),(1000000,93),(94,1000000),(95,1000000),(96,48),(97,49),(1000000,98),(99,1000000),(100,1000000),(66,1000000),(101,72),(1000000,102),(103,1000000),(104,1000000),(105,89),(106,1000000),(107,48),(108,1000000),(109,110),(111,1000000),(112,50),(1000000,113),(114,1000000),(115,1000000),(116,1000000),(1000000,117),(118,82),(1000000,119),(120,1000000),(121,122),(123,72),(1000000,124),(125,1000000),(126,122),(127,128),(129,110),(73,50),(118,77),(130,50),(1000000,131),(132,1000000),(133,1000000),(134,1000000),(135,1000000),(136,137),(138,139),(140,1000000),(141,1000000),(1000000,142),(143,1000000),(144,145),(146,1000000),(147,1000000),(1000000,148),(149,1000000),(150,128),(151,89),(152,48),(153,1000000),(1000000,154),(155,1000000),(156,1000000),(84,157),(136,158),(71,159),(160,1000000),(161,1000000),(92,1000000),(162,48),(163,1000000),(164,1000000),(165,1000000),(166,1000000),(127,167),(152,168),(169,1000000),(1000000,170),(171,172),(115,1000000),(173,139),(174,48),(129,170),(118,1000000),(175,50),(176,1000000),(177,178),(179,167),(180,1000000),(181,1000000),(182,1000000),(152,183),(1000000,184),(185,186),(187,50),(1000000,188),(189,1000000),(190,128),(191,1000000),(192,1000000),(193,194),(195,1000000),(196,1000000),(197,1000000),(198,199),(200,1000000),(201,1000000),(202,1000000),(1000000,203),(204,1000000),(205,48),(206,50),(207,1000000),(208,1000000),(209,1000000),(210,1000000),(1000000,211),(212,1000000),(213,1000000),(214,1000000),(215,1000000),(216,48),(217,50),(218,1000000),(219,1000000),(220,1000000),(221,222),(71,223),(73,172),(1000000,186),(224,1000000),(1000000,225),(177,226),(227,1000000),(228,1000000),(229,1000000),(230,1000000),(231,1000000),(136,232),(233,1000000),(234,1000000),(235,1000000),(236,1000000),(237,238),(239,178),(240,167),(1000000,241),(242,1000000),(243,1000000),(136,70),(244,245),(73,246),(247,89),(248,1000000),(249,1000000),(250,1000000),(251,1000000),(252,1000000),(253,1000000),(254,139),(255,1000000),(1000000,256),(71,257),(258,1000000),(259,1000000),(136,260),(261,262),(263,1000000),(264,1000000),(265,1000000),(1000000,266),(267,48),(268,1000000),(1000000,269),(177,1000000),(1000000,270),(271,1000000),(272,1000000),(129,273),(206,274),(275,1000000),(276,277),(278,128),(279,1000000),(1000000,280),(281,48),(282,1000000),(283,1000000),(284,1000000),(285,1000000),(1000000,286),(287,1000000),(288,1000000),(289,1000000),(290,262),(1000000,291),(292,172),(293,1000000),(294,1000000),(295,167),(296,1000000),(297,1000000),(298,1000000),(73,299),(300,1000000),(301,1000000),(302,1000000),(303,1000000),(92,1000000),(216,304),(305,1000000),(306,1000000),(185,1000000),(1000000,307),(278,308),(309,1000000),(136,310),(311,1000000),(312,1000000),(1000000,313),(314,1000000),(315,1000000),(316,1000000),(317,1000000),(318,319),(1000000,320),(227,321),(278,167),(295,319),(322,1000000),(323,1000000),(324,325),(1000000,246),(326,1000000),(1000000,327),(328,1000000),(329,1000000),(330,1000000),(331,1000000),(332,1000000),(333,1000000),(334,1000000),(335,167),(336,137),(337,1000000),(136,338),(1000000,339),(340,222),(123,223),(1000000,199),(341,1000000),(342,1000000),(343,1000000),(344,1000000),(1000000,85),(345,89),(346,1000000),(1000000,347),(348,1000000),(114,1000000),(1000000,349),(227,262),(350,167),(351,50),(352,1000000),(353,1000000),(267,321),(354,1000000),(355,1000000),(356,1000000),(357,1000000),(247,358),(359,1000000),(355,308),(360,1000000),(1000000,361),(129,291),(362,172),(363,1000000),(364,1000000),(365,1000000),(267,168),(366,1000000),(1000000,367),(136,368),(1000000,369),(281,304),(370,1000000),(355,167),(371,1000000),(372,1000000),(69,277),(373,1000000),(374,1000000),(375,167),(152,376),(377,167),(239,226),(378,1000000),(379,1000000),(380,1000000),(336,368),(381,1000000),(239,1000000),(382,167),(383,1000000),(267,199),(384,1000000),(267,1000000),(330,167),(385,1000000),(386,1000000),(1000000,387),(227,168),(1000000,388),(389,1000000),(390,368),(261,1000000),(391,1000000),(392,1000000),(227,260),(393,1000000),(394,1000000),(395,139),(1000000,396),(136,1000000),(397,48),(380,1000000),(398,186),(1000000,399),(400,1000000),(401,1000000),(290,1000000)]
def weights12 : List Nat := [174869380839,118795027379,90334589220,91738346276,50330501567,108032274256,62802134227,46908929321,60190351780,83175563068,46021830130,33658074888,41447424738,56098405089,52005243693,19976757785,61974995826,37495613949,55037500261,40251365777,49566850581,47111578877,19976757785,56172235913,6020983232,23889525030,33406093471,40710209959,44840777920,46970664605,18848908579,48136452752,39300324005,50319775670,23889525030,29252608826,37924024027,7199453513,20217304685,8351599818,39950014686,48685196371,33648291561,19976757785,56172235913,22540701016,37589674266,40978094057,6020983232,30924915552,8351599818,34982755042,45353124591,8608816574,24177201286,9986698138,47776059193,38245930946,34218682378,23889525030,29252608826,18604211187,38932283816,18080650317,36982709860,9986698138,41835584994,34261020169,19976757785,6995054203,3299256074,22197597103,6715346871,3590554657,37158670293,39717118145,14142403674,26779407070,20217304685,34982755042,22248061084,17536766291,29022162230,21621921086,24250624845,8351599818,35590571684,14440489757,37839136809,3133306759,23889525030,8364370177,3944469649,26545484167,8029860953,4292841181,38416835023,16572616630,16912070122,32024989147,24177201286,19890488479,20971476119,34707157981,25857018319,25867446310,9986698138,36541505386,17268558982,15157792177,30093813579,3746006574,20217304685,10001970538,4716097233,31745234674,9601922317,5132723785,16920327756,19818424622,20224385802,18331787282,19966529043,22197597103,23786353341,25079134367,21539462279,16866838123,14055042425,840538090,12299120238,18126399484,35988773525,4478750113,24177201286,11960419129,2339650521,3299256074,27167630995,10796119693,11481991130,6137161097,20234261341,23700170283,14591005421,9594664300,21922262290,23877292214,26545484167,28445518816,15936546596,22625096924,14149308464,16807592559,1004025284,14707639825,21676633682,18788083628,3015406521,6715346871,14302578412,2796852579,26468292911,12910162630,13730414010,7338393636,24197480157,11475612112,3299256074,11473311064,26216204147,20202675144,8351599818,23221415528,13036748776,11747838581,1199543844,11523148740,6064901904,14446838394,22467958879,3605006633,8029860953,2954318762,3343632333,5539322329,26113597341,7086801393,16419361039,8774978672,14882153537,13722785179,3944469649,6595691919,7124341357,31351440186,24159705440,9986698138,21836465303,5933429784,15589788865,14048347848,1433369541,13779635450,7251977002,11255168232,18517216977,4310124640,9601922317,3531950205,3997540368,6623422792,31228730089,8474093003,19635142279,10493027842,11775772864,8058637707,4716097233,7886762479,8518988026,21318070017,16174731663,6694423136,7094746080,18643035485,5276437594,1713007732,16478226220,8671630790,13459150642,22144022449,2813742961,11481991130,4222754571,4779565882,7919926550,17379520500,19966529043,4068288987,12005366057,12547687243,14081755178,9636337175,4948508305,4482278818,6596327363,22360328200,19342583721,8004837717,8483594248,22294492023,6309032162,2047434269,8909420966,10369431443,16094950163,4283815743,3363831971,13730414010,2709254839,3246004751,2468805648,9470448896,20783421842,23877292214,4864176002,8335348356,15004907516,16839539021,5916853022,5359277145,7887522444,25899560391,4613882894,9571996382,6845297587,3299256074,12606320835,7543938693,2447383605,4632827608,12399875119,19247170926,5121930026,4021697631,16419361039,3238871929,3880785028,2951312527,8855952988,24854235429,20202675144,5815997849,9967262581,6467948628,20137643987,7074921491,6408102108,5841141355,30972757740,5516665870,11446201931,8185272368,3299256074,9020795329,2925693347,14828135183,10410672361,6124252555,2468805648,19635142279,3872254690,4639935164,3528354970,10589867118,29722626608,24159705440,4962369325,1991936868,11918910975,6020983232,7662418985,6984375982,20587195497,16452730065,13687612781,9787782838,3944469649,10787006348,3497716324,17732154145,12449196206,7322955969,2951312527,12005366057,1330477424,5547822427,1878804413,12663499834,19370129776,2381012846,14252937723,7199453513,9162488951,21486256475,19675049201,16368173942,11704266523,12899263750,9729533354,6535519736,8756516359,3528354970,1589956400,6633588263,2245714807,15143410784,803714697,2846318862,8608816574,10956461388,15177104117,19573926308,13996238888,15425366964,7814801026,10470948274,1878804413,1900274013,2684512427,959987241,3402790352,13101919382,18149495165,11932156293,2587959405,6970786969,12521281705,2245714807,2271390865,1146877614,4192115926,21704254441,3093811580,2684512427,2715219098,1370384641,25955482932,3698773264,1330477424,1637682468,31039636954,1589956400,1957350847,26323788452,1900274013,25459119813,4332426150,5180064472,6193777047,7406102112]
def R12 : Nat := 1195924139
def C12 : Nat := 218

theorem check12 : check 12 succ12 = true := by decide +kernel
theorem wcheck12 : wcheck 1000000000 R12 succ12 weights12 = true := by decide +kernel
theorem wmin12 : weights12.all (fun v => Nat.ble 803714697 v) = true := by decide +kernel
theorem len12 : succ12.length = 402 ∧ weights12.length = 402 := by decide +kernel
theorem w0_12 : weights12.getD 0 0 ≤ C12 * 803714697 := by decide +kernel

/-- The width-12 certificate. -/
def cert12 : Cert := ⟨12, succ12, weights12, 1000000000, R12, C12, 803714697⟩

theorem cert12_valid : cert12.Valid where
  hM := by decide
  hcheck := check12
  hw := wcheck12
  hN := by rw [show cert12.succ.length = 402 from len12.1]; decide
  hlen := by show succ12.length ≤ weights12.length; rw [len12.1, len12.2]
  hmin := wmin12
  hmin0 := by decide
  hC := w0_12

/-- **The channel bound at width 12.** For every `n`, a set of at most `218 · 1.195924139 ^ n` words
contains the first `n` visible bits (column `1` at the even times) of every configuration whose
center column reads the clock `0, 1, 0, 1, …` from time `0`: about `0.258` bits of information
per visible bit, asymptotically. -/
theorem channel_bound_12 (n : Nat) :
    ∃ S : Finset (List Bool), (∀ x : Int → Bool, Clock x → visFrom x 0 n ∈ S) ∧
      S.card * 1000000000 ^ n ≤ 218 * 1195924139 ^ n :=
  cert12.bound cert12_valid n

/-- The eventual form at width 12: the clock from any even time `T` on. -/
theorem channel_bound_12_eventually (n : Nat) :
    ∃ S : Finset (List Bool),
      (∀ (x : Int → Bool) (T : Nat), T % 2 = 0 → (∀ t, T ≤ t → evol x t 0 = decide (t % 2 = 1)) →
        visFrom (fun q => evol x T q) 0 n ∈ S) ∧
      S.card * 1000000000 ^ n ≤ 218 * 1195924139 ^ n :=
  cert12.bound_eventually cert12_valid n

theorem channel_ncard_12 (n : Nat) :
    Set.ncard {w : List Bool | ∃ x : Int → Bool, Clock x ∧ visFrom x 0 n = w} * 1000000000 ^ n
      ≤ 218 * 1195924139 ^ n :=
  cert12.ncard_bound cert12_valid n

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
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
