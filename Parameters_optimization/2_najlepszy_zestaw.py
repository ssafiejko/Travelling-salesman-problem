import pandas as pd

'''
W obrębie jednego problemu skaluje min-max na [0,1] koszt funkcji dla danych parametrów.
Wówczas scaled_res można interpretować jako unormowaną odległość od najlepszego rozwiązania.
Szukamy takich parametrów, dla których średnia odległość po wszytskich rozważanych problemach będzie 
najmniejsza. Funckja zwraca i (domyślnie 10) najlepszych zestawów.
'''

def find_best_params(results_df:pd.DataFrame, i=10):

    df = results_df.copy()
    df = df.fillna('-')
    df = df.drop(['path', 'time'], axis=1)

    df['scaled_res'] = df.groupby('file_name')['function_result'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))

    


    df['mean_scaled_res'] = df.groupby(['prob_function', 'prob_parameter', 'temp_function',
                        'cool_parameter', 'T_init'])['scaled_res'].transform('mean')
    
    
    df_dropped = df.drop(['file_name', 'scaled_res', 'function_result'], axis=1)
    df_dropped_duplicates = df_dropped.drop_duplicates()
    
    df_dropped_duplicates = df_dropped_duplicates.sort_values(by=['mean_scaled_res'])


    return df_dropped_duplicates.head(i)


def main():
    pd.set_option('display.max_rows', None)
    df = pd.read_csv('test.csv')

    print(find_best_params(df,5))


if __name__ == '__main__':
    main()