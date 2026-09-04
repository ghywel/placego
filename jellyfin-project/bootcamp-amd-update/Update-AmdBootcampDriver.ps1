#Requires -Version 5.1
<#
.SYNOPSIS
Bind an official AMD Adrenalin display driver ONLY to the GPUs it supports, on a
machine that also has AMD GPUs it does not support (typically a Boot Camp Mac with
an eGPU). Unsupported GPUs keep their existing driver untouched.

.DESCRIPTION
Official AMD packages dropped Polaris/Vega (Radeon Pro 4xx/5xx, RX 4xx/5xx) years
ago, so Boot Camp Macs run community-modified packages. Those pair a modern kernel
driver with an OLD Vulkan user-mode driver so the Mac's own GPU keeps Vulkan - and
any newer card in the same machine (an RDNA eGPU, say) is then invisible to Vulkan
even though Direct3D works. Windows keeps a separate driver store per adapter, so
the fix is to give the newer card the current official driver while the old card
keeps the modified one. Both Vulkan ICDs then coexist, one per adapter.

What this script does, in order:
  1. Inventories AMD display adapters and parses the package INF to report which
     adapters it actually lists (only those will be rebound - Windows does the
     binding, this script never forces a driver onto a device).
  2. Exports every installed AMD driver package with pnputil, plus the display
     class registry, into a timestamped backup folder with a state.json.
  3. Optionally installs a boot-time WATCHDOG (-Watchdog) for machines whose only
     display hangs off the GPU being updated: if the screen has not come back
     within 10 minutes of a reboot, it restores the previous driver and reboots
     once. A healthy boot disarms it automatically in seconds.
  4. pnputil /add-driver /install of the package's display INF (and its OpenCL /
     settings support INFs).
  5. Verifies bindings and per-adapter Vulkan ICD registration; runs vulkaninfo
     if present.
  6. Optionally installs the Adrenalin UI (-InstallSoftware) via the package's
     own ccc2_install.exe /S. (Setup.exe itself refuses to run at all when it
     sees an unsupported GPU: "error 173". Do not bother with it.)

It never runs DDU, never factory-resets, never deletes an existing package.
-Rollback restores the previous binding from the saved state at any time.

No driver files are included: you supply an EXTRACTED official AMD package via
-PackagePath, and your older GPU must already be working on whatever driver it
has - this script leaves it alone and installs nothing for it.

.PARAMETER PackagePath
Folder of an EXTRACTED official AMD Adrenalin package: the one containing
Setup.exe and Packages\Drivers\Display\WT6A_INF. (Run the downloaded installer
and cancel at its first screen - it has already extracted to C:\AMD\... - or
unpack it with 7-Zip.)

.PARAMETER BackupRoot
Where backups and state go. A timestamped subfolder is created. Default
C:\AmdDriverBackup. Needs a few GB free.

.PARAMETER DryRun
Inventory, parse, and print the plan. Changes nothing. Works without elevation.

.PARAMETER Watchdog
Install and arm the boot-time rollback watchdog before installing the driver.
Strongly recommended when the GPU being updated drives your only display.

.PARAMETER InstallSoftware
After the driver, install the Adrenalin UI silently from the package.

.PARAMETER Rollback
Restore the previous driver binding from the newest state.json under BackupRoot
(or -StatePath). Reboot afterwards if it says so. Combine with -DryRun to see
what it would undo without doing it.

.PARAMETER Yes
Skip the confirmation prompt (unattended use).

.EXAMPLE
.\Update-AmdBootcampDriver.ps1 -PackagePath D:\amd-extracted -DryRun

.EXAMPLE
.\Update-AmdBootcampDriver.ps1 -PackagePath D:\amd-extracted -Watchdog -InstallSoftware

.EXAMPLE
.\Update-AmdBootcampDriver.ps1 -Rollback

.NOTES
Unsigned. Run from an elevated PowerShell as
  powershell -ExecutionPolicy Bypass -File .\Update-AmdBootcampDriver.ps1 ...
or let it re-launch itself elevated (it will ask via UAC). Read it first; it is
short and does nothing clever.
#>
[CmdletBinding()]
param(
  [string]$PackagePath,
  [string]$BackupRoot = 'C:\AmdDriverBackup',
  [switch]$DryRun,
  [switch]$Watchdog,
  [switch]$InstallSoftware,
  [switch]$Rollback,
  [string]$StatePath,
  [switch]$Yes
)

