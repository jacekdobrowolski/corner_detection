===================================================================================
Dokumentacja Projektu
===================================================================================

Wstęp
==============

Początkowo projekt miał być aplikacją nanoszącą rezultat pracy algorytmu optical flow na strumień wideo.
Jednak wraz z postępem projektu okazalo się że taki projekt z początkowymi założeniami mógł by działać
(bez nadmiernej pracy) jedynie na systemie linux. Dodatkowo prosta implementacja algorytmu nie dała by
sobie rady z liczbą klatek na sekundę jakie są wymagane od płynnego odtwazania wideo.
Dlatego na pewnym etapie zdecydowałem że projekt będzie implementacją 3 algorytmów wykrywających narożniki
i algorytmu optical flow metodą Lucas Kanade. Wyposarzoną w dokumentację prezentującą ich działanie dla różnych
parametrów i obrazów.

Funkcjonalność
===============

-  Wykrywanie dobrych punktów do śledzenia w obrazie

-  Odnajdowanie przesunięcia śledzonych narożników

Dane wejściowe
===============

-  Klatki nagrania

-  Parametry wejścowe algorytmów

Narzędzia
==========

-  Python

-  NumPy

-  OpenCV

-  Scipy

   Początkowo biblioteka Scipy nie znalazła się w wykazie.
   Okazało się jednak że jest tam niezbędna implementacja splotu dwuwymiarowego.

Co zostało zrobione w ramach projektu
==========================================

W ramach projektu zaimplementowane zostały 3 algorytmy wykrywania krawędzi.

 - Shi-Tomasi :cite:`Shi-Tomasi`

 - Harris-Stephens :cite:`Harris`

 - FAST :cite:`FAST`

Oraz zaimplementowana została metoda Lucas-Kanade :cite:`Lucas-Kanade`
służąca do wyznaczania przesunięcia się fragmentów obrazu.

Projekt w obecnym stanie może zostac użyty jako moduł języka Python.
Jego działanie i sposób użycia można jednak zobaczyć w dalszej części dokumentacji.


Dalszy rozwój
===============

Projekt może zostać rozbudowany o prostą stabilizacje obrazu. Opartą na
wygładzaniu ruchu kamery poprzez odkształcanie obrazu.

Stworzona implementacja jest powolna i raczej nie nadaje się do użytku poza nauką.
Można jednak znacznie poprawić jego działanie poprzez optymalizację lub użycie kilku
procesów w kluczowych częściach.

Co nie zostało wykonane
========================

Implementacja Lucas Kanade jest niezbyt dobra poniważ nie wykorzystuje metody piramid.
A jej wynik działania nie są zbyt zadowalające.

Dokumentacja
===============

.. toctree::
   corner_detection
   optical_flow
   misc
   data_flow
   bibliography
   :maxdepth: 2

