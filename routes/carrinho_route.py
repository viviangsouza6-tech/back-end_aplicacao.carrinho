from fastapi import APIRouter

from schemas.carrinho_schema import (
    CarrinhoProdutoSchema,
    CarrinhoQuantidadeSchema
)

from services.carrinho_service import CarrinhoService


router = APIRouter(
    prefix="/carrinho",
    tags=["Carrinho"]
)


carrinho_service = CarrinhoService()


@router.post("/{idpedido}/produtos")
def adicionar_produto(
    idpedido: int,
    dados: CarrinhoProdutoSchema
):
    return carrinho_service.adicionar_produto(
        idpedido,
        dados.idproduto,
        dados.quantidade
    )


@router.get("/{idpedido}")
def listar_carrinho(idpedido: int):
    return carrinho_service.listar_produtos(idpedido)


@router.put("/{idpedido}/produtos/{idproduto}")
def alterar_quantidade(
    idpedido: int,
    idproduto: int,
    dados: CarrinhoQuantidadeSchema
):
    return carrinho_service.alterar_quantidade(
        idpedido,
        idproduto,
        dados.quantidade
    )


@router.delete("/{idpedido}/produtos/{idproduto}")
def remover_produto(
    idpedido: int,
    idproduto: int
):
    return carrinho_service.remover_produto(
        idpedido,
        idproduto
    )


@router.get("/{idpedido}/total")
def calcular_total(idpedido: int):
    return carrinho_service.calcular_total(idpedido)