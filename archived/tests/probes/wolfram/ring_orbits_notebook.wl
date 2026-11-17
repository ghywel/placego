(* ring_orbits_notebook.wl (Local, L1134): the Lemma R essay's notebook build, adapted from universal_start_notebook.wl
   (the B2 builder, GC2091/GC2096). Run through ring_orbits_notebook_run.wl, as `WolframKernel -script` under
   run_capped.py --track-tree; the driver defines rnEssay, rnNotebook, rnOut (an existing empty folder) and rnKit.
   Builds the notebook with the Wolfram Institute's MarkdownToNotebook ("UseCache" -> False) under a 900 s
   TimeConstrained, recording every message through a handler. Then it checks the notebook itself: exactly 6 Output
   cells, 0 Message cells, no $Failed, and ring_orbits_notebook_checks.wl's structural gates (the computation
   Association, the eight exact axiom sets, and Success["KernelChecked", ...] with 59 declarations). It writes each
   output's InputForm with a digest, the raw message packet, and summary.json through GPT's notebook_receipt.wl
   (nrWriteReceipt, GC2107), whose Failure counts as a failure; DONE is written last. *)

rnReasons = {};
rnNote[why_] := AppendTo[rnReasons, why];
rnHere = DirectoryName[$InputFileName];
rnChecksPath = FileNameJoin[{rnHere, "ring_orbits_notebook_checks.wl"}];
rnReceiptPath = FileNameJoin[{rnHere, "notebook_receipt.wl"}];
If[Quiet[Check[Get[rnChecksPath], $Failed]] === $Failed, rnNote["output check source did not load"]];
If[Quiet[Check[Get[rnReceiptPath], $Failed]] === $Failed, rnNote["receipt helper did not load"]];
If[FileHash[rnEssay, "SHA256", "HexString"] =!= "0cefd19b86f2a8bcf700dfbdf50cad877bb78ce1d9c2696ed21f468dda5fdabe",
  rnNote["essay digest"]];
If[FileExistsQ[rnNotebook], rnNote["notebook path exists"]];
If[!DirectoryQ[rnOut] || FileNames["*", rnOut] =!= {}, rnNote["receipt folder missing or not empty"]];

If[rnReasons === {},
  SetEnvironment["RULE30PRIZE_KIT" -> rnKit];
  If[$CloudBase === Automatic, $CloudBase = "https://www.wolframcloud.com/"];
  rnURL = "https://www.wolframcloud.com/obj/wolframinstitute/DeployedResources/Function/MarkdownToNotebook";
  rnRO = Quiet[ResourceObject[rnURL]];
  rnProvenance = nrResourceMetadata[rnRO];
  rnMD2NB = ResourceFunction[rnURL];
  rnMessages = {};
  rnHandler = Function[m, AppendTo[rnMessages, m]];
  Internal`AddHandler["Message", rnHandler];
  rnTiming = AbsoluteTiming[rnResult = TimeConstrained[rnMD2NB[rnEssay, rnNotebook, "UseCache" -> False], 900, $TimedOut]];
  Internal`RemoveHandler["Message", rnHandler];
  If[rnResult === $TimedOut, rnNote["build timed out"]];
  If[rnResult === $Failed || !FreeQ[rnResult, $Failed], rnNote["build returned $Failed"]];
  If[!FileExistsQ[rnNotebook], rnNote["no notebook written"]];
];