$ErrorActionPreference = 'Stop'
$script:WatchdogDir = 'C:\AmdDriverWatchdog'
$script:DisplayClassKey = 'HKLM:\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}'
$script:LogFile = $null

# ----------------------------------------------------------------- utilities
function Log {
  param([string]$Message, [string]$Level = 'INFO')
  $line = '{0} [{1}] {2}' -f (Get-Date -Format 'HH:mm:ss'), $Level, $Message
  switch ($Level) {
    'WARN' { Write-Host $line -ForegroundColor Yellow }
    'FAIL' { Write-Host $line -ForegroundColor Red }
    'OK'   { Write-Host $line -ForegroundColor Green }
    default { Write-Host $line }
  }
  if ($script:LogFile) { Add-Content -Path $script:LogFile -Value $line -Encoding UTF8 }
}

function Test-Admin {
  ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()
  ).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Invoke-SelfElevate {
  $argList = @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', ('"{0}"' -f $PSCommandPath))
  foreach ($kv in $PSBoundParameters.GetEnumerator()) {
    if ($kv.Value -is [switch]) { if ($kv.Value) { $argList += ('-' + $kv.Key) } }
    else { $argList += ('-' + $kv.Key); $argList += ('"{0}"' -f $kv.Value) }
  }
  Write-Host 'Not elevated - relaunching with a UAC prompt...'
  Start-Process powershell.exe -Verb RunAs -ArgumentList ($argList -join ' ')
  exit 0
}

# Parse `pnputil /enum-drivers` into objects.
function Get-DriverStorePackages {
  $out = pnputil /enum-drivers
  $pkgs = @(); $cur = $null
  foreach ($line in $out) {
    if ($line -match '^Published Name:\s*(\S+)') {
      if ($cur) { $pkgs += $cur }
      $cur = [pscustomobject]@{ Published = $Matches[1]; Original = ''; Provider = ''; Class = ''; Version = '' }
    } elseif ($cur) {
      if ($line -match '^Original Name:\s*(.+)$') { $cur.Original = $Matches[1].Trim() }
      elseif ($line -match '^Provider Name:\s*(.+)$') { $cur.Provider = $Matches[1].Trim() }
      elseif ($line -match '^Class Name:\s*(.+)$') { $cur.Class = $Matches[1].Trim() }
      elseif ($line -match '^Driver Version:\s*(.+)$') { $cur.Version = $Matches[1].Trim() }
    }
  }
  if ($cur) { $pkgs += $cur }
  $pkgs
}

function Get-PnpProp {
  param($InstanceId, $Key)
  try { (Get-PnpDeviceProperty -InstanceId $InstanceId -KeyName $Key -ErrorAction Stop).Data } catch { $null }
}

# Every AMD display adapter, with what it is bound to and whether it has a live display.
function Get-AmdAdapters {
  $controllers = @(Get-CimInstance Win32_VideoController -ErrorAction SilentlyContinue)
  Get-PnpDevice -Class Display -ErrorAction SilentlyContinue |
    Where-Object { $_.InstanceId -like 'PCI\VEN_1002*' } |
    ForEach-Object {
      $id = $_.InstanceId
      $ctl = $controllers | Where-Object { $_.PNPDeviceID -eq $id } | Select-Object -First 1
      $hres = 0; if ($ctl -and $ctl.CurrentHorizontalResolution) { $hres = [int]$ctl.CurrentHorizontalResolution }
      [pscustomobject]@{
        Name          = $_.FriendlyName
        InstanceId    = $id
        Status        = [string]$_.Status
        Problem       = [int]$_.Problem
        Inf           = [string](Get-PnpProp $id 'DEVPKEY_Device_DriverInfPath')
        Version       = [string](Get-PnpProp $id 'DEVPKEY_Device_DriverVersion')
        Provider      = [string](Get-PnpProp $id 'DEVPKEY_Device_DriverProvider')
        HardwareIds   = @(Get-PnpProp $id 'DEVPKEY_Device_HardwareIds')
        CompatibleIds = @(Get-PnpProp $id 'DEVPKEY_Device_CompatibleIds')
        DisplayWidth  = $hres
      }
    }
}

