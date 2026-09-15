
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class CarrinhoProduto(Base):
    __tablename__ = "carrinho_produto"

    idcarrinho: Mapped[int] = mapped_column(
        ForeignKey("carrinho.idcarrinho"),
        primary_key=True
    )

    idproduto: Mapped[int] = mapped_column(
        ForeignKey("produto.idproduto"),
        primary_key=True
    )

    quantidade: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    carrinho = relationship(
        "Carrinho"
    )

    produto = relationship(
        "Produto"
    )

