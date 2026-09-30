"""ENERGY-TRANSFER.md 2.3, the render: a textured ball spinning in place, headless Blender (EEVEE on Metal).

    blender --background --factory-startup --python sphere_blender.py -- <outdir> <axis: vertical|sight|roll|tilt|persp> [deg_per_frame=2]

"roll" (2.3 proper): the camera looks straight DOWN (world x -> image right, world y -> image up), and the ball rolls
along +x at v = 5 px/frame (0.02 units/frame at 250 px a unit), spinning about world y at omega = v/R = 0.02
rad/frame: an axis in the image plane, the top of the ball moving at 2v. deg_per_frame is ignored.
"tilt": spin about world (0, 1, 1)/sqrt 2, halfway between the line of sight and vertical (axis-angle, fixed axis).
"persp": the vertical spin through a PERSPECTIVE camera (50 mm on a 36 mm sensor), 7.11 units back, which puts
the unit ball at about 250 px radius in the frame centre.

1280x720 at 24 fps, 48 frames, black ground. An orthographic camera looks along world +y, so world x is image right,
world z is image up and world y is depth. A unit sphere at the origin, its radius 250 px on screen (ortho scale 5.12
units across 1280 px). Its surface is an EMISSION shader driven by a high-contrast noise texture in object
coordinates, so the pattern turns with the ball and the brightness does not change with the angle to the light.
It spins at a constant deg_per_frame about world z ("vertical": an axis in the image plane, the case curl cannot
see) or about world y ("sight": the line of sight, the control), with linear keyframes. No motion blur. 16-bit PNGs.
"""
import math
import sys

import bpy

argv = sys.argv[sys.argv.index("--") + 1:]
out, axis = argv[0], argv[1]
deg = float(argv[2]) if len(argv) > 2 else 2.0
N = 48

sc = bpy.context.scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o, do_unlink=True)
sc.render.engine = "BLENDER_EEVEE"
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 1280, 720, 100
sc.render.fps = 24
sc.frame_start, sc.frame_end = 1, N
sc.render.use_motion_blur = False
sc.render.image_settings.file_format = "PNG"
sc.render.image_settings.color_depth = "16"
sc.render.image_settings.color_mode = "RGB"
sc.view_settings.view_transform = "Standard"
sc.world = bpy.data.worlds.new("black"); sc.world.use_nodes = True
sc.world.node_tree.nodes["Background"].inputs["Color"].default_value = (0, 0, 0, 1)

cam = bpy.data.cameras.new("cam")
if axis == "persp":
    cam.type = "PERSP"; cam.lens = 50.0; cam.sensor_width = 36.0; cam.sensor_fit = "HORIZONTAL"
else:
    cam.type = "ORTHO"; cam.ortho_scale = 5.12
co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co)
if axis == "roll":
    co.location = (0, 0, 10); co.rotation_euler = (0, 0, 0)        # looking down -z, image up = world +y
else:
    co.location = (0, -7.11 if axis == "persp" else -10, 0); co.rotation_euler = (math.radians(90), 0, 0)
sc.camera = co

bpy.ops.mesh.primitive_uv_sphere_add(segments=128, ring_count=64, radius=1.0, location=(0, 0, 0))
ball = bpy.context.active_object
bpy.ops.object.shade_smooth()
mat = bpy.data.materials.new("tex"); mat.use_nodes = True
nt = mat.node_tree; nt.nodes.clear()
tc = nt.nodes.new("ShaderNodeTexCoord")
nz = nt.nodes.new("ShaderNodeTexNoise"); nz.inputs["Scale"].default_value = 4.0; nz.inputs["Detail"].default_value = 6.0
ramp = nt.nodes.new("ShaderNodeValToRGB")
ramp.color_ramp.elements[0].position = 0.35; ramp.color_ramp.elements[1].position = 0.65
em = nt.nodes.new("ShaderNodeEmission"); em.inputs["Strength"].default_value = 1.0
outn = nt.nodes.new("ShaderNodeOutputMaterial")
nt.links.new(tc.outputs["Object"], nz.inputs["Vector"])
nt.links.new(nz.outputs["Fac"], ramp.inputs["Fac"])
nt.links.new(ramp.outputs["Color"], em.inputs["Color"])
nt.links.new(em.outputs["Emission"], outn.inputs["Surface"])
ball.data.materials.append(mat)

if axis == "roll":
    V = 0.02                                                     # units/frame = 5 px/frame; omega = V / R, R = 1
    ball.location = (-V * (N - 1) / 2, 0, 0); ball.keyframe_insert("location", frame=1)
    ball.location = (V * (N - 1) / 2, 0, 0); ball.keyframe_insert("location", frame=N)
    ball.rotation_euler = (0, 0, 0); ball.keyframe_insert("rotation_euler", frame=1)
    ball.rotation_euler = (0, V * (N - 1), 0); ball.keyframe_insert("rotation_euler", frame=N)
elif axis == "tilt":
    ball.rotation_mode = "AXIS_ANGLE"; a = 1 / math.sqrt(2)
    ball.rotation_axis_angle = (0.0, 0.0, a, a); ball.keyframe_insert("rotation_axis_angle", frame=1)
    ball.rotation_axis_angle = (math.radians(deg * (N - 1)), 0.0, a, a); ball.keyframe_insert("rotation_axis_angle", frame=N)
else:
    idx = {"vertical": 2, "sight": 1, "persp": 2}[axis]
    ball.rotation_euler = (0, 0, 0); ball.keyframe_insert("rotation_euler", frame=1)
    r = [0.0, 0.0, 0.0]; r[idx] = math.radians(deg * (N - 1)); ball.rotation_euler = r
    ball.keyframe_insert("rotation_euler", frame=N)
ad = ball.animation_data
fcs = getattr(ad.action, "fcurves", None)
if fcs is None:                                      # Blender 5 layered actions
    fcs = [fc for layer in ad.action.layers for strip in layer.strips for bag in strip.channelbags for fc in bag.fcurves]
for fc in fcs:
    for kp in fc.keyframe_points: kp.interpolation = "LINEAR"

sc.render.filepath = out.rstrip("/") + "/f"
bpy.ops.render.render(animation=True)
print(f"BRIDGE rendered {N} frames, axis {axis}, {deg} deg/frame -> {out}")
