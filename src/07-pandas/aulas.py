"""Aulas Pandas Exemplo"""

import pandas as pd

data = pd.read_csv(
    'datasets/GasPricesinBrazil_2004-2019.csv', sep=';')

print(data.head())
print(data.info())


estados = data['ESTADO']
estados_alternativo = data.ESTADO
estados_loc = data.loc[:, 'ESTADO']


data['PREÇO MÉDIO REVENDA (dólares)'] = data['PREÇO MÉDIO REVENDA'] * 5.13


data['STATUS'] = 'PROCESSADO'


filtro_sp = (data['ESTADO'] == 'SAO PAULO') & (data['PREÇO MÉDIO REVENDA'] > 2)
postos_sp = data[filtro_sp]

rj_ou_sp = data.query('ESTADO == "RIO DE JANEIRO" or ESTADO == "SAO PAULO"')

postos_sp_reset = postos_sp.reset_index(drop=True)


print(data.isnull().sum())

data.dropna(inplace=True)


print(data.describe())


media_por_regiao = data.groupby('REGIÃO')['PREÇO MÉDIO REVENDA'].mean()
print(media_por_regiao)


resumo = data.groupby(['REGIÃO', 'PRODUTO'])[
    'PREÇO MÉDIO REVENDA'].agg(['mean', 'max', 'min'])
print(resumo)
