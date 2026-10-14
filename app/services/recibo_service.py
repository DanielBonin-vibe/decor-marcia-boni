from app.schemas.recibo import ReciboCreate
from app.repositories.recibo_repository import ReciboRepository
from app.repositories.pagamento_repository import PagamentoRepository

class ReciboService:
    def __init__(self, repository: ReciboRepository, pagamento_repository: PagamentoRepository):
        self.repository = repository
        self.pagamento_repository = pagamento_repository

    def criar_recibo(self, dados: ReciboCreate):
        recibo = self.repository.buscar_recibo_por_pagamento(dados.id_pagamento)

        if recibo is not None:
            raise ValueError('Este pagamento já possui um recibo')

        pagamento = self.pagamento_repository.buscar_pagamento_por_id(dados.id_pagamento)

        if pagamento is None:
            raise ValueError('Não foi possível localizar o pagamento')

        return self.repository.criar_recibo(dados)

    def buscar_recibo_por_id(self, id_recibo: int):
        recibo = self.repository.buscar_recibo_por_id(id_recibo)

        if recibo is None:
            raise ValueError('Não foi possível localizar o recibo.')

        return recibo

    def buscar_recibo_por_pagamento(self, id_pagamento: int):
        recibo = self.repository.buscar_recibo_por_pagamento(id_pagamento)

        if recibo is None:
            raise ValueError('Não foi possível localizar o recibo.')

        return recibo
    
    def buscar_recibo_por_numero(self, numero_recibo: int):
        recibo = self.repository.buscar_recibo_por_numero(numero_recibo)

        if recibo is None:
            raise ValueError('Não foi possível localizar o recibo.')

        return recibo

    def listar_recibos(self):
        return self.repository.listar_recibos()