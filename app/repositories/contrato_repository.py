from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy.exc import IntegrityError

from app.schemas.contrato import ContratoCreate, ContratoUpdate
from app.models import Contrato, Proposta

class ContratoRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar_contrato(self, dados: ContratoCreate):
        contrato = Contrato(**dados.model_dump())

        self.db.add(contrato)

        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise

        self.db.refresh(contrato)
        return contrato

    def buscar_contrato_por_id(self, id_contrato: int):
        consulta = select(Contrato).where(Contrato.id_contrato == id_contrato)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def buscar_contrato_por_numero(self, numero: str):
        consulta = select(Contrato).join(Contrato.numero == numero)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def buscar_contratos_por_evento(self, id_evento: int):
        consulta = select(Contrato).join(Proposta,Contrato.id_proposta == Proposta.id_proposta).where(Proposta.id_evento == id_evento)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def buscar_contratos_por_proposta(self, id_proposta: int):
        consulta = select(Contrato).where(Contrato.id_proposta == id_proposta)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def listar_contratos(self):
        consulta = select(Contrato)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def atualizar_contrato(self, id_contrato: int, dados: ContratoUpdate):
        contrato = self.buscar_contrato_por_id(id_contrato)

        if contrato is None:
            return None

        dados_atualizacao = dados.model_dump(exclude_unset=True)

        for campo, valor in dados_atualizacao.items():
            setattr(contrato, campo, valor)

        self.db.commit()
        self.db.refresh(contrato)

        return contrato

    def atualizar_status_contrato(self, id_contrato: int, status: str):
        contrato = self.buscar_contrato_por_id(id_contrato)

        if contrato is None:
            return None

        contrato.status_contrato = status

        self.db.commit()
        self.db.refresh(contrato)

        return contrato

    def registrar_assinatura(self, id_contrato: int, data_assinatura: datetime):
        contrato = self.buscar_contrato_por_id(id_contrato)

        if contrato is None:
            return None

        contrato.data_assinatura = data_assinatura 
        contrato.status_contrato = 'assinado'

        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise
        
        self.db.refresh(contrato)
        return contrato