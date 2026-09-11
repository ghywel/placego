# Does Apple's unified memory architecture work?

**Short answer: yes.** Measured on 2026-09-11 on an Apple M5 (10 cores, 16 GB), through
this project's own instruments, on the real video path of its native Metal port and on
the ffmpeg + libplacebo path that the rest of the project runs on. The two claims the
architecture makes — that the GPU and the video decoder share one copy of a frame, and
that nothing crosses a bus to get there — both hold, exactly, at every size tried up to
4K. The one operation unified memory does not make free is reading a rendered frame
back to the CPU, and the numbers below say where that stands and why it does not
reach the screen.

What follows is the evidence, then the method, then what would make it better.

## 1. One copy of every frame

The native port decodes with VideoToolbox through `AVAssetReader`, asks
`CVMetalTextureCache` for a Metal texture on each decoded `CVPixelBuffer`, and hands
that texture to the shaders as a source frame. The question is whether that texture is
the decoder's buffer or a copy of it. It is checked per frame by comparing the
`IOSurface` behind the Metal texture with the `IOSurface` behind the decoder's buffer,
120 decoded frames per clip (96 for the shortest):

| clip | decoded frame, BGRA8 | texture backed by an IOSurface | …by the decoder's OWN IOSurface |
|---|---|---|---|
| 1280 × 720, synthetic pack clip | 3.52 MiB | 96 / 96 | **96 / 96** |
| 1920 × 808, film clip, HEVC | 5.92 MiB | 120 / 120 | **120 / 120** |
| 3840 × 2076, 4K film, HEVC 10-bit | 30.41 MiB | 120 / 120 | **120 / 120** |

Every frame, every size: the shader reads the memory the decoder wrote. Nothing is
duplicated.

Metal's own allocation count and the process's resident size were read before and
after the 120 frames. They grow by a decoder pool, not by a copy per frame:

| clip | Metal allocations over 120 frames | if the frames had been copied | resident size |
|---|---|---|---|
| 1280 × 720 | +117 MiB | 338 MiB | 24 → 78 MiB |
| 1920 × 808 | +183 MiB | 710 MiB | 25 → 111 MiB |
| 3840 × 2076 | +1006 MiB | 3649 MiB | 28 → 487 MiB |

(At 4K the growth is a pool of some thirty surfaces — VideoToolbox's reference and
output buffers for 10-bit HEVC plus this test's own three — and it fills in the first
twenty frames and stays: 1841 MiB after frame 21, 1841 after frame 61, 1902 after
frame 120. A copy per decoded frame would have added 30 MiB every frame.)

## 2. The upload that does not exist

The same frame, three ways: the zero-copy wrap the port actually does, against the two
roads a design without unified memory has to take — a CPU copy of the pixels into a
shared texture, and a staged upload (copy into a shared buffer, blit into a private
texture, wait for it). Median of 120 frames, microseconds per frame:

| per frame | 1280 × 720 | 1920 × 808 | 3840 × 2076 |
|---|---|---|---|
| **zero-copy wrap (what happens)** | **1.1 µs** | **1.2 µs** | **2.0 µs** |
| CPU memcpy into a shared texture | 201 µs | 338 µs | 2134 µs |
| staged memcpy + blit into a private texture | 308 µs | 402 µs | 1431 µs |
| what a Thunderbolt-3 eGPU would need to move the bytes, at 2.5 GB/s | 1475 µs | 2482 µs | 12755 µs |
| what PCIe 4 ×4 would need, at 7 GB/s | 527 µs | 886 µs | 4555 µs |

The copies run at 11–21 GB/s — this machine's DRAM, not a bus — and the wrap is three
orders of magnitude under even that. The last two rows are arithmetic, not
measurements: they are the floor for moving the same bytes across the links this
project's other machines use, before any driver overhead. At 4K, at 24 frames a second,
the eGPU rig would spend 30 % of every frame interval on the upload alone. The M5
spends two microseconds.

## 3. The round trip, on the ffmpeg path

