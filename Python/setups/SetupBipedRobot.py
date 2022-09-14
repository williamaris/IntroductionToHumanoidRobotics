# SetupBipedRobot.py
# Set biped robot structure of Figure 2.19, 2.20
# Field definition: Table 2.1 Link Parameters

import numpy as np
from Link import Link
from functions import *

global uLink
uLink = 13 * [None]


ToDeg = 180./np.pi
ToRad = np.pi/180
UX = [1., 0., 0.]
UY = [0., 1., 0.]
UZ = [0., 0., 1.]


uLink[0] = Link(name='BODY', m=10.0, sister=0, child=2, b=[0, 0, 0.7], a=UZ, q=0.0)

uLink[1] = Link(name='RLEG_J0', m=5.0, sister=8, child=3, b=[0, -0.1, 0], a=UZ, q=0.0)
uLink[2] = Link(name='RLEG_J1', m=1.0, sister=0, child=4, b=[0, 0, 0], a=UX, q=0.0)
uLink[3] = Link(name='RLEG_J2', m=5.0, sister=0, child=5, b=[0, 0, 0], a=UY, q=0.0)
uLink[4] = Link(name='RLEG_J3', m=1.0, sister=0, child=6, b=[0, 0, -0.3], a=UY, q=0.0)
uLink[5] = Link(name='RLEG_J4', m=6.0, sister=0, child=7, b=[0, 0, -0.3], a=UY, q=0.0)
uLink[6] = Link(name='RLEG_J5', m=2.0, sister=0, child=0, b=[0, 0, 0, ], a=UX, q=0.0)

uLink[7] = Link(name='LLEG_J0', m=5.0, sister=0, child=9, b=[0, 0.1, 0], a=UZ, q=0.0)
uLink[8] = Link(name='LLEG_J1', m=1.0, sister=0, child=10, b=[0, 0, 0], a=UX, q=0.0)
uLink[9] = Link(name='LLEG_J2', m=5.0, sister=0, child=11, b=[0, 0, 0], a=UY, q=0.0)
uLink[10] = Link(name='LLEG_J3', m=1.0, sister=0, child=12, b=[0, 0, -0.3], a=UY, q=0.0)
uLink[11] = Link(name='LLEG_J4', m=6.0, sister=0, child=13, b=[0, 0, -0.3], a=UY, q=0.0)
uLink[12] = Link(name='LLEG_J5', m=2.0, sister=0, child=0, b=[0, 0, 0, ], a=UX, q=0.0)

# (uLink[0].vertex, uLink[0].face) = MakeBox(...)
# (uLink[6].vertex, uLink[6].face) = MakeBox(...)
# (uLink[13].vertex, uLink[13].face) = MakeBox(...)