# Locate the display INF inside an extracted package and parse what it lists.
function Get-PackageInfo {
  param([string]$Root)
  if (-not (Test-Path $Root)) { throw "PackagePath not found: $Root" }
  $infs = Get-ChildItem -Path $Root -Recurse -Filter '*.inf' -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -match '^u\d+\.inf$' -and $_.FullName -match '\\Display\\' }
  if (-not $infs) { throw "No AMD display INF (u*.inf under Packages\Drivers\Display) found below $Root - is the package extracted?" }
  $inf = $infs | Sort-Object LastWriteTime -Descending | Select-Object -First 1
  $text = Get-Content -Path $inf.FullName -Raw
  $ver = ''; $date = ''
  if ($text -match '(?m)^\s*DriverVer\s*=\s*([^,\r\n]+),\s*([\d.]+)') { $date = $Matches[1].Trim(); $ver = $Matches[2] }

  # [Manufacturer]: "%X% = Prefix, dec1, dec2..." -> model sections "Prefix.decN".
  # Modern models live in the NTamd64.10.0* sections; a trailing build number in a
  # decoration is a MINIMUM build (10.0.1..19044 = Windows 10 19044 and later).
  $sections = @()
  if ($text -match '(?ms)^\[Manufacturer\]\s*(.*?)(?=^\[)') {
    foreach ($l in ($Matches[1] -split "`r?`n")) {
      if ($l -match '^\s*%[^%]+%\s*=\s*([^,\s]+)\s*,?\s*(.*)$') {
        $prefix = $Matches[1]
        foreach ($dec in ($Matches[2] -split ',')) {
          $d = $dec.Trim(); if ($d -match '^NTamd64\.10\.0') { $sections += ($prefix + '.' + $d) }
        }
      }
    }
  }
  $ids = New-Object 'System.Collections.Generic.HashSet[string]'
  $rx = 'PCI\\VEN_1002&DEV_[0-9A-Fa-f]{4}(?:&SUBSYS_[0-9A-Fa-f]{8})?(?:&REV_[0-9A-Fa-f]{2})?'
  foreach ($s in $sections) {
    $pat = '(?ms)^\[' + [regex]::Escape($s) + '\]\s*(.*?)(?=^\[|\z)'
    if ($text -match $pat) {
      foreach ($m in [regex]::Matches($Matches[1], $rx)) { [void]$ids.Add($m.Value.ToUpperInvariant()) }
    }
  }
  $scope = 'Windows 10/11 model sections'
  if ($ids.Count -eq 0) {
    foreach ($m in [regex]::Matches($text, $rx)) { [void]$ids.Add($m.Value.ToUpperInvariant()) }
    $scope = 'whole file (no NTamd64.10.0 sections found)'
  }
  $wt = $inf.Directory.FullName
  $support = @()
  foreach ($rel in @('amdocl\amdocl.inf', 'amdfdans\AMDFDANS.inf', 'amdafd\amdafd.inf')) {
    $p = Join-Path $wt $rel; if (Test-Path $p) { $support += $p }
  }
  $amdwin = Get-ChildItem (Join-Path $wt 'amdwin') -Filter 'amdwin-*.inf' -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($amdwin) { $support += $amdwin.FullName }
  $ccc2 = Get-ChildItem $wt -Directory -Filter 'B*' -ErrorAction SilentlyContinue |
    ForEach-Object { Get-ChildItem $_.FullName -Filter 'ccc2_install.exe' -ErrorAction SilentlyContinue } |
    Select-Object -First 1
  $ccc2Path = $null; if ($ccc2) { $ccc2Path = $ccc2.FullName }
  [pscustomobject]@{
    Inf = $inf.FullName; InfName = $inf.Name; Version = $ver; Date = $date
    ModelIds = $ids; IdScope = $scope; SupportInfs = $support; Ccc2 = $ccc2Path
  }
}

function Test-Coverage {
  param($Adapter, $Package)
  $best = $null
  foreach ($cid in (@($Adapter.HardwareIds) + @($Adapter.CompatibleIds))) {
    if ($cid -and $Package.ModelIds.Contains(([string]$cid).ToUpperInvariant())) { $best = $cid; break }
  }
  $best
}

