from datetime import datetime, date
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict

class ParcelaCreate(BaseModel):
    id_contrato: int
    numero_parcela: int
    valor: Decimal
    data_vencimento: date
    status: str = Field(min_length=3, max_length=100)

class ParcelaUpdate(BaseModel):
    id_contrato: int | None = None
    numero_parcela: int | None = None
    valor: Decimal | None = None
    data_vencimento: date | None = None
    status: str | None = Field(default=None, min_length=3, max_length=100)

class ParcelaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_parcela: int
    id_contrato: int
    numero_parcela: int
    valor: Decimal
    data_vencimento: date
    status: str
    data_criacao: datetime
    data_atualizacao: datetime