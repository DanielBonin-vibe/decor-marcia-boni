from pydantic import BaseModel, Field, ConfigDict

class ItemPropostaCreate(BaseModel):
    id_proposta: int
    nome: str = Field(min_length=3, max_length=100)
    descricao: str | None = Field(default=None, min_length=3, max_length=1000)
    quantidade: int
    categoria: str = Field(min_length=3, max_length=100)
    opcional: bool = False
    ordem: int

class ItemPropostaUpdate(BaseModel):
    id_proposta: int | None = None
    nome: str | None = Field(default=None, min_length=3, max_length=100)
    descricao: str | None = Field(default=None, min_length=3, max_length=1000)
    quantidade: int | None = None
    categoria: str | None = Field(default=None, min_length=3, max_length=100)
    opcional: bool | None = None
    ordem: int | None = None

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