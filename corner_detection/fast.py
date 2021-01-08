"""
FAST
***********************

Corner detection using FAST method.
"""
import numpy as np


def _generate_arc(radius: int):
    arc = set()
    arc.add((radius, 0))
    if radius - 1 > 0:
        for x in range(1, radius):
            min_value = 1.0
            for y in range(1, radius + 1):
                value = abs(((x**2 + y**2) / radius**2) - 1)
                # print(x, y, value, min_value)
                if min_value > value:
                    # print("found min")
                    min_value = value
                    min_x, min_y = x, y
            arc.add((min_x, min_y))

    temp_arc = arc.copy()
    for x, y in temp_arc:
        arc.add((y, x))

    temp_arc = arc.copy()
    for x, y in temp_arc:
        arc.add((-x, y))

    temp_arc = arc.copy()
    for x, y in temp_arc:
        arc.add((x, -y))

    temp_arc = arc.copy()
    for x, y in temp_arc:
        arc.add((-x, -y))

    a = np.zeros((radius*2+1, radius*2+1))
    for x, y in arc:
        a[radius+x, radius+y] = 1

    print(a)

    return arc


def FAST(image: np.ndarray, radius: int, threshold: int, n: float):
    """Finds good corners in grayscale image, using FAST method.

    Args:
        image (np.ndarray): Grayscale image in form of 2 dimensional np.ndarray
        radius (int): radius of a circle around candidate corner.
                    Must be greater or equals 1.
        threshold (int): Threshold value.
        n (int): Fraction of pixels on circle around candidate corner with
                    value difference greater than threshold.
                    Must be between 0 and 1.

    Returns:
        list: List of tuples containing indexes of good corners
    """
    assert isinstance(image, np.ndarray) and image.ndim == 2, \
        'image must be grayscale image, np.ndarray'
    assert isinstance(radius, int), 'radius must be integer'
    assert radius >= 1, 'radius must be greater or equal 1'
    assert n <= 1, 'n must be lesser or equal 1'
    assert radius > 0, 'n must be greater than 0'

    corners = list()
    arc = _generate_arc(radius)
    n = int(n*len(arc))

    for x in range(radius, image.shape[0] - radius):
        for y in range(radius, image.shape[1] - radius):

            darker_count = 0
            brighter_count = 0

            for arcX, arcY in arc:
                diff = int(image[x, y]) - int(image[x + arcX, y + arcY])
                if diff > threshold:
                    darker_count += 1
                elif diff < -threshold:
                    brighter_count += 1

                if darker_count > n or brighter_count > n:
                    # Good corner
                    corners.append(tuple((y, x)))
    return corners
