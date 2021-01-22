Problem przesłony
===========================

Metoda Lucas Kanade jest podatna na problem przesłony jest to zjawisko
kiedy określenie kierunku ruchu nie jest możliwe na podstawie jego
drobnego wycinka. Efekt jest zobrazowany na poniższej ilustracji.

.. figure:: _static/aparature_efect.png
   :alt: problem przesłony
   :align: center

   *Ilustracja obrazująca efekt przysłony*

Piramidy i iteracje
============================

W literaturze można spotkać się z określeniem piramid. Jest to porostu
metoda poprawienia działania algorytmu Lucas-Kanade poprzez obliczanie
wektora najpierw dla obniżonej rozdzielczości. A następnie dla coraz
większej. Ma to na celu zmniejszenie szumu i losowości w miejscach gdzie
wyznaczenie przesunięcia nie jest możliwe. Można spodziewać się
poprawienia trafności algorytmu stosując piramidy.

Badanie działania algorytmów
==============================

Najprostszą miarą badającą złożoność obliczeniową są uzyskane klatki na
sekundę. Wadą takiego pomiaru jest duży wpływ implementacji. Inne miary
jakich planuje użyć sa empiryczne. Istnieją specjalne zestawy danych
rzeczywistych i syntetycznych, jednak porównanie działania algorytmów na
nich zostało już wykonane.

Dalszy rozwój projektu
===============================

Projekt może zostać rozbudowany o prostą stabilizacje obrazu. Opartą na
wygładzaniu ruchu kamery poprzez odkształcanie obrazu.
