# Para criar e sobreescrever sempre
arquivo = open("pessoas.txt", 'w')

# Para adicionar
# arquivo = open("pessoas.txt", 'a+')

arquivo.write("Orion\n")
arquivo.write("Maria\n")
arquivo.write("Jorge\n")

arquivo.close()

with open("pessoas.txt", "r+") as arquivoLeitura:
  for linha in arquivoLeitura:
    print(linha)
