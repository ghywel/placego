import Ruliology.CellularAutomata.Rule30Jen

namespace Ruliology.CellularAutomata.Rule30MovingWall
open Rule30Jen

/-- A rule-30 evolution of the whole line. -/
def IsR30Z (G : Nat → Int → Bool) : Prop :=
  ∀ t x, G (t + 1) x = rule (G t (x - 1)) (G t x) (G t (x + 1))

/-- The ring orbit of `100100000`: row `τ` as a 9-bit number, bit `j` the cell at diagonal index `j`. -/
def orbRows : List Nat := [9, 63, 193, 326, 217, 302, 465, 54, 202, 375, 136, 441, 78, 498, 29, 99, 429, 82, 446, 65, 455, 88, 424, 91, 421, 122, 390, 153, 494, 17, 119, 393, 190, 323, 204, 373, 138, 439, 72, 504, 11, 53, 203, 372, 143, 432, 83, 445, 66, 462, 113, 407, 232, 281, 366, 145, 502]

/-- The closure: `(key, ψ)` with `key = (tq * 9 + dq) * 2 ^ 24 + strip`. -/
def closure : List (Nat × Int) := [
  (2321766113, 0),
  (2506794087, -14),
  (2678767288, -9),
  (2670378680, -9),
  (2846524045, -4),
  (2842329741, -4),
  (2850718349, -4),
  (3014313684, 1),
  (3005925076, 1),
  (3031067222, 6),
  (3026872918, 6),
  (3035261526, 6),
  (3198921682, 11),
  (3190533074, 11),
  (3366496351, 16),
  (3362302047, 16),
  (3370690655, 16),
  (3545979266, 2),
  (3720957638, 7),
  (3712569030, 7),
  (3883889258, 12),
  (3892277866, 12),
  (4051771306, 17),
  (4043382698, 17),
  (4223901866, 22),
  (4211318954, 22),
  (4219707562, 22),
  (4257833815, 8),
  (4245250903, 8),
  (4253639511, 8),
  (4420744528, 13),
  (4414453072, 13),
  (4422841680, 13),
  (4427035984, 13),
  (4588688728, 18),
  (4580300120, 18),
  (4582397272, 18),
  (4590785880, 18),
  (4594980184, 18),
  (4584494424, 18),
  (4773423769, 4),
  (4765035161, 4),
  (4779715225, 4),
  (4771326617, 4),
  (4777618073, 4),
  (4959720927, -10),
  (4951332319, -10),
  (4957623775, -10),
  (4963915231, -10),
  (5131818048, -5),
  (5119235136, -5),
  (5127623744, -5),
  (5125526592, -5),
  (5117137984, -5),
  (5121332288, -5),
  (5137192673, 0),
  (5141386977, 0),
  (5149775585, 0),
  (5145581281, 0),
  (5146629857, 0),
  (5134046945, 0),
  (5142435553, 0),
  (5148727009, 0),
  (5140338401, 0),
  (5330609255, -14),
  (5322220647, -14),
  (5331657831, -14),
  (5319074919, -14),
  (5327463527, -14),
  (5325366375, -14),
  (5495242424, -9),
  (5491048120, -9),
  (5499436728, -9),
  (5494193848, -9),
  (5487902392, -9),
  (5496291000, -9),
  (5500485304, -9),
  (5497339576, -9),
  (5488950968, -9),
  (5668242061, -4),
  (5670339213, -4),
  (5661950605, -4),
  (5662999181, -4),
  (5654610573, -4),
  (5656707725, -4),
  (5665096333, -4),
  (5669290637, -4),
  (5658804877, -4),
  (5660902029, -4),
  (5826594516, 1),
  (5822400212, 1),
  (5830788820, 1),
  (5836031700, 1),
  (5823448788, 1),
  (5831837396, 1),
  (5828691668, 1),
  (5837080276, 1),
  (5832885972, 1),
  (5824497364, 1),
  (5838128852, 1),
  (5829740244, 1),
  (6005877334, 6),
  (5997488726, 6),
  (5991197270, 6),
  (5999585878, 6),
  (6003780182, 6),
  (5994342998, 6),
  (5992245846, 6),
  (6000634454, 6),
  (6004828758, 6),
  (5996440150, 6),
  (5990148694, 6),
  (5998537302, 6),
  (6158003154, 11),
  (6166391762, 11),
  (6160100306, 11),
  (6168488914, 11),
  (6172683218, 11),
  (6162197458, 11),
  (6173731794, 11),
  (6165343186, 11),
  (6164294610, 11),
  (6159051730, 11),
  (6167440338, 11),
  (6171634642, 11),
  (6326626399, 16),
  (6335015007, 16),
  (6339209311, 16),
  (6331869279, 16),
  (6340257887, 16),
  (6336063583, 16),
  (6327674975, 16),
  (6341306463, 16),
  (6332917855, 16),
  (6325577823, 16),
  (6333966431, 16),
  (6329772127, 16),
  (6364551554, 2),
  (6372940162, 2),
  (6368745858, 2),
  (6360357250, 2),
  (6362454402, 2),
  (6370843010, 2),
  (6375037314, 2),
  (6539529926, 7),
  (6531141318, 7),
  (6541627078, 7),
  (6529044166, 7),
  (6537432774, 7),
  (6535335622, 7),
  (6526947014, 7),
  (6702461546, 12),
  (6710850154, 12),
  (6697218666, 12),
  (6701412970, 12),
  (6709801578, 12),
  (6705607274, 12),
  (6708753002, 12),
  (6696170090, 12),
  (6704558698, 12),
  (6870343594, 17),
  (6861954986, 17),
  (6868246442, 17),
  (6876635050, 17),
  (6872440746, 17),
  (6864052138, 17),
  (6866149290, 17),
  (7042474154, 22),
  (7029891242, 22),
  (7038279850, 22),
  (7041425578, 22),
  (7033036970, 22),
  (7037231274, 22),
  (7045619882, 22),
  (7044571306, 22),
  (7036182698, 22),
  (7227401047, 8),
  (7214818135, 8),
  (7223206743, 8),
  (7217963863, 8),
  (7226352471, 8),
  (7221109591, 8),
  (7390311760, 13),
  (7384020304, 13),
  (7392408912, 13),
  (7396603216, 13),
  (7387166032, 13),
  (7395554640, 13),
  (7391360336, 13),
  (7393457488, 13),
  (7385068880, 13),
  (7407261016, 18),
  (7398872408, 18),
  (7400969560, 18),
  (7409358168, 18),
  (7413552472, 18),
  (7403066712, 18),
  (7414601048, 18),
  (7406212440, 18),
  (7412503896, 18),
  (7405163864, 18),
  (7591996057, 4),
  (7583607449, 4),
  (7598287513, 4),
  (7589898905, 4),
  (7596190361, 4),
  (7586753177, 4),
  (7595141785, 4),
  (7778293215, -10),
  (7769904607, -10),
  (7776196063, -10),
  (7782487519, -10),
  (7779341791, -10),
  (7770953183, -10),
  (7950390336, -5),
  (7937807424, -5),
  (7946196032, -5),
  (7944098880, -5),
  (7935710272, -5),
  (7939904576, -5),
  (7942001728, -5),
  (8106759905, 0),
  (8110954209, 0),
  (8119342817, 0),
  (8115148513, 0),
  (8116197089, 0),
  (8103614177, 0),
  (8112002785, 0),
  (8118294241, 0),
  (8109905633, 0),
  (8300176487, -14),
  (8291787879, -14),
  (8301225063, -14),
  (8288642151, -14),
  (8297030759, -14),
  (8294933607, -14),
  (8313814712, -9),
  (8309620408, -9),
  (8318009016, -9),
  (8312766136, -9),
  (8306474680, -9),
  (8314863288, -9),
  (8319057592, -9),
  (8315911864, -9),
  (8307523256, -9),
  (8486814349, -4),
  (8488911501, -4),
  (8480522893, -4),
  (8481571469, -4),
  (8473182861, -4),
  (8475280013, -4),
  (8483668621, -4),
  (8487862925, -4),
  (8477377165, -4),
  (8479474317, -4),
  (38454996, 1),
  (34260692, 1),
  (42649300, 1),
  (47892180, 1),
  (35309268, 1),
  (43697876, 1),
  (40552148, 1),
  (48940756, 1),
  (44746452, 1),
  (36357844, 1),
  (49989332, 1),
  (41600724, 1),
  (217737814, 6),
  (209349206, 6),
  (203057750, 6),
  (211446358, 6),
  (215640662, 6),
  (206203478, 6),
  (204106326, 6),
  (212494934, 6),
  (216689238, 6),
  (208300630, 6),
  (202009174, 6),
  (210397782, 6),
  (369863634, 11),
  (378252242, 11),
  (371960786, 11),
  (380349394, 11),
  (384543698, 11),
  (374057938, 11),
  (385592274, 11),
  (377203666, 11),
  (376155090, 11),
  (370912210, 11),
  (379300818, 11),
  (383495122, 11),
  (538486879, 16),
  (546875487, 16),
  (551069791, 16),
  (543729759, 16),
  (552118367, 16),
  (547924063, 16),
  (539535455, 16),
  (553166943, 16),
  (544778335, 16),
  (537438303, 16),
  (545826911, 16),
  (541632607, 16),
  (727406978, 2),
  (735795586, 2),
  (731601282, 2),
  (723212674, 2),
  (725309826, 2),
  (733698434, 2),
  (737892738, 2),
  (902385350, 7),
  (893996742, 7),
  (904482502, 7),
  (891899590, 7),
  (900288198, 7),
  (898191046, 7),
  (889802438, 7),
  (914322026, 12),
  (922710634, 12),
  (909079146, 12),
  (913273450, 12),
  (921662058, 12),
  (917467754, 12),
  (920613482, 12),
  (908030570, 12),
  (916419178, 12),
  (1082204074, 17),
  (1073815466, 17),
  (1080106922, 17),
  (1088495530, 17),
  (1084301226, 17),
  (1075912618, 17),
  (1078009770, 17),
  (1254334634, 22),
  (1241751722, 22),
  (1250140330, 22),
  (1253286058, 22),
  (1244897450, 22),
  (1249091754, 22),
  (1257480362, 22),
  (1256431786, 22),
  (1248043178, 22),
  (1439261527, 8),
  (1426678615, 8),
  (1435067223, 8),
  (1429824343, 8),
  (1438212951, 8),
  (1432970071, 8),
  (1602172240, 13),
  (1595880784, 13),
  (1604269392, 13),
  (1608463696, 13),
  (1599026512, 13),
  (1607415120, 13),
  (1603220816, 13),
  (1605317968, 13),
  (1596929360, 13),
  (1770116440, 18),
  (1761727832, 18),
  (1763824984, 18),
  (1772213592, 18),
  (1776407896, 18),
  (1765922136, 18),
  (1777456472, 18),
  (1769067864, 18),
  (1775359320, 18),
  (1768019288, 18),
  (1954851481, 4),
  (1946462873, 4),
  (1961142937, 4),
  (1952754329, 4),
  (1959045785, 4),
  (1949608601, 4),
  (1957997209, 4),
  (1990153695, -10),
  (1981765087, -10),
  (1988056543, -10),
  (1994347999, -10),
  (1991202271, -10),
  (1982813663, -10),
  (2162250816, -5),
  (2149667904, -5),
  (2158056512, -5),
  (2155959360, -5),
  (2147570752, -5),
  (2151765056, -5),
  (2153862208, -5),
  (2318620385, 0),
  (2322814689, 0),
  (2331203297, 0),
  (2327008993, 0),
  (2328057569, 0),
  (2315474657, 0),
  (2323863265, 0),
  (2330154721, 0),
  (2512036967, -14),
  (2503648359, -14),
  (2513085543, -14),
  (2500502631, -14),
  (2508891239, -14),
  (2676670136, -9),
  (2672475832, -9),
  (2680864440, -9),
  (2675621560, -9),
  (2669330104, -9),
  (2677718712, -9),
  (2681913016, -9),
  (2849669773, -4),
  (2851766925, -4),
  (2843378317, -4),
  (2844426893, -4),
  (2836038285, -4),
  (2838135437, -4),
  (2840232589, -4),
  (3008022228, 1),
  (3003827924, 1),
  (3012216532, 1),
  (3017459412, 1),
  (3004876500, 1),
  (3013265108, 1),
  (3010119380, 1),
  (3018507988, 1),
  (3019556564, 1),
  (3011167956, 1),
  (3036310102, 6),
  (3027921494, 6),
  (3021630038, 6),
  (3030018646, 6),
  (3034212950, 6),
  (3024775766, 6),
  (3022678614, 6),
  (3020581462, 6),
  (3028970070, 6),
  (3188435922, 11),
  (3196824530, 11),
  (3203115986, 11),
  (3192630226, 11),
  (3204164562, 11),
  (3195775954, 11),
  (3194727378, 11),
  (3189484498, 11),
  (3197873106, 11),
  (3202067410, 11),
  (3357059167, 16),
  (3365447775, 16),
  (3369642079, 16),
  (3358107743, 16),
  (3371739231, 16),
  (3363350623, 16),
  (3356010591, 16),
  (3364399199, 16),
  (3360204895, 16),
  (3554367874, 2),
  (3550173570, 2),
  (3541784962, 2),
  (3543882114, 2),
  (3552270722, 2),
  (3556465026, 2),
  (3723054790, 7),
  (3710471878, 7),
  (3718860486, 7),
  (3716763334, 7),
  (3708374726, 7),
  (3878646378, 12),
  (3882840682, 12),
  (3891229290, 12),
  (3887034986, 12),
  (3890180714, 12),
  (3877597802, 12),
  (3885986410, 12),
  (4049674154, 17),
  (4058062762, 17),
  (4053868458, 17),
  (4045479850, 17),
  (4047577002, 17),
  (4222853290, 22),
  (4214464682, 22),
  (4218658986, 22),
  (4227047594, 22),
  (4225999018, 22),
  (4217610410, 22),
  (4248396631, 8),
  (4256785239, 8),
  (4251542359, 8),
  (4417598800, 13),
  (4425987408, 13),
  (4421793104, 13),
  (4423890256, 13),
  (4415501648, 13),
  (4596028760, 18),
  (4587640152, 18),
  (4593931608, 18),
  (4586591576, 18),
  (4768180889, 4),
  (4776569497, 4),
  (4960769503, -10),
  (4952380895, -10),
  (5123429440, -5)]

