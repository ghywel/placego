# Bootstrap a Windows build of the patched libplacebo + ffmpeg.
#
#   powershell -ExecutionPolicy Bypass -File scripts\build-windows.ps1
#
# Installs MSYS2 if absent, brings its package database up to date, then hands
# off to build-windows.sh inside the MINGW64 environment, which does the
# actual work. Everything here is the part that has to happen on the Windows
# side; everything after is ordinary POSIX tooling.
#
# Safe to re-run. Each step checks whether it is already done.
#
#   -Stage <deps|placebo|ffmpeg|verify>   resume the build partway
#   -Force                                rebuild even where outputs exist
#   -SkipUpdate                           don't run pacman -Syu

param(
    [string]$Stage = "deps",
    [switch]$Force,
    [switch]$SkipUpdate
)

$ErrorActionPreference = "Stop"

function Say  { param($m) Write-Host "`n== $m" -ForegroundColor Cyan }
function Info { param($m) Write-Host "   $m" }
function Die  { param($m) Write-Host "`nFAILED: $m" -ForegroundColor Red; exit 1 }

$repo = Split-Path -Parent $PSScriptRoot
Say "repository"
Info $repo
if (-not (Test-Path "$repo\scripts\frame-mix-hook.patch")) {
    Die "frame-mix-hook.patch not found -- is this the right repository?"
}

# --- MSYS2 -----------------------------------------------------------------
Say "MSYS2"
$msys = "C:\msys64"
if (Test-Path "$msys\usr\bin\bash.exe") {
    Info "already installed at $msys"
} else {
    if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
        Die "winget not available and MSYS2 is not installed. Install MSYS2 by
   hand from https://www.msys2.org/ and re-run."
    }
    Info "installing via winget (this downloads a few hundred MB)"
    & winget install --id MSYS2.MSYS2 --accept-source-agreements --accept-package-agreements
    if (-not (Test-Path "$msys\usr\bin\bash.exe")) {
        Die "MSYS2 did not land at $msys. If it installed elsewhere, edit
   `$msys at the top of this script."
    }
    Info "installed"
}

# --- helper: run a command inside the MINGW64 environment ------------------
function Invoke-Mingw {
    param([string]$Command, [switch]$AllowFail)
    $env:MSYSTEM = "MINGW64"
    $env:CHERE_INVOKING = "1"
    # -l so the MSYS2 profile sets up the MINGW64 PATH and MSYSTEM handling
    & "$msys\usr\bin\bash.exe" -lc $Command
    if ($LASTEXITCODE -ne 0 -and -not $AllowFail) {
        Die "command failed inside MINGW64 (exit $LASTEXITCODE): $Command"
    }
    return $LASTEXITCODE
}

# --- package database ------------------------------------------------------
if (-not $SkipUpdate) {
    Say "package database"
    # A first -Syu can update pacman/msys2-runtime itself and then insist the
    # shell restarts. Running it twice from a fresh shell each time is the
    # documented way through that, and is harmless when already current.
    Info "pacman -Syu (pass 1)"
    Invoke-Mingw "pacman -Syu --noconfirm" -AllowFail | Out-Null
    Info "pacman -Syu (pass 2, after any runtime update)"
    Invoke-Mingw "pacman -Syu --noconfirm" -AllowFail | Out-Null
} else {
    Say "package database"; Info "skipped"
}

# --- hand off --------------------------------------------------------------
Say "handing off to build-windows.sh"
# Translate the Windows repo path into the MSYS2 view: C:\x\y -> /c/x/y
$drive  = $repo.Substring(0, 1).ToLower()
$rest   = $repo.Substring(2) -replace '\\', '/'
$posix  = "/$drive$rest"
$script = "$posix/scripts/build-windows.sh"
Info "script  $script"
Info "stage   $Stage"

$envPrefix = ""
if ($Force) { $envPrefix = "FORCE=1 " }
Invoke-Mingw "$envPrefix bash '$script' $Stage"

Say "finished"
Info "Binaries are under ~/np-build/ffmpeg inside MSYS2,"
Info "which is $msys\home\$env:USERNAME\np-build\ffmpeg from Windows."
