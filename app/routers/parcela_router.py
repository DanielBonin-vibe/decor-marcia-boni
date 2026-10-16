from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.api.dependencias import get_db, exigir_admin
from app.repositories.parcela_repository import ParcelaRepository
from app.repositories.contrato_repository import ContratoRepository
from app.repositories.pagamento_repository import PagamentoRepository

from app.services.parcela_service import ParcelaService
from app.schemas.parcela import ParcelaCreate, ParcelaUpdate, ParcelaResponse
from app.models.usuario import Usuario


router = APIRouter(
    prefix='/parcela',
    tags=['Parcela']
)


def get_parcela_service(db: Session = Depends(get_db)):
    repository = ParcelaRepository(db)
    contrato_repository = ContratoRepository(db)
    pagamento_repository = PagamentoRepository(db)

    service = ParcelaService(repository, contrato_repository, pagamento_repository)

    return service

@router.post('/', response_model=ParcelaResponse, status_code=status.HTTP_201_CREATED)
def criar_parcela(dados: ParcelaCreate, service: ParcelaService = Depends(get_parcela_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.criar_parcela(dados)

    except ValueError as erro:
        mensagem = str(erro)

        if mensagem == 'Não foi possível localizar o contrato.':
            codigo = status.HTTP_404_NOT_FOUND
        else:
            codigo = status.HTTP_400_BAD_REQUEST

        raise HTTPException(
            status_code=codigo,
            detail=mensagem
        )

@router.get('/buscar-id/{id_parcela}', response_model=ParcelaResponse)
def buscar_parcela_por_id(id_parcela: int, service: ParcelaService = Depends(get_parcela_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_parcela_por_id(id_parcela)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-contrato/{id_contrato}', response_model=list[ParcelaResponse])
def buscar_parcelas_por_contrato(id_contrato: int, service: ParcelaService = Depends(get_parcela_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_parcelas_por_contrato(id_contrato)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-status/{status}', response_model=list[ParcelaResponse])
def buscar_parcelas_por_status(status: str, service: ParcelaService = Depends(get_parcela_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_parcelas_por_status(status)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-vencimento/{data_vencimento}', response_model=list[ParcelaResponse])
def buscar_parcelas_por_vencimento(data_vencimento: date, service: ParcelaService = Depends(get_parcela_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_parcelas_por_vencimento(data_vencimento)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/listar', response_model=list[ParcelaResponse])
def listar_parcelas(service: ParcelaService = Depends(get_parcela_service), admin: Usuario = Depends(exigir_admin)):

        return service.listar_parcelas()

@router.patch('/atualizar/{id_parcela}', response_model=ParcelaResponse)
def atualizar_parcela(id_parcela: int, dados: ParcelaUpdate, service: ParcelaService = Depends(get_parcela_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.atualizar_parcela(id_parcela, dados)

    except ValueError as erro:
        mensagem = str(erro)

        if mensagem == 'Não foi possível localizar nenhuma parcela.':
            codigo = status.HTTP_404_NOT_FOUND
        else:
            codigo = status.HTTP_409_CONFLICT

        raise HTTPException(
            status_code=codigo,
            detail=mensagem
        )

@router.patch('/atualizar-status/{id_parcela}', response_model=ParcelaResponse)
def atualizar_status_parcela(id_parcela: int, service: ParcelaService = Depends(get_parcela_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.atualizar_status_parcela(id_parcela)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )