import numpy as np

def Rroll(phi):
    c = np.cos(phi)
    s = np.sin(phi)

    R = np.array([
        [1., 0., 0.],
        [0., c, -s],
        [0., s, c]])

    return R