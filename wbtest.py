import random
import math


# Funkcja zwracająca koszt dla danego rozwiązania
def oblicz_koszt(rozwiazanie, odleglosc):
    # Zwracamy sumę odległości między kolejnymi miastami w rozwiązaniu
    koszt = 0
    for i in range(len(rozwiazanie) - 1):
        koszt += odleglosc[rozwiazanie[i]][rozwiazanie[i + 1]]
    # Dodajemy koszt drogi powrotnej do pierwszego miasta
    koszt += odleglosc[rozwiazanie[-1]][rozwiazanie[0]]
    return koszt


# Funkcja zwracająca prawdopodobieństwo przejścia do gorszego rozwiązania
def prawdopodobienstwo(C1, C2, T):
    return math.exp(-(C2 - C1) / T)

def read_atsp_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

        # Extract the dimension of the problem
        for line in lines:
            if line.startswith('DIMENSION'):
                n = int(line.strip().split()[1])
                break

        # Extract the matrix
        matrix = []
        row = []
        start_reading = False
        for line in lines:
            if line.startswith('EDGE_WEIGHT_SECTION'):
                start_reading = True
                continue
            if start_reading:
                row.extend(list(map(int, line.strip().split())))
                if len(row) == n:
                    matrix.append(row)
                    row = []
                if len(matrix) == n:
                    break

    return matrix

def simulated_annealing(T_init, T_function, Prob_function, Break_point, file_name):
    odleglosc = read_atsp_file(file_name)
    miasta = [i for i in range(len(odleglosc))]
    # Parametry algorytmu
    liczba_iteracji = 1000000000000000  # liczba iteracji

    # Losujemy początkowe rozwiązanie
    S = random.sample(range(len(miasta)), len(miasta))
    print(S)
    for i in range(len(S)):
        if S[i] > len(odleglosc):
            print('Ale gowno' + f'{i}')
    # Pętla główna algorytmu
    C1, C2 = 0, 0
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
            p = Prob_function(C1, C2, T_init)
            if random.random() < p:
                S = S_p

        # Zmniejszamy temperaturę
        T_init = T_function(T_init)
        if T_init < Break_point:
            break

    # Zwracamy najlepsze znalezione rozwiązanie
    najlepsze_rozwiazanie = [miasta[i] for i in S]
    return najlepsze_rozwiazanie, min(C2,C1)

def test(a):
    a *= 0.9999
    return a

def main():
    a, b = simulated_annealing(10000, test, prawdopodobienstwo, 0.000001, 'rbg323.atsp')
    print(a)
    print(b)
if __name__ == '__main__':
    main()