function Show-Adapters {
  param($Adapters, $Package)
  foreach ($a in $Adapters) {
    $disp = 'no active display'
    if ($a.DisplayWidth -gt 0) { $disp = "drives a display ($($a.DisplayWidth) px wide)" }
    Log ("  {0}" -f $a.Name)
    Log ("     {0}" -f $a.InstanceId)
    Log ("     bound: {0} {1} ({2}), status {3}, {4}" -f $a.Inf, $a.Version, $a.Provider, $a.Status, $disp)
    if ($Package) {
      $m = Test-Coverage $a $Package
      if ($m) { Log ("     LISTED in package as {0}" -f $m) }
      else { Log '     NOT listed in package - will keep its current driver' }
    }
  }
}

function Get-VulkanRegistrations {
  Get-ChildItem $script:DisplayClassKey -ErrorAction SilentlyContinue | ForEach-Object {
    try {
      $v = Get-ItemProperty $_.PSPath -ErrorAction Stop
      if ($v.MatchingDeviceId -and $v.MatchingDeviceId -match 'VEN_1002') {
        $icd = [string]$v.VulkanDriverName
        $exists = $false; if ($icd) { $exists = Test-Path $icd }
        [pscustomobject]@{ Key = $_.PSChildName; Desc = $v.DriverDesc; Version = $v.DriverVersion; Icd = $icd; IcdExists = $exists }
      }
    } catch { }
  }
}

function Show-VulkanRegistrations {
  Log 'Vulkan ICD registrations (per adapter, from the display class registry):'
  foreach ($r in (Get-VulkanRegistrations)) {
    $icd = '(none)'; if ($r.Icd) { $icd = $r.Icd }
    $miss = ''; if ($r.Icd -and -not $r.IcdExists) { $miss = '  [MISSING FILE]' }
    Log ("  {0}: {1} {2} -> {3}{4}" -f $r.Key, $r.Desc, $r.Version, $icd, $miss)
  }
}

