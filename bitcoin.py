import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
import numpy.polynomial as Polynomial

df = pd.read_csv('GasPricesinBrazil_2004-2019.csv', sep=';')

dfFilter = df[(df['ESTADO'] == 'SAO PAULO') & (df['PRODUTO'] == 'GASOLINA COMUM')]
dfFilter['DATA FINAL'] = pd.to_datetime(dfFilter['DATA FINAL'])

dfFilter['DATA FINAL'] = dfFilter['DATA FINAL'].dt.year

dataUtils = {}

for year in dfFilter['DATA FINAL'].unique():
    prices = dfFilter[dfFilter['DATA FINAL'] == year]['PREÇO MÉDIO REVENDA'].values
    dataUtils[year] = np.mean(prices)

media_global = np.mean(list(dataUtils.values()))
erro_quadratico = []

for i in dataUtils.values():
    erro_quadratico.append((media_global - i)**2)

a, b = np.polyfit(list(dataUtils.keys()), list(dataUtils.values()), deg=1)

prices_linear = []
quadratico_linear = []
for year in dataUtils.keys():
    prices_linear.append(a * year + b)
    quadratico_linear.append((a * year + b - media_global)**2)


mp.scatter(dataUtils.keys(), dataUtils.values(), label='Preços Originais', color='blue')
mp.scatter(dataUtils.keys(), prices_linear, label='Preços Ajustados Linearmente', color='red')
mp.scatter(dataUtils.keys(), erro_quadratico, label='Erro Quadrático', color='green')
mp.scatter(dataUtils.keys(), quadratico_linear, label='Erro Quadrático Linear', color='purple')

for x, y in zip(dataUtils.keys(), dataUtils.values()):
    mp.text(x, y, f'{y:.2f}', fontsize=6, ha='right', color='blue')

for x, y in zip(dataUtils.keys(), prices_linear):
    mp.text(x, y, f'{y:.2f}', fontsize=6, ha='right', color='red')

for x, y in zip(dataUtils.keys(), erro_quadratico):
    mp.text(x, y, f'{y:.2f}', fontsize=6, ha='right', color='green')

for x, y in zip(dataUtils.keys(), quadratico_linear):
    mp.text(x, y, f'{y:.2f}', fontsize=6, ha='right', color='purple')


mp.title('Análise de Preços de Gasolina - Pará')
mp.xlabel('Ano')
mp.ylabel('Preço / Erro Quadrático / Erro Quadrático Linear')
mp.legend()

mp.show()