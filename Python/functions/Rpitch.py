import numpy as np

def Rpitch(theta):
    c = np.cos(theta)
    s = np.sin(theta)

    R = np.array([
        [c, 0., s],
        [0., 1., 0.],
        [-s, 0., c]])

    return R