# ---------------------------------------------------- rollback script (shared)
# Written to disk for the watchdog; also used by -Rollback. Reads state.json.
$RollbackScript = @'
param([string]$StatePath = 'C:\AmdDriverWatchdog\state.json', [switch]$DryRun)
$ErrorActionPreference = 'Continue'
$tag = ''; if ($DryRun) { $tag = '(dry run) ' }
"rollback start $(Get-Date)   state: $StatePath   $tag"
$state = Get-Content $StatePath -Raw | ConvertFrom-Json
foreach ($pn in @($state.AddedPackages)) {
  if (-not $pn) { continue }
  if ($DryRun) { "${tag}would delete added package $pn (pnputil /delete-driver $pn /uninstall /force)" }
  else { "deleting added package $pn"; pnputil /delete-driver $pn /uninstall /force }
}
if (-not $DryRun) { pnputil /scan-devices; Start-Sleep -Seconds 10 }
$needReboot = $false
foreach ($d in @($state.Devices)) {
  if (-not $d.Covered) { continue }
  $cur = $null
  try { $cur = (Get-PnpDeviceProperty -InstanceId $d.InstanceId -KeyName 'DEVPKEY_Device_DriverInfPath' -ErrorAction Stop).Data } catch { }
  "$($d.Name): bound to '$cur', previous was '$($d.PreviousInf)'"
  if ($cur -ne $d.PreviousInf -and $d.PreviousInf) {
    $inf = Join-Path $env:WINDIR ('INF\' + $d.PreviousInf)
    if (-not (Test-Path $inf)) { "  previous INF $inf missing from C:\Windows\INF - re-add it from the backup folder with pnputil /add-driver"; continue }
    if ($DryRun) { "  ${tag}would force-bind $inf to $($d.HardwareId) if still not bound after the package removal"; continue }
    "  force-binding $($d.PreviousInf) via UpdateDriverForPlugAndPlayDevices"
    if (-not ('DrvUp' -as [type])) {
      Add-Type -TypeDefinition @"
using System; using System.Runtime.InteropServices;
public static class DrvUp {
  [DllImport("newdev.dll", SetLastError=true, CharSet=CharSet.Unicode)]
  public static extern bool UpdateDriverForPlugAndPlayDevices(IntPtr hwndParent, string HardwareId, string FullInfPath, uint InstallFlags, out bool bRebootRequired);
}
"@
    }
    $rb = $false
    $ok = [DrvUp]::UpdateDriverForPlugAndPlayDevices([IntPtr]::Zero, [string]$d.HardwareId, $inf, 1, [ref]$rb)
    "  result: $ok  rebootRequired: $rb  lastError: $([Runtime.InteropServices.Marshal]::GetLastWin32Error())"
    if ($rb) { $needReboot = $true }
  }
}
"rollback end $(Get-Date)  rebootRequired=$needReboot"
'@

$WatchdogScript = @'
$dir = 'C:\AmdDriverWatchdog'; $flags = "$dir\flags"
$log = "$dir\watchdog-$(Get-Date -Format yyyyMMdd-HHmmss).log"
function L($m) { "$(Get-Date -Format s) $m" | Add-Content $log }
if (-not (Test-Path "$flags\armed.flag")) { exit 0 }
L 'armed - watchdog active'
if (Test-Path "$flags\rolledback.flag") { L 'rolledback.flag present; refusing to act twice'; exit 0 }
$state = Get-Content "$dir\state.json" -Raw | ConvertFrom-Json
function Test-Healthy {
  try {
    $ctl = @(Get-CimInstance Win32_VideoController -ErrorAction Stop)
    foreach ($d in @($state.Devices)) {
      if (-not $d.Covered) { continue }
      $p = Get-PnpDevice -InstanceId $d.InstanceId -ErrorAction Stop
      if ($p.Status -ne 'OK') { return $false }
      $prov = (Get-PnpDeviceProperty -InstanceId $d.InstanceId -KeyName 'DEVPKEY_Device_DriverProvider' -ErrorAction Stop).Data
      if ($prov -notmatch 'Advanced Micro|AMD') { return $false }
      if ($d.DrivesDisplay) {
        $c = $ctl | Where-Object { $_.PNPDeviceID -eq $d.InstanceId } | Select-Object -First 1
        if (-not $c -or -not $c.CurrentHorizontalResolution -or $c.CurrentHorizontalResolution -lt 640) { return $false }
      }
    }
    return $true
  } catch { return $false }
}
$deadline = (Get-Date).AddMinutes(10)
while ((Get-Date) -lt $deadline) {
  if (Test-Path "$flags\display-ok.flag") { L 'manual display-ok; disarming'; Remove-Item "$flags\armed.flag" -Force; exit 0 }
  if (Test-Healthy) { L 'auto display-ok: updated adapters healthy and lit; disarming'; Remove-Item "$flags\armed.flag" -Force; exit 0 }
  Start-Sleep -Seconds 10
}
L 'TIMEOUT - assuming a blind machine; rolling back to the previous driver'
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$dir\rollback.ps1" -StatePath "$dir\state.json" >> $log 2>&1
New-Item "$flags\rolledback.flag" -ItemType File -Force | Out-Null
Remove-Item "$flags\armed.flag" -Force
L 'rollback complete; rebooting once'
Restart-Computer -Force
'@

function Install-Watchdog {
  param($State)
  $dir = $script:WatchdogDir
  New-Item -ItemType Directory -Force -Path $dir, "$dir\flags" | Out-Null
  Set-Content -Path "$dir\rollback.ps1" -Value $RollbackScript -Encoding UTF8
  Set-Content -Path "$dir\watchdog.ps1" -Value $WatchdogScript -Encoding UTF8
  $State | ConvertTo-Json -Depth 6 | Set-Content -Path "$dir\state.json" -Encoding UTF8
  icacls "$dir\flags" /grant '*S-1-1-0:(OI)(CI)M' | Out-Null   # anyone may disarm
  $ok = "@echo ok> $dir\flags\display-ok.flag`r`n@echo Display confirmed - AMD driver watchdog disarmed for this boot.`r`n@timeout /t 3 >nul`r`n"
  Set-Content -Path "$dir\DISPLAY-OK.cmd" -Value $ok -Encoding ASCII
  Set-Content -Path 'C:\Users\Public\Desktop\DISPLAY-OK.cmd' -Value $ok -Encoding ASCII
  $principal = New-ScheduledTaskPrincipal -UserId 'SYSTEM' -LogonType ServiceAccount -RunLevel Highest
  $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit ([TimeSpan]::Zero)
  $action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File $dir\watchdog.ps1"
  $trigger = New-ScheduledTaskTrigger -AtStartup; $trigger.Delay = 'PT90S'
  Register-ScheduledTask -TaskName 'AmdDriverWatchdog' -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Force | Out-Null
  Set-Content -Path "$dir\flags\armed.flag" -Value "armed $(Get-Date -Format s)" -Encoding ASCII
  Log "Watchdog installed and ARMED (task AmdDriverWatchdog, files in $dir). Disarm: run DISPLAY-OK.cmd on the desktop, or delete $dir\flags\armed.flag." 'OK'
}

function Invoke-Pnputil {
  param([string[]]$Arguments)
  Log ("  pnputil {0}" -f ($Arguments -join ' '))
  $out = & pnputil @Arguments
  $code = $LASTEXITCODE
  foreach ($l in $out) { if ($l -and "$l".Trim()) { Log ("    {0}" -f "$l".TrimEnd()) } }
  $added = @(); foreach ($l in $out) { if ("$l" -match 'Published Name:\s*(oem\d+\.inf)') { $added += $Matches[1] } }
  [pscustomobject]@{ ExitCode = $code; Added = $added; Output = $out }
}

# ===================================================================== main
if ($Rollback) {
  if (-not $DryRun -and -not (Test-Admin)) { Invoke-SelfElevate }
  if (-not $StatePath) {
    $cands = @()
    if (Test-Path "$script:WatchdogDir\state.json") { $cands += Get-Item "$script:WatchdogDir\state.json" }
    $cands += Get-ChildItem -Path $BackupRoot -Recurse -Filter 'state.json' -ErrorAction SilentlyContinue
    $newest = $cands | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if ($newest) { $StatePath = $newest.FullName }
  }
  if (-not $StatePath -or -not (Test-Path $StatePath)) { throw 'No state.json found - pass -StatePath.' }
  Log "Rolling back using $StatePath"
  $tmp = Join-Path $env:TEMP 'amd-rollback.ps1'
  Set-Content -Path $tmp -Value $RollbackScript -Encoding UTF8
  $rbArgs = @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $tmp, '-StatePath', $StatePath)
  if ($DryRun) { $rbArgs += '-DryRun' }
  & powershell.exe @rbArgs
  if ($DryRun) { Log 'Rollback dry run complete. Nothing was changed.' 'OK'; exit 0 }
  Log 'Rollback finished. Reboot if it reported rebootRequired=True.' 'OK'
  if (Test-Path "$script:WatchdogDir\flags\armed.flag") { Remove-Item "$script:WatchdogDir\flags\armed.flag" -Force; Log 'Watchdog disarmed.' }
  exit 0
}