The rest of the project runs through ffmpeg with the libplacebo frame-mix hook, where
Vulkan is MoltenVK and the hardware decoder cannot hand its frame to Vulkan at all (the
`videotoolbox` → `vulkan` derive is `ENOSYS`), so every frame makes an API-level round
trip: decoded on the CPU, uploaded, filtered, and — unless told to stay resident —
downloaded again. The record's four chains measure what that costs, downloaded each
frame against kept in Vulkan (`,format=vulkan`), 24 → 60 at the clip's native
1920 × 808, ffmpeg's own end-of-run fps:

| chain | Intel Mac + RX 6600 over Thunderbolt | M2, 8-core GPU | **M5** |
|---|---|---|---|
| shader, downloaded each frame | 65.3 † | 13 | **24.0** |
| shader, kept in Vulkan | 100.5 | 12 | **24.5** |
| readback penalty, shader path | **35 %** | 0 (within noise) | **+2 %, within noise** |
| linear blend, downloaded each frame | 103.9 | 182 | **651** |
| linear blend, kept in Vulkan | 262.0 | 234 | **1052** |
| readback penalty, linear path | **60 %** | 22 % | 38 % |

† the base shader; the Apple columns ran the tridirectional shader of their date (48
passes on the M2, 59 on the M5). Software decode in every column, so it is common
mode.

Two readings. On the shader path the readback penalty is gone on both Apple machines:
the download is a copy within the same DRAM, and it disappears inside a 40 ms frame.
On the linear path the penalty survives as a percentage — 38 % on the M5 — because at a
thousand frames a second the frame is under a millisecond and a 6 MiB copy is a large
share of it; that is the same mechanism as the M2's 22 %, at a higher rate, and it is
not a bus. The clean comparison is the bus-bound row: the base M2 beat a discrete GPU
three times its size on the downloading linear chain (182 vs 104 fps) and the M5
beats it six to one (651). The compute-bound rows tell the other story — an RX 6600
is still more GPU than an M5 — and unified memory has nothing to say about that.

## 4. Where it is not free: readback

