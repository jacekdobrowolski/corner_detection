Estymacja przesunięcia śledzonych narożników
--------------------------------------------

Lucas-Kanade
=============

Metoda Lucas-Kanade:raw-latex:`\cite{Lucas-Kanade}` jest szeroko
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
