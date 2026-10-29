(* kernel_group_probe.wl (Local, L1117). Caps: CPU 120 per process, wall 180, RSS 4096 MiB, file 16, disk 32,
   launch 5120, ongoing 1024, swap 256.
   Question: can a WolframKernel that run_capped.py starts directly (`WolframKernel -script`)
   get a licence here, and do its children, including whatever LeanLink starts, stay inside run_capped's process group?
   GC2091 asked for this to be demonstrated, not assumed, before a notebook stage relies on it.

   Run from the pipeline kit root under run_capped.py:
     WolframKernel -script kernel_group_probe.wl
   It prints the kernel's PID and process group, starts a 20 s `sleep` child and checks its group, then builds a
   trivial Lean declaration through LeanLink against the kit (one core import, no Mathlib, no certificate) and lists
   every descendant of the kernel with its process group while LeanLink is loaded. The last line is
   GROUP_PROBE_CONTAINED, or GROUP_PROBE_ESCAPED with the escaping processes.
   Prediction: the kernel starts (this session's MCP kernel is stopped, so a licence slot is free); every descendant
   shares the kernel's group; the LeanLink build succeeds.
   Counterfactual: a licence refusal means this route is unavailable now; a descendant in another group means it
   is not contained, and the attach watcher must be repaired instead. *)
psRows[] := Module[{t = RunProcess[{"/bin/ps", "-A", "-o", "pid=,ppid=,pgid=,comm="}, "StandardOutput"]},
  Select[StringSplit[StringTrim[#], Whitespace, 4] & /@ StringSplit[t, "\n"], Length[#] == 4 &]];
descendants[root_] := Module[{rows = psRows[], ids = {ToString[root]}, grown = True, new},
  While[grown,
    new = Complement[Select[rows, MemberQ[ids, #[[2]]] &][[All, 1]], ids];
    grown = new =!= {}; ids = Join[ids, new]];
  Select[rows, MemberQ[ids, #[[1]]] &]];
self = Select[psRows[], #[[1]] == ToString[$ProcessID] &];
Print["kernel pid ", $ProcessID, "  row ", self];
Print["version ", $VersionNumber, ".", $ReleaseNumber, "  licence ", $LicenseID];
group = If[self === {}, "?", self[[1, 3]]];
child = StartProcess[{"/bin/sleep", "20"}];
Pause[1];
lean = Quiet[Check[
  Needs["Wolfram`LeanLink`"];
  LeanImportString["import Ruliology.CellularAutomata.Rule30Prize\n\ntheorem groupProbe : True := trivial\n",
    "ProjectDir" -> Directory[]], $Failed]];
Print["leanlink head ", Head[lean]];
desc = descendants[$ProcessID];
Print["descendants (pid ppid pgid comm):"];
Scan[Print["  ", StringRiffle[#, " "]] &, desc];
escaped = Select[desc, #[[3]] =!= group &];
KillProcess[child];
Print[If[escaped === {} && group =!= "?", "GROUP_PROBE_CONTAINED", "GROUP_PROBE_ESCAPED " <> ToString[escaped]]];
Exit[0];
