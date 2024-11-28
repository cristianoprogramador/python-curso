import data

class Categoria:
  def __init__(self, tipo = ""):
    self.tipo = tipo

  def taxaAgua(self, consumo):

    print("Data da leitura: ", data.formatarData())

    match self.tipo:
      case "Clínica": return consumo * 1
      case "Restaurante": return consumo * 2
      case "Hotel": return consumo * 2.5

class Imovel:

  imposto = 0.2

  def __init__(self, nome, quartos, suites):
    self.nome = nome
    self.quartos = quartos
    self.suites = suites
    self.categoria = Categoria()

  def __add__(self, other):
    somaSelf = self.quartos + self.suites
    somaOther = other.quartos + other.suites
    return somaSelf + somaOther

  def __gt__(self, other):
    somaSelf = self.quartos + self.suites
    somaOther = other.quartos + other.suites
    return somaSelf > somaOther

  def __lt__(self, other):
    somaSelf = self.quartos + self.suites
    somaOther = other.quartos + other.suites
    return somaSelf < somaOther

  def __str__(self):
    return str(self.__dict__)

  def detalhar(self):
    return self.__dict__

  def somarAposentos(self):
    return self.quartos + self.suites

  @staticmethod
  def metodoEstatico():
    print("Chamou o método estático sem criar um objeto")

  @classmethod
  def metodoClasse(cls):
    print("Chamou o método estático sem criar um objeto", cls.imposto)


casarao = Imovel("Casarão", 3, 4)
mansao = Imovel("Mansão", 4, 5)

categoria = Categoria("Hotel")
hotel = Imovel("Hotel do Chico", 0, 150)
hotel.categoria = categoria

print(hotel.categoria.taxaAgua(300))

print(casarao.somarAposentos())
print(mansao.somarAposentos())

casarao.metodoEstatico()
print(casarao)

Imovel.metodoEstatico()
Imovel.metodoClasse()

soma = casarao + mansao
# print(soma)
# print(casarao > mansao)
# print(casarao < mansao)

# print(casarao)
