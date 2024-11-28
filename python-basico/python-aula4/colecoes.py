# conjuntos
conjunto = set([4, 6, 8, 2, 3, 0, 8])

print("Conjunto: ", conjunto)

# tupla
tupla = (3, 2, 4,5 ,67, 88)
print("tupla: ", tupla)

pessoas = ["Orion", "Maria", "João"]
print("Pessoas: ", pessoas)

pessoa = {"nome": "Orion", "telefone": "(16)3632-2512", "endereco": "ABC"}
print("Pessoa: ", pessoa)
print("Nome da pessoa: ", pessoa["nome"])

grupodepessoa = [
  {"nome": "Orion", "telefone": "(16)3632-2512", "endereco": "ABC"},
  {"nome": "Maria", "telefone": "(16)323-3333", "endereco": "ZVC"},
  {"nome": "Antonio", "telefone": "(16)464576-2512", "endereco": "GFD"}
]

print(grupodepessoa[2])
print(grupodepessoa[2]['nome'])
