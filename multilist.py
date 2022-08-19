class Vendas:
  def __init__(self, nome, valor):
    self.nome = nome
    self.valor = valor
    
class Supermercado:
  def __init__(self, nomes):
    self.nomes = nomes
    self.total = 0
    self.vendas = []
    self.next = None

class Multilista:
  def __init__(self):
    self.head = None

  def cadastrarSupermercado(self, nome):
    if self.head:
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = Supermercado(nome)
    else:
      self.head = Supermercado(nome)

  def buscarSupermercado(self, nome_mercado):
    aux = self.head
    while aux and not(aux.nomes == nome_mercado):
      aux = aux.next
    return aux  
    
  def cadastrarVenda(self, nome, valor, nome_mercado):
    aux = self.buscarSupermercado(nome_mercado)
    if aux:
      aux.vendas.append(Vendas(nome,valor))
      aux.total += valor
    else:
      print('supermercado inexistente')

  def removerSupermercado(self, nome_mercado):
    aux =self.head
    num = 0
    while aux and not(aux.nomes == nome_mercado):
      aux = aux.next
      num +=1
    if aux == nome_mercado:
      aux.pop(num)
    else:
      print('supermercado inexistente')

  def removerVenda(self, nome_mercado, nome_venda):
    aux = self.buscarSupermercado(nome_mercado)
    if aux:
      num = 0
      for i in aux.vendas:
        if i.nome == nome_venda:
          aux.total -= i.valor
          aux.vendas.pop(num)
        else:
          num += 1
    else:
      print('supermercado inexistente')
      
  def imprimirVendas(self, nome_mercado):
    aux = self.buscarSupermercado(nome_mercado)
    if aux:
      for i in aux.vendas:
        print(i.nome,'-',i.valor)
    else: 
      print('supermercado inexistente')

supermercados = Multilista()
supermercados.cadastrarSupermercado('aldo')
supermercados.cadastrarSupermercado('pedro')
supermercados.cadastrarVenda('coca',8,'aldo')
supermercados.cadastrarVenda('biscoito',2,'aldo')
supermercados.cadastrarVenda('bolacha',2,'pedro')
supermercados.cadastrarVenda('miojo',1,'pedro')
supermercados.removerVenda('aldo','biscoito')
supermercados.imprimirVendas('aldo')
