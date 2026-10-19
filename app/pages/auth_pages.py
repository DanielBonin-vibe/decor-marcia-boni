from fastapi import APIRouter, Request, Form, Depends,HTTPException, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.api.dependencias import get_db
from app.repositories.usuario_repository import UsuarioRepository

from app.core.security import verificar_senha
from app.core.jwt import criar_token_acesso

from fastapi.responses import RedirectResponse

router = APIRouter(
    prefix='/login',
    tags=['Páginas - Autenticação']
    )

templates = Jinja2Templates(directory='app/templates')

@router.get('/')
def pagina_login(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='pages/login.html'
    )

@router.post('/')
def processar_login(db: Session = Depends(get_db), username: str = Form(...), password: str = Form(...)):

    repository = UsuarioRepository(db)

    usuario = repository.buscar_usuario_por_email(username)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Email ou senha inválidos'
        )

    if not verificar_senha(password, usuario.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Email ou senha inválidos'
            )

    if not usuario.ativo:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Email ou senha inválidos'
        )

    token = criar_token_acesso(usuario.id_usuario)

    response = RedirectResponse(
        url="/dashboard",
        status_code=status.HTTP_303_SEE_OTHER
        )

    response.set_cookie(
        key="acess_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=1800,
        path='/'
    )

    return response