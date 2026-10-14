from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, status
from app.api.dependencias import get_usuario_atual, get_db, exigir_admin

from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioResponse, UsuarioCreate, UsuarioUpdate

from app.repositories.usuario_repository import UsuarioRepository
from app.services.usuario_service import UsuarioService


router = APIRouter(
    prefix='/usuarios',
    tags=['usuários']
)

def get_usuario_service(db: Session = Depends(get_db)):
    repository = UsuarioRepository(db)

    service = UsuarioService(repository)

    return service




@router.get('/me', response_model=UsuarioResponse)
def obter_meus_dados(usuario: Usuario = Depends(get_usuario_atual)):
    return usuario


@router.post('/', response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def criar_usuario(dados: UsuarioCreate, service: UsuarioService = Depends(get_usuario_service), admin: Usuario = Depends(exigir_admin)):

    return service.criar_usuario(dados)

@router.get('/buscar-id/{id_usuario}', response_model=UsuarioResponse)
def buscar_usuario_por_id(id_usuario: int, service: UsuarioService = Depends(get_usuario_service), admin: Usuario = Depends(exigir_admin)):

    return service.buscar_usuario_por_id(id_usuario)

@router.get('/buscar-email/{email}', response_model=UsuarioResponse)
def buscar_usuario_por_email(email: str, service: UsuarioService = Depends(get_usuario_service), admin: Usuario = Depends(exigir_admin)):

    return service.buscar_usuario_por_email(email)

@router.get('/listar')
def listar_usuarios(service: UsuarioService = Depends(get_usuario_service), admin: Usuario = Depends(exigir_admin)):

    return service.listar_usuarios()

@router.patch('/atualizar-usuario/{id_usuario}', response_model=UsuarioResponse)
def atualizar_usuario(id_usuario: int):