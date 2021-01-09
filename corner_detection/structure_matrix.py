import scipy.signal
import numpy as np


def structure_matrix(image: np.ndarray):
    scharr_kernel_x = np.array([[47, 164, 47], [0, 0, 0], [-47, -164, -47]])
    scharr_kernel_y = np.rot90(scharr_kernel_x)

    derivative_x = scipy.signal.convolve2d(image, scharr_kernel_x)
    derivative_y = scipy.signal.convolve2d(image, scharr_kernel_y)

    derivative_x2 = derivative_x**2
    derivative_y2 = derivative_y**2
    derivative_xy = derivative_x * derivative_y

    structure_first_row = np.stack((derivative_x2, derivative_xy), axis=2)
    structure_second_row = np.stack((derivative_xy, derivative_y2), axis=2)
    structure = np.stack((structure_first_row, structure_second_row), axis=3)
    return structure

# np.sum(np.sum(A[:2, :2], axis=1), axis=0)
