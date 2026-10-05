from app.schemas.contrato import ContratoCreate, ContratoUpdate
from app.repositories.contrato_repository import ContratoRepository
from datetime import datetime

class ContratoService:
    def __init__(self, repository: ContratoRepository):
        self.repository = repository

    def criar_contrato(self, dados: ContratoCreate):
        contrato_evento = self.repository.buscar_contratos_por_evento(dados.id_evento)

        if contrato_evento:
            raise ValueError('Já existe contrato vinculado a este evento.')


        contrato_proposta = self.repository.buscar_contratos_por_proposta(dados.id_proposta)

        if contrato_proposta:
            raise ValueError ('Já existe contrato vinculado a esta proposta.')

        contrato_numero = self.repository.buscar_contrato_por_numero(dados.numero)

        if contrato_numero is not None:
            raise ValueError ('Número de contrato já cadastrado.')


        return self.repository.criar_contrato(dados)

    def buscar_contrato_por_id(self, id_contrato: int):
        contrato = self.repository.buscar_contrato_por_id(id_contrato)

        if contrato is None:
            raise ValueError('Não foi possível localizar nenhum contrato.')

        return contrato

    def buscar_contrato_por_numero(self, numero: str):
        contrato = self.repository.buscar_contrato_por_numero(numero)

        if contrato is None:
            raise ValueError('Não foi possível localizar nenhum contrato.')

        return contrato

    def buscar_contratos_por_evento(self, id_evento: int):
        contratos = self.repository.buscar_contratos_por_evento(id_evento)

        if not contratos:
            raise ValueError('Não foi possível localizar nenhum contrato.')

        return contratos

    def buscar_contratos_por_proposta(self, id_proposta: int):
        contratos = self.repository.buscar_contratos_por_proposta(id_proposta)

        if not contratos:
            raise ValueError('Não foi possível localizar nenhum contrato.')

        return contratos

    def listar_contratos(self):
        contratos = self.repository.listar_contratos()

        if not contratos:
            raise ValueError('Não foi possível localizar nenhum contrato.')

        return contratos

    def atualizar_contrato(self, id_contrato: int, dados: ContratoUpdate):
        contrato = self.repository.buscar_contrato_por_id(id_contrato)

        if contrato is None:
            raise ValueError('Não foi possível localizar nenhum contrato.')

        return self.repository.atualizar_contrato(id_contrato, dados)

    def atualizar_status_contrato(self, id_contrato: int, status: str):
        contrato = self.repository.buscar_contrato_por_id(id_contrato)

        if contrato is None:
            raise ValueError('Não foi possível localizar nenhum contrato.')

        return self.repository.atualizar_status_contrato(id_contrato, status)

    def registrar_assinatura(self, id_contrato: int, data_assinatura: datetime):
        contrato = self.repository.buscar_contrato_por_id(id_contrato)

        if contrato is None:
            raise ValueError('Não foi possível localizar nenhum contrato.')

        return self.repository.registrar_assinatura(id_contrato, data_assinatura)