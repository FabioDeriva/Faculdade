####################################################################################

#EX1
nome = "Fabio Miguel Calo Cruz"

print('Seu nome em letras maiúsculas:', nome.upper())

print('Seu nome em letras minusculas:', nome.lower())

nome_junto = nome.replace(" ", "")
print('Quantas letras tem seu nome:', len(nome_junto))

print('Seu nome final trocado por "do inatel":', nome.replace("Cruz", "do inatel"))

####################################################################################

#EX2
numero = int(input("Digite o numero que, vc deseja ver a tabuada: "))

n = int(input("Digite o intervalo da tabuada que vc deseja ver: "))

i = 1

while i <= n:
    print(numero*i)
    i += 1

####################################################################################

#EX3

sexo = input('Digite seu sexo M(masculino) ou F(feminino): ')
sexo_tratado = sexo.upper()

while sexo_tratado != 'M' and sexo_tratado != 'F':
    print("Sexo inválido. Tente novamente.")
    sexo = input('Digite seu sexo M(masculino) ou F(feminino): ')
    sexo_tratado = sexo.upper()

if sexo_tratado == 'M':
    print('Você é homem!')

else:
    print('Você é mulher!')

