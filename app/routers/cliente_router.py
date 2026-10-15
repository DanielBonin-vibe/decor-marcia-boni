from fastapi import HTTPException, status, APIRouter, Depends

from sqlalchemy.orm import Session

from app.api.dependencias import get_db, exigir_admin

from app.repositories.cliente_repository import ClienteRepository
from app.services.cliente_service import ClienteService
from app.schemas.cliente import ClienteCreate, ClienteUpdate, ClienteResponse
from app.models.usuario import Usuario



router = APIRouter(
    prefix='/clientes',
    tags=['clientes']
)

def get_cliente_service(db: Session = Depends(get_db)):
    repository = ClienteRepository(db)

    service = ClienteService(repository)

    return service

@router.post('/', response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def criar_cliente(dados: ClienteCreate, service: ClienteService = Depends(get_cliente_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.criar_cliente(dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro)
        )

@router.get('/buscar-id/{id_cliente}', response_model=ClienteResponse)
def buscar_cliente_por_id(id_cliente: int, service: ClienteService = Depends(get_cliente_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_cliente_por_id(id_cliente)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-cpf/{cpf}', response_model=ClienteResponse)
def buscar_cliente_por_cpf(cpf: str, service: ClienteService = Depends(get_cliente_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_cliente_por_cpf(cpf)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-email/{email}', response_model=ClienteResponse)
def buscar_cliente_por_email(email: str, service: ClienteService = Depends(get_cliente_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_cliente_por_email(email)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-telefone/{telefone}', response_model=ClienteResponse)
def buscar_cliente_por_telefone(telefone: str, service: ClienteService = Depends(get_cliente_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_cliente_por_telefone(telefone)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/listar', response_model=list[ClienteResponse])
def listar_clientes(service: ClienteService = Depends(get_cliente_service), admin: Usuario = Depends(exigir_admin)):

    return service.listar_clientes()

@router.patch('/atualizar/{cpf}', response_model=ClienteResponse)
def atualizar_cliente(cpf: str, dados: ClienteUpdate, service: ClienteService = Depends(get_cliente_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.atualizar_cliente(cpf, dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.patch('/desativar/{cpf}', response_model=ClienteResponse)
def desativar_cliente(cpf: str, service: ClienteService = Depends(get_cliente_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.desativar_cliente(cpf)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.patch('/reativar/{cpf}', response_model=ClienteResponse)
def reativar_cliente(cpf: str, service: ClienteService = Depends(get_cliente_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.reativar_cliente(cpf)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )