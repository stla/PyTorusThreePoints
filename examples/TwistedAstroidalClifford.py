# -*- coding: utf-8 -*-
from math import cos, sin, pi, sqrt
import numpy as np
import pyvista as pv
import bisect
from torus_three_points.main import transfoMatrix

def scos(x, alpha):
    cosx = cos(x)
    return cosx**alpha if cosx >= 0 else -(-cosx)**alpha

def ssin(x, alpha):
    sinx = sin(x)
    return sinx**alpha if sinx >= 0 else -(-sinx)**alpha

def torusMesh(alpha, ntwists, R, r, S=64, s=32, arc=2*pi):
    vertices = np.empty((0, 3))
    faces = np.empty((0), dtype=int)
    distances = []
    breakpoints = pi*(1/16 + np.linspace(0, 2, 17)) % (2*pi)
    for j in range(s + 1):
        v = j / s * 2 * pi
        rcos3_v = r * scos(v, alpha)
        rsin3_v = r * ssin(v, alpha)
        for i in range(S + 1):
            u = i / S * arc
            cos_u = cos(u)
            sin_u = sin(u)
            cos_2u = cos(ntwists*u)
            sin_2u = sin(ntwists*u)
            cx = R * cos_u
            cy = R * sin_u
            w = rcos3_v*cos_2u + rsin3_v*sin_2u
            vertex = np.array(
                [
                  cx + cos_u * w,
                  cy + sin_u * w,
                  rsin3_v*cos_2u - rcos3_v*sin_2u
                ]
            )
            vertices = np.vstack((vertices, vertex))
            if i < S and j < s:
                k = bisect.bisect_left(breakpoints, v) % 2
                distances.append(k)
    for j in range(s):
        for i in range(S):
            a = (S + 1) * (j + 1) + i
            b = (S + 1) * j + i
            c = (S + 1) * j + i + 1
            d = (S + 1) * (j + 1) + i + 1
            faces = np.concatenate((
              faces, np.array([3, a, b, d, 3, b, c, d])
            ), axis=0)
    mesh = pv.PolyData(vertices, faces).extract_geometry().clean(tolerance=1e-6)
    mesh.point_data["distance"] = np.asarray(distances)
    return mesh

def HopfInverse(p, phi):
	return np.array([
      (1 + p[2]) * cos(phi),
      p[0] * sin(phi) - p[1] * cos(phi), 
      p[0] * cos(phi) + p[1] * sin(phi),
      (1 + p[2]) * sin(phi)
	]) / sqrt(2 * (1 + p[2]))

def Stereo(q):
	return 2*q[0:3] / (1-q[3])

def VillarceauTriplet(theta, phi):
    pt = [cos(theta)*cos(phi), sin(theta)*cos(phi), sin(phi)]
    p1 = Stereo(HopfInverse(pt, 0))
    p2 = Stereo(HopfInverse(pt, pi/2))
    p3 = Stereo(HopfInverse(pt, 3*pi/2))
    return (p1, p2, p3)

def seriesOfTriplets(n):
    theta_ = np.linspace(0, 2*pi, n+1)[:n]
    return [VillarceauTriplet(theta, 2) for theta in theta_]


triplets = seriesOfTriplets(10)
pltr = pv.Plotter(window_size=[512,512])
pltr.set_focus([0, 0, 0])
pltr.set_position([-80, -102, 0])
pltr.camera.zoom(1.3)
for triplet in triplets:
    matAndRad = transfoMatrix(triplet[0], triplet[1], triplet[2])
    mesh0 = torusMesh(3, 1, matAndRad["radius"], 2)
    mesh = mesh0.transform(matAndRad["matrix"])
    pltr.add_mesh(
        mesh, smooth_shading=True, cmap=["#440154", "#FDE725"], specular=10,
        show_scalar_bar=False
    )
pltr.show()