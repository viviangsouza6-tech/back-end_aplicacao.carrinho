from fastapi import APIRouter

router = APIRouter(
    prefix="/carrinho",
    tags=["Carrinho"]
)


@router.post("/{idpedido}/produtos")
def adicionar_produto(
    idpedido: int,
    idproduto: int,
    quantidade: int
):
    pass


@router.get("/{idpedido}")
def listar_carrinho(idpedido: int):
    pass


@router.put("/{idpedido}/produtos/{idproduto}")
def alterar_quantidade(
    idpedido: int,
    idproduto: int,
    quantidade: int
):
    pass


@router.delete("/{idpedido}/produtos/{idproduto}")
def remover_produto(
    idpedido: int,
    idproduto: int
):
    pass


@router.get("/{idpedido}/total")
def calcular_total(idpedido: int):
    pass