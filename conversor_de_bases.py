def decimal(num, base_inicial):
  dicionario = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
               '9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'a':10,
               'b':11,'c':12,'d':13,'e':14,'f':15}
  tamanho = len(str(num))
  decimal = 0

  num = list(num)
  num.reverse()
  for i in range(tamanho):
    num[i] = dicionario.get(num[i])
  for i in range(tamanho):
    decimal = decimal + num[i] * (base_inicial**i)
  return decimal    

def conversor(num,base_inicial,base_final):
  dicionario = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',
               9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
  num = int(decimal(num,base_inicial))
  numero = []
  while num > 0:
    resto = num % base_final
    num = num // base_final
    numero += dicionario.get(resto)
  numero.reverse()
  final =''
  for i in range(len(numero)):
    final += numero[i]
  return final

num = input('Digite um numero:')

print('''A qual base ele pertence:
[2] BINARIO
[4] base 4
[8] OCTAL
[10] DECIMAL
[16] HEXADECIMAL''')

base_inicial = int(input())

print('''Para qual base deseja converter:
[2] converter para BINARIO
[4] converter para base 4
[8] converter para OCTAL
[10] converter para DECIMAL
[16] converter para HEXADECIMAL''')

base_final = int(input())

print (conversor(num,base_inicial,base_final))
