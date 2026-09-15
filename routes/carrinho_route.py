
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers.carrinho_controller import CarrinhoController
from database import get_db
from services.carrinho_service import CarrinhoService
from schemas.carrinho_schema import (
    CarrinhoProdutoSchema,
    CarrinhoQuantidadeSchema
)


router = APIRouter(
    prefix="/carrinho",
    tags=["Carrinho"]
)


@router.post("/{idpessoa}/produtos")
def adicionar_produto(
    idpessoa: int,
    dados: CarrinhoProdutoSchema,
    db: Session = Depends(get_db)
):
    service = CarrinhoService(db)
    controller = CarrinhoController(service)

    return controller.adicionar_produto(
        idpessoa,
        dados.idproduto,
        dados.quantidade
    )


@router.get("/{idpessoa}")
def listar_carrinho(
    idpessoa: int,
    db: Session = Depends(get_db)
):
    service = CarrinhoService(db)
    controller = CarrinhoController(service)

    return controller.listar_produtos(
        idpessoa
    )


@router.put("/{idpessoa}/produtos/{idproduto}")
def alterar_quantidade(
    idpessoa: int,
    idproduto: int,
    dados: CarrinhoQuantidadeSchema,
    db: Session = Depends(get_db)
):
    service = CarrinhoService(db)
    controller = CarrinhoController(service)

    return controller.alterar_quantidade(
        idpessoa,
        idproduto,
        dados.quantidade
    )


@router.delete("/{idpessoa}/produtos/{idproduto}")
def remover_produto(
    idpessoa: int,
    idproduto: int,
    db: Session = Depends(get_db)
):
    service = CarrinhoService(db)
    controller = CarrinhoController(service)

    return controller.remover_produto(
        idpessoa,
        idproduto
    )


@router.get("/{idpessoa}/total")
def calcular_total(
    idpessoa: int,
    db: Session = Depends(get_db)
):
    service = CarrinhoService(db)
    controller = CarrinhoController(service)

    return controller.calcular_total(
        idpessoa
    )


@router.put("/{idpessoa}/finalizar")
def finalizar_carrinho(
    idpessoa: int,
    db: Session = Depends(get_db)
):
    service = CarrinhoService(db)
    controller = CarrinhoController(service)

    return controller.finalizar_carrinho(
        idpessoa
    )

