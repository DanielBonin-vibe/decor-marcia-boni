from app.schemas.documento import DocumentoCreate, DocumentoUpdate
from app.repositories.documento_repository import DocumentoRepository

class DocumentoService:
    def __init__(self, repository: DocumentoRepository):
        self.repository = repository

    def criar_docuemnto(self, dados: DocumentoCreate):