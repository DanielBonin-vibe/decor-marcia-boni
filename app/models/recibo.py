from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey, DateTime, func, CheckConstraint, Sequence
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Recibo(Base):
    __tablename__ = 'recibo'

    __table_args__ = (

        CheckConstraint("numero_recibo > 0", name='ck_numero_recibo_valido'),

    )

    id_recibo: Mapped[int] = mapped_column(primary_key=True)

    id_pagamento: Mapped[int] = mapped_column(Integer, ForeignKey('pagamento.id_pagamento'), unique=True, nullable=False)

    numero_recibo: Mapped[int] = mapped_column(Integer, Sequence('seq_numero_recibo'), unique=True, nullable=False)

    observacoes: Mapped[str | None] = mapped_column(String(1000), nullable=True)

    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    data_emissao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())