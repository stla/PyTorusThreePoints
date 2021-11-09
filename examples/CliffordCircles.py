# -*- coding: utf-8 -*-
import os
from math import cos, pi, sin, sqrt
import numpy as np
import pyvista as pv
from torus_three_points.main import torusThreePoints # https://github.com/stla/PyTorusThreePoints
import seaborn as sb

###############################################################################
def parametrization (beta, theta0, phi):
    a = 1 - sin(beta) * sin(phi)
    return np.array([
        cos(theta0+beta) * cos(phi) / a,
        sin(theta0+beta) * cos(phi) / a,
        cos(beta) * sin(phi) / a
    ])

def tripletOnCircle(phi, ncircles, start=0):
    theta_ = np.linspace(0, 2*pi, ncircles+1)[:ncircles] + start
    return [
      [
        parametrization(0, theta, phi),
        parametrization(2, theta, phi),
        parametrization(4, theta, phi)
      ] for theta in theta_
    ]


def CliffordCircles(phi, ncircles, palette, nframes, radius, gifname=None, convert="magick convert", delay=8):
    myTriplets = tripletOnCircle(phi, ncircles) #+ tripletOnCircle(2.2, 0) + tripletOnCircle(2.1, pi)
    colors = sb.color_palette(palette=palette, n_colors=len(myTriplets))
    angle_ = np.linspace(0, 360, nframes+1)[:nframes]
    for i, angle in enumerate(angle_):
        anim = gifname is not None
        if anim:
            gif_sansext, file_extension = os.path.splitext(os.path.basename(gifname))
            screenshotfmt = gif_sansext + "_%03d.png"
            screenshotglob = gif_sansext + "_*.png"
        pltr = pv.Plotter(window_size=[512, 512], off_screen=anim)
        pltr.set_background("seashell")
        for j, triplet in enumerate(myTriplets):
            p1, p2, p3 = triplet
            torusThreePoints(
                pltr, p1, p2, p3, radius, pbr = True, ambient=10,
                color = sb.saturate(colors[j]), specular=20, diffuse=10, metallic=100
            )
        #pltr.set_position((0, 4, 12))
        pltr.camera_position = "xz"
        pltr.camera.view_angle = 27.0
        pltr.set_focus([0, 0, 0])
        pltr.camera.roll = angle
        pltr.camera.azimuth = angle
        if anim:
            pngname = screenshotfmt % i
            pltr.show(screenshot=pngname)
        else:
            pltr.show()
    if anim:
        os.system(
            convert + (" -dispose previous -loop 0 -delay %d " % delay) + screenshotglob + " " + gifname    
        ) 
    
CliffordCircles(2.4, 16, "rocket", 180, 0.15, gifname="CliffordCircles.gif")