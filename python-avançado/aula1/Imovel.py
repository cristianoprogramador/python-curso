class Imovel:

  def __init__(self, nome, quartos, suites):
    self.nome = nome
    self.quartos = quartos
    self.suites = suites

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

casarao = Imovel("Casarão", 3, 4)
# print(casarao.__dict__)

mansao = Imovel("Mansão", 4, 5)
# print(mansao.__dict__)

soma = casarao + mansao
print(soma)
print(casarao > mansao)
print(casarao < mansao)

print(casarao)
