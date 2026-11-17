"""ompflags.py: the C compiler's OpenMP flags, per platform (Local, 2026-10-05).

Apple's clang has no -fopenmp. It takes OpenMP through Homebrew's libomp (`brew install libomp`). Everywhere else
the flag is -fopenmp. Use: subprocess.run(["cc", "-O2", *OMP, "-o", exe, src]).
"""
import os, sys

OMP = ["-fopenmp"]
if sys.platform == "darwin":
    _lib = next((p for p in ("/opt/homebrew/opt/libomp", "/usr/local/opt/libomp") if os.path.isdir(p)), None)
    if _lib:
        OMP = ["-Xpreprocessor", "-fopenmp", f"-I{_lib}/include", f"-L{_lib}/lib", "-lomp"]
