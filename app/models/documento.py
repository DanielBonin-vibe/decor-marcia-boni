from datetime import datetime

from sqlalchemy import String, Integer, DateTime, ForeignKey, func, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Documento(Base):
    __tablename__ = 'documento'

    __table_args__ = (

        CheckConstraint("tipo IN ('proposta', 'contrato', 'recibo', 'orcamento','nota_fiscal', 'comprovante', 'cotacao', 'outro')", name='ck_documento_tipo_permitido'),

        CheckConstraint("versao > 0", name='ck_documento_versao_positiva'),

        CheckConstraint("formato IN ('pdf', 'docx', 'xlsx', 'jpg', 'png')", name='ck_documento_formato_permitido'),

        CheckConstraint("origem IN ('documento_proprio', 'documento_externo')", name='ck_documento_origem_permitida')

    )

    id_documento: Mapped[int] = mapped_column(primary_key=True)

    id_evento: Mapped[int] = mapped_column(Integer, ForeignKey('evento.id_evento'), nullable=False)

    id_proposta: Mapped[int | None] = mapped_column(Integer, ForeignKey('proposta.id_proposta'), nullable=True)

    tipo: Mapped[str] = mapped_column(String(100), nullable=False)

    versao: Mapped[int] = mapped_column(Integer, nullable=False, server_default='1')

    nome_arquivo: Mapped[str] = mapped_column(String(255), nullable=False)

    formato: Mapped[str] = mapped_column(String(10), nullable=False)

    origem: Mapped[str] = mapped_column(String(30), nullable=False)

    drive_file_id: Mapped[str | None] = mapped_column(String(255), nullable=True)

    drive_url: Mapped[str | None] = mapped_column(String(255), nullable=True)

    data_cadastro: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())