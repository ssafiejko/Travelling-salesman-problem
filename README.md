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
