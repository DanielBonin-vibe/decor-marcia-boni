from datetime import datetime 
from decimal import Decimal

from sqlalchemy import String, Integer, Numeric, ForeignKey, DateTime, func, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Contrato(Base):
    __tablename__ = 'contrato'

    __table_args__ = (

        CheckConstraint("valor_total > 0", name='ck_contrato_valor_positivo'),

        CheckConstraint("status_contrato IN ('rascunho', 'assinado', 'pendente_assinatura', 'cancelado')", name='ck_contrato_status_contrato'),

        CheckConstraint("""
        (status_contrato = 'assinado' AND data_assinatura IS NOT NULL) OR
        (status_contrato = 'rascunho' AND data_assinatura IS NULL) OR
        (status_contrato = 'pendente_assinatura' AND data_assinatura IS NULL) OR
        (status_contrato = 'cancelado')
        """, name='ck_contrato_integridade_assinatura'),
        )

    id_contrato: Mapped[int] = mapped_column(primary_key=True)

    id_proposta: Mapped[int] = mapped_column(Integer, ForeignKey('proposta.id_proposta'), unique=True, nullable=False)

    numero: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    valor_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)

    data_assinatura: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    status_contrato: Mapped[str] = mapped_column(String(100), nullable=False, server_default='rascunho')

    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    data_atualizacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())