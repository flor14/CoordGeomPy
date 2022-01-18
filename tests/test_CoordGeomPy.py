from CoordGeomPy import CoordGeomPy
from CoordGeomPy import dist_pll_lines_2d
import numpy as np
import pytest

def test_dist_pll_lines_2d():
    """Finding the distance between two parallel lines"""

    m = 2
    b1 = 4
    b2 = -1
    d = 2.23606797749979

    # data type errors 
    assert isinstance(m, (int, float)), "Slope is neither an integer nor a float"
    assert isinstance(b1, (int, float)), "Intercept of line 1 is neither an integer nor a float"
    assert isinstance(b2, (int, float)), "Intercept of line 2 is neither an integer nor a float"
    assert isinstance(d, (int, float)), "Result is wrong data type.."

    # result value approximation
    assert CoordGeomPy.dist_pll_lines_2d(m, b1, b2) == d
    assert round(CoordGeomPy.dist_pll_lines_2d(2, 4, -1), 2) == 2.24

    # ivalid arguments check
    try: 
        dist_pll_lines_2d(m)
    except: 
        print("Missing arguments, please add all the inputs required!")


def test_get_distance_int():
    """Tests the get_distance function with integer input"""
    x1 = [1, 2, 3, 4]
    x2 = [5, 6, 7, 8]

    assert CoordGeomPy.get_distance(x1, x1) == 0
    assert CoordGeomPy.get_distance(x1, x2, "Euclidean") == 8
    assert CoordGeomPy.get_distance(x1, x2, "Manhattan") == 16
    assert CoordGeomPy.get_distance(x1, x2, "Chebyshev") == 4
    assert round(CoordGeomPy.get_distance(x1, x2, "Minokoswki", 3), 2) == 6.350


def test_get_distance_float():
    """Tests the get_distance function with float input"""
    x1 = [9.6, -0.6, 7]
    x2 = [1.23, 5.7, -3]

    assert CoordGeomPy.get_distance(x1, x1) == 0
    assert round(CoordGeomPy.get_distance(x1, x2, "euclidean"), 2) == 14.48
    assert round(CoordGeomPy.get_distance(x1, x2, "manhattan"), 2) == 24.67
    assert CoordGeomPy.get_distance(x1, x2, "chebyshev") == 10
    assert round(CoordGeomPy.get_distance(x1, x2, "minokoswki", -5), 2) == 5.94


def test_get_distance_invalid():
    """Tests that get_distance raises the right exceptions for invalid input"""

    x1 = [1, 2, 3, 4]
    x2 = [5, 6, 7, 8]
    x3 = [0]

    # invalid distance metric
    with pytest.raises(ValueError):
        CoordGeomPy.get_distance(x1, x2, "invalid")

    # invalid x1 value
    with pytest.raises(TypeError):
        CoordGeomPy.get_distance("a", x2, "euclidean")

    # invalid x2 value
    with pytest.raises(TypeError):
        CoordGeomPy.get_distance(x2, "b", "euclidean")

    # mismatched dimensions
    with pytest.raises(TypeError):
        CoordGeomPy.get_distance(x1, x3, "euclidean")

    # invalid p value with Minokowski distance
    with pytest.raises(TypeError):
        CoordGeomPy.get_distance(x1, x2, "minokoswki", "1")
