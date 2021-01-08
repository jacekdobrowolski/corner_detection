from corner_detection.fast import FAST
import pytest
import cv2
import numpy as np


def test_CornerDetection_argument_type_assertions():
    lenna = cv2.imread("lenna.png")

    with pytest.raises(AssertionError):
        FAST(lenna, 80, 10)

    with pytest.raises(AssertionError):
        FAST(1, 80, 10)

    with pytest.raises(AssertionError):
        FAST([[1, 2], [1, 2]], 80, 10)

    with pytest.raises(AssertionError):
        FAST(np.zeros(10), 80, 10)


def test_CornerDetection_return_value():
    lenna = cv2.imread("lenna.png")
    lenna_gray = cv2.cvtColor(lenna, cv2.COLOR_BGR2GRAY)

    corners = FAST(lenna_gray, 80, 10)

    assert isinstance(corners, list)
    assert isinstance(corners[0], tuple)
