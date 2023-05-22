from datetime import date, datetime
from esquema import *

lista_categoria = [
    {'descricao' : 'Papelaria'},
    {'descricao' : 'Eletrônicos'},
    {'descricao' : 'Roupas'},
    {'descricao' : 'Alimentos'},
    {'descricao' : 'Acessórios'}
]

Categoria.insert_many(lista_categoria).execute()

lista_cliente = [
    {'nome' : 'João', 'endereco' : 'Rua pindaiba, 123', 'data_registro' : date.today()},
    {'nome' : 'Maria', 'endereco' : 'Rua do lado, 231', 'data_registro' : date.today()},
    {'nome' : 'Jose', 'endereco' : 'Rua de cima, 321', 'data_registro' : date.today()},
    {'nome' : 'Josefa', 'endereco' : 'Rua de baixo, 312', 'data_registro' : date.today()},
    {'nome' : 'Gertrudes', 'endereco' : 'Rua dela, 213', 'data_registro' : date.today()}
]

Cliente.insert_many(lista_cliente).execute()

categoria_papelaria = Categoria.select().where(Categoria.descricao == 'Papelaria').get().id
categoria_Eletrônicos = Categoria.select().where(Categoria.descricao == 'Eletrônicos').get().id
categoria_Roupas = Categoria.select().where(Categoria.descricao == 'Roupas').get().id
categoria_Alimentos = Categoria.select().where(Categoria.descricao == 'Alimentos').get().id
categoria_Acessórios = Categoria.select().where(Categoria.descricao == 'Acessórios').get().id

lista_produtos = [
    {'descricao' : 'Caneta Bic esferográfica azul', 'id_categoria': categoria_papelaria, 'valor' : 1.00},
    {'descricao' : 'Notebook Gamer Dell G15', 'id_categoria' : categoria_Eletrônicos, 'valor' : 5500.00},
    {'descricao' : 'Camiseta', 'id_categoria' : categoria_Roupas, 'valor' : 50.00},
    {'descricao' : 'Chocolate me barra', 'id_categoria' : categoria_Alimentos, 'valor' : 8.00},
    {'descricao' : 'Anel Solitario', 'id_categoria' : categoria_Acessórios, 'valor' : 10000.00}
]

Produto.insert_many(lista_produtos).execute()

lista_precos = [
    {'id_produto': Produto.id, 'valor': Produto.valor, 'data': datetime(2020, 1, 1, 7, 00, 00).strftime('%Y-%m-%d %H:%M:%S')} for Produto in Produto.select()
]

Historico_Precos.insert_many(lista_precos).execute()


