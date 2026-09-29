from datetime import datetime 
from decimal import Decimal

from sqlalchemy import String, Integer, Boolean, Numeric, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Contrato(Base):
    __tablename__ = 'contrato'

    id_contrato: Mapped[int] = mapped_column(primary_key=True)

    id_evento: Mapped[int] = mapped_column(Integer, ForeignKey('evento.id_evento'), nullable=False)

    id_proposta: Mapped[int] = mapped_column(Integer, ForeignKey('proposta.id_proposta'), nullable=False)

    numero: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    valor_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)

    data_assinatura: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    status: Mapped[str] = mapped_column(String(100), nullable=False)

    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    data_atualizacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())