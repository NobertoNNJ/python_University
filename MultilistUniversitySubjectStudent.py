class Alunos:
  def __init__(self,nome):
    self.nome = nome
    self.disciplinas = []
    self.next = None
    
class Disciplinas:
  def __init__(self,disciplina):
    self.disciplina = disciplina
    self.next = None
    
class Universidades:
  def __init__(self,universidade):
    self.universidade = universidade
    self.alunos = []
    self.next = None
    
class  Multilista:
  def __init__(self):
    self.head = None
    self.next = None
    
  def cadastrarUniversidade(self,universidade):
    if self.head:
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = Universidades(universidade)
    else:
      self.head = Universidades(universidade)
      
  def buscarUniversidade(self,nome_universidade):
    aux = self.head
    while aux and not(aux.universidade == nome_universidade):
      aux = aux.next
    return aux
    
  def cadastrarAluno(self,nome,nome_universidade):
    aux = self.buscarUniversidade(nome_universidade)
    if aux:
      aux.alunos.append(Alunos(nome))
    else:
      print('universide inexistente')

  def buscarAluno(self,nome_aluno,nome_universidade):
    aux = self.buscarUniversidade(nome_universidade)
    if aux:
      aux1 = aux.alunos
      for i in aux1:
        if i.nome == nome_aluno:
          return aux1
    
  def cadastrarDisciplina(self,disciplina,nome_aluno,nome_universidade):
    aux = self.buscarAluno(nome_aluno,nome_universidade)
    if aux:
      aux.disciplinas.append(Disciplinas(disciplina))
    else:
      print('aluno inexistente')
      
  def relatorio(self):
    aux = self.head
    while aux:
      print(aux.universidade)
      print('---------------')
      for i in aux.alunos:
        print(i.nome)
      aux = aux.next
      print()    

faculdade = Multilista()
faculdade.cadastrarUniversidade('uepb')
faculdade.cadastrarUniversidade('fip')
faculdade.cadastrarAluno('noberto','uepb')
faculdade.cadastrarAluno('fabio','uepb')
faculdade.cadastrarAluno('felipe','fip')
faculdade.cadastrarAluno('miqueias','uepb')
faculdade.relatorio()
