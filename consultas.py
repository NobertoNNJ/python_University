from esquema import *

# 1 - Liste todo o histórico de preços (valor, data) do produto "Caneta Bic esferográfica azul".
print()

historico = (Historico_Precos.select(Historico_Precos.valor, Historico_Precos.data).join(Produto).where(Produto.descricao == 'Caneta Bic esferográfica azul'))

historico_caneta = [(registro.valor,registro.data) for registro in historico]

for valor, data in historico_caneta:
    print(f"Valor: {valor}, Data: {data}")

print()

# 2 - Liste descrição e preço de todos os produtos da categoria "Papelaria", ordenados no menor para o maior preço.

papelaria = (Produto.select(Produto.descricao, Produto.valor).join(Categoria).where(Categoria.descricao == 'Papelaria').order_by(Produto.valor))

lista_papelaria = [(registro.descricao, registro.valor) for registro in papelaria]

for descricao, valor in lista_papelaria:
    print(f"Descricao: {descricao}, Valor: {valor}")

print()

# 3 - Recupere os nomes dos clientes que fizeram ao menos uma compra com valor superior a R$ 5.000,00 no mês de setembro/2022. Exiba-os em ordem alfabética.

clientes = (Cliente.select(Cliente.nome).join(Venda).where((Venda.valor_total > 5000) &(Venda.data.year == 2022) & (Venda.data.month == 9)).order_by(Cliente.nome))

nome_cliente = [registro.nome for registro in clientes]

for nome in nome_cliente:
    print(f"Nome: {nome}")
