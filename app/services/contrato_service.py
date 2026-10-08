from app.schemas.contrato import ContratoCreate, ContratoUpdate
from app.repositories.contrato_repository import ContratoRepository
from app.repositories.proposta_repository import PropostaRepository
from datetime import datetime

STATUS_PERMITIDOS = {'rascunho', 'assinado', 'pendente_assinatura', 'cancelado'}

class ContratoService:
    def __init__(self, repository: ContratoRepository, proposta_repository: PropostaRepository):
        self.repository = repository
        self.proposta_repository = proposta_repository

    def criar_contrato(self, dados: ContratoCreate):
        proposta = self.proposta_repository.buscar_proposta_por_id(dados.id_proposta)

        if proposta is None:
            raise ValueError('Proposta não encontrada.')


        contratos_proposta = self.repository.buscar_contratos_por_proposta(dados.id_proposta)

        if contratos_proposta:
            raise ValueError("Já existe contrato vinculado a esta proposta.")
        

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
        return self.repository.listar_contratos()

    def atualizar_contrato(self, id_contrato: int, dados: ContratoUpdate):
        contrato = self.repository.buscar_contrato_por_id(id_contrato)

        if contrato is None:
            raise ValueError('Não foi possível localizar nenhum contrato.')

        return self.repository.atualizar_contrato(id_contrato, dados)

    def atualizar_status_contrato(self, id_contrato: int, status: str):
        contrato = self.repository.buscar_contrato_por_id(id_contrato)

        if contrato is None:
            raise ValueError('Não foi possível localizar nenhum contrato.')

        if status not in STATUS_PERMITIDOS:
            raise ValueError('Status de contrato inválido.')

        return self.repository.atualizar_status_contrato(id_contrato, status)

    def registrar_assinatura(self, id_contrato: int, data_assinatura: datetime):
        contrato = self.repository.buscar_contrato_por_id(id_contrato)

        if contrato is None:
            raise ValueError('Não foi possível localizar nenhum contrato.')

        if contrato.status_contrato != 'pendente_assinatura':
            raise ValueError('Somente contratos pendentes de assinatura podem ser assinados.')
                             
        return self.repository.registrar_assinatura(id_contrato, data_assinatura)