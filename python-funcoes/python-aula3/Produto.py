# class Produto:
#   def __init__(self):
#     self.nome = ""
#     self.marca = ""
#     self.modelo = ""
#     self.valor = 0

class Produto:
  def __init__(self, nome = "", valor = 0, marca = "", modelo = "", quantidade = 0):
    self.nome = nome
    self.marca = marca
    self.quantidade = quantidade
    self.modelo = modelo
    self.valor = valor

  def vender(self, quantidade):
    if(quantidade > self.quantidade):
      print("*********************")
      print("Não há estoque suficiente")
      print("*********************")
    # self.quantidade = self.quantidade - quantidade
    self.quantidade -= quantidade

  def comprar(self, quantidade):
    self.quantidade += quantidade

produto0 = Produto("Smartphone", 69.9, "Sony", "J8", 80)
produto0.comprar(10)
produto0.vender(99)

produto1 = Produto("Geladeira", 690.9, "Consair", "BST5600", 4)
produto2 = Produto("Notebook", 333.2)
# produto0.nome = "SmartPhone"
# produto0.marca = "Sony"
# produto0.valor = 69.9

# produto1 = Produto()
# produto1.nome = "Geladeira"

# produto2 = Produto()
# produto2.nome = "Notebook"

print(produto0.__dict__)
print(produto1.__dict__)
print(produto2.__dict__)
