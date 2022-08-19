class fila():
  def __init__(self):
    self.data = []
  def enfileirar(self,nome,cpf,conta,ficha):
    self.data.append(nome)
    self.data.append(cpf)
    self.data.append(conta)
    self.data.append(ficha)
    
  def desenfileirar(self):
    self.data.pop(0)
    self.data.pop(0)
    self.data.pop(0)
    self.data.pop(0)
    
  def vazia(self):
    if len(self.data) == 0:
      print("\nvazia")
    else:
      print("\ntem gente")
 
i = 7
j = 0
fila = fila()

while i != 0:
  nome =[]
  cpf =[]
  conta = []
  ficha =[]
  
  i = int(input('\ndigite 1 para entra na fila, 2 para retirar o primeiro da fila, 3 para checar se tem gente na fila e 0 para fechar o programa: '))
  
  if i == 1:
    j += 1
    ficha = j
    nome = input('\nnome: ')
    cpf = input('\ncpf: ')
    conta = input('\nconta bancaria: ')
    fila.enfileirar(nome,cpf,conta,ficha)
  elif i == 2:
    fila.desenfileirar()
  elif i == 3:
    fila.vazia()
  elif i == 0:
    print("\nfechando fila!")
  else:
    print("\nfunção invalida!")
    
print(fila.data)
