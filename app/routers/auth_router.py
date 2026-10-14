from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.dependencias import get_db
from app.repositories.usuario_repository import UsuarioRepository
from app.core.security import verificar_senha
from app.core.jwt import criar_token_acesso

from app.core.security import verificar_senha


router = APIRouter(
    prefix='/auth',
    tags=['Autenticação']
)

@router.post("/login")
def login(dados: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    email = dados.username
    senha = dados.password
    repository = UsuarioRepository(db)


    usuario = repository.buscar_usuario_por_email(email)

    if usuario is None:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='E-mail ou senha inválidos.',
        headers={'WWW-Authenticate': 'Bearer'}

        )


    senha_valida = verificar_senha(senha, usuario.senha_hash)

    if not senha_valida:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='E-mail ou senha inválidos.',
            headers={"WWW-Authenticate": "Bearer"}
        )


    if not usuario.ativo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Este usuário está desativado.',
            headers={"WWW-Authenticate": "Bearer"}
        )


    token = criar_token_acesso(usuario.id_usuario)

    return {
        'access_token': token,
        'token_type': 'bearer'
    }