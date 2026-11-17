(* gate_clocks_nested_notebook_checks.wl (Local, L1248): structural checks for the six nested gate-clock notebook
   outputs, adapted from gate_clocks_notebook_checks.wl (L1221). Loading this file performs no build or LeanLink call.
   The computation and axiom cells are parsed from their boxes with HoldComplete applied BEFORE evaluation; the
   KernelCheck object is read from its InterpretationBox. The LeanEnvironment and TypeForm cells are retained for the
   manual read, never evaluated. This is an artifact gate, not a replacement for the unchanged Lean checker. *)

rnHeads = {"prefixExp_le_add_two", "first_excess_three", "no_three", "after01_double_iff", "after11_order"};
(* The axiom sets of the release check (receipts/local-l1248-official-check.json), compared after sorting both sides. *)
rnAxioms = AssociationMap[{"propext", "Classical.choice", "Quot.sound"} &, rnHeads];
(* The illustration's values, computed independently by tests/probes/gate_clock_beam2.py's plain bit-parallel
   simulator on the first twenty gates of the traced family (L1248). *)
rnExpectedComputation = HoldComplete[Association[
  Rule["E(2m), m = 0..10", {0, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12}],
  Rule["m + 2", {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}],
  Rule["pairs (first bit, last bit doubles)", {"11", "10", "11", "01", "01", "01", "01", "01", "01", "01"}]]];
(* The release check replayed 507 constants; with internal names included, the notebook's KernelCheck count is
   predicted to agree, as it did for Package A (347 and 347, L1222). *)
rnDeclarations = 507;

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
  If[Length[outs] === 6,
    computationOK = rnHeld[outs[[1]]] === rnExpectedComputation;
    axiomsOK = TrueQ[rnAxiomsOK[rnHeld[outs[[5]]]]];
    kernel = rnKernelData[outs[[6]]];
  ];
  <|"computation_ok" -> TrueQ[computationOK], "axioms_ok" -> TrueQ[axiomsOK], "kernelcheck_ok" -> AssociationQ[kernel],
    "kernelcheck_data" -> If[AssociationQ[kernel], kernel, Null]|>
];
