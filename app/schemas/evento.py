from datetime import datetime, date, time
from pydantic import BaseModel, Field, ConfigDict

class EventoCreate(BaseModel):
    id_cliente: int
    tipo_evento: str = Field(min_length=3, max_length=100)
    data_evento: date
    horario_evento: time
    nome_local: str = Field(min_length=3, max_length=100)
    endereco_local: str = Field(min_length=3, max_length=500)
    numero_convidados: int
    status: str = Field(min_length=3, max_length=100)
    observacoes: str | None = Field(default=None, min_length=3, max_length=1000)

class EventoUpdate(BaseModel):
    id_cliente: int | None = None
    tipo_evento: str | None = Field(default=None, min_length=3, max_length=100)
    data_evento: date | None = None
    horario_evento: time | None = None
    nome_local: str | None = Field(default=None, min_length=3, max_length=100)
    endereco_local: str | None = Field(default=None, min_length=3, max_length=500)
    numero_convidados: int | None = None
    status: str | None = Field(default=None, min_length=3, max_length=100)
    observacoes: str | None = Field(default=None, min_length=3, max_length=1000)

class EventoReponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_evento: int
    id_cliente: int
    tipo_evento: str
    data_evento: date
    horario_evento: time
    nome_local: str
    endereco_local: str 
    numero_convidados: int
    status: str | None
    observacoes: str | None
    drive_folder_id: str | None
    data_criacao: datetime
    data_atualizacao: datetime