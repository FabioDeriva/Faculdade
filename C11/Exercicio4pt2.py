import numpy as np
ds = np.loadtxt('space.csv', 
                delimiter=';', 
                dtype=str, 
                encoding='utf-8')


#Porcentagem que deram certo
ds_status = ds[:, 7]

total = len(ds_status)

sucessos = np.char.find(ds_status, 'Success') >= 0

sucessosTotal = sucessos.sum()

print('missões deram certo')
print(f"{(sucessosTotal/total)*100:.2f}% de sucesso\n")

#Qual a media de gastos de uma missão espacial se baseando em missões que possuam valores disponíveis (>0)?
gastosPorMissão = ds[1:,6].astype(float)

gastosMissãoValidos = gastosPorMissão[gastosPorMissão > 0]

gastoMedio = gastosMissãoValidos.mean()

print('A média de gastos foi de:')
print(f"${gastoMedio:.2f} Milhoes\n")

#Encontre quantas missões foram realizadas pelos Estados Unidos (EUA)
paisDaMissao = ds[:, 2]

missaoUSA = np.char.find(paisDaMissao, 'USA') >= 0

contadorDasMissoes = missaoUSA.sum()

print(contadorDasMissoes, 'missões feitas pelos EUA \n')

#Missão Mais cara da spaceX
empresaDaMissao = ds[1:, 1]
gastosPorMissão = ds[1:,6].astype(float)

associarNomeCusto = empresaDaMissao == 'SpaceX'
gastosSpaceX = gastosPorMissão[associarNomeCusto]
maiorGasto = gastosSpaceX.max()

print(f"${maiorGasto} Milhoes \n")

#Empresas que ja fizeram viagens e suas quantidades
missoesRealizadasEmpresas = np.unique(empresaDaMissao)

for missoesRealizadas in missoesRealizadasEmpresas:
    filtro = empresaDaMissao == missoesRealizadas
    numMissoes = filtro.sum()
    print(f"{missoesRealizadas}: {numMissoes} missoes")
