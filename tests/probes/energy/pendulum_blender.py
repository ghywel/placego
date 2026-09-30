"""ENERGY-TRANSFER.md 1.4 in simulation, the render: a pendulum whose energy must not move.

    blender --background --factory-startup --python pendulum_blender.py -- <outdir> [theta0_deg=30] [frames=96]

Side view, orthographic, 1280x720, 24 fps: image X right, Y down; world x = X / 100, world z = -Y / 100. A bob
(R 60 px) on an invisible rod from the pivot (640, 100), L = 400 px, in EXACT simple-pendulum motion (RK4, 100 steps a
frame): theta'' = -(g / L) sin theta, g = 3.05 px/frame^2 (a 72-frame period at small amplitude). The bob turns with
the swing (a rigid pendulum), so its texture turns too. The bob is an emission noise ramped 0.4-1.0; the wall behind
is emission ramped 0-0.3, so the bob segments cleanly. The truth (states.json): per frame the bob's centre, its speed
L theta', its height above the lowest point L (1 - cos theta), and E / m = 1/2 v^2 + g h, constant.
"""
import json
import math
import sys

import bpy

argv = sys.argv[sys.argv.index("--") + 1:]
out = argv[0]
th0 = math.radians(float(argv[1]) if len(argv) > 1 else 30.0)
N = int(argv[2]) if len(argv) > 2 else 96
PX, PY, L, RB, G = 640.0, 100.0, 400.0, 60.0, 3.05

# the physics: RK4 on (theta, omega)
def acc(th): return -(G / L) * math.sin(th)
th, om, states, sub = th0, 0.0, [], 100
for k in range(N):
    states.append({"k": k, "theta": th, "omega": om, "c": [PX + L * math.sin(th), PY + L * math.cos(th)],
                   "speed": abs(L * om), "h": L * (1 - math.cos(th)), "E": 0.5 * (L * om) ** 2 + G * L * (1 - math.cos(th))})
    dt = 1.0 / sub
    for _ in range(sub):
        k1t, k1o = om, acc(th)
        k2t, k2o = om + 0.5 * dt * k1o, acc(th + 0.5 * dt * k1t)
        k3t, k3o = om + 0.5 * dt * k2o, acc(th + 0.5 * dt * k2t)
        k4t, k4o = om + dt * k3o, acc(th + dt * k3t)
        th += dt / 6 * (k1t + 2 * k2t + 2 * k3t + k4t); om += dt / 6 * (k1o + 2 * k2o + 2 * k3o + k4o)
json.dump({"g": G, "L": L, "R": RB, "pivot": [PX, PY], "states": states}, open(out.rstrip("/") + "/../pendulum.json", "w"))

sc = bpy.context.scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o, do_unlink=True)
sc.render.engine = "BLENDER_EEVEE"
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 1280, 720, 100
sc.render.fps = 24; sc.frame_start, sc.frame_end = 1, N; sc.render.use_motion_blur = False
sc.render.image_settings.file_format = "PNG"; sc.render.image_settings.color_depth = "16"
sc.render.image_settings.color_mode = "RGB"; sc.view_settings.view_transform = "Standard"
sc.world = bpy.data.worlds.new("black"); sc.world.use_nodes = True
sc.world.node_tree.nodes["Background"].inputs["Color"].default_value = (0, 0, 0, 1)
cam = bpy.data.cameras.new("cam"); cam.type = "ORTHO"; cam.ortho_scale = 12.8
co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co)
co.location = (6.4, -10, -3.6); co.rotation_euler = (math.radians(90), 0, 0); sc.camera = co


def emission(name, scale, lo_col, hi_col, lo, hi):
    mat = bpy.data.materials.new(name); mat.use_nodes = True; nt = mat.node_tree; nt.nodes.clear()
    tc = nt.nodes.new("ShaderNodeTexCoord"); nz = nt.nodes.new("ShaderNodeTexNoise")
    nz.inputs["Scale"].default_value = scale; nz.inputs["Detail"].default_value = 6.0
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    e0, e1 = ramp.color_ramp.elements[0], ramp.color_ramp.elements[1]
    e0.position, e1.position = lo, hi; e0.color = (lo_col, lo_col, lo_col, 1); e1.color = (hi_col, hi_col, hi_col, 1)
    em = nt.nodes.new("ShaderNodeEmission"); em.inputs["Strength"].default_value = 1.0
    o = nt.nodes.new("ShaderNodeOutputMaterial")
    nt.links.new(tc.outputs["Object"], nz.inputs["Vector"]); nt.links.new(nz.outputs["Fac"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], em.inputs["Color"]); nt.links.new(em.outputs["Emission"], o.inputs["Surface"])
    return mat


bpy.ops.mesh.primitive_plane_add(size=40, location=(6.4, 3.0, -3.6), rotation=(math.radians(90), 0, 0))
bpy.context.active_object.data.materials.append(emission("wall", 0.6, 0.0, 0.3, 0.3, 0.7))
bpy.ops.mesh.primitive_uv_sphere_add(segments=128, ring_count=64, radius=RB / 100.0, location=(0, 0, 0))
bob = bpy.context.active_object; bpy.ops.object.shade_smooth()
bob.data.materials.append(emission("bob", 3.0, 0.4, 1.0, 0.35, 0.65))
for s in states:
    X, Y = s["c"]
    bob.location = (X / 100.0, 0.0, -Y / 100.0); bob.rotation_euler = (0.0, -s["theta"], 0.0)
    bob.keyframe_insert("location", frame=s["k"] + 1); bob.keyframe_insert("rotation_euler", frame=s["k"] + 1)
sc.render.filepath = out.rstrip("/") + "/f"
bpy.ops.render.render(animation=True)
print(f"BRIDGE rendered {N} frames of the pendulum -> {out}")
