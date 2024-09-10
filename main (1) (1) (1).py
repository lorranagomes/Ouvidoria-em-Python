#Lorrana Gomes, Juan Amaral e Douglas Rodrigues
#Fase02
class Ocorrencia:
  def __init__(self, numero, nome, categoria, comentario):
    self.numero = numero
    self.nome = nome
    self.categoria = categoria
    self.comentario = comentario


class Ouvidoria:
  def __init__(self):
    self.ocorrencias = []

  def menu(self):
    opção = 0

    while opção != 5:

      print("\n                 MENU              ")
      print("-" * 42)
      print("1) Listar as ocorrências")
      print("2) Adicionar nova ocorrência")
      print("3) Remover uma ocorrência")
      print("4) Pesquisar uma ocorrência por código")
      print("5) Sair do programa")
      print("-" *42)

      opção = int(input("\nDigite a sua opção: "))

      if opção == 1:
        self.listar_ocorrencias()

      elif opção == 2:
        self.adicionar_ocorrencia()

      elif opção == 3:
        self.remover_ocorrencia()

      elif opção == 4:
        self.pesquisar_ocorrencia()

      elif opção == 5:
        print("\n Agradecemos a sua participação!")

      else:
        print("\nErro, tente novamente!")

  def listar_ocorrencias(self):
    if not self.ocorrencias:
      print("\n Nenhuma ocorrência cadastrada no sistema.")
    else:
      categoria = input('''\nDigite a categoria que deseja:
     1- elogio
     2- reclamação
     3- Sugestão
     4- Todas: ''')

      for ocorrencia in self.ocorrencias:
        if categoria.lower() == "4" or ocorrencia.categoria.lower() == categoria.lower():
          print(f"{ocorrencia.numero}) {ocorrencia.nome}")

  def adicionar_ocorrencia(self):
    nome = input("\nDigite o título da ocorrência: ")
    categoria = input('''\nDigite o tipo da ocorrência: 
    1- Elogio 
    2- Reclamação 
    3- Sugestão: ''')
    descricao = input("\n Descreva aqui a sua ocorrência: ")

    numero = len(self.ocorrencias) + 1
    ocorrencia = Ocorrencia(numero, nome, categoria, descricao)
    self.ocorrencias.append(ocorrencia)

    print(f"\nOcorrência cadastrada com sucesso. Código: {numero}")

  def remover_ocorrencia(self):
    if not self.ocorrencias:
      print("\nNenhuma ocorrência cadastrada no sistema.")
    else:
      self.listar_ocorrencias()
      numero = int(input("\nPor gentileza, digite o codigo da ocorrência: "))

      if numero < 1 or numero > len(self.ocorrencias):
        print("\nCódigo inválido!")
      else:
        ocorrencia_removida = self.ocorrencias.pop(numero - 1)
        print("\nOcorrência removida com sucesso!")

  def pesquisar_ocorrencia(self):
    if not self.ocorrencias:
      print("\nNenhuma ocorrência cadastrada no sistema.")
    else:
      numero = int(input('''\nPor gentileza, digite o código da ocorrência que deseja pesquisar:
      1 - Elogio
      2 - Reclamação
      3 - Sugestão  '''))

      if numero < 1 or numero > len(self.ocorrencias):
        print("\nNão há ocorrência nesse código, tente novamente!")
      else:
        ocorrencia = self.ocorrencias[numero - 1]
        print("\nTítulo: ", ocorrencia.nome)
        print("Código: ", ocorrencia.categoria)
        print("Descrição: ", ocorrencia.comentario)


ouvidoria = Ouvidoria()
ouvidoria.menu()