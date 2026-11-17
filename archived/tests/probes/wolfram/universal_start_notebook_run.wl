(* universal_start_notebook_run.wl (Local, L1119): the -script driver for stage B.
   Run from the pipeline kit root under run_capped.py --track-tree:
     WolframKernel -script universal_start_notebook_run.wl ESSAY KIT
   It builds into CAPPED_OUT (the supervised, disk-capped folder): a copy of the essay at CAPPED_OUT/essay.md, the
   notebook at CAPPED_OUT/essay.nb and the receipts in a fresh CAPPED_OUT/nb-receipts, then loads universal_start_notebook.wl from this folder. The exit code
   is 0 only when the builder reports no reasons. Paths are passed in, never printed into published receipts. *)
(* L1121: under the bare `WolframKernel -script`, $ScriptCommandLine is {} (a wolframscript feature); the
   arguments are the last two entries of $CommandLine (receipts/local-l1121-script-args-probe.json). *)
{usEssaySource, usKit} = Take[$CommandLine, -2];
If[!FileExistsQ[usEssaySource] || !DirectoryQ[usKit], Print["RESULT FAIL driver arguments"]; Exit[1]];
usCapped = Environment["CAPPED_OUT"];
If[!StringQ[usCapped] || !DirectoryQ[usCapped], Print["RESULT FAIL no CAPPED_OUT"]; Exit[1]];
usTempRoot = FileNameSplit[ExpandFileName[FileNameJoin[{usCapped, "tmp"}]]];
usActualTemp = FileNameSplit[ExpandFileName[$TemporaryDirectory]];
If[Take[usActualTemp, UpTo[Length[usTempRoot]]] =!= usTempRoot,
  Print["RESULT FAIL kernel temporary directory outside supervised root"]; Exit[1]];
(* Build from a copy inside CAPPED_OUT, so that any side file the converter writes beside its input is disk-capped;
   the builder checks this copy's digest. *)
usEssay = FileNameJoin[{usCapped, "essay.md"}];
CopyFile[usEssaySource, usEssay];
usNotebook = FileNameJoin[{usCapped, "essay.nb"}];
usOut = FileNameJoin[{usCapped, "nb-receipts"}];
CreateDirectory[usOut];
Get[FileNameJoin[{DirectoryName[$InputFileName], "universal_start_notebook.wl"}]];
Exit[If[usReasons === {} && TrueQ[usGridOK] && TrueQ[usAxiomsOK] && TrueQ[usKernelOK] &&
  FileExistsQ[usNotebook] && FileExistsQ[FileNameJoin[{usOut, "summary.json"}]] &&
  FileExistsQ[FileNameJoin[{usOut, "messages.m"}]] && FileExistsQ[FileNameJoin[{usOut, "DONE"}]], 0, 1]];
