from sqlalchemy import select
from sqlalchemy.orm import Session

from app.schemas.item_proposta import ItemPropostaCreate, ItemPropostaUpdate
from app.models import ItemProposta

class ItemPropostaRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar_item_proposta(self, dados: ItemPropostaCreate):
        item_proposta = ItemProposta(**dados.model_dump())

        self.db.add(item_proposta)
        self.db.commit()
        self.db.refresh(item_proposta)

        return item_proposta

    def buscar_item_por_id(self, id_item_proposta: int):
        consulta = select(ItemProposta).where(ItemProposta.id_item_proposta == id_item_proposta)

        resultado = self.db.execute(consulta)
        
        return resultado.scalar_one_or_none()


    def buscar_itens_por_proposta(self, id_proposta: int):
        consulta = select(ItemProposta).where(ItemProposta.id_proposta == id_proposta)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def buscar_itens_por_categoria(self, categoria: str):
        consulta = select(ItemProposta).where(ItemProposta.categoria == categoria)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def listar_itens(self):
        consulta = select(ItemProposta)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()   

    def atualizar_item(self, id_item_proposta: int, dados: ItemPropostaUpdate):
        item_proposta = self.buscar_item_por_id(id_item_proposta)

        if item_proposta is None:
            return None

        atualizacao_item_proposta = dados.model_dump(exclude_unset=True)

        for campo, valor in atualizacao_item_proposta.items():
            setattr(item_proposta, campo, valor)

        self.db.commit()
        self.db.refresh(item_proposta)

        return item_proposta

    def atualizar_ordem(self, id_item_proposta: int, ordem: int):
        item_proposta = self.buscar_item_por_id(id_item_proposta)

        if item_proposta is None:
            return None

        item_proposta.ordem = ordem

        self.db.commit()
        self.db.refresh(item_proposta)

        return item_proposta

    def atualizar_opcional(self, id_item_proposta: int, opcional: bool):
        item_proposta = self.buscar_item_por_id(id_item_proposta)

        if item_proposta is None:
            return None

        item_proposta.opcional = opcional

        self.db.commit()
        self.db.refresh(item_proposta)

        return item_proposta