if (-not $PackagePath) { throw 'Specify -PackagePath (an extracted AMD package folder), or -Rollback.' }
if (-not $DryRun -and -not (Test-Admin)) { Invoke-SelfElevate }

$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$backupDir = Join-Path $BackupRoot $stamp
if (-not $DryRun) {
  New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
  $script:LogFile = Join-Path $backupDir 'update.log'
}

$mode = 'INSTALL'; if ($DryRun) { $mode = 'DRY RUN (no changes)' }
Log '=== AMD mixed-generation driver update ==='
Log ("Mode: {0}   Elevated: {1}" -f $mode, (Test-Admin))

# --- package
$pkg = Get-PackageInfo -Root $PackagePath
Log ("Package INF: {0}   version {1} ({2})" -f $pkg.Inf, $pkg.Version, $pkg.Date)
Log ("  {0} device IDs parsed from {1}" -f $pkg.ModelIds.Count, $pkg.IdScope)
$supportNames = 'none found'
if ($pkg.SupportInfs) { $supportNames = ($pkg.SupportInfs | ForEach-Object { Split-Path $_ -Leaf }) -join ', ' }
Log ("  support INFs: {0}" -f $supportNames)
$ccc2Note = 'not found'; if ($pkg.Ccc2) { $ccc2Note = $pkg.Ccc2 }
Log ("  Adrenalin UI installer: {0}" -f $ccc2Note)

# --- adapters
$adapters = @(Get-AmdAdapters)
if (-not $adapters) { throw 'No AMD display adapters (PCI\VEN_1002) found.' }
Log 'AMD display adapters:'
Show-Adapters $adapters $pkg
$targets = @($adapters | Where-Object { Test-Coverage $_ $pkg })
$others  = @($adapters | Where-Object { -not (Test-Coverage $_ $pkg) })
if (-not $targets) { Log 'The package lists none of these adapters - nothing to do.' 'WARN'; exit 2 }
$displayTargets = @($targets | Where-Object { $_.DisplayWidth -gt 0 })

