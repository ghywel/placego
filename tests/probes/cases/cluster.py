"""Cluster the 60 proposed ladder cases into distinct MECHANISMS (2026-09-09).

The workflow's own dedup key was a bag of rare words from the mechanism sentence and it merged nothing: 60
proposed, 60 "distinct", so the adversarial stage was asked to verify the same idea three and four times over
and ran out of session budget doing it. Independent agreement across angles is signal, not noise -- it is
recorded here as a vote count rather than thrown away.

Clusters are assigned by hand from the mechanism text. Each cluster keeps the candidate whose construction is
most concrete, and records the others as corroboration.
"""
import json
import os
import pathlib

HERE = pathlib.Path(os.environ.get("NP_SCRATCH", "E:/nframe-project/np-scratch")) / "cases"   # the survey JSON lives with the data
cands = json.loads((HERE / "candidates.json").read_text(encoding="utf-8"))
by_name = {c["name"]: c for c in cands}

# cluster key -> (representative, [also proposed as]) -- the representative is listed first
CLUSTERS = [
    ("divergence / zoom",              ["Z1_zoom_tex_v8", "Z1_zoom_disc_v12", "G1_plane_perspective"]),
    ("pure shear",                     ["Z2_shear_tex_v6", "G1_shear_tex_g040", "Y1_ground_shear"]),
    ("acceleration perpendicular to velocity (orbit)", ["C1_orbit_tex_v16", "X4_orbit_tex_a133", "C1_orbit_tex_a200"]),
    ("orbit plus spin (turn and travel)", ["C2_orbit_spin_v12"]),
    ("curvature and speed both changing", ["C3_ellipse_tex"]),
    ("parallax: two depths, one camera move", ["D3_parallax_v5v17", "C2_parallax_v6_v14"]),
    ("affine flow: a plane turning",    ["Z1_plane_turn"]),
    ("a crease: flow continuous, its derivative not", ["Z2_corner_crease"]),
    ("self-occlusion as a timed event", ["Z3_corner_vanish"]),
    ("rotating sphere, no silhouette change", ["D1_sphere_spin16", "D2_sphere_spin4"]),
    ("constant jerk, acceleration through zero", ["J1_jerk_tex_j025", "A8_jerk_tex_j056"]),
    ("acceleration discontinuity inside a window", ["K1_kink_tex_a067", "A9_accel_flip_tex_a80"]),
    ("motion reversing inside one source interval", ["J5_cusp_mid_tex_v16"]),
    ("a body that stops dead and restarts", ["J2_dwell_tex_v16"]),
    ("sustained sub-pixel velocity",     ["J1_creep_tex_v05", "X7_subpel_diag_v0p5"]),
    ("held cadence: duplicated source frames", ["J3_ontwos_tex_v16"]),
    ("irregular 2-3 telecine cadence",  ["J4_cadence23_tex_v8"]),
    ("brightness constancy violated, geometry still", ["G1_lift_static"]),
    ("continuous fade under motion",    ["G2_fade_tex_v16"]),
    ("illumination moving over a static surface", ["G3_shadow_pan_v12"]),
    ("a static photometric edge capturing real motion", ["G4_shadow_edge_v16"]),
    ("a highlight sliding differently from its surface", ["G5_glint_half_v16"]),
    ("isoluminant colour motion, invisible in luma", ["G6_isolum_v16"]),
    ("a flash firing the cut gate on a non-cut", ["G7_flash_cutgate", "X1_cutbait_tex880_v16"]),
    ("a real cut, hard",                ["T1_cut_hard_x3"]),
    ("a cut the gate cannot see",       ["T2_cut_belowgate"]),
    ("cross-dissolve: two motions, time-varying weights", ["T3_dissolve_12f", "G8_dissolve_2f"]),
    ("superposition: two motions in one pixel", ["C4_superpose_a50"]),
    ("a static occluder in front of motion", ["C1_grille_static_v16", "X5_fence_static_v16"]),
    ("opposed motion with no occlusion and no background", ["C3_seam_opposed_v16", "S1_seam_tex_da133"]),
    ("correspondence at the frame boundary", ["B1_frame_edge_v16"]),
    ("many small movers at once",       ["X2_swarm24_v6", "X3_swarm24_v16"]),
    ("object size against the estimator's fixed footprints", ["G1_sizeladder_v16"]),
    ("feature width against flow precision", ["G2_thingrid_p40_v16", "G3_thingrid_p100_v16"]),
    ("texture lattice at an angle to the sampling grid", ["G4_tex30deg_v16"]),
    ("aperture at an intermediate angle", ["G5_bars45_along_v16"]),
    ("which pyramid level decides, mapped by position", ["G6_chirp_p6to64_v16"]),
    ("scale of reliable structure vs propagation footprint", ["G7_islands_d300_v16"]),
    ("is the search reach a square or a disc", ["X6_reach30_diag"]),
    ("a null at a non-integer texel speed", ["M5_period40_v9"]),
    ("field noise floor against contrast", ["A8_accel_tex_c009"]),
    ("smooth flow reversing inside every match window", ["D1_deform_wave_v4"]),
    ("a boundary with no rigid correspondence", ["F3_fourier_morph"]),
]

seen, out = set(), []
for key, names in CLUSTERS:
    members = [by_name[n] for n in names if n in by_name]
    if not members:
        print(f"  !! cluster '{key}' matched nothing"); continue
    rep = dict(members[0])
    rep["cluster"] = key
    rep["votes"] = len(members)
    rep["also_proposed_as"] = [m["name"] for m in members[1:]]
    if len(members) > 1:
        rep["corroboration"] = " || ".join(f"{m['name']}: {m['mechanism']}" for m in members[1:])
    out.append(rep)
    seen.update(names)

missing = [c["name"] for c in cands if c["name"] not in seen]
assert not missing, f"unclustered candidates: {missing}"
(HERE / "clustered.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
multi = [o for o in out if o["votes"] > 1]
print(f"{len(cands)} candidates -> {len(out)} distinct mechanisms")
print(f"{len(multi)} were proposed independently by more than one angle (that agreement is evidence, not duplication):")
for o in sorted(multi, key=lambda x: -x["votes"]):
    print(f"   {o['votes']}x  {o['cluster']:52s} ({o['name']} + {', '.join(o['also_proposed_as'])})")
hi = sum(1 for o in out if o["value"] == "high")
print(f"\nvalue as proposed: {hi} high, {len(out)-hi} medium or low")
