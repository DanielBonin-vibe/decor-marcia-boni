from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.api.dependencias import get_db, exigir_admin
from app.repositories.evento_repository import EventoRepository
from app.repositories.cliente_repository import ClienteRepository

from app.services.evento_service import EventoService
from app.schemas.evento import EventoCreate, EventoResponse, EventoUpdate, EventoDriveUpdate
from app.models.usuario import Usuario
from datetime import date

router = APIRouter(
    prefix='/evento',
    tags=['Evento']
)

def get_evento_service(db: Session = Depends(get_db)):
    repository = EventoRepository(db)
    cliente_repository = ClienteRepository(db)

    service = EventoService(repository, cliente_repository)

    return service

@router.post('/', response_model=EventoResponse, status_code=status.HTTP_201_CREATED)
def criar_evento(dados: EventoCreate, service: EventoService = Depends(get_evento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.criar_evento(dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro)
        )

@router.get('/buscar-id/{id_evento}')
def buscar_evento_por_id(id_evento: int, service: EventoService = Depends(get_evento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_evento_por_id(id_evento)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-cliente/{id_cliente}', response_model=list[EventoResponse])
def buscar_eventos_por_cliente(id_cliente: int, service: EventoService = Depends(get_evento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_eventos_por_cliente(id_cliente)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-status/{status}', response_model=list[EventoResponse])
def buscar_eventos_por_status(status: str, service: EventoService = Depends(get_evento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_eventos_por_status(status)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-data/{data_evento}', response_model=list[EventoResponse])
def buscar_eventos_por_data(data_evento: date, service: EventoService = Depends(get_evento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_eventos_por_data(data_evento)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/', response_model=list[EventoResponse])
def listar_eventos(service: EventoService = Depends(get_evento_service), admin: Usuario = Depends(exigir_admin)):

        return service.listar_eventos()

@router.patch('/atualizar/{id_evento}', response_model=EventoResponse)
def atualizar_evento(id_evento: int, dados: EventoUpdate, service: EventoService = Depends(get_evento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.atualizar_evento(id_evento, dados)

    except ValueError as erro:
        mensagem = str(erro)

        if mensagem == 'Não foi possível localizar nenhum evento.':
            codigo = status.HTTP_404_NOT_FOUND
        else:
            codigo = status.HTTP_409_CONFLICT

        raise HTTPException(
            status_code=codigo,
            detail=mensagem
        )

@router.patch('/atualizar-status/{id_evento}/{status}', response_model=EventoResponse)
def atualizar_status_evento(id_evento: int, status: str, service: EventoService = Depends(get_evento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.atualizar_status_evento(id_evento, status)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.patch('/atualizar-drive-folder-id/{id_evento}', response_model=EventoResponse)
def atualizar_drive_folder_id(id_evento: int, dados: EventoDriveUpdate, service: EventoService = Depends(get_evento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.atualizar_drive_folder_id(id_evento, dados.drive_folder_id)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )