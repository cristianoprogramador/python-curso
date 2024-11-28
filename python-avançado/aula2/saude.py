import numpy as np
import pandas as pd

class Paciente:
  def __init__(self, nome, idade, sexo, peso, altura):
    self.nome = nome
    self.idade = idade
    self.sexo = sexo
    self.peso = peso
    self.altura = altura

pacientes = {
  "Paciente 1": Paciente("Maria", 25, "F", 60, 1.70),
  "Paciente 2": Paciente("Orion", 30, "M", 80, 1.80),
  "Paciente 3": Paciente("João", 80, "M", 60, 1.53),
  "Paciente 4": Paciente("Ana", 35, "F", 90, 1.65),
}

l_pacientes = [p.__dict__ for p in pacientes.values()]

df_pacientes = pd.DataFrame.from_records(l_pacientes, index=pacientes.keys())

df_pacientes["IMC"] = df_pacientes.apply(lambda i: i.peso / i.altura ** 2, axis=1)

media = np.mean(df_pacientes["IMC"])

sobrepeso = df_pacientes[df_pacientes["IMC"] > 25]

percentual = len(sobrepeso) / len(df_pacientes) * 100

print(percentual)
