(* L1184: structural checks for the five horizon notebook outputs, adapted from the arc's GC2115 checks.
   Loading this file performs no build or LeanLink call. The illustration and axiom boxes are parsed with HoldComplete
   applied BEFORE evaluation. The grid's data is evaluated only after every symbol in it is on a short whitelist,
   because its slopes are symbolic (GoldenRatio - 1, Sqrt[2] - 1, ...) and a held comparison cannot equate them.
   The KernelCheck object is read from InterpretationBox; the LeanEnvironment cell is retained for the manual read,
   never evaluated; the signatures are static prose. This is an artifact gate, not a replacement for the official
   Lean checker (L1183). *)

hzNotebookHeads = {"Rule30Submission.UniformHorizon.uniform_horizon",
 "Rule30Submission.UniformHorizon.uniform_horizon_witness", "Rule30Submission.RecodedHorizon.uniform_horizon_all",
 "Rule30Submission.RecodedHorizon.recoded_horizon", "Rule30Submission.PhysicalHorizon.piece_bound",
 "Rule30Submission.PhysicalHorizon.reset_step", "Rule30Submission.PhysicalHorizon.first_disagreement",
 "Rule30Submission.PhysicalHorizon.disagreement_step"};
hzNotebookStandardAxioms = {"Classical.choice", "Quot.sound", "propext"};
(* The official checker replayed 324 constants of the same source (L1183, GC2180). *)
hzNotebookDeclarations = 324;
(* The L1177 smoke values, which the notebook must reproduce exactly. *)
hzNotebookExpectedGrid = {{"slope", "C", "smallest witness index found", "proved horizon"},
 {GoldenRatio - 1, 0, 11, 1004}, {GoldenRatio - 1, 2, 29, 1506}, {Sqrt[2] - 1, 0, 11, 1004},
 {Sqrt[2] - 1, 2, 13, 1506}, {E - 2, 0, 15, 1004}, {E - 2, 2, 17, 1506}, {Pi - 3, 0, 3, 1004}, {Pi - 3, 2, 5, 1506}};
(* The only symbols the grid's data may contain before it is evaluated. *)
hzNotebookGridSymbols = {HoldComplete[List], HoldComplete[Plus], HoldComplete[Times], HoldComplete[Power],
 HoldComplete[Sqrt], HoldComplete[Rational], HoldComplete[GoldenRatio], HoldComplete[E], HoldComplete[Pi]};

hzNotebookHeld[BoxData[b_]] := Quiet[Check[ToExpression[b, StandardForm, HoldComplete], $Failed]];
hzNotebookHeld[_] := $Failed;

hzNotebookGridOK[h_] := Module[{data, syms},
  If[!MatchQ[h, HoldComplete[Grid[_List, ___]]], Return[False]];
  data = h /. HoldComplete[Grid[d_, ___]] :> HoldComplete[d];
  (* Level 2 down: with Heads -> True the wrapper's own head sits at level 1. HoldComplete is never whitelisted,
     since ReleaseHold would release an inner one. *)
  syms = Cases[data, s_Symbol :> HoldComplete[s], {2, Infinity}, Heads -> True];
  If[!SubsetQ[hzNotebookGridSymbols, syms], Return[False]];
  ReleaseHold[data] === hzNotebookExpectedGrid
];

hzNotebookAxiomsOK[h_] := Module[{pairs, a},
  If[!MatchQ[h, HoldComplete[Association[Repeated[Rule[_String, {___String}]]]]], Return[False]];
  (* Unwrap only after the literal string/list grammar matched; duplicate keys remain visible in this raw rule list. *)
  pairs = h /. HoldComplete[Association[r___]] :> (List @@@ {r});
  If[Length[pairs] =!= Length[hzNotebookHeads] || Sort[First /@ pairs] =!= Sort[hzNotebookHeads], Return[False]];
  If[!AllTrue[pairs, Complement[Last[#], hzNotebookStandardAxioms] === {} &], Return[False]];
  a = Association[Rule @@@ pairs];
  AllTrue[hzNotebookHeads, Sort[a[#]] === Sort[hzNotebookStandardAxioms] &]
];

hzNotebookKernelData[out_] := Module[{objects, a, m},
  objects = Cases[out,
    HoldPattern[InterpretationBox[_, s : Success["KernelChecked", _Association], ___]] :> HoldComplete[s], Infinity];
  If[Length[objects] =!= 1, Return[$Failed]];
  a = First[objects] /. HoldComplete[Success["KernelChecked", v_Association]] :> v;
  m = Lookup[a, "Module", None];
  (* A different count in the notebook is a retained discrepancy for review, never a reason to weaken this gate. *)
  If[!StringQ[m] || !StringStartsQ[m, "LeanLinkTmp"] || StringLength[m] <= StringLength["LeanLinkTmp"] ||
      Lookup[a, "Declarations", None] =!= hzNotebookDeclarations ||
      Lookup[a, "MessageParameters", None] =!= {hzNotebookDeclarations, m} ||
      Lookup[a, "MessageTemplate", None] =!= "The kernel accepts all `1` declarations of `2`.", Return[$Failed]];
  a
];

hzNotebookOutputChecks[outs_List] := Module[{gridOK = False, axiomsOK = False, kernel = $Failed},
  If[Length[outs] === 5,
    gridOK = TrueQ[hzNotebookGridOK[hzNotebookHeld[outs[[1]]]]];
    axiomsOK = TrueQ[hzNotebookAxiomsOK[hzNotebookHeld[outs[[4]]]]];
    kernel = hzNotebookKernelData[outs[[5]]];
  ];
  <|"grid_ok" -> TrueQ[gridOK], "axioms_ok" -> TrueQ[axiomsOK], "kernelcheck_ok" -> AssociationQ[kernel],
    "kernelcheck_data" -> If[AssociationQ[kernel], kernel, Null]|>
];
