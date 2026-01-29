# %%
import pandas as pd
# %%
pd.Series()
# %%
idades = [39, 30, 27, 18, 9, 6, 4, 40, 13, 22, 18, 18, 27, 25, 
        26, 31, 45, 29, 41, 60, 50, 80, 90, 17, 22]
serie_idades = pd.Series(idades)
serie_idades
# %%
media_idades = serie_idades.mean()
varianca_idades = serie_idades.var()
desvio_padrao_idades = serie_idades.std()
print(f'Média das idades: {media_idades}')
print(f'Variância das idades: {varianca_idades}')
print(f'Desvio padrão das idades: {desvio_padrao_idades}')

# %%
diffs = 0
for i in idades:
    diffs += (i - media_idades) ** 2
varianca_manual = diffs / (len(idades) - 1)
print(f'Variância calculada manualmente: {varianca_manual}')
# %%
sumario = serie_idades.describe()
sumario