# python version 3.5 or greater required

import numpy as np

def CornerDetection( image: np.ndarray, threshold: int, n: int):
    """Finds good corners in grayscale image, using FAST method.

    Args:
        image (np.ndarray): Grayscale image in form of 2 dimensional np.ndarray
        threshold (int): Threshold value.
        n (int): Number of pixels on circle around candidate corner with value difference greater than threshold.

    Returns:
        corners: List of tuples containing indexes of good corners
    """
    assert isinstance(image, np.ndarray) and image.ndim == 2, 'image must be grayscale image, np.ndarray'
    # assert isinstance(radius, int), 'radius must be integer'

    corners = list()

    # arc list
    arcList = [(-1,3),  (0,3),  (1,3),
               (-1,-3), (0,-3), (1,-3),
               (3,-1),  (3,0),  (3,1),
               (-3,-1), (-3,0), (-3,1),
               (2,2),   (2,-2), (-2,2), (-2,-2)]
    radius = 3

    for x in range(radius, image.shape[0] - radius):
        for y in range(radius, image.shape[1] - radius):

            darker_count = 0
            brighter_count = 0

            for arcX, arcY in arcList:
                diff = int(image[x,y]) - int(image[x + arcX, y + arcY])
                if diff > threshold:
                    darker_count += 1
                elif diff < -threshold:
                    brighter_count += 1

                if darker_count > n or brighter_count > n:
                    # Good corner
                    corners.append(tuple((y, x)))
    return corners