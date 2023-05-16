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

# Funkcja generująca słownik funkcji określającej
# Prawdopodobieństwo przyjęcia kandydata
# Słownik ma postać {funkcja: lista_parametrów}
def prob_functions_dict():

    def metropolis_probability(delta_e, temperature, prob_parameter=None):
        return min(1, math.exp(-delta_e / temperature))

    def boltzmann_probability(delta_e, temperature, prob_parameter=None):
        return math.exp(-delta_e / temperature)

    def accept_if_better_probability(delta_e, temperature, prob_parameter=None):
        return 1 if delta_e < 0 else 0

    def exponential_decrease_probability(delta_e, temperature, prob_parameter): #alpha
        return math.exp(-prob_parameter * delta_e / temperature)

    def sigmoid_probability(delta_e, temperature, prob_parameter):
        return 1 / (1 + math.exp(-prob_parameter * delta_e / temperature)) #sigmoid

    def gaussian_probability(delta_e, temperature, prob_parameter): # z sigmami chyba można mocno kombinować
        return math.exp(-(delta_e ** 2) / (2 * (prob_parameter ** 2) * temperature))

    def power_law_probability(delta_e, temperature, prob_parameter): # decay_factor raczej jakiś taki okolo 2
        return 1 / ((delta_e + 1) ** prob_parameter * temperature)

    decay_factors = [0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6]

    sigma_factors = [0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1, 1.5, 2, 2.5, 3]

    alpha_factors = [0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 1, 1.5, 2, 3, 4]

    sigmoid_parameters = [0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 1, 1.5, 2, 3, 4]

    return {metropolis_probability: [None], boltzmann_probability: [None], accept_if_better_probability: [None],
            exponential_decrease_probability: alpha_factors, sigmoid_probability: sigmoid_parameters,
            gaussian_probability: sigma_factors, power_law_probability: decay_factors}

# Funkcja generująca słownik funkcji określającej
# Zmianę temperatury wraz z działaniem algorytmu
# Słownik ma postać {funkcja: lista_parametrów}
def t_decrease_functions_dict():

    def linear_decrease(Top_T, T, iteration, cool_parameter):
        return T * cool_parameter

    def exponential_cooling(T_init, T, iteration, cool_parameter):  # około 0.05
        return T_init * math.exp(-cool_parameter * iteration)

    linear_parameters = [0.99, 0.999, 0.9999, 0.99999, 0.999999]

    exp_parameters = [0.001, 0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

    return {linear_decrease: linear_parameters,
            
            exponential_cooling: exp_parameters}

# Funkcja czytająca format .atsp
# Zwraca macierz sąsiedztwa
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

def simulated_annealing(T_init, T_function, cool_parameter,
                        Prob_function, prob_parameter,
                        break_point, file_name):

    odleglosc = read_atsp_file(file_name)
    miasta = [i for i in range(len(odleglosc))]

    liczba_iteracji = 1000000000000000  # liczba iteracji

    # Losujemy początkowe rozwiązanie
    S = random.sample(range(len(miasta)), len(miasta))

    # Pętla główna algorytmu
    C1, C2 = 0, 0
    T = T_init

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

    # Zwracamy najlepsze znalezione rozwiązanie
    najlepsze_rozwiazanie = [miasta[i] for i in S]
    return najlepsze_rozwiazanie, min(C2,C1)

# TODO: Funkcja ewaluacji danego zestawu parametrów
def evaluate_sa():
    return

def main():
    # a, b = simulated_annealing(10000, test, prawdopodobienstwo, 0.000001, 'rbg323.atsp')

    prob_dict = prob_functions_dict()
    temp_dict = t_decrease_functions_dict()

    starting_temperatures = []  # Lista temperatur początkowych

    file_names = []  # Lista nazw plików

    min_temperature = 0.000001  # Minimalna temperatura, określa potencjalny czas trwania algorytmu

    for file_name in file_names:
        for prob_function in prob_dict:
            for prob_parameter in prob_dict[prob_function]:
                for temp_function in temp_dict:
                    for cool_parameter in temp_dict[temp_function]:
                        for T_init in starting_temperatures:
                            simulated_annealing(T_init=T_init, T_function=temp_function, cool_parameter=cool_parameter,
                                                Prob_function=prob_function, prob_parameter=prob_parameter,
                                                break_point=min_temperature, file_name=file_name)






if __name__ == '__main__':
    main()
