(* ring_orbits_notebook_checks.wl (Local, L1134): structural checks for the six Lemma R notebook outputs, adapted from
   GPT's universal_start_notebook_checks.wl (GC2091). Loading this file performs no build or LeanLink call. The
   computation and axiom cells are parsed from their boxes with HoldComplete applied BEFORE evaluation; the KernelCheck
   object is read from its InterpretationBox. The LeanEnvironment and TypeForm cells are retained for the manual read,
   never evaluated. This is an artifact gate, not a replacement for the unchanged Lean checker. *)

rnHeads = {"orbit_eq_iff", "encode_walk", "decode_ring", "decode_encode", "encode_decode", "ring_fixed",
  "ring_period_two", "alternating_even"};
(* The axiom sets of the release check (receipts/local-gc2108-check.json), compared after sorting both sides. *)
rnAxioms = <|"orbit_eq_iff" -> {"propext", "Quot.sound"}, "encode_walk" -> {"propext", "Quot.sound"},
  "decode_ring" -> {"propext", "Quot.sound"}, "decode_encode" -> {"Quot.sound"},
  "encode_decode" -> {"propext", "Quot.sound"}, "ring_fixed" -> {"propext", "Quot.sound"},
  "ring_period_two" -> {"propext", "Classical.choice", "Quot.sound"}, "alternating_even" -> {"propext", "Quot.sound"}|>;
rnExpectedComputation = HoldComplete[Association[
  Rule["rings of size 1 to 12 with Phi^2 x = x", {1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3}],
  Rule["first return of the ring 0001", 8]]];
(* The release check replayed 59 constants in each form; the notebook's KernelCheck count is predicted to agree. *)
rnDeclarations = 59;

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
