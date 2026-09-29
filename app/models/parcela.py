from datetime import datetime, date
from decimal import Decimal 

from sqlalchemy import String, Integer, ForeignKey, DateTime, Date, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Parcela(Base):
    __tablename__ = 'parcela'

    id_parcela: Mapped[int] = mapped_column(primary_key=True)

    id_contrato: Mapped[int] = mapped_column(Integer, ForeignKey('contrato.id_contrato'), nullable=False)

    numero_parcela: Mapped[int] = mapped_column(Integer, nullable=False)

    valor: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)

    data_vencimento: Mapped[date] = mapped_column(Date, nullable=False)

    status: Mapped[str] = mapped_column(String(100), nullable=False)

    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    data_atualizacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())