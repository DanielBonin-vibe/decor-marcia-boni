from datetime import datetime, time

from sqlalchemy import String, Integer, DateTime, Date, Time, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Evento(Base):
    __tablename__ = 'evento'

    id_evento: Mapped[int] = mapped_column(primary_key=True)

    id_cliente: Mapped[int] = mapped_column(Integer, ForeignKey('cliente.id_cliente'), nullable=False)

    tipo_evento: Mapped[str] = mapped_column(String, nullable=False)

    data_evento: Mapped[datetime] = mapped_column(Date, nullable=False)

    horario_evento: Mapped[time] = mapped_column(Time, nullable=False)

    nome_local: Mapped[str] = mapped_column(String(100), nullable=False)

    endereco_local: Mapped[str] = mapped_column(String(500), unique=True, nullable=False) 

    numero_convidados: Mapped[int] = mapped_column(Integer, nullable=False)

    status: Mapped[str] = mapped_column(String(100), nullable=False)

    observacoes: Mapped[str] = mapped_column(String(1000), nullable=False)

    drive_folder_id: Mapped[int] = mapped_column(Integer, nullable=False)

    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    data_atualizacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())