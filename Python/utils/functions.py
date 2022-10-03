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

        R = np.eye(3) + w_wedge * np.sin(th) + np.matmul(w_wedge, w_wedge) * (1. - np.cos(th))

    return R 

def ForwardKinematics(j, uLINK):

    if j == 0:
        return

    if j != 1:
        mom = uLINK[j].mother
        uLINK[j].p = np.matmul(uLINK[mom].R, uLINK[j].b) + uLINK[mom].p
        uLINK[j].R = np.matmul(uLINK[mom].R, Rodrigues(uLINK[j].a, uLINK[j].q))

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


def rot2omega(R):
    el = np.array([[R[2, 1] - R[1, 2]], [R[0, 2] - R[2, 0]], [R[1, 0] - R[0, 1]]])
    norm_el = np.linalg.norm(el)

    if norm_el > np.spacing(1.):
        w = np.atan2(norm_el, np.trace(R) - 1.) / norm_el * el

    elif R[0, 0] > 0. and R[1, 1] > 0. and R[2, 2] > 0.:
        w = np.array([0., 0., 0.]).T

    else:
        w = np.pi / 2. * np.array([[R[0, 0] + 1.], [R[1, 1] + 1.], [R[2, 2] + 1.]])

    return w


def TotalMass(j, uLINK):
    if j == 0:
        m = 0

    else:
        m = uLINK[j].m + TotalMass(uLINK[j].sister, uLINK) + TotalMass(uLINK[j].child, uLINK)

    return m


def MoveJoints(idx, dq, uLINK):
    
    for n in range(len(idx)):
        j = idx[n]
        uLINK[j].q = uLINK[j].q + dq[n]


def calcP(j, uLINK):
    if j == 0:
        P = np.array([0., 0., 0.]).T

    else:
        c1 = uLINK[j].R * uLINK[j].c
        P = uLINK[j].m * (uLINK[j].v + np.cross(uLINK[j].w, c1))
        P = P + calcP(uLINK[j].sister, uLINK) + calcP(uLINK[j].child, uLINK)

    return P


def calcMC(j, uLINK):

    if j == 0:
        mc = 0

    else:
        mc = uLINK[j].m * (uLINK[j].p + uLINK[j].R * uLINK[j].c)
        mc = mc + calcMC(uLINK[j].sister, uLINK) + calcMC(uLINK[j].child, uLINK)

    return mc


def calcCoM(uLINK):

    M = TotalMass(1, uLINK)
    MC = calcMC(1, uLINK)
    com = MC / M

    return com


def adjointMatrix(M):
    n_row = M.shape[0]
    n_col = M.shape[1]
    adj_M = np.zeros((n_row, n_col))

    if n_col != n_row:
        print('ERROR: Matrix must be square\n')
        return

    for j in range(n_col):
        Mj = np.delete(M, j, 0)
        
        for k in range(n_row):
            Mjk = np.delete(Mj, k, 1)
            adj_M[k, j] = (-1.)**(j+k) * np.linalg.det(Mjk)

    return adj_M


def CalcJacobian_rot(idx, uLINK):
    jsize = len(idx)
    target = uLINK[idx[-1]].p
    J = np.zeros((3, jsize))

    for n in range(0, jsize):
        j = idx[n]
        a = np.matmul(uLINK[j].R, uLINK[j].a)
        J[:, n] = np.cross(a, target - uLINK[j].p)

    return J


def CalcJacobian(idx, uLINK):
    jsize = len(idx)
    target = uLINK[idx[-1]].p
    J = np.zeros((6, jsize))

    for n in range(0, jsize):
        j = idx[n]
        a = np.matmul(uLINK[j].R, uLINK[j].a)
        J[:, n] = np.concatenate((np.cross(a, target - uLINK[j].p), a), axis=0)

    return J


def calcL(j, uLINK):
    if j == 0:
        return 0.

    c1 = np.matmul(uLINK[j].R, uLINK[j].c)
    c = uLINK[j].p + c1
    P = uLINK[j].m * (uLINK[j].v + np.cross(uLINK[j].w, c1))
    R = uLINK[j].R
    I = uLINK[j].I
    w = uLINK[j].w
    L = np.cross(c, P) + np.matmul(R, np.matmul(I, np.matmul(R.T, w)))
    L = L = calcL(uLINK[j].sister, uLINK) + calcL(uLINK[j].child, uLINK)

    return L