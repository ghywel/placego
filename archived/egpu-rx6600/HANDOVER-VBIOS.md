# Handover: retrieve the RX 6600 video BIOS on the Intel MacBook Pro

From: Claude on the M5 MacBook Pro (Local), 2026-11-13 15:45 UTC
To: the Claude instance on the Intel MacBook Pro
Status of this note: a request for one file. It is a side project of the owner's and is not part of the research
programme, so nothing here goes on the board or into the research record.

## What is being asked

The owner is moving the Radeon RX 6600 eGPU (Razer Core X Chroma enclosure) back to your machine for a short while.
While it is there, please save a copy of the card's **video BIOS** (the firmware image stored on the card, also called
the VBIOS or option ROM), check that the copy is sound, and hand it back with its digest. The owner will then return
the card to the M5.

This is a read-only job. Nothing is to be written to the card.

## Why it is needed

We are trying to make this card do compute on the Apple Silicon M5, where Apple ships no driver for it. The route is
tinygrad's "TinyGPU" approach: a small Apple-signed driver extension exposes the card's registers to user space, and
a user-space driver written in Python brings the card up. tinygrad supports the generation after this one (RDNA3 and
later); this card is RDNA2, so its bring-up code has to be written.

First results on the M5 (all MEASURED on Local's host, 2026-11-13):

- The card answers register reads and reports 8176 MB of video memory.
- Its own boot firmware has run: the hardware inventory table is present, and video memory holds written data.
- Its security processor's bootloader is idle and waiting to be given firmware. That is the next stage.
- **The video BIOS cannot be read on the M5.** The card's ROM registers return a constant, and the signed driver
  cannot map the expansion ROM region.

The Linux driver for this card family takes three things from the video BIOS that we expect to need:

1. the power table that is uploaded to the card's power-management controller;
2. the firmware capability flags, which say whether a second stage of memory training must be requested;
3. the initialisation tables, in case the card needs the BIOS's start-up script run by hand.

Your machine has a working Apple driver for this card, so it should be able to see the BIOS.

## The card

| | |
|---|---|
| PCI vendor:device | `1002:73ff` (AMD, Navi 23) |
| Revision | `c7` (RX 6600, non-XT) |
| Subsystem vendor:device | `1eae:6505` |
| Video memory | 8 GB |
| Enclosure | Razer Core X Chroma, Thunderbolt 3 |

## Route A (try first): the copy Apple's driver publishes

On Intel Macs, Apple's AMD driver normally publishes the card's BIOS image as a data property in the IORegistry,
named `ATY,bin_image`, on the graphics device's entry. CONJECTURE: this is my expectation from how the AMD driver
behaves on Intel Macs in general. I have not confirmed it for this card as an eGPU, so treat a missing property as a
real possible outcome and move to Route B.

The script `extract_vbios_intel.py`, next to this note, does the whole of Route A. It needs only the Python standard
library (3.8 or later) and `/usr/sbin/ioreg`. It reads the IORegistry, saves every property whose name ends in
`bin_image`, and validates each one.

```bash
python3 extract_vbios_intel.py --out ./vbios_out
```

What it checks, so that you can judge a result yourself:

- the image starts with the bytes `55 AA`;
- the ATI marker string `761295520` is near offset 0x30;
- the PCI data structure (`PCIR`) names vendor `1002` and device `73ff`;
- the ATOM header, at the offset stored at 0x48, carries the signature `ATOM`;
- the first image's bytes sum to zero modulo 256;
- it then lists each image in the file (a legacy image first, usually a UEFI image after it) and any part-number
  string of the form `113-...`.

Exit status 0 means a valid image for `1002:73ff` was saved. Status 2 means no such property exists. Status 1 means
something was found but failed a check: keep the file and report which checks failed.

Tested on Local's host: the validator accepts a well-formed synthetic image, a padded one, and rejects a corrupted
checksum and a wrong device id, under Python 3.9 and 3.15. The IORegistry walk runs and finds the card. The
extraction itself is untested, because the property does not exist on Apple Silicon.

A quick manual check that the property exists, before running the script:

```bash
ioreg -l -w0 | grep -c "bin_image"
```

## Route B: if the IORegistry has no copy

In order of preference. Each needs the owner's agreement before you start, because each means booting another system
or installing something.

1. **Windows (Boot Camp), if it is installed.** GPU-Z has a "save BIOS to file" button. AMD's `amdvbflash` can also
   save: `amdvbflash -s 0 rx6600.rom`. Use the save option only. Never use an option that programs or flashes.
2. **Linux from a live USB stick, if this machine will boot one with the eGPU attached.** Find the card with
   `lspci -nn | grep 73ff`, then, as root, with `BDF` standing for its address:

   ```bash
   echo 1 > /sys/bus/pci/devices/0000:BDF/rom
   ```

   ```bash
   cat /sys/bus/pci/devices/0000:BDF/rom > rx6600.rom
   ```

   ```bash
   echo 0 > /sys/bus/pci/devices/0000:BDF/rom
   ```

3. **A published image for the same board.** This is a substitute, not the card's own BIOS, and under the working
   agreement (§10) it needs the owner's agreement and must be named as a substitute. If it comes to this, match on
   the part-number string and BIOS version that macOS shows for the card (see "Also worth collecting"), and on
   subsystem `1eae:6505`.

Whatever the route, validate the file with the same script:

```bash
python3 extract_vbios_intel.py --validate rx6600.rom
```

## Do not

- Do not flash, program or modify the card's firmware in any way.
- Do not disable System Integrity Protection or load third-party kernel extensions to reach the ROM. If Routes A and
  B fail, report that and stop.
- Do not commit the BIOS image to git. It is the vendor's firmware. Data stays outside git and is cited by digest
  (working agreement §5).

## Also worth collecting while the card is there

These are small and cost a minute. Remove serial numbers and machine identifiers before saving.

- The graphics section of the system report: `system_profiler SPDisplaysDataType`. The ROM revision, BIOS version
  and EFI driver version lines are the useful ones.
- The script's printed list of `ATY,` properties for the card (it prints them before extracting).
- The macOS version, and which AMD kernel extensions are loaded: `kextstat | grep -i AMD`.

## What to send back

1. The BIOS image file, by the shared store (`sharedstore/README.md`) or carried over by the owner.
2. Its SHA-256 digest and size.
3. The full output of the script run that produced or validated it.
4. Which route worked, and anything that did not behave as this note said it would.

A short reply file beside this one, or a message through the owner, is enough.

## Before unplugging

Use the eGPU "Disconnect" item in the macOS menu bar before pulling the Thunderbolt cable on your machine, so the
Apple driver lets go of the card cleanly.

## Misgivings and curiosities

- The image Apple's driver publishes may be only the first (legacy) image, or may be padded to a round size. Either
  is fine: the ATOM tables we need are in the first image. Report the size and the image list as the script prints
  them.
- I do not know whether the published copy is byte-identical to the flash contents. If Route A and a Route B dump are
  both available, their digests would settle it; one is enough for our purpose.
- It is not yet shown that the port needs the BIOS at all. tinygrad's driver for the next generation never reads it.
  We are fetching it now because the card is easy to move today and a missing file later would stall the work.
- If your machine shows anything unusual about how macOS drives this card (properties naming power states, memory
  timing, or a firmware version), note it. A working driver's view of the card is evidence we cannot get on the M5.
