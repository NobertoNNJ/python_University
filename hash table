class Funcionario:
  def __init__(self, nome, salario):
    self.nomes = nome
    self.salarios = salario

hash = [[],[],[],[],[],[],[],[],[],[]]
num = 5
while num != 0:
  num = int(input('1-inserir funcionario \n2-buscar salario de um funcionario \n0-sair\n'))
  if num == 1:
    nome = input('nome do funcionario:')
    salario = input('salario do funcionario:')
    aux = (ord(nome[0]))
    aux = aux % 10
    if aux < 10:
      hash[aux].append(Funcionario(nome, salario))
  elif num == 2:
    nome = input('nome do funcionario:')
    aux = (ord(nome[0]))
    aux = aux % 10
    if aux < 10:
      for i in hash[aux]:
        if i.nomes == nome:
          print('salario:',i.salarios)
  elif num == 0:
    print('sair do programa.')
  else:
    print('valor invalido.')
