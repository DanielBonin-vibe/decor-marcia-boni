from app.core.database import SessionLocal
from sqlalchemy.orm import Session
from typing import Generator

from fastapi import Depends, HTTPException, status
from app.core.jwt import verificar_token
from app.repositories.usuario_repository import UsuarioRepository
from fastapi.security import OAuth2PasswordBearer  # Configura a autenticação por Bearer

from app.models.usuario import Usuario

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")   # indica ao Swagger onde realziar o login ; oauth2_scheme -> Dependência que extrai o token Bearer do cabeçalho das requisições

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_usuario_atual(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        id_usuario = verificar_token(token)

    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token inválido ou expirado.',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    repository = UsuarioRepository(db)

    usuario = repository.buscar_usuario_por_id(id_usuario)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Credenciais inválidas.',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    if usuario.ativo == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Credenciais inválidas.',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    return usuario


def exigir_admin(usuario: Usuario = Depends(get_usuario_atual)):
    if usuario.perfil != 'admin':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Acesso permitido apenas para administradores.'
        )

    return usuario