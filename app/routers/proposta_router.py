from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.api.dependencias import get_db, exigir_admin
from app.models.usuario import Usuario

from app.repositories.proposta_repository import PropostaRepository
from app.repositories.evento_repository import EventoRepository
from app.services.proposta_service import PropostaService
from app.schemas.proposta import PropostaCreate, PropostaUpdate, PropostaResponse

router = APIRouter(
    prefix='/proposta',
    tags=['Proposta']
)


def get_proposta_service(db: Session = Depends(get_db)):
    repository = PropostaRepository(db)
    evento_repository = EventoRepository(db)

    service = PropostaService(repository, evento_repository)

    return service

@router.post('/', response_model=PropostaResponse, status_code=status.HTTP_201_CREATED)
def criar_proposta(dados: PropostaCreate, service: PropostaService = Depends(get_proposta_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.criar_proposta(dados)

    except ValueError as erro:
        mensagem = str(erro)

        if mensagem == 'O valor da decoração informado deve ser maior que 0.':
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(erro)
                )

        if mensagem == 'O valor dos móveis informado deve ser maior que 0.':
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(erro)
                )

        if mensagem == 'O valor dos adicionais informado deve ser maior que 0.':
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(erro)
                )

        if mensagem == 'O valor total informado deve ser maior que 0.':
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(erro)
                )
        
@router.get('/buscar-id/{id_proposta}', response_model=PropostaResponse)
def buscar_proposta_por_id(id_proposta: int, service: PropostaService = Depends(get_proposta_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_proposta_por_id(id_proposta)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-evento/{id_evento}', response_model=list[PropostaResponse])
def buscar_propostas_por_evento(id_evento: int, service: PropostaService = Depends(get_proposta_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_propostas_por_evento(id_evento)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-status/{status}', response_model=list[PropostaResponse])
def buscar_propostas_por_status(status: str, service: PropostaService = Depends(get_proposta_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_propostas_por_status(status)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-evento-versao/{id_evento}/{versao}', response_model=list[PropostaResponse])
def buscar_proposta_por_evento_e_versao(id_evento: int, versao: int, service: PropostaService = Depends(get_proposta_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_proposta_por_evento_e_versao(id_evento, versao)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/listar', response_model=list[PropostaResponse])
def listar_propostas(service: PropostaService = Depends(get_proposta_service), admin: Usuario = Depends(exigir_admin)):

        return service.listar_propostas()

@router.patch('/atualizar/{id_proposta}', response_model=PropostaResponse)
def atualizar_proposta(id_proposta: int, dados: PropostaUpdate, service: PropostaService = Depends(get_proposta_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.atualizar_proposta(id_proposta, dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.patch('/atualizar-status/{id_proposta}/{status}', response_model=PropostaResponse)
def atualizar_status_proposta(id_proposta: int, status: str, service: PropostaService = Depends(get_proposta_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.atualizar_status_proposta(id_proposta, status)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )