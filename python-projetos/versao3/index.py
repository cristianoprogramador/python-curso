from classes.Produto import Produto

def menu():
  print()
  print("1 - Listar Produtos")
  print("2 - Inserir Produtos")
  print("3 - Alterar Produtos")
  print("4 - Excluir Produtos")
  print("0 - Sair")
  print()

opcao = 1

while opcao != 0:

  menu()
  opcao = int(input("Escolha uma opção: "))

  match opcao:
    case 1:
      print()
      print("****************")
      Produto.listarTodos()
      print("****************")

    case 2:
      codigo = input("Digite o código: ")
      nome = input("Digite o nome: ")
      quantidade = int(input("Digite o quantidade: "))
      valor = int(input("Digite o valor: "))

      produto = Produto(codigo, nome, quantidade, valor)
      produto.inserir()

    case 3:
      Produto.listarTodos()
      selecionado = int(input("Qual item deseja alterar? "))
      item = Produto.consultar(selecionado)

      quantidade = int(input("Qual a nova Quantidade? "))
      valor = int(input("Qual o novo Valor? "))

      produto = Produto(item["codigo"], item["nome"], quantidade, valor)
      produto.alterar(selecionado)

    case 4:
      Produto.listarTodos()
      selecionado = int(input("Qual item deseja excluir? "))
      Produto.excluir(selecionado)
