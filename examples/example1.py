import numpy as np
import pyvista as pv
from torus_three_points.main import torusThreePoints

plotter = pv.Plotter()

p1 = np.array([0,1,0])
p2 = np.array([0,1,1])
p3 = np.array([1,1,1])
p4 = np.array([2,2,-1])

torusThreePoints(
  plotter, p1, p2, p3, 0.2, show = False, smooth_shading = True, color = "red"
)
torusThreePoints(
  plotter, p1, p2, p4, 0.1, show = True, smooth_shading=True, color = "blue"
)

# poetry run python
#  exec(open("examples/example1.py").read())

