numeros = [1, 2, 3, 4, 5]

print(2 % 2)

def impar(n):
  return n % 2 == 1

resultado = filter(lambda n: n % 2 == 1, numeros)
print(list(resultado))
