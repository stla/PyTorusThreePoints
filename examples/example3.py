import numpy as np
import pyvista as pv
from torus_three_points.main import torusThreePoints

# Hopf fiber
def HopfInverse(p, phi):
	return np.array([
      p[0]*np.cos(phi) + p[1]*np.sin(phi),
      (1+p[2])*np.sin(phi),
      (1+p[2])*np.cos(phi),
      p[0]*np.sin(phi) - p[1]*np.cos(phi)
	]) / np.sqrt(2*(1+p[2]))

# stereographic projection
def Stereo(q):
	return q[0:3] / (1-q[3])

# rotation in 4D space (right-isoclinic)
def rotate4d(alpha, beta, xi, vec):
  a = np.cos(xi)
  b = np.sin(alpha)*np.cos(beta)*np.sin(xi)
  c = np.sin(alpha)*np.sin(beta)*np.sin(xi)
  d = np.cos(alpha)*np.sin(xi)
  p = vec[0]
  q = vec[1]
  r = vec[2]
  s = vec[3]
  return np.array(
   [a*p - b*q - c*r - d*s,
    a*q + b*p + c*s - d*r,
    a*r - b*s + c*p + d*q,
    a*s + b*r - c*q + d*p]
  )

nCirclesByCyclide = 100
theta_ = np.linspace(0, 2*np.pi, nCirclesByCyclide+1)[0:nCirclesByCyclide]
nCyclides = 3
beta0_ = np.linspace(0, 2*np.pi, nCyclides+1)[0:nCyclides]
colors = ["blue", "red", "green"]
phi = 1 # -pi/2 < phi < pi/2; close to pi/2 <=> big hole
