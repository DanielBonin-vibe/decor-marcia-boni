from sqlalchemy import select
from sqlalchemy.orm import Session
from app.schemas.cliente import ClienteCreate, ClienteUpdate
from app.models import Cliente

class ClienteRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar_cliente(self, dados: ClienteCreate):
        cliente = Cliente(**dados.model_dump())

        self.db.add(cliente)
        self.db.commit()
        self.db.refresh(cliente)

        return cliente

    def buscar_cliente_por_id(self, id_cliente: int):
        consulta = select(Cliente).where(Cliente.id_cliente == id_cliente)
        
        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def buscar_cliente_por_cpf(self, cpf: str):
        consulta = select(Cliente).where(Cliente.cpf == cpf)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def buscar_cliente_por_email(self, email: str):
        consulta = select(Cliente).where(Cliente.email == email)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def buscar_cliente_por_telefone(self, telefone: str):
        consulta = select(Cliente).where(Cliente.telefone == telefone)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def listar_clientes(self):
        consulta = select(Cliente)

        resultado = self.db.execute(consulta)
        
        return resultado.scalars().all()

    def atualizar_cliente(self, cpf: str, dados: ClienteUpdate):
        cliente = self.buscar_cliente_por_cpf(cpf)

        if cliente is None:
            return None

        dados_atualizacao = dados.model_dump(exclude_unset=True)

        for campo, valor in dados_atualizacao.items():
            setattr(cliente, campo, valor)

        self.db.commit()
        self.db.refresh(cliente)

        return cliente

    def desativar_cliente(self, cpf: str):
        cliente = self.buscar_cliente_por_cpf(cpf)

        if cliente is None:
            return None

        cliente.ativo = False

        self.db.commit()
        self.db.refresh(cliente)

        return cliente

    def reativar_cliente(self, cpf: str):
        cliente = self.buscar_cliente_por_cpf(cpf)

        if cliente is None:
            return None

        cliente.ativo = True

        self.db.commit()
        self.db.refresh(cliente)

        return cliente