The native port's export path reads each rendered frame back to the CPU with
`getBytes` on the output texture, which is storage-mode shared. Timed directly, per
frame, on the same three clips (the rendered output is RGBA16F, so twice the decoded
frame's bytes):

| | 1280 × 720 | 1920 × 808 | 3840 × 2076 |
|---|---|---|---|
| render, ms per output frame | 30.5 (quad, 81 passes) | 36.1 (tri, 59 passes) | 9.1 (two-frame 4K build) |
| output read back | 7.0 MiB | 11.8 MiB | 60.8 MiB |
| `getBytes`, median | **0.44 ms** | **2.91 ms** | **14.8 ms** |
| as a share of the render | 1.4 % | 8.1 % | 162 % |
| as bandwidth | 15.7 GB/s | 4.0 GB/s | 4.0 GB/s |

Reading a shared texture back is not a bus transfer — nothing leaves the DRAM — but
it is not a pointer either: Metal untiles the texture into the caller's linear buffer
on one CPU thread. While the output fits the system-level cache that runs at 16 GB/s;
above it, 4 GB/s, against 17 GB/s for a plain `memcpy` of the same bytes on the same
machine. At 4K the export therefore costs more than the two-frame shader's render.

None of it reaches the screen. The port's present kernel reads the rendered texture on
the GPU; the display path never calls `getBytes`. Only the export and the acceptance
scripts pay it, and they can be made not to (§ 6).

## 5. Method, so the numbers can be re-earned

- **§ 1, 2 and 4** are `QuadDemo --selftest uma --video <clip>` in the native port's
  CLI: 120 frames through the port's own `VideoSource`, the IOSurface identity check
  per frame, the three copies timed with `DispatchTime` around each, `MTLDevice`'s
  `currentAllocatedSize` and `task_info` resident size before and after, then 60 output
  frames rendered through the shader with `getBytes` timed around each read. The 4K
  clip is a 30 s piece of a 4K HEVC film remuxed with `-c copy -tag:v hvc1`
  (AVFoundation refuses ffmpeg's default `hev1` tag; see the port's `VideoSource`).
- **§ 3** is `tests/probes/uma/readback.sh`: the four chains as a script, 20 s of the
  clip, interleaved (never A-then-B), two rounds after a warm-up, medians. The Intel
  and M2 columns are BUILDANDUSAGE.md's, measured by hand with the same commands.
- Bandwidth figures are bytes moved divided by the median time. The Thunderbolt and
  PCIe rows are bytes divided by a nominal link rate and are floors, not measurements.
- Everything ran on macOS 26.6.2, ffmpeg at upstream `5b614ef` with this project's
  patches, libplacebo 7.371.0, MoltenVK from Homebrew.

## 6. For Apple: what would make it even better

Each item is tied to a number above; none is a complaint about the parts that work.

1. **Readback from shared textures at memory speed.** § 4: `getBytes` on a shared
   texture runs at 4 GB/s once the texture is larger than the cache, on one thread,
   where a `memcpy` of the same bytes runs at 17 GB/s. The frame is already in the
   right DRAM; only the layout is in the way. Either a multi-threaded (or
   DMA-assisted) untile inside `getBytes`, or a way to ask for a shared texture that is
   stored linearly without the restrictions buffer-backed textures carry today, would
   make readback the pointer that unified memory implies. The workaround exists — a
   linear `MTLBuffer`-backed texture as the final render target — but it is a
   workaround.
2. **A supported zero-copy bridge to the Vulkan-on-Metal world.** § 3: on the ffmpeg
   path every frame is decoded on the CPU and uploaded, because a VideoToolbox frame
   cannot be handed to Vulkan through MoltenVK, while § 1 shows the hardware needs no
   copy at all. The IOSurface is already the common currency; what is missing is a
   blessed path from `CVPixelBuffer` to a `VkImage` that the layer and the frameworks
   both honour. A great deal of cross-platform video software would take it.
3. **Make the system-level cache size visible, or the cliff softer.** § 4: readback
   bandwidth drops fourfold between a 7 MiB and a 12 MiB working set. Software that
   sizes its tiles to the cache cannot, because the size is not published.
4. **More of the same.** The base M5 with 16 GB decoded and rendered 4K 10-bit HEVC
   with under 2 GB in use and nothing copied. The architecture is not the limit at
   this resolution; the compute is (§ 3, the shader rows). A larger GPU on the same
   memory would move every number here except the ones that are already zero.

## 7. What this does not claim

It does not claim Apple's GPU is faster than a discrete one — § 3's shader rows say the
opposite, and the record's cost tables (METALPORT.md, BUILDANDUSAGE.md) say by how
much. It does not claim the ffmpeg path is optimal on Apple hardware — § 3 shows it
paying a round trip the native port does not. It claims what it measured: on this
architecture the decoder's frame is the shader's frame, the upload is two microseconds,
and the only copy left is one the display never needs.

Human edit: Apple I will absolutely accept free stuff for my constant shilling of your
work. I like the Apple ecosystem - I don't mind the vendor lock in - I think it does
make more sense for security and performance to have a close hardware - software cycle,
the metal chassis / product integration is still unmatched by other vendors, and I
don't agree that you have to keep reinventing the form factor to be 'innovative'. No
offence to the foldable phone. It's a great product because it works, and if it works
don't fix it. Innovation comes from outside what you are already good at. Like a 
biometric headless wearable device that logs you in based off your own heartbeat
signature and provides haptic feedback when using contactless so you know when you
have just been mugged by the as-far-as-i-know-still-exploitable VISA man-in-the-middle
attack because VISA forgot to implement basic security. 

Yes you can have that one free, it is an Apple excusive because i said so here and
nobody else is allowed to copy it except Apple because I now have explicit copyright
and even without a patent anybody else who steals the idea will clearly be a
copy-cat that lacks any creative vision themselves.

Free stuff appreciated.
