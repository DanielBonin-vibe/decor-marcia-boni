from sqlalchemy import select
from sqlalchemy.orm import Session

from app.schemas import PropostaCreate, PropostaUpdate 
from app.models import Proposta

class PropostaRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar_proposta(self, dados: PropostaCreate):
        proposta = Proposta(**dados.model_dump())

        self.db.add(proposta)
        self.db.commit()
        self.db.refresh(proposta)

        return proposta

    def buscar_proposta_por_id(self, id_proposta: int):
        consulta = select(Proposta).where(Proposta.id_proposta == id_proposta)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def buscar_propostas_por_evento(self, id_evento: int):
        consulta = select(Proposta).where(Proposta.id_evento == id_evento)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def buscar_propostas_por_status(self, status: str):
        consulta = select(Proposta).where(Proposta.status == status)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def buscar_proposta_por_evento_e_versao(self, id_evento: int, versao: int):
        consulta = select(Proposta).where(Proposta.id_evento == id_evento, Proposta.versao == versao)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def listar_propostas(self):
        consulta = select(Proposta)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def atualizar_proposta(self, id_proposta: int, dados: PropostaUpdate):
        proposta = self.buscar_proposta_por_id(id_proposta)

        if proposta is None:
            return None

        atualizacao_proposta = dados.model_dump(exclude_unset=True)

        for campo, valor in atualizacao_proposta.items():
            setattr(proposta, campo, valor)

        self.db.commit()
        self.db.refresh(proposta)

        return proposta

    def atualizar_status_proposta(self, id_proposta: int, status: str):
        proposta = self.buscar_proposta_por_id(id_proposta)

        if proposta is None:
            return None

        proposta.status = status

        self.db.commit()
        self.db.refresh(proposta)

        return proposta