# -*- coding: utf-8 -*-
import os
from math import sqrt, cos, sin, pi
import numpy as np
import pyvista as pv
from torus_three_points.main import torusThreePoints 

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

radius = 0.32



for N in range(30):
    k = 0
    color = "yellow"
    pltr = pv.Plotter(window_size=[512,512], off_screen=True)
    pltr.set_background("#363940")
    pltr.set_position([-20, -40, 10])
    pltr.camera.view_angle = 17.0
    pltr.set_focus([0, 0, 0])
    for i in range(N+1):
        if i > 9:
            k = 1
            color = "red"
        if i > 19:
            k = 2
            color = "blue"
        (p1, p2, p3) = VillarceauTriplet(2*(3*i+k)*pi/30, 0)
        torusThreePoints(
            pltr, p1, p2, p3, radius, pbr = True, ambient=10,
            color = color, specular=20, diffuse=10, metallic=100
        )
        if i == N:
            pltr.show(screenshot="zpic_%03d.png" % i)

os.system(
    "magick convert -dispose previous -loop 0 -delay 12 zpic_*.png VillarceauCircles.gif"    
)