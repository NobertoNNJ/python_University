def rotate_word(palavra,valor):
  word_rot = ''
  for letra in palavra:
    letra_temp = ord(letra +valor)
    if letra_temp >ord('z'):
      letra_temp -= 26
    elif letra_temp < ord('a'):
      letra_temp += 26
    word_rot += chr(letra_temp)
  return word_rot

def gerar_dicionario(endereco):
  arquivo = open (endereco,'r')
  lista = arquivo.read().lower().split()
  for palavra in lista:
    dicionario[palavra] = None
  return dicionario

def verifica_palavra(palavra,dicionario):
  for i in range(1,14):
    palavra_rot = rotate_word(palavra,i)
    if palavra_rot in dicionario:
      print(palavra,i,palavra_rot)
