dia = int(input("Digite o número do dia da semana:"))

"""
if dia == 1:
  print("Domingo")
elif dia == 2:
  print("Segunda")
elif dia == 3:
  print("Terça")
elif dia == 4:
  print("Quarta")
elif dia == 5:
  print("Quinta")
elif dia == 6:
  print("Sexta")
elif dia == 7:
  print("Sabado")
else:
  print("Esse dia não existe")
"""

match dia:
  case 1:
    print("Domingo")
  case 2:
    print("Segunda")
  case 3:
    print("Terça")
  case 4:
    print("Quarta")
  case 5:
    print("Quinta")
  case 6:
    print("Sexta")
  case 7:
    print("Sabado")
  case other:
    print("Esse dia não existe")
