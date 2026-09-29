from datetime import datetime
from decimal import Decimal 

from sqlalchemy import String, Integer, ForeignKey, DateTime, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Proposta(Base):
    __tablename__ = 'proposta'

    id_proposta: Mapped[int] = mapped_column(primary_key=True)

    id_evento: Mapped[int] = mapped_column(Integer, ForeignKey('evento.id_evento'), nullable=False)

    versao: Mapped[int] = mapped_column(Integer, nullable=False)

    titulo: Mapped[str] = mapped_column(String(100), nullable=False)

    observacoes: Mapped[str | None] = mapped_column(String(1000), nullable=True)

    valor_decoracao: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)

    valor_moveis: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)

    valor_adicionais: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)

    valor_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)

    condicao_pagamento: Mapped[str] = mapped_column(String(100), nullable=False)

    status: Mapped[str] = mapped_column(String(100), nullable=False)

    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    data_atualizacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())