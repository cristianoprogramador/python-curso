
numeros = [10, 20, 30, 17]
print(numeros[1])

carros = ["Palio", "Gol", "Ka", "Onix", "Virtus"]
print(carros[2])
print(len(carros))

carros.append("Kombi")
print(carros)

carros.remove("Gol")
print(carros)

del carros[0]
print(carros)

carros = sorted(carros)
print(carros)

for carro in carros:
  print(carro)
