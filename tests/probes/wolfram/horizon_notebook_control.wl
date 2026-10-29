(* L1184: 20 non-building output-gate controls, adapted from the arc's 18 (GC2110/GC2115), with two grid controls
   added for the whitelist: a wrong symbolic slope, and side-effect code inside a grid. Callable before the one build
   in the SAME fresh kernel. Bait code is held and its side effect must stay 0. No LeanLink/resource/build on loading. *)
hzNotebookControlResults[] := Module[{axes, kernel, bait, gridbait, outs, axcell, kcell, gcell, replace, pass, dup},
 hzFixtureSideEffect = 0;
 axes = AssociationMap[hzNotebookStandardAxioms &, hzNotebookHeads];
 kernel = <|"MessageTemplate" -> "The kernel accepts all `1` declarations of `2`.",
  "MessageParameters" -> {324, "LeanLinkTmp123x456"}, "Module" -> "LeanLinkTmp123x456", "Declarations" -> 324|>;
 axcell[a_] := BoxData[ToBoxes[a, StandardForm]];
 kcell[a_] := BoxData[InterpretationBox["Success", Success["KernelChecked", a]]];
 gcell[g_] := BoxData[ToBoxes[Grid[g, Frame -> All], StandardForm]];
 bait = BoxData[RowBox[{"hzFixtureSideEffect", "=", "1"}]];
 gridbait = BoxData[RowBox[{"Grid", "[", RowBox[{"{", RowBox[{"{", RowBox[{"hzFixtureSideEffect", "=", "1"}], "}"}],
   "}"}], "]"}]];
 outs = {gcell[hzNotebookExpectedGrid], BoxData["True"], bait, axcell[axes], kcell[kernel]};
 replace[i_, c_] := ReplacePart[outs, i -> c];
 pass[o_, key_] := TrueQ[hzNotebookOutputChecks[o][key]];
 dup = Replace[Prepend[(# -> hzNotebookStandardAxioms) & /@ hzNotebookHeads,
   First[hzNotebookHeads] -> hzNotebookStandardAxioms], {r___} :> HoldComplete[Association[r]]];
 <|
  "positive_grid" -> pass[outs, "grid_ok"],
  "positive_axioms" -> pass[outs, "axioms_ok"],
  "positive_kernel" -> pass[outs, "kernelcheck_ok"],
  "missing_output" -> !pass[Most[outs], "kernelcheck_ok"],
  "wrong_grid_value" -> !pass[replace[1, gcell[ReplacePart[hzNotebookExpectedGrid, {9, 3} -> 6]]], "grid_ok"],
  "wrong_grid_slope" -> !pass[replace[1, gcell[ReplacePart[hzNotebookExpectedGrid, {2, 1} -> GoldenRatio - 2]]], "grid_ok"],
  "wrong_grid_head" -> !pass[replace[1, bait], "grid_ok"],
  "grid_code_is_held" -> !pass[replace[1, gridbait], "grid_ok"],
  "unknown_axiom" -> !pass[replace[4, axcell[Join[axes, <|First[hzNotebookHeads] -> {"customAxiom"}|>]]], "axioms_ok"],
  "missing_axiom_key" -> !pass[replace[4, axcell[KeyDrop[axes, First[hzNotebookHeads]]]], "axioms_ok"],
  "extra_axiom_key" -> !pass[replace[4, axcell[Join[axes, <|"extra" -> {}|>]]], "axioms_ok"],
  "duplicate_axiom_key" -> (Length[dup /. HoldComplete[Association[r___]] :> {r}] === 9 && !hzNotebookAxiomsOK[dup]),
  "missing_standard_axiom" -> !pass[replace[4, axcell[Join[axes, <|First[hzNotebookHeads] -> {"propext"}|>]]], "axioms_ok"],
  "axiom_code_is_held" -> !pass[replace[4, bait], "axioms_ok"],
  "failure_containing_Success" -> !pass[replace[5, BoxData[InterpretationBox["Success", Failure["Success", <||>]]]],
    "kernelcheck_ok"],
  "display_only_Success" -> !pass[replace[5, BoxData["Success"]], "kernelcheck_ok"],
  "wrong_success_tag" -> !pass[replace[5, BoxData[InterpretationBox["Success", Success["Other", kernel]]]], "kernelcheck_ok"],
  "wrong_declaration_count" -> !pass[replace[5, kcell[Join[kernel, <|"Declarations" -> 323|>]]], "kernelcheck_ok"],
  "inconsistent_module" -> !pass[replace[5, kcell[Join[kernel, <|"Module" -> "LeanLinkTmp789x123"|>]]], "kernelcheck_ok"],
  "no_output_code_evaluated" -> (hzFixtureSideEffect === 0)
 |>
];
