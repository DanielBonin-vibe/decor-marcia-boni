from app.schemas.parcela import ParcelaCreate, ParcelaUpdate
from app.repositories.parcela_repository import ParcelaRepository
from app.repositories.contrato_repository import ContratoRepository
from app.repositories.pagamento_repository import PagamentoRepository
from datetime import date
from decimal import Decimal


class ParcelaService:
    def __init__(self, repository: ParcelaRepository, contrato_repository: ContratoRepository, pagamento_repository: PagamentoRepository):
        self.repository = repository
        self.contrato_repository = contrato_repository
        self.pagamento_repository = pagamento_repository

    def criar_parcela(self, dados: ParcelaCreate):
        if dados.valor <= 0:
            raise ValueError('O valor da parcela deve ser maior que zero.')

        contrato = self.contrato_repository.buscar_contrato_por_id(dados.id_contrato)

        if contrato is None:
            raise ValueError('Não foi possível localizar o contrato.')

        return self.repository.criar_parcela(dados)

    def buscar_parcela_por_id(self, id_parcela: int):
        parcela = self.repository.buscar_parcela_por_id(id_parcela)

        if parcela is None:
            raise ValueError ('Não foi possível localizar nenhuma parcela.')

        return parcela


    def buscar_parcelas_por_contrato(self, id_contrato: int):
        return self.repository.buscar_parcelas_por_contrato(id_contrato)


    def buscar_parcelas_por_status(self, status: str):
        return self.repository.buscar_parcelas_por_status(status)


    def buscar_parcelas_por_vencimento(self, data_vencimento: date):
        return self.repository.buscar_parcelas_por_vencimento(data_vencimento)

    def listar_parcelas(self):
        return self.repository.listar_parcelas()


    def atualizar_parcela(self, id_parcela: int, dados: ParcelaUpdate):
        parcela = self.repository.buscar_parcela_por_id(id_parcela)

        if parcela is None:
            raise ValueError ('Não foi possível localizar nenhuma parcela.')


        if dados.id_contrato is not None:
            contrato = self.contrato_repository.buscar_contrato_por_id(dados.id_contrato)

            if contrato is None:
                raise ValueError('Não foi possível localizar o contrato.')

        return self.repository.atualizar_parcela(id_parcela, dados)

    def atualizar_status_parcela(self, id_parcela: int):
        parcela = self.repository.buscar_parcela_por_id(id_parcela)

        if parcela is None:
            raise ValueError ('Não foi possível localizar nenhuma parcela.')


        if parcela.status == 'cancelada':
                raise ValueError('Não é possível atualizar uma parcela cancelada.')


        pagamentos = self.pagamento_repository.buscar_pagamentos_por_parcela(id_parcela)

        total_pago = sum((pagamento.valor for pagamento in pagamentos), Decimal('0.00'))


        if total_pago >= parcela.valor:
            status= 'paga'

        elif total_pago > 0:
            status = 'parcialmente_paga'

        elif parcela.data_vencimento < date.today():
            status = 'atrasada'

        else: 
            status = 'pendente'
        return self.repository.atualizar_status_parcela(id_parcela, status)