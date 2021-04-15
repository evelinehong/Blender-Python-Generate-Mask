bpy.context.scene.use_nodes = True
tree = bpy.context.scene.node_tree

# prev = bpy.context.area.type
# bpy.context.area.type = 'NODE_EDITOR'

# area = bpy.context.area    

# clear default nodes
# for node in tree.nodes:
#         tree.nodes.remove(node)

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
  i += 1
  obj.pass_index = i
  mask_node = bpy.context.scene.node_tree.nodes.new('CompositorNodeIDMask')
  mask_node.index = i
  link = links.new(render.outputs["IndexOB"], mask_node.inputs["ID value"])
  output_node.layer_slots.new(str(i))
  link = links.new(mask_node.outputs[0], output_node.inputs[i])
  obs.append(obj)
  ctx['active_object'] = obj
  # else:
  #   obj.hide_render = True

bpy.ops.render.render()