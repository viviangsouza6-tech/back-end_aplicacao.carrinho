
from sqlalchemy.orm import Session

from models.carrinho_model import Carrinho
from models.carrinhoproduto_model import CarrinhoProduto
from models.produto_model import Produto


class CarrinhoRepository:

    def __init__(self, db: Session):
        self.db = db

    def buscar_carrinho_ativo(self, idpessoa: int):
        return (
            self.db.query(Carrinho)
            .filter(
                Carrinho.idpessoa == idpessoa,
                Carrinho.status_carrinho == "ATIVO"
            )
            .first()
        )

    def criar_carrinho(self, idpessoa: int):
        carrinho = Carrinho(
            idpessoa=idpessoa,
            status_carrinho="ATIVO"
        )

        self.db.add(carrinho)
        self.db.commit()
        self.db.refresh(carrinho)

        return carrinho

    def adicionar_produto(
        self,
        idcarrinho: int,
        idproduto: int,
        quantidade: int
    ):
        item = CarrinhoProduto(
            idcarrinho=idcarrinho,
            idproduto=idproduto,
            quantidade=quantidade
        )

        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)

        return item

    def listar_produtos(self, idcarrinho: int):
        return (
            self.db.query(CarrinhoProduto)
            .filter(
                CarrinhoProduto.idcarrinho == idcarrinho
            )
            .all()
        )

    def buscar_produto(
        self,
        idcarrinho: int,
        idproduto: int
    ):
        return (
            self.db.query(CarrinhoProduto)
            .filter(
                CarrinhoProduto.idcarrinho == idcarrinho,
                CarrinhoProduto.idproduto == idproduto
            )
            .first()
        )

    def alterar_quantidade(
        self,
        idcarrinho: int,
        idproduto: int,
        quantidade: int
    ):
        item = self.buscar_produto(
            idcarrinho,
            idproduto
        )

        if not item:
            return None

        item.quantidade = quantidade

        self.db.commit()
        self.db.refresh(item)

        return item

    def remover_produto(
        self,
        idcarrinho: int,
        idproduto: int
    ):
        item = self.buscar_produto(
            idcarrinho,
            idproduto
        )

        if not item:
            return None

        self.db.delete(item)
        self.db.commit()

        return item

    def calcular_total(self, idcarrinho: int):
        itens = (
            self.db.query(CarrinhoProduto)
            .filter(
                CarrinhoProduto.idcarrinho == idcarrinho
            )
            .all()
        )

        total = 0

        for item in itens:
            produto = (
                self.db.query(Produto)
                .filter(
                    Produto.idproduto == item.idproduto
                )
                .first()
            )

            if produto:
                total += (
                    float(produto.valor_unitario)
                    * item.quantidade
                )

        return total

    def finalizar_carrinho(self, idcarrinho: int):
        carrinho = (
            self.db.query(Carrinho)
            .filter(
                Carrinho.idcarrinho == idcarrinho
            )
            .first()
        )

        if not carrinho:
            return None

        carrinho.status_carrinho = "FINALIZADO"

        self.db.commit()
        self.db.refresh(carrinho)

        return carrinho

