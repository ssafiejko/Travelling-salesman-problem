# Travelling-salesman-problem

Wybrany algorytm- symulowane wyżarzanie

Opis algorytmu:

Losujemy początkowe rozwiązanie, na przykład drogę, oznaczając ją jako S.
Następnie wykonujemy następujące kroki, aż osiągniemy wymaganą liczbę iteracji lub zauważymy, że wynik nie poprawia się już przez dłuższy czas:

1. Wybieramy dwa losowe miasta i zamieniamy je miejscami, aby otrzymać nowe rozwiązanie S'.

2. Obliczamy koszt C(S') nowego rozwiązania.

3. Jeśli C(S') jest mniejsze niż C(S), to przyjmujemy nowe rozwiązanie i ustawiamy S na S'. W przeciwnym przypadku, przyjmujemy nowe rozwiązanie z pewnym prawdopodobieństwem P(C(S), C(S'), T), gdzie T to parametr temperatury.

4. Zmniejszamy wartość parametru temperatury T.

Po wykonaniu iteracji zwracamy najlepsze znalezione rozwiązanie.

# Sciezka sciezeczka ftv38
[3, 38, 2, 4, 35, 33, 30, 26, 23, 24, 36, 21, 22, 25, 31, 32, 34, 29, 28, 27, 20, 13, 12, 11, 15, 6, 7, 5, 8, 37, 9, 10, 16, 14, 17, 18, 19, 0, 1]
1652


# Sciezka sciezeczka ft70
[29, 23, 56, 54, 52, 51, 50, 17, 16, 15, 6, 38, 35, 42, 41, 40, 36, 39, 37, 69, 65, 68, 67, 63, 66, 64, 21, 27, 24, 28, 30, 34, 32, 12, 14, 10, 9, 11, 7, 13, 8, 20, 18, 19, 46, 45, 49, 47, 55, 53, 2, 4, 22, 25, 3, 5, 1, 0, 26, 33, 31, 62, 61, 60, 59, 58, 57, 44, 48, 43]
40286
