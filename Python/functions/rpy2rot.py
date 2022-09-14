import numpy as np

def rpy2rot(roll, pitch, yaw):
    Cphi = np.cos(roll)
    Sphi = np.sin(roll)

    Cthe = np.cos(pitch)
    Sthe = np.sin(pitch)

    Cpsi = np.cos(yaw)
    Spsi = np.sin(yaw)

    rot = np.array([
        [Cpsi*Cthe, -Spsi*Cphi+Cpsi*Sthe*Sphi, Spsi*Sphi+Cpsi*Sthe*Cphi],
        [Spsi*Cthe, Cpsi*Cphi+Spsi*Sthe*Sphi, -Cpsi*Sphi+Spsi*Sthe*Cphi],
        [-Sthe, Cthe*Sphi, Cthe*Cphi]])

    return rot