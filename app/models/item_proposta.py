
from sqlalchemy import String, Integer, ForeignKey, Boolean, func, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class ItemProposta(Base):
    __tablename__ = 'item_proposta'

    __table_args__ = (

        CheckConstraint("quantidade > 0", name='ck_item_proposta_quantidade_valida'),

        CheckConstraint("categoria IN ('movel', 'decoracao', 'iluminacao', 'flores', 'servico', 'outros')", name='ck_item_proposta_categorias_validas'),

        CheckConstraint("ordem > 0", name='ck_item_proposta_ordem_valida'),

        CheckConstraint("LENGTH(TRIM(nome)) > 0", name='ck_item_proposta_tamanho_nome_valido')

    )

    id_item_proposta: Mapped[int] = mapped_column(primary_key=True)

    id_proposta: Mapped[int] = mapped_column(Integer, ForeignKey('proposta.id_proposta'), nullable=False)

    nome: Mapped[str] = mapped_column(String(100), nullable=False)

    descricao: Mapped[str | None] = mapped_column(String(1000), nullable=True) 

    quantidade: Mapped[int] = mapped_column(Integer, nullable=False)

    categoria: Mapped[str] = mapped_column(String(100), nullable=False, server_default='decoracao')

    opcional: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default='false')

    ordem: Mapped[int] = mapped_column(Integer, nullable=False)