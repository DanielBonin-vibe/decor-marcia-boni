from datetime import datetime 
from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

class DocumentoCreate(BaseModel):
    id_evento: int = Field(gt=0)

    id_proposta: int | None = Field(default=None, gt=0)

    tipo: Literal['proposta', 'contrato', 'recibo', 'orcamento', 'nota_fiscal','comprovante', 'cotacao', 'outro']

    versao: int = Field(default=1, gt=0)

    nome_arquivo: str = Field(min_length=3, max_length=255)

    formato: Literal['pdf', 'docx', 'xlsx', 'jpg', 'png']

    origem: Literal['documento_proprio', 'documento_externo']

class DocumentoUpdate(BaseModel):
    id_evento: int | None = Field(default=None, gt=0)

    id_proposta: int | None = Field(default=None, gt=0)

    tipo: Literal['proposta', 'contrato', 'recibo', 'orcamento', 'nota_fiscal','comprovante', 'cotacao', 'outro'] | None = None

    versao: int | None = Field(default=None, gt=0)

    nome_arquivo: str | None = Field(default=None, min_length=3, max_length=255)

    formato: Literal['pdf', 'docx', 'xlsx', 'jpg', 'png'] | None = None

    origem: Literal['documento_proprio', 'documento_externo'] | None = None


class DocumentoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_documento: int
    id_evento: int
    id_proposta: int | None

    tipo: str
    versao: int
    nome_arquivo: str
    formato: str
    origem: str

    drive_file_id: str | None
    drive_url: str | None

    data_cadastro: datetime