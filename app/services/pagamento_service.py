from app.schemas.pagamento import PagamentoCreate, PagamentoUpdate
from app.repositories.pagamento_repository import PagamentoRepository
from app.repositories.parcela_repository import ParcelaRepository
from datetime import date
from decimal import Decimal


class PagamentoService:
    def __init__(self, repository: PagamentoRepository, parcela_repository: ParcelaRepository):
        self.repository = repository
        self.parcela_repository = parcela_repository

    def criar_pagamento(self, dados: PagamentoCreate):
        if dados.valor <= 0:
            raise ValueError('O valor de pagamento deve ser maior que zero.')


        parcela = self.parcela_repository.buscar_parcela_por_id(dados.id_parcela)

        if parcela is None:
            raise ValueError('Não foi possível localizar a parcela.')
        

        pagamentos = self.repository.buscar_pagamentos_por_parcela(dados.id_parcela)

        total_pago = sum(
            (pagamento.valor for pagamento in pagamentos),
            Decimal('0.00')
        )

        saldo_restante = parcela.valor - total_pago

        if dados.valor > saldo_restante:
            raise ValueError('O pagamento ultrapassa o saldo restante da parcela.')

        return self.repository.criar_pagamento(dados)

    def buscar_pagamento_por_id(self, id_pagamento: int):
        pagamento = self.repository.buscar_pagamento_por_id(id_pagamento)

        if pagamento is None:
            raise ValueError ('Não foi possível localizar nenhum pagamento.')

        return pagamento

    def buscar_pagamentos_por_parcela(self, id_parcela: int):
        pagamentos = self.repository.buscar_pagamentos_por_parcela(id_parcela)

        if not pagamentos:
            return []

        return pagamentos

    def buscar_pagamentos_por_forma_pagamento(self, forma_pagamento: str):
        pagamentos = self.repository.buscar_pagamentos_por_forma_pagamento(forma_pagamento)

        if not pagamentos:
            return []
        return pagamentos

    def buscar_pagamentos_por_data(self, data_pagamento: date):
        pagamentos = self.repository.buscar_pagamentos_por_data(data_pagamento)

        if not pagamentos:
            return []

        return pagamentos

    def listar_pagamentos(self):
        return self.repository.listar_pagamentos()

    def atualizar_pagamento(self, id_pagamento: int, dados: PagamentoUpdate):
        pagamento = self.repository.buscar_pagamento_por_id(id_pagamento)

        if pagamento is None:
            raise ValueError('Não foi possível localizar nenhum pagamento.')


        id_parcela = pagamento.id_parcela
        valor = pagamento.valor

        if dados.id_parcela is not None:
            id_parcela = dados.id_parcela

        if dados.valor is not None:
            valor = dados.valor

        parcela = self.parcela_repository.buscar_parcela_por_id(id_parcela)

        if parcela is None:
            raise ValueError('Não foi possível localizar a parcela.')

        pagamentos = self.repository.buscar_pagamentos_por_parcela(id_parcela)

        total_pago = sum(
            (
                item.valor
                for item in pagamentos
                if item.id_pagamento != id_pagamento
            ),
            Decimal('0.00')
        )

        if total_pago + valor > parcela.valor:
            raise ValueError('O pagamento ultrapassa o valor da parcela.')

        return self.repository.atualizar_pagamento(id_pagamento, dados)