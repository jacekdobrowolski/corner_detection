import numpy as np
from corner_detection.structure_matrix import generate_structure_matrix
from corner_detection.select_good_features import select_good_features


def harris(image: np.ndarray, operator: np.ndarray,
           window: np.ndarray, k: float, max_corners: int, min_distance: int):
    """Implementuje metodę Harrisa

    Args:
        image (:class:`np.ndarray`): Obraz w którym mają zostać znalezione
            narożniki.
        operator (:class:`np.ndarray`): Operator służący do przybliżenia
            pochodnych obrazu. Przykładowo: :class:`filter_kernels.SOBEL` lub
            :class:`filter_kernels.SCHARR`
        window (:class:`np.ndarray`): Okno służące do sumowania wartości
            macierzy struktury.
        k (:class:`float`): Stała k odpowiadająca za czułość algorytmu
            zwykle między 0.04 a 0.15.
        max_corners (:class:`int`): Maksymalna liczba narożników
            jakie zwróci funkcja.
        min_distance (:class:`int`): Minimalny dystans pomiędzy narożnikami
            jakie zwróci funkcja.

    Returns:
        :class:`set`: zwraca zbiór par kordynatów narożników.
    """
    structure = generate_structure_matrix(image, operator, window)
    corner_map = np.empty(structure.shape[:2])
    for x in range(structure.shape[0]):
        for y in range(structure.shape[1]):
            A = structure[x, y]
            corner_map[x, y] = np.linalg.det(A) - k * np.trace(A)

    return select_good_features(corner_map, max_corners, min_distance)
