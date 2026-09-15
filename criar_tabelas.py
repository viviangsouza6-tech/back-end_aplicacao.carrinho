from database import Base, engine

from models.pessoa_model import Pessoa
from models.setor_model import Setor
from models.produto_model import Produto
from models.pedido_model import Pedido
from models.pedidoproduto_model import PedidoProduto


print("Criando tabelas...")

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")