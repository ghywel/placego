(* gate_clocks_nested_notebook_checks_control.wl (Local, L1248): positive and adversarial fixtures for the nested
   gate-clock output gate, adapted from gate_clocks_notebook_checks_control.wl (L1221). No MarkdownToNotebook,
   LeanLink, resource lookup, external process or certificate evaluation. These fixtures test the artifact logic, not
   the theorem or the notebook. Prediction: all 18 true and GATE_OUTPUT_CONTROLS_PASS. Counterfactual: any false
   entry rejects the gate as it stands. *)
Get[FileNameJoin[{DirectoryName[$InputFileName], "gate_clocks_nested_notebook_checks.wl"}]];
rfSideEffect = 0;
rfComputation = ReleaseHold[rnExpectedComputation];
rfAxioms = rnAxioms;
rfKernel = <|"MessageTemplate" -> "The kernel accepts all `1` declarations of `2`.",
  "MessageParameters" -> {507, "LeanLinkTmp123x456"}, "Module" -> "LeanLinkTmp123x456", "Declarations" -> 507|>;
rfBoxes[a_] := BoxData[ToBoxes[a, StandardForm]];
rfKCell[a_] := BoxData[InterpretationBox["Success", Success["KernelChecked", a]]];
rfBait = BoxData[RowBox[{"rfSideEffect", "=", "1"}]];
rfOutputs = {rfBoxes[rfComputation], BoxData["True"], rfBait, rfBait, rfBoxes[rfAxioms], rfKCell[rfKernel]};
rfReplace[i_, c_] := ReplacePart[rfOutputs, i -> c];
rfPass[outs_, key_] := TrueQ[rnOutputChecks[outs][key]];

rfResults = <|
  "positive_computation" -> rfPass[rfOutputs, "computation_ok"],
  "positive_axioms" -> rfPass[rfOutputs, "axioms_ok"],
  "positive_kernel" -> rfPass[rfOutputs, "kernelcheck_ok"],
  "missing_output" -> !rfPass[Most[rfOutputs], "kernelcheck_ok"],
  "wrong_exponent" -> !rfPass[rfReplace[1, rfBoxes[ReplacePart[rfComputation,
    "E(2m), m = 0..10" -> {0, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13}]]], "computation_ok"],
  "wrong_pair" -> !rfPass[rfReplace[1, rfBoxes[ReplacePart[rfComputation,
    "pairs (first bit, last bit doubles)" -> {"11", "10", "11", "01", "01", "01", "01", "01", "01", "10"}]]],
    "computation_ok"],
  "wrong_key" -> !rfPass[rfReplace[1, rfBoxes[KeyMap[StringReplace[#, "m + 2" -> "m + 3"] &, rfComputation]]],
    "computation_ok"],
  "extra_computation_key" -> !rfPass[rfReplace[1, rfBoxes[Join[rfComputation, <|"extra" -> 1|>]]], "computation_ok"],
  "computation_code_is_held" -> !rfPass[rfReplace[1, rfBait], "computation_ok"],
  "missing_axiom_key" -> !rfPass[rfReplace[5, rfBoxes[KeyDrop[rfAxioms, "after11_order"]]], "axioms_ok"],
  "extra_axiom_key" -> !rfPass[rfReplace[5, rfBoxes[Join[rfAxioms, <|"extra" -> {"propext"}|>]]], "axioms_ok"],
  "wrong_axiom_set" -> !rfPass[rfReplace[5, rfBoxes[Join[rfAxioms, <|"no_three" -> {"propext", "Quot.sound"}|>]]],
    "axioms_ok"],
  "unknown_axiom" -> !rfPass[rfReplace[5,
    rfBoxes[Join[rfAxioms, <|"prefixExp_le_add_two" -> {"propext", "sorryAx"}|>]]], "axioms_ok"],
  "failure_containing_Success" -> !rfPass[rfReplace[6, BoxData[InterpretationBox["Success", Failure["Success", <||>]]]],
    "kernelcheck_ok"],
  "display_only_Success" -> !rfPass[rfReplace[6, BoxData["Success"]], "kernelcheck_ok"],
  "wrong_success_tag" -> !rfPass[rfReplace[6, BoxData[InterpretationBox["Success", Success["Other", rfKernel]]]],
    "kernelcheck_ok"],
  "wrong_declaration_count" -> !rfPass[rfReplace[6, rfKCell[Join[rfKernel, <|"Declarations" -> 506|>]]], "kernelcheck_ok"],
  "no_output_code_evaluated" -> (rfSideEffect === 0)
|>;
Print[ExportString[rfResults, "JSON"]];
If[Length[rfResults] === 18 && AllTrue[Values[rfResults], TrueQ],
  Print["GATE_OUTPUT_CONTROLS_PASS"]; Exit[0],
  Print["GATE_OUTPUT_CONTROLS_FAIL"]; Exit[1]];
