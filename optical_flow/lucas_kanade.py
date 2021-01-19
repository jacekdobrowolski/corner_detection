import numpy as np
import scipy.signal


def lucas_kanade(previous: np.ndarray, current: np.ndarray,
                 features: set, window_size: int, operator: np.ndarray):
    """Implements Lucas Kanade method of calculating optical flow.

    Args:
        previous (:class:`np.ndarray`): previous frame.
        current (:class:`np.ndarray`): current frame.
        features (:class:`set`): Set of features to track.
        window_size (:class:`int`): Size of window around feature,
            in which optical flow will be calculated.
        operator (:class:`np.ndarray`): Derivative operator like
            Scharr or Sobel.

    Returns:
        List of tuples containing feature coordinates and
        calculated transition vector.
    """
    assert window_size % 2 == 1, 'window_size must be odd'
    assert isinstance(previous, np.ndarray) and previous.ndim == 2, \
        'previous image must be grayscale image, np.ndarray'
    assert isinstance(current, np.ndarray) and current.ndim == 2, \
        'current must be grayscale image, np.ndarray'
    window_radius = int((window_size - 1) / 2 + (operator.shape[0] - 1) / 2)
    result = list()

    for x, y in features:
        current_window = current[x-window_radius:x + window_radius,
                                 y-window_radius:y + window_radius]
        previous_window = previous[x-window_radius:x + window_radius,
                                   y-window_radius:y + window_radius]
        Ix = scipy.signal.convolve2d(current_window,
                                     operator, mode='valid')
        Iy = scipy.signal.convolve2d(current_window,
                                     np.rot90(operator), mode='valid')
        It = current_window - previous_window
        It = It[1:-1, 1:-1].flatten()
        A = np.stack((Ix.flatten(), Iy.flatten()), axis=1)

        result.append((x, y, *np.linalg.lstsq(A, It)[0]))

    return result
