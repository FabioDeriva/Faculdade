####################################################################################

#EX4
distancia = float(input('Digite a distancia da sua viagem em KM: '))

if distancia <= 200: 
    preçoPassagem = 0.5*distancia

else:
    preçoPassgem = 0.45*distancia

print('O preço de sua passagem será: ', preçoPassagem)

####################################################################################

#EX5

numero = int(input("Qual o numero vc deseja checar? "))

while numero < 1000 or numero > 9999:
    numero = int(input("Digite um numero valido "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = numero // 1000

print("Unidade:", unidade)
print("Dezena:", dezena)
print("Centena:", centena)
print("Milhar:", milhar)

####################################################################################

#EX6

import math

num = float(input("Digite um número decimal: "))

raiz = math.sqrt(num)
teto = math.ceil(num)
chao = math.floor(num)
parte_inteira = int(num)

print("Raiz quadrada:", raiz)
print("Função teto:", teto)
print("Função chão:", chao)
print("Parte inteira:", parte_inteira)
