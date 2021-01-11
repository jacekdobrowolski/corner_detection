import scipy.signal
import numpy as np


def calc_derivatives(image: np.ndarray,
                     operator: np.ndarray) -> (np.ndarray, np.ndarray):
    derivative_x = scipy.signal.convolve2d(image, operator,
                                           mode='same', boundary='symm')
    derivative_y = scipy.signal.convolve2d(image, np.rot90(operator),
                                           mode='same', boundary='symm')
    return derivative_x, derivative_y


def structure_matrix(image: np.ndarray,
                     operator: np.ndarray, window: np.ndarray):
    Ix, Iy = calc_derivatives(image, operator)
    Ix2 = Ix**2
    Iy2 = Iy**2
    Ixy = Ix*Iy
    Ix2_local_sums = scipy.signal.convolve2d(Ix2, window,
                                             mode='same', boundary='symm')
    Iy2_local_sums = scipy.signal.convolve2d(Iy2, window,
                                             mode='same', boundary='symm')
    Ixy_local_sums = scipy.signal.convolve2d(Ixy, window,
                                             mode='same', boundary='symm')

    structure_first_row = np.stack((Ix2_local_sums, Ixy_local_sums), axis=2)
    structure_second_row = np.stack((Ixy_local_sums, Iy2_local_sums), axis=2)
    structure = np.stack((structure_first_row, structure_second_row), axis=3)
    return structure


def shi_tomasi(image: np.ndarray, operator: np.ndarray, window: np.ndarray):
    structure = structure_matrix(image, operator, window)
    result = np.empty(structure.shape[:2])
    for x in range(structure.shape[0]):
        for y in range(structure.shape[1]):
            result[x, y] = np.linalg.eigvals(structure[x, y]).min()
    return result


def harris(image: np.ndarray, operator: np.ndarray,
           window: np.ndarray, k: float):
    structure = structure_matrix(image, operator, window)
    result = np.empty(structure.shape[:2])
    for x in range(structure.shape[0]):
        for y in range(structure.shape[1]):
            A = structure[x, y]
            result[x, y] = np.linalg.det(A) - k * (np.trace(A)**2)
    return result
