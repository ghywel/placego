(* gate_clocks_notebook_run.wl (Local, L1221): the -script driver for the gate-clock notebook stage, adapted from
   ring_orbits_notebook_run.wl (L1134). Run from the pipeline kit root under run_capped.py --track-tree, through
   universal_start_notebook_launch.py (which binds TMPDIR inside CAPPED_OUT and execs the kernel):
     WolframKernel -script gate_clocks_notebook_run.wl ESSAY KIT
   It builds into CAPPED_OUT: a copy of the essay, the notebook, and a fresh nb-receipts folder. The exit code is 0
   only when the builder reports no reasons, every structural gate is true, and summary.json is a nonempty,
   round-tripped receipt with its required keys and an empty reasons list (nrReceiptFileOK, GC2107). *)
{rnEssaySource, rnKit} = Take[$CommandLine, -2];
If[!FileExistsQ[rnEssaySource] || !DirectoryQ[rnKit], Print["RESULT FAIL driver arguments"]; Exit[1]];
rnCapped = Environment["CAPPED_OUT"];
If[!StringQ[rnCapped] || !DirectoryQ[rnCapped], Print["RESULT FAIL no CAPPED_OUT"]; Exit[1]];
rnTempRoot = FileNameSplit[ExpandFileName[FileNameJoin[{rnCapped, "tmp"}]]];
rnActualTemp = FileNameSplit[ExpandFileName[$TemporaryDirectory]];
If[Take[rnActualTemp, UpTo[Length[rnTempRoot]]] =!= rnTempRoot,
  Print["RESULT FAIL kernel temporary directory outside supervised root"]; Exit[1]];
rnEssay = FileNameJoin[{rnCapped, "essay.md"}];
CopyFile[rnEssaySource, rnEssay];
rnNotebook = FileNameJoin[{rnCapped, "essay.nb"}];
rnOut = FileNameJoin[{rnCapped, "nb-receipts"}];
CreateDirectory[rnOut];
Get[FileNameJoin[{DirectoryName[$InputFileName], "gate_clocks_notebook.wl"}]];
rnSummaryPath = FileNameJoin[{rnOut, "summary.json"}];
rnRequired = {"essay_sha256", "notebook_sha256", "output_cells", "message_cells", "computation_ok", "axioms_ok",
  "kernelcheck_ok", "kernelcheck_data", "reasons"};
rnReceiptOK = nrReceiptFileOK[rnSummaryPath, rnRequired] &&
  With[{r = nrReadReceipt[rnSummaryPath]}, r["reasons"] === {} && r["output_cells"] === 6 && r["message_cells"] === 0 &&
    TrueQ[r["computation_ok"]] && TrueQ[r["axioms_ok"]] && TrueQ[r["kernelcheck_ok"]]];
If[!rnReceiptOK, Print["RESULT FAIL summary receipt missing, incomplete or not clean"]];
Exit[If[rnReasons === {} && rnReceiptOK && FileExistsQ[rnNotebook] && FileExistsQ[FileNameJoin[{rnOut, "messages.m"}]] &&
  FileExistsQ[FileNameJoin[{rnOut, "DONE"}]], 0, 1]];
