# SetupBipedRobot.py
# Set biped robot structure of Figure 2.19, 2.20
# Field definition: Table 2.1 Link Parameters

import sys

sys.path.append('..')

import numpy as np
from utils.functions import *
from utils.Link import Link
from utils.MatlabList import MatlabList

uLINK = MatlabList(13)

ToDeg = 180./np.pi
ToRad = np.pi/180
UX = np.array([1., 0., 0.]).T
UY = np.array([0., 1., 0.]).T
UZ = np.array([0., 0., 1.]).T

uLINK[1] = Link(name='BODY', m=10.0, sister=0, child=2, b=np.array([0, 0, 0.7]).T, a=UZ, q=0.0)

uLINK[2] = Link(name='RLEG_J0', m=5.0, sister=8, child=3, b=np.array([0, -0.1, 0]).T, a=UZ, q=0.0)
uLINK[3] = Link(name='RLEG_J1', m=1.0, sister=0, child=4, b=np.array([0, 0, 0]).T, a=UX, q=0.0)
uLINK[4] = Link(name='RLEG_J2', m=5.0, sister=0, child=5, b=np.array([0, 0, 0]).T, a=UY, q=0.0)
uLINK[5] = Link(name='RLEG_J3', m=1.0, sister=0, child=6, b=np.array([0, 0, -0.3]).T, a=UY, q=0.0)
uLINK[6] = Link(name='RLEG_J4', m=6.0, sister=0, child=7, b=np.array([0, 0, -0.3]).T, a=UY, q=0.0)

uLINK[7] = Link(name='RLEG_J5', m=2.0, sister=0, child=0, b=np.array([0, 0, 0, ]).T, a=UX, q=0.0)
uLINK[8] = Link(name='LLEG_J0', m=5.0, sister=0, child=9, b=np.array([0, 0.1, 0]).T, a=UZ, q=0.0)
uLINK[9] = Link(name='LLEG_J1', m=1.0, sister=0, child=10, b=np.array([0, 0, 0]).T, a=UX, q=0.0)
uLINK[10] = Link(name='LLEG_J2', m=5.0, sister=0, child=11, b=np.array([0, 0, 0]).T, a=UY, q=0.0)
uLINK[11] = Link(name='LLEG_J3', m=1.0, sister=0, child=12, b=np.array([0, 0, -0.3]).T, a=UY, q=0.0)
uLINK[12] = Link(name='LLEG_J4', m=6.0, sister=0, child=13, b=np.array([0, 0, -0.3]).T, a=UY, q=0.0)
uLINK[13] = Link(name='LLEG_J5', m=2.0, sister=0, child=0, b=np.array([0, 0, 0, ]).T, a=UX, q=0.0)


(uLINK[1].vertex, uLINK[1].face) = MakeBox([0.1, 0.3, 0.5], [0.05, 0.15, -0.05])    # BODY
(uLINK[7].vertex, uLINK[7].face) = MakeBox([0.2, 0.1, 0.02], [0.05, 0.05, 0.05])    # Foot
(uLINK[13].vertex, uLINK[13].face) = MakeBox([0.2, 0.1, 0.02], [0.05, 0.05, 0.05])  # Foot

FindMother(1, uLINK) # Find mother link from sister and child data

# Substitue the ID to the link name variables. For example, BODY=1
for n in range(1, len(uLINK) + 1):
    exec(uLINK[n].name + " = n")

uLINK[BODY].p = np.array([0.0, 0.0, 0.65]).T
uLINK[BODY].R = np.eye(3)
ForwardKinematics(1, uLINK)

uLINK[BODY].v = np.array([0., 0., 0.]).T
uLINK[BODY].w = np.array([0., 0., 0.]).T

for n in range(1, len(uLINK) + 1):
    uLINK[n].dq = 0.    # Joint speed [rad/s]
