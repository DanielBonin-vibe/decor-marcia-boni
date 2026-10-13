from app.schemas.evento import EventoCreate, EventoUpdate
from app.repositories.evento_repository import EventoRepository
from app.repositories.cliente_repository import ClienteRepository
from datetime import date

class EventoService:
    def __init__(self, repository: EventoRepository, cliente_repository : ClienteRepository):
        self.repository = repository
        self.cliente_repository = cliente_repository

    def criar_evento(self, dados: EventoCreate):
        cliente = self.cliente_repository.buscar_cliente_por_id(dados.id_cliente)

        if cliente is None:
            raise ValueError('Não foi possível localizar o cliente.')
        
        return self.repository.criar_evento(dados)
    
    def buscar_evento_por_id(self, id_evento: int):
        evento = self.repository.buscar_evento_por_id(id_evento)

        if evento is None:
            raise ValueError('Não foi possível localizar nenhum evento.')

        return evento

    def buscar_eventos_por_cliente(self, id_cliente: int):
        eventos = self.repository.buscar_eventos_por_cliente(id_cliente)

        if not eventos:
            return []

        return eventos

    def buscar_eventos_por_status(self, status: str):
        eventos = self.repository.buscar_eventos_por_status(status)

        if not eventos:
            return []

        return eventos

    def buscar_eventos_por_data(self, data_evento: date):
        eventos = self.repository.buscar_eventos_por_data(data_evento)

        if not eventos:
            return []

        return eventos

    def listar_eventos(self):
        return self.repository.listar_eventos()

    def atualizar_evento(self, id_evento: int, dados: EventoUpdate):
        evento = self.repository.buscar_evento_por_id(id_evento)

        if evento is None:
            raise ValueError('Não foi possível localizar nenhum evento.')

        if dados.id_cliente is not None:
            cliente = self.cliente_repository.buscar_cliente_por_id(dados.id_cliente)

            if cliente is None:
                raise ValueError('Não foi possível localizar o cliente.')
        
        return self.repository.atualizar_evento(id_evento, dados)

    def atualizar_status_evento(self, id_evento: int, status: str):
        evento = self.repository.buscar_evento_por_id(id_evento)

        if evento is None:
            raise ValueError('Não foi possível localizar nenhum evento.')

        status_evento = evento.status

        transicoes_permitidas = {'planejamento': ['confirmado', 'cancelado'], 'confirmado': ['realizado', 'cancelado'], 
            'realizado': [], 'cancelado': []     
        }

        if status_evento not in transicoes_permitidas:
            raise ValueError('O evento possui um status inválido.')

        if status not in transicoes_permitidas[status_evento]:
            raise ValueError(f'Não é permitido alterar o status de {status_evento} para {status}.')
        

        return self.repository.atualizar_status_evento(id_evento, status)

    def atualizar_drive_folder_id(self, id_evento: int, drive_folder_id: str):
        evento = self.repository.buscar_evento_por_id(id_evento)

        if evento is None:
            raise ValueError('Não foi possível localizar nenhum evento.')

        return self.repository.atualizar_drive_folder_id(id_evento, drive_folder_id)