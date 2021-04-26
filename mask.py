import bpy
import pdb

bpy.ops.wm.open_mainfile(filepath='./base_scene.blend')
bpy.context.scene.use_nodes = True
tree = bpy.context.scene.node_tree

# args
render_args = bpy.context.scene.render
render_args.engine = 'CYCLES'
render_args.resolution_x = 480
render_args.resolution_y = 320
render_args.resolution_percentage = 100
render_args.tile_x = 256
render_args.tile_y = 256
render_args.filepath = 'test.png'
bpy.data.scenes[0].render.engine = "CYCLES"


# prev = bpy.context.area.type
# bpy.context.area.type = 'NODE_EDITOR'

# area = bpy.context.area

# clear default nodes
# for node in tree.nodes:
#         tree.nodes.remove(node)
# create a new cube
bpy.ops.mesh.primitive_cube_add(location=(0,0,0), radius=1.0)

# newly created cube will be automatically selected
cube = bpy.context.selected_objects[0]
# change name
cube.name = "Cube1"

bpy.ops.mesh.primitive_cube_add(location=(2,2,0), radius=0.5)

# newly created cube will be automatically selected
cube = bpy.context.selected_objects[0]
# change name
cube.name = "Cube2"

render = tree.nodes['Render Layers']
links = tree.links

output_node = bpy.context.scene.node_tree.nodes.new('CompositorNodeOutputFile')
output_node.base_path = "./tmp/"
# link = links.new(render.outputs["Image"], output_node.inputs[0])

i = 0

# mask_node = bpy.context.scene.node_tree.nodes.new('CompositorNodeIDMask')
# mask_node.index = 0
# link = links.new(render.outputs["IndexOB"], mask_node.inputs["ID value"])
# link = links.new(mask_node.outputs[0], output_node.inputs[0])
for obj in bpy.data.objects:
    # if name in obj.name:
    if obj.name == 'Camera' or 'Lamp' in obj.name or obj.name in ['Area', 'Empty', 'Ground']: continue
    print (obj.name)
    i += 1
    obj.pass_index = i
    mask_node = bpy.context.scene.node_tree.nodes.new('CompositorNodeIDMask')
    mask_node.index = i
    link = links.new(render.outputs["IndexOB"], mask_node.inputs["ID value"])
    output_node.layer_slots.new(str(i))
    link = links.new(mask_node.outputs[0], output_node.inputs[i])
    # obs.append(obj)
    #ctx['active_object'] = obj
    # else:
    #   obj.hide_render = True
# pdb.set_trace()
bpy.ops.render.render(write_still=False)
