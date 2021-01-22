Harris-Stephens
================

Jako że wyznaczanie wartości własnych macierzy jest złożone
obliczeniowo. Dlatego stosuje funkcje :math:`M_c`

.. math::

   M_c = \lambda_1 \lambda_2 - \kappa \, (\lambda_1 + \lambda_2)^2
               = \operatorname{det}(A) - \kappa \, \operatorname{trace}^2(A)

Gdzie :math:`\kappa` to stała wyznaczana empirycznie, która odpowiada sa
czułość algorytmu. W literaturze można się spotkać z wartościami między
:math:`0.04` do :math:`0.15`.

Przykładowe dzialanie metody Harrisa:

Najpierw przyjrzyjmy się dokumentacji funkcji

.. currentmodule:: corner_detection

.. autofunction:: harris

.. jupyter-execute::
    :hide-code:
    :hide-output:

    %cd ..

Najpierw importowane są potrzebne moduły

.. jupyter-execute::

    import corner_detection
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt

.. jupyter-execute::
    :hide-code:

    plt.rcParams['figure.figsize'] = [12, 8]
    plt.rcParams['figure.dpi'] = 300

Następnie wczytywany jest białoczarny obraz z zbioru danych danych z uniwersytetu Middlebury.

.. jupyter-execute::

    img = cv2.imread('datasets/Urban2/frame10.png', 0)
    plt.imshow(img, cmap='gray'), plt.axis('off');


Przykładowe wywołanie

.. jupyter-execute::

    corners = corner_detection.harris(image=img, operator=corner_detection.SCHARR,
                                      window=np.ones((5,5)), k=0.1, max_corners=10, min_distance=10)
    plt.imshow(corner_detection.draw_corners(img, corners), cmap='gray'), plt.axis('off');

Badanie wpływu różnego rozmiaru okien

.. jupyter-execute::
    :hide-code:

    img = cv2.imread('datasets/Urban2/frame10.png', 0)
    corners = corner_detection.harris(img, corner_detection.SCHARR, np.ones((3,3)), 0.1, 10, 10)
    plt.subplot(221)
    plt.title('Okno 3x3')
    plt.imshow(corner_detection.draw_corners(img, corners), cmap='gray')
    plt.axis('off');

    img = cv2.imread('datasets/Urban2/frame10.png', 0)
    corners = corner_detection.harris(img, corner_detection.SCHARR, np.ones((5,5)), 0.1, 10, 10)
    plt.subplot(222)
    plt.title('Okno 5x5')
    plt.imshow(corner_detection.draw_corners(img, corners), cmap='gray')
    plt.axis('off');

    img = cv2.imread('datasets/Urban2/frame10.png', 0)
    corners = corner_detection.harris(img, corner_detection.SCHARR, np.ones((7,7)), 0.1, 10, 10)
    plt.subplot(223)
    plt.title('Okno 7x7')
    plt.imshow(corner_detection.draw_corners(img, corners), cmap='gray')
    plt.axis('off');

    img = cv2.imread('datasets/Urban2/frame10.png', 0)
    corners = corner_detection.harris(img, corner_detection.SCHARR, np.ones((9,9)), 0.1, 10, 10)
    plt.subplot(224)
    plt.title('Okno 9x9')
    plt.imshow(corner_detection.draw_corners(img, corners), cmap='gray')
    plt.axis('off');

Większe okna pozwalają uniknąć niepewnych narożników.
Sprawdźmy jeszcze wpływ stałej k. Dla przypomnienia w literaturze podawane są wartości z zakresu 0.04 0.15.

.. jupyter-execute::
    :hide-code:

    img = cv2.imread('datasets/Urban2/frame10.png', 0)
    corners = corner_detection.harris(img, corner_detection.SCHARR, np.ones((7, 7)), 0.01, 10, 10)
    plt.subplot(221)
    plt.title('k = 0.01')
    plt.imshow(corner_detection.draw_corners(img, corners), cmap='gray')
    plt.axis('off');

    img = cv2.imread('datasets/Urban2/frame10.png', 0)
    corners = corner_detection.harris(img, corner_detection.SCHARR, np.ones((7, 7)), 0.05, 10, 10)
    plt.subplot(222)
    plt.title('k = 0.05')
    plt.imshow(corner_detection.draw_corners(img, corners), cmap='gray')
    plt.axis('off');

    img = cv2.imread('datasets/Urban2/frame10.png', 0)
    corners = corner_detection.harris(img, corner_detection.SCHARR, np.ones((7, 7)), 0.1, 10, 10)
    plt.subplot(223)
    plt.title('k = 0.1')
    plt.imshow(corner_detection.draw_corners(img, corners), cmap='gray')
    plt.axis('off');

    img = cv2.imread('datasets/Urban2/frame10.png', 0)
    corners = corner_detection.harris(img, corner_detection.SCHARR, np.ones((7, 7)), 0.2, 10, 10)
    plt.subplot(224)
    plt.title('k = 0.2')
    plt.imshow(corner_detection.draw_corners(img, corners), cmap='gray')
    plt.axis('off');


Jak widać nie ma ona większego wpływu na efekt końcowy w tym przypadku.
Na koniec działanie na innych obrazach dla poniższych argumentów.


.. jupyter-execute::
    :hide-output:

    corner_detection.harris(img, corner_detection.SCHARR, np.ones((7, 7)), 0.1, 10, 10)


.. jupyter-execute::
    :hide-code:

    img_color = cv2.imread('datasets/RubberWhale/frame10.png')
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    corners = corner_detection.harris(img, corner_detection.SCHARR, np.ones((7,7)), 0.1, 10, 10)
    plt.subplot(121)
    plt.imshow(img_color)
    plt.axis('off');
    plt.subplot(122)
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');

.. jupyter-execute::
    :hide-code:

    img_color = cv2.imread('datasets/Venus/frame10.png')
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    corners = corner_detection.harris(img, corner_detection.SCHARR, np.ones((7,7)), 0.1, 10, 10)
    plt.subplot(121)
    plt.imshow(img_color)
    plt.axis('off');
    plt.subplot(122)
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');

.. jupyter-execute::
    :hide-code:

    img_color = cv2.imread('datasets/Hydrangea/frame10.png')
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    corners = corner_detection.harris(img, corner_detection.SCHARR, np.ones((7,7)), 0.1, 10, 10)
    plt.subplot(121)
    plt.imshow(img_color)
    plt.axis('off');
    plt.subplot(122)
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');

.. jupyter-execute::
    :hide-code:

    img_color = cv2.imread('datasets/Grove2/frame10.png')
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    corners = corner_detection.harris(img, corner_detection.SCHARR, np.ones((7,7)), 0.1, 10, 10)
    plt.subplot(121)
    plt.imshow(img_color)
    plt.axis('off');
    plt.subplot(122)
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');