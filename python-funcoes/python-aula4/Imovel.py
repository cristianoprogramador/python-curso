from abc import ABC, abstractmethod

class Imovel(ABC):
  def __init__(self, nome, uf, valor, endereco = "", area = ""):
    self._nome = nome
    self._uf = uf
    self._valor = valor
    self._endereco = endereco
    self._area = area

  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, nome):
    self._nome = nome

  @property
  def uf(self):
    return self._uf

  @uf.setter
  def uf(self, uf):
    self._uf = uf

  # def getNome(self):
  #   return self.nome

  # def setNome(self, nome):
  #   self.nome = nome

  def detalhar(self):
    print(self.__dict__)

  def calcularImposto(self):
    return self._valor * 0.02

  @abstractmethod
  def aluguelSugerido(self):
    ...


class ImovelResidencial(Imovel):
  def __init__(self, nome, uf, valor, endereco = "", area = ""):
    super().__init__(nome, uf, valor, endereco = "", area = "")
    self._quartos = 0
    self._piscina = False

  def aluguelSugerido(self):
    return self._valor * 0.01


class ImovelComercial(Imovel):

  def aluguelSugerido(self):
      return self._valor * 0.015

  def calcularImposto(self):
    match self._uf:
      case "DF": taxa = 0.03
      case "SP": taxa = 0.04
      case "RJ": taxa = 0.025
      case other: taxa = 0.02

    return self._valor * taxa

class ImovelRural:
  def __init__(self, hectares = "", curral = "", produtiva = True):
    self._hectares = hectares
    self._curral = curral
    self._produtiva = produtiva

  def mesPlantacao(self, mes):
    match int(mes):
      case 1: print("Milho")
      case 2: print("Feijão")
      case 3: print("Soja")
      case other: print("Algodão")


class Fazenda(Imovel, ImovelRural):

  def aluguelSugerido(self):
      return self._valor * 0.025

"""
fazenda = Fazenda("Fazenda Modelo", "GO", 1500000)
fazenda.detalhar()
print(fazenda.calcularImposto())
fazenda.mesPlantacao(2)
"""

casa = ImovelResidencial("Minha casa", "SP", 300000)
casa.detalhar()
# casa.setNome("Casa Bonita")
# print(casa.getNome()),
casa.nome = "Casa Bonita"
casa.uf = "RJ"
print(casa.nome)
print(casa.uf)
print(casa.aluguelSugerido())

print("***********")
print(casa.calcularImposto())
clinica = ImovelComercial("Clinica x", "SP", 800000)
# clinica.detalhar()

print(clinica.calcularImposto())

# imovel = Imovel("Solar do Cerrado", "DF", 500000)
# imovel.detalhar()

"""
imovel.endereco = "ABC"
imovel.area = "2000"
imovel.detalhar()
print(imovel.__dict__)
"""
