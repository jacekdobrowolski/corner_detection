import numpy as np
from corner_detection.structure_matrix import generate_structure_matrix


def shi_tomasi(image: np.ndarray, operator: np.ndarray, window: np.ndarray):
    """Shi-Tomasi method implementation

    Args:
        image (:class:`np.ndarray`): Image in which corners are to be found.
        operator (:class:`np.ndarray`): Operator used for approximating
            image derivatives. For example: :class:`filter_kernels.SOBEL`
            :class:`filter_kernels.SCHARR`
        window (:class:`np.ndarray`): Window

    Returns:
        :class:`np.ndarray`: :obj:`image` sized array containing value
        coresponding to how good of a corner a given pixel is.
    """
    structure = generate_structure_matrix(image, operator, window)
    result = np.empty(structure.shape[:2])
    for x in range(structure.shape[0]):
        for y in range(structure.shape[1]):
            result[x, y] = np.linalg.eigvals(structure[x, y]).min()
    return result
