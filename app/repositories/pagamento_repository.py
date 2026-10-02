from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import date
from app.schemas.pagamento import PagamentoCreate, PagamentoUpdate
from app.models import Pagamento

class PagamentoRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar_pagamento(self, dados: PagamentoCreate):
        pagamento = Pagamento(**dados.model_dump())

        self.db.add(pagamento)
        self.db.commit()
        self.db.refresh(pagamento)

        return pagamento

    def buscar_pagamento_por_id(self, id_pagamento: int):
        consulta = select(Pagamento).where(Pagamento.id_pagamento == id_pagamento)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def buscar_pagamentos_por_parcela(self, id_parcela: int):
        consulta = select(Pagamento).where(Pagamento.id_parcela == id_parcela)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def buscar_pagamentos_por_forma_pagamento(self, forma_pagamento: str):
        consulta = select(Pagamento).where(Pagamento.forma_pagamento == forma_pagamento)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def buscar_pagamentos_por_data(self, data_pagamento: date):
        consulta = select(Pagamento).where(Pagamento.data_pagamento == data_pagamento)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def listar_pagamentos(self):
        consulta = select(Pagamento)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def atualizar_pagamento(self, id_pagamento: int, dados: PagamentoUpdate):
        pagamento = self.buscar_pagamento_por_id(id_pagamento)

        if pagamento is None:
            return None

        atualizacao_pagamento = dados.model_dump(exclude_unset=True) 

        for campo, valor in atualizacao_pagamento.items():
            setattr(pagamento, campo, valor)

        self.db.commit()
        self.db.refresh(pagamento)

        return pagamento