from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from datetime import date

from app.schemas.parcela import ParcelaCreate, ParcelaUpdate 
from app.models.parcela import Parcela

class ParcelaRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar_parcela(self, dados: ParcelaCreate):
        parcela = Parcela(**dados.model_dump())

        self.db.add(parcela)

        try:
            self.db.commit()

        except IntegrityError:
            self.db.rollback()
            raise

        self.db.refresh(parcela)
        return parcela

    def buscar_parcela_por_id(self, id_parcela: int):
        consulta = select(Parcela).where(Parcela.id_parcela == id_parcela)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def buscar_parcelas_por_contrato(self, id_contrato: int):
        consulta = select(Parcela).where(Parcela.id_contrato == id_contrato).order_by(Parcela.numero_parcela)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()
    
    def buscar_parcelas_por_status(self, status: str):
        consulta = select(Parcela).where(Parcela.status == status).order_by(Parcela.numero_parcela)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def buscar_parcelas_por_vencimento(self, data_vencimento: date):
        consulta = select(Parcela).where(Parcela.data_vencimento == data_vencimento).order_by(Parcela.numero_parcela)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def listar_parcelas(self):
        consulta = select(Parcela)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def atualizar_parcela(self, id_parcela: int, dados: ParcelaUpdate):
        parcela = self.buscar_parcela_por_id(id_parcela)

        if parcela is None:
            return None

        atualizacao_parcela = dados.model_dump(exclude_unset=True)

        for campo, valor in atualizacao_parcela.items():
            setattr(parcela, campo, valor)

        try:
            self.db.commit()

        except IntegrityError:
            self.db.rollback()
            raise
        
        self.db.refresh(parcela)
        return parcela

    def atualizar_status_parcela(self, id_parcela: int, status: str):
        parcela = self.buscar_parcela_por_id(id_parcela)

        if parcela is None:
            return None

        parcela.status = status

        try:
            self.db.commit()

        except IntegrityError:
            self.db.rollback()
            raise
        
        self.db.refresh(parcela)
        return parcela