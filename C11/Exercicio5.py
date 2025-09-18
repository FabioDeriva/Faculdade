#EX1
import pandas as pd
import numpy as np          

seriesAno1 = pd.Series({'Java': 16.5, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

print(seriesAno1, '\n')
print(seriesAno2, '\n')
#EX2

print('Total do ano 1: ' , seriesAno1.sum())
print('Total do ano 2 ' , seriesAno2.sum(), '\n')

#Ex3
variacao = seriesAno2 - seriesAno1
print('Variação: \n', variacao, '\n')

#EX4
variacaoPositivo = variacao[variacao > 0]
print('Variação positiva: \n', variacaoPositivo, '\n')

#EX5
projecao = seriesAno2 + (variacao*2)
linguagemMaisPopular = projecao.nlargest(1)
print("Linguagem mais popular projetada:\n", linguagemMaisPopular)

#Parte2

#EX1
np.random.seed(10)
df = pd.DataFrame(
index=['A', 'B', 'C', 'D', 'E'],
columns=['W', 'X', 'Y', 'Z'],
data=np.random.randint(1, 50, [5, 4]))

dfX = df['X']
mediaMenor30 = df.loc[dfX < 30, 'X'].mean()
print("Média dos menores que 30: ", mediaMenor30, '\n')

#EX2
dfMediaD = df.loc['D'].mean()
print("Média D:", dfMediaD)

dsSomaE = df.loc['E'].sum()
print("Soma E:", dsSomaE, '\n')

#EX3 
sliceACEeXY = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print(sliceACEeXY)

somandoAsLinhas = sliceACEeXY.sum(axis=1)
print("Soma linhas:\n", somandoAsLinhas)

somandoAsColunas = sliceACEeXY.sum(axis=0)
print("Soma colunas:\n", somandoAsColunas)