from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func, CheckConstraint, Index, text
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Cliente(Base):
    __tablename__ = 'cliente'

    __table_args__ = (
        
        CheckConstraint("cpf ~ '^[0-9]{11}$'",  name="ck_cliente_cpf_formato"),
        
        CheckConstraint("cep ~ '^[0-9]{8}$'", name="ck_cliente_cep_formato"),

        CheckConstraint("estado IN ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO')", name="ck_cliente_estado_formato"),
    
        CheckConstraint("telefone ~ '^[0-9]{10,11}$'", name="ck_cliente_telefone_formato"),

        Index("up_cliente_email_lower", text("LOWER(email)"), unique=True),
    )

    id_cliente: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(150), nullable=False)

    nacionalidade: Mapped[str | None] = mapped_column(String(150), nullable=True)

    estado_civil: Mapped[str | None] = mapped_column(String(150), nullable=True)

    profissao: Mapped[str | None] = mapped_column(String(150), nullable=True)

    cpf: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)

    telefone: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)

    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)

    endereco: Mapped[str] = mapped_column(String(150), nullable=False)

    cidade: Mapped[str] = mapped_column(String(150), nullable=False)

    estado: Mapped[str] = mapped_column(String(2), nullable=False)

    cep: Mapped[str] = mapped_column(String(8), nullable=False)

    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default='true')

    data_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    data_atualizacao: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())