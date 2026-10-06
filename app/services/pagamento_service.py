from app.schemas.pagamento import PagamentoCreate, PagamentoUpdate
from app.repositories.pagamento_repository import PagamentoRepository

class PagamentoService:
    def __init__(self, repository: PagamentoRepository):
        self.repository = repository

    def criar_pagamento(self, )