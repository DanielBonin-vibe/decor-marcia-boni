from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

class ItemPropostaCreate(BaseModel):
    id_proposta: int = Field(gt=0)
    nome: str = Field(min_length=3, max_length=100)
    descricao: str | None = Field(default=None, min_length=3, max_length=1000)
    quantidade: int = Field(gt=0)
    categoria: Literal['movel', 'decoracao', 'iluminacao', 'flores', 'servico', 'outros'] = 'decoracao'
    opcional: bool = False
    ordem: int = Field(gt=0)

class ItemPropostaUpdate(BaseModel):
    id_proposta: int | None = None
    nome: str | None = Field(default=None, min_length=3, max_length=100)
    descricao: str | None = Field(default=None, min_length=3, max_length=1000)
    quantidade: int | None = Field(default=None, gt=0)
    categoria: Literal['movel', 'decoracao', 'iluminacao', 'flores', 'servico', 'outros'] | None = None
    opcional: bool | None = None
    ordem: int | None = Field(default=None, gt=0)

class ItemPropostaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_item_proposta: int
    id_proposta: int
    nome: str
    descricao: str | None
    quantidade: int
    categoria: str 
    opcional: bool
    ordem: int