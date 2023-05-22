from peewee import *

# Conexão com o banco de dados
db = PostgresqlDatabase('BancoAtv', user='postgres', password='mypassword',host='localhost', port=5432)

# Definição das classes para cada tabela

class BaseModel(Model):
    class Meta():
        database = db

class Categoria(BaseModel):
    id = AutoField(primary_key=True)
    descricao = CharField()

class Cliente(BaseModel):
    id = AutoField(primary_key=True)
    nome = CharField()
    endereco = CharField()
    data_registro = DateField()

class Produto(BaseModel):
    id = AutoField(primary_key=True)
    descricao = CharField()
    id_categoria = ForeignKeyField(Categoria, backref='produtos')
    valor = DecimalField(10,2)

class Historico_Precos(BaseModel):
    id = AutoField(primary_key=True)
    id_produto = ForeignKeyField(Produto, backref='historico_precos')
    valor = DecimalField(10,2)
    data = DateField()

class Venda(BaseModel):
    id = AutoField(primary_key=True)
    id_produto = ForeignKeyField(Produto, backref='vendas')
    id_cliente = ForeignKeyField(Cliente, backref='vendas')
    data = DateField()
    quantidade = IntegerField()
    valor_unitario = DecimalField(10,2)
    valor_total = DecimalField(10,2)

# Criação das tabelas
if __name__ == '__main__':
    with db:
        db.create_tables([Categoria, Cliente, Produto, Historico_Precos, Venda])