lista_vendas = [
    {'id_produto' : Produto.select().where(Produto.descricao == 'Anel Solitario').get().id,
    'id_cliente' : Cliente.select().where(Cliente.nome == 'João').get().id, 
    'data': datetime(2022, 9, 26, 9, 45, 39).strftime('%Y-%m-%d %H:%M:%S'), 
    'quantidade' : 1, 
    'valor_unitario' : Produto.select().where(Produto.descricao == 'Anel Solitario').get().valor, 
    'valor_total' : 1 * Produto.select().where(Produto.descricao == 'Anel Solitario').get().valor},

    {'id_produto' : Produto.select().where(Produto.descricao == 'Chocolate me barra').get().id,
    'id_cliente' : Cliente.select().where(Cliente.nome == 'Jose').get().id, 
    'data': date.today(), 
    'quantidade' : 5, 
    'valor_unitario' : Produto.select().where(Produto.descricao == 'Chocolate me barra').get().valor, 
    'valor_total' : 5 * Produto.select().where(Produto.descricao == 'Chocolate me barra').get().valor},

    {'id_produto' : Produto.select().where(Produto.descricao == 'Camiseta').get().id,
    'id_cliente' : Cliente.select().where(Cliente.nome == 'Maria').get().id, 
    'data': datetime(2022, 9, 15, 10, 30, 59).strftime('%Y-%m-%d %H:%M:%S'), 
    'quantidade' : 300, 
    'valor_unitario' : Produto.select().where(Produto.descricao == 'Camiseta').get().valor, 
    'valor_total' : 300 * Produto.select().where(Produto.descricao == 'Camiseta').get().valor},

    {'id_produto' : Produto.select().where(Produto.descricao == 'Caneta Bic esferográfica azul').get().id,
    'id_cliente' : Cliente.select().where(Cliente.nome == 'Josefa').get().id, 
    'data': date.today(), 
    'quantidade' : 2, 
    'valor_unitario' : Produto.select().where(Produto.descricao == 'Caneta Bic esferográfica azul').get().valor, 
    'valor_total' : 2 * Produto.select().where(Produto.descricao == 'Caneta Bic esferográfica azul').get().valor},

    {'id_produto' : Produto.select().where(Produto.descricao == 'Camiseta').get().id,
    'id_cliente' : Cliente.select().where(Cliente.nome == 'Gertrudes').get().id, 
    'data': datetime(2022,9, 3, 7, 59, 15).strftime('%Y-%m-%d %H:%M:%S'), 
    'quantidade' : 200, 
    'valor_unitario' : Produto.select().where(Produto.descricao == 'Camiseta').get().valor, 
    'valor_total' : 200 * Produto.select().where(Produto.descricao == 'Camiseta').get().valor},

    {'id_produto' : Produto.select().where(Produto.descricao == 'Camiseta').get().id,
    'id_cliente' : Cliente.select().where(Cliente.nome == 'Gertrudes').get().id, 
    'data': datetime(2023,4, 20, 10, 59, 15).strftime('%Y-%m-%d %H:%M:%S'), 
    'quantidade' : 400, 
    'valor_unitario' : Produto.select().where(Produto.descricao == 'Camiseta').get().valor, 
    'valor_total' : 400 * Produto.select().where(Produto.descricao == 'Camiseta').get().valor},

    {'id_produto' : Produto.select().where(Produto.descricao == 'Camiseta').get().id,
    'id_cliente' : Cliente.select().where(Cliente.nome == 'Maria').get().id, 
    'data': datetime(2023, 2, 13, 9, 30, 59).strftime('%Y-%m-%d %H:%M:%S'), 
    'quantidade' : 350, 
    'valor_unitario' : Produto.select().where(Produto.descricao == 'Camiseta').get().valor, 
    'valor_total' : 350 * Produto.select().where(Produto.descricao == 'Camiseta').get().valor},

    {'id_produto' : Produto.select().where(Produto.descricao == 'Notebook Gamer Dell G15').get().id,
    'id_cliente' : Cliente.select().where(Cliente.nome == 'João').get().id, 
    'data': datetime(2021, 12, 31, 16, 45, 39).strftime('%Y-%m-%d %H:%M:%S'), 
    'quantidade' : 5, 
    'valor_unitario' : Produto.select().where(Produto.descricao == 'Notebook Gamer Dell G15').get().valor, 
    'valor_total' : 5 * Produto.select().where(Produto.descricao == 'Notebook Gamer Dell G15').get().valor},

    {'id_produto' : Produto.select().where(Produto.descricao == 'Notebook Gamer Dell G15').get().id,
    'id_cliente' : Cliente.select().where(Cliente.nome == 'João').get().id, 
    'data': date.today(), 
    'quantidade' : 10, 
    'valor_unitario' : Produto.select().where(Produto.descricao == 'Notebook Gamer Dell G15').get().valor, 
    'valor_total' : 10 * Produto.select().where(Produto.descricao == 'Notebook Gamer Dell G15').get().valor},

    {'id_produto' : Produto.select().where(Produto.descricao == 'Camiseta').get().id,
    'id_cliente' : Cliente.select().where(Cliente.nome == 'Jose').get().id, 
    'data': date.today(), 
    'quantidade' : 1, 
    'valor_unitario' : Produto.select().where(Produto.descricao == 'Camiseta').get().valor, 
    'valor_total' : 1 * Produto.select().where(Produto.descricao == 'Camiseta').get().valor}

]

Venda.insert_many(lista_vendas).execute()