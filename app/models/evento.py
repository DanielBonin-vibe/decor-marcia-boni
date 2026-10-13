from datetime import datetime, time, date

from sqlalchemy import String, Integer, DateTime, Date, Time, ForeignKey, func, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Evento(Base):
    __tablename__ = 'evento'

    __table_args__ = (

        CheckConstraint("numero_convidados > 0", name='ck_evento_convidados_validos'),

        CheckConstraint("tipo_evento IN ('casamento', 'aniversario', 'formatura', 'corporativo', 'batizado', 'outro')", name='ck_evento_tipos_validos'),

        CheckConstraint("status IN ('planejamento', 'confirmado', 'realizado', 'cancelado')", name='ck_evento_status_valido'),

    )

    id_evento: Mapped[int] = mapped_column(primary_key=True)

    id_cliente: Mapped[int] = mapped_column(Integer, ForeignKey('cliente.id_cliente'), nullable=False)

    tipo_evento: Mapped[str] = mapped_column(String(100), nullable=False)

    data_evento: Mapped[date] = mapped_column(Date, nullable=False)

    horario_evento: Mapped[time] = mapped_column(Time, nullable=False)

    nome_local: Mapped[str] = mapped_column(String(100), nullable=False)

    endereco_local: Mapped[str] = mapped_column(String(500), nullable=False) 

    numero_convidados: Mapped[int] = mapped_column(Integer, nullable=False)

    status: Mapped[str] = mapped_column(String(100), nullable=False, server_default='planejamento')

    observacoes: Mapped[str | None] = mapped_column(String(1000), nullable=True)

    drive_folder_id: Mapped[str | None] = mapped_column(String(255), nullable=True)

    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    data_atualizacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())