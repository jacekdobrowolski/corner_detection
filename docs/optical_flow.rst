Estymacja przesunięcia śledzonych punktów
----------------------------------------------

Lucas-Kanade
=============

Metoda Lucas-Kanade :cite:`Lucas-Kanade` jest szeroko
stosowana w wizji komputerowej. Polega na założeniu że ruch w sąsiednich
pixeli przebiega w jednym kierunku. Jako metoda o działaniu lokalnym nie
radzi sobie z wyznaczaniem ruchu dla regionów o jednakowej
intensywności. Dlatego jako dane wejściowe podajemy dobre punkty do
śledzenia. Metoda ta zakłada również nie wielki ruch między
poszczególnymi klatkami. Wynikają z tego pewne ograniczenia takie jak
słabe działanie dla szybkich obiektów lub konieczność szybszego
próbkowania obrazu. Algorytm wyznacza wektor który najlepiej opisuje
ruch danego wycinka obrazu.

.. math::

   \begin{matrix}
               I_{x}(q_{1})V_{x}+I_{y}(q_{1})V_{y}=-I_{t}(q_{1}) \\
               I_{x}(q_{2})V_{x}+I_{y}(q_{2})V_{y}=-I_{t}(q_{2}) \\
               \vdots  \\ 
               I_{x}(q_{n})V_{x}+I_{y}(q_{n})V_{y}=-I_{t}(q_{n}) \\
           \end{matrix}

Gdzie :math:`V_x` to współrzędna pozioma wektora ruchu regionu a
:math:`V_y` to współrzędna pionowa tegoż wektora.
:math:`q_1, q_2, \dots q_n` to pixele wewnątrz regionu. A
:math:`I_{x}(q_{i}),I_{y}(q_{i}),I_{t}(q_{i})` to pochodne cząstkowe
intensywności obrazu. Równanie to można zapisać w formie macierzowej
jako. :math:`\mathbf{A}v=b` gdzie:

.. math::

   {\displaystyle 
           \mathbf{A}={
           \begin{bmatrix}
               I_{x}(q_{1})&I_{y}(q_{1})\\
               I_{x}(q_{2})&I_{y}(q_{2})\\
               \vdots &\vdots \\
               I_{x}(q_{n})&I_{y}(q_{n})
           \end{bmatrix}}
           \quad \quad \quad 
           v={
           \begin{bmatrix}
               V_{x}\\
               V_{y}
           \end{bmatrix}
           }\quad \quad \quad 
           b={
           \begin{bmatrix}
               -I_{t}(q_{1})\\
               -I_{t}(q_{2})\\
               \vdots \\
               -I_{t}(q_{n})
           \end{bmatrix}}}

Jest to zwykle układ nadokreślony metoda Lucas-Kanade przybliża wynik
metodą najmniejszych kwadratów.

.. math:: {\mathrm  {v}}=(\mathbf{A^{T}}\mathbf{A})^{{-1}}\mathbf{A^{T}}b


.. currentmodule:: optical_flow

.. autofunction:: lucas_kanade


Najpierw należy wczytać dopowiednie moduły oraz klatki obrazu.

.. jupyter-execute::

    %cd ..

.. jupyter-execute::

    import corner_detection
    import optical_flow
        
    import cv2
    from matplotlib import pyplot as plt
    import numpy as np

    sample_path = 'datasets/Hydrangea'

    prev_color = cv2.imread(sample_path + '/frame10.png')
    prev_color = cv2.cvtColor(prev_color, cv2.COLOR_BGR2RGB)
    prev = cv2.cvtColor(prev_color, cv2.COLOR_RGB2GRAY)

    curr_color = cv2.imread(sample_path + '/frame11.png')
    curr_color = cv2.cvtColor(curr_color, cv2.COLOR_BGR2RGB)
    curr = cv2.cvtColor(curr_color, cv2.COLOR_RGB2GRAY)

    plt.subplot(121), plt.imshow(prev_color), plt.axis('off');
    plt.subplot(122), plt.imshow(curr_color), plt.axis('off');

Następnie należy w obrazie wykryć narożniki. W tym przykładzie posłuże się metodą Shi-Tomasi.

.. jupyter-execute::

    window = np.ones((7,7))
    corners = corner_detection.shi_tomasi(prev, corner_detection.SCHARR, window, 10, 10)
    plt.imshow(corner_detection.draw_corners(prev_color, corners)), plt.axis('off');

Następnie wykryte punkty należy przekazać do funkcji lucas_kanade wraz dwiema sąsiednimi klatkami.

.. jupyter-execute::

    flow = optical_flow.lucas_kanade(prev, curr, corners, 7, corner_detection.SCHARR)

    for feature in flow:
        x = feature[0]
        y = feature[1]
        cv2.line(prev_color, (y, x), (int(x + feature[2]*200), int(y + feature[3]*200)), (0, 0,255), 2)

    plt.imshow(prev_color), plt.axis('off');

Linie odpowiadają ruchowi klatek.