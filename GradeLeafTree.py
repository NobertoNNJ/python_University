class BSTNode:
  def __init__(self, value=None):
    self.data = value
    self.left = self.right = None

  def insert(self,value):
    if not self.data:
      self.data = value
    elif value < self.data:
      if self.left:
        self.left.insert(value)
      else:
        self.left = BSTNode(value)
    elif value > self.data:
      if self.right:
        self.right.insert(value)
      else:
        self.right = BSTNode(value)

  def graus(self):
    if not self.data:
      return 0
    else:
      if self.left and self.right:
        print('no:',self.data,'grau 2')
        return self.left.graus() + self.right.graus()
      elif self.left:  
        print('no:',self.data,'grau 1')
        return (self.left.graus() if self.left else 0) + (self.right.graus() if self.right else 0)
      elif self.right:  
        print('no:',self.data,'grau 1')
        return (self.left.graus() if self.left else 0) + (self.right.graus() if self.right else 0)
      else:
         print('no:',self.data,'grau 0')
         return (self.left.graus() if self.left else 0) + (self.right.graus() if self.right else 0)
  

  def folhas(self):
    if not self.data:
      return 0
    elif not (self.right and self.left):
      print('no folha:',self.data)
      return 1
    else:
      return self.left.folhas() + self.right.folhas()
      

root = BSTNode()
root.insert(10)
root.insert(20)
root.insert(5)
root.insert(15)
root.insert(7)
root.insert(22)
root.insert(4)
root.graus()
print()
print('total de folhas:', root.folhas())