If[FileExistsQ[rnNotebook],
  rnNB = Quiet[Get[rnNotebook]];
  rnOuts = Cases[rnNB, Cell[c_, "Output", ___] :> c, Infinity];
  rnMsgCells = Cases[rnNB, Cell[_, "Message" | "MSG", ___], Infinity];
  If[Length[rnOuts] =!= 6, rnNote["output cells " <> ToString[Length[rnOuts]]]];
  If[rnMsgCells =!= {}, rnNote["message cells " <> ToString[Length[rnMsgCells]]]];
  If[!FreeQ[rnOuts, $Failed], rnNote["$Failed in an output"]];
  rnStrings = ToString[#, InputForm] & /@ rnOuts;
  rnDigests = Table[
    Export[FileNameJoin[{rnOut, "cell-" <> IntegerString[i, 10, 2] <> ".txt"}], rnStrings[[i]], "Text"];
    Hash[rnStrings[[i]], "SHA256", "HexString"], {i, Length[rnStrings]}];
  rnChecks = rnOutputChecks[rnOuts];
  rnComputationOK = TrueQ[rnChecks["computation_ok"]];
  If[!rnComputationOK, rnNote["computation output differs from the expected Association"]];
  rnAxiomsOK = TrueQ[rnChecks["axioms_ok"]];
  If[!rnAxiomsOK, rnNote["axiom output missing, incomplete or nonstandard"]];
  rnKernelOK = TrueQ[rnChecks["kernelcheck_ok"]];
  If[!rnKernelOK, rnNote["KernelCheck object/tag/module/count mismatch"]];
];

rnNames = If[ValueQ[rnMessages],
  Tally[Cases[rnMessages, Hold[Message[n_, ___], _] :> ToString[Unevaluated[n], InputForm], {1}]], {}];
rnPrinted = If[ValueQ[rnMessages], Count[rnMessages, Hold[_, True]], 0];
If[ValueQ[rnMessages], Put[rnMessages, FileNameJoin[{rnOut, "messages.m"}]]];
rnSummary = <|
  "essay_sha256" -> FileHash[rnEssay, "SHA256", "HexString"],
  "output_checks_sha256" -> If[FileExistsQ[rnChecksPath], FileHash[rnChecksPath, "SHA256", "HexString"], Missing["NoFile"]],
  "receipt_helper_sha256" -> If[FileExistsQ[rnReceiptPath], FileHash[rnReceiptPath, "SHA256", "HexString"], Missing["NoFile"]],
  "resource" -> If[ValueQ[rnProvenance], rnProvenance, Missing["NotQueried"]],
  "build_seconds" -> If[ValueQ[rnTiming], Round[First[rnTiming], 0.1], Missing["NotBuilt"]],
  "notebook_sha256" -> If[FileExistsQ[rnNotebook], FileHash[rnNotebook, "SHA256", "HexString"], Missing["NoNotebook"]],
  "notebook_bytes" -> If[FileExistsQ[rnNotebook], FileByteCount[rnNotebook], Missing["NoNotebook"]],
  "output_cells" -> If[ValueQ[rnOuts], Length[rnOuts], Missing["NoNotebook"]],
  "output_digests" -> If[ValueQ[rnDigests], rnDigests, {}],
  "message_cells" -> If[ValueQ[rnMsgCells], Length[rnMsgCells], Missing["NoNotebook"]],
  "handler_events" -> If[ValueQ[rnMessages], Length[rnMessages], 0],
  "handler_events_printed" -> rnPrinted,
  "handler_tally" -> (Rule @@@ SortBy[rnNames, -Last[#] &]),
  "computation_ok" -> TrueQ[rnComputationOK], "axioms_ok" -> TrueQ[rnAxiomsOK], "kernelcheck_ok" -> TrueQ[rnKernelOK],
  "kernelcheck_data" -> If[ValueQ[rnChecks], rnChecks["kernelcheck_data"], Missing["NotChecked"]],
  "kernel_pid" -> $ProcessID,
  "reasons" -> rnReasons|>;
rnWrite = nrWriteReceipt[FileNameJoin[{rnOut, "summary.json"}], rnSummary];
If[FailureQ[rnWrite], rnNote["summary receipt: " <> ToString[rnWrite[[1]]]]];
Print[If[rnReasons === {}, "RESULT OK", "RESULT FAIL " <> StringRiffle[rnReasons, "; "]]];
Export[FileNameJoin[{rnOut, "DONE"}], "done", "Text"];
