from datetime import datetime, date, time
from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

class EventoCreate(BaseModel):
    id_cliente: int = Field(gt=0)
    tipo_evento: Literal['casamento', 'aniversario', 'formatura', 'corporativo', 'batizado', 'outro']
    data_evento: date
    horario_evento: time
    nome_local: str = Field(min_length=3, max_length=100)
    endereco_local: str = Field(min_length=3, max_length=500)
    numero_convidados: int = Field(gt=0)
    status: Literal['planejamento', 'confirmado', 'realizado', 'cancelado'] = 'planejamento'
    observacoes: str | None = Field(default=None, min_length=3, max_length=1000)

class EventoUpdate(BaseModel):
    id_cliente: int | None = Field(default=None, gt=0)
    tipo_evento: Literal['casamento', 'aniversario', 'formatura', 'corporativo', 'batizado', 'outro'] | None = None
    data_evento: date | None = None
    horario_evento: time | None = None
    nome_local: str | None = Field(default=None, min_length=3, max_length=100)
    endereco_local: str | None = Field(default=None, min_length=3, max_length=500)
    numero_convidados: int | None = Field(default=None, gt=0)
    status: Literal ['planejamento', 'confirmado', 'realizado', 'cancelado'] | None = None
    observacoes: str | None = Field(default=None, min_length=3, max_length=1000)

class EventoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_evento: int
    id_cliente: int
    tipo_evento: str
    data_evento: date
    horario_evento: time
    nome_local: str
    endereco_local: str 
    numero_convidados: int
    status: str
    observacoes: str | None
    drive_folder_id: str | None
    data_criacao: datetime
    data_atualizacao: datetime