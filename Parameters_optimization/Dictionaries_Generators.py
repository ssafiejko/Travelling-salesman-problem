import math

"""
Zestaw dwóch funkcji zwracających słownik, gdzie kluczami są funkcje odpowiednio chłodzenia oraz prawdopodobieństwa,
natomiast wartościami - zestaw parametrów dla danej funkcji. Poniższe funkcje wykorzystywane są do zbadania jaki
zestaw funkcji i parametrów optymalizuje najlepiej asymetryczny problem komiwojażera przy zastosowanej w projekcie
implementacji symulowanego wyżarzania.
"""

# Funkcja generująca słownik funkcji określającej
# Prawdopodobieństwo przyjęcia kandydata
# Słownik ma postać {funkcja: lista_parametrów}
def prob_functions_dict():

    def metropolis_probability(delta_e, temperature, prob_parameter=None):
        return min(1, math.exp(-delta_e / temperature))

    def boltzmann_probability(delta_e, temperature, prob_parameter=None):
        return math.exp(-delta_e / temperature)

    def exponential_decrease_probability(delta_e, temperature, prob_parameter):
        return math.exp(-prob_parameter * delta_e / temperature)

    def gaussian_probability(delta_e, temperature, prob_parameter):
        return math.exp(-(delta_e ** 2) / (2 * (prob_parameter ** 2) * temperature))

    def power_law_probability(delta_e, temperature, prob_parameter):
        return 1 / ((delta_e + 1) ** prob_parameter * temperature)

    decay_factors = [0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6]

    sigma_factors = [0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1, 1.5, 2, 2.5, 3]

    alpha_factors = [0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 1, 1.5, 2, 3, 4]

    return {metropolis_probability: [None], boltzmann_probability: [None],
            exponential_decrease_probability: alpha_factors,
            gaussian_probability: sigma_factors, power_law_probability: decay_factors}

# Funkcja generująca słownik funkcji określającej
# Zmianę temperatury wraz z działaniem algorytmu
# Słownik ma postać {funkcja: lista_parametrów}
def t_decrease_functions_dict():

    def linear_decrease(Top_T, T, iteration, cool_parameter):
        return T * cool_parameter

    def exponential_cooling(T_init, T, iteration, cool_parameter):  # około 0.05
        return T_init * math.exp(-cool_parameter * iteration)

    linear_parameters = [0.99999, 0.999999, 0.9999999]

    exp_parameters = [0.001, 0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
    return {
        exponential_cooling: exp_parameters,
        linear_decrease: linear_parameters
            }