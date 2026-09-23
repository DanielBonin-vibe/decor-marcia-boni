from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Cliente(Base):
    __tablename__ = 'cliente'

    id_cliente: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(150), nullable=False)

    nacionalidade: Mapped[str | None] = mapped_column(String(150), nullable=True)

    estado_civi: Mapped[str | None] = mapped_column(String(150), nullable=True)

    profissao: Mapped[str | None] = mapped_column(String(150), nullable=True)

    cpf: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)

    telefone: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)

    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)

    endereco: Mapped[str] = mapped_column(String(150), nullable=False)

    cidade: Mapped[str] = mapped_column(String(150), nullable=False)

    estado: Mapped[str] = mapped_column(String(150), nullable=False)

    cep: Mapped[str] = mapped_column(String(8), nullable=False)

    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False)

    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    data_atualizacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())