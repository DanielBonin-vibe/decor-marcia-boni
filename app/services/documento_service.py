from app.schemas.documento import DocumentoCreate, DocumentoUpdate
from app.repositories.documento_repository import DocumentoRepository

class DocumentoService:
    def __init__(self, repository: DocumentoRepository):
        self.repository = repository

    def criar_documento(self, dados: DocumentoCreate):
        return self.repository.criar_documento(dados)

    def buscar_documento_por_id(self, id_documento: int):
        documento = self.repository.buscar_documento_por_id(id_documento)

        if documento is None:
            raise ValueError ('Não foi possível localizar nenhum documento.')

        return documento

    def buscar_documentos_por_evento(self, id_evento: int):
        documentos = self.repository.buscar_documentos_por_evento(id_evento)

        if not documentos:
            raise ValueError ('Não foi possível localizar nenhum documento.')

        return documentos

    def buscar_documentos_por_tipo(self, tipo: str):
        documentos = self.repository.buscar_documentos_por_tipo(tipo)

        if not documentos:
            raise ValueError ('Não foi possível localizar nenhum documento.')

        return documentos

    def documentos_por_evento_e_tipo(self, id_evento: int, tipo: str):
        documentos = self.repository.documentos_por_evento_e_tipo(id_evento, tipo)

        if not documentos:
            raise ValueError ('Não foi possível localizar nenhum documento.')

        return documentos

    def listar_documentos(self):
        return self.repository.listar_documentos()

    def atualizar_documento(self, id_documento: int, dados: DocumentoUpdate):
        documento = self.repository.buscar_documento_por_id(id_documento)

        if documento is None:
            raise ValueError('Não foi possível localizar nenhum documento.')

        return self.repository.atualizar_documento(id_documento, dados)

    def atualizar_dados_drive(self, id_documento: int, drive_file_id: str, drive_url: str):
        documento = self.repository.buscar_documento_por_id(id_documento)

        if documento is None:
            raise ValueError('Não foi possível localizar nenhum documento.')

        return self.repository.atualizar_dados_drive(id_documento, drive_file_id, drive_url)