EIGHT STREETS ON FIRE: RELEASE
==============================
Code and data behind the result L_8 = 68 (every eight-path forest whose paths all have at least 68 vertices is
well-burnable; Tan and Teh's forest (67,67,67,67,102,102,102,102) shows 67 is not enough). Computed 18-19 October
2026. Page: ../index.html, section 10. Python 3, standard library only.

CODE (code/)
  cert_check.py                715673d54a2790bf96427dbca8805ecfbcba883dccd2e3350985df074e1dc45e
      checks the third program's certificate files
  e_slice.py                   154b1ece1a972106a9f77914bd883262ccac0760250bc9d5c87f5a81befcdcaf
      the third program: its own enumerator and search (levels 24, 25, 31, 32)
  l8_certificate_census.py     cb56fdb9aeff6dbd90f36f56d679b244f4ab54564b5906fa6c20e33e48c7d333
      per-chunk census of the stream against exact counts
  l8_certificates.py           00e66a4d2e13d8f8daf57bd3c87176c79ad7a4572ee26bd4620fbdf9d72289f7
      generator and its checker; "check" prints the byte-stream and timing-free digests
  l8_release_pack.py           329589b94bf09eee90610cf96d7e3a059ba536abfa53b09e2a40046f7a7b1f04
      packs a certificate directory into the nine level files and manifest.json
  l8_release_unpack.py         ca0d56a066925582e6e9ffd79852f9f15c0f730693057c68e9ffbfbf6a428ebf
      restores the chunk files from the level files and checks every digest
  l8_stream_verify.py          cef30db19d6401f2eeb31755395fe1a7e346fe64023cc24b42093b4500babd47
      independent verifier: completeness, order, per-chunk counts, every tiling
  mechanism.py                 d9804b4af74386c2447f7ec55c4264bb0bf0b6889c20b3d639cb1d769b806f79
      the three no-backtracking rules scored on real towns
  pile_counts.py               eb44ccf5b59d14ade8d7c018073e3df10e6e3ba56013cf3918159809665ad9ea
      how many towns the reduction leaves, for any number of streets
  r3_certcounts.py             4b4d4fda26c35aa3908a3e785a8610de3e84fc15dacc1077fd204924df32300d
      the count-first rule's assignment stage with the certified plank counts

THE CERTIFICATE STREAM (data/E24.jsonl.xz ... data/E32.jsonl.xz, data/manifest.json)
  One record per town: {"m": days, "town": [eight street lengths], "a": street index of each plank, largest plank
  first, "n": search nodes, "g": first-branch flag}. Each chunk (days, shortest street) ends in a footer line.
  64,787,844 records in 285 chunks; 6.9 GB uncompressed.
  Byte-stream SHA-256 of the retained run (chunk files concatenated in name order):
      90fea878fc36d18da25e52b2e73fbfcb8e4a447c72e470f9e5c3a5ea30d1063b
  Timing-free SHA-256 (footers without their elapsed-time field; identical for every regeneration):
      da7c2e7716df23188cba01580ceabb4172e924529b9b73721671c330479c3a96
  The same for levels 24, 25, 31 and 32 alone, which equals two fresh regenerations on another machine:
      0d3799d021b0182d998426f5fe17ff7dac7be3af652acea4ccd7bb30669530f1
  Files: E24.jsonl.xz ... E32.jsonl.xz, 340 MB in all (E28 is the largest, 122 MB), and manifest.json (8,988 bytes,
  SHA-256 4523b4b4d27cdad86ffb8c1dd9ed9f16a77435f4ea27ce2e3d169f4a1bcc313b). Per-file sizes and SHA-256s, before and
  after compression, are in manifest.json. The folder has no index page; use the names above.

SMALLER DATASETS (data/)
  mechanism_rates.json         65b28fc5765f2fe29e547b73c3db198fb4472f80c1c9dd78ed9a959a3ea4e92e        608 bytes
      success counts of the three no-backtracking rules, by level
  third_program_E24.json.xz    1037227d6d4e991c04cd7ec856a107fae37bab3fe07dbf9bbdde0599ca65ef50     31,692 bytes
      third program's certificates, 24 days (3,319 towns)
  third_program_E25.json.xz    2d70b5ae0e45ab584b9892e214f511c5731921b4c7d46ff5625148ea5ce27311  2,916,760 bytes
      third program's certificates, 25 days (425,632 towns)
  third_program_E31.json.xz    1039febb486d762a7238413d6efcd126bff1f3c82999de2e953cbad5225eb6cb    900,996 bytes
      third program's certificates, 31 days (106,518 towns)
  third_program_E32.json.xz    5a1db14a35e8c872386bf68a48a7d428045cba29466fe3ae4de3f122ddc1f307      2,908 bytes
      third program's certificates, 32 days (186 towns)

CHECK IT YOURSELF
  Restore and verify the released certificates:
      python3 code/l8_release_unpack.py data CERTS
      python3 code/l8_certificates.py check CERTS
      python3 code/l8_stream_verify.py CERTS
  Or regenerate them from nothing (about two hours on eight cores) and compare the timing-free digest:
      python3 code/l8_certificates.py run  NEW --workers 8
      python3 code/l8_certificates.py check NEW
  Count the towns for any number of streets:
      python3 code/pile_counts.py 8 68
