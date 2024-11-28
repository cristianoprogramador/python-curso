
def somar(n1, n2):
  return n1 + n2

def subtrair(n1, n2):
  return n1 - n2

def multiplicar(n1, n2):
  return n1 * n2

def dividir(n1, n2):
  # resultado = n1 / n2
  # print(f"{n1} / {n2} = {resultado}")
  return n1 / n2

def calcular(n1, n2, operador):
  try:
    match operador:
      case "+": return somar(n1, n2)
      case "-": return subtrair(n1, n2)
      case "*": return multiplicar(n1, n2)
      case "/": return dividir(n1, n2)
      case other: return "Operador não encontrado"

  except ZeroDivisionError:
    return "Não é possivel dividir um numero por zero"

  except Exception:
    return "Ocorreu um erro"

print(calcular(5, 10, "+"))
print(calcular(5, 10, "-"))
print(calcular(5, 10, "*"))
print(calcular(5, 0, "/"))
print(calcular(5, 10, "x"))

# try:

# except ZeroDivisionError:
#   print("Não é possivel dividir um numero por zero")

# except Exception:
#   print("Ocorreu um erro")
