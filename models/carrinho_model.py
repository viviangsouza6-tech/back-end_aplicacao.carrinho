
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Carrinho(Base):
    __tablename__ = "carrinho"

    idcarrinho: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    idpessoa: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("pessoa.idpessoa"),
        nullable=False
    )

    data_criacao: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default="CURRENT_TIMESTAMP"
    )

    status_carrinho: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )


