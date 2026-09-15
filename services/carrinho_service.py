
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from repositories.carrinho_repository import CarrinhoRepository
from repositories.produto_repository import ProdutoRepository


class CarrinhoService:

    def __init__(self, db: Session):
        self.repository = CarrinhoRepository(db)
        self.produto_repository = ProdutoRepository(db)

    def obter_ou_criar_carrinho(self, idpessoa: int):
        carrinho = self.repository.buscar_carrinho_ativo(
            idpessoa
        )

        if carrinho:
            return carrinho

        return self.repository.criar_carrinho(
            idpessoa
        )

    def adicionar_produto(
        self,
        idpessoa: int,
        idproduto: int,
        quantidade: int
    ):
        if quantidade <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A quantidade deve ser maior que zero"
            )

        produto = self.produto_repository.buscar_por_id(
            idproduto
        )

        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado"
            )

        carrinho = self.obter_ou_criar_carrinho(
            idpessoa
        )

        item_existente = self.repository.buscar_produto(
            carrinho.idcarrinho,
            idproduto
        )

        if item_existente:
            nova_quantidade = (
                item_existente.quantidade + quantidade
            )

            if produto.estoque < nova_quantidade:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Estoque insuficiente"
                )

            return self.repository.alterar_quantidade(
                carrinho.idcarrinho,
                idproduto,
                nova_quantidade
            )

        if produto.estoque < quantidade:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Estoque insuficiente"
            )

        return self.repository.adicionar_produto(
            carrinho.idcarrinho,
            idproduto,
            quantidade
        )

    def listar_produtos(self, idpessoa: int):
        carrinho = self.repository.buscar_carrinho_ativo(
            idpessoa
        )

        if not carrinho:
            return []

        return self.repository.listar_produtos(
            carrinho.idcarrinho
        )

    def alterar_quantidade(
        self,
        idpessoa: int,
        idproduto: int,
        quantidade: int
    ):
        if quantidade <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A quantidade deve ser maior que zero"
            )

        carrinho = self.repository.buscar_carrinho_ativo(
            idpessoa
        )

        if not carrinho:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Carrinho não encontrado"
            )

        produto = self.produto_repository.buscar_por_id(
            idproduto
        )

        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado"
            )

        if produto.estoque < quantidade:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Estoque insuficiente"
            )

        item = self.repository.alterar_quantidade(
            carrinho.idcarrinho,
            idproduto,
            quantidade
        )

        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado no carrinho"
            )

        return item

    def remover_produto(
        self,
        idpessoa: int,
        idproduto: int
    ):
        carrinho = self.repository.buscar_carrinho_ativo(
            idpessoa
        )

        if not carrinho:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Carrinho não encontrado"
            )

        item = self.repository.remover_produto(
            carrinho.idcarrinho,
            idproduto
        )

        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado no carrinho"
            )

        return item

    def calcular_total(self, idpessoa: int):
        carrinho = self.repository.buscar_carrinho_ativo(
            idpessoa
        )

        if not carrinho:
            return 0

        return self.repository.calcular_total(
            carrinho.idcarrinho
        )

    def finalizar_carrinho(self, idpessoa: int):
        carrinho = self.repository.buscar_carrinho_ativo(
            idpessoa
        )

        if not carrinho:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Carrinho ativo não encontrado"
            )

        return self.repository.finalizar_carrinho(
            carrinho.idcarrinho
        )

