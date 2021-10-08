import numpy as np
import pyvista as pv
from torus_three_points.main import torusThreePoints

# vertices ####
phi = (1 + np.sqrt(5)) / 2
a = 1 / np.sqrt(3)
b = a / phi
c = a * phi

vertices = np.vstack(
    (
        np.array([a, a, a]),
        np.array([a, a, -a]),
        np.array([a, -a, a]),
        np.array([-a, -a, a]),
        np.array([-a, a, -a]),
        np.array([-a, a, a]),
        np.array([0, b, -c]),
        np.array([0, -b, -c]),
        np.array([0, -b, c]),
        np.array([c, 0, -b]),
        np.array([-c, 0, -b]),
        np.array([-c, 0, b]),
        np.array([b, c, 0]),
        np.array([b, -c, 0]),
        np.array([-b, -c, 0]),
        np.array([-b, c, 0]),
        np.array([0, b, c]),
        np.array([a, -a, -a]),
        np.array([c, 0, b]),
        np.array([-a, -a, -a]),
    )
)

# tetrahedra vertices indices ####
tetra1Idxs = np.vstack(
    (
        np.array([16, 13, 1]),
        np.array([16, 10, 13]),
        np.array([10, 1, 13]),
        np.array([10, 16, 1]),
    )
)
tetra2Idxs = np.vstack(
    (
        np.array([17, 0, 3]),
        np.array([17, 4, 0]),
        np.array([4, 17, 3]),
        np.array([4, 3, 0]),
    )
)
tetra3Idxs = np.vstack(
    (
        np.array([18, 5, 14]),
        np.array([18, 6, 5]),
        np.array([18, 14, 6]),
        np.array([6, 14, 5]),
    )
)
tetra4Idxs = np.vstack(
    (
        np.array([2, 12, 11]),
        np.array([2, 7, 12]),
        np.array([7, 11, 12]),
        np.array([11, 7, 2]),
    )
)
tetra5Idxs = np.vstack(
    (
        np.array([19, 15, 9]),
        np.array([19, 8, 15]),
        np.array([8, 9, 15]),
        np.array([19, 9, 8]),
    )
)

plotter = pv.Plotter()

r = 0.05

tetra = tetra1Idxs
for j in range(4):
    p1 = vertices[
        tetra[j, 0],
    ]
    p2 = vertices[
        tetra[j, 1],
    ]
    p3 = vertices[
        tetra[j, 2],
    ]
    torusThreePoints(
        plotter,
        p1,
        p2,
        p3,
        r,
        show=False,
        smooth_shading=True,
        specular=0.8,
        color="blue",
    )

tetra = tetra2Idxs
for j in range(4):
    p1 = vertices[
        tetra[j, 0],
    ]
    p2 = vertices[
        tetra[j, 1],
    ]
    p3 = vertices[
        tetra[j, 2],
    ]
    torusThreePoints(
        plotter,
        p1,
        p2,
        p3,
        r,
        show=False,
        smooth_shading=True,
        specular=0.8,
        color="red",
    )

tetra = tetra3Idxs
for j in range(4):
    p1 = vertices[
        tetra[j, 0],
    ]
    p2 = vertices[
        tetra[j, 1],
    ]
    p3 = vertices[
        tetra[j, 2],
    ]
    torusThreePoints(
        plotter,
        p1,
        p2,
        p3,
        r,
        show=False,
        smooth_shading=True,
        specular=0.8,
        color="green",
    )

tetra = tetra4Idxs
for j in range(4):
    p1 = vertices[
        tetra[j, 0],
    ]
    p2 = vertices[
        tetra[j, 1],
    ]
    p3 = vertices[
        tetra[j, 2],
    ]
    torusThreePoints(
        plotter,
        p1,
        p2,
        p3,
        r,
        show=False,
        smooth_shading=True,
        specular=0.8,
        color="yellow",
    )

tetra = tetra5Idxs
for j in range(4):
    p1 = vertices[
        tetra[j, 0],
    ]
    p2 = vertices[
        tetra[j, 1],
    ]
    p3 = vertices[
        tetra[j, 2],
    ]
    torusThreePoints(
        plotter,
        p1,
        p2,
        p3,
        r,
        show=False,
        smooth_shading=True,
        specular=0.8,
        color="purple",
    )

plotter.show()

# poetry run python
#  exec(open("examples/example2.py").read())
