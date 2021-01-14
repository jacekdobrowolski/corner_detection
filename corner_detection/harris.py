import numpy as np
from corner_detection.structure_matrix import generate_structure_matrix


def harris(image: np.ndarray, operator: np.ndarray,
           window: np.ndarray, k: float):
    """Harris method implementation

    Args:
        image (:class:`np.ndarray`): Image in with corners are to be found.
        operator (:class:`np.ndarray`): Operator used for approximating
            image derivatives. For example: :class:`filter_kernels.SOBEL`
            :class:`filter_kernels.SCHARR`
        window (:class:`np.ndarray`): Window
        k (:class:`int`): Constant determining algorithm sensitivity,
            usually  beetwen 0.04 and 0.15

    Returns:
        :class:`np.ndarray`: :obj:`image` sized array containing value
        coresponding to how good of a corner a given pixel is.
    """
    structure = generate_structure_matrix(image, operator, window)
    result = np.empty(structure.shape[:2])
    for x in range(structure.shape[0]):
        for y in range(structure.shape[1]):
            A = structure[x, y]
            result[x, y] = np.linalg.det(A) - k * (np.trace(A)**2)
    return result
