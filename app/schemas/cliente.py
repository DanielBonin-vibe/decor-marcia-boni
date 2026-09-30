from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, ConfigDict

class ClienteCreate(BaseModel):
    nome: str = Field(min_length=3, max_length=150)
    nacionalidade: str | None = Field(default=None, min_length=3, max_length=150)
    estado_civil: str | None = Field(default=None, min_length=3, max_length=150)
    profissao: str | None = Field(default=None, min_length=3, max_length=150)
    cpf: str = Field(min_length=11, max_length=11)
    telefone: str = Field(min_length=11, max_length=11)
    email: EmailStr = Field(min_length=3, max_length=150)
    endereco: str = Field(min_length=3, max_length=150)
    cidade: str = Field(min_length=3, max_length=150)
    estado: str = Field(min_length=3, max_length=150)
    cep: str = Field(min_length=8, max_length=8)

class ClienteUpdate(BaseModel):
    nome: str | None = Field(default=None, min_length=3, max_length=150)
    nacionalidade: str | None = Field(default=None, min_length=3, max_length=150)
    estado_civil: str | None = Field(default=None, min_length=3, max_length=150)
    profissao: str | None = Field(default=None, min_length=3, max_length=150)
    cpf: str | None = Field(default=None, min_length=11, max_length=11)
    telefone: str | None = Field(default=None, min_length=11, max_length=11)
    email: EmailStr | None = Field(default=None, min_length=3, max_length=150)
    endereco: str | None = Field(default=None, min_length=3, max_length=150)
    cidade: str | None = Field(default=None, min_length=3, max_length=150)
    estado: str | None = Field(default=None, min_length=3, max_length=150)
    cep: str | None = Field(default=None, min_length=8, max_length=8)
    ativo: bool | None = None

class ClienteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nome: str
    nacionalidade: str | None
    estado_civil: str | None
    profissao: str | None
    cpf: str
    telefone: str
    email: EmailStr
    endereco: str
    cidade: str
    estado: str
    cep: str
    ativo: bool
    data_criacao: datetime
    data_atualizacao: datetime