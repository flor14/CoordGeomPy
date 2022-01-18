from CoordGeomPy import CoordGeomPy
import pytest

def test_is_intersection_3d_base():
    """Base tests on correct input"""
    
    # not intersecting
    assert CoordGeomPy.is_intersection_3d((1, 3, -1), (0, -2, 4), (2, 1, 4), (0, 3, -3)) == False

    # parallel lines
    assert CoordGeomPy.is_intersection_3d((1, 1, 1), (0, 0, 0), (1, 1, 1), (1, 1, 1)) == False

    # "normal" intersection
    assert CoordGeomPy.is_intersection_3d((1, 0, 0), (0, 0, 0), (0, 1, 0), (0, 0, 0)) == True
    assert CoordGeomPy.is_intersection_3d((1, 0, 0), (0, 0, 0), (0, 1, 0), (1, 1, 0)) == True

def test_is_intersection_3d_float():
    """Test to make sure function rounds floating point numbers"""
    
    # not intersecting
    assert CoordGeomPy.is_intersection_3d((1.1, 3.2, -1.3), (0.0, -2.4, 4.2), (2.1, 1, 4), (0.2, 3.3, -3.0)) == False

    # parallel lines
    assert CoordGeomPy.is_intersection_3d((1.1, 0.8, 0.9), (0, 0, 0), (1.2, 0.8, 1.4), (1, 1, 1)) == False

    # "normal" intersection
    assert CoordGeomPy.is_intersection_3d((1.2, 0.3, 0.4), (0, 0.1, 0.1), (0, 1, 0), (0, 0, 0)) == True
    assert CoordGeomPy.is_intersection_3d((1.3, 0.3, 0), (0, 0, 0), (0, 0.9, 0), (0.7, 1.3, 0)) == True

def test_is_intersection_3d_input():
    """Error testing"""

    m1 = {1, 1, 1}
    m2 = (0, 0, 0)
    b1 = (0, 0, 0)
    b2 = (0, 0, 0)

    # Invalid m1 type
    with pytest.raises(TypeError): 
        CoordGeomPy.is_intersection_3d(m1, b1, m2, b2)

    # Invalid b1 type
    m1 = (1, 1, 1)
    b1 = {0, 0, 0}
    with pytest.raises(TypeError): 
        CoordGeomPy.is_intersection_3d(m1, b1, m2, b2)


    # Invalid m1 length
    m1 = (1, 1, 1, 1)
    b1 = (0, 0, 0)
    with pytest.raises(ValueError): 
        CoordGeomPy.is_intersection_3d(m1, b1, m2, b2)