#!/usr/bin/env python3
"""Extract and validate an AMD video BIOS on an Intel Mac where macOS drives the card natively.

Read-only. It looks through the IORegistry for the copy of the video BIOS that Apple's AMD driver publishes
(a data property whose name ends in "bin_image", usually "ATY,bin_image"), saves it, and checks that it is a
well-formed ATOM BIOS for the expected PCI device. Nothing is written to the card.

  python3 extract_vbios_intel.py --out ./vbios_out            # extract from the IORegistry and validate
  python3 extract_vbios_intel.py --validate some_dump.rom     # validate a file obtained another way

Needs only the Python standard library (3.8 or later) and /usr/sbin/ioreg.
"""
import argparse, hashlib, os, plistlib, re, struct, subprocess, sys

VENDOR, DEVICE = 0x1002, 0x73FF   # AMD, Navi 23 (RX 6600 family)

def le(b):
  return int.from_bytes(bytes(b)[:4], "little") if isinstance(b, (bytes, bytearray)) else None

def validate(rom, expect_dev=DEVICE):
  """Return (ok, lines). ok is True only when every structural check passes."""
  out, ok = [], True
  def check(cond, msg):
    nonlocal ok
    out.append(("  ok   " if cond else "  FAIL ") + msg)
    ok = ok and bool(cond)
  out.append("size %d bytes, sha256 %s" % (len(rom), hashlib.sha256(rom).hexdigest()))
  if len(rom) < 0x200:
    return False, out + ["  FAIL file too short to be a video BIOS"]
  check(rom[0:2] == b"\x55\xaa", "option ROM signature 55 AA at offset 0")
  img_len = rom[2] * 512
  check(0 < img_len <= len(rom), "first image length %d bytes fits in the file" % img_len)
  check(b"761295520" in rom[0x28:0x48], "ATI magic string '761295520' near offset 0x30")
  pcir = struct.unpack_from("<H", rom, 0x18)[0]
  if pcir + 0x18 <= len(rom) and rom[pcir:pcir + 4] == b"PCIR":
    ven, dev = struct.unpack_from("<HH", rom, pcir + 4)
    check(ven == VENDOR, "PCIR vendor id %04x is AMD (1002)" % ven)
    check(dev == expect_dev, "PCIR device id %04x matches the card (%04x)" % (dev, expect_dev))
  else:
    check(False, "PCIR structure found at the offset stored at 0x18")
  atom = struct.unpack_from("<H", rom, 0x48)[0]
  check(atom + 8 <= len(rom) and rom[atom + 4:atom + 8] == b"ATOM", "ATOM header signature at the offset stored at 0x48 (%#x)" % atom)
  if 0 < img_len <= len(rom):
    check(sum(rom[:img_len]) & 0xff == 0, "first image checksum is zero")
  # list every image in the file (legacy x86 image first, a UEFI image usually follows)
  off, n = 0, 0
  while off + 0x1c <= len(rom) and rom[off:off + 2] == b"\x55\xaa" and n < 8:
    p = off + struct.unpack_from("<H", rom, off + 0x18)[0]
    if rom[p:p + 4] != b"PCIR": break
    length = struct.unpack_from("<H", rom, p + 0x10)[0] * 512
    code, ind = rom[p + 0x14], rom[p + 0x15]
    out.append("  image %d at %#x: %d bytes, type %s%s" % (n, off, length, {0: "legacy x86", 3: "UEFI"}.get(code, hex(code)), ", last" if ind & 0x80 else ""))
    if ind & 0x80 or length == 0: break
    off, n = off + length, n + 1
  for s in sorted(set(re.findall(rb"113-[A-Z0-9_.\-]{4,40}", rom))):
    out.append("  part number string: " + s.decode("ascii", "replace"))
  for s in sorted(set(re.findall(rb"[ -~]{0,40}(?:RX ?6600|NAVI ?23|DIMGREY)[ -~]{0,40}", rom, re.I)))[:6]:
    out.append("  name string: " + s.decode("ascii", "replace").strip())
  return ok, out

def walk(node, path, anc, found, gpus):
  if not isinstance(node, dict): return
  name = node.get("IORegistryEntryName", "?")
  path = path + [name]
  ven, dev = le(node.get("vendor-id")), le(node.get("device-id"))
  if ven is not None and dev is not None: anc = (ven, dev, name)
  if ven == VENDOR and (le(node.get("class-code")) or 0) >> 16 == 0x03: gpus.append((node, path))
  for k, v in node.items():
    if isinstance(v, (bytes, bytearray)) and k.lower().endswith("bin_image"):
      found.append((k, bytes(v), "/".join(path[-6:]), anc))
  for child in node.get("IORegistryEntryChildren", []): walk(child, path, anc, found, gpus)

def from_ioreg(outdir):
  raw = subprocess.run(["/usr/sbin/ioreg", "-a", "-l", "-w0", "-p", "IOService"], stdout=subprocess.PIPE, check=True).stdout
  tree = plistlib.loads(raw)
  found, gpus = [], []
  for root in (tree if isinstance(tree, list) else [tree]): walk(root, [], None, found, gpus)
  print("AMD display-class PCI devices seen: %d" % len(gpus))
  for node, path in gpus:
    print("  %04x:%04x at .../%s" % (le(node.get("vendor-id")), le(node.get("device-id")), "/".join(path[-3:])))
    for k in sorted(node):
      v = node[k]
      if k.startswith("ATY,") or k in ("model", "subsystem-id", "subsystem-vendor-id", "revision-id"):
        if isinstance(v, (bytes, bytearray)) and len(v) > 64: print("    %s: <%d bytes>" % (k, len(v)))
        elif isinstance(v, (bytes, bytearray)): print("    %s: %s  %r" % (k, bytes(v).hex(), bytes(v).rstrip(b"\0")))
        else: print("    %s: %r" % (k, v))
  if not found:
    print("\nNo '*bin_image' property anywhere in the IORegistry. Use one of the fallback routes in the handover.")
    return 2
  os.makedirs(outdir, exist_ok=True)
  rc = 1
  for i, (key, data, path, anc) in enumerate(found):
    who = "%04x:%04x" % (anc[0], anc[1]) if anc else "unknown device"
    print("\ncandidate %d: property '%s' on %s (nearest PCI device %s), %d bytes" % (i, key, path, who, len(data)))
    ok, lines = validate(data)
    print("\n".join(lines))
    fn = os.path.join(outdir, "vbios_%s_%d_%s.rom" % (who.replace(":", "_"), i, hashlib.sha256(data).hexdigest()[:12]))
    with open(fn, "wb") as f: f.write(data)
    print("saved %s  ->  %s" % (fn, "VALID" if ok else "NOT VALID (keep it anyway and report the failed checks)"))
    if ok and anc and anc[:2] == (VENDOR, DEVICE): rc = 0
  return rc

if __name__ == "__main__":
  ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
  ap.add_argument("--out", default="vbios_out", help="directory for extracted images")
  ap.add_argument("--validate", metavar="FILE", help="validate an existing dump instead of reading the IORegistry")
  args = ap.parse_args()
  if args.validate:
    with open(args.validate, "rb") as f: ok, lines = validate(f.read())
    print("\n".join(lines)); print("VALID" if ok else "NOT VALID")
    sys.exit(0 if ok else 1)
  sys.exit(from_ioreg(args.out))
