arquivo = open('test.txt','r')

letra = arquivo.read().lower()

lista = letra.split()

ocorrencias = {}

for palavra in lista:
  ocorrencias[palavra] = ocorrencias.get(palavra,0) + 1
max_ocorrencias = None
max_palavra = None
for i in range(10):
  for chave,valor in ocorrencias.items():
    if max_ocorrencias == None or valor > max_ocorrencias:
      max_ocorrencias = valor
      max_palavra = chave
  print('A palavra',max_palavra,'foi a que mais ocorreu, num total de',max_ocorrencias,'vezes.')
  ocorrencias[max_palavra] = ocorrencias.pop(max_palavra)        
