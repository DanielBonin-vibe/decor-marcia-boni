from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict

class PropostaCreate(BaseModel):
    id_evento: int
    versao: int
    titulo: str = Field(min_length=3, max_length=100)
    observacoes:str | None = Field(default=None, min_length=3, max_length=1000)
    valor_decoracao: Decimal
    valor_moveis: Decimal
    valor_adicionais: Decimal
    valor_total: Decimal
    condicao_pagamento: str = Field(min_length=3, max_length=100)
    status: str = Field(min_length=3, max_length=100)

class PropostaUpdate(BaseModel):
    id_evento: int | None = None
    versao: int | None = None
    titulo: str | None = Field(default=None, min_length=3, max_length=100)
    observacoes:str | None = Field(default=None, min_length=3, max_length=1000)
    valor_decoracao: Decimal | None = None
    valor_moveis: Decimal | None = None
    valor_adicionais: Decimal | None = None
    valor_total: Decimal | None = None
    condicao_pagamento: str | None = Field(default=None, min_length=3, max_length=100)
    status: str | None = Field(default=None, min_length=3, max_length=100)

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