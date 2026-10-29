(* universal_start_notebook_run.wl (Local, L1119): the -script driver for stage B.
   Run from the pipeline kit root under run_capped.py --track-tree:
     WolframKernel -script universal_start_notebook_run.wl ESSAY KIT
   It builds into CAPPED_OUT (the supervised, disk-capped folder): a copy of the essay at CAPPED_OUT/essay.md, the
   notebook at CAPPED_OUT/essay.nb and the receipts in a fresh CAPPED_OUT/nb-receipts, then loads universal_start_notebook.wl from this folder. The exit code
   is 0 only when the builder reports no reasons. Paths are passed in, never printed into published receipts. *)
{usEssaySource, usKit} = Take[$ScriptCommandLine, -2];
usCapped = Environment["CAPPED_OUT"];
If[!StringQ[usCapped] || !DirectoryQ[usCapped], Print["RESULT FAIL no CAPPED_OUT"]; Exit[1]];
(* Build from a copy inside CAPPED_OUT, so that any side file the converter writes beside its input is disk-capped;
   the builder checks this copy's digest. *)
usEssay = FileNameJoin[{usCapped, "essay.md"}];
CopyFile[usEssaySource, usEssay];
usNotebook = FileNameJoin[{usCapped, "essay.nb"}];
usOut = FileNameJoin[{usCapped, "nb-receipts"}];
CreateDirectory[usOut];
Get[FileNameJoin[{DirectoryName[$InputFileName], "universal_start_notebook.wl"}]];
Exit[If[usReasons === {}, 0, 1]];
