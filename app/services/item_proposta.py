from app.schemas.item_proposta import ItemPropostaCreate, ItemPropostaUpdate
from app.repositories.item_proposta_repository import ItemPropostaRepository

class ItemPropostaService:
    def __init__(self, repository: ItemPropostaRepository):
        self.repository = repository 

    def criar_item_proposta(self, dados: ItemPropostaCreate):
        return self.repository.criar_item_proposta(dados)

    def buscar_item_por_id(self, id_item_proposta: int):
        item_proposta = self.repository.buscar_item_por_id(id_item_proposta)

        if item_proposta is None:
            raise ValueError('Não foi possível localizar nenhum item da proposta.')

        return item_proposta

    def buscar_itens_por_proposta(self, id_proposta: int):
        itens_proposta = self.repository.buscar_itens_por_proposta(id_proposta)

        if not itens_proposta:
            raise ValueError('Não foi possível localizar nenhum item da proposta.')

        return itens_proposta

    def buscar_itens_por_categoria(self, categoria: str):
        itens_proposta = self.repository.buscar_itens_por_categoria(categoria)

        if not itens_proposta:
            raise ValueError('Não foi possível localizar nenhum item da proposta.')

        return itens_proposta

    def listar_itens(self):
        return self.repository.listar_itens()

    def atualizar_item(self, id_item_proposta: int, dados: ItemPropostaUpdate):
        item_proposta = self.repository.buscar_item_por_id(id_item_proposta)
        
        if item_proposta is None:
            raise ValueError('Não foi possível localizar nenhum item da proposta.')

        return self.repository.atualizar_item(id_item_proposta, dados)

    def atualizar_ordem(self, id_item_proposta: int, ordem: int):
        item_proposta = self.repository.buscar_item_por_id(id_item_proposta)
        
        if item_proposta is None:
            raise ValueError('Não foi possível localizar nenhum item da proposta.')

        return self.repository.atualizar_ordem(id_item_proposta, ordem)

    def atualizar_opcional(self, id_item_proposta: int, opcional: bool):
        item_proposta = self.repository.buscar_item_por_id(id_item_proposta)
        
        if item_proposta is None:
            raise ValueError('Não foi possível localizar nenhum item da proposta.')

        return self.repository.atualizar_opcional(id_item_proposta, opcional)