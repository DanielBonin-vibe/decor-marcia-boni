from datetime import datetime

from sqlalchemy import String, ForeignKey, Boolean, DateTime, func, CheckConstraint, true, Index, text
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    __table_args__ = (

        CheckConstraint("perfil IN ('funcionario', 'admin')", name='ck_usuario_perfil_valido'),

        CheckConstraint("LENGTH(TRIM(nome)) > 0", name='ck_usuario_tamanho_nome_valido'),

        CheckConstraint("LENGTH(TRIM(senha_hash)) > 0", name='ck_usuario_tamanho_senha_hash__valido'),

        CheckConstraint("LENGTH(TRIM(email)) > 0", name='ck_usuario_formato_email_valido'),

        Index("uq_usuario_email_lower", text("LOWER(email)"), unique=True)
    )

    id_usuario: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(String(100), nullable=False)

    senha_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    perfil: Mapped[str] = mapped_column(String(100), nullable=False)

    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=true())

    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
    data_atualizacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())