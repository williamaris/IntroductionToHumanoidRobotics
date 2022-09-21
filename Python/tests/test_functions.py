import os
import sys

sys.path.append('..')

import numpy as np
from numpy.testing import assert_almost_equal

from matlab_utils import MatlabEnv
from Python.utils.functions import *


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


