"""
FAST
***********************

Corner detection using FAST method.
"""
import numpy as np


def _generate_ring(radius: int):
    """Generates list of relative coordinates of
            a one pixel wide ring of a given radius.

    Args:
        radius (:class`int`): Radius of a ring to be generated.

    Returns:
        Returns list of tuples containing coordinates,
                                    relative to center, of pixels on the ring.
    """
    ring = set()
    ring.add((radius, 0))
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
            ring.add((min_x, min_y))

    temp_ring = ring.copy()
    for x, y in temp_ring:
        ring.add((y, x))

    temp_ring = ring.copy()
    for x, y in temp_ring:
        ring.add((-x, y))

    temp_ring = ring.copy()
    for x, y in temp_ring:
        ring.add((x, -y))

    temp_ring = ring.copy()
    for x, y in temp_ring:
        ring.add((-x, -y))

    a = np.zeros((radius*2+1, radius*2+1))
    for x, y in ring:
        a[radius+x, radius+y] = 1

    print(a)

    return ring


def FAST(image: np.ndarray, radius: int, threshold: int, n: float):
    """Finds good corners in grayscale image, using FAST method.

    Args:
        image (:class:`np.ndarray`): Grayscale image in form of 2 dimensional
                                                            :class:`np.ndarray`
        radius (:class:`int`): Radius of a ring around candidate corner.
                                    Must be greater or equals to 1.
        threshold (:class:`int`): Threshold value.
        n (:class:`int`): Fraction of pixels on ring around candidate corner with
                    value difference greater than threshold.
                    Must be between 0 and 1.

    Returns:
        List of tuples containing indexes of good corners
    """
    assert isinstance(image, np.ndarray) and image.ndim == 2, \
        'image must be grayscale image, np.ndarray'
    assert isinstance(radius, int), 'radius must be integer'
    assert radius >= 1, 'radius must be greater or equal 1'
    assert n <= 1, 'n must be lesser or equal to 1'
    assert radius > 0, 'n must be greater than 0'

    corners = list()
    ring = _generate_ring(radius)
    n = int(n*len(ring))

    for x in range(radius, image.shape[0] - radius):
        for y in range(radius, image.shape[1] - radius):

            darker_count = 0
            brighter_count = 0

            for ringX, ringY in ring:
                diff = int(image[x, y]) - int(image[x + ringX, y + ringY])
                if diff > threshold:
                    darker_count += 1
                elif diff < -threshold:
                    brighter_count += 1

                if darker_count > n or brighter_count > n:
                    # Good corner
                    corners.append(tuple((y, x)))
    return corners
