class Nota:
  def __init__(self, nota):
    self.nota = nota

class Disciplina:
  def __init__(self, disciplina):
    self.disciplina = disciplina
    self.nota = []
    self.next = None

    
class BSTnode:
  def __init__(self, nome = None):
    self.aluno = nome
    self.disciplinas = None
    self.quantdisciplinas = 0
    self.left = self.right = None

  def insert(self, nome):
    if not self.aluno:
        self.aluno = nome
    elif nome < self.aluno:
        if self.left:
            self.left.insert(nome)
        else:
            self.left = BSTnode(nome)
    elif nome > self.aluno:
        if self.right:
            self.right.insert(nome)
        else:
            self.right = BSTnode(nome)       

  def insert_disciplina(self, nome, disciplina):
    if self.aluno == nome:
      if self.disciplinas:
        aux = self.disciplinas
        while aux.next:
          aux = aux.next
        aux.next = Disciplina(disciplina)
        self.quantdisciplinas += 1
      else:
        self.disciplinas = Disciplina(disciplina)
        self.quantdisciplinas += 1
    if self.left:
        self.left.insert_disciplina(nome, disciplina) 
    if self.right:
        self.right.insert_disciplina(nome, disciplina)

  def insert_nota(self, nome, disciplina, nota):
    if self.aluno == nome:
      if self.disciplinas:
        aux = self.disciplinas
        while aux and not (aux.disciplina == disciplina):
          aux = aux.next
        if not (aux.disciplina == disciplina):
          print('disciplina inexistente.')
        else:  
          if len(aux.nota) < 2:
            aux.nota.append(Nota(nota))
          else:
            print('maximo de notas cadastradas.')
      else:
        print('não possui disciplinas.')
    if self.left:
        self.left.insert_nota(nome, disciplina, nota) 
    if self.right:
        self.right.insert_nota(nome, disciplina, nota)

  def remove_nota(self,nome, disciplina, remover):
    if self.aluno == nome:
      if self.disciplinas:
        aux = self.disciplinas
        while aux and not (aux.disciplina == disciplina):
          aux = aux.next
        if not (aux.disciplina == disciplina):
          print('disciplina inexistente.')
        else:  
          aux.nota.pop(remover)
      else:
        print('não possui disciplinas.')
    if self.left:
        self.left.remove_nota(nome, disciplina, remover) 
    if self.right:
        self.right.remove_nota(nome, disciplina, remover)

  def remove_disciplina(self, nome, disciplina):
    if self.aluno == nome:
      if self.disciplinas:
        aux = self.disciplinas
        while aux.next and not (aux.next.disciplina == disciplina):
          aux = aux.next
        if self.disciplinas.disciplina == disciplina:
          self.disciplinas.disciplina = None
        elif aux.next.disciplina == disciplina:
          aux1 = aux.next.disciplina 
          aux.next.disciplina = aux.next.next.disciplina
          del aux1
        else:
          print('disciplina inexistente.')
    if self.left:
        self.left.remove_disciplina(nome, disciplina) 
    if self.right:
        self.right.remove_disciplina(nome, disciplina)
        

  def remove_aluno(self, nome):
        if nome < self.aluno:
            self.left = self.left.remove_aluno(nome)
        elif nome > self.aluno:
            self.right = self.right.remove_aluno(nome)
        else:
            if not self.right :
                return self.left
            if not self.left :
                return self.right
            aux = self.right._min()
            self.aluno= aux.aluno
            self.right._remove_min()
        return self
 
  def _min(self):
      if not self.left :
          return self
      else:
          return self.left._min()
 
  def _remove_min(self):
    if not self.left : 
      return self.right
    self.left = self.left._remove_min()
    return self

  def att_aluno(self, nome, aluno):
    if self.aluno == nome:
        self.aluno = aluno
    if self.left:
        self.left.att_aluno(nome, aluno) 
    if self.right:
        self.right.att_aluno(nome, aluno)

  def att_disciplina(self, nome, disciplina, nova):
    if self.aluno == nome:
      if self.disciplinas:
        aux = self.disciplinas
        while aux.next and not (aux.next.disciplina == disciplina):
          aux = aux.next
        if self.disciplinas.disciplina == disciplina:
          self.disciplinas.disciplina = nova
        elif aux.next.disciplina == disciplina:
          aux.next.disciplina = nova
        else:
          print('disciplina inexistente.')
    if self.left:
        self.left.att_disciplina(nome, disciplina, nova) 
    if self.right:
        self.right.att_disciplina(nome, disciplina, nova)   
 

  def att_nota(self, aluno, disciplina, nota, nova):
    self.remove_nota(aluno, disciplina, nota)
    self.insert_nota(aluno, disciplina, nova)

  def media_disciplina(self, nome, disciplina):
    if self.aluno == nome:
      if self.disciplinas:
        aux = self.disciplinas
        while aux and not (aux.disciplina == disciplina):
          aux = aux.next
        if aux and aux.disciplina == disciplina:
          aux1 = 0
          for i in aux.nota:
            aux1 = aux1 + i.nota
          aux1 = aux1/2
          return aux1
      else:
        print('disciplina inexistente.')
    if self.left:
        self.left.media_disciplina(nome, disciplina) 
    if self.right:
        self.right.media_disciplina(nome, disciplina)

  def medias_aluno(self, nome):
    if self.aluno == nome:
      if self.disciplinas:
        aux = self.disciplinas
        while aux:
          aux1 = 0
          for i in aux.nota:
            aux1 = aux1 + i.nota
          aux1 = aux1/2
          print(aux.disciplina,' nota:', aux1)
          aux = aux.next         
    if self.left:
        self.left.medias_aluno(nome) 
    if self.right:
        self.right.medias_aluno(nome)

  def aprovados(self):
    if self.aluno:
      aux2 = self.aluno
      if self.disciplinas:
        aux = self.disciplinas
        aux1 =0
        while aux:
          for i in aux.nota:
            aux1 = aux1 + i.nota
          aux = aux.next
        aux1 = aux1/(2*self.quantdisciplinas)
        if aux1 >= 7:
          print(aux2)
    if self.left:
        self.left.aprovados() 
    if self.right:
        self.right.aprovados()

  def reprovados(self):
    if self.aluno:
      aux2 = self.aluno
      if self.disciplinas:
        aux = self.disciplinas
        aux1 =0
        while aux:
          for i in aux.nota:
            aux1 = aux1 + i.nota
          aux = aux.next
        aux1 = aux1/(2*self.quantdisciplinas)
        if aux1 < 7:
          print(aux2)
    if self.left:
        self.left.reprovados() 
    if self.right:
        self.right.reprovados()
    
    
  def imprimir_central(self):
      if self.left:
          self.left.imprimir_central()
      if self.aluno:
          print(self.aluno,end=' ')
      if self.right:
          self.right.imprimir_central()     

