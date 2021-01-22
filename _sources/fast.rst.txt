FAST
===============

Metoda FAST (Features from accelerated segment
test) :cite:`FAST` polega na znalezieniu punktów dla których
w danym promieniu. Znaczna część pixeli różni się od centralnego pixela
o wartość progu detekcji. Zaletą tej metody jest niska złożoność
obliczeniowa. Algorytm ten ma 3 parametry które można zbadać.

.. currentmodule:: corner_detection

.. autofunction:: FAST

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


Działanie dla różnych wartości promienia:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. jupyter-execute::
    :hide-output:

    img_color = cv2.imread('datasets/Urban2/frame10.png')
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    corners = corner_detection.FAST(image=img, radius=2, threshold=70, n=0.7)


.. jupyter-execute::
    :hide-code:

    plt.subplot(221)
    plt.title('radius=2')
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');

    corners = corner_detection.FAST(image=img, radius=3, threshold=70, n=0.7)

    plt.subplot(222)
    plt.title('radius=3')
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');

    corners = corner_detection.FAST(image=img, radius=4, threshold=70, n=0.7)

    plt.subplot(223)
    plt.title('radius=4')
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');

    corners = corner_detection.FAST(image=img, radius=5, threshold=70, n=0.7)

    plt.subplot(224)
    plt.title('radius=5')
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');


Działanie dla innych wartości progu:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. jupyter-execute::
    :hide-code:
    
    corners = corner_detection.FAST(image=img, radius=3, threshold=50, n=0.7)

    plt.subplot(221)
    plt.title('threshold=50')
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');

    corners = corner_detection.FAST(image=img, radius=3, threshold=70, n=0.7)

    plt.subplot(222)
    plt.title('threshold=70')
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');

    corners = corner_detection.FAST(image=img, radius=3, threshold=90, n=0.7)

    plt.subplot(223)
    plt.title('threshold=90')
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');

    corners = corner_detection.FAST(image=img, radius=3, threshold=120, n=0.7)

    plt.subplot(224)
    plt.title('threshold=120')
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');



Działanie dla różnych wartości n:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. jupyter-execute::
    :hide-code:
    
    corners = corner_detection.FAST(image=img, radius=3, threshold=70, n=0.6)

    plt.subplot(221)
    plt.title('n=0.6')
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');

    corners = corner_detection.FAST(image=img, radius=3, threshold=70, n=0.7)

    plt.subplot(222)
    plt.title('n=0.7')
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');

    corners = corner_detection.FAST(image=img, radius=3, threshold=70, n=0.8)

    plt.subplot(223)
    plt.title('n=0.8')
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');

    corners = corner_detection.FAST(image=img, radius=3, threshold=70, n=0.9)

    plt.subplot(224)
    plt.title('n=0.9')
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');

Działanie na przykładowych obrazach:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. jupyter-execute::

    img_color = cv2.imread('datasets/Venus/frame10.png')
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    corners = corner_detection.FAST(image=img, radius=3, threshold=80, n=0.7)

.. jupyter-execute::
    :hide-code:

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

    corners = corner_detection.FAST(image=img, radius=3, threshold=80, n=0.7)

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

    corners = corner_detection.FAST(image=img, radius=3, threshold=80, n=0.7)

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

    corners = corner_detection.FAST(image=img, radius=3, threshold=80, n=0.7)

    plt.subplot(121)
    plt.imshow(img_color)
    plt.axis('off');
    plt.subplot(122)
    plt.imshow(corner_detection.draw_corners(img_color, corners))
    plt.axis('off');