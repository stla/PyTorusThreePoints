# -*- coding: utf-8 -*-
from math import cos, pi, sin
import numpy as np
import pyvista as pv
from torus_three_points.main import torusThreePoints # https://github.com/stla/PyTorusThreePoints
import seaborn as sb


###~~~ Hopf fibration ~~~###


def parametrization (beta, theta0, phi):
    a = 1 - sin(beta) * sin(phi)
    return np.array([
        cos(theta0+beta) * cos(phi) / a,
        sin(theta0+beta) * cos(phi) / a,
        cos(beta) * sin(phi) / a
    ])

def tripletOnCircle(phi, start):
    theta_ = np.linspace(0, pi, 11)[:10] + start
    return [
      [
        parametrization(0, theta, phi),
        parametrization(2, theta, phi),
        parametrization(4, theta, phi)
      ] for theta in theta_
    ]

myTriplets = tripletOnCircle(2.4, pi/2) #+ tripletOnCircle(2.2, 0) + tripletOnCircle(2.1, pi)
  

colors = sb.color_palette(palette="rocket", n_colors=len(myTriplets))

pltr = pv.Plotter(window_size=[512, 512])
pltr.set_background("seashell")
for j, triplet in enumerate(myTriplets):
    p1, p2, p3 = triplet
    torusThreePoints(
        pltr, p1, p2, p3, 0.2, pbr = True, ambient=10,
        color = sb.saturate(colors[j]), specular=20, diffuse=10, metallic=100
    )
pltr.set_position((0, 4, 12))
pltr.camera.view_angle = 30.0
pltr.set_focus([0, 0, 0])
pltr.show()
    
