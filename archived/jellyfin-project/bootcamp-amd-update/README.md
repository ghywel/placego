Human edit:

Congratulations for making it this far in the dungeon you venturous soul. You
may have rolled a 20 d20 or this is completely irrelevant to you, such is the
nature of RPG loot. 

This is the script i had Claude Code Fable write to update my intel mac bootcamp
drivers to the latest AMD release to better support my RDNA 2 RX 6600 If you have
a bootcamped machine with an AMD GPU you are welcome to try it. It doesn't pack
any binaries and requires you to download the drivers from AMD yourself. 
I have only tested it once, I don't have a second machine, it might break your
system, I don't know. It does contain safeguards to roll things go back if
things go wrong - which may or may not work. My MacBook Pro mid-2019 is a bit
weird, and a bit crashy, but that's probably my fault because I have literally
cut a hole in the base plate with an angle grinder to try and waft some more
air through the abysmal cooling system. It may work for you or it may not. If
it breaks your windows i recommend running parallels in macOS, so you can boot
a VM of your bootcamp - fix your mess - and reboot back to Windows. Where you
get parallels is up to you. Don't forgot your panoply of weird button presses
at power on to choose the boot device, boot into recovery or reset NVRAM,
PRAM, and SMC, any of which can help resolve annoying mac issues. 

Aside: It does make me sad Apple dropped bootcamp support for the m-series.
Apple - I know you have a tightly controlled software-hardware ethos. I
genuinely love your products. The iPhone has always been better than android.
(In my opinion). But it would really be nice to have bootcamp back on the
m-series. Some things are nicer to do in Windows. Some things are nicer to 
do in macOS. I would like to be able to choose. 


# Update-AmdBootcampDriver

Bind a current official AMD Adrenalin driver to the AMD GPUs it supports, on a
Windows machine that also has AMD GPUs it does *not* support - and leave those
alone. Written for Boot Camp Macs with an eGPU; applies to any mixed-generation
AMD box.

## What you need

No driver files are included, and none should be: AMD's packages are not
freely redistributable, they are over a gigabyte, and bundling one would pin
this tool to a single version. You bring the package; the script reads
whatever AMD has published.

- **This script** (`Update-AmdBootcampDriver.ps1`, one file).
- **An official AMD Adrenalin package for your newer card**, downloaded from
  AMD's site and *extracted*. Running the downloaded installer and cancelling
  at its first screen leaves the extracted files under `C:\AMD\...`; 7-Zip can
  also unpack it. You want the folder that contains `Setup.exe` and
  `Packages\Drivers\Display\WT6A_INF`. That folder is `-PackagePath`.
- **A working driver already on your older GPU** (on a Boot Camp Mac, the
  community-modified package). The script leaves that GPU exactly as it finds
  it; it does not install anything for a GPU the new package does not list.
  If your Mac's own GPU currently has no driver, fix that first.
- **Administrator rights** on the machine, and a few GB free on `C:` for the
  backups.

## The problem it solves

Official AMD packages stopped listing Polaris/Vega parts (Radeon Pro 4xx/5xx,
RX 4xx/5xx) years ago, so Boot Camp Macs run community-modified packages. Those
keep the Mac's own GPU working by pairing a modern kernel driver with an *old*
Vulkan user-mode driver. Any newer card in the same machine - an RDNA eGPU, say -
then works under Direct3D but is **invisible to Vulkan**, because the old Vulkan
driver does not know it.

Windows keeps a separate driver store per adapter, and Vulkan drivers are
registered per adapter too. So the fix is simply to give the newer card the
current official driver and leave the old card on the modified one. Both Vulkan
drivers then coexist, one per GPU. AMD's own `Setup.exe` will not do this for
you: it sees the unsupported GPU and refuses to run at all ("error 173").

## What the script does

1. Lists your AMD display adapters and parses the package INF to say which of
   them it actually supports. Only those get the new driver; Windows does the
   binding by INF match, nothing is forced.
