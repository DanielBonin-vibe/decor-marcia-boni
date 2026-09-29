from datetime import datetime, time
from decimal import Decimal

from sqlalchemy import String, Integer, Numeric, DateTime, Date, Time, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base 

class Pagamento(Base):
    __tablename__ = 'pagamento'

    id_pagamento: Mapped[int] = mapped_column(primary_key=True)

    id_parcela: Mapped[int] = mapped_column(Integer, ForeignKey('parcela.id_parcela'), nullable=False)

    valor: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)

    data_pagamento: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    forma_pagamento: Mapped[str] = mapped_column(String(50), nullable=False)

    observacoes: Mapped[str | None] = mapped_column(String(1000), nullable=True)

    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

