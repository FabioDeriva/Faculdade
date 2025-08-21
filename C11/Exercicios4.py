import numpy as np

#Exercicio 1
arr = np.ones(8)
arr2 = np.random.randint(0, 9, 8)
arr3 = arr + arr2

if arr3.sum() >= 40:
    matriz = arr3.reshape(4,2)

else:
    matriz = arr3.reshape(2,4)

print('A Nova Matriz fica: \n' ,matriz)

#Exercicio 2

arrPar =  np.arange(0,51,2)
arrParReg = np.arange(100, 50, -2)

arrConcatenado = np.concatenate((arrPar, arrParReg))
print(np.sort(arrConcatenado))

#Exercicio 3

#a) criar a 2x2 formado apenas de 0
matriz = np.array([[0,0], [0,0]])

#b) adicionar o 1 numa posição aleatoria
linha  = np.random.randint(0,2)
coluna = np.random.randint(0,2)
matriz[linha, coluna] = 1

#c)Fazer o usuario escolher uma posição
tentativas = 0 
maxDeTentaivas = 3
posicoesOcultas =[[False, False] , [False, False]]
while tentativas < maxDeTentaivas:


    print("Escolha uma das posições: ")
    linha = input('0 ou 1 ')
    coluna = input('0 ou 1 ')

    if linha not in  ['0', '1'] or coluna not in ['0', '1']:
        print("Numero invalido")
        continue

    linha = int(linha)
    coluna = int(coluna)

    if posicoesOcultas[linha][coluna]:
        print('posição já foi selecionada anteriormente')
        continue

    posicoesOcultas[linha][coluna] = True
    tentativas += 1
    posicaoRevelada = matriz[linha][coluna]

    print(f'Posição [{linha}, {coluna}] revelada: {posicaoRevelada}')

    if posicaoRevelada == 1:
        print('EXPLODIU!!!!')
        break

    posicoesSemBomba = 0
    for i in range(2):
        for j in range(2):
            if matriz[i][j] == 0 and posicoesOcultas[i][j]:
                posicoesSemBomba += 1
    
    if posicoesSemBomba ==3:
        print("Vc venceu!")
        break

#Exercicio 4
seed_rand = np.random.seed(10)
arr_4x4 = np.random.randint(1, 51, 16)
mtz_4x4 = arr_4x4.reshape(4, 4)
print('matriz:\n', mtz_4x4)

#a)media de cada linha e coluna da matriz
mediaLinhas = np.mean(mtz_4x4, axis=1)
print('\nMédia de cada linha:', mediaLinhas)

mediaColunas = np.mean(mtz_4x4, axis=0)
print('\nMedia de cada coluna:', mediaColunas)

#b)maior numero das medias das linhas e colunas

print('\nMaior número da média de linhas:', mediaLinhas.max())

print('\nMaior número da média colunas:', mediaColunas.max())

#c) Mostre a quantidade de aparições de cada um dos numeros gerados na matriz e depois os que aparecem 2x
valores, contagens = np.unique(mtz_4x4, return_counts=True)

print(f"Vezes que aparecem: ")
for valor, count in zip(valores, contagens):
    print(f"Numero {valor} | aparece {count}")

numeros2Vezes = valores[contagens == 2]
print(f"Números que aparecem 2x: {numeros2Vezes}")