from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

class PropostaCreate(BaseModel):
    id_evento: int = Field(gt=0)
    versao: int = Field(gt=0)
    titulo: str = Field(min_length=3, max_length=100)
    observacoes:str | None = Field(default=None, min_length=3, max_length=1000)
    valor_decoracao: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    valor_moveis: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    valor_adicionais: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    valor_total: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    condicao_pagamento: str = Field(min_length=3, max_length=100)
    status: Literal['aceito', 'recusado', 'cancelado', 'pendente'] = 'pendente'

class PropostaUpdate(BaseModel):
    id_evento: int | None = Field(default=None, gt=0)
    versao: int | None = Field(default=None, gt=0)
    titulo: str | None = Field(default=None, min_length=3, max_length=100)
    observacoes:str | None = Field(default=None, min_length=3, max_length=1000)
    valor_decoracao: Decimal | None = Field(default=None, gt=0, max_digits=12, decimal_places=2)
    valor_moveis: Decimal | None = Field(default=None, gt=0, max_digits=12, decimal_places=2)
    valor_adicionais: Decimal | None = Field(default=None, gt=0, max_digits=12, decimal_places=2)
    valor_total: Decimal | None = Field(default=None, gt=0, max_digits=12, decimal_places=2)
    condicao_pagamento: str | None = Field(default=None, min_length=3, max_length=100)
    status: Literal['aceito', 'recusado', 'cancelado', 'pendente'] | None = None

class PropostaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_proposta: int
    id_evento: int
    versao: int
    titulo: str
    observacoes: str | None
    valor_decoracao: Decimal
    valor_moveis: Decimal
    valor_adicionais: Decimal
    valor_total: Decimal
    condicao_pagamento: str
    status: str
    data_criacao: datetime
    data_atualizacao: datetime