(* universal_start_notebook.wl (Local, L1116): stage B, the universal-start essay's notebook build.

   L1119: run through universal_start_notebook_run.wl, as `WolframKernel -script` under run_capped.py --track-tree (the
   attach watcher and the MCP kernel are retired). Evaluate with Get in a FRESH kernel, after defining
     usEssay    the essay copy to build (its sha256 is checked),
     usNotebook the notebook path to write (must not exist),
     usOut      an existing empty folder for the receipts,
     usKit      the pipeline kit copy (RULE30PRIZE_KIT).
   The supervisor samples the kernel and its observed owned descendants across process groups, retaining
   already observed children after reparenting. Processes born and orphaned within one sample may be missed.

   Builds the notebook with the Wolfram Institute's MarkdownToNotebook ("UseCache" -> False) under a 900 s
   TimeConstrained, recording every message through a handler. Then it checks the notebook itself:
     * the count of Output cells (predicted 6), the count of Message cells (predicted 0), and no $Failed in any output;
     * the illustration grid, rebuilt from its boxes, equals the retained corrected table row for row
       (receipts/illustration-mcp.md, evaluation 3);
     * all six exact axiom keys have complete standard-only lists, with the four main sets matching A2;
     * the KernelCheck InterpretationBox carries Success["KernelChecked", ...], with consistent module/count.
   GC2091 replaces the original substring/blacklist checks with universal_start_notebook_checks.wl.
   Its small non-building fixtures MUST pass before a full stage, under a separately accepted supervisor.
   It writes each Output cell's InputForm with a digest, the message packet, a message-name tally and summary.json to
   usOut, prints RESULT OK or RESULT FAIL <reasons>, and touches usOut/DONE last. *)

usReasons = {};
usNote[why_] := AppendTo[usReasons, why];
usChecksPath = FileNameJoin[{DirectoryName[$InputFileName], "universal_start_notebook_checks.wl"}];
usChecksLoad = Quiet[Check[Get[usChecksPath], $Failed]];
If[usChecksLoad === $Failed, usNote["output check source did not load"]];
If[FileHash[usEssay, "SHA256", "HexString"] =!= "326720821e32f10593df1b2fc68d3382fada08856a5ce0f536f5c7ee0c7dec0f",
  usNote["essay digest"]];
If[FileExistsQ[usNotebook], usNote["notebook path exists"]];
If[!DirectoryQ[usOut] || FileNames["*", usOut] =!= {}, usNote["receipt folder missing or not empty"]];

If[usReasons === {},
  SetEnvironment["RULE30PRIZE_KIT" -> usKit];
  If[$CloudBase === Automatic, $CloudBase = "https://www.wolframcloud.com/"];
  usURL = "https://www.wolframcloud.com/obj/wolframinstitute/DeployedResources/Function/MarkdownToNotebook";
  usRO = Quiet[ResourceObject[usURL]];
  usProvenance = Quiet[Check[#, "unknown"]] & /@ <|"Name" -> usRO["Name"], "Version" -> usRO["Version"],
    "UUID" -> usRO["UUID"], "ReleaseDate" -> ToString[usRO["ReleaseDate"]]|>;
  usMD2NB = ResourceFunction[usURL];
  usMessages = {};
  usHandler = Function[m, AppendTo[usMessages, m]];
  Internal`AddHandler["Message", usHandler];
  usTiming = AbsoluteTiming[usResult = TimeConstrained[usMD2NB[usEssay, usNotebook, "UseCache" -> False], 900, $TimedOut]];
  Internal`RemoveHandler["Message", usHandler];
  If[usResult === $TimedOut, usNote["build timed out"]];
  If[usResult === $Failed || !FreeQ[usResult, $Failed], usNote["build returned $Failed"]];
  If[!FileExistsQ[usNotebook], usNote["no notebook written"]];
];

If[FileExistsQ[usNotebook],
  usNB = Quiet[Get[usNotebook]];
  usOuts = Cases[usNB, Cell[c_, "Output", ___] :> c, Infinity];
  usMsgCells = Cases[usNB, Cell[_, "Message" | "MSG", ___], Infinity];
  If[Length[usOuts] =!= 6, usNote["output cells " <> ToString[Length[usOuts]]]];
  If[usMsgCells =!= {}, usNote["message cells " <> ToString[Length[usMsgCells]]]];
  If[!FreeQ[usOuts, $Failed], usNote["$Failed in an output"]];
  usStrings = ToString[#, InputForm] & /@ usOuts;
  usDigests = Table[
    Export[FileNameJoin[{usOut, "cell-" <> IntegerString[i, 10, 2] <> ".txt"}], usStrings[[i]], "Text"];
    Hash[usStrings[[i]], "SHA256", "HexString"], {i, Length[usStrings]}];
  usChecks = usNotebookOutputChecks[usOuts];
  usGridOK = TrueQ[usChecks["grid_ok"]];
  If[!usGridOK, usNote["illustration grid differs from the retained table"]];
  usAxiomsOK = TrueQ[usChecks["axioms_ok"]];
  If[!usAxiomsOK, usNote["axiom output missing or nonstandard"]];
  usKernelOK = TrueQ[usChecks["kernelcheck_ok"]];
  If[!usKernelOK, usNote["KernelCheck object/tag/module/count mismatch"]];
];

usNames = If[ValueQ[usMessages],
  Tally[Cases[usMessages, Hold[Message[n_, ___], _] :> ToString[Unevaluated[n], InputForm], {1}]], {}];
usPrinted = If[ValueQ[usMessages], Count[usMessages, Hold[_, True]], 0];
If[ValueQ[usMessages], Put[usMessages, FileNameJoin[{usOut, "messages.m"}]]];
Export[FileNameJoin[{usOut, "summary.json"}], <|
  "essay_sha256" -> FileHash[usEssay, "SHA256", "HexString"],
  "output_checks_sha256" -> If[FileExistsQ[usChecksPath], FileHash[usChecksPath, "SHA256", "HexString"], Null],
  "resource" -> If[ValueQ[usProvenance], usProvenance, Null],
  "build_seconds" -> If[ValueQ[usTiming], Round[First[usTiming], 0.1], Null],
  "notebook_sha256" -> If[FileExistsQ[usNotebook], FileHash[usNotebook, "SHA256", "HexString"], Null],
  "notebook_bytes" -> If[FileExistsQ[usNotebook], FileByteCount[usNotebook], Null],
  "output_cells" -> If[ValueQ[usOuts], Length[usOuts], Null],
  "output_digests" -> If[ValueQ[usDigests], usDigests, {}],
  "message_cells" -> If[ValueQ[usMsgCells], Length[usMsgCells], Null],
  "handler_events" -> If[ValueQ[usMessages], Length[usMessages], 0],
  "handler_events_printed" -> usPrinted,
  "handler_tally" -> (Rule @@@ SortBy[usNames, -Last[#] &]),
  "grid_ok" -> TrueQ[usGridOK], "axioms_ok" -> TrueQ[usAxiomsOK], "kernelcheck_ok" -> TrueQ[usKernelOK],
  "kernelcheck_data" -> If[ValueQ[usChecks], usChecks["kernelcheck_data"], Null],
  "kernel_pid" -> $ProcessID,
  "reasons" -> usReasons|>, "JSON"];
Print[If[usReasons === {}, "RESULT OK", "RESULT FAIL " <> StringRiffle[usReasons, "; "]]];
Export[FileNameJoin[{usOut, "DONE"}], "done", "Text"];
