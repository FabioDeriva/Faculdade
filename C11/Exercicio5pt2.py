import numpy as np
import pandas as pd
import pandas as pd

df = pd.read_csv("paises.csv",delimiter=";")

#EX1
oceania = df[df['Region'].str.contains('OCEANIA', case=False)]
print("Países da Oceania:")
print(oceania['Country'])


print("\nQuantidade de países na Oceania:", len(oceania))

#EX2
max_pop = df.loc[df['Population'].idxmax(), ['Country', 'Region', 'Population']]
print("\nPaís com maior população:")
print(max_pop)

#EX3
media_literacy = df.groupby('Region')['Literacy (%)'].mean()
print("\nMédia de alfabetização por região:")
print(media_literacy)

#EX4
no_coast = df[df['Coastline (coast/area ratio)'] == 0]
print ("\nPaíses sem litoral:")
print(no_coast['Country'])

#EX5
def humanitarian_help(rate):
    return 'Balanced' if rate < 9 else 'Urgent'

df['Humanitarian Help'] = df['Deathrate'].apply(humanitarian_help)
print("\nDataset atualizado com a coluna 'Humanitarian Help':")
print(df[['Country', 'Deathrate', 'Humanitarian Help']].head())