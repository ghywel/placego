(* synthesis_notebook.wl (Local, L1478): the release build of the synthesis essay, adapted from episode_bridge_notebook.wl
   (L1464). Run as `WolframKernel -script` through universal_start_notebook_launch.py, under run_capped.py --track-tree,
   from the kit at the verifier's commit 93d98bbe:  KERNEL synthesis_notebook.wl ESSAY KIT.
   MarkdownToNotebook ("UseCache" -> False) under a 900 s TimeConstrained, with every message recorded; then the notebook's
   own gates: 8 Output cells, no Message cells, no $Failed; the computation cell's white diagonals {2, 7, 28} and a table
   with no False; the Lean source in an icon; the kit cell True; a LeanEnvironment; the ten headlines' axiom sets as the
   portal Check printed them (farther_of_child none, the rest propext and Quot.sound); Success["KernelChecked", ...] with
   37 declarations, the count the official check replayed (L1476). Receipts through notebook_receipt.wl; DONE last; exit 0
   only when every gate holds. *)

{rnEssaySource, rnKit} = Take[$CommandLine, -2];
rnReasons = {};
rnNote[why_] := AppendTo[rnReasons, why];
rnCapped = Environment["CAPPED_OUT"];
If[!StringQ[rnCapped] || !DirectoryQ[rnCapped], Print["RESULT FAIL no CAPPED_OUT"]; Exit[1]];
If[Take[FileNameSplit[ExpandFileName[$TemporaryDirectory]], UpTo[Length[FileNameSplit[ExpandFileName[FileNameJoin[{rnCapped, "tmp"}]]]]]] =!=
    FileNameSplit[ExpandFileName[FileNameJoin[{rnCapped, "tmp"}]]], Print["RESULT FAIL temporary directory outside supervised root"]; Exit[1]];
rnHere = DirectoryName[$InputFileName];
If[Quiet[Check[Get[FileNameJoin[{rnHere, "notebook_receipt.wl"}]], $Failed]] === $Failed, rnNote["receipt helper did not load"]];
rnEssay = FileNameJoin[{rnCapped, "essay.md"}];
CopyFile[rnEssaySource, rnEssay];
If[FileHash[rnEssay, "SHA256", "HexString"] =!= "ac5b6350116a021cdd144217e0a51837614272f45a3ba28927043437fe4bbef1",
  rnNote["essay digest"]];
rnNotebook = FileNameJoin[{rnCapped, "essay.nb"}];
rnOut = FileNameJoin[{rnCapped, "nb-receipts"}];
CreateDirectory[rnOut];

rnHeads = {"closed_form", "farther_of_child", "solutions_agree", "coincidence_iff", "D_closed_form", "D_coincidence_iff",
   "white_of_coincidence", "evwhite_iff_eventually_eq", "D_white_of_coincidence", "D_evwhite_iff_eventually_eq"};
rnAxioms = Append[AssociationMap[{"Quot.sound", "propext"} &, rnHeads], "farther_of_child" -> {}];
rnDeclarations = 37;
rnHeld[BoxData[b_]] := Quiet[Check[ToExpression[b, StandardForm, HoldComplete], $Failed]];
rnHeld[_] := $Failed;

