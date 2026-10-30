(* gate_clocks_notebook_checks_control.wl (Local, L1221): positive and adversarial fixtures for the gate-clock output
   gate, adapted from ring_orbits_notebook_checks_control.wl (L1134). No MarkdownToNotebook, LeanLink, resource lookup,
   external process or certificate evaluation. These fixtures test the artifact logic, not the theorem or the notebook.
   Prediction: all 18 true and GATE_OUTPUT_CONTROLS_PASS. Counterfactual: any false entry rejects the gate as it stands. *)
Get[FileNameJoin[{DirectoryName[$InputFileName], "gate_clocks_notebook_checks.wl"}]];
rfSideEffect = 0;
rfComputation = ReleaseHold[rnExpectedComputation];
rfAxioms = rnAxioms;
rfKernel = <|"MessageTemplate" -> "The kernel accepts all `1` declarations of `2`.",
  "MessageParameters" -> {347, "LeanLinkTmp123x456"}, "Module" -> "LeanLinkTmp123x456", "Declarations" -> 347|>;
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
    "OR (gate 14) from seed 1" -> {0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7}]]], "computation_ok"],
  "wrong_bound" -> !rfPass[rfReplace[1, rfBoxes[ReplacePart[rfComputation,
    "B(n), n = 0..12" -> {0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 9}]]], "computation_ok"],
  "wrong_key" -> !rfPass[rfReplace[1, rfBoxes[KeyMap[StringReplace[#, "seed 3" -> "seed 1"] &, rfComputation]]],
    "computation_ok"],
  "extra_computation_key" -> !rfPass[rfReplace[1, rfBoxes[Join[rfComputation, <|"extra" -> 1|>]]], "computation_ok"],
  "computation_code_is_held" -> !rfPass[rfReplace[1, rfBait], "computation_ok"],
  "missing_axiom_key" -> !rfPass[rfReplace[5, rfBoxes[KeyDrop[rfAxioms, "affine_prefix_bound"]]], "axioms_ok"],
  "extra_axiom_key" -> !rfPass[rfReplace[5, rfBoxes[Join[rfAxioms, <|"extra" -> {"propext"}|>]]], "axioms_ok"],
  "wrong_axiom_set" -> !rfPass[rfReplace[5, rfBoxes[Join[rfAxioms, <|"prefix_period_iff" -> {"propext", "Classical.choice", "Quot.sound"}|>]]],
    "axioms_ok"],
  "unknown_axiom" -> !rfPass[rfReplace[5, rfBoxes[Join[rfAxioms, <|"prefixExp_le_B" -> {"propext", "sorryAx"}|>]]],
    "axioms_ok"],
  "failure_containing_Success" -> !rfPass[rfReplace[6, BoxData[InterpretationBox["Success", Failure["Success", <||>]]]],
    "kernelcheck_ok"],
  "display_only_Success" -> !rfPass[rfReplace[6, BoxData["Success"]], "kernelcheck_ok"],
  "wrong_success_tag" -> !rfPass[rfReplace[6, BoxData[InterpretationBox["Success", Success["Other", rfKernel]]]],
    "kernelcheck_ok"],
  "wrong_declaration_count" -> !rfPass[rfReplace[6, rfKCell[Join[rfKernel, <|"Declarations" -> 346|>]]], "kernelcheck_ok"],
  "no_output_code_evaluated" -> (rfSideEffect === 0)
|>;
Print[ExportString[rfResults, "JSON"]];
If[Length[rfResults] === 18 && AllTrue[Values[rfResults], TrueQ],
  Print["GATE_OUTPUT_CONTROLS_PASS"]; Exit[0],
  Print["GATE_OUTPUT_CONTROLS_FAIL"]; Exit[1]];
