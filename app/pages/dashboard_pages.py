from fastapi import APIRouter, Depends, HTTPException, status, Cookie, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session
from app.api.dependencias import get_db

from app.core.jwt import verificar_token
from app.repositories.usuario_repository import UsuarioRepository


router = APIRouter(
    prefix='/dashboard',
    tags=['Dashboard']
    )

templates = Jinja2Templates(directory='app/templates')

@router.get('/')
def dashboard(request: Request, access_token: str | None = Cookie(default=None), db: Session = Depends(get_db)):

    if access_token is None:
        print("ERRO: O COOKIE NÃO CHEGOU AO DASHBOARD")
        return RedirectResponse(
            url='/login/',
            status_code=status.HTTP_303_SEE_OTHER
        )

    try:
        id_usuario = verificar_token(access_token)

    except ValueError:
        return RedirectResponse(
            url='/login/',
            status_code=status.HTTP_303_SEE_OTHER
        )

    repository = UsuarioRepository(db)

    usuario = repository.buscar_usuario_por_id(id_usuario)

    if usuario is None:
        return RedirectResponse(
            url='/login/',
            status_code=status.HTTP_303_SEE_OTHER
        )

    if not usuario.ativo:
        return RedirectResponse(
            url='/login/',
            status_code=status.HTTP_303_SEE_OTHER
        )
    

    return templates.TemplateResponse(
        request=request,
        name='pages/dashboard.html'
    )