2. Backs up every installed AMD driver package (`pnputil /export-driver`) and the
   display-class registry into `C:\AmdDriverBackup\<timestamp>\`, and writes a
   `state.json` describing the before-state.
3. Optionally installs a boot-time **watchdog** (`-Watchdog`). If the GPU being
   updated drives your only display and the screen does not come back after a
   reboot, the watchdog restores the previous driver and reboots once, on its
   own. A healthy boot disarms it within a couple of minutes.
4. Installs the package's display INF and support INFs with `pnputil`.
5. Verifies bindings and per-adapter Vulkan registration; runs `vulkaninfo` if
   it is on your PATH.
6. Optionally installs the Adrenalin UI (`-InstallSoftware`) using the
   package's own `ccc2_install.exe /S`, which does not have Setup.exe's
   hardware gate.

It never runs DDU, never factory-resets, and never deletes an existing package.
`-Rollback` restores the previous binding from `state.json` at any time.

## Usage

Extract the official AMD package first. Running the downloaded installer and
cancelling at its first screen leaves the extracted files under `C:\AMD\...`;
7-Zip can also unpack it. You want the folder that contains `Setup.exe` and
`Packages\Drivers\Display\WT6A_INF`.

Then, in PowerShell:

```powershell
# See the plan. Changes nothing; does not need admin.
powershell -ExecutionPolicy Bypass -File .\Update-AmdBootcampDriver.ps1 -PackagePath C:\AMD\extracted -DryRun

# Do it, with the boot watchdog and the Adrenalin UI. Asks for UAC if needed.
powershell -ExecutionPolicy Bypass -File .\Update-AmdBootcampDriver.ps1 -PackagePath C:\AMD\extracted -Watchdog -InstallSoftware

# See what undo would do, then undo.
powershell -ExecutionPolicy Bypass -File .\Update-AmdBootcampDriver.ps1 -Rollback -DryRun
powershell -ExecutionPolicy Bypass -File .\Update-AmdBootcampDriver.ps1 -Rollback
```

Expect the screen to blank for a few seconds when the driver binds. The script
survives that; keep the window open and wait for the summary.

## If you have no way to see the screen

This is the Boot Camp eGPU case: internal panel removed or lid closed, monitor on
the eGPU, and a bad driver means a black screen you cannot click through.

- Run with `-Watchdog`. It is armed *before* the driver is touched.
- After a reboot the watchdog waits up to 10 minutes for the updated adapter to
  report healthy with a video mode set. If it does, it disarms itself. If not,
  it puts the previous driver back and reboots once.
- If you *can* see the screen, `DISPLAY-OK.cmd` on the desktop disarms it
  immediately. Deleting `C:\AmdDriverWatchdog\flags\armed.flag` does the same.
- The watchdog only ever acts once per arming (`rolledback.flag` guards it) and
  is inert whenever `armed.flag` is absent. Leave it installed or delete the
  `AmdDriverWatchdog` scheduled task and folder when you are done.

If everything is black and the watchdog is not armed: an elevated console still
works blind, so `-Rollback` can be typed by touch, or boot into whatever other
OS or recovery you have and run it from there next time.

## Checking Vulkan afterwards

`vulkaninfo --summary` (LunarG Vulkan SDK) should list every AMD adapter. Any
Vulkan program will do: an ffmpeg with Vulkan support prints a "GPU listing"
at `-v verbose` with `-init_hw_device vulkan`. The script also prints the
registry entries it relies on: each adapter's `VulkanDriverName` should point
into its own package folder under `DriverStore\FileRepository`.

## Known limits

- Tested on one machine: a 2018 15-inch MacBook Pro (Radeon Pro 560X, kept on
  its modified driver) with an RX 6600 in a Thunderbolt enclosure, Windows 11,
  moving the 6600 from the modified 24.x-era package to Adrenalin 26.8.1. Your
  GPUs, package version and Windows build will differ; read the dry run.
- The script only ever *adds* a driver and lets Windows rank it. If Windows
  decides the existing driver is a better match (it ranks by hardware-ID
  specificity before version), nothing changes; the summary will say so.
- Windows Update may later offer its own AMD driver for the updated card. That
  is the normal state for any AMD card and unrelated to this script.
- The Adrenalin UI may report the unsupported GPU as unsupported. That is true.
- Unsigned script. `-ExecutionPolicy Bypass` runs it regardless of policy;
  read it first, it is one file and does nothing you cannot see.

## License

MIT.