Log 'Plan:'
foreach ($t in $targets) {
  $note = ''; if ($t.Version -eq $pkg.Version) { $note = ' (already on this version - Windows will report up-to-date)' }
  Log ("  UPDATE  {0}: {1} {2} -> {3}{4}" -f $t.Name, $t.Inf, $t.Version, $pkg.Version, $note)
}
foreach ($o in $others) { Log ("  KEEP    {0}: stays on {1} {2} (not listed in this package)" -f $o.Name, $o.Inf, $o.Version) }
if ($displayTargets) {
  Log ("  The display you are looking at is driven by an adapter being updated ({0}). Expect it to blank for a few seconds." -f (($displayTargets | ForEach-Object { $_.Name }) -join ', ')) 'WARN'
  if (-not $Watchdog -and -not $DryRun) { Log '  No -Watchdog: if the screen does not come back after a reboot there is no automatic recovery. Consider re-running with -Watchdog.' 'WARN' }
}
Show-VulkanRegistrations

if ($DryRun) { Log 'Dry run complete. Nothing was changed.' 'OK'; exit 0 }

if (-not $Yes) {
  $ans = Read-Host 'Proceed with the plan above? [y/N]'
  if ($ans -notmatch '^[Yy]') { Log 'Aborted by user.'; exit 1 }
}

