from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ReciboCreate(BaseModel):
    id_pagamento: int

class ReciboUpdate(BaseModel):
    id_pagamento: int | None = None

class ReciboResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_recibo: int
    id_pagamento: int
    numero_recibo: int
    data_emissao: datetime