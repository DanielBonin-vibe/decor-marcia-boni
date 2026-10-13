from datetime import datetime, date
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

class ParcelaCreate(BaseModel):
    id_contrato: int = Field(gt=0)
    numero_parcela: int = Field(gt=0)
    valor: Decimal
    data_vencimento: date

class ParcelaUpdate(BaseModel):
    id_contrato: int | None = None
    numero_parcela: int | None = None
    valor: Decimal | None = None
    data_vencimento: date | None = None

class ParcelaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_parcela: int
    id_contrato: int
    numero_parcela: int
    valor: Decimal
    data_vencimento: date
    status: Literal['paga', 'cancelada', 'atrasada', 'pendente', 'parcialmente_paga']
    data_criacao: datetime
    data_atualizacao: datetime