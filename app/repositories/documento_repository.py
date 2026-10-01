from sqlalchemy import select
from sqlalchemy.orm import Session

from app.schemas.documento import DocumentoCreate, DocumentoUpdate
from app.models import Documento

class DocumentoRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar_documento(self, dados: DocumentoCreate):
        documento = Documento(**dados.model_dump())

        self.db.add(documento)
        self.db.commit()
        self.db.refresh(documento)

        return documento

    def buscar_documento_por_id(self, id_documento: int):
        consulta = select(Documento).where(Documento.id_documento == id_documento)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def buscar_documentos_por_evento(self, id_evento: int):
        consulta = select(Documento).where(Documento.id_evento == id_evento)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def buscar_documentos_por_tipo(self, tipo: str):
        consulta = select(Documento).where(Documento.tipo == tipo)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def documentos_por_evento_e_tipo(self, id_evento: int, tipo: str):
        consulta = select(Documento).where(Documento.id_evento == id_evento, Documento.tipo == tipo)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def listar_documentos(self):
        consulta = select(Documento)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def atualizar_documento(self, id_documento: int, dados: DocumentoUpdate):
        documento = self.buscar_documento_por_id(id_documento)

        if documento is None:
            return None

        atualizacao_documento = dados.model_dump(exclude_unset=True)

        for campo, valor in atualizacao_documento.items():
            setattr(documento, campo, valor)

        self.db.commit()
        self.db.refresh(documento)

        return documento

    def atualizar_dados_drive(self, id_documento: int, drive_file_id: str, drive_url: str):
        documento = self.buscar_documento_por_id(id_documento)

        if documento is None:
            return None

        documento.drive_file_id = drive_file_id
        documento.drive_url = drive_url

        self.db.commit()
        self.db.refresh(documento)

        return documento
