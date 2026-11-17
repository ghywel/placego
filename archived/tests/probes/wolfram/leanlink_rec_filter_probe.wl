(* L1187: a small probe of LeanLink 1.2.2's internal-name filter, on a core-only module of two theorems, one with a
   name containing ".rec". The argument "default" or "internal" picks the import option; each mode runs in its own
   kernel, because KernelCheck resets LeanLink's elaboration state.
   Prediction: by default Probe.recoded is missing and Probe.plain present; with "IncludeInternal" -> True both are
   present, with standard (here empty) axioms; KernelCheck reports the same declaration count in both modes.
   Counterfactual: a missing name under "internal", or different counts, means the essay repair would not work. *)
mode = Last[$ScriptCommandLine];
Needs["Wolfram`LeanLink`"];
src = "namespace Probe\ntheorem plain : 1 + 1 = 2 := rfl\ntheorem recoded : 2 + 2 = 4 := rfl\nend Probe\n";
env = If[mode === "internal", LeanImportString[src, "IncludeInternal" -> True], LeanImportString[src]];
Print["PROBE ", mode, " head ", Head[env]];
Print["PROBE ", mode, " missing {plain, recoded} ", {MissingQ[env["Probe.plain"]], MissingQ[env["Probe.recoded"]]}];
Print["PROBE ", mode, " axioms of plain ", env["Probe.plain"]["Axioms"]];
If[!MissingQ[env["Probe.recoded"]], Print["PROBE ", mode, " axioms of recoded ", env["Probe.recoded"]["Axioms"]]];
k = env["Probe.plain"]["KernelCheck"];
Print["PROBE ", mode, " kernel ", If[MatchQ[k, Success["KernelChecked", _Association]], k[[2]]["Declarations"], k]];
