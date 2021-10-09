import numpy as np
import pyvista as pv
from torus_three_points.main import torusThreePoints


def clifford(beta, theta, phi):
    cosphi = np.cos(phi)
    sinphi = np.sin(phi)
    d = 1 - np.sin(beta) * sinphi
    return np.array(
        [
            np.cos(theta + beta) * cosphi / d,
            np.sin(theta + beta) * cosphi / d,
            np.cos(beta) * sinphi / d,
        ]
    )


def tripletOnCircle(theta, phi):
    return [clifford(0, theta, phi), clifford(2, theta, phi), clifford(4, theta, phi)]


nTori = 30
_theta_ = np.linspace(0, 2 * np.pi, nTori + 1)[0:nTori]

phi = 1

r = 0.1

plotter = pv.Plotter()

for theta in _theta_:
    pts = tripletOnCircle(theta, phi)
    torusThreePoints(
          plotter, pts[0], pts[1], pts[2], r,
          color="orange", specular=0.9, smooth_shading=True
    )
plotter.show()    

# poetry run python
#  exec(open("examples/example4.py").read())
