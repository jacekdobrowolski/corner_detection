import numpy as np
import scipy.signal


def lucas_kanade(previous: np.ndarray, current: np.ndarray,
                 features: set, window_size: int, operator: np.ndarray):
    """Implementuje metodę Lucas Kanade

    Args:
        previous (:class:`np.ndarray`): Poprzednia białoczarna klatka
        current (:class:`np.ndarray`): Obecna białoczarna klatka
        features (:class:`set`): Zbiór punktów do śledzenia
        window_size (:class:`int`): Rozmiar okna w którym znaleziono punkt.
        operator (:class:`np.ndarray`): Operator służący do wyznaczania
            pochodnych obrazu.

    Returns:
        :class:`set` :class:`tuple` Kordynaty punktu i wektor u, v.
    """
    assert window_size % 2 == 1, 'window_size must be odd'
    assert isinstance(previous, np.ndarray) and previous.ndim == 2, \
        'previous image must be grayscale image, np.ndarray'
    assert isinstance(current, np.ndarray) and current.ndim == 2, \
        'current must be grayscale image, np.ndarray'
    window_radius = int((window_size - 1) / 2 + (operator.shape[0] - 1) / 2)
    result = list()

    for y, x in features:
        current_window = current[x - window_radius: x + window_radius,
                                 y - window_radius: y + window_radius]
        previous_window = previous[x - window_radius: x + window_radius,
                                   y - window_radius: y + window_radius]

        Ix = scipy.signal.convolve2d(current_window,
                                     operator, mode='valid')
        Iy = scipy.signal.convolve2d(current_window,
                                     np.rot90(operator), mode='valid')
        It = current_window - previous_window
        It = It[1:-1, 1:-1].flatten()
        A = np.stack((Ix.flatten(), Iy.flatten()), axis=1)

        result.append((x, y, *np.linalg.lstsq(A, It, rcond=None)[0]))

    return result
