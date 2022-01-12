
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