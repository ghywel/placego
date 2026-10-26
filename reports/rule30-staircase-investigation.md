# The owner's staircase observation: investigation

2026-10-26, GPT; owner-authorized local investigation. No schedules or M5 job.
Status: specification before image diagnostic; no result yet.

The owner reports that every staircase inspected terminates in a vertical
alternating segment, and provided a crop marking a staircase and its endpoint.
Preserve that full conjecture; do not substitute the weaker claim that an
alternating column is possible. First determine the actual cells and orientation,
then define the staircase without building alternation into its definition.

Pull: repeated vertical bars may be a forced local structure. Unease: the crop's
palette and time axis have not been checked, and the red ink obscures cells.

Record searched: `staircase|vertical stripe|vertical run|rotat.*diagram` via
record_find.py: 166 paragraphs in 46 files. Main relevant pointers: §8.18,
§8.59, §8.73/74, GC847 and GC1932/33. No novelty claim. Prior work distinguishes
spatial stripes, moving diagonals and fixed-column time traces.

## Frozen image diagnostic

Source: tests/probes/wolfram/staircase_image_read.py. Grid spacing estimated
from unmarked colour transitions: x centre 3.6+7.18*c, y centre 0.6+7.16*r,
32 by 32. Dark/light anchors (21,24,28)/(235,230,218). Ignore any centre whose
RGB L1 distance to both anchors is at least75, including red annotations.

Prediction: one orientation/encoding should account for every sufficiently
well-extracted unobscured neighbourhood. This is a diagnostic prediction, not
the staircase theorem. Conventional downward time is not assumed in testing.
Counterfactual: incorrect orientations/encodings should produce mismatches.
Controls: literal eight-entry rule30 table; omit unknown cells, rather than
imputing values from the conclusion. Unexpected check: test horizontal time
as well as upward/downward time. If no exact fit, stop mathematical inference
from this grid and diagnose sampling/orientation before any census.

Bounds: one process, 20 CPU seconds, 30 wall seconds, 512 MiB address space,
2 MiB per output file; output below20 KiB expected. No simulation or census.
Read only the supplied228-square image; no image editing, export or upload.
The script takes the private path at runtime; repository carries no local path.

Pre-analysis failure retained: first invocation stopped at RLIMIT_AS with
ValueError (host rejects this limit), before reading any image cells. Amended
containment: 128 MiB data-segment hard limit, CPU/wall/file limits unchanged;
actual peak process RSS reported separately. This is NOT a 512 MiB total-memory
hard cap. The fixed228-square input and fixed1024-cell arrays bound workload.

## Further work after the diagnostic

Define the staircase in the identified coordinates. Derive its local transition
and endpoint by hand, including margins and short cases. Only then freeze a
small exact enumeration or finite-seed test with independent controls. An
observed alternating segment is not an endless period-two column.

Second pre-analysis failure: RLIMIT_DATA also rejected before image reading.
Do not retry resource-limit variants. Final diagnostic uses fixed input/array
bounds and measured peak RSS, with CPU/wall/file caps enforced; no OS memory
cap is claimed. No large arrays or simulation are permitted in this stage.
