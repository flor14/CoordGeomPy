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
