from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.recibo import ReciboCreate, ReciboUpdate 
from app.models.recibo import Recibo

class ReciboRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar_recibo(self, dados: ReciboCreate):
        recibo = Recibo(**dados.model_dump())

        self.db.add(recibo)

        try:
            self.db.commit()

        except IntegrityError:
            self.db.rollback()
            raise

        self.db.refresh(recibo)
        return recibo

    def buscar_recibo_por_id(self, id_recibo: int):
        consulta = select(Recibo).where(Recibo.id_recibo == id_recibo)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def buscar_recibo_por_pagamento(self, id_pagamento: int):
        consulta = select(Recibo).where(Recibo.id_pagamento == id_pagamento)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def buscar_recibo_por_numero(self, numero_recibo: int):
        consulta = select(Recibo).where(Recibo.numero_recibo == numero_recibo)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def listar_recibos(self):
        consulta = select(Recibo).order_by(Recibo.numero_recibo)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()