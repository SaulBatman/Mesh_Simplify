# Mesh_Simplify
Simplify meshes(.ply) with fewer vertices and faces. Tested on Stanford bunny.

Please install numpy, scipy and quad_mesh_simplify:  
```
pip intall numpy
pip install scipy
pip install quad_mesh_simplify
```

if you encounter some error while installing quad_mesh_simplify library, please:  
Tested on Ubuntu & Python 3.7.9  
```
wget https://files.pythonhosted.org/packages/b6/67/db0d559c1e7c6c5d3a49f18cd2f23a200d853e0d59276dcd96e2baf7c3ee/quad_mesh_simplify-1.1.1a-cp37-cp37m-manylinux1_x86_64.whl  
pip install quad_mesh_simplify-1.1.1a-cp37-cp37m-manylinux1_x86_64.whl  
```

Then, please enter the meshSimp.py, DIY your parameters.  

Run:  
```
python meshSimp.py
```

>References:  
>ply format introduction: http://paulbourke.net/dataformats/ply/  
>quad-mesh-simplify 1.1.1https://pypi.org/project/quad-mesh-simplify/#description
