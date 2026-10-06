from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import date

from app.schemas.evento import EventoCreate, EventoUpdate
from app.models import Evento

class EventoRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar_evento(self, dados: EventoCreate):
        evento = Evento(**dados.model_dump())

        self.db.add(evento)
        self.db.commit()
        self.db.refresh(evento)

        return evento

    def buscar_evento_por_id(self, id_evento: int):
        consulta = select(Evento).where(Evento.id_evento == id_evento)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def buscar_eventos_por_cliente(self, id_cliente: int):
        consulta = select(Evento).where(Evento.id_cliente == id_cliente)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def buscar_eventos_por_status(self, status: str):
        consulta = select(Evento).where(Evento.status == status)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def buscar_eventos_por_data(self, data_evento: date):
        consulta = select(Evento).where(Evento.data_evento == data_evento)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def listar_eventos(self):
        consulta = select(Evento)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def atualizar_evento(self, id_evento: int, dados: EventoUpdate):
        evento = self.buscar_evento_por_id(id_evento)

        if evento is None:
            return None

        atualizacao_evento = dados.model_dump(exclude_unset=True)

        for campo, valor in atualizacao_evento.items():
            setattr(evento, campo, valor)

        self.db.commit()
        self.db.refresh(evento)

        return evento

    def atualizar_status_evento(self, id_evento: int, status: str):
        evento = self.buscar_evento_por_status(id_evento)

        if evento is None:
            return None

        evento.status = status

        self.db.commit()
        self.db.refresh(evento)

        return evento

    def atualizar_drive_folder_id(self, id_evento: int, drive_folder_id: str):
        evento = self.buscar_evento_por_id(id_evento)

        if evento is None:
            return None

        evento.drive_folder_id = drive_folder_id

        self.db.commit()
        self.db.refresh(evento)

        return evento