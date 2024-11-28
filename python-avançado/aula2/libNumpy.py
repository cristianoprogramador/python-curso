
import numpy as np

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0

for n in numeros:
  soma += n

mediaManual = soma / len(numeros)


array_numeros = np.array(numeros)
mediaNumpy = np.mean(array_numeros)



print(array_numeros)
print(mediaNumpy)
