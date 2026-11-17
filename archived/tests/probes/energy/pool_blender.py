"""ENERGY-TRANSFER.md 2.4 in simulation, the render: pool_sim.py's states, top-down, headless Blender (EEVEE on Metal).

    blender --background --factory-startup --python pool_blender.py -- <states.json> <outdir>

1280x720, orthographic, looking straight down: world = (X, -Y, -Z) / 100 from the simulation's image frame (X right,
Y down, Z into the table), so the orientation quaternion (w, x, y, z) becomes (w, x, -y, -z). Two unit-0.8 balls
(80 px), each an EMISSION noise texture in object coordinates (so the pattern turns with the ball and brightness does
not change with the angle), on a dim textured table plane (also emission) at the balls' contact height. Every frame
is keyed from the states; no motion blur; 16-bit PNGs.
"""
import json
import sys

import bpy

argv = sys.argv[sys.argv.index("--") + 1:]
st = json.load(open(argv[0])); out = argv[1]
frames = st["frames"]; N = len(frames); Rw = st["R"] / 100.0

sc = bpy.context.scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o, do_unlink=True)
sc.render.engine = "BLENDER_EEVEE"
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 1280, 720, 100
sc.render.fps = 24; sc.frame_start, sc.frame_end = 1, N
sc.render.use_motion_blur = False
sc.render.image_settings.file_format = "PNG"; sc.render.image_settings.color_depth = "16"
sc.render.image_settings.color_mode = "RGB"; sc.view_settings.view_transform = "Standard"
sc.world = bpy.data.worlds.new("black"); sc.world.use_nodes = True
sc.world.node_tree.nodes["Background"].inputs["Color"].default_value = (0, 0, 0, 1)

cam = bpy.data.cameras.new("cam"); cam.type = "ORTHO"; cam.ortho_scale = 12.8
co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co)
co.location = (6.4, -3.6, 10); co.rotation_euler = (0, 0, 0); sc.camera = co


def emission(name, scale, lo, hi, strength):
    mat = bpy.data.materials.new(name); mat.use_nodes = True; nt = mat.node_tree; nt.nodes.clear()
    tc = nt.nodes.new("ShaderNodeTexCoord"); nz = nt.nodes.new("ShaderNodeTexNoise")
    nz.inputs["Scale"].default_value = scale; nz.inputs["Detail"].default_value = 6.0
    ramp = nt.nodes.new("ShaderNodeValToRGB"); ramp.color_ramp.elements[0].position = lo; ramp.color_ramp.elements[1].position = hi
    em = nt.nodes.new("ShaderNodeEmission"); em.inputs["Strength"].default_value = strength
    o = nt.nodes.new("ShaderNodeOutputMaterial")
    nt.links.new(tc.outputs["Object"], nz.inputs["Vector"]); nt.links.new(nz.outputs["Fac"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], em.inputs["Color"]); nt.links.new(em.outputs["Emission"], o.inputs["Surface"])
    return mat


bpy.ops.mesh.primitive_plane_add(size=40, location=(6.4, -3.6, -Rw))
table = bpy.context.active_object; table.data.materials.append(emission("table", 0.6, 0.3, 0.7, 0.3))
balls = {}
for name, scale in (("cue", 3.0), ("obj", 5.5)):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=128, ring_count=64, radius=Rw, location=(0, 0, 0))
    b = bpy.context.active_object; bpy.ops.object.shade_smooth(); b.rotation_mode = "QUATERNION"
    b.data.materials.append(emission(name, scale, 0.35, 0.65, 1.0)); balls[name] = b

for f in frames:
    for name, b in balls.items():
        s_ = f[name]; X, Y = s_["p"]; w, x, y, z = s_["q"]
        b.location = (X / 100.0, -Y / 100.0, 0.0); b.rotation_quaternion = (w, x, -y, -z)
        b.keyframe_insert("location", frame=f["k"] + 1); b.keyframe_insert("rotation_quaternion", frame=f["k"] + 1)

sc.render.filepath = out.rstrip("/") + "/f"
bpy.ops.render.render(animation=True)
print(f"BRIDGE rendered {N} frames of the {st['shot']} shot -> {out}")
