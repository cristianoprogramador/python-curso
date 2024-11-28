
# try:
#   n1 = int(input("Número 1: "))
#   n2 = int(input("Número 2: "))

#   resultado = n1/n2

#   print(f"O resultado da divisão é {resultado}")

# except Exception as erro:
#   print(f"Error: {erro}")

try:
  n1 = int(input("Número 1: "))
  n2 = int(input("Número 2: "))

  resultado = n1/n2

  print(f"O resultado da divisão é {resultado}")

except ValueError:
  print("Favor digitar somente números")

except ZeroDivisionError:
  print("Não é possivel dividir um número por zero")

except Exception as error:
  print(f"Ocorreu um error: {error}")

else:
  print("O programa foi executado corretamente")

finally:
  print("Fim")
