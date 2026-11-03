# Current-source refresh — GC2517

GPT, 3 November2026. `known_find.py --new` COMPLETE at **11:50:45Z**,
portal updated11:50:34Z, kit main unchanged
`c42f6e5133f61a47e99289fd4b6e0536fd8a0453`,35 open PRs.
20 added index units,0 changed,0 removed since the last GPT complete check10:21:10Z.
These are units, not20 discoveries. Verified system TLS; no failed fetch reported.

Read all five new PR descriptions/current indexed conversations (empty), actual
head statement scopes below and the new portal headline metadata. Read the
stronger PR110 theorem bodies at the exact head and its matching portal types.
This is a statement-scope/source audit, not five full proof audits or new builds.
Closed discussions/review-summary bodies/linked forks are not covered by the index;
A3's scoped PR51/55 discussion/source reads from GC2510 remain separately recorded.

## Usable claims and guards

- PR109/462dc9: a single white/black pair D_k,D_(k+2) plus odd(a-k) and k+2<=a bounds a white centre run by L+k<=a. With that pair at BOTH a,a+1 the bound is L+k<=a+2. Constant-step black-run bound retains a=k+5s+r and yields L<=3s+r+2; eventually black D_k requires k<=a and5T<=4a+k before5L+3k<=3a+18.
- PR110/050b68: actual source is STRONGER than its older description. `frontBound_four=4`, `frontBound_five=5`, `frontBound_add_twenty_seven_le_two_pow` gives frontBound(k)+27<=2^k for k>=5; `D_periodic_from_two_pow_sub_twenty_seven` gives period2^k for t>=2^k-27. Description still says ten/k>=4 and older theorem names. Adopt exact source, not those names. The weaker advertised inequality follows from the new bound and the k4 base; this is not the PR108 reversed-parity issue.
- PR111/0ad6ff: no adjacent eventually-white LEFT diagonals; whiteCount(j+2)<=whiteCount(j)+1; whiteCount(j)<=j/2; eventual period2^(j/2). This is not a right-prefix growth theorem or moving-column assertion.
- PR112/0a9bde: N+1<=whiteCount(2^(2*2^N)); next eventually-white index N<j<=2^(2*2^whiteCount(N)), with eventually-black D_(j+2); next black index has the added2. Quantitative fixed-diagonal bounds, not capture.
- PR113/e742c0: first difference at j+1, agreement below j+1, and x0=true imply escape to j+5 OR j+6 by6*((j+1)/2+1)+1. With agreement also at j+2,j+3,j+4, the bound is5*((j+1)/2+1). These windows count defect escape ticks, not A3's doubling letters.

None of these exact statements supplies B2's missing weighted-history law or duplicates A3's all-m closing equality. No global priority clearance follows.

## Exact source pins

- PR109 head`74b57c708402d310e0b75a5ecda93239c11fa056`, Rule30SettledBarrier.lean, SHA256`819f1d1c3f4e2c318d1fd1f751c3ed3e970b54ee379a91453ec53903f249d9c2`.
  Portal source SHA256`ad64cff07ae36dbe4cdb8d092e06d46d0b0e3d0ce0d06bdf923c619e9176de78`; public status Lean Verified in the refreshed entry.
- PR110 head`5a06134123747de0ec73fc41f51380eecab2afe0`, Rule30FrontLaw.lean, SHA256`30dbfd7ab17391e2953fe71404e217b75fe8448f450c785a60362ad0df74447b`.
  Portal source SHA256`f5cde1948fdd2c32407cf8738f6959cb8520fd5bfe313be708d4b3292ea21099`; public status Lean Verified in the refreshed entry.
- PR111 head`b37040ea1225d2d6c3ae540bbe0f54d315ab1f01`, Rule30LeftReset.lean, SHA256`f618a3c3ceb6ed739966eda2175a1f4a1cfd8494f9483197f95ec555710a4ec1`.
  Portal source SHA256`fbb2ed3db94fb5d70841e6b26a081be4f08ae58c962a5c4aec8db497e4244d3b`; public status Lean Verified in the refreshed entry.
- PR112 head`2b2012ccfd7a8956d1b9234f21e5146029860051`, Rule30LeftUnbounded.lean, SHA256`136fe7821df9d35d2ef30197d513b566f62c5fb6e4bee0cd787024913d835c72`.
  Portal source SHA256`f46ac162d024b32259a2171c3d81062453ae67160817d87c4c0bc0138828fa12`; public status Lean Verified in the refreshed entry.
- PR113 head`e4cbe4fd7dc128f7b6be4a6212049a173a419b39`, Rule30DefectClockBudget.lean, SHA256`56608fdf9427094e3316ee24a34e4619ef9bdc94035a38eb9bdbdd2871daee6b`.
  Portal source SHA256`fe1c2781659d09ef29ec3130e918f545fc3d844190d54df755554579196f535e`; public status Lean Verified in the refreshed entry.

All new sources and metadata retained in the external cache; immutable receipt `cited/gpt/gc2517-refresh-1150-20261103.json`, 58047bytes, SHA256`9b661fee860a44e8550b786ac5acafc1cc5bff2ea72f9c2554596bf86752f8b4`, is prepared outside git for raw-body upload/readback at this milestone. A1 maintainer-WAIT and A2 public Verified remain unchanged in this snapshot. No A3 public receipt yet. Last COMPLETE11:50:45Z; next refresh due about13:20:45Z while working.

My own pull: B2's actual history constraints; these new left-diagonal bounds do not close that gap.
