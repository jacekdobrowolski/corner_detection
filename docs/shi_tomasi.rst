Shi-Tomasi
==============


Metoda Shi-Tomasi bezpośrednio wyznacza :math:`min(\lambda_1, \lambda_2)`
Co daje nieco lesze wyniki kosztem złożoności obliczeniowej.

.. currentmodule:: corner_detection

.. autofunction:: shi_tomasi

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



Działanie na przykładowych obrazach:

.. jupyter-execute::

    img_color = cv2.imread('datasets/Urban2/frame10.png')
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    corners = corner_detection.shi_tomasi(img, corner_detection.SCHARR, np.ones((7,7)), 10, 10)

    plt.subplot(121)
    plt.imshow(img_color)
    plt.axis('off');
    plt.subplot(122)
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');


.. jupyter-execute::
    :hide-code:

    img_color = cv2.imread('datasets/RubberWhale/frame10.png')
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    corners = corner_detection.shi_tomasi(img, corner_detection.SCHARR, np.ones((7,7)), 10, 10)
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
    corners = corner_detection.shi_tomasi(img, corner_detection.SCHARR, np.ones((7,7)), 10, 10)
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
    corners = corner_detection.shi_tomasi(img, corner_detection.SCHARR, np.ones((7,7)), 10, 10)
    plt.subplot(121)
    plt.imshow(img_color)
    plt.axis('off');
    plt.subplot(122)
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');