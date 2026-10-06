from app.schemas.evento import EventoCreate, EventoUpdate
from app.repositories.evento_repository import EventoRepository
from datetime import date

class EventoService:
    def __init__(self, repository: EventoRepository):
        self.repository = repository

    def criar_evento(self, dados: EventoCreate):
        return self.repository.criar_evento(dados)
    
    def buscar_evento_por_id(self, id_evento: int):
        evento = self.repository.buscar_evento_por_id(id_evento)

        if evento is None:
            raise ValueError('Não foi possível localizar nenhum evento.')

        return evento

    def buscar_eventos_por_cliente(self, id_cliente: int):
        eventos = self.repository.buscar_eventos_por_cliente(id_cliente)

        if not eventos:
            raise ValueError('Não foi possível localizar nenhum evento.')

        return eventos

    def buscar_eventos_por_status(self, status: str):
        eventos = self.repository.buscar_eventos_por_status(status)

        if not eventos:
            raise ValueError('Não foi possível localizar nenhum evento.')

        return eventos

    def buscar_eventos_por_data(self, data_evento: date):
        eventos = self.repository.buscar_eventos_por_data(data_evento)

        if not eventos:
            raise ValueError('Não foi possível localizar nenhum evento.')

        return eventos

    def listar_eventos(self):
        return self.repository.listar_eventos()

    def atualizar_evento(self, id_evento: int, dados: EventoUpdate):
        evento = self.repository.buscar_evento_por_id(id_evento)

        if evento is None:
            raise ValueError('Não foi possível localizar nenhum evento.')

        return self.repository.atualizar_evento(id_evento, dados)

    def atualizar_status_evento(self, id_evento: int, status: str):
        evento = self.repository.buscar_evento_por_id(id_evento)

        if evento is None:
            raise ValueError('Não foi possível localizar nenhum evento.')

        return self.repository.atualizar_status_evento(id_evento, status)

    def atualizar_drive_folder_id(self, id_evento: int, drive_folder_id: str):
        evento = self.repository.buscar_evento_por_id(id_evento)

        if evento is None:
            raise ValueError('Não foi possível localizar nenhum evento.')

        return self.repository.atualizar_drive_folder_id(id_evento, drive_folder_id)