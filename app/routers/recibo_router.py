from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.api.dependencias import get_db, exigir_admin
from app.models.usuario import Usuario

from app.repositories.recibo_repository import ReciboRepository
from app.repositories.pagamento_repository import PagamentoRepository
from app.services.recibo_service import ReciboService
from app.schemas.recibo import ReciboCreate, ReciboUpdate, ReciboResponse

router = APIRouter(
    prefix='/recibo',
    tags=['Recibo']
)

def get_recibo_service(db: Session = Depends(get_db)):
    repository = ReciboRepository(db)
    pagamento_repository = PagamentoRepository(db)

    service = ReciboService(repository, pagamento_repository)

    return service

@router.post('/', response_model=ReciboResponse, status_code=status.HTTP_201_CREATED)
def criar_recibo(dados: ReciboCreate, service: ReciboService = Depends(get_recibo_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.criar_recibo(dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-id/{id_recibo}', response_model=ReciboResponse)
def buscar_recibo_por_id(id_recibo: int, service: ReciboService = Depends(get_recibo_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_recibo_por_id(id_recibo)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-pagamento/{id_pagamento}', response_model=ReciboResponse)
def buscar_recibo_por_pagamento(id_pagamento: int, service: ReciboService = Depends(get_recibo_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_recibo_por_pagamento(id_pagamento)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-numero/{numero_recibo}', response_model=ReciboResponse)
def buscar_recibo_por_numero(numero_recibo: int, service: ReciboService = Depends(get_recibo_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_recibo_por_numero(numero_recibo)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/listar', response_model=list[ReciboResponse])
def listar_recibos(service: ReciboService = Depends(get_recibo_service), admin: Usuario = Depends(exigir_admin)):
        
        return service.listar_recibos()