root = BSTnode()
aux = 1
while aux != 0:
  print('menu'.center(50,' '))
  aux = int(input('1-Cadastrar aluno \n2-Cadastrar disciplina em aluno \n3-Cadastrar nota em disciplina de aluno \n4-Remover aluno \n5-Remover disciplina de aluno \n6-Remover nota de disciplina de aluno \n7-Atualizar aluno \n8-Atualizar disciplina de aluno \n9-Atualizar nota de disciplina de aluno \n10-Visualizar a média do aluno em uma disciplina \n11-Visualizar os nomes dos alunos em ordem alfabética \n12-Visualizar os nomes dos alunos que estão com média menor que 7 \n13-Visualizar os nomes dos alunos que estão com média maior ou igual a 7 \n14-Visualizar as notas das disciplinas cadastradas em um aluno \n0-fechar menu\n'))
  if aux == 1:
    nome = input('\nnome:')
    root.insert(nome)
  elif aux == 2:
    nome = input('\nnome:')
    disciplina = input('\ndisciplina:')
    root.insert_disciplina(nome,disciplina)
  elif aux == 3:
    nome = input('\nnome:')
    disciplina = input('\ndisciplina:')
    nota = int(input('\nnota:'))
    root.insert_nota(nome,disciplina,nota)
  elif aux == 4:
    nome = input('\nnome:')
    root.remove_aluno(nome)
  elif aux == 5:
    nome = input('\nnome:')
    disciplina = input('\ndisciplina:')
    root.remove_disciplina(nome,disciplina)
  elif aux == 6:
    nome = input('\nnome:')
    disciplina = input('\ndisciplina:')
    nota = int(input('\nprimeira ou segunda nota:')) - 1
    root.remove_nota(nome,disciplina,nota)
  elif aux == 7:
    nome = input('\nnome:')
    novo = input('\nnovo:')
    root.att_aluno(nome,novo)
  elif aux == 8:
    nome = input('\nnome:')
    disciplina = input('\ndisciplina:')
    nova = input('\nnova:')
    root.att_disciplina(nome,disciplina,nova)
  elif aux == 9:
    nome = input('\nnome:')
    disciplina = input('\ndisciplina:')
    nota = int(input('\nprimeira ou segunda nota:')) - 1
    nova_nota = int(input('\nnota:'))
    root.att_nota(nome,disciplina,nota,nova_nota)
  elif aux == 10:
    nome = input('\nnome:')
    disciplina = input('\ndisciplina:')
    aux = root.media_disciplina(nome,disciplina)
    print(aux)
  elif aux == 11:
    root.imprimir_central()
  elif aux == 12:
    root.aprovados()
  elif aux == 13:
    root.reprovados()
  elif aux == 14:
    nome = input('nome:')
    root.medias_aluno(nome)
  elif aux == 0:
    print('fechando menu.')
  else:
    print('valor invalido.')
