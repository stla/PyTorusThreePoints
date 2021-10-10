# -*- coding: utf-8 -*-
import numpy as np
import pyvista as pv


def torusMesh(R, r, S=64, s=32, arc=2 * np.pi):
    vertices = np.empty((0, 3))
    faces = np.empty((0), dtype=int)
    for j in range(s + 1):
        v = j / s * 2 * np.pi
        cos_v = np.cos(v)
        sin_v = np.sin(v)
        for i in range(S + 1):
            u = i / S * arc
            vertex = np.array(
                [(R + r * cos_v) * np.cos(u), (R + r * cos_v) * np.sin(u), r * sin_v]
            )
            vertices = np.vstack((vertices, vertex))
    for j in range(s):
        for i in range(S):
            a = (S + 1) * (j + 1) + i
            b = (S + 1) * j + i
            c = (S + 1) * j + i + 1
            d = (S + 1) * (j + 1) + i + 1
            faces = np.concatenate((faces, np.array([3, a, b, d, 3, b, c, d])), axis=0)
    return pv.PolyData(vertices, faces).extract_geometry().clean(tolerance=1e-6)


# plane passing by points p1, p2, p3 #
def plane3pts(p1, p2, p3):
    xcoef = (p1[1] - p2[1]) * (p2[2] - p3[2]) - (p1[2] - p2[2]) * (p2[1] - p3[1])
    ycoef = (p1[2] - p2[2]) * (p2[0] - p3[0]) - (p1[0] - p2[0]) * (p2[2] - p3[2])
    zcoef = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p1[1] - p2[1]) * (p2[0] - p3[0])
    offset = p1[0] * xcoef + p1[1] * ycoef + p1[2] * zcoef
    return np.array([xcoef, ycoef, zcoef, offset])


# center, radius and normal of the circle passing by three points #
def circleCenterAndRadius(p1, p2, p3):
    p12 = (p1 + p2) / 2
    p23 = (p2 + p3) / 2
    v12 = p2 - p1
    v23 = p3 - p2
    plane = plane3pts(p1, p2, p3)
    A = np.column_stack((plane[0:3], v12, v23))
    b = np.array([plane[3], np.vdot(p12, v12), np.vdot(p23, v23)])
    center = np.matmul(np.linalg.inv(np.transpose(A)), b)
    r = np.linalg.norm(p1 - center)
    return dict(center=center, radius=r, normal=plane[0:3])


# transformation matrix #
def transfoMatrix(p1, p2, p3):
    crn = circleCenterAndRadius(p1, p2, p3)
    center = crn["center"]
    radius = crn["radius"]
    normal = crn["normal"]
    measure = np.linalg.norm(normal)
    normal = normal / measure
    s = np.linalg.norm(normal[0:2])  # TODO: case s=0
    u = np.array([normal[1] / s, -normal[0] / s, 0])
    v = np.cross(normal, u)
    m = np.vstack((np.column_stack((u, v, normal, center)), np.array([0, 0, 0, 1])))
    return dict(matrix=m, radius=radius)


# main function #
def torusThreePoints(pvPlotter, p1, p2, p3, r, S=64, s=32, show=False, **kwargs):
    """
    Add a torus to a pyvista plotter region.

    Keywords arguments:
        pvPlotter -- the pyvista plotter region

        p1, p2, p3 -- the three points through which the torus passes

        r -- the minor radius f the torus

        S, s -- controls of the torus mesh

        show -- whether to show the figure

        kwargs -- named arguments passed to `add_mesh`, e.g. color="red"

    """
    tMatrix = transfoMatrix(p1, p2, p3)
    torus = torusMesh(tMatrix["radius"], r, S, s)
    ttorus = torus.transform(tMatrix["matrix"])
    pvPlotter.add_mesh(ttorus, **kwargs)
    if show:
        pvPlotter.show()
