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
        radius (:class:`int`): Radius of a ring to be generated.

    Returns:
        Returns set of tuples containing coordinates,
        relative to center, of pixels on the ring.
    """
    ring = set()
    ring.add((radius, 0))
    if radius - 1 > 0:
        for x in range(1, radius):
            min_value = 1.0
            for y in range(1, radius + 1):
                value = abs(((x**2 + y**2) / radius**2) - 1)
                if min_value > value:
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

    return ring


def FAST(image: np.ndarray, radius: int, threshold: int, n: float):
    """Znajduje dobre narożniki w białoczarnym obrazie metodą FAST

    Args:
        image (:class:`np.ndarray`): Białoczarny obraz w postaci 2 wymiarowej
            :class:`np.ndarray`
        radius (:class:`int`): Promień pierścienia wokół kandydującego
            piksela. Musi być równy lub większy niż 1.
        threshold (:class:`int`): Wartość progowa różnicy w jasności.
        n (:class:`int`): Część pikseli z pierścienia, o różnicy wartości
            jasności z pikselem kandudującym, wymagana do rozpoznania
            narożnika. Musi być między 0 a 1.

    Returns:
        :class:`set` Zwraca zbiór par kordynatów znalezionych narożników.
    """
    assert isinstance(image, np.ndarray) and image.ndim == 2, \
        'image must be grayscale image, np.ndarray'
    assert isinstance(radius, int), 'radius must be integer'
    assert radius >= 1, 'radius must be greater or equal 1'
    assert n <= 1, 'n must be lesser or equal to 1'
    assert radius > 0, 'n must be greater than 0'

    corners = set()
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
                    corners.add(tuple((y, x)))
    return corners
