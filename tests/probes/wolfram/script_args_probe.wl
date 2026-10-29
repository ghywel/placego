(* script_args_probe.wl (Local, L1121): what does `WolframKernel -script FILE A B` put in $CommandLine and
   $ScriptCommandLine? Stage B's driver read $ScriptCommandLine and got {} (receipts/local-gc2094-stageB.json).
   Prediction: $ScriptCommandLine is {} under the bare kernel; $CommandLine ends with FILE, A, B.
   No resource, LeanLink, notebook or external process. Caps: CPU 30, wall 60, RSS 1024, file 1, disk 1, launch 2048. *)
Print["ScriptCommandLine ", $ScriptCommandLine];
Print["CommandLine tail ", Take[$CommandLine, -3]];
Exit[0];
