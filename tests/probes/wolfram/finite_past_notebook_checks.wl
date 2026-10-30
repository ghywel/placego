(* finite_past_notebook_checks.wl (Local, L1231): structural checks for the eight finite-past notebook outputs, adapted
   from gate_clocks_notebook_checks.wl (L1221). Loading this file performs no build or LeanLink call. The
   computation and axiom cells are parsed from their boxes with HoldComplete applied BEFORE evaluation; the KernelCheck
   object is read from its InterpretationBox. The LeanEnvironment and TypeForm cells are retained for the manual read,
   never evaluated. This is an artifact gate, not a replacement for the unchanged Lean checker. *)

rnHeads = "Rule30Submission." <> # & /@ {"finite_root_age", "finite_parent_test", "normalized_ancestor_bijection",
  "finite_word_enumeration", "finite_parent_enumeration", "finite_parent_count", "finite_parent_small_widths"};
(* The axiom sets of the L1229 development stage's guard reports for the seven headlines, compared after sorting. *)
rnAxioms = <|"Rule30Submission.finite_root_age" -> {"propext", "Classical.choice", "Quot.sound"},
  "Rule30Submission.finite_parent_test" -> {"propext", "Classical.choice", "Quot.sound"},
  "Rule30Submission.normalized_ancestor_bijection" -> {"propext", "Classical.choice", "Quot.sound"},
  "Rule30Submission.finite_word_enumeration" -> {"propext", "Classical.choice", "Quot.sound"},
  "Rule30Submission.finite_parent_enumeration" -> {"propext", "Classical.choice", "Quot.sound"},
  "Rule30Submission.finite_parent_count" -> {"propext", "Quot.sound"},
  "Rule30Submission.finite_parent_small_widths" -> {"propext", "Quot.sound"}|>;
(* The illustration's values: GPT's VALIDATION-SPEC expectations, reproduced offline by Local (L1230). *)
rnExpectedComputation = HoldComplete[Association[
  Rule["rows at times 0 to 4", {"1", "111", "11001", "1101111", "110010001"}],
  Rule["centre bits", {1, 1, 0, 1, 1}],
  Rule["width, all words, finite-parent words, roots", {{1, 1, 0, 1}, {2, 1, 0, 1}, {3, 2, 1, 1}, {4, 4, 1, 3},
    {5, 8, 2, 6}, {6, 16, 4, 12}, {7, 32, 8, 24}, {8, 64, 16, 48}}],
  Rule["orientation agrees with A269160", True]]];
(* The official replay count (196 in both forms, L1230 probe); the notebook's KernelCheck count is predicted to agree. *)
rnDeclarations = 196;

rnHeld[BoxData[b_]] := Quiet[Check[ToExpression[b, StandardForm, HoldComplete], $Failed]];
rnHeld[_] := $Failed;

rnAxiomsOK[h_] := Module[{pairs},
  If[!MatchQ[h, HoldComplete[Association[Repeated[Rule[_String, {___String}]]]]], Return[False]];
  pairs = h /. HoldComplete[Association[r___]] :> (List @@@ {r});
  If[Length[pairs] =!= Length[rnHeads] || Sort[First /@ pairs] =!= Sort[rnHeads], Return[False]];
  AllTrue[pairs, Sort[Last[#]] === Sort[rnAxioms[First[#]]] &]
];

rnKernelData[out_] := Module[{objects, a, m},
  objects = Cases[out,
    HoldPattern[InterpretationBox[_, s : Success["KernelChecked", _Association], ___]] :> HoldComplete[s], Infinity];
  If[Length[objects] =!= 1, Return[$Failed]];
  a = First[objects] /. HoldComplete[Success["KernelChecked", v_Association]] :> v;
  m = Lookup[a, "Module", None];
  If[!StringQ[m] || !StringStartsQ[m, "LeanLinkTmp"] || StringLength[m] <= StringLength["LeanLinkTmp"] ||
      Lookup[a, "Declarations", None] =!= rnDeclarations || Lookup[a, "MessageParameters", None] =!= {rnDeclarations, m} ||
      Lookup[a, "MessageTemplate", None] =!= "The kernel accepts all `1` declarations of `2`.", Return[$Failed]];
  a
];

rnOutputChecks[outs_List] := Module[{computationOK = False, axiomsOK = False, kernel = $Failed},
  If[Length[outs] === 8,
    computationOK = rnHeld[outs[[3]]] === rnExpectedComputation;
    axiomsOK = TrueQ[rnAxiomsOK[rnHeld[outs[[7]]]]];
    kernel = rnKernelData[outs[[8]]];
  ];
  <|"computation_ok" -> TrueQ[computationOK], "axioms_ok" -> TrueQ[axiomsOK], "kernelcheck_ok" -> AssociationQ[kernel],
    "kernelcheck_data" -> If[AssociationQ[kernel], kernel, Null]|>
];
