(* usage: wolframscript -file read_nb_full.wl NAME OUTDIR [NOTEBOOK-FILE]
   Writes every Output cell of NAME/essay.nb (or NAME/NOTEBOOK-FILE) in full InputForm to OUTDIR/cell-NN.txt, the count
   to OUTDIR/count.txt and a sha256 per cell to OUTDIR/digests.txt; exits 1 if the notebook cannot be read. *)
name = $ScriptCommandLine[[2]]; outdir = $ScriptCommandLine[[3]];
nbfile = If[Length[$ScriptCommandLine] >= 4, $ScriptCommandLine[[4]], "essay.nb"];
path = FileNameJoin[{Directory[], name, nbfile}];
If[!FileExistsQ[path], Print["NO NOTEBOOK: ", path]; Exit[1]];
nb = Quiet[Get[path]];
If[Head[nb] =!= Notebook, Print["NOT A NOTEBOOK: head ", Head[nb]]; Exit[1]];
cells = Cases[nb, Cell[c_, "Output", ___] :> c, Infinity];
If[!DirectoryQ[outdir], CreateDirectory[outdir]];
Export[FileNameJoin[{outdir, "count.txt"}], ToString[Length[cells]], "Text"];
digests = Table[
  t = ToString[cells[[i]], InputForm];
  Export[FileNameJoin[{outdir, "cell-" <> IntegerString[i, 10, 2] <> ".txt"}], t, "Text"];
  IntegerString[Hash[t, "SHA256"], 16, 64], {i, Length[cells]}];
Export[FileNameJoin[{outdir, "digests.txt"}], StringRiffle[digests, "\n"], "Text"];
Print["output cells: ", Length[cells], "  written to ", outdir];
