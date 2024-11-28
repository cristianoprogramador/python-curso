from sklearn.cluster import KMeans
import numpy as np

class Produto:
  def __init__(self, nome, preco, peso):
    self.nome = nome
    self.preco = preco
    self.peso = peso

produtos = [
  Produto("Produto 1", 60.50, 0.70),
  Produto("Produto 2", 25, 0.5),
  Produto("Produto 3", 5.88, 0.75),
  Produto("Produto 4", 50.12, 0.4),
  Produto("Produto 5", 12.50, 0.3),
  Produto("Produto 6", 8.75, 0.56),
]

precos = [[p.preco, p.peso] for p in produtos]
matriz = np.array(precos)

kmeans = KMeans(n_init='auto', n_clusters=2, random_state=0).fit(matriz)
labels = kmeans.labels_

for i in range(2):
  print(f"Grupo {i + 1}:")
  for j in range(len(produtos)):
    if labels[j] == i:
     print(" - ", produtos[j].nome)

