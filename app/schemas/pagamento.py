from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict

class PagamentoCreate(BaseModel):
    id_parcela: int
    valor: Decimal
    forma_pagamento: str = Field(min_length=3, max_length=50)
    observacoes: str | None = Field(default=None, min_length=3, max_length=1000)

class PagamentoUpdate(BaseModel):
    id_parcela: int | None = None
    valor: Decimal | None = None
    forma_pagamento: str | None = Field(default=None, min_length=3, max_length=100)
    observacoes: str | None = Field(default=None, min_length=3, max_length=1000)

class PagamentoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_pagamento: int
    id_parcela: int
    valor: Decimal
    data_pagamento: datetime
    forma_pagamento: str
    observacoes: str | None
    data_criacao: datetime