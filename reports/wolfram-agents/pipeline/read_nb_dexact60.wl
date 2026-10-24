nb = Get[FileNameJoin[{Directory[], "d-exact-60", "essay.nb"}]];
cells = Cases[nb, Cell[c_, "Output", ___] :> c, Infinity];
Print["output cells: ", Length[cells]];
Do[t = ToString[c, InputForm]; Print[i, ": ", StringTake[StringReplace[t, "\n" -> " "], UpTo[160]]], {i, Length[cells]}, {c, {cells[[i]]}}];
