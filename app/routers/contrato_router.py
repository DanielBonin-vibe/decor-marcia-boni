from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from datetime import datetime

from app.repositories.contrato_repository import ContratoRepository
from app.repositories.proposta_repository import PropostaRepository
from app.services.contrato_service import ContratoService

from app.models.usuario import Usuario
from app.schemas.contrato import ContratoResponse, ContratoUpdate, ContratoCreate
from app.api.dependencias import get_db, exigir_admin


router = APIRouter(
    prefix='/contrato',
    tags=['Contrato']
)


def get_contrato_service(db: Session = Depends(get_db)):
    repository = ContratoRepository(db)
    proposta_repository = PropostaRepository(db)

    service = ContratoService(repository, proposta_repository)

    return service

@router.post('/', response_model=ContratoResponse, status_code=status.HTTP_201_CREATED)
def criar_contrato(dados: ContratoCreate, service: ContratoService = Depends(get_contrato_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.criar_contrato(dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro)
        )

@router.get('/buscar-id/{id_contrato}', response_model=ContratoResponse)
def buscar_contrato_por_id(id_contrato: int, service: ContratoService = Depends(get_contrato_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_contrato_por_id(id_contrato)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-numero/{numero}', response_model=ContratoResponse)
def buscar_contrato_por_numero(numero: str, service: ContratoService = Depends(get_contrato_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_contrato_por_numero(numero)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-evento/{id_evento}', response_model=list[ContratoResponse])
def buscar_contratos_por_evento(id_evento: int, service: ContratoService = Depends(get_contrato_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_contratos_por_evento(id_evento)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/contrato-proposta/{id_proposta}', response_model=list[ContratoResponse])
def buscar_contratos_por_proposta(id_proposta: int, service: ContratoService = Depends(get_contrato_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.buscar_contratos_por_proposta(id_proposta)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/listar', response_model=list[ContratoResponse])
def listar_contratos(service: ContratoService = Depends(get_contrato_service), admin: Usuario = Depends(exigir_admin)):

        return service.listar_contratos()

@router.patch('/atualizar/{id_contrato}', response_model=ContratoResponse)
def atualizar_contrato(id_contrato: int, dados: ContratoUpdate, service: ContratoService = Depends(get_contrato_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.atualizar_contrato(id_contrato, dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.patch('/atualizar-status/{id_contrato}/{status}', response_model=ContratoResponse)
def atualizar_status_contrato(id_contrato: int, status: str, service: ContratoService = Depends(get_contrato_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.atualizar_status_contrato(id_contrato, status)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
        )

@router.patch('/assinatura/{id_contrato}', response_model=ContratoResponse)
def registrar_assinatura(id_contrato: int, data_assinatura: datetime = Body(embed=True), service: ContratoService = Depends(get_contrato_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.registrar_assinatura(id_contrato, data_assinatura)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro)
        )