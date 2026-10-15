from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.api.dependencias import get_db, exigir_admin
from app.repositories.pagamento_repository import PagamentoRepository
from app.repositories.parcela_repository import ParcelaRepository

from app.services.pagamento_service import PagamentoService
from app.schemas.pagamento import PagamentoCreate, PagamentoUpdate, PagamentoResponse
from app.models.usuario import Usuario

router = APIRouter(
    prefix='/pagamento',
    tags=['Pagamento']
)

def get_pagamento_service(db: Session = Depends(get_db)):
    repository = PagamentoRepository(db)
    parcela_repository = ParcelaRepository(db)

    service = PagamentoService(repository, parcela_repository)

    return service

@router.post('/', response_model=PagamentoResponse, status_code=status.HTTP_201_CREATED)
def criar_pagamento(dados: PagamentoCreate, service: PagamentoService = Depends(get_pagamento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.criar_pagamento(dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro)
        )

@router.get('/buscar-id/{id_pagamento}', response_model=PagamentoResponse)
def buscar_pagamento_por_id(id_pagamento: int, service: PagamentoService = Depends(get_pagamento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_pagamento_por_id(id_pagamento)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-parcela/{id_parcela}', response_model=list[PagamentoResponse])
def buscar_pagamentos_por_parcela(id_parcela: int, service: PagamentoService = Depends(get_pagamento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_pagamentos_por_parcela(id_parcela)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-forma-pagamento/{forma_pagamento}', response_model=list[PagamentoResponse])
def buscar_pagamentos_por_forma_pagamento(forma_pagamento: str, service: PagamentoService = Depends(get_pagamento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_pagamentos_por_forma_pagamento(forma_pagamento)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-data/{data_pagamento}', response_model=list[PagamentoResponse])
def buscar_pagamentos_por_data(data_pagamento: date, service: PagamentoService = Depends(get_pagamento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_pagamentos_por_data(data_pagamento)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/listar', response_model=list[PagamentoResponse])
def listar_pagamentos(service: PagamentoService = Depends(get_pagamento_service), admin: Usuario = Depends(exigir_admin)):

        return service.listar_pagamentos()

@router.patch('/atualizar/{id_pagamento}', response_model=PagamentoResponse)
def atualizar_pagamento(id_pagamento: int, dados: PagamentoUpdate, service: PagamentoService = Depends(get_pagamento_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.atualizar_pagamento(id_pagamento, dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )