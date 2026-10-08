from app.schemas.documento import DocumentoCreate, DocumentoUpdate
from app.repositories.documento_repository import DocumentoRepository
from app.repositories.evento_repository import EventoRepository
from app.repositories.proposta_repository import PropostaRepository

class DocumentoService:
    def __init__(self, repository: DocumentoRepository, repository_evento: EventoRepository, repository_proposta: PropostaRepository):
        self.repository = repository
        self.repository_evento = repository_evento
        self.repository_proposta = repository_proposta

    def criar_documento(self, dados: DocumentoCreate):
        evento = self.repository_evento.buscar_evento_por_id(dados.id_evento)

        if evento is None:
            raise ValueError('Evento não encontrado.')
        

        if dados.id_proposta is not None:
            proposta = self.repository_proposta.buscar_proposta_por_id(dados.id_proposta)

            if proposta is None:
                raise ValueError('Proposta não encontrada.')

            if proposta.id_evento != dados.id_evento:
                raise ValueError('A proposta não pertence ao evento informado.')


        return self.repository.criar_documento(dados)

    def buscar_documento_por_id(self, id_documento: int):
        documento = self.repository.buscar_documento_por_id(id_documento)

        if documento is None:
            raise ValueError ('Não foi possível localizar nenhum documento.')

        return documento
    

    def buscar_documentos_por_evento(self, id_evento: int):
        return self.repository.buscar_documentos_por_evento(id_evento)
    

    def buscar_documentos_por_tipo(self, tipo: str):
        return self.repository.buscar_documentos_por_tipo(tipo)
    
    
    def documentos_por_evento_e_tipo(self, id_evento: int, tipo: str):
        return self.repository.documentos_por_evento_e_tipo(id_evento, tipo)
    

    def listar_documentos(self):
        return self.repository.listar_documentos()


    def atualizar_documento(self, id_documento: int, dados: DocumentoUpdate):
        documento = self.repository.buscar_documento_por_id(id_documento)

        if documento is None:
            raise ValueError('Não foi possível localizar nenhum documento.')

        id_evento = documento.id_evento
        id_proposta = documento.id_proposta

        if dados.id_evento is not None:
            id_evento = dados.id_evento

        if 'id_proposta' in dados.model_fields_set:
            id_proposta = dados.id_proposta

        evento = self.repository_evento.buscar_evento_por_id(id_evento)

        if evento is None:
            raise ValueError('Evento não encontrado.')

        if id_proposta is not None:
            proposta = self.repository_proposta.buscar_proposta_por_id(id_proposta)

            if proposta is None:
                raise ValueError('Proposta não encontrada.')

            if proposta.id_evento != id_evento:
                raise ValueError('A proposta não pertence ao evento informado.')


        return self.repository.atualizar_documento(id_documento, dados)
    

    def atualizar_dados_drive(self, id_documento: int, drive_file_id: str, drive_url: str):
        documento = self.repository.buscar_documento_por_id(id_documento)

        if documento is None:
            raise ValueError('Não foi possível localizar nenhum documento.')

        return self.repository.atualizar_dados_drive(id_documento, drive_file_id, drive_url)