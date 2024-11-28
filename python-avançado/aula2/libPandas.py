import pandas as pd

cidades = [
  {"nome": "São Paulo", "uf": "SP", "populacao": 125121},
  {"nome": "Rio de Janeiro", "uf": "RJ", "populacao": 32323},
  {"nome": "Ribeirao Preto", "uf": "SP", "populacao": 25000},
  {"nome": "Recife", "uf": "PE", "populacao": 56565}
]

dataFrame = pd.DataFrame(cidades)

ordenada = dataFrame.sort_values(by="populacao", ascending=True)


print(dataFrame)
print(ordenada)
print(ordenada.head(2))
