
from sqlalchemy import String, Integer, ForeignKey, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class ItemProposta(Base):
    __tablename__ = 'item_proposta'

    id_item_proposta: Mapped[int] = mapped_column(primary_key=True)

    id_proposta: Mapped[int] = mapped_column(Integer, ForeignKey('proposta.id_proposta'), nullable=False)

    nome: Mapped[str] = mapped_column(String(100), nullable=False)

    descricao: Mapped[str | None] = mapped_column(String(1000), nullable=True) 

    quantidade: Mapped[int] = mapped_column(Integer, nullable=False)

    categoria: Mapped[str] = mapped_column(String(100), nullable=False)

    opcional: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    ordem: Mapped[int] = mapped_column(Integer, nullable=False)