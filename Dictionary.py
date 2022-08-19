armazenamento = {}
i = 4
while i != 0:
  print("o que deseja fazer:\n")
  print("1-cadastrar produto \n2-pesquisar produto \n3-remover produto \n0-parar execução do programa ")
  i = int(input())
  if i == 1:
    produto = input('nome  do produto\n')
    valor = float(input('valor do produto\n'))
    armazenamento[produto] = valor
  elif i == 2:
    produto = input('nome  do produto: ')
    print("\nnome:",produto,"valor:",armazenamento.get(produto),"$\n")
  elif i == 3:
    produto = input('nome  do produto\n')
    armazenamento.pop(produto)
  elif i == 0:
    break
  else:
    print("numero invalido.\n")  
