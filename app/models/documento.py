from datetime import datetime

from sqlalchemy import String, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Documento(Base):
    __tablename__ = 'documento'

    id_documento: Mapped[int] = mapped_column(primary_key=True)

    id_evento: Mapped[int] = mapped_column(Integer, ForeignKey('evento.id_evento'), nullable=False)

    tipo: Mapped[str] = mapped_column(String(100), nullable=False)

    versao: Mapped[int] = mapped_column(Integer, nullable=False)

    nome_arquivo: Mapped[str] = mapped_column(String(100), nullable=False)

    drive_file_id: Mapped[str] = mapped_column(String, nullable=False)

    drive_url: Mapped[str] = mapped_column(String, nullable=False)

    data_geracao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())