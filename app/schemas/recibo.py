from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class ReciboCreate(BaseModel):
    id_pagamento: int = Field(gt=0)
    observacoes: str | None = Field(default=None, min_length=3, max_length=1000)

class ReciboUpdate(BaseModel):
    observacoes: str | None = Field(default=None, min_length=3, max_length=1000)

class ReciboResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_recibo: int
    id_pagamento: int
    numero_recibo: int
    observacoes: str | None
    data_criacao: datetime
    data_emissao: datetime