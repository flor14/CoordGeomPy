from CoordGeomPy.CoordGeomPy import is_intersection_3d, dist_pll_lines_2d, get_distance, is_orthogonal
import numpy as np
import pytest

def test_is_intersection_3d_base():
    """Base tests on correct input"""
    
    # not intersecting
    assert is_intersection_3d((1, 3, -1), (0, -2, 4), (2, 1, 4), (0, 3, -3)) == False

    # parallel lines
    assert is_intersection_3d((1, 1, 1), (0, 0, 0), (1, 1, 1), (1, 1, 1)) == False

    # "normal" intersection
    assert is_intersection_3d((1, 0, 0), (0, 0, 0), (0, 1, 0), (0, 0, 0)) == True
    assert is_intersection_3d((1, 0, 0), (0, 0, 0), (0, 1, 0), (1, 1, 0)) == True

def test_is_intersection_3d_float():
    """Test to make sure function rounds floating point numbers"""
    
    # not intersecting
    assert is_intersection_3d((1.1, 3.2, -1.3), (0.0, -2.4, 4.2), (2.1, 1, 4), (0.2, 3.3, -3.0)) == False

    # parallel lines
    assert is_intersection_3d((1.1, 0.8, 0.9), (0, 0, 0), (1.2, 0.8, 1.4), (1, 1, 1)) == False

    # "normal" intersection
    assert is_intersection_3d((1.2, 0.3, 0.4), (0, 0.1, 0.1), (0, 1, 0), (0, 0, 0)) == True
    assert is_intersection_3d((1.3, 0.3, 0), (0, 0, 0), (0, 0.9, 0), (0.7, 1.3, 0)) == True

def test_is_intersection_3d_input():
    """Error testing"""

    m1 = {1, 1, 1}
    m2 = (0, 0, 0)
    b1 = (0, 0, 0)
    b2 = (0, 0, 0)

    # Invalid m1 type
    with pytest.raises(TypeError): 
        is_intersection_3d(m1, b1, m2, b2)

    # Invalid b1 type
    m1 = (1, 1, 1)
    b1 = {0, 0, 0}
    with pytest.raises(TypeError): 
        is_intersection_3d(m1, b1, m2, b2)

    # Invalid m1 length
    m1 = (1, 1, 1, 1)
    b1 = (0, 0, 0)
    with pytest.raises(ValueError): 
        is_intersection_3d(m1, b1, m2, b2)

# ==============================================================================================

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
    assert dist_pll_lines_2d(m, b1, b2) == d
    assert round(dist_pll_lines_2d(2, 4, -1), 2) == 2.24
  
# ==============================================================================================

def test_get_distance_int():
    """Tests the get_distance function with integer input"""
    x1 = [1, 2, 3, 4]
    x2 = [5, 6, 7, 8]

    assert get_distance(x1, x1) == 0
    assert get_distance(x1, x2, "Euclidean") == 8
    assert get_distance(x1, x2, "Manhattan") == 16
    assert get_distance(x1, x2, "Chebyshev") == 4
    assert round(get_distance(x1, x2, "Minokoswki", 3), 2) == 6.350


def test_get_distance_float():
    """Tests the get_distance function with float input"""
    x1 = [9.6, -0.6, 7]
    x2 = [1.23, 5.7, -3]

    assert get_distance(x1, x1) == 0
    assert round(get_distance(x1, x2, "euclidean"), 2) == 14.48
    assert round(get_distance(x1, x2, "manhattan"), 2) == 24.67
    assert get_distance(x1, x2, "chebyshev") == 10
    assert round(get_distance(x1, x2, "minokoswki", -5), 2) == 5.94


def test_get_distance_invalid():
    """Tests that get_distance raises the right exceptions for invalid input"""

    x1 = [1, 2, 3, 4]
    x2 = [5, 6, 7, 8]
    x3 = [0]

    # invalid distance metric
    with pytest.raises(ValueError):
        get_distance(x1, x2, "invalid")

    # invalid x1 value
    with pytest.raises(TypeError):
        get_distance("a", x2, "euclidean")

    # invalid x2 value
    with pytest.raises(TypeError):
        get_distance(x2, "b", "euclidean")

    # mismatched dimensions
    with pytest.raises(TypeError):
        get_distance(x1, x3, "euclidean")

    # invalid p value with Minokowski distance
    with pytest.raises(TypeError):
        get_distance(x1, x2, "minokoswki", "1")

# ==============================================================================================

def test_is_orthogonal_input():
    # Invalid input type
    with pytest.raises(TypeError): 
        is_orthogonal({1,2,3}, (1,2,3))
    with pytest.raises(TypeError): 
        is_orthogonal([1,2,3], 12)
    with pytest.raises(TypeError): 
        is_orthogonal("Wrong", [1,2,3])

    # Invalid length
    with pytest.raises(ValueError): 
        is_orthogonal([1,2], [1,1,1])
    with pytest.raises(ValueError): 
        is_orthogonal([], [1,1,1])

def test_is_orthogonal_T():
    assert is_orthogonal((0, 0, 0), (1, 1, 1)) == True
    assert is_orthogonal((1, 0, 0), (0, 1, 0)) == True
    assert is_orthogonal((13, -1, 2, 0), (-1, 1, 7, 10)) == True
    assert is_orthogonal([0.2, -4.8], [12, 0.5]) == True
    assert is_orthogonal((0.2, -4.8), [12, 0.5]) == True

def test_is_orthogonal_F():
    assert is_orthogonal((0, 0, 1), (1, 1, 1)) == False
    assert is_orthogonal((1, 1, 0), (-1, 2, 0)) == False
    assert is_orthogonal((13, -1, 2, 0), (-1, 1, 8, 10)) == False
    assert is_orthogonal([0.2, -4.8], [12.000001, 0.5]) == False
