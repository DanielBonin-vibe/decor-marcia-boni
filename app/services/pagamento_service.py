from app.schemas.pagamento import PagamentoCreate, PagamentoUpdate
from app.repositories.pagamento_repository import PagamentoRepository
from datetime import date


class PagamentoService:
    def __init__(self, repository: PagamentoRepository):
        self.repository = repository

    def criar_pagamento(self, dados: PagamentoCreate):
        if dados.valor <= 0:
            raise ValueError('O valor de pagamento deve ser maior que zero.')

        return self.repository.criar_pagamento(dados)

    def buscar_pagamento_por_id(self, id_pagamento: int):
        pagamento = self.repository.buscar_pagamento_por_id(id_pagamento)

        if pagamento is None:
            raise ValueError ('Não foi possível localizar nenhum pagamento.')

        return pagamento

    def buscar_pagamentos_por_parcela(self, id_parcela: int):
        pagamentos = self.repository.buscar_pagamentos_por_parcela(id_parcela)

        if not pagamentos:
            raise ValueError ('Não foi possível localizar nenhum pagamento.')

        return pagamentos

    def buscar_pagamentos_por_forma_pagamento(self, forma_pagamento: str):
        pagamentos = self.repository.buscar_pagamentos_por_forma_pagamento(forma_pagamento)

        if not pagamentos:
            raise ValueError ('Não foi possível localizar nenhum pagamento.')

        return pagamentos

    def buscar_pagamentos_por_data(self, data_pagamento: date):
        pagamentos = self.repository.buscar_pagamentos_por_data(data_pagamento)

        if not pagamentos:
            raise ValueError ('Não foi possível localizar nenhum pagamento.')

        return pagamentos

    def listar_pagamentos(self):
        return self.repository.listar_pagamentos()

    def atualizar_pagamento(self, id_pagamento: int, dados: PagamentoUpdate):
        pagamento = self.repository.buscar_pagamento_por_id(id_pagamento)

        if pagamento is None:
            raise ValueError('Não foi possível localizar nenhum pagamento.')

        return self.repository.atualizar_pagamento(id_pagamento, dados)