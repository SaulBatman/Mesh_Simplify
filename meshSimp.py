import numpy as np
import scipy.io as scio
from quad_mesh_simplify import simplify_mesh

#Load the .mat file in which the vertex and face data come from ply file.
#V is a [Number_Vertex, 3] matrix
#F is a [Number_Face, 3] matrix
dataVertex = scio.loadmat('Matrix.mat')
V = dataVertex['V']
print('imported',V)
F = dataVertex['F']
print('imported',F)


#normalize vertices with a scale of 10
V=V*10/(V.max()-V.min())

#Transform your data into available input for simplify_mesh
V = V.astype(np.double)
F = F.astype(np.uint32)
scio.savemat('transformed_V.mat',{'new_V':V})
scio.savemat('transformed_P.mat',{'new_F':F})

# DIY your vertex number
vertices_after_simplification = 100
new_position, new_face = simplify_mesh(V, F, vertices_after_simplification)
print('start simplfying')

#new_position = new_position.astype(np.uint8)
new_face = new_face.astype(np.uint8)

#DIY your need for face features
face = np.zeros((new_face.shape[0],8))
face[0:new_face.shape[0],0:5]=[202,209,238,0,3]
face[0:new_face.shape[0],5:8]=new_face

#save your simplified data in mat file
scio.savemat('new1_V.mat',{'new_V':new_position})
scio.savemat('new1_F.mat',{'new_F':face})
print('success!')