If[rnReasons === {},
  SetEnvironment["RULE30PRIZE_KIT" -> rnKit];
  If[$CloudBase === Automatic, $CloudBase = "https://www.wolframcloud.com/"];
  rnConnected = TrueQ[$CloudConnected];
  If[!rnConnected, rnNote["kernel not connected to the cloud"]];
  rnMD2NB = ResourceFunction["https://www.wolframcloud.com/obj/wolframinstitute/DeployedResources/Function/MarkdownToNotebook"];
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
  If[Length[rnOuts] =!= 8, rnNote["output cells " <> ToString[Length[rnOuts]]]];
  If[rnMsgCells =!= {}, rnNote["message cells " <> ToString[Length[rnMsgCells]]]];
  If[!FreeQ[rnOuts, $Failed], rnNote["$Failed in an output"]];
  rnIconOK = !FreeQ[Import[rnNotebook, "NB"], "IconizedObject"];
  If[!rnIconOK, rnNote["Lean source not in an icon"]];
  rnStrings = ToString[#, InputForm] & /@ rnOuts;
  rnDigests = Table[Export[FileNameJoin[{rnOut, "cell-" <> IntegerString[i, 10, 2] <> ".txt"}], rnStrings[[i]], "Text"];
    Hash[rnStrings[[i]], "SHA256", "HexString"], {i, Length[rnStrings]}];
  If[Length[rnOuts] === 8,
    rnWhiteOK = rnHeld[rnOuts[[1]]] === HoldComplete[{2, 7, 28}];
    If[!rnWhiteOK, rnNote["white diagonals differ"]];
    rnGrid = rnHeld[rnOuts[[2]]];
    rnGridOK = MatchQ[rnGrid, HoldComplete[_Grid]] && FreeQ[rnGrid, False] && Count[rnGrid, True, Infinity] === 8;
    If[!rnGridOK, rnNote["computation table differs"]];
    rnKitOK = rnHeld[rnOuts[[3]]] === HoldComplete[True];
    If[!rnKitOK, rnNote["kit directory cell is not True"]];
    rnEnvOK = !FreeQ[rnOuts[[4]], "LeanEnvironment"];
    If[!rnEnvOK, rnNote["no LeanEnvironment"]];
    rnAx = rnHeld[rnOuts[[7]]];
    rnAxiomsOK = MatchQ[rnAx, HoldComplete[_Association]] && With[{a = ReleaseHold[rnAx]},
      Sort[Keys[a]] === Sort[rnHeads] && AllTrue[rnHeads, Sort[ToString /@ a[#]] === Sort[rnAxioms[#]] &]];
    If[!rnAxiomsOK, rnNote["axiom sets differ"]];
    rnKC = Cases[rnOuts[[8]], HoldPattern[InterpretationBox[_, s : Success["KernelChecked", _Association], ___]] :> s, Infinity];
    rnKernelOK = Length[rnKC] === 1 && With[{a = First[rnKC][[2]]},
      a["Declarations"] === rnDeclarations && StringQ[a["Module"]] && StringStartsQ[a["Module"], "LeanLinkTmp"] &&
      a["MessageParameters"] === {rnDeclarations, a["Module"]} && a["MessageTemplate"] === "The kernel accepts all `1` declarations of `2`."];
    If[!rnKernelOK, rnNote["KernelCheck object, module or count differs"]];
  ];
];

rnSummary = <|
  "essay_sha256" -> FileHash[rnEssay, "SHA256", "HexString"],
  "driver_sha256" -> FileHash[$InputFileName, "SHA256", "HexString"],
  "build_seconds" -> If[ValueQ[rnTiming], Round[First[rnTiming], 0.1], Missing["NotBuilt"]],
  "notebook_sha256" -> If[FileExistsQ[rnNotebook], FileHash[rnNotebook, "SHA256", "HexString"], Missing["NoNotebook"]],
  "notebook_bytes" -> If[FileExistsQ[rnNotebook], FileByteCount[rnNotebook], Missing["NoNotebook"]],
  "output_cells" -> If[ValueQ[rnOuts], Length[rnOuts], Missing["NoNotebook"]],
  "output_digests" -> If[ValueQ[rnDigests], rnDigests, {}],
  "message_cells" -> If[ValueQ[rnMsgCells], Length[rnMsgCells], Missing["NoNotebook"]],
  "handler_events" -> If[ValueQ[rnMessages], Length[rnMessages], 0],
  "iconized" -> TrueQ[rnIconOK], "axioms_ok" -> TrueQ[rnAxiomsOK],
  "white_ok" -> TrueQ[rnWhiteOK], "table_ok" -> TrueQ[rnGridOK],
  "kernelcheck_ok" -> TrueQ[rnKernelOK], "environment_ok" -> TrueQ[rnEnvOK],
  "kernelcheck_declarations" -> If[ValueQ[rnKC] && rnKC =!= {}, First[rnKC][[2]]["Declarations"], Missing["NotChecked"]],
  "reasons" -> rnReasons|>;
rnWrite = nrWriteReceipt[FileNameJoin[{rnOut, "summary.json"}], rnSummary];
If[FailureQ[rnWrite], rnNote["summary receipt failed"]];
Print[If[rnReasons === {}, "RESULT OK", "RESULT FAIL " <> StringRiffle[rnReasons, "; "]]];
Export[FileNameJoin[{rnOut, "DONE"}], "done", "Text"];
Exit[If[rnReasons === {}, 0, 1]];