# --- backups
Log "Backing up to $backupDir ..."
$pkgs = Get-DriverStorePackages
$amdPkgs = @($pkgs | Where-Object { $_.Provider -match 'Advanced Micro|^AMD' })
foreach ($p in $amdPkgs) {
  $dst = Join-Path $backupDir ('drivers\' + ($p.Published -replace '\.inf$', ''))
  New-Item -ItemType Directory -Force -Path $dst | Out-Null
  $r = Invoke-Pnputil @('/export-driver', $p.Published, $dst)
  if ($r.ExitCode -ne 0) { Log ("  export of {0} returned {1}" -f $p.Published, $r.ExitCode) 'WARN' }
}
& reg export 'HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}' (Join-Path $backupDir 'display-class.reg') /y | Out-Null
$adapters | Format-List | Out-String | Set-Content (Join-Path $backupDir 'adapters-before.txt') -Encoding UTF8
try { Checkpoint-Computer -Description "pre-AMD-$($pkg.Version)" -RestorePointType MODIFY_SETTINGS -ErrorAction Stop; Log '  System Restore point requested (Windows may decline if one was made in the last 24h).' }
catch { Log ("  System Restore point not created ({0}) - the pnputil exports are the real backup." -f $_.Exception.Message.Split("`n")[0]) 'WARN' }

$state = [pscustomobject]@{
  Timestamp = $stamp; PackagePath = $PackagePath; Inf = $pkg.Inf; Version = $pkg.Version; BackupDir = $backupDir
  AddedPackages = @()
  Devices = @($adapters | ForEach-Object {
    [pscustomobject]@{
      Name = $_.Name; InstanceId = $_.InstanceId; HardwareId = [string]$_.HardwareIds[0]
      PreviousInf = $_.Inf; PreviousVersion = $_.Version
      Covered = [bool](Test-Coverage $_ $pkg); DrivesDisplay = ($_.DisplayWidth -gt 0)
    }
  })
}
$state | ConvertTo-Json -Depth 6 | Set-Content (Join-Path $backupDir 'state.json') -Encoding UTF8
Log ("Backed up {0} AMD packages + registry; state.json written." -f $amdPkgs.Count) 'OK'

# --- watchdog (armed before the risky step)
if ($Watchdog) { Install-Watchdog -State $state }

# --- install
$added = @()
foreach ($s in $pkg.SupportInfs) {
  $r = Invoke-Pnputil @('/add-driver', $s)
  $added += $r.Added
}
Log ("Installing display driver {0} - the screen may blank briefly..." -f $pkg.InfName)
$r = Invoke-Pnputil @('/add-driver', $pkg.Inf, '/install')
$added += $r.Added
$rebootNeeded = ($r.ExitCode -eq 3010 -or $r.ExitCode -eq 1641)
if ($r.ExitCode -ne 0 -and -not $rebootNeeded) {
  Log ("pnputil failed with exit code {0}. Nothing else will be attempted. Use -Rollback if a device is now misbound." -f $r.ExitCode) 'FAIL'
  exit 3
}
$state.AddedPackages = @($added | Select-Object -Unique)
$state | ConvertTo-Json -Depth 6 | Set-Content (Join-Path $backupDir 'state.json') -Encoding UTF8
if ($Watchdog) { $state | ConvertTo-Json -Depth 6 | Set-Content "$script:WatchdogDir\state.json" -Encoding UTF8 }
Start-Sleep -Seconds 8

# --- verify
Log 'After install:'
$after = @(Get-AmdAdapters)
Show-Adapters $after $null
$bad = @()
foreach ($t in $targets) {
  $a = $after | Where-Object { $_.InstanceId -eq $t.InstanceId } | Select-Object -First 1
  if (-not $a) { $bad += $t.Name; continue }
  if ($a.Version -ne $pkg.Version) { Log ("  {0} is on {1}, expected {2}" -f $a.Name, $a.Version, $pkg.Version) 'WARN'; $bad += $a.Name }
  if ($a.Status -ne 'OK') { Log ("  {0} status {1} (problem {2})" -f $a.Name, $a.Status, $a.Problem) 'FAIL'; $bad += $a.Name }
  if ($t.DisplayWidth -gt 0 -and $a.DisplayWidth -le 0) { Log ("  {0} no longer reports a video mode - if your screen is black, run -Rollback now (this console still works blind: type it carefully)." -f $a.Name) 'FAIL'; $bad += $a.Name }
}
foreach ($o in $others) {
  $a = $after | Where-Object { $_.InstanceId -eq $o.InstanceId } | Select-Object -First 1
  if ($a -and $a.Inf -ne $o.Inf) { Log ("  {0} changed binding {1} -> {2} unexpectedly" -f $a.Name, $o.Inf, $a.Inf) 'WARN' }
}
Show-VulkanRegistrations
$vi = Get-Command vulkaninfo -ErrorAction SilentlyContinue
if ($vi) {
  Log 'vulkaninfo --summary devices:'
  try { & $vi.Source --summary | Select-String 'deviceName' | ForEach-Object { Log ("  {0}" -f $_.Line.Trim()) } } catch { Log '  vulkaninfo failed' 'WARN' }
} else { Log '  (vulkaninfo not on PATH - install the LunarG Vulkan SDK, or check with any Vulkan app, to confirm every adapter enumerates)' }

# --- software
if ($InstallSoftware) {
  if (-not $pkg.Ccc2) { Log 'ccc2_install.exe not found in the package; skipping the Adrenalin UI.' 'WARN' }
  else {
    Log 'Installing the Adrenalin UI silently (ccc2_install.exe /S) - this takes several minutes...'
    $p = Start-Process $pkg.Ccc2 -ArgumentList '/S' -PassThru
    if (-not $p.WaitForExit(30 * 60 * 1000)) { Log '  installer still running after 30 min; leaving it - check Apps & Features later.' 'WARN' }
    else { Log ("  installer exit code {0}" -f $p.ExitCode) }
    foreach ($rk in 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*', 'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*') {
      Get-ItemProperty $rk -ErrorAction SilentlyContinue | Where-Object { $_.DisplayName -match '^AMD' } | ForEach-Object { Log ("  installed: {0} {1}" -f $_.DisplayName, $_.DisplayVersion) }
    }
  }
}

# --- summary
if ($bad) { Log ("Finished WITH PROBLEMS on: {0}. Backups and state.json are in {1}. -Rollback restores the previous binding." -f (($bad | Select-Object -Unique) -join ', '), $backupDir) 'FAIL' }
else { Log ("Finished. Updated {0} adapter(s) to {1}; {2} left untouched. Backups in {3}." -f $targets.Count, $pkg.Version, $others.Count, $backupDir) 'OK' }
if ($rebootNeeded) { Log 'pnputil asked for a reboot to finish.' 'WARN' }
if ($Watchdog) { Log 'The watchdog stays ARMED for your next reboot: a healthy boot disarms it within about two minutes; a black screen for 10 minutes triggers the automatic rollback and one reboot.' }
$rc = 0; if ($bad) { $rc = 4 }
exit $rc