def ringBit (τ j : Nat) : Bool := (orbRows.getD τ 0).testBit j

theorem ring_table : ∀ τ, τ < 57 → ∀ j, j < 9 →
    ringBit ((τ + 1) % 57) ((j + 1) % 9) = rule (ringBit τ ((j + 1) % 9)) (ringBit τ j) (ringBit τ ((j + 8) % 9)) := by
  decide

/-- The background at alignment `(0, 0)`: `E t x` is the ring orbit's row `t mod 57` at diagonal index `(t - x) mod 9`. -/
def E (t : Nat) (x : Int) : Bool := ringBit (t % 57) (((t : Int) - x) % 9).toNat

theorem E_rule : IsR30Z E := by
  intro t x
  have h := ring_table (t % 57) (Nat.mod_lt _ (by decide)) (((t : Int) - x) % 9).toNat (by omega)
  unfold E
  have e1 : (t + 1) % 57 = (t % 57 + 1) % 57 := by omega
  have e2 : ((((t + 1 : Nat) : Int) - x) % 9).toNat = ((((t : Int) - x) % 9).toNat + 1) % 9 := by omega
  have e3 : (((t : Int) - (x - 1)) % 9).toNat = ((((t : Int) - x) % 9).toNat + 1) % 9 := by omega
  have e4 : (((t : Int) - (x + 1)) % 9).toNat = ((((t : Int) - x) % 9).toNat + 8) % 9 := by omega
  rw [e1, e2, e3, e4]; exact h

