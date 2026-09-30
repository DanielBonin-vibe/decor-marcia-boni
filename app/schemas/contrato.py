from datetime import datetime 
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict

class ContratoCreate(BaseModel):
    id_evento: int
    id_proposta: int 
    numero: str = Field(min_length=1, max_length=20)
    valor_total: Decimal
    status: str = Field(min_length=3, max_length=100)

class ContratoUpdate(BaseModel):
    id_evento: int | None = None
    id_proposta: int | None = None
    numero: str | None = Field(default=None, min_length=1, max_length=20)
    valor_total: Decimal | None = None
    status: str | None = Field(default=None, min_length=3, max_length=100)

class ContratoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_evento: int
    id_proposta: int
    numero: str
    valor_total: Decimal
    status: str
    data_criacao: datetime
    data_atualizacao: datetime