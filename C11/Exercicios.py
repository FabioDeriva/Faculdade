print("Exercício 1")
times = ["Real Madrid", "Manchester City", "Bayern de Munique", "Liverpool", "PSG"]

print("Top 3 primeiros colocados:", times[0:3])
print("Times nas últimas posições:", times[3:])
print("Times em ordem alfabética:", sorted(times))
if "Barcelona" in times:
    print("O Barcelona está na posição:", times.index("Barcelona") + 1)
else:
    print("Barcelona não consta na lista.")

print("Exercício 2")
loja1 = {'Galaxy S25', 'Iphone 20', 'Redmi Note 9', 'Asus RogPhone'}
loja2 = {'Iphone 20', 'Mi 10', 'byd cell', 'Moto G'}

print(f"A loja 1 possui {len(loja1)} modelos de celulares.")
print("Catálogo da loja 1:", loja1)
print(f"A loja 2 possui {len(loja2)} modelos de celulares.")
print("Catálogo da loja 2:", loja2)

todos_modelos = loja1 | loja2
print("Lista geral de modelos disponíveis:", todos_modelos)

modelos_iguais = loja1 & loja2
print("Modelos encontrados em ambas as lojas:", modelos_iguais)

modelo_busca = input("Qual modelo deseja pesquisar? ")
if modelo_busca in todos_modelos:
    lojas_encontradas = []
    if modelo_busca in loja1:
        lojas_encontradas.append("Loja 1")
    if modelo_busca in loja2:
        lojas_encontradas.append("Loja 2")
    print(f"O modelo {modelo_busca} está disponível nas seguintes lojas:")
    for loja in lojas_encontradas:
        print("-", loja)
else:
    print("O modelo não está disponível em nenhuma loja.")

print("Exercício 3")
aluno_nome = input("Digite o nome do estudante: ")
media_final = float(input("Digite a média final do estudante: "))

if media_final >= 50:
    print("APROVADO")
else:
    print("REPROVADO")

dados_aluno = {'nome': aluno_nome, 'média': media_final}
print("Registro do estudante:", dados_aluno)

print("Exercício 4")
nomes_pacientes = []
pesos_pacientes = []

for _ in range(3):
    paciente_nome = input("Nome do paciente: ")
    paciente_peso = float(input("Peso do paciente (kg): "))
    nomes_pacientes.append(paciente_nome)
    pesos_pacientes.append(paciente_peso)

print("O paciente mais pesado é:", nomes_pacientes[pesos_pacientes.index(max(pesos_pacientes))])
print("O paciente mais leve é:", nomes_pacientes[pesos_pacientes.index(min(pesos_pacientes))])

print("Exercício 5")
pessoas = []
soma_idades = 0
mulheres_menos_20 = 0

quantidade = int(input("Quantas pessoas serão cadastradas? "))
for _ in range(quantidade):
    nome_pessoa = input("Nome: ")
    idade_pessoa = int(input("Idade: "))
    soma_idades += idade_pessoa

    while True:
        sexo_pessoa = input("Sexo (M ou F): ").upper()
        if sexo_pessoa in ['M', 'F']:
            break
        print("Digite apenas M ou F.")

    if sexo_pessoa == 'F' and idade_pessoa < 20:
        mulheres_menos_20 += 1

    pessoas.append({'nome': nome_pessoa, 'idade': idade_pessoa, 'sexo': sexo_pessoa})

print(pessoas)
media_idades = soma_idades / quantidade
print("Média de idades do grupo:", media_idades)
print("Número de mulheres com menos de 20 anos:", mulheres_menos_20)
