from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

class PagamentoCreate(BaseModel):
    id_parcela: int = Field(gt=0)
    valor: Decimal
    forma_pagamento: Literal['pix', 'dinheiro', 'cartao_credito', 'cartao_debito', 'transferencia', 'boleto', 'outros']
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