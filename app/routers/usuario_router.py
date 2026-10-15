from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, status, Body


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

    try:
        return service.criar_usuario(dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro)
        )

@router.get('/buscar-id/{id_usuario}', response_model=UsuarioResponse)
def buscar_usuario_por_id(id_usuario: int, service: UsuarioService = Depends(get_usuario_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_usuario_por_id(id_usuario)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-email/{email}', response_model=UsuarioResponse)
def buscar_usuario_por_email(email: str, service: UsuarioService = Depends(get_usuario_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_usuario_por_email(email)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/listar', response_model=list[UsuarioResponse])
def listar_usuarios(service: UsuarioService = Depends(get_usuario_service), admin: Usuario = Depends(exigir_admin)):

    return service.listar_usuarios()

@router.patch('/atualizar-usuario/{id_usuario}', response_model=UsuarioResponse)
def atualizar_usuario(id_usuario: int, dados: UsuarioUpdate, service: UsuarioService = Depends(get_usuario_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.atualizar_usuario(id_usuario, dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.patch('/atualizar-senha/{id_usuario}', response_model=UsuarioResponse)
def atualizar_senha(id_usuario: int, senha: str = Body(embed=True, min_length=8, max_length=100), service: UsuarioService = Depends(get_usuario_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.atualizar_senha(id_usuario, senha)

    except ValueError as erro:
        mensagem = str(erro)

        if mensagem == "A senha deve conter entre 8 e 100 caracteres.":
            codigo = status.HTTP_400_BAD_REQUEST
        else:
            codigo = status.HTTP_404_NOT_FOUND

        raise HTTPException(
            status_code=codigo,
            detail=mensagem
        )

@router.patch('/atualizar-perfil/{id_usuario}/{perfil}', response_model=UsuarioResponse)
def atualizar_perfil(id_usuario: int, perfil: str, service: UsuarioService = Depends(get_usuario_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.atualizar_perfil(id_usuario, perfil)

    except ValueError as erro:
        mensagem = str(erro)

        if mensagem == 'Este perfil não existe.':
            codigo = status.HTTP_400_BAD_REQUEST
        else:
            codigo = status.HTTP_404_NOT_FOUND

        raise HTTPException(
            status_code=codigo,
            detail=mensagem
        )

@router.patch('/desativar/{id_usuario}', response_model=UsuarioResponse)
def desativar_usuario(id_usuario: int, service: UsuarioService = Depends(get_usuario_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.desativar_usuario(id_usuario)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.patch('/reativar/{id_usuario}', response_model=UsuarioResponse)
def reativar_usuario(id_usuario: int, service: UsuarioService = Depends(get_usuario_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.reativar_usuario(id_usuario)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )