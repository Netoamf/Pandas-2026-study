# %%
import pandas as pd
# %%
idades = [39, 30, 27, 18, 9, 6, 4, 40, 13, 22, 18, 18, 27, 25, 
        26, 31, 45, 29, 41, 60, 50, 80, 90, 17, 22]
serie_idades = pd.Series(idades)
serie_idades
#%%
serie_idades[1] 
# %%
serie_idades[0:5]
serie_idades[5:]
serie_idades[:10]
# %%
serie_idades = serie_idades.sort_values()
serie_idades
# %%
serie_idades.iloc[0:5]
# Observe que o iloc funciona com o índice posicional.
# Enquanto o indice tradicional de uma series em pandas funciona como uma chave, o iloc permite acessar os elementos pela sua posição.
# %%
serie_idades.iloc[-5:]
# %%
serie_idades.iloc[-1]
# %%
idades = [39, 30, 27, 18, 9, 6, 4, 40, 13, 22, 18, 18, 27, 25, 
        26, 31, 45, 29, 41, 60, 50, 80, 90, 17, 22]

indexes = [
    'idade_1', 'idade_2', 'idade_3', 'idade_4', 'idade_5',
    'idade_6', 'idade_7', 'idade_8', 'idade_9', 'idade_10',
    'idade_11', 'idade_12', 'idade_13', 'idade_14', 'idade_15',
    'idade_16', 'idade_17', 'idade_18', 'idade_19', 'idade_20',
    'idade_21', 'idade_22', 'idade_23', 'idade_24', 'idade_25'
]
serie_idades = pd.Series(idades, index=indexes)
serie_idades
# %%
serie_idades['idade_10']