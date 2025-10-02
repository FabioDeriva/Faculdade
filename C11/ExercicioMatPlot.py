import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os arquivos CSV
paises = pd.read_csv("paises.csv", sep=None, engine="python")
space = pd.read_csv("space.csv", sep=None, engine="python")

# Corrigir possíveis espaços extras nos nomes das colunas
paises.columns = [col.strip() for col in paises.columns]

# EX1
norte = paises[paises["Region"].str.contains("NORTHERN AMERICA", case=False, na=False)]

plt.figure(figsize=(10,6))
plt.plot(norte["Country"], norte["Birthrate"], marker='o', label="Natalidade")
plt.plot(norte["Country"], norte["Deathrate"], marker='s', label="Mortalidade")
plt.xticks(rotation=45)
plt.title("Taxa de natalidade e mortalidade - América do Norte")
plt.xlabel("Países")
plt.ylabel("Taxa")
plt.legend()
plt.tight_layout()
plt.show()

#Ex2
def pais_origem(local):
    if "USA" in local:
        return "USA"
    if "China" in local or "Jiuquan" in local:
        return "CHINA"
    return None

space["Country"] = space["Location"].apply(pais_origem)

filtro = space[space["Country"].isin(["USA", "CHINA"])]

empresas = filtro.drop_duplicates(subset=["Company Name", "Country"]) \
                 .groupby("Country")["Company Name"].count()

plt.figure(figsize=(6,6))
empresas.plot(kind="bar", color=["blue", "red"])
plt.title("Empresas espaciais - EUA x China")
plt.ylabel("Quantidade de empresas")
plt.show()

# EX3

roscosmos = space[space["Company Name"].str.contains("Roscosmos", case=False, na=False)]

resultados = roscosmos["Status Mission"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(resultados, labels=resultados.index, autopct='%1.1f%%', startangle=90, colors=["green", "red"])
plt.title("Missões da Roscosmos - Sucesso x Fracasso")
plt.show()

