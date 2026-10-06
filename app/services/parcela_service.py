from app.schemas.parcela import ParcelaCreate, ParcelaUpdate
from app.repositories.parcela_repository import ParcelaRepository
from datetime import date


class ParcelaService:
    def __init__(self, repository: ParcelaRepository):
        self.repository = repository

    def criar_parcela(self, dados: ParcelaCreate):
        if dados.valor <= 0:
            raise ValueError('O valor da parcela deve ser maior que zero.')

        return self.repository.criar_parcela(dados)

    def buscar_parcela_por_id(self, id_parcela: int):
        parcela = self.repository.buscar_parcela_por_id(id_parcela)

        if parcela is None:
            raise ValueError ('Não foi possível localizar nenhuma parcela.')

        return parcela

    def buscar_parcelas_por_contrato(self, id_contrato: int):
        parcelas = self.repository.buscar_parcelas_por_contrato(id_contrato)

        if not parcelas:
            raise ValueError ('Não foi possível localizar nenhuma parcela.')

        return parcelas

    def buscar_parcelas_por_status(self, status: str):
        parcelas = self.repository.buscar_parcelas_por_status(status)

        if not parcelas:
            raise ValueError ('Não foi possível localizar nenhuma parcela.')

        return parcelas

    def buscar_parcelas_por_vencimento(self, data_vencimento: date):
        parcelas = self.repository.buscar_parcelas_por_vencimento(data_vencimento)

        if not parcelas:
            raise ValueError ('Não foi possível localizar nenhuma parcela.')

        return parcelas

    def listar_parcelas(self):
        return self.repository.listar_parcelas()

    def atualizar_parcela(self, id_parcela: int, dados: ParcelaUpdate):
        parcela = self.repository.buscar_parcela_por_id(id_parcela)

        if parcela is None:
            raise ValueError ('Não foi possível localizar nenhuma parcela.')

        return self.repository.atualizar_parcela(id_parcela, dados)

    def atualizar_status_parcela(self, id_parcela: int, status: str):
        parcela = self.repository.buscar_parcela_por_id(id_parcela)

        if parcela is None:
            raise ValueError ('Não foi possível localizar nenhuma parcela.')

        return self.repository.atualizar_status_parcela(id_parcela, status)