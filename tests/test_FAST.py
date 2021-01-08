import pytest
from corner_detection.fast import FAST
import cv2
import numpy as np


def test_corner_detection_fast_argument_type():
    lenna = cv2.imread("lenna.png")
    lenna_gray = cv2.cvtColor(lenna, cv2.COLOR_BGR2GRAY)

    with pytest.raises(AssertionError):
        FAST(lenna, 3, 80, 0.8)

    with pytest.raises(AssertionError):
        FAST(1, 3, 80, 0.8)

    with pytest.raises(AssertionError):
        FAST([[1, 2], [1, 2]], 3, 80, 0.8)

    with pytest.raises(AssertionError):
        FAST(np.zeros(10), 3, 80, 0.8)

    with pytest.raises(AssertionError):
        FAST(lenna_gray, 0, 80, 0.8)


def test_corner_detection_fast_return_value():
    lenna = cv2.imread("lenna.png")
    lenna_gray = cv2.cvtColor(lenna, cv2.COLOR_BGR2GRAY)

    corners = FAST(lenna_gray, 3, 80, 0.8)

    assert isinstance(corners, list)
    assert isinstance(corners[0], tuple)
