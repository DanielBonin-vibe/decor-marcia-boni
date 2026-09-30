from datetime import datetime 
from pydantic import BaseModel, Field, ConfigDict

class DocumentoCreate(BaseModel):
    id_evento: int
    tipo: str = Field(min_length=3, max_length=100)
    versao: int
    nome_arquivo: str = Field(min_length=3, max_length=100)

class DocumentoUpdate(BaseModel):
    id_evento: int | None = None
    tipo: str | None = Field(default=None, min_length=3, max_length=100)
    versao: int | None = None
    nome_arquivo: str | None = Field(default=None, min_length=3, max_length=100)

class DocumentoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_docuemnto: int
    id_evento: int
    tipo: str
    versao: int
    nome_arquivo: str
    drive_file_id: str | None
    drive_url: str | None 
    data_geracao: datetime