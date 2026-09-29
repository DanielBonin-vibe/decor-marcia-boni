from datetime import datetime

from sqlalchemy import String, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id_usuario: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    senha_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    perfil: Mapped[str] = mapped_column(String(100), nullable=False)

    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False)

    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
    data_atualizacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())