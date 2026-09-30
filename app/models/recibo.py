from datetime import datetime

from sqlalchemy import Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Recibo(Base):
    __tablename__ = 'recibo'

    id_recibo: Mapped[int] = mapped_column(primary_key=True)

    id_pagamento: Mapped[int] = mapped_column(Integer, ForeignKey('pagamento.id_pagamento'), nullable=False)

    numero_recibo: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)

    data_emissao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())