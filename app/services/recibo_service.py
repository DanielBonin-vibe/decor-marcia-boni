from app.schemas.recibo import ReciboCreate
from app.repositories.recibo_repository import ReciboRepository

class ReciboService:
    def __init__(self, repository: ReciboRepository):
        self.repository = repository

    def criar_recibo(self, dados: ReciboCreate):
        recibos = self.repository.listar_recibos()

        if recibos:
            numero_recibo = max(recibo.numero_recibo for recibo in recibos) + 1

        else:
            numero_recibo + 1

        return self.repository.criar_recibo(dados, numero_recibo)

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