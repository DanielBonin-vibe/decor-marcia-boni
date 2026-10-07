from datetime import datetime

from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UsuarioCreate(BaseModel):
    nome: str = Field(min_length=3, max_length=100)
    email: EmailStr
    senha: str = Field(min_length=8, max_length=100)
    perfil: str = Field(min_length=3,max_length=100)

class UsuarioUpdate(BaseModel):
    nome: str | None = Field(default=None,min_length=3, max_length=100)
    email: EmailStr | None = None
    senha: str | None = Field(default=None, min_length=8, max_length=100)
    perfil: str | None = Field(default=None, min_length=3, max_length=100)
    ativo: bool | None = None

class UsuarioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_usuario: int
    nome: str
    email: EmailStr
    perfil: str
    ativo: bool
    data_criacao: datetime
    data_atualizacao: datetime