class Node:
  def __init__(self, value):
    self.data = value
    self.next = None
    
class pilha():
  def __init__(self):
    self.data = []
    
  def push (self,value):
    self.data.append(value)
    
  def pop (self):
    return self.data.pop()
    
  def isEmpty (self):
    len (self.data) == 0

class LinkedList:
  def __init__(self):
    self.head = None
    self.__size = 0

  def append(self, value):
    if self.head:
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = Node(value)   
    else:
      self.head = Node(value)
    self.__size += 1

  def append_inicio(self,value):
    if self.head:
      aux = Node(value)
      aux.next = self.head
      self.head = aux
    else:
      self.head = Node(value)
    self.__size += 1

  def insert(self,index,value):
    if index == 0:
      aux = Node(value)
      aux.next = self.head
      self.head = aux
    elif index > len(self) -1 :
      print("\nindex não existe")
    else:
      aux = self.head
      aux2 = Node(value)
      for i in range(index-1):
        aux = aux.next
      aux2.next = aux.next
      aux.next = aux2
      

    def pop(self,index):
      if index >= len(self):
        print("deu pau")
      elif index == 0:
        aux = self.head
        self.head = self.head.next
        del aux
      else:
        aux = self.head
        for i in range(index):
          ant = aux
          aux = aux.next
        ant.next = aux.next
        del aux
 

    def pop(self):
      if not self.head:
        print("deu pau")
      elif not self.head.next:
        del self.head
        self.head = None
      else:
        aux = self.head
        while aux.next.next:
          aux = aux.next
        del aux.next
        aux.next = None
          

  def pares(self, lista):
    if(self.head):
      print("pares:")
      for num in lista:
        if num % 2 == 0:
          print (num)
      
    else:
        raise IndexError('Lista Vazia')
      
  def  print_partial(self,valor1,valor2):
    aux = self.head
    for i in range(valor1):
      aux = aux.next
    for i in range(valor2 - valor1 +1):
      valores = aux.data
      print("\nvalor:",valores)
      aux = aux.next

  def concatenar(self,lista):
    if not self.head and lista.head:
      self.head = lista.head
      lista.head = None
    elif self.head and lista.head:
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = lista.next
      lista.head = None

  def inverse(self):
    aux = self.head
    invert = pilha()
    while aux:
      invert.push(aux.data)
      aux = aux.next 
    aux = invert.pop()
    print(aux)  
      
  def __len__(self):
    return self.__size

  def __getitem__(self, index):
    if self.head:
      aux = self.head
      for i in range(index):
        if aux.next:
          aux = aux.next
        else:
          raise IndexError('Posição não existe.')
      return aux.data
    else:
      raise IndexError('Lista vazia.')

  def __setitem__(self, index, value):
    if self.head:
      aux = self.head
      for i in range (index):
        if aux.next:
          aux = aux.next
        else:
          raise IndexError('Posição não existe')
      aux.data = value
    else:
      raise IndexError('Lista Vazia')

  def __str__(self):
    output = '['
    aux = self.head
    if aux:
      while aux:
        output += str(aux.data)
        if aux.next:
          output += ', '
        aux = aux.next
      output += ']'
      return output
    else:
      return '[]'

l = LinkedList()
l.append(10)
l.append(15)
l.append(8)
l.append(25)
l.append(16)
l.pares(l)
l.append_inicio(6)
l.insert(2,5)
l.print_partial(0,4)
l.inverse()

print(type(l))
print(l)
