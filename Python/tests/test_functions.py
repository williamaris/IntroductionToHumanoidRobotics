import os
import sys

sys.path.append('..')

import numpy as np
from numpy.testing import assert_almost_equal

from matlab_utils import MatlabEnv
from utils.functions import *
from setups.SetupBipedRobot import uLINK


matlab_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'Matlab')
matlab = MatlabEnv(dir=matlab_dir)


def test_Rpitch():
    matlab_res = matlab.run_func("Rpitch(0.5)")
    python_res = Rpitch(0.5)

    assert_almost_equal(matlab_res, python_res, decimal=4)


def test_RPY2R():
    matlab_res = matlab.run_func("RPY2R([0.1, 0.1, 0.1])")
    python_res = RPY2R([0.1, 0.1, 0.1])

    assert_almost_equal(matlab_res, python_res, decimal=4)


def test_rpy2rot():
    matlab_res = matlab.run_func("rpy2rot(0.1, 0.1, 0.1)")
    python_res = rpy2rot(0.1, 0.1, 0.1)

    assert_almost_equal(matlab_res, python_res, decimal=4)


def test_Rroll():
    matlab_res = matlab.run_func("Rroll(0.5)")
    python_res = Rroll(0.5)

    assert_almost_equal(matlab_res, python_res, decimal=4)


def test_Ryaw():
    matlab_res = matlab.run_func("Ryaw(0.5)")
    python_res = Ryaw(0.5)

    assert_almost_equal(matlab_res, python_res, decimal=4)


def test_Rodrigues():

    matlab_res = matlab.run_func("Rodrigues([1 0 0]', 0.5)")
    python_res = Rodrigues(np.array([1., 0., 0.]).T, 0.5)
    
    assert_almost_equal(matlab_res, python_res, decimal=4)


def test_AdjointMatrix():
    matlab_res = matlab.run_func("AdjointMatrix([1. 2. 9.; 7. 3. -2.; 4. 7. -1])")
    python_res = adjointMatrix(np.array([[1., 2., 9.], [7., 3., -2.], [4., 7., -1.]]))

    assert_almost_equal(matlab_res, python_res, decimal=4)


def test_FindMother():
    """ MANUALLY TESTED

    Answers for SetupBipedRobot
    Link    | Python    | Matlab
    --------+-----------+----------
    1         0           0
    2         1           1
    3         2           2
    4         3           3
    5         4           4
    6         5           5
    7         6           6
    8         1           1
    9         8           8
    10        9           9
    11        10          10
    12        11          11
    13        12          12
    """

    assert True


def test_ForwardKinematics():
    """ MANUALLY TESTED
    """

    assert True


def test_TotalMass():
    matlab_res = 50.
    python_res = TotalMass(1, uLINK)

    assert_almost_equal(matlab_res, python_res, decimal=4)


def test_CalcJacobian_rot():
    matlab_res = np.array([[0.1, 0], [0., 0.], [0., 0.]])
    python_res = CalcJacobian_rot([1, 2], uLINK)

    assert_almost_equal(matlab_res, python_res, decimal=4)

def test_CalcJacobian():
    matlab_res = np.zeros((6, 3))
    matlab_res[0, 0] = 0.1
    matlab_res[3, 2] = 1.
    matlab_res[5, 0] = 1.
    matlab_res[5, 1] = 1.

    python_res = CalcJacobian([1, 2, 3], uLINK)

    assert_almost_equal(matlab_res, python_res, decimal=4)
