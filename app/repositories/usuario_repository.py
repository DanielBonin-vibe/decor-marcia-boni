from sqlalchemy import select
from sqlalchemy.orm import Session

from app.schemas import UsuarioCreate, UsuarioUpdate 
from app.models import Usuario

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar_usuario(self, dados: UsuarioCreate, senha_hash: str):
        dados_usuario = dados.model_dump(exclude={'senha'})

        usuario = Usuario(**dados_usuario, senha_hash=senha_hash, ativo = True)

        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)

        return usuario

    def buscar_usuario_por_id(self, id_usuario: int):
        consulta = select(Usuario).where(Usuario.id_usuario == id_usuario)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def buscar_usuario_por_email(self, email: str):
        consulta = select(Usuario).where(Usuario.email == email)

        resultado = self.db.execute(consulta)

        return resultado.scalar_one_or_none()

    def listar_usuarios(self):
        consulta = select(Usuario)

        resultado = self.db.execute(consulta)

        return resultado.scalars().all()

    def atualizar_usuario(self, id_usuario: int, dados: UsuarioUpdate):
        usuario = self.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            return None

        atualizacao_usuario = dados.model_dump(exclude_unset=True, exclude={'senha'})

        for campo, valor in atualizacao_usuario.items():
            setattr(usuario, campo, valor)

        self.db.commit()
        self.db.refresh(usuario)

        return usuario

    def atualizar_senha(self, id_usuario: int, senha_hash: str):
        usuario = self.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            return None

        usuario.senha_hash = senha_hash

        self.db.commit()
        self.db.refresh(usuario)

        return usuario

    def atualizar_perfil(self, id_usuario: int, perfil: str):
        usuario = self.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            return None

        usuario.perfil = perfil

        self.db.commit()
        self.db.refresh(usuario)

        return usuario

    def desativar_usuario(self, id_usuario: int):
        usuario = self.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            return None

        usuario.ativo = False

        self.db.commit()
        self.db.refresh(usuario)

        return usuario

    def reativar_usuario(self, id_usuario: int):
        usuario = self.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            return None

        usuario.ativo = True

        self.db.commit()
        self.db.refresh(usuario)

        return usuario