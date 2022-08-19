def tempoAlugado():
  dias = int(input('quantos dias alugado?'))
  km = int(input('quantos kilimetors percorrido?'))
  pagar = (dias * 60) + (km * 0.15)
  print ("preço a pagar: R${:.2f}".format(pagar))
tempoAlugado()
