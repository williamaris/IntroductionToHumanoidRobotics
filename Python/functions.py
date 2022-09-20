import numpy as np

def FindMother(j, uLINK):

    if j != 0:
        if j == 1:
            uLINK[j].mother = 0
        
        if uLINK[j].child != 0:
            uLINK[uLINK[j].child].mother = j
            FindMother(uLINK[j].child, uLINK)

        if uLINK[j].sister != 0:
            uLINK[uLINK[j].sister].mother = uLINK[j].mother
            FindMother(uLINK[j].sister, uLINK)


def MakeBox(dim, org):

    vert = np.array([
        [0.,     0.,     0.],
        [0.,     dim[1], 0.],
        [dim[0], dim[1], 0.],
        [dim[0], 0.,     0.],
        [0.,     0.,     dim[2]],
        [0.,     dim[1], dim[2]],
        [dim[0], dim[1], dim[2]],
        [dim[0], 0.,     dim[2]]
    ]).T

    vert[0, :] = vert[0, :] - org[0]
    vert[1, :] = vert[1, :] - org[1]
    vert[2, :] = vert[2, :] - org[2]

    face = np.array([
        [1., 2., 3., 4.],
        [2., 6., 7., 3.],
        [4., 3., 7., 8.],
        [1., 5., 8., 4.],
        [1., 2., 6., 5.],
        [5., 6., 7., 8.]
    ]).T

    return (vert, face)

def Rodrigues(w, dt):
    norm_w = np.linalg.norm(w)

    if norm_w < np.spacing(1.):
        R = np.eye(3)

    else:
        wn = w / norm_w
        th = norm_w * dt
        w_wedge = np.array([
            [0., -wn[2], wn[1]],
            [wn[2], 0., -wn[0]],
            [-wn[1], wn[0], 0.]
        ])

        R = np.eye(3) + w_wedge * np.sin(th) + w_wedge**(2) * (1. - np.cos(th))

    return R 

def ForwardKinematics(j, uLINK):

    if j == 0:
        return

    if j != 1:
        mom = uLINK[j].mother
        uLINK[j].p = uLINK[mom].R * uLINK[j].b + uLINK[mom].p
        uLINK[j].R = uLINK[mom].R * Rodrigues(uLINK[j].a, uLINK[j].q)

    ForwardKinematics(uLINK[j].sister, uLINK)
    ForwardKinematics(uLINK[j].child, uLINK)


def Rpitch(theta):
    c = np.cos(theta)
    s = np.sin(theta)

    R = np.array([
        [c, 0., s],
        [0., 1., 0.],
        [-s, 0., c]])

    return R


def RPY2R(rpy):
    roll = rpy[0]
    pitch = rpy[1]
    yaw = rpy[2]

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


def Rroll(phi):
    c = np.cos(phi)
    s = np.sin(phi)

    R = np.array([
        [1., 0., 0.],
        [0., c, -s],
        [0., s, c]])

    return R


def Ryaw(psi):
    
    c = np.cos(psi)
    s = np.sin(psi)
    
    R = np.array([
        [c, -s, 0.],
        [s, c, 0.],
        [0., 0., 1.]])

    return R