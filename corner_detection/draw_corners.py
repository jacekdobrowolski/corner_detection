import cv2
import numpy as np


def draw_corners(image: np.ndarray, corners: set):
    image_copy = image.copy()
    for corner in corners:
        cv2.circle(image_copy, corner, radius=2, thickness=3, color=(255))

    return image_copy
