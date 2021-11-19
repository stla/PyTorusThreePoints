# -*- coding: utf-8 -*-
import os
from math import cos, pi, sin
import numpy as np
import pyvista as pv
from torus_three_points.main import torusThreePoints # https://github.com/stla/PyTorusThreePoints


###############################################################################
def parametrization(beta, theta0, phi):
    a = 1 - sin(beta) * sin(phi)
    return np.array([
        cos(theta0+beta) * cos(phi) / a,
        sin(theta0+beta) * cos(phi) / a,
        cos(beta) * sin(phi) / a
    ])


phi1 = 1.8
phi2 = 2
ncircles = 20
radius = 0.3

def draw(pltr, start):
  for i in range(ncircles):
    theta0 = i * 2*pi/ncircles
    p1 = parametrization(0, theta0 + start, phi1);
    p2 = parametrization(2, theta0 + start, phi1);
    p3 = parametrization(4, theta0 + start, phi1);
    torusThreePoints(
        pltr, p1, p2, p3, r=radius, pbr = True, ambient=10,
        color = "red", specular=20, diffuse=10, metallic=100
    )
    p1 = parametrization(0, theta0 - start, phi2);
    p2 = parametrization(2, theta0 - start, phi2);
    p3 = parametrization(4, theta0 - start, phi2);
    torusThreePoints(
        pltr, p1, p2, p3, r=radius, pbr = True, ambient=10,
        color = "blue", specular=20, diffuse=10, metallic=100
    )


def NestedCliffordCircles(n, gifname=None, convert="magick convert", delay=8):
    anim = gifname is not None
    if anim:
        gif_sansext, file_extension = os.path.splitext(os.path.basename(gifname))
        screenshotfmt = gif_sansext + "_%03d.png"
        screenshotglob = gif_sansext + "_*.png"
    for i in range(n):
        s = i * 2*pi/ncircles/n
        pltr = pv.Plotter(window_size=[512, 512], off_screen=anim)
        pltr.set_background("seashell")
        draw(pltr, s)
        pltr.set_position((0, -84, 50))
        pltr.camera.view_angle = 13.0
        pltr.set_focus([0, 0, 0])
        if anim:
            pngname = screenshotfmt % i
            pltr.show(screenshot=pngname)
        else:
            pltr.show()
    if anim:
        os.system(
            convert + (" -dispose previous -loop 0 -delay %d " % delay) + screenshotglob + " " + gifname    
        ) 
    
NestedCliffordCircles(10, gifname="NestedCliffordCircles.gif")