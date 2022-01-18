from CoordGeomPy import CoordGeomPy
import pytest


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