/-- The background at column `A + i`, from the phases `tq = t mod 57` and `dq = (t - A) mod 9`. -/
def refAt (tq dq : Nat) (i : Int) : Bool := ringBit tq (((dq : Int) - i) % 9).toNat

theorem refAt_spec {t tq dq : Nat} {A : Int} (htq : tq = t % 57) (hdq : dq = (((t : Int) - A) % 9).toNat) (i : Int) :
    refAt tq dq i = E t (A + i) := by
  unfold refAt E; subst htq; congr 1; omega

/-- The first `n` values of `f` as bits. -/
def bitsOf (f : Nat → Bool) : Nat → Nat
  | 0 => 0
  | n + 1 => bitsOf f n ||| (if f n then 2 ^ n else 0)

def mask : Nat := 2 ^ 24 - 1

/-- The background's 24 cells right of the anchor, as a bit mask. -/
def refMask (tq dq : Nat) : Nat := bitsOf (fun i => refAt tq dq ((i : Int) + 1)) 24

/-- The window's 24 cells after one tick, from the anchor cell `eA`, the strip `m` and the input `b` beyond it. -/
def restOf (eA b : Bool) (m : Nat) : Nat :=
  (((m <<< 1) ||| (if eA then 1 else 0)) ^^^ (m ||| ((m >>> 1) ||| (if b then 2 ^ 23 else 0)))) &&& mask

