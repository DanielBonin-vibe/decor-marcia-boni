from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.api.dependencias import get_db, exigir_admin
from app.repositories.item_proposta_repository import ItemPropostaRepository
from app.repositories.proposta_repository import PropostaRepository

from app.services.item_proposta_service import ItemPropostaService
from app.schemas.item_proposta import ItemPropostaCreate, ItemPropostaUpdate, ItemPropostaResponse
from app.models.usuario import Usuario

router = APIRouter(
    prefix='/item_proposta',
    tags=['Item Proposta']
)

def get_item_proposta_service(db: Session = Depends(get_db)):
    repository = ItemPropostaRepository(db)
    proposta_repository = PropostaRepository(db)

    service = ItemPropostaService(repository, proposta_repository)

    return service

@router.post('/', response_model=ItemPropostaResponse, status_code=status.HTTP_201_CREATED)
def criar_item_proposta(dados: ItemPropostaCreate, service: ItemPropostaService = Depends(get_item_proposta_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.criar_item_proposta(dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro)
        )

@router.get('/buscar-proposta/{id_item_proposta}', response_model=list[ItemPropostaResponse])
def buscar_itens_por_proposta(id_proposta: int, service: ItemPropostaService = Depends(get_item_proposta_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_itens_por_proposta(id_proposta)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/buscar-categoria/{categoria}', response_model=list[ItemPropostaResponse])
def buscar_itens_por_categoria(categoria: str, service: ItemPropostaService = Depends(get_item_proposta_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.buscar_itens_por_categoria(categoria)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.get('/listar', response_model=list[ItemPropostaResponse])
def listar_itens(service: ItemPropostaService = Depends(get_item_proposta_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.listar_itens()

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.patch('/atualizar/{id_item_proposta}', response_model=ItemPropostaResponse)
def atualizar_item(id_item_proposta: int, dados: ItemPropostaUpdate, service: ItemPropostaService = Depends(get_item_proposta_service), admin: Usuario = Depends(exigir_admin)):

    try:
        return service.atualizar_item(id_item_proposta, dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.patch('/atualizar-ordem/{id_item_proposta}/{ordem}', response_model=ItemPropostaResponse)
def atualizar_ordem(id_item_proposta: int, ordem: int, service: ItemPropostaService = Depends(get_item_proposta_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.atualizar_ordem(id_item_proposta, ordem)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )

@router.patch('atualizar-opcional{id_item_proposta}/{opcional}', response_model=ItemPropostaResponse)
def atualizar_opcional(id_item_proposta: int, opcional: bool, service: ItemPropostaService = Depends(get_item_proposta_service), admin: Usuario = Depends(exigir_admin)):
    try:
        return service.atualizar_opcional(id_item_proposta, opcional)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )