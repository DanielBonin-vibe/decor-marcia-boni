from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.api.dependencias import get_db, exigir_admin
from app.repositories.documento_repository import DocumentoRepository
from app.repositories.evento_repository import EventoRepository
from app.repositories.proposta_repository import PropostaRepository
from app.services.documento_service import DocumentoService
from app.schemas.documento import DocumentoCreate, DocumentoResponse, DocumentoUpdate, DocumentoDriveUpdate
from app.models.usuario import Usuario

router = APIRouter(
    prefix='/documento',
    tags=['Documento']
)


def get_documento_service(db: Session = Depends(get_db)):
    repository = DocumentoRepository(db)
    evento_repository = EventoRepository(db)
    proposta_repository = PropostaRepository(db)

    service = DocumentoService(repository, evento_repository, proposta_repository)

    return service


@router.post('/', response_model=DocumentoResponse, status_code=status.HTTP_201_CREATED)
def criar_documento(dados: DocumentoCreate, service: DocumentoService = Depends(get_documento_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.criar_documento(dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro)
        )

@router.get('buscar-id/{id_documento}', response_model=DocumentoResponse)
def buscar_documento_por_id(id_documento: int, service: DocumentoService = Depends(get_documento_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_documento_por_id(id_documento)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-evento/{id_evento}', response_model=list[DocumentoResponse])
def buscar_documentos_por_evento(id_evento: int, service: DocumentoService = Depends(get_documento_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_documentos_por_evento(id_evento)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-tipo/{tipo}', response_model=list[DocumentoResponse])
def buscar_documentos_por_tipo(tipo: str, service: DocumentoService = Depends(get_documento_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_documentos_por_tipo(tipo)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-evento-tipo/{id_evento}/{tipo}', response_model=list[DocumentoResponse])
def documentos_por_evento_e_tipo(id_evento: int, tipo: str, service: DocumentoService = Depends(get_documento_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.documentos_por_evento_e_tipo(id_evento, tipo)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/listar', response_model=list[DocumentoResponse])
def listar_documentos(service: DocumentoService = Depends(get_documento_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.listar_documentos()

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.patch('/atualizar/{id_documento}', response_model=DocumentoResponse)
def atualizar_documento(id_documento: int, dados: DocumentoUpdate, service: DocumentoService = Depends(get_documento_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.atualizar_documento(id_documento, dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.patch('/atualizar-drive/{id_documento}', response_model=DocumentoResponse)
def atualizar_dados_drive(id_documento: int, dados: DocumentoDriveUpdate, service: DocumentoService = Depends(get_documento_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.atualizar_dados_drive(id_documento, dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )