from pydantic import BaseModel


class CarrinhoProdutoSchema(BaseModel):
    idproduto: int
    quantidade: int


class CarrinhoQuantidadeSchema(BaseModel):
    quantidade: int