/-- The anchor cell after one tick. -/
def n0Of (tq dq m : Nat) : Bool := rule (refAt tq dq (-1)) (refAt tq dq 0) (m.testBit 0)

/-- The anchor retreats when its own cell becomes a mismatch. -/
def retreats (tq dq m : Nat) : Bool := n0Of tq dq m != refAt ((tq + 1) % 57) ((dq + 1) % 9) 0

/-- One tick of the anchored window: the new phases, the new strip and whether the anchor retreats. -/
def step (tq dq m : Nat) (b : Bool) : Nat × Nat × Nat × Bool :=
  if retreats tq dq m then
    ((tq + 1) % 57, (dq + 2) % 9, ((restOf (refAt tq dq 0) b m <<< 1) ||| (if n0Of tq dq m then 1 else 0)) &&& mask, true)
  else ((tq + 1) % 57, (dq + 1) % 9, restOf (refAt tq dq 0) b m, false)

def keyOf (tq dq m : Nat) : Nat := (tq * 9 + dq) * 2 ^ 24 + m

def decode (k : Nat) : Nat × Nat × Nat := (k / 2 ^ 24 / 9, k / 2 ^ 24 % 9, k % 2 ^ 24)

/-- One checked edge: the successor of entry `e` under input `b` is in `cl`, its potential is `e.2 + 19 * motion + 5`, and
its strip differs from the background's. -/
def okStep (cl : List (Nat × Int)) (e : Nat × Int) (b : Bool) : Bool :=
  match cl.lookup (keyOf (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).1
      (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.1
      (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.2.1) with
  | some ψ' => ψ' == e.2 + (if (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.2.2 then -19 else 0) + 5 &&
      (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.2.1 !=
        refMask (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).1 (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.1
  | none => false

/-- Every entry of `cl` steps into `cl` under both inputs. -/
def checkCl (cl : List (Nat × Int)) : Bool := cl.all (fun e => okStep cl e false && okStep cl e true)

theorem closure_ok : checkCl closure = true := by decide +kernel

/-- The start: phases `(15, 3)` and the strip of the inserted edge at time `300`, with potential `0`. -/
def startKey : Nat := 2321766113

theorem start_ok : closure.lookup startKey = some 0 := by decide +kernel

theorem closure_bounds : closure.all (fun e => decide (-14 ≤ e.2) && decide (e.2 ≤ 22)) = true := by decide +kernel

/-! ### Soundness of one tick -/

theorem testBit_ite_pow (c : Bool) (k i : Nat) : (if c then 2 ^ k else 0 : Nat).testBit i = (c && decide (k = i)) := by
  cases c <;> simp [Nat.testBit_two_pow]

theorem testBit_ite_one (c : Bool) (i : Nat) : (if c then 1 else 0 : Nat).testBit i = (c && decide (0 = i)) := by
  have := testBit_ite_pow c 0 i; simpa using this

theorem testBit_mask (i : Nat) : mask.testBit i = decide (i < 24) := by
  unfold mask; exact Nat.testBit_two_pow_sub_one 24 i

theorem and_mask_lt (a : Nat) : a &&& mask < 2 ^ 24 :=
  Nat.lt_of_le_of_lt Nat.and_le_right (by unfold mask; decide)

theorem restOf_bit {eA b : Bool} {m : Nat} (hm : m < 2 ^ 24) {i : Nat} (hi : i < 24) :
    (restOf eA b m).testBit i =
      rule (if i = 0 then eA else m.testBit (i - 1)) (m.testBit i) (if i = 23 then b else m.testBit (i + 1)) := by
  unfold restOf
  rw [Nat.testBit_and, testBit_mask, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_or, Nat.testBit_or,
    Nat.testBit_shiftLeft, Nat.testBit_shiftRight, testBit_ite_one, testBit_ite_pow]
  have h24 : m.testBit 24 = false :=
    Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hm (Nat.pow_le_pow_right (by decide) (by omega)))
  by_cases h0 : i = 0
  · subst h0; simp [rule]
  · have hi0 : ¬ (0 = i) := fun h => h0 h.symm
    by_cases h23 : i = 23
    · subst h23; simp [rule, h24]
    · have hi23 : ¬ (23 = i) := fun h => h23 h.symm
      simp [rule, h0, h23, hi0, hi23, hi, show i ≥ 1 by omega, show 1 + i = i + 1 by omega]

/-- The invariant at time `t`: the background holds at and left of the anchor `A`, the phases are `t`'s and `A`'s, and the
strip `m` holds the 24 cells right of the anchor. -/
def Inv (G : Nat → Int → Bool) (t : Nat) (A : Int) (tq dq m : Nat) : Prop :=
  tq = t % 57 ∧ dq = (((t : Int) - A) % 9).toNat ∧ (∀ x, x ≤ A → G t x = E t x) ∧ m < 2 ^ 24 ∧
    ∀ i, i < 24 → m.testBit i = G t (A + 1 + i)

/-- **One tick is sound.** On a rule-30 evolution of the whole line, the invariant passes to the next tick with the anchor
moved by `step`'s retreat flag, whatever the cell beyond the window is. -/
theorem step_sound {G : Nat → Int → Bool} (hG : IsR30Z G) {t : Nat} {A : Int} {tq dq m : Nat}
    (h : Inv G t A tq dq m) :
    Inv G (t + 1) (if (step tq dq m (G t (A + 25))).2.2.2 then A - 1 else A)
      (step tq dq m (G t (A + 25))).1 (step tq dq m (G t (A + 25))).2.1 (step tq dq m (G t (A + 25))).2.2.1 := by
  obtain ⟨htq, hdq, hE, hm, hs⟩ := h
  have hrefA : refAt tq dq 0 = G t A := by
    rw [refAt_spec htq hdq, show A + 0 = A by omega]; exact (hE A (Int.le_refl A)).symm
  have hrefAm : refAt tq dq (-1) = G t (A - 1) := by
    rw [refAt_spec htq hdq, show A + -1 = A - 1 by omega]; exact (hE (A - 1) (by omega)).symm
  have hcell : ∀ i, i < 24 → (restOf (refAt tq dq 0) (G t (A + 25)) m).testBit i = G (t + 1) (A + 1 + i) := by
    intro i hi
    rw [restOf_bit hm hi, hG]
    have e1 : (if i = 0 then refAt tq dq 0 else m.testBit (i - 1)) = G t (A + 1 + (i : Int) - 1) := by
      by_cases h0 : i = 0
      · subst h0; rw [if_pos rfl, hrefA]; congr 1; omega
      · rw [if_neg h0, hs (i - 1) (by omega)]; congr 1; omega
    have e2 : m.testBit i = G t (A + 1 + (i : Int)) := hs i hi
    have e3 : (if i = 23 then G t (A + 25) else m.testBit (i + 1)) = G t (A + 1 + (i : Int) + 1) := by
      by_cases h23 : i = 23
      · subst h23; rw [if_pos rfl]; congr 1; omega
      · rw [if_neg h23, hs (i + 1) (by omega)]; congr 1; omega
    rw [e1, e2, e3]
  have hn0 : n0Of tq dq m = G (t + 1) A := by
    unfold n0Of
    rw [hrefAm, hrefA, hs 0 (by omega), hG, show A + 1 + ((0 : Nat) : Int) = A + 1 by omega]
  have hnext : refAt ((tq + 1) % 57) ((dq + 1) % 9) 0 = E (t + 1) A := by
    rw [refAt_spec (t := t + 1) (A := A) (by omega) (by omega)]; rw [show A + 0 = A by omega]
  have hleft : ∀ x, x ≤ A - 1 → G (t + 1) x = E (t + 1) x := by
    intro x hx
    rw [hG, E_rule, hE (x - 1) (by omega), hE x (by omega), hE (x + 1) (by omega)]
  unfold step
  by_cases hr : retreats tq dq m = true
  · simp only [hr, ite_true]
    refine ⟨by omega, by omega, fun x hx => hleft x hx, and_mask_lt _, ?_⟩
    intro i hi
    rw [Nat.testBit_and, testBit_mask, Nat.testBit_or, Nat.testBit_shiftLeft, testBit_ite_one]
    by_cases h0 : i = 0
    · subst h0; simp [hn0]
    · have hi0 : ¬ (0 = i) := fun h => h0 h.symm
      simp only [hi0, decide_false, Bool.and_false, Bool.or_false, show i ≥ 1 by omega, decide_true, Bool.true_and,
        show i < 24 from hi]
      rw [hcell (i - 1) (by omega), Bool.and_true]
      congr 1; omega
  · have hr' : retreats tq dq m = false := by simpa using hr
    simp only [hr', Bool.false_eq_true, ite_false]
    have hstay : G (t + 1) A = E (t + 1) A := by
      unfold retreats at hr'; rw [hn0, hnext] at hr'; simpa using hr'
    refine ⟨by omega, by omega, fun x hx => ?_, by unfold restOf; exact and_mask_lt _, fun i hi => hcell i hi⟩
    rcases Int.lt_or_eq_of_le hx with hlt | heq
    · exact hleft x (by omega)
    · rw [heq]; exact hstay

/-! ### The closure carries the invariant for ever -/

theorem lookup_mem : ∀ (l : List (Nat × Int)) (k : Nat) (v : Int), l.lookup k = some v → (k, v) ∈ l
  | [], _, _, h => by simp [List.lookup] at h
  | (k', v') :: l, k, v, h => by
    unfold List.lookup at h
    split at h
    · rename_i hk
      have hv : v' = v := by simpa using h
      have hkk : k = k' := by simpa using hk
      subst hv; subst hkk; exact List.mem_cons_self
    · exact List.mem_cons_of_mem _ (lookup_mem l k v h)

theorem decode_keyOf {tq dq m : Nat} (hdq : dq < 9) (hm : m < 2 ^ 24) : decode (keyOf tq dq m) = (tq, dq, m) := by
  unfold decode keyOf
  have h : (2 : Nat) ^ 24 = 16777216 := rfl
  rw [h] at hm ⊢
  have e1 : ((tq * 9 + dq) * 16777216 + m) / 16777216 = tq * 9 + dq := by omega
  have e2 : ((tq * 9 + dq) * 16777216 + m) % 16777216 = m := by omega
  rw [e1, e2]
  have e3 : (tq * 9 + dq) / 9 = tq := by omega
  have e4 : (tq * 9 + dq) % 9 = dq := by omega
  rw [e3, e4]

theorem okStep_spec {cl : List (Nat × Int)} {e : Nat × Int} {b : Bool} (h : okStep cl e b = true) :
    ∃ ψ', cl.lookup (keyOf (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).1
        (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.1
        (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.2.1) = some ψ' ∧
      ψ' = e.2 + (if (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.2.2 then -19 else 0) + 5 ∧
      (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.2.1 ≠
        refMask (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).1
          (step (decode e.1).1 (decode e.1).2.1 (decode e.1).2.2 b).2.1 := by
  unfold okStep at h
  split at h
  · rename_i ψ' hl
    simp only [Bool.and_eq_true, beq_iff_eq, bne_iff_ne, ne_eq] at h
    exact ⟨ψ', hl, h.1, h.2⟩
  · exact absurd h (by simp)

theorem checkCl_spec {cl : List (Nat × Int)} (hok : checkCl cl = true) {k : Nat} {ψ : Int} (hk : cl.lookup k = some ψ)
    (b : Bool) : okStep cl (k, ψ) b = true := by
  unfold checkCl at hok
  have he := List.all_eq_true.1 hok (k, ψ) (lookup_mem _ _ _ hk)
  simp only [Bool.and_eq_true] at he
  cases b
  · exact he.1
  · exact he.2

theorem step_dq_lt (tq dq m : Nat) (b : Bool) : (step tq dq m b).2.1 < 9 := by
  unfold step; split
  · exact Nat.mod_lt _ (by decide)
  · exact Nat.mod_lt _ (by decide)

/-- **The anchored law, for any checked list.** From a state of `cl` with potential `ψ0` at time `t0` and anchor `A0`, for
every `n` the invariant holds at time `t0 + n` with some anchor `A`, the state is in `cl` with potential
`ψ0 + 19 (A - A0) + 5 n`, and its strip differs from the background's. -/
theorem anchored {cl : List (Nat × Int)} (hok : checkCl cl = true) {G : Nat → Int → Bool} (hG : IsR30Z G)
    {t0 : Nat} {A0 : Int} {tq0 dq0 m0 : Nat} {ψ0 : Int} (hinv : Inv G t0 A0 tq0 dq0 m0) (hdq0 : dq0 < 9)
    (hk : cl.lookup (keyOf tq0 dq0 m0) = some ψ0) (hne0 : m0 ≠ refMask tq0 dq0) :
    ∀ n : Nat, ∃ A : Int, ∃ tq dq m : Nat, ∃ ψ : Int, Inv G (t0 + n) A tq dq m ∧ dq < 9 ∧
      cl.lookup (keyOf tq dq m) = some ψ ∧ ψ = ψ0 + 19 * (A - A0) + 5 * (n : Int) ∧ m ≠ refMask tq dq := by
  intro n
  induction n with
  | zero =>
    exact ⟨A0, tq0, dq0, m0, ψ0, hinv, hdq0, hk, by omega, hne0⟩
  | succ n ih =>
    obtain ⟨A, tq, dq, m, ψ, hI, hdq, hl, hψ, -⟩ := ih
    have hdec : decode (keyOf tq dq m) = (tq, dq, m) := decode_keyOf hdq hI.2.2.2.1
    have hc := okStep_spec (checkCl_spec hok hl (G (t0 + n) (A + 25)))
    simp only [hdec] at hc
    obtain ⟨ψ', hl', hψ', hne⟩ := hc
    have hs := step_sound hG hI
    refine ⟨if (step tq dq m (G (t0 + n) (A + 25))).2.2.2 then A - 1 else A,
      (step tq dq m (G (t0 + n) (A + 25))).1, (step tq dq m (G (t0 + n) (A + 25))).2.1,
      (step tq dq m (G (t0 + n) (A + 25))).2.2.1, ψ', ?_, step_dq_lt _ _ _ _, hl', ?_, hne⟩
    · rw [show t0 + (n + 1) = t0 + n + 1 by omega]; exact hs
    · rw [hψ', hψ]
      cases (step tq dq m (G (t0 + n) (A + 25))).2.2.2 <;> simp <;> omega

/-! ### Bits of masks -/

theorem testBit_bitsOf (f : Nat → Bool) : ∀ n i, (bitsOf f n).testBit i = (decide (i < n) && f i)
  | 0, i => by simp [bitsOf]
  | n + 1, i => by
    unfold bitsOf
    rw [Nat.testBit_or, testBit_bitsOf f n i, testBit_ite_pow]
    by_cases h : i = n
    · subst h; simp
    · have h' : ¬ n = i := fun e => h e.symm
      by_cases hi : i < n
      · simp [hi, show i < n + 1 by omega, h']
      · simp [hi, show ¬ i < n + 1 by omega, h']

theorem bitsOf_lt (f : Nat → Bool) : ∀ n, bitsOf f n < 2 ^ n
  | 0 => by simp [bitsOf]
  | n + 1 => by
    unfold bitsOf
    have ih := bitsOf_lt f n
    have h1 : bitsOf f n < 2 ^ (n + 1) := Nat.lt_of_lt_of_le ih (Nat.pow_le_pow_right (by decide) (by omega))
    have h2 : (if f n then 2 ^ n else 0) < 2 ^ (n + 1) := by
      split
      · exact Nat.pow_lt_pow_right (by decide) (by omega)
      · exact Nat.two_pow_pos _
    exact Nat.or_lt_two_pow h1 h2

/-- A strip that differs from the background's mask holds a mismatch with the background inside the window. -/
theorem mismatch_of_ne {G : Nat → Int → Bool} {t : Nat} {A : Int} {tq dq m : Nat} (h : Inv G t A tq dq m)
    (hne : m ≠ refMask tq dq) : ∃ x, A < x ∧ x ≤ A + 24 ∧ G t x ≠ E t x := by
  obtain ⟨htq, hdq, -, hm, hs⟩ := h
  have : ∃ i, m.testBit i ≠ (refMask tq dq).testBit i := by
    apply Classical.byContradiction
    intro hc
    apply hne
    apply Nat.eq_of_testBit_eq
    intro i
    apply Classical.byContradiction
    intro hi
    exact hc ⟨i, hi⟩
  obtain ⟨i, hi⟩ := this
  have hi24 : i < 24 := by
    apply Classical.byContradiction
    intro hge
    have h1 : m.testBit i = false := Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hm (Nat.pow_le_pow_right (by decide) (by omega)))
    have h2 : (refMask tq dq).testBit i = false := by unfold refMask; rw [testBit_bitsOf]; simp [show ¬ i < 24 by omega]
    exact hi (by rw [h1, h2])
  refine ⟨A + 1 + i, by omega, by omega, ?_⟩
  rw [← hs i hi24]
  unfold refMask at hi
  rw [testBit_bitsOf, refAt_spec htq hdq] at hi
  simpa [hi24, show A + ((i : Int) + 1) = A + 1 + i by omega] using hi

/-! ### The inserted edge on the ring background -/

/-- The row at time `0`: the background left of `0`, a black cell at `0`, white to the right. -/
def initRow (x : Int) : Bool := if x < 0 then E 0 x else decide (x = 0)

/-- Its rule-30 evolution on the whole line. -/
def Gedge : Nat → Int → Bool
  | 0, x => initRow x
  | t + 1, x => rule (Gedge t (x - 1)) (Gedge t x) (Gedge t (x + 1))

theorem Gedge_isR30 : IsR30Z Gedge := fun _ _ => rfl

/-- Light cone: the columns `x < -t` are still the background. -/
theorem Gedge_left : ∀ t : Nat, ∀ x : Int, x + t < 0 → Gedge t x = E t x := by
  intro t
  induction t with
  | zero => intro x hx; show initRow x = _; unfold initRow; simp [show x < 0 by omega]
  | succ t ih =>
    intro x hx
    show rule (Gedge t (x - 1)) (Gedge t x) (Gedge t (x + 1)) = _
    rw [ih (x - 1) (by omega), ih x (by omega), ih (x + 1) (by omega), ← E_rule]

/-- Whole-row step on bit masks: bit `i` is column `lo + i`. -/
def stepN (a : Nat) : Nat := (a <<< 1) ^^^ (a ||| (a >>> 1))

theorem stepN_bit (a i : Nat) (hi : 1 ≤ i) :
    (stepN a).testBit i = rule (a.testBit (i - 1)) (a.testBit i) (a.testBit (i + 1)) := by
  unfold stepN
  rw [Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft, Nat.testBit_shiftRight]
  simp [show i ≥ 1 from hi, show 1 + i = i + 1 by omega, rule]

def lo : Int := -700

/-- The edge's row on `x = -700 .. 0`; white beyond. -/
def row0 : Nat := bitsOf (fun i => initRow (lo + i)) 701

def rowAt : Nat → Nat
  | 0 => row0
  | t + 1 => stepN (rowAt t)

theorem row0_spec : ∀ i, row0.testBit i = Gedge 0 (lo + i) := by
  intro i
  show _ = initRow (lo + i)
  unfold row0; rw [testBit_bitsOf]
  by_cases hi : i < 701
  · simp [hi]
  · simp only [hi, decide_false, Bool.false_and]
    unfold initRow lo
    simp [show ¬ (-700 + (i : Int) < 0) by omega, show ¬ (-700 + (i : Int) = 0) by omega]

theorem rowAt_spec : ∀ t i, t ≤ i → (rowAt t).testBit i = Gedge t (lo + i) := by
  intro t
  induction t with
  | zero => intro i _; exact row0_spec i
  | succ t ih =>
    intro i hi
    show (stepN (rowAt t)).testBit i = rule (Gedge t (lo + i - 1)) (Gedge t (lo + i)) (Gedge t (lo + i + 1))
    rw [stepN_bit _ _ (by omega), ih _ (by omega), ih _ (by omega), ih _ (by omega)]
    rw [show lo + ((i - 1 : Nat) : Int) = lo + (i : Int) - 1 by omega,
      show lo + ((i + 1 : Nat) : Int) = lo + (i : Int) + 1 by omega]

/-- The start check at `t = 300`: columns `-400 .. -72` are the background, and columns `-71 .. -48` are the strip of
`startKey`, which differs from the background's. -/
def entryOK : Bool :=
  let r := rowAt 300
  (List.range 229).all (fun j => r.testBit (400 + j) == E 300 (lo + ((400 + j : Nat) : Int))) &&
  (List.range 24).all (fun j => r.testBit (629 + j) == (startKey % 2 ^ 24).testBit j) &&
  (startKey % 2 ^ 24 != refMask 15 3) && (keyOf 15 3 (startKey % 2 ^ 24) == startKey)

theorem entry_ok : entryOK = true := by decide +kernel

theorem entry_inv : Inv Gedge 300 (-72) 15 3 (startKey % 2 ^ 24) ∧ startKey % 2 ^ 24 ≠ refMask 15 3 ∧
    keyOf 15 3 (startKey % 2 ^ 24) = startKey := by
  have h := entry_ok
  unfold entryOK at h
  simp only [Bool.and_eq_true, List.all_eq_true, List.mem_range, beq_iff_eq, bne_iff_ne, ne_eq] at h
  obtain ⟨⟨⟨hrow, hstrip⟩, hne⟩, hkey⟩ := h
  refine ⟨⟨by decide, by decide, fun x hx => ?_, Nat.mod_lt _ (by decide), fun i hi => ?_⟩, hne, hkey⟩
  · by_cases hlt : x + 300 < 0
    · exact Gedge_left 300 x (by omega)
    · have e := hrow (x + 300).toNat (by omega)
      rw [rowAt_spec 300 _ (by omega)] at e
      rw [show lo + ((400 + (x + 300).toNat : Nat) : Int) = x by unfold lo; omega] at e
      exact e
  · have e := hstrip i hi
    rw [rowAt_spec 300 _ (by omega)] at e
    have hx : lo + ((629 + i : Nat) : Int) = -72 + 1 + (i : Int) := by unfold lo; omega
    rw [hx] at e
    exact e.symm

/-- **The front law of the inserted edge on the ring background `100100000` (temporal period 57).** For every `t ≥ 300`
there is an anchor `A` with the background intact at and left of `A`, a mismatch within the 24 cells right of it, and
`-14 ≤ 19 (A + 72) + 5 (t - 300) ≤ 22`. So the leftmost difference moves left at exactly `5/19` cell per tick. -/
theorem edge_law : ∀ t : Nat, 300 ≤ t → ∃ A : Int, (∀ x, x ≤ A → Gedge t x = E t x) ∧
    (∃ x, A < x ∧ x ≤ A + 24 ∧ Gedge t x ≠ E t x) ∧
    -14 ≤ 19 * (A + 72) + 5 * ((t : Int) - 300) ∧ 19 * (A + 72) + 5 * ((t : Int) - 300) ≤ 22 := by
  intro t ht
  obtain ⟨hinv, hne, hkey⟩ := entry_inv
  have hk : closure.lookup (keyOf 15 3 (startKey % 2 ^ 24)) = some 0 := by rw [hkey]; exact start_ok
  obtain ⟨A, tq, dq, m, ψ, hI, -, hl, hψ, hne'⟩ :=
    anchored closure_ok Gedge_isR30 hinv (by decide) hk hne (t - 300)
  have hb := List.all_eq_true.1 closure_bounds _ (lookup_mem _ _ _ hl)
  simp only [Bool.and_eq_true, decide_eq_true_eq] at hb
  rw [show 300 + (t - 300) = t by omega] at hI
  refine ⟨A, hI.2.2.1, mismatch_of_ne hI hne', ?_, ?_⟩ <;> push_cast [show ((t - 300 : Nat) : Int) = (t : Int) - 300 by omega] at hψ <;> omega

end Ruliology.CellularAutomata.Rule30MovingWall
