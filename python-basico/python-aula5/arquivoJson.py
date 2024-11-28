import json

pessoas = [
  {"nome": "Cristiano", "telefone": "(16) 3621-2135", "endereco": "ABC"},
  {"nome": "Maria", "telefone": "(33) 3621-1111", "endereco": "Higienopolis"},
  {"nome": "Joao", "telefone": "(54) 6565-3333", "endereco": "GFDD"}
]

with open("pessoas.json", 'w') as arquivo:
  json.dump(pessoas, arquivo, indent=4)
