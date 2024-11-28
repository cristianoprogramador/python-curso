# i = 1

# while i < 11:
#   print(f"2 x {i} = {2*i}")
#   # i = i + 1
#   i += 1

continuar = True

while continuar:

  numero = int(input("Qual tabuada?"))

  for i in range(1, 11):
    print(f"2 x {numero} = {i*numero}")

  continuar = input("Deseja continuar? (s/n)")
  continuar = True if continuar == 's' else False
