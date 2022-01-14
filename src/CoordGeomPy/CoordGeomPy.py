def dist_pll_lines(m, b1, b2):
    """Finding the distance between two parallel lines.

    The distance between two parallel lines is the distance between the points where a perpendicular line intersects.
    This function will find that distance (d).

    Parameters
    ----------
    m  : float
        slope of two parallel lines which are the same.
    b1 : float
        intercept of line 1 where y = mx + b1
    b2 : float
        intercept of line 2 where y = mx + b2

    Returns
    -------
    float
        distance d between two parallel lines

    Examples
    --------
    >>> dist_pll_lines(3.0, 4.5, 2.5)
    0.25
    >>> dist_pll_lines(-4, 11, 23)
    0.8
    """


def get_distance(x1, x2, metric="Euclidean", p=None):
    """Calculates the distance between two n dimensional vectors.

    Possible metrics include: Euclidean, Manhattan, Chebyshev, or Minkowski.

    Parameters
    ----------
    x1 : list of int or float
        The first n dimensional vector.
    x2 : list of int or float
        The second n dimensional vector.
    metric : str, default="Euclidean"
        The distance metric, must be one of "Euclidean", "Manhattan", Chebyshev,
        or "Minkowski"
    p : int, default=None
        The order of Minkowski distance to calculate.  Only required if `metric` is
        set to "Minkowski".

    Returns
    -------
    float
        The relevant distance between the two vectors.

    Examples
    --------
    >>> x1 = [1, 2, 3, 4]
    >>> x2 = [5, 6, 7, 8]
    >>> get_distance(x1, x2, metric="Euclidean")
    8
    >>> get_distance(x1, x2, metric="Manhattan")
    16
    >>> get_distance(x1, x2, metric="Chebyshev")
    4
    >>> get_distance(x1, x2, metric="Minkowski", 3)
    6.3496
    """

def is_intersection(m1, b1, m2, b2):
    """Determines whether two infinite lines intersect in 3-dimensional space.

    Note that if two equivalent lines are provided, they will be considered as intersecting. 

    Parameters
    ----------
    m1 : list or tuple of floats
        This list corresponds to a 3-dimensional vector ⟨𝑚𝑥1,𝑚𝑦1,𝑚𝑧1⟩ describing the 
        direction vector (or slope) of line 2. List or tuple must be of length 3. 
    b1 : list or tuple of floats
        Any point on line 1. This list corresponds to a point (x1, y1, z1) that lies on line 1. 
        This point must lie on line 2. 
    m2 : list or tuple of floats
        This list corresponds to a 3-dimensional vector ⟨𝑚𝑥2,𝑚𝑦2,𝑚𝑧2⟩ describing the 
        direction vector (or slope) of line 2.
    b2 : list or tuple of floats
        Any point on line 2. This list corresponds to a point (x2, y2, z2) that lies on line 2. 
        This point must lie on line 2. 

    Returns
    -------
    bool
        True if there is intersection, False if not. 

    Examples
    --------
    >>> m1 = (1, 0, 0)
    >>> m2 = (0, 1, 0)
    >>> b1 = (0, 0, 0)
    >>> b2 = (0, 0, 0)
    >>> is_intersection(m1, b1, m2, b2)
    True

    >>> m3 = (1, 1, 1)
    >>> m4 = (1, 1, 1)
    >>> b3 = (0, 0, 0)
    >>> b4 = (1, 1, 1)
    >>> is_intersection(m3, m4, b3, b4)
    False
    """
    
def is_orthogonal(m1, m2):
    """Determines whether two infinite lines are perpendicular in n-dimensional space.
    Parameters
    ----------
    m1 : list or tuple of floats
        This list corresponds to a n-dimensional vector ⟨mx1, my1, mz1, ...⟩ describing the 
        direction vector of line 1.
    m2 : list or tuple of floats
        This list corresponds to a n-dimensional vector ⟨mx2, my2, mz2, ...⟩ describing the 
        direction vector of line 2. Demensions of line 1 and line 2 must be equal. 
    Returns
    -------
    bool
        True if there is orthogonal, False if not. 
    Examples
    --------
    >>> m1 = (1, 0)
    >>> m2 = (0, 1)
    >>> is_orthogonal(m1, m2)
    True
    >>> m3 = (0, 0, 1)
    >>> m4 = (1, 1, 1)
    >>> is_orthogonal(m3, m4)
    False
    """
