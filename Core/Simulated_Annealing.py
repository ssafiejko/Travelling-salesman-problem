import random
import time
from Core.ATSP_file_reader import read_atsp_file

''' 
Funkcja symulowanego wyżarzania przyjmująca jako parametry wszystkie możliwe zmienne w ramach przyjętej
implementacji. Race_mode ogranicza czas działania algorytmu do 5 minut.
'''
def simulated_annealing(T_init, T_function, cool_parameter,
                        Prob_function, prob_parameter,
                        break_point, file_name, race_mode=False):

    # Funkcja zwracająca koszt dla danego rozwiązania
    def oblicz_koszt(rozwiazanie, odleglosc):
        # Zwracamy sumę odległości między kolejnymi miastami w rozwiązaniu
        koszt = 0
        for i in range(len(rozwiazanie) - 1):
            koszt += odleglosc[rozwiazanie[i]][rozwiazanie[i + 1]]
        # Dodajemy koszt drogi powrotnej do pierwszego miasta
        koszt += odleglosc[rozwiazanie[-1]][rozwiazanie[0]]
        return koszt

    start = time.time()
    odleglosc = read_atsp_file('data/' + file_name)
    miasta = [i for i in range(len(odleglosc))]

    liczba_iteracji = 10  # liczba iteracji

    # Losujemy początkowe rozwiązanie
    S = random.sample(range(len(miasta)), len(miasta))

    # Pętla główna algorytmu
    C1, C2 = 0, 0
    T = T_init

    global_min = float('inf')
    global_min_path = []

    for i in range(liczba_iteracji):

        # Losujemy dwa miasta i zamieniamy je miejscami
        S_p = S.copy()
        a = random.randint(0, len(S_p) - 1)
        b = random.randint(0, len(S_p) - 1)
        S_p[a], S_p[b] = S_p[b], S_p[a]

        # Obliczamy koszty dla obu rozwiązań
        C1 = oblicz_koszt(S, odleglosc)
        C2 = oblicz_koszt(S_p, odleglosc)

        # Sprawdzamy czy akceptujemy nowe rozwiązanie
        if C2 < C1:
            S = S_p

        else:
            delta_e = abs(C1-C2)
            p = Prob_function(delta_e, T, prob_parameter)
            if random.random() < p:
                S = S_p

        # Zmniejszamy temperaturę
        T = T_function(T_init, T, i, cool_parameter)
        if T < break_point:
            break

        if oblicz_koszt(S, odleglosc) < global_min:
            global_min_path = [miasta[i] for i in S]
            global_min = oblicz_koszt(S, odleglosc)

        if race_mode:
            end = time.time()
            if end-start > 300:
                return global_min_path, global_min, end - start

    end = time.time()

    # Sciezka, koszt, czas
    return global_min_path, global_min, end - start
