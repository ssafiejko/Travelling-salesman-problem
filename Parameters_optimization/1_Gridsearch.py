import pandas as pd
from Core.Simulated_Annealing import simulated_annealing
from Parameters_optimization.Dictionaries_Generators import prob_functions_dict, t_decrease_functions_dict

'''
Skrypt sprawdzający performance wszystkich możliwych kombinacji parametrów podanych przez użytkownika. Zwraca
plik .csv, gdzie każdy rekord reprezentuje uzyskany wynik oraz czas wymagany do jego uzyskania.
'''

def main():
    prob_dict = prob_functions_dict()
    temp_dict = t_decrease_functions_dict()

    starting_temperatures = [15000]  # Lista temperatur początkowych

    # Lista nazw plików
    file_names = ['data/br17.atsp', 'data/ft53.atsp','data/ft70.atsp','data/ftv33.atsp','data/ftv35.atsp','data/ftv38.atsp',
                  'data/ftv44.atsp','data/ftv47.atsp','data/ftv55.atsp','data/ftv64.atsp',
                  'data/ftv70.atsp','data/ftv170.atsp','data/kro124p.atsp','data/p43.atsp','data/rbg323.atsp','data/rbg358.atsp',
                  'data/rbg403.atsp','data/rbg443.atsp', 'data/ry48p.atsp']

    min_temperature = 0.1  # Minimalna temperatura, określa potencjalny czas trwania algorytmu

    df = pd.DataFrame(columns=['file_name', 'prob_function', 'prob_parameter', 'temp_function',
                               'cool_parameter', 'T_init', 'function_result', 'time', 'path'])

    for file_name in file_names:
        for prob_function in prob_dict:
            for prob_parameter in prob_dict[prob_function]:
                for temp_function in temp_dict:
                    for cool_parameter in temp_dict[temp_function]:
                        for T_init in starting_temperatures:
                            print(cool_parameter)
                            # Append the row to the DataFrame
                            path, function_result, time = simulated_annealing(T_init=T_init, T_function=temp_function,
                                                                              cool_parameter=cool_parameter,
                                                                              Prob_function=prob_function,
                                                                              prob_parameter=prob_parameter,
                                                                              break_point=min_temperature,
                                                                              file_name=file_name)
                            row = {'file_name': file_name,
                                   'prob_function': prob_function.__name__,
                                   'prob_parameter': prob_parameter,
                                   'temp_function': temp_function.__name__,
                                   'cool_parameter': cool_parameter,
                                   'T_init': T_init,
                                   'function_result': function_result,
                                   'time': time,
                                   'path': path}
                            df = df.append(row, ignore_index=True)
                            print(file_name)

    df.to_csv('WYNIKOSTATECZNY.csv', index=False)