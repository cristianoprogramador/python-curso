import csv

carros = [
  ["VW", "Virtus", "2017"],
  ["VW", "Gol", "2020"],
  ["Fiat", "Palio", "2019"],
]

with open("carros.csv", "w", newline="") as arquivo:
   fileCSV = csv.writer(arquivo, delimiter=",")

   fileCSV.writerow(["Marca", "Modelo", "Ano"])
   fileCSV.writerows(carros)
