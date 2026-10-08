from datetime import datetime 
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

StatusContrato = Literal['rascunho', 'pendente_assinatura', 'assinado', 'cancelado']

class ContratoCreate(BaseModel):
    id_proposta: int = Field(gt=0)
    numero: str = Field(min_length=1, max_length=20)
    valor_total: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    status_contrato: StatusContrato = 'rascunho'

class ContratoUpdate(BaseModel):
    numero: str | None = Field(default=None, min_length=1, max_length=20)
    valor_total: Decimal | None = Field(default=None, gt=0, max_digits=12, decimal_places=2)
    status_contrato: StatusContrato | None = None
    
class ContratoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_contrato: int = Field(gt=0)
    id_proposta: int
    numero: str
    valor_total: Decimal
    status_contrato: StatusContrato
    data_criacao: datetime
    data_atualizacao: datetime
    data_assinatura: datetime | None