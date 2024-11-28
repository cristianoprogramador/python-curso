from datetime import datetime

def formatarData(data = datetime.now(), formato = "%d/%m/%Y"):
  return datetime.strftime(data, formato)

def criarData(data, formato = "%Y-%m-%d"):
  return datetime.strptime(data, formato)

data = criarData("2023-12-12")

print(formatarData(data))
